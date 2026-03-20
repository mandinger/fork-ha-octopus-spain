# Unions

Total `UNION` types: **28**

## `A629Details`

- Possible types: `A629DetailsAcceptance`, `A629DetailsRejection`

## `AccountEvent`

- Possible types: `EmailEventType`, `PrintEventType`, `SMSEventType`

## `ActionType`

Actions are things to do upon a user interaction, such as tapping a button.

- Possible types: `DeeplinkActionType`, `LinkActionType`, `BackendScreenEventActionType`, `CloseActionType`, `ScreenActionType`, `ShowInputFieldErrorsActionType`

## `BackendScreenType`

A backend screen is the top-level container for mobile UI.

- Possible types: `ComponentListType`, `GenericBackendScreen`, `Dashboard`, `FormScreenType`

## `CardItemType`

Items are sections making up a card.

- Possible types: `TextType`, `ImageType`, `AnimationType`, `RectangularButtonType`, `PillButtonType`

## `CharacteristicValueUnion`

- Possible types: `StringCharacteristicValueType`, `IntegerCharacteristicValueType`

## `ChargeDetail`

Supporting information about a charge

- Possible types: `SupplyOrServiceCharge`

## `ContractParty`

Union type representing the subject that entered into a contract, either an Account or Business.

- Possible types: `Account`, `BusinessType`

## `EnrollmentProcess`

- Possible types: `JoinSupplierProcessType`, `OccupyPropertyProcessType`

## `ErrorTypeUnion`

- Possible types: `SerializerErrorType`, `SerializerFieldErrorsType`

## `InkConversationEvent`

- Possible types: `InkNewMessage`

## `InkMessage`

- Possible types: `InkEmail`, `InkSMS`, `InkLine`, `InkWhatsApp`, `InkTwilioWhatsApp`, `InkPost`, `InkGenericMessage`, `InkLiveChatMessage`

## `ItemSizeType`

- Possible types: `FractionSizeType`, `PointsSizeType`

## `ItemType`

Items are sections making up a screen. They can be different types, hence Union.

- Possible types: `TextType`, `ImageType`, `AnimationType`, `RectangularButtonType`, `PillButtonType`, `CardComponentType`

## `LegacyOrderCustomerType`

Union type representing a customer, either an account or a business.

- Possible types: `Account`, `BusinessType`

## `LegacyOrderLinePeriodType`

Union type representing either a date range or a duration for an order line period.

- Possible types: `LegacyOrderLineDateRangeType`, `LegacyOrderLineDurationType`

## `LineMessage`

- Possible types: `LineTextMessage`, `LineStickerMessage`, `LineImageMessage`

## `LinkUserToLineResponse`

- Possible types: `LineLinkRedirectResponse`, `LinkTokenNotFound`, `AlreadyLinkedError`

## `P0Details`

- Possible types: `P0DetailsAcceptance`, `P0DetailsRejection`

## `PaymentPreferenceUnion`

One of PreferredInstructionType or UserManagedPaymentType

- Possible types: `PreferredInstruction`, `UserManagedPayment`

## `QuoteCostUnionType`

- Possible types: `DecimalType`, `FloatType`, `IntegerType`, `QuantityType`, `StringType`

## `SIPSData`

- Possible types: `SIPSElectricityData`, `SIPSGasData`

## `SalesRecordType`

A union type representing different kinds of sales records.

- Possible types: `KrakenDrivenSalesInfoType`, `KrakenTrackedSalesInfoType`, `ExternalSalesInfoType`

## `SectionContent`

- Possible types: `CardComponentType`, `CarouselItemType`

## `SmartFlexChargingProblem`

- Possible types: `SmartFlexChargingError`, `SmartFlexChargingTruncation`

## `SpecialCircumstanceRecordUnion`

- Possible types: `SpecialCircumstanceRecordType`, `TemporarySpecialCircumstanceRecordType`

## `UnlinkUserFromLineResponse`

- Possible types: `LineUnlinkedResponse`, `LinkTokenNotFound`, `LineCommonError`

## `UtilityFiltersOutput`

- Possible types: `ElectricityFiltersOutput`, `EmbeddedElectricityFiltersOutput`, `GasFiltersOutput`, `WaterFiltersOutput`

