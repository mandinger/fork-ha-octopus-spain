# GraphQL Helper Generation (Optional)

This repository now includes an additive codegen path that produces typed GraphQL helper classes from:

- `docs/InstrospectionQuery.json` (introspection schema)
- `graphql/operations/*.graphql` (operation definitions)

It does **not** change runtime integration code unless you import the generated helpers yourself.

## Generate helper DTOs + request builders

```bash
python3 scripts/generate_graphql_helpers.py
```

Output file:

- `custom_components/octopus_spain/lib/graphql_helpers/generated.py`

## Current operation files

- `graphql/operations/obtain_kraken_token.graphql`
- `graphql/operations/get_account_names.graphql`
- `graphql/operations/get_measurements.graphql`
- `graphql/operations/get_account_billing.graphql`

## Optional usage example

```python
from custom_components.octopus_spain.lib.graphql_helpers.generated import (
    ObtainJSONWebTokenInput,
    ObtainKrakenTokenVariables,
    build_obtain_kraken_token_request,
)

payload = build_obtain_kraken_token_request(
    ObtainKrakenTokenVariables(
        input=ObtainJSONWebTokenInput(APIKey="my-api-key"),
    )
)
# payload can be passed to your GraphQL client
```
