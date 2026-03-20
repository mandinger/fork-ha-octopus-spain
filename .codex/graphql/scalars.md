# Scalars

Total `SCALAR` types: **20**

## `BigInt`

The `BigInt` scalar type represents non-fractional whole numeric values. `BigInt` is not constrained to 32-bit like the `Int` type and thus is a less compatible type.

_Scalar type._

## `Boolean`

The `Boolean` scalar type represents `true` or `false`.

_Scalar type._

## `BusinessRoleString`

Graphene String that validates against the available business roles. Available business roles: - OWNER - SUPPLIER

_Scalar type._

## `BusinessSectorString`

Graphene String that validates against the available business sectors. Available business sectors: No business sectors configured.

_Scalar type._

## `Date`

The `Date` scalar type represents a Date value as specified by [iso8601](https://en.wikipedia.org/wiki/ISO_8601).

_Scalar type._

## `DateTime`

The `DateTime` scalar type represents a DateTime value as specified by [iso8601](https://en.wikipedia.org/wiki/ISO_8601).

_Scalar type._

## `Decimal`

The `Decimal` scalar type represents a python Decimal.

_Scalar type._

## `Email`

_Scalar type._

## `Float`

The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

_Scalar type._

## `GenericScalar`

The `GenericScalar` scalar type represents a generic GraphQL scalar value that could be: String, Boolean, Int, Float, List or Object.

_Scalar type._

## `ID`

The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.

_Scalar type._

## `Int`

The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

_Scalar type._

## `JSONString`

Allows use of a JSON String for input / output from the GraphQL schema. Use of this type is *not recommended* as you lose the benefits of having a defined, static schema (one of the key benefits of GraphQL).

_Scalar type._

## `MonthlyFinancingScalar`

This is a scalar that allows us to return a dictionary of monthly financing prices, in the format dict[str, float] equating to dict[month, price].

_Scalar type._

## `NonEmptyID`

Custom scalar type representing a non-empty ID.

_Scalar type._

## `NonEmptyString`

Custom scalar type representing a non-empty string.

_Scalar type._

## `RoleString`

Graphene String that validates against the available roles. Available roles: - ACCOUNT_HOLDER - BILLING_REPRESENTATIVE - BILL_RECIPIENT - COMMUNICATION_RECIPIENT - CONTACT_PERSON - LEGAL_COMMUNICATION_RECIPIENT - LEGAL_REPRESENTATIVE - PRIMARY_BUSINESS_REPRESENTATIVE - PRIMARY_REPRESENTATIVE - USER

_Scalar type._

## `String`

The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

_Scalar type._

## `Time`

The `Time` scalar type represents a Time value as specified by [iso8601](https://en.wikipedia.org/wiki/ISO_8601).

_Scalar type._

## `UUID`

Leverages the internal Python implementation of UUID (uuid.UUID) to provide native UUID objects in fields, resolvers and input.

_Scalar type._

