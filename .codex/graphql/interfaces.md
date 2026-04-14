# Interfaces

Total `INTERFACE` types: **47**

## `AbstractSupplyPointProcessInterface`

Interface for all lifecycle journey processes that inherit from AbstractSupplyPointProcess.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | The ID or the primary key of the lifecycle process. |
| `status` | `LifecycleSupplyPointProcessStatus` |  | No | The status of the process. |
| `supplyPoints` | `SupplyPointConnectionTypeConnection!` | `before: String, after: String, first: Int, last: Int` | No | The supply points associated with the process. |

## `AccessibilityInterface`

Properties relating to the accessibility of features.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accessibilityHidden` | `Boolean` |  | No | Whether the element is hidden from view. |
| `accessibilityLabel` | `String` |  | No | Accessible description of the element. |

## `AccountInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountType` | `AccountTypeChoices` |  | No | The type of account. |
| `activeHardshipAgreements` | `[HardshipAgreementType]` |  | No | List of active hardship agreements for the user when is_in_hardship is True. |
| `activeReferralSchemes` | `ReferralSchemeTypes` |  | No | The referral schemes currently active for this account. |
| `address` | `RichAddressType` |  | No | The billing address of this account, stored in the new libaddressinput-based format. Note that `name` and `organization` are very unlikely to be supplied here; the `billing_name` field on the account itself is generally used for that purpose instead. |
| `annualStatements` | `AnnualStatementConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Fetch annual statements for the account. |
| `applications` | `AccountApplicationConnectionTypeConnection` | `status: AccountApplicationStatus, before: String, after: String, first: Int, last: Int` | No | Applications by this account to become our customer. More recent applications will be listed first. |
| `assistanceAgreements` | `[AssistanceAgreementType]` |  | No | Assistance agreements for account. |
| `balance` | `Int!` | `includeAllLedgers: Boolean = false` | No | The current account balance. |
| `bill` | `BillInterface` | `id: ID, identifier: String, billType: BillTypeEnum, ledgerNumber: String` | No | Fetch a specific issued bill (invoice/statement) for the account. |
| `billingAddress` | `String` |  | No | The billing address of the account. |
| `billingAddressLine1` | `String` |  | No |  |
| `billingAddressLine2` | `String` |  | No |  |
| `billingAddressLine3` | `String` |  | No |  |
| `billingAddressLine4` | `String` |  | No |  |
| `billingAddressLine5` | `String` |  | No |  |
| `billingAddressPostcode` | `String` |  | No |  |
| `billingCountryCode` | `String` |  | No |  |
| `billingDeliveryPointIdentifier` | `String` |  | No |  |
| `billingEmail` | `String` |  | No | The billing email of the account. |
| `billingName` | `String` |  | No | The billing name of the account. |
| `billingOptions` | `BillingOptionsType` |  | No | Information about the account's billing cycle. |
| `billingSubName` | `String` |  | No | The billing sub name of the account. |
| `bills` | `BillConnectionTypeConnection` | `includeBillsWithoutPDF: Boolean = false, includeOpenStatements: Boolean = false, includeHeldStatements: Boolean = false, includeHistoricStatements: Boolean = true, onlyCurrentEmail: Boolean = false, ledgerNumber: String, fromDate: Date, toDate: Date, issuedFromDate: Date, issuedToDate: Date, orderBy: BillsOrderBy = FROM_DATE_DESC, offset: Int, before: String, after: String, first: Int, last: Int` | No | Fetch issued bills (invoices/statements) for the account. |
| `brand` | `String` |  | No | The brand of the account. |
| `business` | `BusinessType` |  | No | Business info related to a business account. |
| `businessType` | `BusinessTypeOptions` |  | Yes (The 'businessType' field is deprecated. Use `business.businessType` instead - Marked as deprecated on 2022-03-09. - Scheduled for removal on or after 2024-01-01.) | The company type of a business account. |
| `campaigns` | `[AccountCampaignType]` |  | No | The campaigns associated with an account. |
| `canRequestRefund` | `Boolean` |  | No | Whether the account can request a credit refund. |
| `commsDeliveryPreference` | `CommsDeliveryPreference` |  | No | The method the account has specified they prefer we contact them. |
| `communicationDeliveryPreference` | `String` |  | Yes (The 'communicationDeliveryPreference' field is deprecated. Use `commsDeliveryPreference` instead - Marked as deprecated on 2022-05-27. - Scheduled for removal on or after 2024-01-01.) |  |
| `complaints` | `ComplaintConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The complaints associated with an account. |
| `consents` | `[ConsentType!]!` |  | No | Consents linked to this account. |
| `contributionAgreements` | `[ContributionAgreementType]` |  | No | Contribution agreements for account. |
| `createdAt` | `DateTime` |  | No | The datetime that the account was originally created. |
| `debtCollectionProceedings` | `[DebtCollectionProceedingType]` |  | No | Debt collection proceedings for account. |
| `directDebitInstructions` | `DirectDebitInstructionConnectionTypeConnection` | `statuses: [DirectDebitInstructionStatus], before: String, after: String, first: Int, last: Int` | No | The direct debit instructions of the account |
| `documentAccessibility` | `DocumentAccessibilityChoices` |  | No | The document accessibility preference of the account. |
| `events` | `AccountEventConnectionTypeConnection` | `eventTypes: [AccountEventType], before: String, after: String, first: Int, last: Int` | No | The account events that were recorded for the account. |
| `fileAttachments` | `[AccountFileAttachment]` |  | No | Files attached to this account. |
| `isInHardship` | `Boolean` |  | No | True if there is an active Hardship Agreement for this account. False otherwise. |
| `ledgers` | `[LedgerType]` | `ledgerNumber: String, includeDebtLedgers: Boolean = true` | No | Ledgers provide the foundation of bookkeeping functionality. Similar to a bank account, they allow us to keep track of financial activity on a particular customer account. |
| `maximumRefund` | `MaximumRefundType` | `ledgerNumber: String` | No | The maximum amount a customer is allowed to request as a refund and the reason why that's the maximum amount. |
| `metadata` | `[Metadata]` |  | No | Metadata associated with the account. |
| `notes` | `[AccountNoteType]` |  | No | Notes for the account. |
| `number` | `String` |  | No | A code that uniquely identifies the account. |
| `overdueBalance` | `Int` |  | No | The current account overdue balance. |
| `paginatedFileAttachments` | `AccountFileAttachmentConnectionTypeConnection` | `id: Int, category: String, before: String, after: String, first: Int, last: Int` | No | Files attached to this account. |
| `paginatedPaymentForecast` | `PaymentForecastConnectionTypeConnection` | `dateTo: Date, ledgerNumber: String, before: String, after: String, first: Int, last: Int` | No | Paginated payment forecasts for an account. Starts from today's date (inclusive). The interface supports `last` but does not guarantee 'lastness'. |
| `paymentForecast` | `[PaymentForecastType]` | `dateTo: Date!, ledgerNumber: String` | Yes (The 'paymentForecast' field is deprecated. Please use 'paginatedPaymentForecast' instead. - Marked as deprecated on 2024-01-03. - Scheduled for removal on or after 2025-01-01.) | A list displaying the payment forecast for an account. The list starts from today's date (inclusive). |
| `paymentMethods` | `PaymentInstructionConnectionTypeConnection` | `statuses: [PaymentInstructionStatus], before: String, after: String, first: Int, last: Int` | No | The payment instructions of the account. |
| `paymentPlans` | `PaymentPlanConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The payment plans that have been created for this account. |
| `paymentSchedules` | `PaymentScheduleConnectionTypeConnection` | `activeOnDate: Date, active: Boolean, includeDormant: Boolean = true, ledgerType: Int, ledgerNumber: String, reason: PaymentScheduleReasonOptions, before: String, after: String, first: Int, last: Int` | No | The schedules that describe how we would expect to take payments for an account on a given month. |
| `payments` | `AccountPaymentConnectionTypeConnection` | `ledgerNumber: String, status: AccountPaymentStatusOptions, reason: PaymentReasonOptions, includePromises: Boolean = true, before: String, after: String, first: Int, last: Int` | No | The payments made into an account from a payment instruction. |
| `portfolio` | `PortfolioType` |  | No | The portfolio this account is linked to. |
| `preferredLanguageForComms` | `String` |  | No | The language that the account preferred for communications. |
| `provisionalTransactions` | `ProvisionalTransactionConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No |  |
| `references` | `[AccountReferenceType]` |  | No | Account references linked to this account. |
| `referrals` | `ReferralConnectionTypeConnection` | `status: ReferralStatus, before: String, after: String, first: Int, last: Int` | No | The referrals created by this account. |
| `referralsCreated` | `Int` |  | No | Number of referrals created by this account. |
| `reminders` | `AccountReminderConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The reminders associated with an account. |
| `repayments` | `AccountRepaymentConnectionTypeConnection` | `statuses: [AccountRepaymentStatusOptions], before: String, after: String, first: Int, last: Int` | No | The repayments that have been requested for this account. |
| `requestRefundEligibility` | `RequestRefundEligibilityType` | `ledgerNumber: String` | No | Details about the eligibility status for requesting a refund. |
| `rewards` | `[RewardType]` |  | No | The rewards applied to this account. |
| `splitBillingAddress` | `[String]` |  | No | List of billing address lines. |
| `status` | `AccountStatus` |  | No | The current status of the account. |
| `transactions` | `TransactionConnectionTypeConnection` | `transactionTypes: [TransactionTypeFilter] = [], transactionTypesExcluded: [TransactionTypeFilter] = [], ledgerNumber: String, includeAllLedgers: Boolean, fromDate: Date, toDate: Date, orderBy: TransactionsOrderBy = POSTED_DATE_DESC, offset: Int, before: String, after: String, first: Int, last: Int` | No | Fetch transactions that have taken place on the account. |
| `urn` | `String` |  | No | Unique reference number from a 3rd party enrolment. |

