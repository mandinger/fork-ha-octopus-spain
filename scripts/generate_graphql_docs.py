#!/usr/bin/env python3
"""Generate Markdown GraphQL reference docs from introspection JSON."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

DEFAULT_INPUT = Path("docs/InstrospectionQuery.json")
DEFAULT_OUT_DIR = Path(".codex/graphql")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Markdown docs from a GraphQL introspection JSON file."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Path to introspection JSON. Default: {DEFAULT_INPUT}",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help=f"Output directory for markdown docs. Default: {DEFAULT_OUT_DIR}",
    )
    parser.add_argument(
        "--include-internal",
        action="store_true",
        help="Include GraphQL internal __* types in generated docs.",
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


def clean_desc(text: str | None) -> str:
    if not text:
        return ""
    return " ".join(text.split())


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def code(text: str | None) -> str:
    if not text:
        return ""
    return f"`{text}`"


def fmt_type(type_ref: dict[str, Any] | None) -> str:
    if not type_ref:
        return "Unknown"
    kind = type_ref.get("kind")
    name = type_ref.get("name")
    of_type = type_ref.get("ofType")
    if kind == "NON_NULL":
        return f"{fmt_type(of_type)}!"
    if kind == "LIST":
        return f"[{fmt_type(of_type)}]"
    if name:
        return name
    if of_type:
        return fmt_type(of_type)
    return kind or "Unknown"


def fmt_args(args: list[dict[str, Any]] | None) -> str:
    if not args:
        return ""
    chunks: list[str] = []
    for arg in args:
        arg_name = arg.get("name", "")
        arg_type = fmt_type(arg.get("type"))
        default_value = arg.get("defaultValue")
        if default_value is None:
            chunks.append(f"{arg_name}: {arg_type}")
        else:
            chunks.append(f"{arg_name}: {arg_type} = {default_value}")
    return ", ".join(chunks)


def write(path: Path, lines: list[str]) -> None:
    try:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError as err:
        raise OSError(f"Unable to write {path}: {err}") from err


def fields_table(
    fields: list[dict[str, Any]] | None,
) -> list[str]:
    lines: list[str] = []
    if not fields:
        lines.append("_No fields._")
        return lines
    lines.append("| Field | Type | Args | Deprecated | Description |")
    lines.append("|---|---|---|---|---|")
    for field in sorted(fields, key=lambda x: x.get("name", "")):
        deprecation = "No"
        if field.get("isDeprecated"):
            reason = clean_desc(field.get("deprecationReason"))
            deprecation = f"Yes ({reason})" if reason else "Yes"
        lines.append(
            "| "
            + " | ".join(
                [
                    code(field.get("name")),
                    code(fmt_type(field.get("type"))),
                    code(fmt_args(field.get("args"))),
                    md_escape(deprecation),
                    md_escape(clean_desc(field.get("description"))),
                ]
            )
            + " |"
        )
    return lines


def input_fields_table(fields: list[dict[str, Any]] | None) -> list[str]:
    lines: list[str] = []
    if not fields:
        lines.append("_No input fields._")
        return lines
    lines.append("| Field | Type | Default | Description |")
    lines.append("|---|---|---|---|")
    for field in sorted(fields, key=lambda x: x.get("name", "")):
        default = field.get("defaultValue")
        lines.append(
            "| "
            + " | ".join(
                [
                    code(field.get("name")),
                    code(fmt_type(field.get("type"))),
                    code(str(default) if default is not None else ""),
                    md_escape(clean_desc(field.get("description"))),
                ]
            )
            + " |"
        )
    return lines


def enum_values_table(values: list[dict[str, Any]] | None) -> list[str]:
    lines: list[str] = []
    if not values:
        lines.append("_No enum values._")
        return lines
    lines.append("| Value | Deprecated | Description |")
    lines.append("|---|---|---|")
    for value in values:
        deprecation = "No"
        if value.get("isDeprecated"):
            reason = clean_desc(value.get("deprecationReason"))
            deprecation = f"Yes ({reason})" if reason else "Yes"
        lines.append(
            "| "
            + " | ".join(
                [
                    code(value.get("name")),
                    md_escape(deprecation),
                    md_escape(clean_desc(value.get("description"))),
                ]
            )
            + " |"
        )
    return lines


def root_operations_doc(
    root_name: str,
    root_type: dict[str, Any] | None,
) -> list[str]:
    if root_name == "Query":
        title = "Queries"
    else:
        title = f"{root_name}s"
    lines = [f"# {title}", ""]
    if not root_type:
        lines.append(f"_No `{root_name}` root type found in schema._")
        return lines
    fields = sorted(root_type.get("fields") or [], key=lambda x: x.get("name", ""))
    lines.append(f"Total `{root_name}` operations: **{len(fields)}**")
    lines.append("")
    for field in fields:
        operation_name = field.get("name", "")
        args = fmt_args(field.get("args"))
        signature = f"{operation_name}({args})" if args else operation_name
        lines.append(f"## `{signature}`")
        lines.append("")
        lines.append(f"- Return type: `{fmt_type(field.get('type'))}`")
        if field.get("isDeprecated"):
            reason = clean_desc(field.get("deprecationReason"))
            if reason:
                lines.append(f"- Deprecated: Yes ({reason})")
            else:
                lines.append("- Deprecated: Yes")
        description = clean_desc(field.get("description"))
        if description:
            lines.append(f"- Description: {md_escape(description)}")
        lines.append("")
        args_list = field.get("args") or []
        if args_list:
            lines.append("| Arg | Type | Default | Description |")
            lines.append("|---|---|---|---|")
            for arg in args_list:
                default = arg.get("defaultValue")
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            code(arg.get("name")),
                            code(fmt_type(arg.get("type"))),
                            code(str(default) if default is not None else ""),
                            md_escape(clean_desc(arg.get("description"))),
                        ]
                    )
                    + " |"
                )
            lines.append("")
    return lines


def type_group_doc(title: str, kind: str, entries: list[dict[str, Any]]) -> list[str]:
    lines = [f"# {title}", "", f"Total `{kind}` types: **{len(entries)}**", ""]
    for entry in entries:
        lines.append(f"## `{entry.get('name', '')}`")
        lines.append("")
        description = clean_desc(entry.get("description"))
        if description:
            lines.append(description)
            lines.append("")
        if kind in {"OBJECT", "INTERFACE"}:
            lines.extend(fields_table(entry.get("fields")))
            lines.append("")
        elif kind == "INPUT_OBJECT":
            lines.extend(input_fields_table(entry.get("inputFields")))
            lines.append("")
        elif kind == "ENUM":
            lines.extend(enum_values_table(entry.get("enumValues")))
            lines.append("")
        elif kind == "UNION":
            possible = entry.get("possibleTypes") or []
            if possible:
                lines.append("- Possible types: " + ", ".join(code(fmt_type(p)) for p in possible))
            else:
                lines.append("_No possible types._")
            lines.append("")
        elif kind == "SCALAR":
            lines.append("_Scalar type._")
            lines.append("")
    return lines


def directives_doc(directives: list[dict[str, Any]]) -> list[str]:
    lines = ["# Directives", "", f"Total directives: **{len(directives)}**", ""]
    for directive in sorted(directives, key=lambda d: d.get("name", "")):
        lines.append(f"## `{directive.get('name', '')}`")
        lines.append("")
        desc = clean_desc(directive.get("description"))
        if desc:
            lines.append(desc)
            lines.append("")
        locations = directive.get("locations") or []
        lines.append("- Locations: " + (", ".join(code(loc) for loc in locations) if locations else "_None_"))
        lines.append("")
        lines.append("| Arg | Type | Default | Description |")
        lines.append("|---|---|---|---|")
        args = directive.get("args") or []
        if args:
            for arg in args:
                default = arg.get("defaultValue")
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            code(arg.get("name")),
                            code(fmt_type(arg.get("type"))),
                            code(str(default) if default is not None else ""),
                            md_escape(clean_desc(arg.get("description"))),
                        ]
                    )
                    + " |"
                )
        else:
            lines.append("| _No args_ |  |  |  |")
        lines.append("")
    return lines


def main() -> int:
    args = parse_args()
    schema = read_schema(args.input)

    all_types = schema.get("types", [])
    types = all_types if args.include_internal else [t for t in all_types if not t.get("name", "").startswith("__")]
    by_name = {t.get("name"): t for t in types}
    by_kind: dict[str, list[dict[str, Any]]] = {
        "SCALAR": [],
        "ENUM": [],
        "INTERFACE": [],
        "UNION": [],
        "OBJECT": [],
        "INPUT_OBJECT": [],
    }
    for type_info in types:
        kind = type_info.get("kind")
        if kind in by_kind:
            by_kind[kind].append(type_info)
    for entries in by_kind.values():
        entries.sort(key=lambda x: x.get("name", ""))

    query_name = (schema.get("queryType") or {}).get("name")
    mutation_name = (schema.get("mutationType") or {}).get("name")
    subscription_name = (schema.get("subscriptionType") or {}).get("name")
    query_type = by_name.get(query_name)
    mutation_type = by_name.get(mutation_name)

    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    readme_lines = [
        "# GraphQL API Reference (Generated)",
        "",
        f"- Source: `{args.input}`",
        f"- Generated on: {date.today().isoformat()}",
        f"- Total types in schema: {len(all_types)}",
        f"- Documented types: {len(types)}",
        "",
        "## Files",
        "",
        "- `schema-summary.md`",
        "- `queries.md`",
        "- `mutations.md`",
        "- `directives.md`",
        "- `scalars.md`",
        "- `enums.md`",
        "- `interfaces.md`",
        "- `unions.md`",
        "- `objects.md`",
        "- `input-objects.md`",
        "",
        "## Regenerate",
        "",
        "```bash",
        "python3 scripts/generate_graphql_docs.py",
        "```",
    ]
    try:
        write(out_dir / "README.md", readme_lines)

        summary_lines = [
        "# Schema Summary",
        "",
        f"- Query root type: `{query_name}`",
        f"- Mutation root type: `{mutation_name}`",
        f"- Subscription root type: `{subscription_name}`",
        f"- Directives: {len(schema.get('directives') or [])}",
        "",
        "## Type Counts",
        "",
        "| Kind | Count |",
        "|---|---:|",
        f"| `SCALAR` | {len(by_kind['SCALAR'])} |",
        f"| `ENUM` | {len(by_kind['ENUM'])} |",
        f"| `INTERFACE` | {len(by_kind['INTERFACE'])} |",
        f"| `UNION` | {len(by_kind['UNION'])} |",
        f"| `OBJECT` | {len(by_kind['OBJECT'])} |",
        f"| `INPUT_OBJECT` | {len(by_kind['INPUT_OBJECT'])} |",
        "",
        "## Root Field Counts",
        "",
        f"- Queries: {len((query_type or {}).get('fields') or [])}",
        f"- Mutations: {len((mutation_type or {}).get('fields') or [])}",
        ]
        write(out_dir / "schema-summary.md", summary_lines)

        write(out_dir / "queries.md", root_operations_doc("Query", query_type))
        write(out_dir / "mutations.md", root_operations_doc("Mutation", mutation_type))
        write(out_dir / "directives.md", directives_doc(schema.get("directives") or []))
        write(out_dir / "scalars.md", type_group_doc("Scalars", "SCALAR", by_kind["SCALAR"]))
        write(out_dir / "enums.md", type_group_doc("Enums", "ENUM", by_kind["ENUM"]))
        write(
            out_dir / "interfaces.md",
            type_group_doc("Interfaces", "INTERFACE", by_kind["INTERFACE"]),
        )
        write(out_dir / "unions.md", type_group_doc("Unions", "UNION", by_kind["UNION"]))
        write(out_dir / "objects.md", type_group_doc("Objects", "OBJECT", by_kind["OBJECT"]))
        write(
            out_dir / "input-objects.md",
            type_group_doc("Input Objects", "INPUT_OBJECT", by_kind["INPUT_OBJECT"]),
        )
    except OSError as err:
        print(err)
        return 1

    print(f"Generated docs in {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
