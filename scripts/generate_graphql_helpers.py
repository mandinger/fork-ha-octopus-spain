#!/usr/bin/env python3
"""Generate typed GraphQL helper classes and request builders.

This script is intentionally additive: it only writes generated helper files and
never modifies runtime integration code.
"""

from __future__ import annotations

import argparse
import json
import keyword
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_INTROSPECTION = Path("docs/InstrospectionQuery.json")
DEFAULT_OPERATIONS_DIR = Path("graphql/operations")
DEFAULT_OUTPUT = Path("custom_components/octopus_spain/lib/graphql_helpers/generated.py")

SCALAR_MAP = {
    "String": "str",
    "ID": "str",
    "Int": "int",
    "Float": "float",
    "Boolean": "bool",
    "Date": "str",
    "DateTime": "str",
    "Decimal": "float",
    "JSONString": "dict[str, Any]",
    "UUID": "str",
}


@dataclass(frozen=True)
class GqlTypeNode:
    kind: str  # NAMED or LIST
    name: str | None = None
    of_type: "GqlTypeNode | None" = None
    non_null: bool = False


@dataclass(frozen=True)
class OperationVariable:
    name: str
    gql_type: GqlTypeNode


@dataclass(frozen=True)
class OperationSpec:
    kind: str
    name: str
    source_path: Path
    query_text: str
    variables: list[OperationVariable]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate typed GraphQL helper classes and request builders."
    )
    parser.add_argument(
        "--introspection",
        type=Path,
        default=DEFAULT_INTROSPECTION,
        help=f"Path to introspection JSON. Default: {DEFAULT_INTROSPECTION}",
    )
    parser.add_argument(
        "--operations-dir",
        type=Path,
        default=DEFAULT_OPERATIONS_DIR,
        help=f"Directory containing .graphql operation files. Default: {DEFAULT_OPERATIONS_DIR}",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Generated python file path. Default: {DEFAULT_OUTPUT}",
    )
    return parser.parse_args()