## `ActionInterface`

Actions are events created by buttons and other interaction.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `typeName` | `String` |  | No | The name of the action object's type. |

## `AgreementInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreedFrom` | `DateTime` |  | No | The datetime the agreement was entered. |
| `agreedTo` | `DateTime` |  | No | The datetime the agreement was terminated. |
| `id` | `Int` |  | No | The ID of the agreement. |
| `isRevoked` | `Boolean` |  | No | Whether the agreement is revoked. |
| `rescissionDeadlineAt` | `DateTime` |  | No | The deadline datetime for rescinding the agreement. |
| `validFrom` | `DateTime` |  | No | The start datetime of the agreement. |
| `validTo` | `DateTime` |  | No | The end datetime of the agreement. |

## `BackendScreenInterface`

A backend screen is the top-level container for mobile UI.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `name` | `String!` |  | No | The name of the screen. |
| `refreshFrequency` | `Int` |  | No | The refresh / polling frequency in milliseconds. |
| `screenData` | `String` |  | No | Serialized JSON representation of the screen. |

## `BillInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `BillingAttachmentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No |  |
| `billType` | `BillTypeEnum` |  | No | The type of the bill. |
| `fromDate` | `Date` |  | No | The date of the bill is covered from. |
| `id` | `ID` |  | No | The ID of the bill. |
| `issuedDate` | `Date` |  | No | The date the bill was sent to the customer. |
| `reversalsAfterClose` | `StatementReversalsAfterClose!` |  | No | How many charges have been reversed after the close date. |
| `temporaryUrl` | `String` |  | Yes (The 'temporaryUrl' field is deprecated. This field is deprecated. Use the 'attachments' field instead. - Marked as deprecated on 2024-09-16. - Scheduled for removal on or after 2025-09-01.) | Requesting this field generates a temporary URL at which bill is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). This field can raise an error with errorClass NOT_FOUND if the bill document has not been created/issued yet. This field is deprecated use 'attachments' field instead. |
| `toDate` | `Date` |  | No | The date of the bill is covered to. |

