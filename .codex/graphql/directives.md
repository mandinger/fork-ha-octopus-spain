# Directives

Total directives: **5**

## `deprecated`

Marks an element of a GraphQL schema as no longer supported.

- Locations: `FIELD_DEFINITION`, `ARGUMENT_DEFINITION`, `INPUT_FIELD_DEFINITION`, `ENUM_VALUE`

| Arg | Type | Default | Description |
|---|---|---|---|
| `reason` | `String` | `"No longer supported"` | Explains why this element was deprecated, usually also including a suggestion for how to access supported similar data. Formatted using the Markdown syntax, as specified by [CommonMark](https://commonmark.org/). |

## `include`

Directs the executor to include this field or fragment only when the `if` argument is true.

- Locations: `FIELD`, `FRAGMENT_SPREAD`, `INLINE_FRAGMENT`

| Arg | Type | Default | Description |
|---|---|---|---|
| `if` | `Boolean!` |  | Included when true. |

## `oneOf`

Indicates an Input Object is a OneOf Input Object.

- Locations: `INPUT_OBJECT`

| Arg | Type | Default | Description |
|---|---|---|---|
| _No args_ |  |  |  |

## `skip`

Directs the executor to skip this field or fragment when the `if` argument is true.

- Locations: `FIELD`, `FRAGMENT_SPREAD`, `INLINE_FRAGMENT`

| Arg | Type | Default | Description |
|---|---|---|---|
| `if` | `Boolean!` |  | Skipped when true. |

## `specifiedBy`

Exposes a URL that specifies the behavior of this scalar.

- Locations: `SCALAR`

| Arg | Type | Default | Description |
|---|---|---|---|
| `url` | `String!` |  | The URL that specifies the behavior of this scalar. |