def read_schema(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    schema = payload.get("data", {}).get("__schema")
    if not isinstance(schema, dict):
        raise ValueError("Invalid introspection payload: missing data.__schema")
    if not isinstance(schema.get("types"), list):
        raise ValueError("Invalid introspection payload: __schema.types is not a list")
    return schema


def parse_operations(operations_dir: Path) -> list[OperationSpec]:
    if not operations_dir.exists():
        raise FileNotFoundError(f"Operations dir not found: {operations_dir}")

    specs: list[OperationSpec] = []
    pattern = re.compile(
        r"^\s*(query|mutation|subscription)\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\((.*?)\))?",
        re.DOTALL,
    )

    for path in sorted(operations_dir.glob("*.graphql")):
        text = path.read_text(encoding="utf-8").strip()
        match = pattern.search(text)
        if not match:
            raise ValueError(f"Unable to parse operation declaration in {path}")

        kind = match.group(1)
        name = match.group(2)
        raw_vars = (match.group(4) or "").strip()
        variables = parse_operation_variables(raw_vars)

        specs.append(
            OperationSpec(
                kind=kind,
                name=name,
                source_path=path,
                query_text=text,
                variables=variables,
            )
        )

    if not specs:
        raise ValueError(f"No .graphql files found under {operations_dir}")
    return specs


def parse_operation_variables(raw: str) -> list[OperationVariable]:
    if not raw:
        return []

    chunks: list[str] = []
    current: list[str] = []
    depth = 0
    for ch in raw:
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1

        if ch == "," and depth == 0:
            chunk = "".join(current).strip()
            if chunk:
                chunks.append(chunk)
            current = []
            continue
        current.append(ch)

    tail = "".join(current).strip()
    if tail:
        chunks.append(tail)

    variables: list[OperationVariable] = []
    line_splitter = re.compile(r"\s+(?=\$)")
    exploded: list[str] = []
    for chunk in chunks:
        parts = [part.strip() for part in line_splitter.split(chunk) if part.strip()]
        exploded.extend(parts)

    item_pattern = re.compile(r"^\$([A-Za-z_][A-Za-z0-9_]*)\s*:\s*([^=]+?)(?:\s*=\s*.+)?$")
    for item in exploded:
        match = item_pattern.match(item)
        if not match:
            raise ValueError(f"Unable to parse variable declaration: {item!r}")
        name = match.group(1)
        gql_type = parse_gql_type(match.group(2).strip())
        variables.append(OperationVariable(name=name, gql_type=gql_type))

    return variables


def parse_gql_type(type_str: str) -> GqlTypeNode:
    index = 0

    def parse_node() -> GqlTypeNode:
        nonlocal index
        if index >= len(type_str):
            raise ValueError(f"Unexpected end parsing GraphQL type: {type_str!r}")

        if type_str[index] == "[":
            index += 1
            inner = parse_node()
            if index >= len(type_str) or type_str[index] != "]":
                raise ValueError(f"Missing closing bracket in GraphQL type: {type_str!r}")
            index += 1
            node = GqlTypeNode(kind="LIST", of_type=inner)
        else:
            start = index
            while index < len(type_str) and (type_str[index].isalnum() or type_str[index] == "_"):
                index += 1
            if start == index:
                raise ValueError(f"Expected named GraphQL type in: {type_str!r}")
            node = GqlTypeNode(kind="NAMED", name=type_str[start:index])

        if index < len(type_str) and type_str[index] == "!":
            index += 1
            node = GqlTypeNode(kind=node.kind, name=node.name, of_type=node.of_type, non_null=True)
        return node

    compact = "".join(type_str.split())
    type_str = compact
    node = parse_node()
    if index != len(type_str):
        raise ValueError(f"Unexpected trailing content in GraphQL type: {type_str!r}")
    return node


def introspection_type_to_node(type_ref: dict[str, Any] | None) -> GqlTypeNode:
    if not type_ref:
        return GqlTypeNode(kind="NAMED", name="String")
    kind = type_ref.get("kind")
    name = type_ref.get("name")
    of_type = type_ref.get("ofType")

    if kind == "NON_NULL":
        inner = introspection_type_to_node(of_type)
        return GqlTypeNode(kind=inner.kind, name=inner.name, of_type=inner.of_type, non_null=True)
    if kind == "LIST":
        return GqlTypeNode(kind="LIST", of_type=introspection_type_to_node(of_type), non_null=False)
    if name:
        return GqlTypeNode(kind="NAMED", name=name, non_null=False)
    return GqlTypeNode(kind="NAMED", name="String", non_null=False)


def named_types_in_node(node: GqlTypeNode) -> set[str]:
    if node.kind == "NAMED":
        return {node.name} if node.name else set()
    if node.of_type is None:
        return set()
    return named_types_in_node(node.of_type)


def sanitize_identifier(value: str) -> str:
    out = re.sub(r"[^0-9A-Za-z_]", "_", value)
    if not out:
        out = "field"
    if out[0].isdigit():
        out = f"_{out}"
    if keyword.iskeyword(out):
        out = f"{out}_"
    return out


def pascal_case(value: str) -> str:
    parts = re.findall(r"[A-Za-z0-9]+", value)
    if not parts:
        return "Generated"
    return "".join(p[:1].upper() + p[1:] for p in parts)


def snake_case(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    return value.strip("_").lower() or "generated"


def input_class_name(graphql_input_name: str) -> str:
    if graphql_input_name.endswith("Input"):
        return graphql_input_name
    return f"{graphql_input_name}Input"


def node_to_python_type(
    node: GqlTypeNode,
    *,
    known_inputs: set[str],
    known_enums: set[str],
) -> str:
    if node.kind == "LIST":
        assert node.of_type is not None
        inner = node_to_python_type(node.of_type, known_inputs=known_inputs, known_enums=known_enums)
        base = f"list[{inner}]"
    else:
        assert node.name is not None
        if node.name in known_inputs:
            base = input_class_name(node.name)
        elif node.name in known_enums:
            base = node.name
        else:
            base = SCALAR_MAP.get(node.name, "Any")

    if node.non_null:
        return base
    return f"{base} | None"


def collect_needed_input_and_enum_types(
    schema_types: dict[str, dict[str, Any]],
    operations: list[OperationSpec],
) -> tuple[list[str], list[str]]:
    pending_inputs: list[str] = []
    seen_inputs: set[str] = set()
    seen_enums: set[str] = set()

    for op in operations:
        for variable in op.variables:
            for name in named_types_in_node(variable.gql_type):
                spec = schema_types.get(name)
                if not spec:
                    continue
                kind = spec.get("kind")
                if kind == "INPUT_OBJECT" and name not in seen_inputs:
                    seen_inputs.add(name)
                    pending_inputs.append(name)
                elif kind == "ENUM":
                    seen_enums.add(name)

    index = 0
    while index < len(pending_inputs):
        input_name = pending_inputs[index]
        index += 1
        input_spec = schema_types.get(input_name) or {}
        for field in input_spec.get("inputFields") or []:
            node = introspection_type_to_node(field.get("type"))
            for name in named_types_in_node(node):
                spec = schema_types.get(name)
                if not spec:
                    continue
                kind = spec.get("kind")
                if kind == "INPUT_OBJECT" and name not in seen_inputs:
                    seen_inputs.add(name)
                    pending_inputs.append(name)
                elif kind == "ENUM":
                    seen_enums.add(name)

    return sorted(seen_inputs), sorted(seen_enums)


def render_enum_aliases(enum_names: list[str], schema_types: dict[str, dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for enum_name in enum_names:
        enum_spec = schema_types.get(enum_name) or {}
        values = [v.get("name") for v in enum_spec.get("enumValues") or [] if v.get("name")]
        if values:
            literal_values = ", ".join(f'"{v}"' for v in values)
            lines.append(f"{enum_name} = Literal[{literal_values}]")
        else:
            lines.append(f"{enum_name} = str")
    return lines


def render_input_dataclasses(
    input_names: list[str],
    enum_names: set[str],
    schema_types: dict[str, dict[str, Any]],
) -> list[str]:
    lines: list[str] = []
    known_inputs = set(input_names)

    for input_name in input_names:
        input_spec = schema_types.get(input_name) or {}
        fields = input_spec.get("inputFields") or []
        lines.append("@dataclass(slots=True)")
        lines.append(f"class {input_class_name(input_name)}:")
        if not fields:
            lines.append("    pass")
            lines.append("")
            continue

        mappings: list[tuple[str, str, bool]] = []
        for field in fields:
            graphql_name = field.get("name")
            if not graphql_name:
                continue
            node = introspection_type_to_node(field.get("type"))
            py_name = sanitize_identifier(graphql_name)
            py_type = node_to_python_type(node, known_inputs=known_inputs, known_enums=enum_names)
            required = node.non_null
            mappings.append((graphql_name, py_name, required))
            if required:
                lines.append(f"    {py_name}: {py_type}")
            else:
                lines.append(f"    {py_name}: {py_type} = None")

        lines.append("")
        lines.append("    def to_dict(self) -> dict[str, Any]:")
        lines.append("        out: dict[str, Any] = {}")
        for graphql_name, py_name, required in mappings:
            if required:
                lines.append(f"        out[{graphql_name!r}] = _serialize_input(self.{py_name})")
            else:
                lines.append(f"        if self.{py_name} is not None:")
                lines.append(f"            out[{graphql_name!r}] = _serialize_input(self.{py_name})")
        lines.append("        return out")
        lines.append("")

    return lines


def render_operation_helpers(
    operations: list[OperationSpec],
    input_names: set[str],
    enum_names: set[str],
) -> list[str]:
    lines: list[str] = []

    for op in operations:
        lines.append(f"{op.name}_QUERY = '''{op.query_text}'''")
        lines.append("")

        class_name = f"{pascal_case(op.name)}Variables"
        lines.append("@dataclass(slots=True)")
        lines.append(f"class {class_name}:")
        if not op.variables:
            lines.append("    pass")
            lines.append("")
            lines.append("    def to_dict(self) -> dict[str, Any]:")
            lines.append("        return {}")
            lines.append("")
        else:
            rendered_vars: list[tuple[str, str, bool]] = []
            for var in op.variables:
                py_name = sanitize_identifier(var.name)
                py_type = node_to_python_type(var.gql_type, known_inputs=input_names, known_enums=enum_names)
                required = var.gql_type.non_null
                rendered_vars.append((var.name, py_name, required))
                if required:
                    lines.append(f"    {py_name}: {py_type}")
                else:
                    lines.append(f"    {py_name}: {py_type} = None")
            lines.append("")
            lines.append("    def to_dict(self) -> dict[str, Any]:")
            lines.append("        out: dict[str, Any] = {}")
            for graphql_name, py_name, required in rendered_vars:
                if required:
                    lines.append(f"        out[{graphql_name!r}] = _serialize_input(self.{py_name})")
                else:
                    lines.append(f"        if self.{py_name} is not None:")
                    lines.append(f"            out[{graphql_name!r}] = _serialize_input(self.{py_name})")
            lines.append("        return out")
            lines.append("")

        fn_name = f"build_{snake_case(op.name)}_request"
        lines.append(f"def {fn_name}(variables: {class_name} | None = None) -> dict[str, Any]:")
        lines.append("    payload: dict[str, Any] = {")
        lines.append(f"        'operationName': {op.name!r},")
        lines.append(f"        'query': {op.name}_QUERY,")
        lines.append("    }")
        lines.append("    if variables is not None:")
        lines.append("        payload['variables'] = variables.to_dict()")
        lines.append("    return payload")
        lines.append("")

    return lines


def build_generated_module(
    operations: list[OperationSpec],
    input_names: list[str],
    enum_names: list[str],
    schema_types: dict[str, dict[str, Any]],
) -> str:
    lines: list[str] = []
    lines.append('"""Generated GraphQL helper DTOs and request builders.')
    lines.append("")
    lines.append("Do not edit manually. Regenerate with:")
    lines.append("  python3 scripts/generate_graphql_helpers.py")
    lines.append('"""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from dataclasses import dataclass")
    lines.append("from typing import Any, Literal")
    lines.append("")
    lines.append("")
    lines.append("def _serialize_input(value: Any) -> Any:")
    lines.append("    if hasattr(value, 'to_dict') and callable(value.to_dict):")
    lines.append("        return value.to_dict()")
    lines.append("    if isinstance(value, list):")
    lines.append("        return [_serialize_input(item) for item in value]")
    lines.append("    return value")
    lines.append("")

    if enum_names:
        lines.append("# Enum aliases")
        lines.extend(render_enum_aliases(enum_names, schema_types))
        lines.append("")

    if input_names:
        lines.append("# Input DTOs")
        lines.extend(render_input_dataclasses(input_names, set(enum_names), schema_types))

    lines.append("# Operation helpers")
    lines.extend(render_operation_helpers(operations, set(input_names), set(enum_names)))

    exports: list[str] = []
    exports.extend(enum_names)
    exports.extend(input_class_name(name) for name in input_names)
    for op in operations:
        exports.append(f"{op.name}_QUERY")
        exports.append(f"{pascal_case(op.name)}Variables")
        exports.append(f"build_{snake_case(op.name)}_request")

    lines.append("__all__ = [")
    for name in exports:
        lines.append(f"    {name!r},")
    lines.append("]")
    lines.append("")

    return "\n".join(lines)


def ensure_package_init(path: Path) -> None:
    init_path = path / "__init__.py"
    if init_path.exists():
        return
    init_path.write_text(
        "\"\"\"Generated GraphQL helper package for optional future usage.\"\"\"\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    schema = read_schema(args.introspection)
    schema_types_list = schema.get("types") or []
    schema_types = {
        item.get("name"): item
        for item in schema_types_list
        if isinstance(item, dict) and item.get("name")
    }

    operations = parse_operations(args.operations_dir)
    input_names, enum_names = collect_needed_input_and_enum_types(schema_types, operations)

    generated = build_generated_module(
        operations=operations,
        input_names=input_names,
        enum_names=enum_names,
        schema_types=schema_types,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    ensure_package_init(args.output.parent)
    args.output.write_text(generated, encoding="utf-8")

    print(f"Generated helpers in {args.output}")
    print(f"Operations: {len(operations)} | Input DTOs: {len(input_names)} | Enums: {len(enum_names)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