## `BillTransactionType`

Transactions are a record of money being added or subtracted from a ledger

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amounts` | `TransactionAmountType` |  | No | The net, tax and gross amounts for the transaction. Note: for payments and repayments, only the net amount is returned. |
| `createdAt` | `DateTime` |  | No | The date time when the transaction is created. |
| `id` | `ID` |  | No | The unique identifier for the transaction. |
| `note` | `String` |  | No | Returns the note field value for the transaction, which contains additional info. |
| `postedDate` | `Date` |  | No | The date the transaction was posted. |
| `reasonCode` | `String` |  | No | Returns the reason. |
| `title` | `String` |  | No | A user readable string that indicates what this transaction relates to. |

## `ButtonInterface`

The button interface.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `buttonAction` | `ActionType!` |  | No | The action to perform when the button is pressed. |
| `buttonStyle` | `ButtonStyle` |  | No | The button style. |
| `title` | `String!` |  | No | Title text of the button. |

## `CallInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | If known, this is the account that a call is about. For inbound calls, we attempt to identify the account based on the phone number of the incoming call. For outbound calls, the account will be automatically set if the call was initiated from an account page. For all call types, the account can be updated, for example to correct a misidentification of an incoming call. |
| `id` | `ID!` |  | No | The ID of the call. |
| `metadata` | `[CallMetadataItemType]!` |  | No | Metadata related to the call, for example metrics or data passed via an interactive voice response (IVR). |

