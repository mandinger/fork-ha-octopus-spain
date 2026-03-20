#!/usr/bin/env python3
"""Fetch and save a GraphQL introspection schema from the command line.

Example:
    python3 scripts/update_introspection.py \
      --endpoint https://api.example.com/graphql \
      --bearer-token "$API_TOKEN"
"""

from __future__ import annotations

import argparse
import json
import os
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict


DEFAULT_OUTPUT = Path("docs/InstrospectionQuery.json")
DEFAULT_QUERY_FILE = Path("docs/introspection.full.query")
DEFAULT_ENDPOINT = "https://api.oees-kraken.energy/v1/graphql/"
DEFAULT_DOCS_DIR = Path(".codex/graphql")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update a GraphQL introspection JSON file."
    )
    parser.add_argument(
        "--endpoint",
        default=DEFAULT_ENDPOINT,
        help=(
            "GraphQL HTTP endpoint URL. "
            f"Default: {DEFAULT_ENDPOINT}"
        ),
    )
    parser.add_argument(
        "--query-file",
        type=Path,
        default=DEFAULT_QUERY_FILE,
        help=(
            "Path to the GraphQL introspection query file. "
            f"Default: {DEFAULT_QUERY_FILE}"
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Where to save introspection JSON. Default: {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--header",
        action="append",
        default=[],
        metavar="KEY: VALUE",
        help=(
            "Extra HTTP header. Repeat to add multiple headers. "
            "Example: --header 'x-api-key: abc123'"
        ),
    )
    parser.add_argument(
        "--bearer-token",
        help="Bearer token value for Authorization header.",
    )
    parser.add_argument(
        "--bearer-token-env",
        help=(
            "Environment variable name containing bearer token. "
            "Used only if --bearer-token is not provided."
        ),
    )
    parser.add_argument(
        "--operation-name",
        default="IntrospectionQuery",
        help="GraphQL operation name. Default: IntrospectionQuery",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP timeout in seconds. Default: 30",
    )
    parser.add_argument(
        "--insecure",
        action="store_true",
        help="Disable TLS certificate validation (not recommended).",
    )
    parser.add_argument(
        "--generate-docs",
        action="store_true",
        help="Also regenerate Markdown docs under .codex/graphql after updating JSON.",
    )
    parser.add_argument(
        "--docs-out-dir",
        type=Path,
        default=DEFAULT_DOCS_DIR,
        help=f"Docs output directory used with --generate-docs. Default: {DEFAULT_DOCS_DIR}",
    )
    return parser.parse_args()


def parse_headers(items: list[str]) -> Dict[str, str]:
    headers: Dict[str, str] = {}
    for item in items:
        if ":" not in item:
            raise ValueError(f"Invalid --header format: {item!r}. Expected 'KEY: VALUE'.")
        key, value = item.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            raise ValueError(f"Invalid --header key in: {item!r}")
        headers[key] = value
    return headers


def load_query(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(
            f"Query file not found: {path}. "
            "Create it or pass --query-file with a valid path."
        )
    query = path.read_text(encoding="utf-8").strip()
    if not query:
        raise ValueError(f"Query file is empty: {path}")
    return query


def build_ssl_context(insecure: bool) -> ssl.SSLContext | None:
    if not insecure:
        return None
    return ssl._create_unverified_context()  # noqa: SLF001


def main() -> int:
    args = parse_args()

    token = args.bearer_token
    if not token and args.bearer_token_env:
        token = os.getenv(args.bearer_token_env)

    try:
        headers = parse_headers(args.header)
        query = load_query(args.query_file)
    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}", file=sys.stderr)
        return 2

    if token:
        headers["Authorization"] = f"Bearer {token}"

    payload = {
        "query": query,
        "operationName": args.operation_name,
        "variables": {},
    }
    body = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        args.endpoint,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            **headers,
        },
    )

    context = build_ssl_context(args.insecure)

    try:
        with urllib.request.urlopen(request, timeout=args.timeout, context=context) as resp:
            response_text = resp.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", errors="replace")
        print(f"HTTP error {err.code}: {detail}", file=sys.stderr)
        return 1
    except urllib.error.URLError as err:
        print(f"Request failed: {err}", file=sys.stderr)
        return 1

    try:
        parsed = json.loads(response_text)
    except json.JSONDecodeError as err:
        print(f"Invalid JSON response: {err}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(parsed, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    schema = parsed.get("data", {}).get("__schema", {})
    type_count = len(schema.get("types", []) or [])
    print(f"Introspection saved to {args.output} ({type_count} types).")

    if args.generate_docs:
        script_path = Path(__file__).with_name("generate_graphql_docs.py")
        if not script_path.exists():
            print(
                f"Warning: docs generator not found at {script_path}. Skipping docs generation.",
                file=sys.stderr,
            )
        else:
            result = subprocess.run(
                [
                    sys.executable,
                    str(script_path),
                    "--input",
                    str(args.output),
                    "--out-dir",
                    str(args.docs_out_dir),
                ],
                check=False,
            )
            if result.returncode != 0:
                print(
                    f"Warning: docs generator exited with code {result.returncode}.",
                    file=sys.stderr,
                )
                return result.returncode

    if parsed.get("errors"):
        print("Warning: response contains GraphQL errors.", file=sys.stderr)
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