## `CharacteristicValueInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `characteristic` | `CharacteristicType` |  | No | The product characteristic. |
| `value` | `String` |  | No | A string representation of a characteristic value, for convenience. |

## `CommonSupplyPointInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `externalIdentifier` | `String` |  | No | The external identifier of the supply point. |
| `id` | `ID!` |  | No | The ID of the supply point. |
| `marketName` | `String!` |  | No | The market this supply point belongs to. |

## `ConstituentInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fromDate` | `Date` |  | No | The date of the constituent bill covered from. |
| `id` | `ID` |  | No | The ID of the constituent bill. |
| `toDate` | `Date` |  | No | The date of the constituent bill covered to. |

## `ContractJourneyInterface`

Represents a Contract Journey.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contractDetails` | `ContractDetails` |  | No | The details of the associated contract. |
| `journeyType` | `ContractJourneyType` |  | No | The type of the contract journey. |
| `notes` | `[ContractNoteType]` |  | No | Notes associated with this contract journey. |
| `number` | `NonEmptyString!` |  | No | The number of the contract journey. |
| `orderReference` | `String` |  | No | The order reference associated with the contract journey. |
| `requestedAt` | `DateTime` |  | No | The date and time when the contract journey was requested. |
| `status` | `ContractJourneyStatus` |  | No | The status of the contract journey. |

## `DeviceChargingSession`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cost` | `Money` |  | No | The cost for the charge added during a charging session. |
| `end` | `DateTime!` |  | No | The end time of a charging session. |
| `energyAdded` | `Energy` |  | No | The energy added during a charging session. |
| `start` | `DateTime!` |  | No | The start time of a charging session. |
| `stateOfChargeChange` | `Decimal` |  | No | The change in state of charge during a charging session. The value will be between 0 and 100, if not null. |
| `stateOfChargeFinal` | `Decimal` |  | No | The final state of charge after a charging session. The value will be between 0 and 100, if not null. |

## `DeviceReAuthenticationInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isEligible` | `Boolean` |  | No | Whether the device is eligible for re-authentication. If it returns False, then re-authentication is not supported for this device. Please remove and re-add the device to restore connectivity. |

## `ElectricDevice`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `chargingSessions` | `DeviceChargingSessionConnection` | `before: DateTime, after: DateTime, sessionTypes: [ChargingSessionType], first: Int, last: Int` | No | History of charging sessions for a SmartFlex device. |

## `FileAttachment`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fetchUrl` | `String` |  | No |  |
| `isReady` | `Boolean` |  | No | Is the file ready for use / downloadable? |
| `isUploaded` | `Boolean` |  | No | Is the file uploaded to S3? |
| `sizeInBytes` | `Int` |  | No |  |

## `FlexDevicePreferenceScheduleSettingInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `Int!` |  | No | The unique id of the device preference schedule setting. |
| `max` | `Decimal` |  | No | The maximum value a preference can be set to (inclusive). |
| `maxConstraint` | `PreferenceConstraint` |  | No | The constraint applied to the max value. |
| `min` | `Decimal` |  | No | The minimum value a preference can be set to (inclusive). |
| `minConstraint` | `PreferenceConstraint` |  | No | The constraint applied to the min value. |
| `step` | `Decimal!` |  | No | The step size preference can be set to. |
| `targetConstraint` | `PreferenceConstraint` |  | No | The constraint applied to the target value. |
| `timeFrom` | `Time` |  | No | The minimum time a preference can be set to (inclusive). |
| `timeStep` | `Int!` |  | No | The step amount (in minutes) a preference schedule time can be set. |
| `timeTo` | `Time` |  | No | The maximum time a preference can be set to (inclusive). |

## `FlexDevicePreferenceSettingInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceType` | `String!` |  | No | The device type of the setting. |
| `id` | `Int!` |  | No | The unique id of the device preference setting. |
| `mode` | `PreferencesModeChoices!` |  | No | The mode of the setting. |
| `scheduleSettings` | `[FlexDevicePreferenceScheduleSettingInterface]!` |  | No | Scheduled preference settings. |
| `unit` | `PreferencesUnitChoices!` |  | No | The unit of the min and max values in the preferences setting. |

## `HasReadings`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `readings` | `Readings` | `startAt: DateTime!, endAt: DateTime!, readingType: ReadingTypes!, timeGranularity: TimeGranularities, timezone: String = "Europe/Madrid", units: [Units]` | No | Get readings from a readable device e.g., a supply point, device, or register. |

## `IdentifiableInterface`

The identity of an object.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | Unique identifier of the object. |
| `typename` | `String` |  | No | The name of the object's type. |

## `InkConversationEventInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `occurredAt` | `DateTime!` |  | No | The time the conversation event occurred. |

## `LeaveSupplierProcessDataInterface`

Represents data associated with a LeaveSupplier journey. i.e. concrete implementation of AbstractLeaveSupplierProcessData.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `futureBillingAddress` | `RichAddressType` |  | No | The future billing address for the customers account. |
| `marketData` | `LeaveSupplierMarketOutputType` |  | No | The market data associated with the process. |
| `requestedAt` | `DateTime` |  | No | The time at which the process was initiated. |
| `requestedSupplyEndDate` | `Date` |  | No | The requested supply end date. |
| `waiveExitFee` | `Boolean` |  | No | Whether the exit fee is to be waived. |

## `LedgerInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptsPayments` | `Boolean` |  | No | Whether payments can be posted onto this ledger. |
| `affectsAccountBalance` | `Boolean` |  | No | Whether this ledger's balance contributes to the account's balance. |
| `agreements` | `AgreementConnection` | `before: String, after: String, first: Int, last: Int` | No | The charged supply agreements of the ledger. |
| `amountOwedByCustomer` | `Int` |  | No | The amount owed from the customer perspective. A positive value implies the customer owes the business, while a negative amount implies the customer is in credit. |
| `balance` | `Int` |  | No | The current balance on the ledger in minor units of currency. |
| `creditTransferPermissionsData` | `CreditTransferPermissionsDataType` |  | No | Permissions data for credit transfers involving the given ledger. |
| `debtLedger` | `LedgerInterface` |  | No | The debt ledger assigned to this ledger. |
| `id` | `ID` |  | Yes (The 'ledgerId' field is deprecated. Please use 'ledgerNumber' instead. This is in the form of 'L-123456789A' - Marked as deprecated on 2024-10-22. - Scheduled for removal on or after 2025-06-25.) |  |
| `invoices` | `InvoiceBillingDocumentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | An invoice is a bill that contains individual transactions (i.e. charges, credits, payments, and repayments). These may come from any period of time. |
| `ledgerType` | `String` |  | No |  |
| `name` | `String` |  | No | The display name of the ledger. |
| `number` | `String` |  | No | The canonical name of the ledger. |
| `paymentAdequacy` | `PaymentAdequacyDetailsType` |  | No |  |
| `paymentPreferenceAtTime` | `PaymentPreferenceUnion` | `atTime: DateTime!` | No | The customer's preferred payment method at a point in time. The possible errors that can be raised are: - KT-CT-3976: The ledger has no configured payment preference. - KT-CT-3977: Ledger was not accepting payments at this time. - KT-CT-1113: Disabled GraphQL field requested. |
| `paymentPreferences` | `PaymentPreferenceConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The customer's preferred payment methods. |
| `refundRequests` | `RefundRequestConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Refund requests for a given ledger. |
| `repaymentRequests` | `RepaymentRequestConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Repayment requests for a given ledger. |
| `statements` | `StatementBillingDocumentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A statement is a billing document that contains all entries on a ledger during a period of time. A customer can understand how their ledger's balance has changed by looking at each statement in series. |
| `transactions` | `TransactionConnectionTypeConnection` | `transactionTypes: [TransactionTypeFilter] = [], fromDate: Date, toDate: Date, orderBy: TransactionsOrderBy = POSTED_DATE_DESC, before: String, after: String, first: Int, last: Int` | No | Transactions on the given ledger. |
| `usablePaymentInstructions` | `PaymentInstructionConnectionTypeConnection` | `usableAt: DateTime, before: String, after: String, first: Int, last: Int` | No | The usable payment instructions for this ledger. |

## `MeasurementInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `metaData` | `MeasurementsMetadataOutput` |  | No | This type will return more granular data about the measurement. |
| `readAt` | `DateTime!` |  | No | The datetime the measurement was taken. |
| `source` | `String!` |  | No | The data source of the measurement. |
| `unit` | `String!` |  | No | The unit of the measurement. |
| `value` | `Decimal!` |  | No | The value of the measurement. |

## `MediaInterface`

The media interface.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `horizontalAlignment` | `Alignment` |  | No | The horizontal alignment of the media. |
| `mediaUrl` | `String!` |  | No | The resource URL of the media. |

## `Node`

An object with an ID

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No | The ID of the object |

## `PreferenceConstraint`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `max` | `Decimal` |  | No | The maximum value this constraint allows. |
| `min` | `Decimal` |  | No | The minimum value this constraint allows. |

## `ProductInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `prices` | `PowerAndEnergyPrices` | `powerDecimalPlaces: Int` | No | Active power and energy prices for this product. |

## `PropertyInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `address` | `String` |  | No | The address of the property, formatted into a single string. |
| `ancestors` | `PropertyConnection` | `hierarchyName: String = "default", before: String, after: String, first: Int, last: Int` | No | Ancestor properties in the specified hierarchy, ordered from root to immediate parent. Returns empty list if the property is not in the hierarchy. |
| `coordinates` | `CoordinatesType` |  | No | Coordinates for the property, useful for displaying the property on a map. |
| `descendants` | `PropertyConnection` | `hierarchyName: String = "default", depth: Int = 1, before: String, after: String, first: Int, last: Int` | No | Descendant properties in the specified hierarchy. Returns empty list if the property is not in the hierarchy. |
| `embeddedNetwork` | `EmbeddedNetworkType` |  | No | The embedded network this property belongs to, if any. |
| `id` | `String` |  | No |  |
| `label` | `String` |  | No | An optional label for the property. |
| `measurements` | `MeasurementConnection` | `startAt: DateTime = "0001-01-03T00:00:00-00:14:44", endAt: DateTime = "9999-12-29T23:59:59.999999+01:00", startOn: Date, endOn: Date, timezone: String = "Europe/Madrid", utilityFilters: [UtilityFiltersInput] = [], before: String, after: String, first: Int, last: Int` | No | Measurements at a property |
| `occupancyPeriods` | `[OccupancyPeriodType]` |  | No | Time periods during which the property is associated with an account. Useful to display information about house-moves, as performing a move out of a property will set the end date for the occupancy period. |
| `parent` | `PropertyInterface` | `hierarchyName: String = "default"` | No | The parent property in the specified hierarchy. Returns null if the property has no parent or is not in the hierarchy. |
| `richAddress` | `PropertyRichAddressType` |  | No | Property rich address. |
| `splitAddress` | `[String]` |  | No | List of address lines. |

## `ReferralInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The referral code. |
| `combinedPaymentAmount` | `Int` |  | No | The payment amount in the smallest unit of the clients currency received by the referrer and the referee combined. |
| `paymentDate` | `Date` |  | No | The date when the payment was made. |
| `paymentStatus` | `String` |  | No | The status of the payment. |
| `referredUserJoinDate` | `DateTime` |  | No | The date the referred user joined. |
| `referredUserName` | `String` |  | No | The name of the referred user. |
| `referredUserPaymentAmount` | `Int` |  | No | Payment amount given to the referred account in the smallest unit of the client's currency. |
| `referringUserPaymentAmount` | `Int` |  | No | Payment amount given to the referring account in the clients fractional currency unit. |
| `schemeType` | `ReferralSchemeTypeChoices` |  | No | The type of reward scheme. |

## `RewardInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The referral code. |
| `paymentDate` | `Date` |  | No | The date when the payment was made. |
| `paymentStatus` | `ReferralStatusChoices` |  | No | The status of the reward payment. |
| `rewardAmount` | `Int` |  | No | Reward amount given to the account in the smallest unit of the clients currency. |
| `schemeType` | `ReferralSchemeTypeChoices` |  | No | The type of reward scheme. |

## `SelectFromList`

A base implementation of an interface where the user must select an option from a list.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SizedItemInterface`

Sizes for elements.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `width` | `ItemSizeType` |  | No | The measurement of the element. |

## `SmartFlexDeviceAlertInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String` |  | No | A device alert message. |
| `publishedAt` | `DateTime` |  | No | When a device alert message is published. |

## `SmartFlexDeviceInterface`

Some general information about a device.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `alerts` | `[SmartFlexDeviceAlertInterface]` |  | No | Active alert message(s) for a device, showing the latest first. |
| `deviceType` | `KrakenFlexDeviceTypes!` |  | No | The type of device. |
| `id` | `ID!` |  | No | A UUID that identifies this device registration. Re-registering this device will result in a different ID. |
| `integrationDeviceId` | `String` |  | No | The third-party integration device ID. |
| `name` | `String` |  | No | The user-friendly name for the device. |
| `onboardingWizard` | `SmartFlexOnboardingWizard` |  | No | The current onboarding wizard for a device. |
| `preferenceSetting` | `FlexDevicePreferenceSettingInterface` |  | No | The preference setting for this device. |
| `preferences` | `SmartFlexDevicePreferencesInterface` |  | No | The device's preference details. |
| `propertyId` | `String` |  | No | The id of the property linked to the device. |
| `provider` | `ProviderChoices!` |  | No | The third-party that enables control of this device. |
| `reAuthenticationState` | `DeviceReAuthenticationInterface` |  | No | The re-authentication state of this device, if applicable. |
| `status` | `SmartFlexDeviceStatusInterface!` |  | No | Information about the current status of this device. |

## `SmartFlexDevicePreferencesInterface`

Details about a device's preferences.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `gridExport` | `FlexGridExportStatus!` |  | No | The status of the device's grid export capability. |
| `isChargingDurationCapped` | `FlexIsChargingDurationCapped!` |  | No | The status of the device's charging duration cap. |
| `mode` | `PreferencesModeChoices!` |  | No | The device's preference mode. |
| `schedules` | `[SmartFlexDevicePreferenceSchedule]` |  | No | The schedules of the device's preference. |
| `targetType` | `PreferencesTargetType!` |  | No | The target type of the preference. |
| `unit` | `PreferencesUnitChoices!` |  | No | The unit of the preference schedules' min and max values. |

## `SmartFlexDeviceStatusInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `current` | `SmartFlexDeviceLifecycleStatus` |  | No | The current status of the device. |
| `currentState` | `SmartFlexDeviceState` |  | No | The current state of this SmartFlex device state machine. |
| `isSuspended` | `Boolean` |  | No | Whether control of the device is currently disabled. |

## `SmartFlexListItemInterface`

An interface for a list item in a SmartFlex onboarding step.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this list item. |

## `SmartFlexOnboardingErrorInterface`

An interface for errors that can occur during SmartFlex onboarding.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String` |  | No | A human readable error message. |

## `SmartFlexOnboardingStepInterface`

The next step of the SmartFlex onboarding wizard.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |

## `SupplementaryLedgerInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `currentBalance` | `Int` |  | No | The current final balance of the ledger in pence. |
| `id` | `ID` |  | Yes (The 'ledgerId' field is deprecated. Please use 'ledgerNumber' instead. This is in the form of 'L-123456789A' - Marked as deprecated on 2024-10-22. - Scheduled for removal on or after 2025-06-25.) |  |
| `ledgerType` | `String` |  | No |  |
| `name` | `String` |  | No | The display name of the ledger. |
| `number` | `String` |  | No | The canonical name of the ledger. |
| `paymentAdequacy` | `PaymentAdequacyDetailsType` |  | No |  |

## `SupplyPointContextDataInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `externalIdentifier` | `String` |  | No | Supply point external identifier. |
| `marketName` | `String` |  | No | Supply point market name. |
| `requestedSupplyStartDate` | `Date` |  | No | Requested supply start date. |
| `selectedProduct` | `SelectedProductType` |  | No | The selected product information for this supply point or None if no product is selected. |

## `TermInterface`

Represents a term in a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `TextInterface`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `textAlignment` | `Alignment` |  | No | The text alignment. |
| `textStyle` | `TextStyleV1` |  | No | The text style, i.e. header, body. |
| `value` | `String!` |  | No | The text content. |

## `TransactionType`

Transactions are a record of money being added or subtracted from the overall account balance

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | Unique identifier of the account the transaction belongs to. |
| `amount` | `Int` |  | Yes (The 'amount' field is deprecated. Use `amounts` instead for a breakdown of the relevant net, tax, and gross amounts. - Marked as deprecated on 2023-12-06. - Scheduled for removal on or after 2024-06-01.) | Gross amount including tax (when payable). Refer to the `amounts` field for a breakdown of this information. |
| `amounts` | `TransactionAmountType` |  | No | The net, tax and gross amounts for the transaction. Note: for payments and repayments, only the net amount is returned. |
| `balanceCarriedForward` | `Int` |  | No | The customer's resulting balance after this transaction has been applied, in the smallest unit of currency. |
| `billingDocumentIdentifier` | `ID` |  | No | The unique identifier for the most recent billing document linked with the transaction.Note: a transaction may be linked with multiple documents, but this field will only return the identifier for the most recent billing document. |
| `createdAt` | `DateTime` |  | No | The date time when the transaction is created. |
| `hasStatement` | `Boolean` |  | No | Returns True if the transaction is linked with a statement. |
| `id` | `ID` |  | No | Unique identifier for the transaction. |
| `isAccountCharge` | `Boolean` |  | Yes (The 'isAccountCharge' field is deprecated. This information is provided by the __typename introspection query. - Marked as deprecated on 2020-06-19. - Scheduled for removal on or after 2022-11-15.) | Deprecated. |
| `isAccountPayment` | `Boolean` |  | Yes (The 'isAccountPayment' field is deprecated. This information is provided by the __typename introspection query. - Marked as deprecated on 2020-06-19. - Scheduled for removal on or after 2022-11-15.) | Deprecated. |
| `isCredit` | `Boolean` |  | Yes (The 'isCredit' field is deprecated. This information is provided by the __typename introspection query. - Marked as deprecated on 2020-06-19. - Scheduled for removal on or after 2022-11-15.) | Deprecated. |
| `isHeld` | `Boolean` |  | No | Whether the statement this transaction is on has been held. A held statement is not sent to a customer automatically, but is instead marked for manual attention by operations staff. Returns False if a statement is not linked with the transaction. |
| `isIssued` | `Boolean` |  | No | Whether this transaction has been issued on any billing document.Note: Look for the most recently issued transaction instead of looking through all transactions as some accounts may have initial transactions that were not issued.This will return False if the transaction is not associated with any billing documents. |
| `isReversed` | `Boolean!` |  | No |  |
| `note` | `String` |  | No | Returns the note field value for the transaction, which contains additional info. |
| `postedDate` | `Date` |  | No | Date when the transaction was posted to the account. |
| `reasonCode` | `String` |  | No | Returns the reason. |
| `statementId` | `ID` |  | Yes (The 'statementId' field is deprecated. Use `billingDocumentIdentifier` instead. - Marked as deprecated on 2023-11-30. - Scheduled for removal on or after 2024-06-01.) | Returns None if a statement is not linked with the transaction. |
| `title` | `String` |  | No | Human-readable title describing the transaction. |

