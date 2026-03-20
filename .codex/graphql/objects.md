# Objects

Total `OBJECT` types: **1081**

## `A629DetailsAcceptance`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `atrTariff` | `String` |  | No | ATR tariff code (extracted from <tarifapeaje>). |
| `clientValidationResult` | `Boolean` |  | No | Result of client validation (extracted from <resvalidacioncliente>). |
| `cnae` | `String` |  | No | CNAE (extracted from <cnae>). |
| `consumptionProfile` | `String` |  | No | Consumption profile (extracted from <perfil>). |
| `cutPoint` | `Boolean` |  | No | Cut point (extracted from <puntocortado>). |
| `distributorCode` | `String` |  | No | Distributor code (extracted from <distribuidor>). |
| `essentialIndicator` | `String` |  | No | Essential supply point indicator (extracted from <essentialtype>). |
| `pressureDesignRange` | `String` |  | No | Pressure range (extracted from <rangopresiondiseno>). |
| `protectedType` | `String` |  | No | Protected type (extracted from <protectedtype>). |
| `qmax` | `Decimal` |  | No | Contracted peak flow (extracted from <qmax>). |
| `resultCode` | `String` |  | No | Result code (extracted from <codresultado>). |
| `resultDescription` | `String` |  | No | Result description (extracted from <descresultado>). |
| `satelliteConnectedIndicator` | `Boolean` |  | No | Satellite plant connection indicator (extracted from <indconectadoplantasatelite>). |
| `telemetry` | `Boolean` |  | No | Telemetry (extracted from <contelemedida>). |
| `turRights` | `Boolean` |  | No | TUR right (extracted from <derechotur>). |

## `A629DetailsRejection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `reasonCode` | `String` |  | No | Rejection reason code. |
| `reasonDescription` | `String` |  | No | Rejection description. |
| `resultCode` | `String` |  | No | Result code (extracted from <codresultado>). |
| `resultDescription` | `String` |  | No | Result description (extracted from <descresultado>). |

## `APIBrownout`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `apiType` | `APIType` |  | No | The API type effected by this brownout. |
| `disablesRequestsTo` | `NonEmptyString` |  | No | For GraphQL APIs this will be a field identifier in the format <ParentType>.≤fieldName>, for REST APIs this will be an endpoint. |
| `endsAt` | `NonEmptyString` |  | No | The iso formatted datetime at which this brownout will end. |
| `startsAt` | `NonEmptyString` |  | No | The iso formatted datetime at which this brownout will take effect. |
| `status` | `APIBrownoutStatus` |  | No | The current status of this brownout. |

## `APIBrownoutConnection`

Paginator of API brownouts.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[APIBrownoutEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `APIBrownoutEdge`

A Relay edge containing a `APIBrownout` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `APIBrownout` |  | No | The item at the end of the edge |

## `APICallType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `context` | `JSONString` |  | No | Storage for the API client to submit any contextual information. |
| `correlationId` | `String!` |  | No | The request's correlation id. |
| `createdAt` | `DateTime!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `inputData` | `JSONString` |  | No | Input data for the API call if any. |
| `operationName` | `String!` |  | No | Free field for the API caller to categorise their own operation name. This field can be used to filter entries on the UI. |
| `response` | `JSONString` |  | No | The response from the API call if any. |

## `APIExceptionConnectionTypeConnection`

Paginator of API exceptions.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[APIExceptionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `APIExceptionConnectionTypeEdge`

A Relay edge containing a `APIExceptionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `APIExceptionType` |  | No | The item at the end of the edge |

## `APIExceptionEventType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `category` | `String!` |  | No | The category of the event. |
| `context` | `JSONString` |  | No | A JSON context to be provided with the event, if any. |
| `createdAt` | `DateTime!` |  | No |  |
| `description` | `String` |  | No | A description of the event. |
| `eventType` | `String!` |  | No | The type of the event. |
| `id` | `ID!` |  | No |  |

## `APIExceptionNoteType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `body` | `String!` |  | No | The content of the API Exception note. |
| `createdAt` | `DateTime!` |  | No | Timestamp of when the API Exception note was created. |
| `id` | `ID!` |  | No | The ID of the API Exception note. |

## `APIExceptionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | The account number provided to the exception. |
| `apiCalls` | `[APICallType]` |  | No | The API calls associated with this exception if any. |
| `assignedUser` | `AssignedUserType` |  | No | The user assigned to handle this exception if any. |
| `category` | `APIExceptionCategories` |  | No | Category associated with this exception. |
| `channel` | `String!` |  | No | Free field for the API caller to categorise a channel. This could be (but not limited to) the client's team that calleded the API, the name of the 'flow' the call belongs to, etc. |
| `context` | `JSONString` |  | No | Storage for the API client to submit any contextual information. |
| `createdAt` | `DateTime!` |  | No |  |
| `customerContact` | `String` |  | No | The customer contact provided to the exception. |
| `events` | `[APIExceptionEventType]` |  | No | The events associated with this exception if any. |
| `externalIdentifier` | `String!` |  | No | External identifier submitted by the API client to track this exception on their end. |
| `id` | `ID!` |  | No |  |
| `keyDate` | `Date` |  | No | The key date associated with the exception, if available. |
| `notes` | `[APIExceptionNoteType]` |  | No | Notes associated with this exception if any. |
| `operationsTeam` | `OperationsTeamType` |  | No | The operations team assigned to this exception if any. |
| `priority` | `APIExceptionPriority!` |  | No | The current priority for the API exception. |
| `resolutionStatus` | `APIExceptionResolutionStatus!` |  | No | The current resolution status for the API exception. |
| `resolutionType` | `APIExceptionResolutionType!` |  | No | The current resolution type for the API exception. |
| `supplyPointIdentifier` | `String` |  | No | The supply point identifier provided to the exception. |
| `tags` | `[APIExceptionTags]` |  | No | Tags associated with this exception if any. |
| `userId` | `BigInt` |  | No | The user id provided to the exception. |

## `ATRTariff`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `validFrom` | `DateTime` |  | No | The supply point ATR effective date. |
| `value` | `String` |  | No | The supply point ATR value. |

## `AcceptGoodsQuote`

The possible errors that can be raised are: - KT-CT-8223: Unauthorized. - KT-CT-8201: Received an invalid quoteId. - KT-CT-8224: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `goodsPurchase` | `GoodsPurchase` |  | No | Goods purchase created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AcceptOfferForQuoting`

Accept a quoting offer in an offer group. The possible errors that can be raised are: - KT-CT-12402: Unable to accept offer. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `offer` | `OfferType` |  | No | Accepted quoting offer. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `Account`

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
| `billingPostcode` | `String!` |  | No |  |
| `billingSubName` | `String` |  | No | The billing sub name of the account. |
| `bills` | `BillConnectionTypeConnection` | `includeBillsWithoutPDF: Boolean = false, includeOpenStatements: Boolean = false, includeHeldStatements: Boolean = false, includeHistoricStatements: Boolean = true, onlyCurrentEmail: Boolean = false, ledgerNumber: String, fromDate: Date, toDate: Date, issuedFromDate: Date, issuedToDate: Date, orderBy: BillsOrderBy = FROM_DATE_DESC, offset: Int, before: String, after: String, first: Int, last: Int` | No | Fetch issued bills (invoices/statements) for the account. |
| `brand` | `String` |  | No | The brand of the account. |
| `business` | `BusinessType` |  | No | Business info related to a business account. |
| `businessType` | `BusinessTypeOptions` |  | Yes (The 'businessType' field is deprecated. Use `business.businessType` instead - Marked as deprecated on 2022-03-09. - Scheduled for removal on or after 2024-01-01.) | The company type of a business account. |
| `campaigns` | `[AccountCampaignType]` |  | No | The campaigns associated with an account. |
| `canModifyPayments` | `CanModifyPaymentsType` |  | No | Data about whether or not an account can modify their payments. |
| `canRequestRefund` | `Boolean` |  | No | Whether the account can request a credit refund. |
| `commsDeliveryPreference` | `CommsDeliveryPreference` |  | No | The method the account has specified they prefer we contact them. |
| `communicationDeliveryPreference` | `String` |  | Yes (The 'communicationDeliveryPreference' field is deprecated. Use `commsDeliveryPreference` instead - Marked as deprecated on 2022-05-27. - Scheduled for removal on or after 2024-01-01.) |  |
| `complaints` | `ComplaintConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The complaints associated with an account. |
| `consents` | `[ConsentType!]!` |  | No | Consents linked to this account. |
| `contributionAgreements` | `[ContributionAgreementType]` |  | No | Contribution agreements for account. |
| `createdAt` | `DateTime` |  | No | The datetime that the account was originally created. |
| `currentGiftCreditLeftInEur` | `Decimal` |  | No | The amount of gift credit left in the account supplementary ledgers in euros. |
| `debtCollectionProceedings` | `[DebtCollectionProceedingType]` |  | No | Debt collection proceedings for account. |
| `directDebitInstructions` | `DirectDebitInstructionConnectionTypeConnection` | `statuses: [DirectDebitInstructionStatus], before: String, after: String, first: Int, last: Int` | No | The direct debit instructions of the account |
| `documentAccessibility` | `DocumentAccessibilityChoices` |  | No | The document accessibility preference of the account. |
| `events` | `AccountEventConnectionTypeConnection` | `eventTypes: [AccountEventType], before: String, after: String, first: Int, last: Int` | No | The account events that were recorded for the account. |
| `fileAttachments` | `[AccountFileAttachment]` |  | No | Files attached to this account. |
| `hasSolarWallet` | `Boolean` |  | Yes (The 'hasSolarWallet' field is deprecated. Use 'account.ledgers' instead and filter on the SOLAR_WALLET_LEDGER 'ledgerType' field. - Marked as deprecated on 2025-02-10. - Scheduled for removal on or after 2025-08-10.) | Whether the account has solar wallet activated. |
| `holderName` | `String` |  | No | The name of the contract holder. |
| `holderNif` | `String` |  | No | The nif of the contract holder. |
| `id` | `ID!` |  | No |  |
| `isInHardship` | `Boolean` |  | No | True if there is an active Hardship Agreement for this account. False otherwise. |
| `ledgers` | `[LedgerType]` | `ledgerNumber: String, includeDebtLedgers: Boolean = true` | No | Ledgers provide the foundation of bookkeeping functionality. Similar to a bank account, they allow us to keep track of financial activity on a particular customer account. |
| `loggedRepresentative` | `PersonalInformation` |  | No | Logged representative information. |
| `marketSupplyAgreements` | `AgreementConnection` | `id: ID, active: Boolean = false, before: String, after: String, first: Int, last: Int` | No | Retrieve all market supply agreements under this account. Note that when `active` is set to false it actually means 'return both active and inactive agreements'. |
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
| `properties` | `[PropertyType]` | `activeFrom: DateTime` | No | Properties linked to the account now and in the future. |
| `provisionalTransactions` | `ProvisionalTransactionConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No |  |
| `references` | `[AccountReferenceType]` |  | No | Account references linked to this account. |
| `referrals` | `ReferralConnectionTypeConnection` | `status: ReferralStatus, before: String, after: String, first: Int, last: Int` | No | The referrals created by this account. |
| `referralsCreated` | `Int` |  | No | Number of referrals created by this account. |
| `reminders` | `AccountReminderConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The reminders associated with an account. |
| `repayments` | `AccountRepaymentConnectionTypeConnection` | `statuses: [AccountRepaymentStatusOptions], before: String, after: String, first: Int, last: Int` | No | The repayments that have been requested for this account. |
| `requestRefundEligibility` | `RequestRefundEligibilityType` | `ledgerNumber: String` | No | Details about the eligibility status for requesting a refund. |
| `rewards` | `[RewardType]` |  | No | The rewards applied to this account. |
| `solarWalletAvailableCredit` | `Int` |  | Yes (The 'solarWalletAvailableCredit' field is deprecated. Use 'account.ledgers.balance' instead. - Marked as deprecated on 2025-02-10. - Scheduled for removal on or after 2025-08-10.) | Solar wallet available credit. |
| `solarWalletLedgers` | `[SolarWalletLedgers]` |  | Yes (The 'solarWalletLedgers' field is deprecated. Use 'account.ledgers.creditTransferPermissionsData.toTargetLedgers' instead. - Marked as deprecated on 2025-02-10. - Scheduled for removal on or after 2025-08-10.) | Solar wallet information. |
| `spanishLedgers` | `[LedgerWithPaymentsInstructions]` | `ledgerNumber: String` | No | Retrieve different supplementary ledgers used in Spain market. |
| `splitBillingAddress` | `[String]` |  | No | List of billing address lines. |
| `status` | `AccountStatus` |  | No | The current status of the account. |
| `transactions` | `TransactionConnectionTypeConnection` | `transactionTypes: [TransactionTypeFilter] = [], transactionTypesExcluded: [TransactionTypeFilter] = [], ledgerNumber: String, includeAllLedgers: Boolean, fromDate: Date, toDate: Date, orderBy: TransactionsOrderBy = POSTED_DATE_DESC, offset: Int, before: String, after: String, first: Int, last: Int` | No | Fetch transactions that have taken place on the account. |
| `urn` | `String` |  | No | Unique reference number from a 3rd party enrolment. |
| `users` | `[EspAccountUserType!]!` |  | No |  |

## `AccountApplicationConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountApplicationConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountApplicationConnectionTypeEdge`

A Relay edge containing a `AccountApplicationConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `AccountApplicationType` |  | No | The item at the end of the edge |

## `AccountApplicationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `coolingOffEndDate` | `Date` |  | No | Last day of the cooling off period. Barring changes or objections, the account will be gained on the next business day after this date. This value will only be returned for current applications. |
| `dateOfSale` | `Date` |  | No | Date at which this account decided to switch to us. |
| `isMigrated` | `Boolean` |  | No | Whether this account application represents a migration into the current system or a regular gain. |
| `migrationSource` | `String` |  | No | The source system for a migrated account. This could be the previous supplier or the previous account management system. |
| `preferredSsd` | `Date` |  | No | Preferred supply start date. If null, it means ASAP. |
| `salesChannel` | `String!` |  | No |  |
| `salesSubchannel` | `String` |  | No | The sales subchannel used when signing up. This could for example be a price comparison site. |
| `status` | `AccountApplicationStatus!` |  | No |  |

## `AccountBalanceTransferType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountCharge` | `AccountChargeType` |  | No | Debit details. |
| `accountCredit` | `AccountCreditType` |  | No | Credit details. |
| `id` | `ID` |  | No | Balance transfer ID. |
| `reason` | `String` |  | No | The reason for the balance transfer. |

## `AccountBillingInfo`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `billingAddress` | `String` |  | No | Account billing address. |
| `billingAddressLine1` | `String!` |  | No |  |
| `billingAddressLine2` | `String!` |  | No |  |
| `billingAddressLine3` | `String!` |  | No |  |
| `billingAddressLine4` | `String!` |  | No |  |
| `billingAddressLine5` | `String!` |  | No |  |
| `billingCountryCode` | `String!` |  | No |  |
| `billingName` | `String!` |  | No | Name for this account. If one exists, the billing name of the portfolio will prepend this. |
| `billingPostcode` | `String!` |  | No |  |
| `canModifyPayments` | `CanModifyPaymentsType` |  | No | Data about whether or not an account can modify their payments. |
| `id` | `ID!` |  | No |  |
| `ledgers` | `[LedgerWithPaymentsInstructions]` | `ledgerNumber: String` | No | Retrieve different supplementary ledgers used in Spain market. |
| `marketSupplyAgreements` | `AgreementConnection` | `id: ID, active: Boolean = false, before: String, after: String, first: Int, last: Int` | No | Retrieve all market supply agreements under this account. Note that when `active` is set to false it actually means 'return both active and inactive agreements'. |
| `number` | `String!` |  | No |  |
| `properties` | `[PropertyType]` | `activeFrom: DateTime` | No | Properties linked to the account now and in the future. |
| `splitBillingAddress` | `[String]` |  | No | List of billing address lines. |
| `status` | `String!` |  | No |  |

## `AccountCampaignConnectionTypeConnection`

Paginator of Account Campaigns

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountCampaignConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountCampaignConnectionTypeEdge`

A Relay edge containing a `AccountCampaignConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `AccountCampaignType` |  | No | The item at the end of the edge |

## `AccountCampaignType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `campaignExpiryDate` | `Date` |  | No | The date on which the associated campaign itself concludes. |
| `expiryDate` | `Date` |  | No | The date on which the account's participation in the campaign ends. |
| `name` | `String` |  | No | The name of the campaign. |
| `slug` | `String` |  | No | The slug of the campaign. |
| `startDate` | `Date` |  | No | The date that the account's link to the campaign started. |

## `AccountChargeMetadataType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `data` | `JSONString` |  | No | A JSON object containing unstructured data about the account charge. |
| `updatedAt` | `DateTime` |  | No | The date and time the metadata was last updated. |

## `AccountChargeType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cclAmount` | `BigInt` |  | No | The climate change levy amount of the charge. |
| `displayNote` | `String` |  | No | The display note for the charge. |
| `grossAmount` | `BigInt` |  | No | The gross amount of the charge. |
| `id` | `ID` |  | No | The ID of the account charge. |
| `metadata` | `AccountChargeMetadataType` |  | No | JSON metadata containing unstructured data about the account charge. |
| `netAmount` | `BigInt` |  | No | The net amount of the charge. |
| `note` | `String` |  | No | The note for the charge. |
| `reason` | `String` |  | No | The reason for the charge. |
| `salesTaxAmount` | `BigInt` |  | No | The sales tax amount of the charge. |

## `AccountConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountConnectionTypeEdge`

A Relay edge containing a `AccountConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `Account` |  | No | The item at the end of the edge |

## `AccountCreditMetadataType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `data` | `JSONString!` |  | No |  |
| `updatedAt` | `DateTime!` |  | No |  |

## `AccountCreditType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `grossAmount` | `BigInt!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `metadata` | `AccountCreditMetadataType` |  | No |  |
| `netAmount` | `BigInt!` |  | No |  |
| `note` | `String!` |  | No |  |
| `reason` | `String!` |  | No |  |
| `salesTaxAmount` | `BigInt!` |  | No |  |

## `AccountEventConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountEventConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountEventConnectionTypeEdge`

A Relay edge containing a `AccountEventConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `AccountEvent` |  | No | The item at the end of the edge |

## `AccountFileAttachment`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `category` | `String!` |  | No |  |
| `fetchUrl` | `String` |  | No |  |
| `filename` | `String!` |  | No |  |
| `id` | `ID!` |  | No | The ID of the object |
| `isReady` | `Boolean` |  | No | Is the file ready for use / downloadable? |
| `isUploaded` | `Boolean` |  | No | Is the file uploaded to S3? |
| `sizeInBytes` | `Int` |  | No |  |

## `AccountFileAttachmentConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountFileAttachmentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountFileAttachmentConnectionTypeEdge`

A Relay edge containing a `AccountFileAttachmentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `AccountFileAttachment` |  | No | The item at the end of the edge |

## `AccountIoEligibility`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isEligibleForIo` | `Boolean` |  | No | Whether account is eligible to register devices with Intelligent Octopus or not. |

## `AccountLoyaltyPointsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `loyaltyPoints` | `Int` |  | No | The number of loyalty points the account (or user with the given id) has. |
| `totalMonetaryAmount` | `Int` |  | No | The net monetary value of the loyalty points in the currency's sub-units. |

## `AccountNoteType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `body` | `String!` |  | No |  |
| `createdAt` | `DateTime!` |  | No |  |
| `isPinned` | `Boolean!` |  | No |  |
| `unpinAt` | `DateTime` |  | No |  |

## `AccountPaymentConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountPaymentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountPaymentConnectionTypeEdge`

A Relay edge containing a `AccountPaymentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `AccountPaymentType` |  | No | The item at the end of the edge |

## `AccountPaymentInfo`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `electricityIban` | `String` |  | No | Billing address postcode. |
| `gasIban` | `String` |  | No | Billing address postcode. |
| `holderName` | `String` |  | No | Instruction holder's name. |
| `postcode` | `String` |  | No | Billing address postcode. |
| `splitAddress` | `[String]` |  | No | List of billing address lines. |

## `AccountPaymentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `BigInt!` |  | No | Amount of payment in the currency's minor unit |
| `id` | `ID!` |  | No |  |
| `paymentDate` | `Date!` |  | No | The date this payment is scheduled to be debited |
| `paymentInstruction` | `PaymentInstructionType` |  | No | The payment instruction that was used to make this payment. |
| `reference` | `String!` |  | No |  |
| `status` | `AccountPaymentStatusOptions` |  | No | The current status of the payment. |
| `surchargeAmount` | `Int` |  | No | Surcharge amount generated by this payment. |
| `transactionType` | `AccountPaymentTransactionTypeChoices` |  | No | The transaction type of the payment. |

## `AccountReferenceType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account!` |  | No |  |
| `createdAt` | `DateTime!` |  | No |  |
| `namespace` | `String!` |  | No |  |
| `updatedAt` | `DateTime!` |  | No |  |
| `value` | `String!` |  | No |  |

## `AccountReminder`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `content` | `String` |  | No | Reminder content. |
| `dueAt` | `DateTime` |  | No | When the reminder is due. |
| `reminderType` | `AccountReminderTypes` |  | No | The reminder type. |

## `AccountReminderConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountReminderConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountReminderConnectionTypeEdge`

A Relay edge containing a `AccountReminderConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `Reminder` |  | No | The item at the end of the edge |

## `AccountRepaymentConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountRepaymentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountRepaymentConnectionTypeEdge`

A Relay edge containing a `AccountRepaymentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `AccountRepaymentType` |  | No | The item at the end of the edge |

## `AccountRepaymentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `BigInt!` |  | No | Amount of payment in the currency's minor unit |
| `id` | `ID!` |  | No |  |
| `paymentDate` | `Date!` |  | No | The date this payment is scheduled to be debited |
| `status` | `AccountRepaymentStatusOptions` |  | No | The current status of the repayment. |

## `AccountSearchItemType`

A single account search hit

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | The account found. |
| `score` | `Decimal` |  | No | How well the account matched the search terms. |

## `AccountUserCommsPreferences`

Information about the preferences set up for a user.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `emailFormat` | `EmailFormats` |  | No | What format the user would like to receive their emails in. |
| `fontSizeMultiplier` | `Float` |  | No | This setting allows the user to adjust the default font size of the communications sent to them. |
| `isOptedInMeterReadingConfirmations` | `Boolean` |  | No | Whether the user has opted in to receive meter reading confirmation emails. |
| `isOptedInToClientMessages` | `Boolean` |  | No | Whether a user has opted in to receive messages from the client or client group. For example, for Octopus Energy this describes whether a user is opted in to offers from Octopus Investments. |
| `isOptedInToLifeSupportCall` | `Boolean` |  | No | Whether the user is opted in to life support call. |
| `isOptedInToOfferMessages` | `Boolean` |  | No | Whether a user has opted in to receive messages offering discounts or other services not directly related to the services the client provides. |
| `isOptedInToRecommendedMessages` | `Boolean` |  | No | Whether a user has opted in to receive messages we recommend they read, but are not vital to the utilities the client provides. For example, these could be reminders that the client will take a payment. |
| `isOptedInToSmsMessages` | `Boolean` |  | No | Whether the user has opted in to receive SMS messages. |
| `isOptedInToThirdPartyMessages` | `Boolean` |  | No | Whether a user has opted in to receive messages from the client's preferred third parties. |
| `isOptedInToUpdateMessages` | `Boolean` |  | No | Whether a user has opted in to receive messages updating them on client activities. |
| `isUsingInvertedEmailColours` | `Boolean` |  | No | Whether a user has opted to have inverted colours in their emails. This is currently only relevant to the Octopus Energy brand, whose emails have a dark background by default. |
| `preferredHoldMusic` | `Songs` |  | No | Song which will be used as hold music for the user. |
| `smsOptInLastChangeDate` | `DateTime` |  | No | The date the SMS opt-in was last changed. |

## `AccountUserConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AccountUserConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AccountUserConnectionTypeEdge`

A Relay edge containing a `AccountUserConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `EspAccountUserType` |  | No | The item at the end of the edge |

## `AccountUserConsents`

Information about the consents for an account user.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `consents` | `[ConsentType!]!` |  | No | Consents linked to this user. |

## `AccountUserDetailType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isSensitive` | `Boolean` |  | No | Whether the value is sensitive and encrypted. |
| `namespace` | `String` |  | No | The namespace for the property. |
| `value` | `String` |  | No | The property value. |

## `AccountUserMeta`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `firstFamilyName` | `String` |  | No | Customer's first family name. |
| `nif` | `String` |  | No | Customer's national ID number. |
| `secondFamilyName` | `String` |  | No | Customer's second family name. |

## `AccountUserPermission`

Holds information about a specific permission.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `permission` | `String` |  | No | The short name of the permission. |

## `AccountUserRoleType`

The role a user has in association with one account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `role` | `RoleString` |  | No | The account role. |
| `user` | `EspAccountUserType!` |  | No |  |

## `ActorType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `username` | `String` |  | No | Username of the Actor. |

## `ActualizeContractOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contract` | `Contract` |  | No | The contract actualized. |

## `AddBusinessToSegmentMutation`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-11111: Segment does not exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `businessSegmentPeriod` | `BusinessSegmentPeriodType` |  | No | The business segment period that was created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AddCampaignToAccount`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-7427: No campaign found with given slug. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `campaignAdded` | `Boolean` |  | No | Whether the campaign was successfully added. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AddChildToProperty`

Add a child property to a parent property in a hierarchy. If the child is already in the hierarchy with a different parent, it will be reparented. If the child is already a child of the specified parent, this operation is idempotent and does nothing. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-6622: Unauthorized. - KT-CT-6634: Unable to add child to property. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `child` | `PropertyType` |  | No | The child property that was added to the parent. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AddItemsToRiskList`

Add new items to risk list. The possible errors that can be raised are: - KT-CT-12105: Risk list item addition failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `riskIdentifiers` | `[RiskListItemType]` |  | No | List of successfully added risk identifiers. |

## `AddNoteToInkConversation`

The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `note` | `InkNote` |  | No | The ink conversation note. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AddParentToProperty`

Add a parent property to a child property in a hierarchy. If the child is already in the hierarchy with a different parent, it will be reparented. If the child is already a child of the specified parent, this operation is idempotent and does nothing. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-6622: Unauthorized. - KT-CT-6635: Unable to add parent to property. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `parent` | `PropertyType` |  | No | The parent property that was added to the child. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AddPortfolioReference`

Add a reference to an existing portfolio. The possible errors that can be raised are: - KT-CT-9403: Received an invalid portfolioId. - KT-CT-9410: Conflicting portfolio reference. - KT-CT-9408: Invalid portfolio number format. - KT-CT-9409: Invalid portfolio reference. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AddProperty`

Add a property to an account. The possible errors that can be raised are: - KT-CT-6623: Unauthorized. - KT-CT-6629: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `property` | `PropertyType` |  | No | The property that was added to the account. |

## `AddPropertyToHierarchy`

Add a property to a hierarchy as a root node. If the property is already a root node in the hierarchy, this operation is idempotent. If the property is already in the hierarchy as a child, an error will be raised. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-6633: Property is already in the hierarchy as a child. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `property` | `PropertyType` |  | No | The property that was added to the hierarchy. |

## `AddSignupReferralOnAccount`

Create a referral scheme reward for an organization. This allows businesses to issue rewards based on a referral scheme. The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6729: This scheme cannot be applied to given account. - KT-CT-6710: Unable to create referral. - KT-CT-6728: This referral scheme's usage is at capacity. - KT-CT-6712: Invalid reference. - KT-CT-6713: Referring and referred account brands do not match. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountReferral` | `ReferralType` |  | No | The created account referral instance. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AddStorylineToInkConversation`

The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-7651: Only one storyline entry can be marked as the root cause. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `storyline` | `InkStoryline` |  | No | The storyline that was added to the conversation. |

## `AddUserToPortfolio`

The possible errors that can be raised are: - KT-CT-5461: Invalid role code. - KT-CT-5462: Invalid user number format. - KT-CT-5463: Unauthorized. - KT-CT-9407: Unauthorized. - KT-CT-9408: Invalid portfolio number format. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AddressOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `countryCode` | `String` |  | No | Country code of billing address. |
| `line1` | `String` |  | No | Line 1 of address. |
| `line2` | `String` |  | No | Line 2 of address. |
| `line3` | `String` |  | No | Line 3 of address. |
| `line4` | `String` |  | No | Line 4 of address. |
| `line5` | `String` |  | No | Line 5 of address. |
| `postcode` | `String` |  | No | Postcode of billing address. |

## `AdjustmentMechanism`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `average` | `Float` |  | No | Adjustment mechanism mean. |
| `averageWithTaxes` | `Float` |  | No | Adjustment mechanism mean with taxes. |
| `period` | `String` |  | No | Adjustment mechanism month period. |
| `units` | `String` |  | No | Adjustment mechanism units. |

## `AffiliateAudioRecordingPresignedPostType`

Metadata returned when generating a pre-signed post URL for an affiliate.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `bucket` | `String!` |  | No | The S3 bucket. |
| `fields` | `JSONString!` |  | No | The fields to be included in the pre-signed post. |
| `key` | `String!` |  | No | The S3 bucket key. |
| `preSignedUrl` | `String!` |  | No | The pre-signed S3 URL. |

## `AffiliateLinkType`

Affiliate link for the organization.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contactEmail` | `String!` |  | No |  |
| `contactName` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `isBusiness` | `Boolean!` |  | No |  |
| `landingUrl` | `String!` |  | No |  |
| `organisation` | `AffiliateOrganisationType` |  | No | Affiliate Organisation. |
| `subdomain` | `String!` |  | No |  |
| `trainingStatus` | `LinkTrainingStatus!` |  | No |  |

## `AffiliateOrganisationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `allowAlternativePaymentMethods` | `Boolean` |  | No | Is this partner allowed to specify payment methods other than Direct Debit in the import csv or API. |
| `canRegisterBusinessMeterPoints` | `Boolean` |  | No | Are meter point registrations limited for profile classes 1 and 2 for registrations from csv or API. |
| `canRegisterCustomersWithoutEmailAddress` | `Boolean` |  | No | Allow registration requests with customers without an email address. |
| `canRegisterPortfolioAccounts` | `Boolean` |  | No | Allow registration requests with exiting account user emails to add to the portfolio belonging to the account user. |
| `canRenewTariffs` | `Boolean` |  | No | Allow performing tariff renewals via API. |
| `canUseIvrSupportApi` | `Boolean` |  | No | Allow this partner access to the IVR support API (modify their own IVR handling through third party 'IVR Flow Editor'). |
| `contactEmail` | `String!` |  | No | The primary contact email for the organisation. |
| `defaultAccountType` | `AccountTypeChoices` |  | No | Default Account Type. |
| `id` | `ID!` |  | No |  |
| `isFieldSalesOnlyProduct` | `Boolean` |  | No | Restrict to field-sales-only products? This is only allowed for the 'field-sales' and 'events' sales channels. |
| `name` | `String!` |  | No |  |
| `number` | `String` |  | No | Unique identifier for the organisation in the format O-XXXXXXXX. |
| `salesChannel` | `SalesChannelChoices` |  | Yes (The 'salesChannel' field is deprecated. Please use salesChannelCode instead. - Marked as deprecated on 2025-07-17. - Scheduled for removal on or after 2025-10-17.) | Sales Channel. |
| `salesChannelCode` | `String` |  | No | Sales Channel Code. |
| `skipMeterPointAddressValidation` | `Boolean` |  | No | Allow this partner to skip validation that ensures all meter points belong to the same address. |

## `AffiliateProductType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `numMaxAgreements` | `Int` |  | No | The maximum number of agreements for the product. |
| `numTotalAgreements` | `Int` |  | No | The total number of agreements for the product. |
| `productName` | `String` |  | No | The name of the product. |

## `AffiliateSessionType`

A tracked session for the affiliate link.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No |  |
| `ipAddress` | `String` |  | No |  |
| `link` | `AffiliateLinkType` |  | No | Affiliate Link. |
| `queryParams` | `JSONString!` |  | No |  |
| `userAgent` | `String!` |  | No |  |

## `AgentCallCenterStatusType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | The ID of the agent call center status. |
| `mostRecentCallId` | `Int` |  | No | The ID of the most recent call handled by the agent. If the agent status is BUSY then this will be the ID of the current call. |
| `status` | `String` |  | No | The current status of the agent in the call center. |
| `updatedAt` | `DateTime` |  | No | The timestamp when the status was last updated. |

## `Agreement`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | The account this agreement belongs to. |
| `agreedFrom` | `DateTime` |  | No | The datetime the agreement was entered. |
| `agreedTo` | `DateTime` |  | No | The datetime the agreement was terminated. |
| `details` | `AgreementDetails` |  | No | Spanish specific details of the agreement. |
| `id` | `Int` |  | No | The ID of the agreement. |
| `isRevoked` | `Boolean` |  | No | Whether the agreement is revoked. |
| `product` | `Product` |  | No | The agreement's product. |
| `rescissionDeadlineAt` | `DateTime` |  | No | The deadline datetime for rescinding the agreement. |
| `validFrom` | `DateTime` |  | No | The start datetime of the agreement. |
| `validTo` | `DateTime` |  | No | The end datetime of the agreement. |

## `AgreementConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AgreementEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AgreementDetails`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cnae` | `String` |  | No | The agreement CNAE which defines the use of the supply point. |
| `contractualMaxPower` | `[Decimal]` |  | No | The agreement contractual_max_power. |
| `customerRequestedStartDate` | `DateTime` |  | No | The date when the customer requested to start. |
| `estimatedConsumption` | `Int` |  | No | The agreement estimated_consumption. |
| `foreseenStartDate` | `DateTime` |  | No | The date when the agreement is foreseen to start. |
| `ieeExemption` | `Int` |  | No | The agreement iee_exemption which only applies to electricity supply_points. |
| `iehExemption` | `Int` |  | No | The agreement ieh_exemption which only applies to gas supply_points. |
| `monthlyValueAddedTax` | `TaxTypes` |  | No | The value added tax applied to the current month. |

## `AgreementEdge`

A Relay edge containing a `Agreement` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `CommonAgreementType` |  | No | The item at the end of the edge |

## `AgreementRescissionType`

Details of an agreement rescission

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreement` | `Agreement!` |  | No |  |
| `createdAt` | `DateTime!` |  | No |  |
| `failureReason` | `String!` |  | No |  |
| `flowReference` | `String` |  | No |  |
| `id` | `ID!` |  | No |  |
| `status` | `AgreementRescissionStatus` |  | No | The current status of the agreement rescission. |
| `stepName` | `String` |  | No |  |
| `stepSlug` | `String` |  | No |  |
| `updatedAt` | `DateTime!` |  | No |  |

## `AgreementRolloverType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `actualSendDate` | `Date` |  | No |  |
| `agreement` | `Agreement!` |  | No |  |
| `createdAt` | `DateTime!` |  | No |  |
| `expectedSendDate` | `Date!` |  | No |  |
| `failureReason` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `number` | `String!` |  | No |  |
| `params` | `JSONString!` |  | No |  |
| `quoteRequests` | `[MarketSupplyQuoteRequestType!]!` |  | No |  |
| `rolledOnTo` | `Agreement` |  | No |  |
| `rolloverType` | `AgreementRolloverRolloverType!` |  | No |  |
| `status` | `AgreementRolloverStatus!` |  | No |  |
| `suppressComms` | `Boolean!` |  | No |  |
| `tags` | `[String]` |  | No | List of tag names associated with this agreement rollover. |
| `updatedAt` | `DateTime!` |  | No |  |

## `AllocationIntentionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `allocationAmount` | `Int!` |  | No | The amount of the transaction that has been allocated to the billing document. A positive amount indicates money received from the customer (payments, credits). A negative amount indicates money paid to the customer (repayments). |
| `allocationReason` | `String` |  | No | Reason for the allocation intention. |
| `transactionAmount` | `Int!` |  | No | The amount of the transaction. A positive amount indicates money received from the customer (payments, credits). A negative amount indicates money paid to the customer (repayments). |
| `transactionId` | `Int!` |  | No | ID of the allocated transaction. |
| `transactionType` | `TransactionTypes!` |  | No | The type of the transaction. |

## `AllocationType`

Represents an allocation of a fulfilment to an obligation.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int!` |  | No | The amount of the allocation (in minor currency units), unsigned. |
| `fulfilment` | `FulfilmentType!` |  | No | The fulfilment that is allocated. |

## `AllowRepaymentSubmission`

Allow a repayment to be submitted. The possible errors that can be raised are: - KT-CT-3944: Account repayment does not exist. - KT-CT-3945: Unable to allow a repayment to be submitted. - KT-CT-3950: The provided reason text is too long. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `repaymentId` | `ID` |  | No | The repayment ID. |
| `repaymentIntervention` | `RepaymentInterventionType` |  | No | Resulting Repayment Intervention details. |

## `AlreadyLinkedError`

Returned when an account already has a LINE account linked to it.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `type` | `LineLinkErrorType!` |  | No | The type of error that occurred. |

## `AmendPayment`

The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-3970: The account cannot amend payments. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payment` | `AccountPaymentType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AnimationType`

A media element containing an animation, such as a Lottie.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accessibilityHidden` | `Boolean` |  | No | Whether the element is hidden from view. |
| `accessibilityLabel` | `String` |  | No | Accessible description of the element. |
| `horizontalAlignment` | `Alignment` |  | No | The horizontal alignment of the media. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `mediaUrl` | `String!` |  | No | The resource URL of the media. |
| `typename` | `String` |  | No | The name of the object's type. |
| `width` | `ItemSizeType` |  | No | The measurement of the element. |

## `AnnualStatementConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AnnualStatementConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AnnualStatementConnectionTypeEdge`

A Relay edge containing a `AnnualStatementConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `AnnualStatementType` |  | No | The item at the end of the edge |

## `AnnualStatementType`

Annual statements that are sent to the account. They summarize important information about usage and tariffs.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No |  |
| `pdfUrl` | `String` |  | No |  |
| `periodEndsAt` | `DateTime!` |  | No |  |
| `periodStartsAt` | `DateTime!` |  | No |  |

## `AnnulmentBillingDocumentType`

An annulment is a billing document that annuls another billing document.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `annulledBillingDocumentId` | `Int!` |  | No | ID of the billing document annulled by this annulment. |
| `firstIssued` | `DateTime` |  | No | First time the annulment was issued. |
| `id` | `Int!` |  | No | ID for the annulment billing document. |
| `pdfUrl` | `String` |  | No | URL to the PDF of the annulment. |

## `AppSessionConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[AppSessionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `AppSessionConnectionTypeEdge`

A Relay edge containing a `AppSessionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `AppSessionType` |  | No | The item at the end of the edge |

## `AppSessionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No |  |
| `addressLine1` | `String!` |  | No |  |
| `addressLine2` | `String!` |  | No |  |
| `addressLine3` | `String!` |  | No |  |
| `addressLine4` | `String!` |  | No | Post town |
| `addressLine5` | `String!` |  | No | County |
| `createdAt` | `DateTime!` |  | No |  |
| `id` | `UUID!` |  | No |  |
| `isArchived` | `Boolean` |  | No |  |
| `link` | `AffiliateLinkType!` |  | No |  |
| `locationAt` | `DateTime` |  | No |  |
| `locationHorizontalAccuracy` | `Int` |  | No | The location accuracy level in meters |
| `locationLatitude` | `Decimal` |  | No |  |
| `locationLongitude` | `Decimal` |  | No |  |
| `outcomes` | `[OutcomeType]` |  | No | A list of outcomes associated with the app session. |
| `postcode` | `String!` |  | No |  |
| `salesMode` | `AppSessionSalesMode` |  | No |  |
| `startedAt` | `DateTime!` |  | No |  |
| `stoppedAt` | `DateTime!` |  | No |  |
| `type` | `AppSessionType` |  | No |  |
| `updatedAt` | `DateTime!` |  | No |  |

## `ApproveRepayment`

The possible errors that can be raised are: - KT-CT-3934: Repayment request already approved. - KT-CT-3935: Repayment request cannot be paid. - KT-CT-3959: Unauthorized. - KT-CT-3973: Repayment request is not in a state to be approved. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `repayment` | `AccountRepaymentType` |  | No | The approved repayment. |

## `AssessCollectionProcessRecordForPause`

Assess the Collection Process for pause and pause or unpause it based on the assessment. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessProcessed` | `AssessCollectionProcessRecordForPauseOutputType` |  | No | Details of collection process after running the pause assessment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AssessCollectionProcessRecordForPauseOutputType`

Output for assessing a Collection process for pause.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isPaused` | `Boolean` |  | No | The pause status of the collection process. |
| `number` | `String` |  | No | The number of the collection process record. |

## `AssignInkBucket`

The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-7613: The Ink bucket was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `bucket` | `InkBucket!` |  | No | The bucket that the conversation will be assigned to. |
| `conversation` | `InkConversation!` |  | No | The conversation that will be assigned to the bucket. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AssignSupplyPointToEstimationGroup`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-13601: Estimation Group does not exist. - KT-CT-13602: Supply Point already has an Estimation Group. - KT-CT-13603: Supply Point does not exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `supplyPointEstimationGroup` | `AssignedSupplyPointEstimationGroupType` |  | No | The created supply point estimation group mapping. |

## `AssignedSupplyPointEstimationGroupType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `estimationGroupCode` | `String!` |  | No | The code of the estimation group. |
| `supplyPointExternalId` | `String!` |  | No | The external identifier of the assigned supply point. |

## `AssignedUserType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No | The ID of the assigned user. |
| `username` | `String!` |  | No | The username of the assigned user. |

## `AssistanceAgreementType`

A single Assistance Agreement.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `activeFrom` | `Date` |  | No | The start datetime of the agreement. |
| `activeTo` | `Date` |  | No | The end datetime of the agreement, if any. |
| `assistanceType` | `String` |  | No | The type of assistance provided by the agreement. |

## `AssociateCallWithAccount`

The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-4178: No account found with given account number. - KT-CT-11808: Unable to associate account to call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `call` | `InboundCallType` |  | No | The call. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AssociateItemToCollectionProcess`

Associate an item to collection process record The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11205: Item already associated to collection process. - KT-CT-11216: Invalid extra_details for associated item type. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessAssociatedItem` | `AssociateItemToCollectionProcessOutputType` |  | No | Item associated to the collection process. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `AssociateItemToCollectionProcessOutputType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `itemId` | `ID` |  | No | Associated item identifier. |
| `number` | `String` |  | No | The number of the collection process record. |

## `AttachmentType`

Represents a file to attach to a communication

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `filename` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `temporaryUrl` | `String` |  | No | Temporary URL at which the attachment is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). |

## `AudioRecordingType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `appSession` | `AppSessionType` |  | No | The app session associated with this audio recording. |
| `contentType` | `String!` |  | No |  |
| `createdAt` | `DateTime!` |  | No |  |
| `duration` | `Float!` |  | No |  |
| `fileSize` | `Int!` |  | No |  |
| `id` | `UUID!` |  | No |  |
| `s3Bucket` | `String!` |  | No |  |
| `s3Key` | `String!` |  | No |  |
| `startedAt` | `DateTime!` |  | No |  |
| `stoppedAt` | `DateTime!` |  | No |  |
| `updatedAt` | `DateTime!` |  | No |  |

## `AuthFlow`

A step where the user must complete an auth flow.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `authorizationUri` | `String` |  | No | The URL to redirect the user to for authorization. |
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `redirectUri` | `String` |  | No | The URI where the auth flow is going to redirect back to at the end. |

## `AuthorizedApplication`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientId` | `String` |  | No | The client ID of the application. |
| `name` | `String` |  | No | The name of the application. |

## `AwardLoyaltyPoints`

Award Loyalty Points. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9202: Loyalty Points adapter not configured. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-9212: Points exceed maximum limit. - KT-CT-9219: Loyalty points user not found. - KT-CT-9221: Idempotency key already used on ledger entry. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `ledgerEntry` | `LoyaltyPointLedgerEntryType` |  | No | The ledger entry for the awarded loyalty points. |
| `pointsAwarded` | `Int` |  | No | The number of loyalty points that were awarded. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `BackendScreenEvent`

Returns an Action to perform, e.g. a screen to load. BackendScreenEvents are specific types of Action which trigger a mutation in the Kraken backend. They return an action (any type), such as a ScreenActionType (which is then used to load the next screen). Any action registered in the registry should really be an "event" with some side-effect in the backend. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-8002: No event found. - KT-CT-8003: Event has no execute function. - KT-CT-8004: Error executing event in the backend. - KT-CT-8007: Incorrect or missing parameters for backend screen event. - KT-GB-9310: Account ineligible for joining Octoplus. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `action` | `ActionType` |  | No | An action to perform. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `BackendScreenEventActionType`

An action which triggers some event in the Kraken backend.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `eventId` | `String!` |  | No | The ID of the event to trigger. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `params` | `[BackendScreenParam]!` |  | No | List of key-value pairs to pass as parameters to the event. |
| `typeName` | `String` |  | No | The name of the action object's type. |
| `typename` | `String` |  | No | The name of the object's type. |

## `BackendScreenParam`

A key-value pair (both Strings) which is passed as a parameter to a screen.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `key` | `String!` |  | No |  |
| `value` | `String!` |  | No |  |

## `BankDetailsValidationResult`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `areValid` | `Boolean!` |  | No | Indicates whether the provided bank details are valid. |
| `message` | `String` |  | No | Provides additional information about validation result. |

## `BatteryTelemetry`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `connectionStatus` | `ConnectionStatus` |  | No | Whether the battery is currently connected (online/offline). |
| `powerInKw` | `Decimal` |  | No | The current power being used to charge the battery, or discharging from the battery, in kW. A negative value indicates this power is being used to charge the battery; a positive value indicates power is being discharged from the battery. |
| `stateOfCharge` | `Decimal` |  | No | The current state of charge (SoC) of the battery (0-100). |

## `BespokeRateConfigurationType`

The BespokeRateConfiguration term.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `schedules` | `[BespokeRateScheduleType]` |  | No | The schedules for the bespoke rate configuration. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `BespokeRateItemType`

Item for the BespokeRateConfiguration term.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `pricePerUnit` | `Decimal` |  | No | The price per unit for the bespoke rate item. |
| `rateSpecificationCode` | `String` |  | No | The rate specification code for the bespoke rate item. |
| `variantProfile` | `VariantProfile` |  | No | The variant profile for the bespoke rate item. |

## `BespokeRateScheduleType`

Schedule for the BespokeRateConfiguration term.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `items` | `[BespokeRateItemType]` |  | No | The items for the bespoke rate schedule. |
| `productCode` | `String` |  | No | The product code for the bespoke rate schedule. |
| `supplyPointIdentifier` | `String` |  | No | The external identifier of the supply point this schedule targets. |
| `validFrom` | `DateTime` |  | No | The datetime the schedule of bespoke rates is valid from. |
| `validTo` | `DateTime` |  | No | The datetime the schedule of bespoke rates is valid to. |

## `BillCharge`

A charge to the customer from the energy retailer.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amounts` | `TransactionAmountType` |  | No | The net, tax and gross amounts for the transaction. Note: for payments and repayments, only the net amount is returned. |
| `consumption` | `Consumption` |  | No | If this charge is for consumption of a good or service, this field will contain details of how much was consumed. Omitted in cases where the charge is not for consumption, or where consumption information is not available (e.g. for some older records). |
| `createdAt` | `DateTime` |  | No | The date time when the transaction is created. |
| `detail` | `ChargeDetail` |  | No | Supporting information about this charge (if any is available). |
| `id` | `ID` |  | No | The unique identifier for the transaction. |
| `note` | `String` |  | No | Returns the note field value for the transaction, which contains additional info. |
| `postedDate` | `Date` |  | No | The date the transaction was posted. |
| `reasonCode` | `String` |  | No | Returns the reason. |
| `title` | `String` |  | No | A user readable string that indicates what this transaction relates to. |

## `BillConnectionTypeConnection`

This field is a connection type. Connections are used to implement [cursor based pagination](https://graphql.org/learn/pagination/#pagination-and-edges).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[BillConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `BillConnectionTypeEdge`

A Relay edge containing a `BillConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `BillInterface` |  | No | The item at the end of the edge |

## `BillCredit`

A credit to the customer from the energy retailer.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amounts` | `TransactionAmountType` |  | No | The net, tax and gross amounts for the transaction. Note: for payments and repayments, only the net amount is returned. |
| `createdAt` | `DateTime` |  | No | The date time when the transaction is created. |
| `id` | `ID` |  | No | The unique identifier for the transaction. |
| `note` | `String` |  | No | Returns the note field value for the transaction, which contains additional info. |
| `postedDate` | `Date` |  | No | The date the transaction was posted. |
| `reasonCode` | `String` |  | No | Returns the reason. |
| `title` | `String` |  | No | A user readable string that indicates what this transaction relates to. |

## `BillDueDateType`

Represents bill due dates to be applied in a contract. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `BillPayment`

A payment from the customer to the energy supplier.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amounts` | `TransactionAmountType` |  | No | The net, tax and gross amounts for the transaction. Note: for payments and repayments, only the net amount is returned. |
| `createdAt` | `DateTime` |  | No | The date time when the transaction is created. |
| `id` | `ID` |  | No | The unique identifier for the transaction. |
| `note` | `String` |  | No | Returns the note field value for the transaction, which contains additional info. |
| `postedDate` | `Date` |  | No | The date the transaction was posted. |
| `reasonCode` | `String` |  | No | Returns the reason. |
| `title` | `String` |  | No | A user readable string that indicates what this transaction relates to. |

## `BillRefund`

A refund to the customer from the energy supplier.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amounts` | `TransactionAmountType` |  | No | The net, tax and gross amounts for the transaction. Note: for payments and repayments, only the net amount is returned. |
| `createdAt` | `DateTime` |  | No | The date time when the transaction is created. |
| `id` | `ID` |  | No | The unique identifier for the transaction. |
| `note` | `String` |  | No | Returns the note field value for the transaction, which contains additional info. |
| `postedDate` | `Date` |  | No | The date the transaction was posted. |
| `reasonCode` | `String` |  | No | Returns the reason. |
| `title` | `String` |  | No | A user readable string that indicates what this transaction relates to. |

## `BillRepresentationConnectionTypeConnection`

A connection that can provide links to the representations of a bill.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[BillRepresentationConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `BillRepresentationConnectionTypeEdge`

A Relay edge containing a `BillRepresentationConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `BillRepresentationType` |  | No | The item at the end of the edge |

## `BillRepresentationType`

representations are associated with a bill files and can be used to provide additional information to the customer.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The type of representation. |
| `filename` | `String` |  | No | The name of the file. |
| `temporaryUrl` | `String` |  | No | The `TemporaryURL` type represents a temporary URL at which the file is available. It is intended for redirection purposes, NOT persistence in any form. (e.g. inclusion in emails or the body of a web page). |
| `temporaryUrlExpiresAt` | `DateTime` |  | No | The expiry datetime field of the temporary URL. |
| `version` | `Int` |  | No | The version of the representation. |

## `BillTransactionConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[BillTransactionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `BillTransactionConnectionTypeEdge`

A Relay edge containing a `BillTransactionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `BillTransactionType` |  | No | The item at the end of the edge |

## `BillingAttachmentConnectionTypeConnection`

A connection that can provide links to the attachments of the bill.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[BillingAttachmentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `BillingAttachmentConnectionTypeEdge`

A Relay edge containing a `BillingAttachmentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `BillingAttachmentType` |  | No | The item at the end of the edge |

## `BillingAttachmentType`

Attachments are associated with a bill files and can be used to provide additional information to the customer.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `filename` | `String` |  | No | The name of the file. |
| `temporaryUrl` | `String` |  | No | The `TemporaryURL` type represents a temporary URL at which the file is available. It is intended for redirection purposes, NOT persistence in any form. (e.g. inclusion in emails or the body of a web page). |
| `temporaryUrlExpiresAt` | `DateTime` |  | No | The expiry datetime field of the temporary URL. |

## `BillingDocumentIssuanceFrequencyType`

Represents billing document issuance frequency to be applied during a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `frequency` | `String` |  | No | Billing frequency. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term can be amended after creation. |
| `multiplier` | `Int` |  | No | Multiplier applied to the frequency. |
| `periodStartDay` | `Int` |  | No | Start day of the billing period. |
| `periodStartMonth` | `Int` |  | No | Start month of the billing period. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `BillingDocumentPositionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `allocationIntentions` | `[AllocationIntentionType]!` |  | No | Allocation intentions for the billing document. |
| `allocations` | `[AllocationType]!` |  | No | Allocations for the billing document. |
| `dueDate` | `Date!` |  | No | The date when the payment is due for the billing document. |
| `expectedAmount` | `Int!` |  | No | The expected amount for the billing document (in minor currency units). |
| `remainingAmount` | `Int!` |  | No | The amount that remains to be paid for the billing document (in minor currency units). |

## `BillingOptionsType`

Information about an account's billing schedule.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `currentBillingPeriodEndDate` | `Date` |  | No | The date on which the current billing cycle will end. Null if the account is on flexible billing. |
| `currentBillingPeriodStartDate` | `Date` |  | No | The date on which the current billing cycle started. |
| `isFixed` | `Boolean!` |  | No | If true, this account is billed on specific day of a regular cycle. If false, the billing schedule is flexible, depending on when meter readings are submitted. |
| `nextBillingDate` | `Date` |  | No | The next date on which this account will next be billed. This is the same as the start date for their next bill cycle. Null if the account is on flexible billing. |
| `periodLength` | `AccountBillingOptionsPeriodLength` |  | No |  |
| `periodLengthMultiplier` | `Int` |  | No |  |
| `periodStartDay` | `Int` |  | No | The day of the month on which the account's billing period should start. |

## `BlockRepaymentSubmission`

Block a repayment from being submitted. The possible errors that can be raised are: - KT-CT-3944: Account repayment does not exist. - KT-CT-3946: Unable to block a repayment from being submitted. - KT-CT-3950: The provided reason text is too long. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `repaymentId` | `ID` |  | No | The repayment ID. |
| `repaymentIntervention` | `RepaymentInterventionType` |  | No | Resulting Repayment Intervention details. |

## `Brand`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No |  |
| `name` | `String!` |  | No |  |

## `BusinessConnectionTypeConnection`

Paginator of Businesses

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[BusinessConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `BusinessConnectionTypeEdge`

A Relay edge containing a `BusinessConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `BusinessType` |  | No | The item at the end of the edge |

## `BusinessDetailType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `key` | `String!` |  | No | The key of the business detail. |
| `value` | `String` |  | No | The value of the business detail. |

## `BusinessSegmentPeriodType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `endAt` | `DateTime` |  | No | The end date and time of the segment period. |
| `id` | `ID!` |  | No | The ID of the business segment period. |
| `segment` | `SegmentType!` |  | No | The segment associated with this period. |
| `startAt` | `DateTime` |  | No | The start date and time of the segment period. |

## `BusinessType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `billingAddress` | `RichAddressType` |  | No | The billing address of the business. |
| `businessType` | `BusinessTypeOptions` |  | No | The company type of a business account. |
| `details` | `[BusinessDetailType]` |  | No | The details of the business. |
| `id` | `ID!` |  | No | The business ID. |
| `legalAddress` | `RichAddressType` |  | No | The legal address of the business. |
| `linkedAccountNumber` | `ID!` |  | Yes (The 'linkedAccountNumber' field is deprecated. Please use 'linkedAccountNumbers' instead, businesses can be related to multiple Accounts now. - Marked as deprecated on 2025-02-05. - Scheduled for removal on or after 2025-08-01.) | Account number linked to this business. The possible errors that can be raised are: - KT-CT-11102: Business without related account. - KT-CT-1113: Disabled GraphQL field requested. |
| `linkedAccountNumbers` | `[ID]!` |  | No | Account numbers linked to this business. |
| `name` | `String!` |  | No | The business' name. |
| `number` | `String!` |  | No | The business' number. |
| `paymentMethods` | `PaymentInstructionConnectionTypeConnection` | `validAt: DateTime, statuses: [PaymentInstructionStatus], before: String, after: String, first: Int, last: Int` | No | List payment instructions owned by this business. |
| `sectors` | `[BusinessSectorString!]!` |  | No | The sectors the business operates in. |
| `segmentName` | `String` |  | No | The segment this business is assigned to. |

## `CadastreRichAddressType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `administrativeArea` | `String` |  | No | Top-level administrative subdivision, e.g. US state, AU state/territory, NZ, region, IT region, JP prefecture. ### `AU`: Australia This must be one of `NSW`, `VIC`, `QLD`, `TAS`, `ACT`, `SA`, `NT`, `WA`. For addresses not within these locations, use the value that Australia Post uses, e.g. `ACT` for the Jervis Bay Territory or `WA` for Christmas Island. |
| `asString` | `String` | `showCountry: Boolean = true, showName: Boolean = true, showPostalCode: Boolean = true` | No | The entire formatted address represented as a single string, as it would be written on an envelope. The formatting of this field may vary according to the country of the address (which may not match this Kraken installation's home country). It may also change if we update our address-formatting code or if our understanding of the correct formatting for a given country changes. Avoid parsing individual components of an address out of this field's value; use the other fields on this type instead. |
| `country` | `String` |  | No | ISO 3166-1 alpha-2 code of the country this address belongs to, e.g. `AU`, `GB`, `NZ`. |
| `deliveryPointIdentifier` | `String` |  | No | Identifier used by the local postal service for this address, e.g. AU DPID, GB postcode + Delivery Point Suffix, US Zip-9 + Delivery Point. This is the value that gets encoded in the barcode printed on the envelope by large-volume bulk mail providers. |
| `dependentLocality` | `String` |  | No | UK dependent localities, or neighbourhoods or boroughs in some other locations. |
| `geographicalId` | `String!` |  | No | Unique territory-specific identifier, i.e. cadastral reference. |
| `locality` | `String` |  | No | City or town portion of an address, e.g. US city, AU suburb/town, NZ suburb and city/town, IT comune, UK post town. |
| `name` | `String` |  | No | A personal name. |
| `organization` | `String` |  | No | The name of a business or organisation. |
| `postalCode` | `String` |  | No | Postal code (ZIP code in the US). |
| `sortingCode` | `String` |  | No | Sorting code, e.g. FR CEDEX code. This field is not used in many countries. |
| `streetAddress` | `String` |  | No | The 'street address' component. This value can (and often will) contain newline characters when appropriate. In some cases, data may appear in this field instead of the below fields; e.g. a UK post town name may appear here instead of in the `dependent_locality` field. This happens when data has been migrated from a legacy format, and that format had insufficient metadata to determine the appropriate field. If `structured_street_address` is also set, the value of this field will be a string generated from that value. |
| `structuredStreetAddress` | `GenericScalar` |  | No | The 'street address' component, in a structured format. This field stores the same value as `street_address`, but with more detail; for instance, instead of `123 Example Street` it might be `{'street_number': '123', 'street_name': 'Example', 'street_type': 'Street'}`. In many cases this will be blank; we only use this field for Krakens where we need to supply this level of granularity to some third-party service, like a bulk mail provider. The exact structure of this value depends on the country _of the address_, which is not necessarily the same as the country this Kraken is configured to serve. For addresses outside of the countries listed below, this field will be left blank. ### `AU`: Australia The following keys may be present; all are optional. All keys have string values, and their meaning is the same as their aseXML counterparts. (Note that, unlike aseXML, all keys are provided at the top level, rather than being nested.) - `flat_or_unit_type` - `flat_or_unit_number` - `floor_or_level_type` - `floor_or_level_number` - `building_or_property_name` - `location_descriptor` - `lot_number` - `house_number_1` - `house_number_suffix_1` - `house_number_2` - `house_number_suffix_2` - `street_name` - `street_type` - `street_suffix` - `postal_delivery_type` - `postal_delivery_number_prefix` - `postal_delivery_number_value` - `postal_delivery_number_suffix` ### `JP`: Japan The following keys may be present; all are optional. If keys are empty, they may be omitted from the response entirely. - `chome` - `banchi` - `go` - `edaban` - `kana_building_name` - `kanji_building_name` - `building_number` - `room_number` - `address_code` - `physical_location_identifier` - `kana_company_name` - `kanji_company_name` ### `NZ`: New Zealand The following keys may be present; all are optional. If keys are empty, they may be omitted from the response entirely. - `flat_or_unit_type` - `flat_or_unit_number` - `floor_or_level_type` - `floor_or_level_number` - `property_name` - `building_name` - `house_number_1` - `house_number_suffix_1` - `house_number_2` - `house_number_suffix_2` - `street_prefix` - `street_name` - `street_type` - `street_suffix` - `rural_delivery_number` - `mailtown` - `postal_delivery_type` - `postal_delivery_location` - `postal_delivery_number_prefix` - `postal_delivery_number_value` - `postal_delivery_number_suffix` |

## `CallMetadataItemType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `key` | `String!` |  | No | The key of the call metadata item. |
| `value` | `String!` |  | No | The value of the call metadata item. |

## `CallTagConnectionTypeConnection`

Paginator of Call Tags

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[CallTagConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `CallTagConnectionTypeEdge`

A Relay edge containing a `CallTagConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `CallTagType` |  | No | The item at the end of the edge |

## `CallTagType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | ID of the call tag. |
| `isActive` | `Boolean` |  | No | Whether the tag can currently be used to tag calls. |
| `name` | `String` |  | No | Name of the tag that will be used to identify it. |

## `CanModifyPaymentsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `canAmendPayments` | `Boolean` |  | No | Whether or not the account can amend payments. |
| `canCancelPayments` | `Boolean` |  | No | Whether or not the account can cancel payments. |

## `CancelOnSiteJobsAppointment`

The possible errors that can be raised are: - KT-CT-13001: Appointment does not exist. - KT-CT-13019: Vendor not found. - KT-CT-13017: Appointment cancellation not supported. - KT-CT-13053: Failed to cancel the appointment with the agent. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13043: Cannot update appointment as it has terminal status. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `onSiteJobsAppointment` | `OnSiteJobsAppointmentType` |  | No | The Appointment that was cancelled. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CancelPayment`

The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-3954: Payment cancellation failed. - KT-CT-3955: Payment cannot be cancelled. - KT-CT-3956: Temporary error occurred. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payment` | `AccountPaymentType` |  | No | The cancelled payment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CancelRepaymentRequest`

Cancel a repayment or refund request. The possible errors that can be raised are: - KT-CT-4231: Unauthorized. - KT-CT-3930: The repayment or refund request does not exist. - KT-CT-3931: This repayment or refund request cannot be cancelled. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `repaymentRequest` | `CancelRepaymentRequestOutputType` |  | No | The cancelled repayment/refund request. |

## `CancelRepaymentRequestOutputType`

Output from cancelling a repayment or refund request.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `requestId` | `String` |  | No | The ID of the cancelled request. |
| `status` | `RepaymentRequestStatus` |  | No | The current status of the cancelled request. |

## `CancelSmartFlexOnboarding`

Cancel onboarding of a device with SmartFlex. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `CardComponentType`

A card containing a list of items

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accessibilityHidden` | `Boolean` |  | No | Whether the element is hidden from view. |
| `accessibilityLabel` | `String` |  | No | Accessible description of the element. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `items` | `[CardItemType]!` |  | No | The list of components. |
| `typename` | `String` |  | No | The name of the object's type. |

## `CarouselItemType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cards` | `[CardComponentType]!` |  | No | The list of cards. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `typename` | `String` |  | No | The name of the object's type. |

## `CatalogProductType`

Represents a product in the catalog.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | Unique identifier of the component. |
| `customerDescription` | `String!` |  | No | Customer-facing description of the product. |
| `customerName` | `String!` |  | No | Customer-facing name of the product. |
| `identifier` | `ID!` |  | No | Unique identifier of the product. |
| `internalName` | `String!` |  | No | Internal name of the product. |
| `marketName` | `String!` |  | No | The market the product is associated with. |
| `sourceProductType` | `ProductType` |  | No | The type of product. |
| `tags` | `[TagType]` |  | No | Tags associated with this product for classification. |

## `CharacteristicOverrideConfigurationType`

Represents a characteristic override configuration term in a contract. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `overrides` | `[CharacteristicOverrideType!]!` |  | No | List of characteristic overrides. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `CharacteristicOverrideType`

An override for a specific characteristic.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `characteristic` | `CharacteristicType` |  | No | The characteristic being overridden. |
| `overrideValue` | `CharacteristicValueInterface` |  | No | The value to override the characteristic with. |
| `productCode` | `String` |  | No | Optional product code. If specified, the override applies only to this product. |

## `CharacteristicType`

A characteristic associated with a product.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | The code of the characteristic. |
| `description` | `String!` |  | No | The description of the characteristic. |
| `name` | `String!` |  | No | The name of the characteristic. |
| `values` | `[CharacteristicValueUnion]!` |  | No | The possible values for the characteristic (can be strings or integers). |

## `Charge`

A charge to the customer.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | Unique identifier of the account the transaction belongs to. |
| `amount` | `Int` |  | Yes (The 'amount' field is deprecated. Use `amounts` instead for a breakdown of the relevant net, tax, and gross amounts. - Marked as deprecated on 2023-12-06. - Scheduled for removal on or after 2024-06-01.) | Gross amount including tax (when payable). Refer to the `amounts` field for a breakdown of this information. |
| `amounts` | `TransactionAmountType` |  | No | The net, tax and gross amounts for the transaction. Note: for payments and repayments, only the net amount is returned. |
| `balanceCarriedForward` | `Int` |  | No | The customer's resulting balance after this transaction has been applied, in the smallest unit of currency. |
| `billingDocumentIdentifier` | `ID` |  | No | The unique identifier for the most recent billing document linked with the transaction.Note: a transaction may be linked with multiple documents, but this field will only return the identifier for the most recent billing document. |
| `consumption` | `Consumption` |  | No | If this charge is for consumption of a good or service, this field will contain details of how much was consumed. Omitted in cases where the charge is not for consumption, or where consumption information is not available (e.g. for some older records). |
| `createdAt` | `DateTime` |  | No | The date time when the transaction is created. |
| `detail` | `ChargeDetail` |  | No | Supporting information about this charge (if any is available). |
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

## `ChargePointVariantModelType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amperage` | `Int` |  | No | Supply amperage. Used in markets where customers are more familiar with amps than power output. |
| `integrationStatus` | `IntegrationStatus` |  | No | Shows the availability status of an integration. |
| `isIntegrationLive` | `Boolean` |  | No |  |
| `model` | `String` |  | No |  |
| `powerInKw` | `Decimal` |  | No |  |
| `variantId` | `Int` |  | No |  |

## `ChargePointVariantType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `make` | `String` |  | No |  |
| `models` | `[ChargePointVariantModelType]` |  | No |  |

## `ChargeReasonType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The charge reason code. |
| `display` | `String` |  | No | The charge reason display text. |
| `group` | `String` |  | No | The group the charge reason belongs to (if applicable). |
| `isDeprecated` | `Boolean` |  | No | Whether the charge reason is deprecated. |
| `isHidden` | `Boolean` |  | No | Whether the charge reason is hidden. |
| `isTaxExempt` | `Boolean` |  | No | Whether the charge reason is sales tax exempt. |

## `ChargesBreakdownConnectionTypeConnection`

This field is a connection type. Connections are used to implement [cursor based pagination](https://graphql.org/learn/pagination/#pagination-and-edges).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ChargesBreakdownConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ChargesBreakdownConnectionTypeEdge`

A Relay edge containing a `ChargesBreakdownConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ChargesBreakdownType` |  | No | The item at the end of the edge |

## `ChargesBreakdownType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `charge` | `Int` |  | No | Charge in minor currency. |
| `periodEnd` | `Date` |  | No | The end date of the period the charge is for (exclusive). |
| `periodStart` | `Date` |  | No | The start date of the period the charge is for (inclusive). |

## `CheckCreditRisk`

The possible errors that can be raised are: - KT-CT-3921: Account not found. - KT-CT-5518: Account user not found. - KT-CT-5523: Invalid account or account user. - KT-ES-10701: Default property not found. - KT-ES-10702: Credit check only available for domestic accounts. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `passedCreditCheck` | `Boolean` |  | No | Indicates whether the user has passed the credit risk check. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CheckResultType`

GraphQL type for check result.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `context` | `String` |  | No | Additional context about the check. |
| `name` | `String` |  | No | Name of the check. |
| `status` | `CheckResultStatus` |  | No | Status of the check. |

## `CloseActionType`

Closes the screen.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accessibilityHidden` | `Boolean` |  | No | Whether the element is hidden from view. |
| `accessibilityLabel` | `String` |  | No | Accessible description of the element. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `typeName` | `String` |  | No | The name of the action object's type. |
| `typename` | `String` |  | No | The name of the object's type. |

## `CloseDCAProceeding`

The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11602: Could not find DCA with that name. - KT-CT-11603: Could not stop debt collection proceeding. - KT-CT-11604: Active debt collection proceeding does not exist for account. - KT-CT-11605: Multiple active Proceeding's found for same agency and campaign on account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dcaProceedingClosureStatus` | `DCAProceedingClosureStatus` |  | No | Whether the closure could be applied. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CloseInkConversation`

The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `conversation` | `InkConversation` |  | No | The conversation that was closed. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CloseInkLiveChatConversation`

The possible errors that can be raised are: - KT-CT-7616: Not yet implemented. - KT-CT-7643: The Live Chat was not found. - KT-CT-7644: Ink Live Chat conversation not found. - KT-CT-7652: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `liveChatConversation` | `InkLiveChatConversation` |  | No | The live chat conversation. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CloseOpenPrintBatch`

Close the Open Print Batch if any. The possible errors that can be raised are: - KT-CT-9010: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `printBatch` | `PrintBatchType` |  | No |  |

## `CollateralRequiredType`

Represents required collaterals to be applied in a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int!` |  | No | Amount set up as collateral as condition for account creation. |
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `interestPolicy` | `String` |  | No | Type of interest policy of required collateral. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `reason` | `String!` |  | No | Reason for setting up required collateral. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `CollectDeposit`

Collect deposit for the given account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-5711: No collection is required. - KT-CT-5712: Deposit agreement does not exist or has not been accepted. - KT-CT-5713: Payment instruction is not usable. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payment` | `CollectDepositOutput` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CollectDepositOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `paymentDate` | `Date` |  | No |  |
| `status` | `CollectDepositStatusChoices` |  | No |  |

## `CollectPayment`

The possible errors that can be raised are: - KT-CT-3932: Invalid data. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payment` | `AccountPaymentType` |  | No | Details about the collected payment. Note that we might not be able to collect the payment (e.g. if there is no usable payment instruction), in which case the status of the returned payment might be failed or cancelled. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `Collection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `String` |  | No | The description of the collection. |
| `fields` | `[FunnelField]` |  | No | The fields of the collection. |
| `name` | `String` |  | No | The name of the collection. |
| `order` | `Int` |  | No | The order of the collection. |

## `CollectionProcessDetailsType`

Collection process details type

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `associatedItems` | `[CollectionProcessRecordAssociatedItemType]` |  | No | Items associated to the collection process. |
| `collectionProcessRecordNumber` | `String` |  | No | The collection process record number. |
| `collectionProcessType` | `CollectionProcessTypes` |  | No | The type of the collection process (ACCOUNT, LEDGER, or BILLING_DOCUMENT). |
| `completionType` | `String` |  | No | What kind of completion happened. |
| `isActive` | `Boolean` |  | No | The active status of the collection process. |
| `isComplete` | `Boolean` |  | No | The completion status of the collection process. |
| `isPaused` | `Boolean` |  | No | The pause status of the collection process. |
| `pausedDays` | `Int` |  | No | Total number of days collection process were on pause. |
| `targetObjectIdentifier` | `String` |  | No | The identifier of the target object (account number, ledger number, or billing document ID) based on the collection process type. |

## `CollectionProcessEventOutputType`

Output for creating a collection process event.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `number` | `String` |  | No | The number of the collection process record this event belongs to. |

## `CollectionProcessPauseStatusRecord`

Collection process pause record

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `name` | `String` |  | No | Collection process pause name. |
| `pausedAt` | `DateTime` |  | No | Start of pause period. |
| `reason` | `String` |  | No | Reason for pausing. |
| `resumedAt` | `DateTime` |  | No | End of pause period. |
| `resumedReason` | `String` |  | No | Reason for ending pause period. |

## `CollectionProcessRecordAssociatedItemType`

Item associated to collection process

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `extraDetails` | `JSONString` |  | No | Additional details of the item. |
| `itemReference` | `String!` |  | No | Unique reference of item. |
| `itemType` | `String!` |  | No | Type of item. |
| `occurredAt` | `DateTime!` |  | No | Datetime of when action that resulted in item happened. |

## `CollectiveBillType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `BillingAttachmentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No |  |
| `billType` | `BillTypeEnum` |  | No | The type of the bill. |
| `constituents` | `ConstituentConnection` | `before: String, after: String, first: Int, last: Int` | No | Constituents of the bill. |
| `fromDate` | `Date` |  | No | The date of the bill is covered from. |
| `id` | `ID` |  | No | The ID of the bill. |
| `issuedDate` | `Date` |  | No | The date the bill was sent to the customer. |
| `reversalsAfterClose` | `StatementReversalsAfterClose!` |  | No | How many charges have been reversed after the close date. |
| `temporaryUrl` | `String` |  | Yes (The 'temporaryUrl' field is deprecated. This field is deprecated. Use the 'attachments' field instead. - Marked as deprecated on 2024-09-16. - Scheduled for removal on or after 2025-09-01.) | Requesting this field generates a temporary URL at which bill is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). This field can raise an error with errorClass NOT_FOUND if the bill document has not been created/issued yet. This field is deprecated use 'attachments' field instead. |
| `toDate` | `Date` |  | No | The date of the bill is covered to. |

## `CombinedRateLimitInformation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fieldSpecificRateLimits` | `FieldSpecificRateLimitInformationConnectionTypeConnection!` | `fields: [String], before: String, after: String, first: Int, last: Int` | No | Information about the current state of the rate limiting for rate limited fields at the time of the request. |
| `pointsAllowanceRateLimit` | `PointsAllowanceRateLimitInformation` |  | No | Information about points-allowance rate limit for viewer. |

## `CommenceDCAProceeding`

The possible errors that can be raised are: - KT-CT-11606: Debt Collection Agency cannot use campaign. - KT-CT-11601: Cannot start collection proceeding, proceeding for this account already exists. - KT-CT-11602: Could not find DCA with that name. - KT-CT-11607: Invalid ledger number for debt collection proceeding. - KT-CT-11608: Ledger does not belong to account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dcaProceedingCommencementStatus` | `DCAProceedingCommencementStatus` |  | No | Whether the commencement could be applied. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CommonAgreementType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account!` |  | No | The account associated with the agreement. |
| `agreedAt` | `DateTime` |  | No |  |
| `agreedFrom` | `DateTime` |  | No | The datetime the agreement was entered. |
| `agreedTo` | `DateTime` |  | No | The datetime the agreement was terminated. |
| `characteristicValues` | `[CharacteristicValueInterface]` | `at: DateTime` | No | The characteristic values associated with the agreement. |
| `id` | `ID!` |  | No |  |
| `isActive` | `Boolean` |  | No | Whether the agreement is currently active. |
| `isRevoked` | `Boolean` |  | No | Whether the agreement is revoked. |
| `params` | `JSONString` |  | No | General parameters providing additional information about the agreement. |
| `product` | `SupplyProductType` |  | No | The product associated with the agreement. |
| `rescissionDeadlineAt` | `DateTime` |  | No | The deadline until which the customer is allowed to rescind this agreement. If it is null, rescission is not permitted. |
| `supplyPoint` | `SupplyPointType!` |  | No | The agreement's supply point. |
| `terminatedAt` | `DateTime` |  | No |  |
| `validFrom` | `DateTime!` |  | No |  |
| `validTo` | `DateTime` |  | No |  |

## `ComplaintConnectionTypeConnection`

Paginator of Complaint type.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ComplaintConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ComplaintConnectionTypeEdge`

A Relay edge containing a `ComplaintConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ComplaintType` |  | No | The item at the end of the edge |

## `ComplaintContactConnectionTypeConnection`

Paginator of Complaint contact type.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ComplaintContactConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ComplaintContactConnectionTypeEdge`

A Relay edge containing a `ComplaintContactConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ComplaintContactType` |  | No | The item at the end of the edge |

## `ComplaintContactType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `actionTaken` | `String!` |  | No | Description of action taken. |
| `createdAt` | `DateTime!` |  | No | Created at for contact. |
| `email` | `String` |  | No | Complaint email. |
| `landline` | `String` |  | No | Complaint landline. |
| `mobile` | `String` |  | No | Complaint phone. |
| `name` | `String!` |  | No | Complainant name. |
| `preferredCommunicationMethod` | `String` |  | No | Complaint preferred method. |
| `status` | `String!` |  | No | Status of complaint. |
| `summary` | `String` |  | No | Complaint summary. |

## `ComplaintType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `assigneeId` | `ID` |  | No | Complaint Assignee. |
| `contacts` | `ComplaintContactConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Complaint contacts. |
| `creationDate` | `Date` |  | No | Complaint creation date. |
| `id` | `ID!` |  | No |  |
| `resolutionDate` | `Date` |  | No | Complaint resolution date. |
| `subtype` | `String` |  | No | Complaint subtype. |
| `type` | `String` |  | No | Complaint type. |

## `CompleteAuthFlowForSmartFlexOnboarding`

Complete the auth flow step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `CompleteSelectVehicleOrChargePointForSmartFlexOnboarding`

Complete the select vehicle or charge point step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `CompleteStandalonePayment`

Completes an initiated standalone payment. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3823: Unauthorized. - KT-CT-3974: Unauthorized. - KT-CT-3975: Unable to complete standalone payment. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payment` | `CompleteStandalonePaymentOutput` |  | No | The completed standalone payment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CompleteStandalonePaymentOutput`

Result of the complete standalone payment operation.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `status` | `PaymentIntentCompletionStatus!` |  | No | The status of the standalone payment. |

## `CompleteTeslaSetupVirtualKeyForSmartFlexOnboarding`

Complete the Tesla setup virtual key onboarding step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `CompleteUserActionRequiredForSmartFlexOnboarding`

Complete the UserActionRequired step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `CompleteUserInputRequiredForSmartFlexOnboarding`

Complete the UserInputRequired step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `ComponentListType`

A list of components which comprise a screen. This is a legacy type; GenericBackendScreen should be preferred. This is because API clients should not need to explicitly query for screen attributes like `items` - these fields are embedded in the screenData field.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accessibilityHidden` | `Boolean` |  | No | Whether the element is hidden from view. |
| `accessibilityLabel` | `String` |  | No | Accessible description of the element. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `items` | `[ItemType]!` |  | Yes (The 'items' field is deprecated. Access `items` via `screenData` instead. - Marked as deprecated on 2024-07-02. - Scheduled for removal on or after 2024-08-01.) | The list of components. |
| `name` | `String!` |  | No | The name of the screen. |
| `refreshFrequency` | `Int` |  | No | The refresh / polling frequency in milliseconds. |
| `screenData` | `String` |  | No | Serialized JSON representation of the screen. |
| `typename` | `String` |  | No | The name of the object's type. |

## `ConfirmDoubleOptIn`

Confirm a requested consent. This mutation will update the value of the consent associated with the provided token to ACCEPTED. The possible errors that can be raised are: - KT-CT-9016: Consent management not enabled. - KT-CT-9020: Invalid consent expiring token. - KT-CT-9021: Consent expiring token not found. - KT-CT-9022: Consent for given token already accepted. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `consent` | `ConsentType` |  | No | The consent that was created or updated. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `ConnectAiAgentToCall`

The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11815: Unable to connect a call to an AI agent. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `call` | `InboundCallType` |  | No | The call the AI agent was connected to. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `ConsentOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The code of the consent type. |
| `value` | `String` |  | No | The value to update the consent to. |

## `ConsentType`

A consent given by a signing identity for a consent type.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | Unique code given to this consent type. |
| `id` | `BigInt!` |  | No | id of the consent. |
| `type` | `ConsentTypeType` |  | No | The type of the consent. |
| `value` | `ConsentValue!` |  | No | Value of the consent. |

## `ConsentTypeType`

A type of consent that a signing identity can accept or reject to.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | Unique code given to this consent type. |
| `defaultValue` | `ConsentValue!` |  | No | Default value of the consent type. |
| `description` | `String!` |  | No | Description of the consent type. |
| `name` | `String!` |  | No | Name of the consent type. |

## `ConstituentConnection`

This field is a connection type. Connections are used to implement [cursor based pagination](https://graphql.org/learn/pagination/#pagination-and-edges).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ConstituentEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ConstituentEdge`

A Relay edge containing a `Constituent` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ConstituentInterface` |  | No | The item at the end of the edge |

## `Consumption`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `endDate` | `Date` |  | No | End date of the consumption period. |
| `quantity` | `Decimal` |  | No | Amount of energy or resource consumed. |
| `startDate` | `Date` |  | No | Start date of the consumption period. |
| `supplyCharge` | `Int` |  | No | Supply charge amount in minor currency units. |
| `unit` | `ConsumptionUnit` |  | No |  |
| `usageCost` | `Int` |  | No | Cost for the consumption usage in minor currency units. |

## `ConsumptionBreakdownConnectionTypeConnection`

This field is a connection type. Connections are used to implement [cursor based pagination](https://graphql.org/learn/pagination/#pagination-and-edges).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ConsumptionBreakdownConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ConsumptionBreakdownConnectionTypeEdge`

A Relay edge containing a `ConsumptionBreakdownConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ConsumptionBreakdownType` |  | No | The item at the end of the edge |

## `ConsumptionBreakdownType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `charges` | `ChargesBreakdownConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Charges grouped per displayed period. |
| `marketName` | `String` |  | No | Name of the market the charges are for. |

## `Contract`

A legally binding relationship agreed with a subject (e.g. an account).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cancelledAt` | `DateTime` |  | No | Date when the contract was cancelled, null if not cancelled. |
| `identifier` | `NonEmptyString` |  | No | Unique identifier for the contract. |
| `lifecycle` | `ContractVersion` |  | No | The current version information for this contract. |
| `notes` | `[ContractNoteType]` |  | No | Notes associated with this contract. |
| `party` | `ContractParty` |  | No | The party (Account or Business) that entered into this contract. |
| `signedAt` | `DateTime` |  | No | Date when the contract was signed. |
| `status` | `ContractStatus` |  | No | The status of the contract. |
| `subject` | `[Account]` |  | No | The accounts impacted by this contract. |
| `terms` | `[TermInterface]` |  | No | The terms of the contract. |
| `title` | `String` |  | No | Title of the contract. |
| `validFrom` | `DateTime` |  | No | Date from which the contract is valid. |
| `validTo` | `DateTime` |  | No | Date until which the contract is valid, null if the contract is rolling. |

## `ContractCreationContext`

Represents a version of a contract with its effective date.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `confirmedValidityPeriod` | `ValidityPeriod` |  | No | The confirmed validity period for the associated contract. |
| `requestedValidityPeriod` | `ValidityPeriod` |  | No | The requested validity period for the associated contract. |

## `ContractCreationJourneyType`

Represents a Contract Creation Journey.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `context` | `ContractCreationContext` |  | No | The context data for the contract creation journey. |
| `contractDetails` | `ContractDetails` |  | No | The details of the associated contract. |
| `journeyType` | `ContractJourneyType` |  | No | The type of the contract journey. |
| `notes` | `[ContractNoteType]` |  | No | Notes associated with this contract journey. |
| `number` | `NonEmptyString!` |  | No | The number of the contract journey. |
| `orderReference` | `String` |  | No | The order reference associated with the contract journey. |
| `requestedAt` | `DateTime` |  | No | The date and time when the contract journey was requested. |
| `status` | `ContractJourneyStatus` |  | No | The status of the contract journey. |

## `ContractDetails`

Details of a contract excluding terms.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cancelledAt` | `DateTime` |  | No | Date when the contract was cancelled, null if not cancelled. |
| `identifier` | `NonEmptyString` |  | No | Unique identifier for the contract. |
| `lifecycle` | `ContractVersion` |  | No | The current version information for this contract. |
| `notes` | `[ContractNoteType]` |  | No | Notes associated with this contract. |
| `party` | `ContractParty` |  | No | The party (Account or Business) that entered into this contract. |
| `signedAt` | `DateTime` |  | No | Date when the contract was signed. |
| `status` | `ContractStatus` |  | No | The status of the contract. |
| `subject` | `[Account]` |  | No | The accounts impacted by this contract. |
| `title` | `String` |  | No | Title of the contract. |
| `validFrom` | `DateTime` |  | No | Date from which the contract is valid. |
| `validTo` | `DateTime` |  | No | Date until which the contract is valid, null if the contract is rolling. |

## `ContractMetaDataType`

Represents additional metadata for a contract term.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `metadata` | `JSONString` |  | No | The additional metadata of the contract. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `ContractNoteReasonType`

A reason that can be associated with a contract note.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `activityTypes` | `[ContractActivityTypeOptions]` |  | No | The contract activity types this reason applies to. |
| `description` | `String` |  | No | Human-readable description of this reason. |
| `slug` | `String` |  | No | Unique slug identifier for this reason. |

## `ContractNoteType`

A note associated with a contract or contract journey.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `activityType` | `ContractActivityTypeOptions` |  | No | The contract activity type this note is associated with. |
| `createdAt` | `DateTime` |  | No | When the note was created. |
| `note` | `String` |  | No | The content of the note. |
| `reason` | `ContractNoteReasonType` |  | No | The reason associated with this note. |

## `ContractTerminationInstigated`

Contract termination was successfully instigated.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String!` |  | No | The message to display to the user on termination instigation. |

## `ContractVersion`

Represents a version of a contract with its effective date.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `effectiveFrom` | `DateTime` |  | No | The date from which this version of the contract becomes effective. |
| `versionReference` | `Int` |  | No | The reference number for this contract version. |

## `ContractedPower`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `period1` | `Decimal` |  | No | Contracted power for period 1 in kW. |
| `period2` | `Decimal` |  | No | Contracted power for period 2 in kW. |
| `period3` | `Decimal` |  | No | Contracted power for period 3 in kW. |
| `period4` | `Decimal` |  | No | Contracted power for period 4 in kW. |
| `period5` | `Decimal` |  | No | Contracted power for period 5 in kW. |
| `period6` | `Decimal` |  | No | Contracted power for period 6 in kW. |

## `ContractedVolumeConfigurationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `periods` | `[ContractedVolumePeriodType]` |  | No | The periods for the contracted volume configuration. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `ContractedVolumePeriodType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `marketName` | `String` |  | No | The market name the contracted volume applies to. |
| `unit` | `String` |  | No | The unit for the commodity provided by the contracted volume. |
| `validFrom` | `DateTime` |  | No | The datetime the period the contracted volume is valid from. |
| `validTo` | `DateTime` |  | No | The datetime the period the contracted volume is valid to. |
| `value` | `Decimal` |  | No | The decimal value of the quantity provided by the contracted volume. |

## `ContributionAgreementType`

A single Contribution Agreement.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `activeFrom` | `DateTime` |  | No | The start datetime of the agreement. |
| `activeTo` | `DateTime` |  | No | The end datetime of the agreement, if any. |
| `amount` | `Int` |  | No | The amount contributed per interval. Note, this is in the smallest domination that the currecy support. e.g. Pence, Cents, Yen, etc. |
| `contributionScheme` | `ContributionSchemeType` |  | No | The scheme to which the agreement contributes. |
| `id` | `ID!` |  | No |  |
| `interval` | `Interval` |  | No | The frequency of contributions. |
| `periods` | `ContributionPeriodConnection` | `before: String, after: String, first: Int, last: Int` | No | The periods over which contributions have been made. |

## `ContributionPeriodConnection`

Pagination for contribution periods.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ContributionPeriodEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ContributionPeriodEdge`

A Relay edge containing a `ContributionPeriod` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ContributionPeriodType` |  | No | The item at the end of the edge |

## `ContributionPeriodType`

A single Contribution Period.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreement` | `ContributionAgreementType!` |  | No |  |
| `fulfilledAt` | `DateTime` |  | No | When the contribution was fulfilled |
| `id` | `ID!` |  | No |  |
| `periodFrom` | `DateTime` |  | No | The datetime the marks the beginning of the period. |
| `periodTo` | `DateTime` |  | No | The datetime the marks the end of the period. |

## `ContributionSchemeType`

A single Contribution Scheme.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptingContributions` | `Boolean!` |  | No | Is this scheme currently accepting contributions? |
| `code` | `String!` |  | No |  |
| `displayName` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `taxable` | `Boolean!` |  | No | Are contributions to this scheme taxable? |

## `CoordinatesType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `latitude` | `Float` |  | No |  |
| `longitude` | `Float` |  | No |  |

## `CoreSiteworksAppointmentType`

An appointment linked to a request

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `appointmentDate` | `Date` |  | No | The date of the appointment in local time. |
| `createdAt` | `DateTime!` |  | No |  |
| `externalReference` | `String!` |  | No |  |
| `id` | `UUID!` |  | No |  |
| `jobType` | `String` |  | No | The type of job for the appointment. |
| `status` | `OnSiteJobsAppointmentStatus` |  | No | The current status of the appointment. |
| `timeSlotEnd` | `Time` |  | No | The end time of the appointment slot in local time. |
| `timeSlotStart` | `Time` |  | No | The start time of the appointment slot in local time. |

## `CoreSiteworksRequestConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[CoreSiteworksRequestConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `CoreSiteworksRequestConnectionTypeEdge`

A Relay edge containing a `CoreSiteworksRequestConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `CoreSiteworksRequestType` |  | No | The item at the end of the edge |

## `CoreSiteworksRequestType`

A Siteworks Request

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `appointments` | `[CoreSiteworksAppointmentType]` |  | No | List of appointments linked to this request. |
| `createdAt` | `DateTime!` |  | No |  |
| `id` | `UUID!` |  | No |  |
| `lastStatusUpdateAt` | `DateTime!` |  | No | When the request status was last updated. |
| `marketSupplyPoints` | `SupplyPointConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of supply points on request. |
| `reason` | `String!` |  | No |  |
| `status` | `String!` |  | No |  |

## `CostOfChargeType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `costOfChargeId` | `String` |  | No |  |
| `isSmartCharge` | `Boolean` |  | No |  |
| `krakenflexDeviceId` | `String` |  | No |  |
| `reportDate` | `Date` |  | No |  |
| `totalConsumption` | `Float` |  | No | Consumption in kWh. |
| `totalCostExclTax` | `Float` |  | No | Cost in pence (excl. tax). |
| `totalCostInclTax` | `Float` |  | No | Cost in pence (incl. tax). |

## `CreateAPICall`

The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `apiCall` | `APICallType` |  | No | The created APICall. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAPIException`

The possible errors that can be raised are: - KT-CT-7801: Received an invalid operationsTeamId. - KT-CT-7802: The external identifier already exists. - KT-CT-7805: Too many tags associated with this API Exception. - KT-CT-7806: Cannot create duplicate tags for the same API exception. - KT-CT-7811: Received an invalid assignedUserId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `apiException` | `APIExceptionType` |  | No | The created APIException. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAPIExceptionEvent`

The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `apiExceptionEvent` | `APIExceptionEventType` |  | No | The created APIExceptionEvent. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAPIExceptionNote`

The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `apiException` | `APIExceptionType` |  | No | The created APIExceptionNote. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAccountCharge`

Add charges to an account. The possible errors that can be raised are: - KT-CT-5211: The charge reason with the requested code is deprecated. - KT-CT-5212: The charge reason with the requested code does not exist. - KT-CT-5213: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountCharge` | `AccountChargeType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAccountCredit`

Add credits to an account. The possible errors that can be raised are: - KT-CT-5315: Invalid data. - KT-CT-5314: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountCredit` | `AccountCreditType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAccountFileAttachmentPayload`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientMutationId` | `String` |  | No |  |
| `postRequest` | `UploadPostRequest` |  | No |  |

## `CreateAccountNote`

The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4180: Account note must be a valid string. - KT-CT-4196: Unpin at date provided is in the past. - KT-CT-4195: Unpin at date provided for an unpinned note. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | Account, which has the added note. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAccountPaymentSchedule`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3815: No active payment schedule found for this account. - KT-CT-3822: Unauthorized. - KT-CT-3923: Unauthorized. - KT-CT-3941: Invalid data. - KT-CT-3942: An unexpected error occurred. - KT-CT-3947: An unexpected error occurred. - KT-CT-3960: Invalid value for payment day. - KT-CT-3961: Cannot update plan-associated payment schedule. - KT-CT-3962: No new value provided to update payment schedule. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `schedule` | `PaymentScheduleType!` |  | No | New payment schedule. |

## `CreateAccountReference`

Create an account reference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8311: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountReference` | `AccountReferenceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAccountReminder`

The possible errors that can be raised are: - KT-CT-1401: Invalid data. - KT-CT-1402: Unable to create account reminder. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountReminder` | `AccountReminder` |  | No | Account reminder. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAffiliateLink`

Create an affiliate link for a new sales agent. The possible errors that can be raised are: - KT-CT-7711: Invalid data. - KT-CT-7713: Invalid data. - KT-CT-7714: Invalid data. - KT-CT-7715: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `affiliateLink` | `AffiliateLinkType` |  | No | The created affiliate link. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAffiliateOrganisation`

Create an affiliate organisation. The possible errors that can be raised are: - KT-CT-7716: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `affiliateOrganisation` | `AffiliateOrganisationType` |  | No | The created affiliate organisation. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAffiliateSession`

Create a session for an affiliate link.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `affiliateSession` | `AffiliateSessionType` |  | No | The created affiliate session. |

## `CreateAgreement`

The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-4910: No product exists with the given input. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1509: Unable to create agreement. - KT-CT-1511: Cannot create overlapping agreement. - KT-CT-1512: Account type does not support agreements. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreement` | `CommonAgreementType` |  | No | The created agreement. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAgreementRollover`

The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-4910: No product exists with the given input. - KT-CT-4924: Unauthorized. - KT-CT-13701: An active agreement rollover already exists for this agreement. - KT-CT-13702: Expected send date cannot be in the past. - KT-CT-13703: Rollover date cannot be in the past. - KT-CT-13704: Unable to create agreement rollover. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreementRollover` | `AgreementRolloverType` |  | No | The new agreement rollover. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateAudioRecording`

The possible errors that can be raised are: - KT-CT-7720: Invalid S3 key format. - KT-CT-7721: Link not found. - KT-CT-7722: Invalid input for audio recording upload. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `audioRecording` | `AudioRecordingType` |  | No | The created audio recording. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateBusiness`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11108: Invalid data. - KT-CT-11109: Invalid data. - KT-CT-11110: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `business` | `BusinessType` |  | No | The created business. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateCallMetadata`

The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11806: Call metadata item key cannot be an empty string. - KT-CT-11807: A call metadata item with this key already exists for this call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `call` | `CallInterface` |  | No | The call metadata was attached to. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateCampaignItems`

The possible errors that can be raised are: - KT-CT-11501: Voice campaign not found. - KT-CT-4178: No account found with given account number. - KT-CT-11503: One or more campaign items are invalid and cannot be created. - KT-CT-11504: The batch of campaign items is too large. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `batchIdentifier` | `String` |  | No | The identifier for this batch of items to assist in tracking and logging. |
| `campaignItems` | `[VoiceCampaignItemType]` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateCollectionProcessEvent`

Create a collection process event. This mutation allows creating event records for collection processes to track significant events like reactivations and errors. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1605: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessEvent` | `CollectionProcessEventOutputType` |  | No | The created collection process event. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateComplaint`

The possible errors that can be raised are: - KT-CT-10801: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `complaint` | `ComplaintType` |  | No | The complaint that has been created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateContractOutput`

Output type for creating a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `identifier` | `NonEmptyString` |  | No | Unique identifier for the created contract. |
| `wasCreated` | `Boolean!` |  | No | Indicates whether a new contract was created (True) or an existing contract was matched (False). When False, the mutation is idempotent and returns the existing contract that matches the provided parameters. |

## `CreateContributionAgreement`

The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-9601: Invalid data. - KT-CT-9602: Unable to create contribution agreement. - KT-CT-9605: Contribution amount cannot be 0 or negative. - KT-CT-9606: Scheme is not accepting contributions at this time. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contributionAgreement` | `ContributionAgreementType` |  | No | The created contribution agreement. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateCreditTransferPermission`

Mutation to create a credit transfer permission. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3827: The ledger is not valid. - KT-CT-3828: At least one of the provided ledgers must be a credit storage ledger. - KT-CT-3829: The credit transfer permission already exists. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `validFrom` | `DateTime` |  | No | Datetime when the credit transfer permission is valid. |

## `CreateCustomerFeedback`

The possible errors that can be raised are: - KT-CT-5516: Invalid data. - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `customerFeedback` | `CustomerFeedbackType` |  | No | The created customer feedback object. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateDepositAgreement`

Create a new deposit agreement for the account if it needs one. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `depositAgreement` | `CreateDepositAgreementOutput` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateDepositAgreementOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `depositAmount` | `Int` |  | No |  |
| `depositRequired` | `Boolean` |  | No |  |

## `CreateEnergyAccount`

Creates an Account instance. The possible errors that can be raised are: - KT-CT-4910: No product exists with the given input. - KT-CT-4911: Product not available. - KT-ES-4117: Invalid data. - KT-ES-4111: Supply point already exists. - KT-ES-4113: ATR not valid for contracting. - KT-ES-7701: The affiliate client failed to meet the requirements. - KT-ES-4121: Gas tariffs are not available. - KT-ES-4102: Account with multiple properties. - KT-ES-4122: Unable to create a referral. - KT-ES-4123: Nif not found. - KT-ES-4914: The received CUPS is invalid. - KT-ES-7819: The request to Chipiron to get SIPS data failed. - KT-ES-4917: The given supply point is not valid to contract. - KT-CT-7899: An internal error occurred. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNif` | `String` |  | No | Customer's Spanish fiscal code. |
| `accountNumber` | `String` |  | No | The account number. |
| `electricityAgreementNumber` | `String` |  | No | Electricity supply point agreement number. |
| `gasAgreementNumber` | `String` |  | No | Gas supply point agreement number. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `referralCreated` | `Boolean` |  | No | Resolves whether a referral was created as part of this account creation. |
| `token` | `String` |  | No | Token for setting the initial password. |
| `userId` | `String` |  | No | Id for setting the initial password. |

## `CreateExternalAccountEvent`

Create an external account event. The possible errors that can be raised are: - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `event` | `ExternalAccountEvent` |  | No | The new event data. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateExternalAccountUserEvent`

Create an external account user event. The possible errors that can be raised are: - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `event` | `ExternalAccountUserEvent` |  | No | The new event data. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateExternalMessage`

Create an external message to record communications sent by external vendors. This allows you to import messages, such as emails, sent using other tools into Kraken. The possible errors that can be raised are: - KT-CT-14201: Vendor is empty. - KT-CT-14202: Vendor message ID is empty. - KT-CT-14203: Account number is empty. - KT-CT-14204: Message already exists. - KT-CT-14205: Unable to create the external message. - KT-CT-14206: An email body is missing. - KT-CT-14207: To email is empty. - KT-CT-14208: To email is not a valid email address. - KT-CT-14209: From email is empty. - KT-CT-14210: From email is an invalid format. - KT-CT-14211: A reply to email address is empty. - KT-CT-14212: A reply to email address is not a valid email address. - KT-CT-14213: The external messaging API is not enabled. - KT-CT-14214: An account number was provided, but no corresponding account could be found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `externalMessage` | `ExternalMessageType` |  | No | The external message that was created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateGoodsPurchase`

The possible errors that can be raised are: - KT-CT-8206: Invalid data. - KT-CT-1131: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `goodsPurchase` | `GoodsPurchase` |  | No | Goods purchase created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateGoodsQuote`

The possible errors that can be raised are: - KT-CT-8202: Invalid data. - KT-CT-8205: Unable to create quote. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `goodsQuote` | `GoodsQuote` |  | No | Goods quote created for the customer. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateGoodsQuoteWithoutAccount`

The possible errors that can be raised are: - KT-CT-8202: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `goodsQuote` | `GoodsQuote` |  | No | Goods quote created for the customer. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateInboundCall`

The possible errors that can be raised are: - KT-CT-11805: Invalid input for creating an inbound call. - KT-CT-11810: Caller is blocked. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `call` | `InboundCallType` |  | No | The call that was created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateInkInboundMessage`

Register an Ink inbound message. The possible errors that can be raised are: - KT-CT-7622: Attachment bucket is invalid. - KT-CT-7623: Attachment path is invalid. - KT-CT-7621: Attachment not found. - KT-CT-7618: Unable to process message. - KT-CT-7625: Invalid email address. - KT-CT-7630: Message with this message ID has already been processed. - KT-CT-7632: The text content of the Ink Inbound Generic Message is too long. - KT-CT-7620: Channel not supported. - KT-CT-7627: The 'email' object is missing from the payload. - KT-CT-7628: The 'generic' object is missing from the payload. - KT-CT-7629: The 'post' object is missing from the payload. - KT-CT-7653: Account numbers on the message and message type must match if both are supplied. - KT-CT-7654: An account number was provided, but no corresponding account could be found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `InkMessage!` |  | No | The Ink message that was created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateInkLiveChatMessage`

The possible errors that can be raised are: - KT-CT-7616: Not yet implemented. - KT-CT-1111: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-7642: No account user was found for the given fromHandle. - KT-CT-7641: Live Chat message with this message ID has already been processed. - KT-CT-7645: The user is not authorized to access this Live Chat. - KT-CT-7622: Attachment bucket is invalid. - KT-CT-7623: Attachment path is invalid. - KT-CT-7621: Attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `liveChatConversation` | `InkLiveChatConversation` |  | No | The live chat conversation. |
| `messageRelayId` | `String!` |  | No | The ID of the Ink Live Chat message that was created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateLead`

The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8930: Unable to parse address. - KT-CT-8928: The funnel is not active and cannot be used to create this entity. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8919: Funnel initial stage not set. - KT-CT-9017: Consent type not found. - KT-CT-8932: Lead contact details missing legal contact. - KT-CT-8934: Lead contact details missing communications contact. - KT-CT-8935: National ID bad input. - KT-CT-4121: Invalid phone number. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `leadNumber` | `String` |  | No | The unique number of the lead. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateMetadata`

Create metadata on an object. The possible errors that can be raised are: - KT-CT-8412: Invalid data. - KT-CT-8414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `metadata` | `Metadata` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateMfaDevice`

Create a multi-factor authentication (MFA) device for user. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1151: MFA device not found. - KT-CT-1153: Unable to create MFA device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceEmail` | `String` |  | No | Email address to send the MFA code by default. |
| `devicePhone` | `String` |  | No | Phone number to send the MFA code by default. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `totpSecret` | `String` |  | No | Secret to setup Time-based One-Time Passwords (TOTP) in your authenticator or password manager manually. |

## `CreateNewAgreementFromProductSwitchProcess`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4924: Unauthorized. - KT-CT-1509: Unable to create agreement. - KT-CT-1507: Agreement product switch date is not within the acceptable range. - KT-CT-1510: Product switch process not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreement` | `CommonAgreementType` |  | No | The new agreement created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateOfferGroupForQuoting`

Create a quoting offer group. The possible errors that can be raised are: - KT-CT-12401: Unable to create offer group. - KT-CT-12405: Missing rates for quoting. - KT-CT-12406: Product not configured correctly for quoting. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `offerGroup` | `CreateOfferGroupType` |  | No | Quoting Offer Group. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateOfferGroupType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `identifier` | `ID` |  | No | Identifier of the Offer Group. |
| `offers` | `[OfferType]` |  | No | One or more Offers contained in the Offer Group. |

## `CreateOnSiteJobsAppointment`

The possible errors that can be raised are: - KT-CT-13030: Booking session not found. - KT-CT-13025: Booking session has expired. - KT-CT-13033: Slot not found. - KT-CT-13028: Agent not found. - KT-CT-13019: Vendor not found. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13035: Request is inactive. - KT-CT-13032: Request does not exist. - KT-CT-13036: Booking service currently unavailable. - KT-CT-13037: Appointment reference not provided by booking service. - KT-CT-13031: Timeslot is no longer available. - KT-CT-13027: Booking system error occurred. - KT-CT-13056: Appointment cannot be rescheduled. - KT-CT-13044: Failed to update appointment slot. - KT-CT-13001: Appointment does not exist. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13006: No properties found for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `onSiteJobsAppointment` | `OnSiteJobsAppointmentType` |  | No | The created On-Site Jobs appointment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateOnSiteJobsAppointmentWithDate`

The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13020: Could not identify agent from property. - KT-CT-13021: Invalid job type. - KT-CT-13022: Work category not found for job type. - KT-CT-13057: Date booking mode is not applicable for this request. - KT-CT-13023: Appointment booking checks failed. - KT-CT-13024: Appointment booking checks returned warnings. - KT-CT-13028: Agent not found. - KT-CT-13019: Vendor not found. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13035: Request is inactive. - KT-CT-13036: Booking service currently unavailable. - KT-CT-13037: Appointment reference not provided by booking service. - KT-CT-13027: Booking system error occurred. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-13006: No properties found for the given supply points. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `onSiteJobsAppointment` | `OnSiteJobsAppointmentType` |  | No | The created On-Site Jobs appointment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateOnSiteJobsAppointmentWithoutBooking`

The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13035: Request is inactive. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13021: Invalid job type. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13039: Cancellation fields require CANCELLED status. - KT-CT-13027: Booking system error occurred. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13062: Datetime field must be timezone-aware. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `onSiteJobsAppointment` | `OnSiteJobsAppointmentType` |  | No | The created Appointment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateOnSiteJobsRequest`

The possible errors that can be raised are: - KT-CT-13002: Supply point not found. - KT-CT-13003: Supply points must belong to the same account. - KT-CT-13004: No account found for the given supply points. - KT-CT-13006: No properties found for the given supply points. - KT-CT-13028: Agent not found. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13007: At least one of the request checks failed. - KT-CT-13008: At least one of the request checks has warnings. - KT-CT-13009: On site jobs Request already exists. - KT-CT-13012: Viewer is not allowed to create a request. - KT-CT-13013: Reporter post init error. - KT-CT-13014: Request reason is not supported. - KT-CT-13015: Request sub_reason is not supported. - KT-CT-13041: User is not allowed to override request/appointment checks. - KT-CT-13042: Multiple supply points not supported by this booking adapter. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13047: Multiple supply points found. - KT-CT-13048: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_ids. - KT-CT-13049: Neither supply_point_identifier_to_market_name_mapping nor supply_point_internal_ids provided. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13058: Reason approval details are required when the reason requires approval. - KT-CT-13059: Emergency approval details are required when the emergency requires approval. - KT-CT-13060: Reason approval details should not be provided when the reason does not require approval. - KT-CT-13061: Emergency approval details should not be provided when the emergency does not require approval. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `onSiteJobsRequest` | `OnSiteJobsRequestType` |  | No | The created request. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateOpportunityAndLead`

The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8919: Funnel initial stage not set. - KT-CT-8930: Unable to parse address. - KT-CT-8907: Lead not found. - KT-CT-8901: Unable to create lead. - KT-CT-8902: Unable to create lead. - KT-CT-8935: National ID bad input. - KT-CT-4121: Invalid phone number. - KT-CT-8931: Extra detail value is invalid. - KT-CT-9017: Consent type not found. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-8936: Only one address is required to create an opportunity. - KT-CT-8937: One or more Supply Points cannot be validated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dateOfCreation` | `DateTime` |  | No | The date the opportunity was created. |
| `funnelCode` | `String` |  | No | The code of the funnel. |
| `opportunityNumber` | `String` |  | No | The unique number of the opportunity. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `stage` | `String` |  | No | The stage of the opportunity. |

## `CreateOpportunityFileAttachment`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `result` | `String` |  | No | Whether the operation was successful. |

## `CreateOpportunityForLead`

The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8919: Funnel initial stage not set. - KT-CT-8907: Lead not found. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-8924: Unable to create opportunity. - KT-CT-8925: Unable to create opportunity. - KT-CT-8926: Unable to create opportunity. - KT-CT-8928: The funnel is not active and cannot be used to create this entity. - KT-CT-8930: Unable to parse address. - KT-CT-8936: Only one address is required to create an opportunity. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8937: One or more Supply Points cannot be validated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dateOfCreation` | `DateTime` |  | No | The date the opportunity was created. |
| `opportunityNumber` | `String` |  | No | The unique number of the opportunity. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateOrUpdateLoyaltyCardMutation`

Create a Loyalty Card for the given account user. The possible errors that can be raised are: - KT-CT-5412: No account user exists with the given id. - KT-CT-8610: Invalid data. - KT-CT-8611: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `loyaltyCard` | `LoyaltyCardType` |  | No | Created or updated loyalty card. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateOrUpdateTimeSeriesEntries`

Summary information on the time series and associated variants once the creation and update operations have been completed.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | The time series code. |
| `description` | `String` |  | No | The time series description. |
| `meta` | `JSONString` |  | No | The time series meta information. |
| `name` | `String!` |  | No | The time series display name. |
| `periodSize` | `String!` |  | No | The time series period size value. |
| `productCode` | `String` |  | No | The product code associated to the time series. |
| `unit` | `String!` |  | No | The time series unit value. |
| `variants` | `[VariantProfile!]!` |  | No | The existing time series variants based on the prices created. |

## `CreatePaymentActionIntent`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3980: Invalid ledger identifier. - KT-CT-3981: Unauthorized. - KT-CT-3982: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `token` | `ID!` |  | No | The action intent token. |

## `CreatePortfolio`

Create a new portfolio. The possible errors that can be raised are: - KT-CT-9402: Received an invalid brandCode. - KT-CT-9401: Received an invalid operationsTeamId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `portfolio` | `PortfolioType` |  | No | The created portfolio. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreatePortfolioUserRole`

The possible errors that can be raised are: - KT-CT-9403: Received an invalid portfolioId. - KT-CT-9404: Received an invalid accountUserId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `portfolioUserRole` | `PortfolioUserRoleType` |  | No | The created role for a user in association with a portfolio. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreatePostEvents`

Create post delivery events from external vendors. The possible errors that can be raised are: - KT-CT-9907: Post events batch size exceeded. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `createdEventsCount` | `Int` |  | No | Number of events successfully created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `CreateProductOutput`

Output type for creating a product.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `product` | `SupplyProductType` |  | No | The created product. |

## `CreateQuote`

The possible errors that can be raised are: - KT-CT-4639: Unable to quote for the provided market identifier. - KT-CT-1501: Agreement not found. - KT-CT-4131: Invalid brand. - KT-CT-7719: Session not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `quoteRequest` | `QuoteRequest` |  | No | The quote request. |

## `CreateQuoteForAccount`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. - KT-CT-4616: Unable to create a quote. - KT-CT-4631: Unable to quote for the chosen market. - KT-CT-4645: No supply point found belonging to the account for the provided identifier. - KT-CT-4924: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `quoteRequest` | `MarketSupplyQuoteRequestType` |  | No | Returns a quote request. |

## `CreateReferral`

Use a referral code to create a referral and trigger a referral reward. This is for customers to refer other customers so it only works with friend referrals and not partner referrals. This will try to find a user with given referral code as their personal referral code. If found, it will create an AccountReferral instance for the given account number. The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6710: Unable to create referral. - KT-CT-6711: Accounts may not self-refer. - KT-CT-6713: Referring and referred account brands do not match. - KT-CT-6712: Invalid reference. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `referredAccountRewardAmount` | `Int` |  | No | The reward amount to be issued to the referred account, in smallest currency subunits. |

## `CreateReminder`

The possible errors that can be raised are: - KT-CT-1401: Invalid data. - KT-CT-1402: Unable to create account reminder. - KT-CT-1403: Missing user or team assignee. - KT-CT-1404: This reminder type is deprecated. - KT-CT-1405: Both user and team assignee provided. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `reminder` | `Reminder` |  | No | Account reminder. |

## `CreateScheduledTransactions`

Mutation to create scheduled transactions. The possible errors that can be raised are: - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3830: Invalid action. - KT-CT-3831: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `scheduledTransactions` | `[ScheduledTransactionType]` |  | No |  |

## `CreateShellAccountPayload`

Create a shell account (a billable account with no property/energy supply).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `AccountInterface` |  | No |  |
| `billingAddressLine1` | `String` |  | No |  |
| `billingAddressLine2` | `String` |  | No |  |
| `billingAddressLine3` | `String` |  | No |  |
| `billingAddressLine4` | `String` |  | No |  |
| `billingAddressLine5` | `String` |  | No |  |
| `billingName` | `String` |  | No |  |
| `billingPeriodDay` | `Int` |  | No | Day to fixed bill on if billing_period_length set. |
| `billingPeriodLength` | `String` |  | No | For fixed billing accounts only, the length of their billing period. Can be MONTHLY or QUARTERLY. |
| `billingPeriodMonth` | `Int` |  | No | Month to start billing from if billing_period_length set to QUARTERLY or the multiplier is > 1. |
| `billingPeriodMultiplier` | `Int` |  | No | For fixed billing accounts only, the number the period length is to be multiplied by to get the total period length, i.e. for billing every second month, select 2 combined with a billing period length MONTHLY. Can't be > 1 for quarterly billing. |
| `billingPostcode` | `String` |  | No |  |
| `billingRichAddress` | `String` |  | No | This must be a string-ified version of the JSON representation of RichAddressInput type. |
| `brand` | `String` |  | No |  |
| `businessType` | `String` |  | No |  |
| `clientMutationId` | `String` |  | No |  |
| `companyName` | `String` |  | No |  |
| `companyNumber` | `String` |  | No |  |
| `dateOfBirth` | `Date` |  | No |  |
| `email` | `String!` |  | No |  |
| `errors` | `[ErrorType]` |  | No |  |
| `familyName` | `String!` |  | No |  |
| `givenName` | `String!` |  | No |  |
| `isBusinessAccount` | `Boolean` |  | No |  |
| `landline` | `String` |  | No |  |
| `mobile` | `String` |  | No |  |
| `password` | `String` |  | No |  |
| `passwordUpdateToken` | `String` |  | No |  |
| `portfolioNumber` | `String` |  | No |  |
| `urn` | `String` |  | No |  |

## `CreateSolarWalletRelationship`

Create the solar wallet credit sharing ledger with a validity date range betweena solar wallet ledger source and an electricity ledger target The possible errors that can be raised are: - KT-ES-7805: The request to create a solar wallet sharing credit between ledgers was incomplete or malformed. - KT-CT-4123: Unauthorized. - KT-ES-4116: Account not found. - KT-ES-7809: There is no ledger of this type on this account.. - KT-ES-7806: Couldn't create sharing credit between ledgers because credit sharing ledger already exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `creditSharingLedgerId` | `Int` |  | No | Credit sharing ledgers id. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `sourceAccountNumber` | `String` |  | No | Source account number of the solar wallet ledger. |
| `success` | `Boolean` |  | No | A flag that ensures changes have been made. |
| `targetAccountNumber` | `String` |  | No | Target account number of the electricity ledger. |
| `targetGivenName` | `String` |  | No | Target account given name. |
| `validFrom` | `DateTime` |  | No | Datetime when the solar wallet credit sharing ledger begins. |
| `validTo` | `DateTime` |  | No | Datetime when the solar wallet credit sharing ledger ends. |

## `CreateTimeSeriesPrices`

Time series information and existing variants based on the prices created.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | The time series code. |
| `description` | `String` |  | No | The time series description. |
| `meta` | `JSONString` |  | No | The time series meta information. |
| `name` | `String!` |  | No | The time series display name. |
| `periodSize` | `String!` |  | No | The time series period size value. |
| `productCode` | `String` |  | No | The product code associated to the time series. |
| `unit` | `String!` |  | No | The time series unit value. |
| `variants` | `[VariantProfile!]!` |  | No | The existing time series variants based on the prices created. |

## `Credit`

A credit to the customer from the energy retailer.

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

## `CreditReasonType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The credit reason code. |
| `display` | `String` |  | No | The credit reason display text. |
| `group` | `String` |  | No | The group the credit reason belongs to (if applicable). |
| `isDeprecated` | `Boolean` |  | No | Whether the credit reason is deprecated. |
| `isHidden` | `Boolean` |  | No | Whether the credit reason is hidden. |
| `isTaxExempt` | `Boolean` |  | No | Whether the credit reason is sales tax exempt. |

## `CreditTransferPermissionFromSourceLedgerType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | The number of the account linked to this permission. |
| `ledgerNumber` | `String` |  | No | The number of the ledger linked to this permission. |
| `validFrom` | `DateTime` |  | No | The datetime from which the permission is valid. |
| `validTo` | `DateTime` |  | No | The datetime to which the permission is valid. |

## `CreditTransferPermissionToTargetLedgerType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | The number of the account linked to this permission. |
| `ledgerNumber` | `String` |  | No | The number of the ledger linked to this permission. |
| `validFrom` | `DateTime` |  | No | The datetime from which the permission is valid. |
| `validTo` | `DateTime` |  | No | The datetime to which the permission is valid. |

## `CreditTransferPermissionsDataType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fromSourceLedgers` | `[CreditTransferPermissionFromSourceLedgerType]` |  | No | Permissions for credit transfers when the ledger is the target. |
| `toTargetLedgers` | `[CreditTransferPermissionToTargetLedgerType]` |  | No | Permissions for credit transfers when the ledger is the source. |

## `CupsValidationToContract`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `availableContractElectricity` | `Boolean` |  | No | Whether electricity cups is able to contract or not. |
| `availableContractGas` | `Boolean` |  | No | Whether gas cups is able to contract or not. |
| `electricityProductId` | `ID` |  | No | The electricity product ID this supply point can contract. |
| `gasProductId` | `ID` |  | No | The gas product ID this supply point can contract. |
| `spanishValidationMessage` | `String` |  | No | Message in spanish describing the validation resolution. |
| `validationMessage` | `String` |  | No | Message describing the validation resolution. |

## `CurrentEligibilityStatusOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isEligible` | `Boolean` |  | No | The current eligibility status for a deposit return. |
| `reasonsForIneligibility` | `[String]` |  | No | The reasons why the account is currently ineligible for a deposit return. |

## `CustomerFeedbackFormConnectionTypeConnection`

Paginator of Customer Feedback Form.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[CustomerFeedbackFormConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `CustomerFeedbackFormConnectionTypeEdge`

A Relay edge containing a `CustomerFeedbackFormConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `CustomerFeedbackFormType` |  | No | The item at the end of the edge |

## `CustomerFeedbackFormType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | The unique identifier for the customer feedback form. |
| `name` | `String` |  | No | The name of the customer feedback form. |

## `CustomerFeedbackType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No |  |
| `rawScore` | `Int` |  | No | The value attached to the source |
| `submittedAt` | `DateTime` |  | No | The datetime the feedback was submitted |

## `DCAProceedingClosureStatus`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String!` |  | No | The account number. |
| `ledgerNumber` | `String` |  | No | The ledger identifier. |

## `DCAProceedingCommencementStatus`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String!` |  | No | The account number. |
| `agency` | `String!` |  | No | The agency. |
| `campaign` | `String!` |  | No | The campaign. |
| `commencementStatus` | `Boolean!` |  | No | Whether the commencement could be applied. |
| `ledgerNumber` | `String` |  | No | The ledger identifier. |

## `DCAProceedingUpdateStatus`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String!` |  | No | The account number. |
| `commencementStatus` | `Boolean!` |  | No | Whether the update has been applied. |

## `DailyWholesalePrice`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `date` | `Date!` |  | No | The date of the wholesale price. |
| `hour` | `Int!` |  | No |  |
| `price` | `Decimal!` |  | No |  |

## `Dashboard`

A list of components which comprise a dashboard screen.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dashboardItems` | `[SectionType]!` |  | No | The list of sections for a dashboard. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `serialisedDashboardItems` | `String!` |  | No | The serialised dashboard items. |
| `typename` | `String` |  | No | The name of the object's type. |

## `DateTimePageInfo`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `endCursor` | `DateTime` |  | No | The cursor of the last item. |
| `hasNextPage` | `Boolean` |  | No | Whether there are more items when paginating forwards. |
| `hasPreviousPage` | `Boolean` |  | No | Whether there are previous items when paginating backwards. |
| `startCursor` | `DateTime` |  | No | The cursor of the first item. |

## `DeauthenticateDevice`

De-authenticate a registered device. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4350: Unable to de-authenticate device. - KT-CT-4352: This device cannot currently be de-authenticated. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `DeviceDetailsType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `DeauthenticateFlexDevice`

De-authenticate a registered device by device id. The possible errors that can be raised are: - KT-CT-4350: Unable to de-authenticate device. - KT-CT-4352: This device cannot currently be de-authenticated. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `DeviceDetailsType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `DebtCollectionAgencyType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No |  |
| `isActive` | `Boolean!` |  | No |  |
| `name` | `String!` |  | No |  |

## `DebtCollectionCampaignType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No |  |
| `deprecatedAt` | `DateTime` |  | No |  |
| `displayName` | `String!` |  | No |  |
| `requiresFieldVisit` | `Boolean!` |  | No |  |

## `DebtCollectionProceedingType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agency` | `DebtCollectionAgencyType` |  | No | The agency responsible for the collection proceedings. |
| `amount` | `Int` |  | No |  |
| `campaign` | `CollectionCampaignType` |  | Yes (The 'campaign' field is deprecated. Use `collectionCampaign` instead - Marked as deprecated on 2025-03-20. - Scheduled for removal on or after 2025-04-30.) | The campaign type of the collection proceedings. |
| `collectionCampaign` | `DebtCollectionCampaignType` |  | No | The campaign type of the collection proceedings. |
| `startedAt` | `DateTime!` |  | No |  |
| `stopReason` | `DebtCollectionProceedingStopReason` |  | No |  |
| `stoppedAt` | `DateTime` |  | No |  |

## `DecimalReading`

A reading with a decimal value taken at a specific time.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `timestamp` | `DateTime!` |  | No | The timestamp when the reading was taken. |
| `value` | `Decimal!` |  | No | The decimal value of the reading. |

## `DecimalType`

Graphene type object to represent float values

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `decimalValue` | `Decimal!` |  | No | Value of this field. |

## `DeductLoyaltyPoints`

Deduct a set amount of loyalty points from an account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-5420: Unauthorized. - KT-CT-9211: Invalid reason for loyalty points award. - KT-CT-9219: Loyalty points user not found. - KT-CT-9204: Negative or zero points set. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9221: Idempotency key already used on ledger entry. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `ledgerEntry` | `LoyaltyPointLedgerEntryType` |  | No | The ledger entry for the deducted loyalty points. |
| `pointsDeducted` | `Int` |  | No | The number of loyalty points that were deducted. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `DeeplinkActionType`

An action which navigates to the URL of another backend screen.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | Unique identifier of the object. |
| `typeName` | `String` |  | No | The name of the action object's type. |
| `typename` | `String` |  | No | The name of the object's type. |
| `url` | `String!` |  | No | The URL to navigate to. |

## `DelayerDaysType`

Represents delayer days for active payment in a contract. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `days` | `Int!` |  | No | Number of days to delay based on delay strategy. |
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `strategy` | `DelayerDaysStrategy!` |  | No | Defines the method for calculating the delay period. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `DeleteAccountReference`

Delete a reference for a particular account and namespace. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8312: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountReference` | `DeleteAccountReferenceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `DeleteAccountReferenceType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `namespace` | `String!` |  | No | The namespace associated with the removed AccountReference. |

## `DeleteBoostCharge`

The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4354: Unable to cancel boost charge. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `KrakenFlexDeviceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `DeleteMfaDevice`

Delete a multi-factor authentication (MFA) device for the authenticated user. The possible errors that can be raised are: - KT-CT-1150: MFA device not found. - KT-CT-1154: Unable to delete MFA device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceDeleted` | `Boolean` |  | No | Flag to indicate if the MFA device has been successfully deleted. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `DeletePropertyDescendants`

Delete all descendants of a property in a hierarchy. This permanently deletes all descendant nodes (children, grandchildren, etc.) but keeps the property node itself in the hierarchy. This operation is idempotent - if the property is not in the hierarchy or has no descendants, it will succeed without error. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `property` | `PropertyType` |  | No | The property whose descendants were deleted. |

## `DeletePushNotificationBinding`

The possible errors that can be raised are: - KT-CT-5411: Invalid token or no push notification binding found for the given account user. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `status` | `DeletePushNotificationBindingOutput` |  | No |  |

## `DeletedSupplyPointEstimationGroupType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `supplyPointExternalId` | `String!` |  | No | The external identifier of the detached supply point. |

## `DepositAgreementOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptedAt` | `DateTime` |  | No | The timestamp at which the customer accepted the deposit agreement. |
| `collectionDate` | `Date` |  | No | The date on which a payment is requested for deposit collection (defaults to current date, if not specified in the deposit policy). |
| `currentEligibilityStatus` | `CurrentEligibilityStatusOutput` |  | No | The current eligibility status for a deposit return. |
| `depositAmount` | `Int` |  | No | The deposit agreement amount. |
| `depositKey` | `String` |  | No | The deposit agreement key (unique). |
| `dueDate` | `Date` |  | No | The date by which the deposit agreement must be fulfilled (defaults to 31-12-9999 i.e. deposit is never late, if not specified in the deposit policy). |
| `fulfilledAt` | `DateTime` |  | No | The timestamp at which the deposit agreement was fulfilled. |
| `returnStrategy` | `String` |  | No | The return strategy used to return the deposit. |

## `DepositReturnScheduleOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int` |  | No | The amount to be returned in this installment. |
| `dueDate` | `Date` |  | No | The date by which the deposit return installment is due. |
| `status` | `String` |  | No | The status of this return installment. |

## `DetachSupplyPointFromEstimationGroup`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-13603: Supply Point does not exist. - KT-CT-13604: Supply point has no estimation group assigned. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `supplyPoint` | `DeletedSupplyPointEstimationGroupType` |  | No | The deleted supply point. |

## `Device`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceIdentifier` | `String` |  | No | The id of the device. This field can only be provided in the output if device level readings are also requested. |
| `readings` | `Readings` | `startAt: DateTime!, endAt: DateTime!, readingType: ReadingTypes!, timeGranularity: TimeGranularities, timezone: String = "Europe/Madrid", units: [Units]` | No | Get readings from a readable device e.g., a supply point, device, or register. |
| `registers` | `RegistersConnection` | `registerIdentifiers: [String], before: String, after: String, first: Int, last: Int` | No | The registers associated with this device. |

## `DeviceChargingSessionConnection`

Paginator for device charging session.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edges` | `[DeviceChargingSessionEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `DateTimePageInfo` |  | No | Information to aid in DateTime pagination. |

## `DeviceChargingSessionEdge`

A Relay edge containing a `DeviceChargingSession` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `DateTime` |  | No | The cursor of the item. |
| `node` | `DeviceChargingSession` |  | No | The item at the end of the edge |

## `DeviceDetailsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceType` | `KrakenFlexDeviceTypes` |  | No | The type of device. |
| `krakenflexDeviceId` | `String` |  | No |  |
| `provider` | `ProviderChoices` |  | No | The third party that provides control over this device. |

## `DeviceReAuthentication`

Information about a device's re-authentication eligibility and status.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isEligible` | `Boolean` |  | No | Whether the device is eligible for re-authentication. If it returns False, then re-authentication is not supported for this device. Please remove and re-add the device to restore connectivity. |

## `DeviceRegister`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `readings` | `Readings` | `startAt: DateTime!, endAt: DateTime!, readingType: ReadingTypes!, timeGranularity: TimeGranularities, timezone: String = "Europe/Madrid", units: [Units]` | No | Get readings from a readable device e.g., a supply point, device, or register. |
| `registerIdentifier` | `String` |  | No | The id of the register. This field can only be provided in the output if register level readings are also requested. |

## `DeviceRegistration`

Register a device for smart controlling. Where device refers to batteries, electric vehicles, heat pumps or thermostats. The possible errors that can be raised are: - KT-CT-4324: Device already registered error. - KT-CT-4321: Serializer validation error. - KT-CT-4312: Unable to register device. - KT-CT-4363: No capable devices found. - KT-CT-4364: Multiple devices found. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `registeredDeviceIds` | `[String]` |  | No | Device ID(s) of the registered device(s). |

## `DevicesConnection`

Pagination for devices.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[DevicesEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `DevicesEdge`

A Relay edge containing a `Devices` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `Device` |  | No | The item at the end of the edge |

## `DirectDebitInstructionConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[DirectDebitInstructionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `DirectDebitInstructionConnectionTypeEdge`

A Relay edge containing a `DirectDebitInstructionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `DirectDebitInstructionType` |  | No | The item at the end of the edge |

## `DirectDebitInstructionType`

Direct Debit Instructions

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountHolder` | `String!` |  | No |  |
| `cardExpiryMonth` | `Int` |  | No |  |
| `cardExpiryYear` | `Int` |  | No |  |
| `cardPaymentNetwork` | `String` |  | No |  |
| `iban` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `instructionType` | `String!` |  | No |  |
| `lastFourDigitsOfAccountNumber` | `String` |  | Yes (The 'lastFourDigitsOfAccountNumber' field is deprecated. Use 'maskedAccountIdentifier' for a masked reference to the instruction. - Marked as deprecated on 2021-12-23. - Scheduled for removal on or after 2024-01-01.) | The last four digits of the account number. |
| `maskedAccountIdentifier` | `String` |  | No | A masked reference to a recurring payment method. |
| `maskedIban` | `String` |  | No | A masked version of the IBAN. |
| `owners` | `[PaymentInstructionOwnerType]` |  | No | The owners of the financial account this instruction represents. |
| `sortCode` | `String!` |  | No |  |
| `status` | `String!` |  | No |  |

## `DualFuelConsumption`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `elecAnnualConsumption` | `Int` |  | No | Estimated annual consumption for electricity. |
| `gasAnnualConsumption` | `Int` |  | No | Estimated annual consumption for gas. |

## `DualFuelProductQuote`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `annualFee` | `Float` |  | No | Annual fee for dual fuel. |
| `annualFeeUnits` | `String` |  | No | Annual fee units for dual fuel. |
| `annualFeeWithTaxes` | `Float` |  | No | Annual fee with taxes for dual fuel. |
| `electricity` | `SummaryProductInfo` |  | No | Quotation for electricity. |
| `gas` | `SummaryProductInfo` |  | No | Quotation for gas. |
| `monthlyFee` | `Float` |  | No | Monthly fee for dual fuel. |
| `monthlyFeeUnits` | `String` |  | No | Monthly fee units for dual fuel. |
| `monthlyFeeWithTaxes` | `Float` |  | No | Monthly fee with taxes for dual fuel. |

## `ElectricVehicleModelType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `availableFrom` | `Int` |  | No | This field is replacing `year`. |
| `availableTo` | `Int` |  | No |  |
| `batterySize` | `Decimal` |  | No |  |
| `integrationStatus` | `IntegrationStatus` |  | No | Shows the availability status of an integration. |
| `isIntegrationLive` | `Boolean` |  | No |  |
| `model` | `String` |  | No |  |
| `supportedProviders` | `[String]` |  | No |  |
| `vehicleId` | `Int` |  | No |  |
| `year` | `Int` |  | No |  |

## `ElectricVehicleType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `make` | `String` |  | No |  |
| `models` | `[ElectricVehicleModelType]` |  | No |  |

## `ElectricityFiltersOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceId` | `String` |  | No | The identifier of the device associated to this reading. |
| `marketSupplyPointId` | `String` |  | No | The identifier of the market supply point associated to this reading. |
| `readingDirection` | `ReadingDirectionType` |  | No | Reading direction is based on the utility generated or consumed by the customer. |
| `readingFrequencyType` | `ReadingFrequencyType` |  | No | The frequency of the reading. |
| `readingQuality` | `ReadingQualityType` |  | No |  |
| `registerId` | `String` |  | No | The identifier of the register associated to this reading. |

## `ElectricitySupplyPoint`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `activeAgreement` | `Agreement` |  | No | The active agreement in the supply point. The possible errors that can be raised are: - KT-ES-4110: Multiple active agreements. - KT-CT-1113: Disabled GraphQL field requested. |
| `agreements` | `[Agreement]!` |  | No | All agreements of the supply point. |
| `atrTariffs` | `[ATRTariff]` |  | No | Historical changes to the supply point ATRs. |
| `cups` | `String!` |  | No | The supply point identification number. |
| `id` | `ID` |  | No | The supply point ID. |
| `networkOperator` | `NetworkOperator` |  | No | The network operator information. |
| `selfConsumption` | `String` |  | No | The supply point self consumption status description. |
| `selfConsumptionCode` | `String` |  | No | The supply point self consumption status code. |
| `status` | `String` |  | No | The supply point kraken status. |
| `supplierChangeInProgress` | `Boolean` |  | No | Whether there is an ongoing change to the supplier contract. |
| `supplyPeriods` | `SupplyPeriodConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The supply periods for the supply point |

## `ElectricityTerminationOutput`

Output data related to a LeaveSupplier journey for the electricity market.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `additionalInformation` | `String` |  | No | The declared additional information for the request. |
| `contactName` | `String` |  | No | The declared contact name for the request. |
| `contactTelephoneNumber` | `String!` |  | No | The contact phone number for the request. |
| `cutReason` | `CutReason!` |  | No | The declared reason for the request. |
| `desiredEffectiveDate` | `Date` |  | No | The requested last day of supply. |
| `desiredEffectiveDateType` | `RequestedDateType!` |  | No | The requested supply end date type for the leave supplier. |
| `supplyPointIdentifier` | `String!` |  | No | The market supply point identification number. |

## `EmailAttachmentType`

Represents a file to attach to a email message.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `filename` | `String!` |  | No | The filename of the attachment. |
| `id` | `ID!` |  | No | The ID of the attachment. |
| `temporaryUrl` | `String` |  | No | Temporary URL at which the attachment is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). |

## `EmailEventType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `eventType` | `String!` |  | No |  |
| `id` | `ID!` |  | No | The ID of the object |
| `message` | `EmailType` |  | No | Email message of the email event. Returns null for message's sent/received by other user's on the account. |
| `occurredAt` | `DateTime!` |  | No |  |

## `EmailType`

Represents an email communication

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `[EmailAttachmentType]` |  | No | Attachments of the email message. |
| `channel` | `String!` |  | No |  |
| `createdAt` | `DateTime!` |  | No | The date and time the email was created. |
| `fromEmail` | `String!` |  | No | The address the email was sent from. |
| `fromNumber` | `String!` |  | No |  |
| `htmlBody` | `String` |  | No | HTML body of the email message. |
| `id` | `ID!` |  | No | The ID of the email. |
| `recipient` | `String` |  | No | Email recipient. |
| `sender` | `String` |  | No | Email sender. |
| `sentAt` | `DateTime` |  | No | The date and time the email was sent. |
| `subject` | `String` |  | No | Subject line of the email message. |
| `supportSiteUrl` | `String` |  | No | URL to view the email in the support site. |
| `templateCode` | `String!` |  | No | The email template code. |
| `textBody` | `String` |  | No | Text body of the email message. |
| `toAddress` | `String!` |  | No | The email address of the recipient. |
| `toNumber` | `String!` |  | No |  |

## `EmailVerificationStatus`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `email` | `String!` |  | No | The email address to be checked. |
| `status` | `VerificationRequestStatus` |  | No | The status of verification for associated email. |

## `EmbeddedElectricityFiltersOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceId` | `String` |  | No | The identifier of the device associated to this reading. |
| `marketSupplyPointId` | `String` |  | No | The identifier of the market supply point associated to this reading. |
| `readingDirection` | `ReadingDirectionType` |  | No | Reading direction is based on the utility generated or consumed by the customer. |
| `readingFrequencyType` | `ReadingFrequencyType` |  | No | The frequency of the reading. |
| `readingQuality` | `ReadingQualityType` |  | No |  |
| `registerId` | `String` |  | No | The identifier of the register associated to this reading. |

## `EmbeddedNetworkType`

Represents an embedded network that holds multiple embedded properties.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `embeddedProperties` | `[EmbeddedPropertyType]` |  | No | Get details about properties in an embedded network. |
| `id` | `ID!` |  | No |  |
| `name` | `String!` |  | No | A unique name/code for the network |

## `EmbeddedPropertyType`

Represents an embedded property in an embedded network.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `embeddedNetwork` | `EmbeddedNetworkType!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `propertyId` | `ID` |  | No | The id of the physical property related to this embedded property type. |

## `EndContributionAgreement`

The possible errors that can be raised are: - KT-CT-9603: Unable to find contribution agreement. - KT-CT-4123: Unauthorized. - KT-CT-9604: Unable to end contribution agreement. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contributionAgreement` | `ContributionAgreementType` |  | No | The created contribution agreement. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `Energy`

Describes the energy (not power) consumed (e.g. as electricity) or returned (e.g. as heat) by a system over a given span of time. Differs from `Power` in that it describes the *total* amount of energy transferred during a given time frame (not a single point in time).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `unit` | `EnergyUnit!` |  | No | The units in which the energy is being measured. |
| `value` | `Decimal` |  | No | The amount of energy (not power) transmitted. |

## `EnergyMixDataType`

Energy mix data can include the latest carbon intensity index in a region.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `carbonIntensityIndex` | `String` |  | No | Current carbon intensity index. |

## `EnodeLinkSessionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `linkState` | `String` |  | No |  |
| `linkUrl` | `String` |  | No |  |

## `EnqueueInboundCall`

The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11803: Unable to enqueue the call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `call` | `InboundCallType` |  | No | The call that was enqueued. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `EnrollAccountInLoyaltyProgram`

Enroll an account into the loyalty program. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9213: ineligible loyalty points enrollment. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `outcome` | `EnrollAccountInLoyaltyProgramOutcome` |  | No | Outcome of the loyalty points campaign enrollment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `EnrollAccountInLoyaltyProgramOutcome`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `hasEnrolled` | `Boolean` |  | No | Whether or not this account has been enrolled in the loyalty points campaign. |

## `EnrollmentCancelled`

Enrollment was successfully cancelled.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `enrollmentProcess` | `EnrollmentProcess!` |  | No | The Enrollment process that was cancelled. |
| `message` | `String!` |  | No | The message to display to the user on Enrollment initiation. |

## `EnrollmentInitiated`

Enrollment was successfully initiated.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `enrollmentProcesses` | `[EnrollmentProcess]!` |  | No | The Enrollment processes that were initiated. |
| `message` | `String!` |  | No | The message to display to the user on Enrollment initiation. |

## `EnrollmentReversed`

Enrollment was successfully reversed.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `enrollmentProcess` | `EnrollmentProcess!` |  | No | The Enrollment process that was reversed. |
| `message` | `String!` |  | No | The message to display to the user on reversal. |

## `ErrorType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `field` | `String!` |  | No |  |
| `messages` | `[String!]!` |  | No |  |

## `EspAccountUserType`

User objects are the core of the authentication system. They typically represent a customer who manages a portfolio of one or more accounts.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountUserMeta` | `AccountUserMeta` |  | No | Customer's meta information. |
| `accountUserRoles` | `[AccountUserRoleType]` | `accountNumber: String` | No | List of roles a user has for each account they're linked to. |
| `accounts` | `[AccountInterface]` | `allowedBrandCodes: [BrandChoices], restrictToPublicFacingBrands: Boolean, restrictToAccountNumbers: [String], excludeAccountTypes: [AccountTypeChoices], excludeAccountsWithoutAgreements: Boolean` | No | List of accounts that the user is linked to either via portfolio role or account role. |
| `address` | `RichAddressType` |  | No | This user's address. |
| `alternativePhoneNumbers` | `[String]` |  | No | List of alternative phone numbers for the account user. |
| `businesses` | `BusinessConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of businesses that the user has access to through their granted roles. |
| `consents` | `[ConsentType!]!` |  | No | Consents linked to this user. |
| `createdAt` | `DateTime!` |  | No |  |
| `dateOfBirth` | `Date` |  | No | AccountUser's date of birth. |
| `details` | `[AccountUserDetailType]` |  | No | List of details linked to this user. |
| `displayName` | `String` |  | Yes (The 'displayName' field is deprecated. Please use fullName instead of this field. - Marked as deprecated on 2019-12-11. - Scheduled for removal on or after 2024-01-01.) | We recommend you use fullName instead of this field. |
| `email` | `String!` |  | No |  |
| `familyName` | `String!` |  | No |  |
| `firstName` | `String` |  | Yes (The 'firstName' field is deprecated. Use 'givenName' instead. - Marked as deprecated on 2020-09-23. - Scheduled for removal on or after 2023-06-05.) | We recommend you use preferredName or fullName instead of this field. |
| `fullName` | `String` |  | No | The user's full name. |
| `givenName` | `String!` |  | No |  |
| `hasFamilyIssues` | `Boolean` |  | No | Whether there are family issues. |
| `id` | `ID!` |  | No |  |
| `isActive` | `Boolean` |  | No | Whether this user is active. |
| `isDeceased` | `Boolean!` |  | No | Designates whether this user is deceased. |
| `isInHardship` | `Boolean` |  | No | True if user is linked to an account with an active hardship agreement. |
| `label` | `String` |  | No | A free text field to help identifying the customer (e.g. for a job title). |
| `landline` | `String!` |  | No |  |
| `landlinePhoneNumber` | `String` |  | Yes (The 'landlinePhoneNumber' field is deprecated. Use 'landline' instead. - Marked as deprecated on 2021-03-22. - Scheduled for removal on or after 2024-01-01.) | The user's landline phone number. |
| `lastName` | `String` |  | Yes (The 'lastName' field is deprecated. Use 'familyName' instead. - Marked as deprecated on 2020-09-23. - Scheduled for removal on or after 2023-06-05.) | We recommend you use preferredName or fullName instead of this field. |
| `liveSecretKey` | `String` |  | No | The user's secret key to access the Developer API. |
| `mobile` | `String!` |  | No |  |
| `number` | `String` |  | No | A code that uniquely identifies the account user. |
| `paymentMethods` | `PaymentInstructionConnectionTypeConnection` | `validAt: DateTime, statuses: [PaymentInstructionStatus], before: String, after: String, first: Int, last: Int` | No | List payment instructions linked to this user. |
| `permissions` | `[AccountUserPermission]` |  | No | Holds information about the permissions of the current viewer. |
| `portfolioId` | `ID` |  | Yes (The 'portfolioId' field is deprecated. Please use 'portfolioIds' instead. - Marked as deprecated on 2022-08-04. - Scheduled for removal on or after 2024-01-01.) | We recommend you use portfolioIds instead of this field. |
| `portfolioIds` | `[ID]` | `allowedBrandCodes: [BrandChoices], restrictToPublicFacingBrands: Boolean` | No | List of portfolio ids that the user is linked to via their portfolio roles. |
| `portfolioUserRoles` | `[PortfolioUserRoleType]` | `portfolioNumber: String, accountNumber: String` | No | List of roles a user has for each portfolio they're linked to. |
| `portfolios` | `PortfolioConnectionTypeConnection` | `allowedBrandCodes: [BrandChoices], restrictToPublicFacingBrands: Boolean, before: String, after: String, first: Int, last: Int` | No | List of portfolios that the user is linked to via their portfolio roles. |
| `preferences` | `AccountUserCommsPreferences` |  | No |  |
| `preferredName` | `String` |  | No | The user's preferred name. |
| `pronouns` | `String` |  | No | The user's pronouns e.g. 'she/her', 'he/him', 'they/them'. |
| `specialCircumstances` | `SpecialCircumstancesType` |  | No |  |
| `title` | `String` |  | No |  |

## `EstimatedMoneyType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `costCurrency` | `String!` |  | No | Monetary currency of the statistic in ISO-4217 format. |
| `estimatedAmount` | `Decimal!` |  | No | Monetary cost of the statistic. This is the smallest unit of currency, e.g. cents for USD or yen for JPY. Because electricity is priced as a commodity, we must account for fractional cents and this field must be a Decimal. Values from this field should likely not be used for accounting purposes. |
| `pricePerUnit` | `PricePerUnit` |  | No | Net price per unit of the statistic if applicable. |

## `EstimationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dualFuel` | `DualFuelConsumption` |  | No | Dual fuel information. |
| `electricity` | `SingleFuelConsumption` |  | No | Electricity information. |

## `ExcessPrice`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `price` | `Float` |  | No | Excess energy price. |
| `units` | `String` |  | No | Units of excess price. |

## `ExportReadingsConnection`

Pagination for readings representing outgoing utility flow e.g., solar generation.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ExportReadingsEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ExportReadingsEdge`

A Relay edge containing a `ExportReadings` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `Reading` |  | No | The item at the end of the edge |

## `ExternalAccountEvent`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `category` | `String!` |  | No |  |
| `content` | `JSONString` |  | No |  |
| `description` | `String` |  | No |  |
| `eventType` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `occurredAt` | `DateTime!` |  | No |  |
| `subcategory` | `String!` |  | No |  |

## `ExternalAccountEventConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ExternalAccountEventConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ExternalAccountEventConnectionTypeEdge`

A Relay edge containing a `ExternalAccountEventConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ExternalAccountEvent` |  | No | The item at the end of the edge |

## `ExternalAccountUserEvent`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `category` | `String!` |  | No |  |
| `content` | `JSONString` |  | No |  |
| `description` | `String` |  | No |  |
| `eventType` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `occurredAt` | `DateTime!` |  | No |  |
| `subcategory` | `String!` |  | No |  |

## `ExternalMessageType`

An external message, which is a record of a communication such as an email, sent by an external messaging vendor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No | The ID in Kraken of the external message. |
| `sentAt` | `DateTime!` |  | No | The date and time this message was sent. |
| `vendor` | `String!` |  | No | The name of the external messaging vendor that sent this message. |
| `vendorMessageId` | `String!` |  | No | The unique ID of the message in the external vendor's system. |

## `ExternalSalesInfoType`

GraphQL type representing external sales information. This type is used to represent sales records that originate from external systems or processes outside of Kraken's direct tracking mechanisms.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `salesRecordIdentifier` | `String` |  | No | The unique identifier for the sales record. |

## `ExtraDetail`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `field` | `FunnelField` |  | No | The extra detail metadata associated with the opportunity. |
| `key` | `String` |  | No | The key of the extra detail item. |
| `value` | `GenericScalar` |  | No | The value of the extra detail item. |

## `ExtrasOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `String` |  | No | Description of the extra for the parent node. |
| `label` | `String` |  | No | Display label of the extra for the parent node. |
| `value` | `String` |  | No | Value of the extra. |

## `FetchGeneratePaymentFingerprint`

The possible errors that can be raised are: - KT-CT-12101: Payment instruction not found. - KT-CT-12102: Payment vendor not supported. - KT-CT-12103: Missing payment metadata from vendor. - KT-CT-12104: Unable to fetch or generate payment fingerprint. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fingerprint` | `String` |  | No | Fetched or generated fingerprint from vendor. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `vendor` | `String` |  | No | Vendor name. |

## `FetchPreSignedLinkForOpportunityAttachment`

The possible errors that can be raised are: - KT-CT-8933: Opportunity file attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `opportunityFileAttachment` | `OpportunityFileAttachment` |  | No | The opportunity file attachment with pre-signed URL. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `FieldSpecificRateLimitInformation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `field` | `String` |  | No | The name of the GraphQL field for which the rate is limited. |
| `isBlocked` | `Boolean` |  | No | Whether the viewer is currently blocked from making requests to this field due to exceeding the allowed request rate. |
| `rate` | `String` |  | No | Indicates the rate limit allowed for this field (e.g. 10/m). |
| `ttl` | `Int` |  | No | Time to live: The time remaining before the user is unblocked from making requests to this field. |

## `FieldSpecificRateLimitInformationConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[FieldSpecificRateLimitInformationConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `FieldSpecificRateLimitInformationConnectionTypeEdge`

A Relay edge containing a `FieldSpecificRateLimitInformationConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `FieldSpecificRateLimitInformation` |  | No | The item at the end of the edge |

## `FinancialRiskLevelType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `identifierType` | `String` |  | No | The ID type. Currently only 'meter_point' is supported. |
| `identifierValue` | `ID` |  | No | The ID to be checked. |
| `isInRiskList` | `Boolean` |  | No | Returns True if the risk identifier is in the risk list. |
| `riskLevel` | `Decimal` |  | No | Returns the level of risk for the supplied object between `0.0` and `1.0`. Higher is worse. |

## `FlexDevicePreferenceConstraint`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `max` | `Decimal` |  | No | The maximum value this constraint allows. |
| `min` | `Decimal` |  | No | The minimum value this constraint allows. |

## `FlexDevicePreferenceScheduleSetting`

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

## `FlexDevicePreferenceSetting`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceType` | `String!` |  | No | The device type of the setting. |
| `id` | `Int!` |  | No | The unique id of the device preference setting. |
| `mode` | `PreferencesModeChoices!` |  | No | The mode of the setting. |
| `scheduleSettings` | `[FlexDevicePreferenceScheduleSettingInterface]!` |  | No | Scheduled preference settings. |
| `unit` | `PreferencesUnitChoices!` |  | No | The unit of the min and max values in the preferences setting. |

## `FlexSupportedDevices`

A list of supported makes and models for a given device type.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceType` | `KrakenFlexDeviceTypes!` |  | No | The type of device. |
| `supportedMakes` | `[FlexSupportedMake]!` |  | No | List of supported brands or manufacturer. |

## `FlexSupportedMake`

A brand or manufacturer of the device and its associated models. If models is empty, all models for this make are supported.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `make` | `String!` |  | No | Brand or manufacturer of the device. |
| `models` | `[FlexSupportedModel]!` |  | No | List of supported models for the device make. If empty, all models are supported. |

## `FlexSupportedModel`

A supported model for a given make. If model year range is null, all years are supported.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `modelName` | `String!` |  | No | Model name of the device. |
| `modelYearRange` | `ModelYearRange` |  | No | Model years supported. If null, all model years are supported. |

## `FloatType`

Graphene type object to represent float values

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `floatValue` | `Float!` |  | No | Value of this field. |

## `ForceReauthentication`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `effectiveAt` | `DateTime!` |  | No | The time at which forced reauthentication is effective. Kraken and refresh tokens issued before this time will be invalid. |
| `tokensInvalidated` | `Boolean!` |  | No | Reports whether the mutation applied successfully. Should always be 'true'. |

## `FormScreenType`

A screen type for forms with input fields. Combines display items with input fields (TextField, Checkbox, Toggle), and provides primary/secondary buttons for form submission. Note: header and footer are embedded in screenData and not exposed as separate GraphQL fields, following the pattern of ComponentListType.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accessibilityHidden` | `Boolean` |  | No | Whether the element is hidden from view. |
| `accessibilityLabel` | `String` |  | No | Accessible description of the element. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `name` | `String!` |  | No | The name of the screen. |
| `refreshFrequency` | `Int` |  | No | The refresh / polling frequency in milliseconds. |
| `screenData` | `String` |  | No | Serialized JSON representation of the screen. |
| `typename` | `String` |  | No | The name of the object's type. |

## `FormSubmissionOuput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `content` | `JSONString` |  | No |  |
| `errors` | `[SerializerFieldErrorsType]` |  | No |  |
| `id` | `Int` |  | No |  |

## `FractionSizeType`

A fractional measurement.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fraction` | `Decimal!` |  | No | The fractional value. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `typename` | `String` |  | No | The name of the object's type. |

## `FraudMeterPointCheckType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isInSuspiciousList` | `Boolean` |  | No | Returns True if the meter point ID is in the list of suspicious meter point IDs. |
| `meterPointId` | `String` |  | No | The meter point ID. |

## `FulfilmentType`

Represents an amount of money that can be used to fulfil an obligation.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int!` |  | No | The amount of the fulfilment (in minor currency units), unsigned. |
| `sourceIdentifier` | `String` |  | No | The database ID of the fulfilment source, e.g. the database ID of the payment. |
| `sourceType` | `FulfilmentSourceType` |  | No | The type of the fulfilment source, e.g. PAYMENT. |

## `FundingSourceAmountConnectionTypeConnection`

This field is a connection type. Connections are used to implement [cursor based pagination](https://graphql.org/learn/pagination/#pagination-and-edges).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[FundingSourceAmountConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `FundingSourceAmountConnectionTypeEdge`

A Relay edge containing a `FundingSourceAmountConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `FundingSourceAmountType` |  | No | The item at the end of the edge |

## `FundingSourceAmountType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int` |  | No | Amount used from a funding source in minor currency. |
| `reason` | `String` |  | No | Reason why the funding source was used. |

## `FunnelField`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | The code of the field. |
| `deprecated` | `Boolean!` |  | No | Whether the field is deprecated. |
| `fieldType` | `FieldTypeChoices!` |  | No | The type of the field. |
| `name` | `String!` |  | No | The name of the field. |
| `orderInCollection` | `Int` |  | No | The order of the field in the collection. |
| `textChoices` | `[String]` |  | No | The choices for the field if applicable. |

## `GasFiltersOutput`

Filter measurements by gas parameters.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceId` | `String` |  | No | The identifier of the device associated to this reading. |
| `marketSupplyPointId` | `String` |  | No | The identifier of the market supply point associated to this reading. |
| `readingFrequencyType` | `ReadingFrequencyType` |  | No | The frequency of the reading. |
| `registerId` | `String` |  | No | The identifier of the register associated to this reading. |

## `GasSupplyPoint`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `activeAgreement` | `Agreement` |  | No | The active agreement in the supply point. The possible errors that can be raised are: - KT-ES-4110: Multiple active agreements. - KT-CT-1113: Disabled GraphQL field requested. |
| `agreements` | `[Agreement]!` |  | No | All agreements of the supply point. |
| `atrTariffs` | `[ATRTariff]` |  | No | Historical changes to the supply point ATRs. |
| `cups` | `String!` |  | No | The supply point identification number. |
| `id` | `ID` |  | No | The supply point ID. |
| `networkOperator` | `NetworkOperator` |  | No | The network operator information. |
| `status` | `String` |  | No | The supply point kraken status. |
| `supplyPeriods` | `SupplyPeriodConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The supply periods for the supply point |

## `GasTerminationOutput`

Output data related to a LeaveSupplier journey for the gas market.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `additionalInformation` | `String` |  | No | The declared additional information for the request. |
| `contactTelephoneNumber` | `String!` |  | No | The contact phone number for the request. |
| `cutReason` | `CutReason!` |  | No | The declared reason for the request. |
| `desiredEffectiveDate` | `Date` |  | No | The requested last day of supply. |
| `desiredEffectiveDateType` | `RequestedDateType!` |  | No | The requested supply end date type for the leave supplier. |
| `desiredEffectiveTime` | `Time` |  | No | The requested suppy end time for the leave supplier. |
| `supplyPointIdentifier` | `String!` |  | No | The market supply point identification number. |
| `typeOfPerson` | `PersonType` |  | No | The declared reason for the request. |

## `GenerateAffiliatesAudioRecordingPreSignedUrl`

Generate a pre-signed URL for uploading a audio file for use with affiliates.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `affiliatesAudioRecordingPreSignedUrl` | `AffiliateAudioRecordingPresignedPostType` |  | No | Input fields required to generate a presigned S3 post for affiliates audio recording. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `GenerateInkPresignedUrl`

The possible errors that can be raised are: - KT-CT-7620: Channel not supported. - KT-CT-7618: Unable to process message. - KT-CT-7624: Error when generating the presigned URL. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fields` | `JSONString!` |  | No | Presigned post fields required to upload the file. |
| `key` | `String!` |  | No | The key for the item. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `uploadUrl` | `String!` |  | No | A presigned URL for the user to upload to the quarantine bucket. |

## `GenerateLeadsFileAttachmentDownloadPreSignedUrl`

Generate a pre-signed URL for downloading a leads attachment file. The possible errors that can be raised are: - KT-CT-8933: Opportunity file attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `leadsFileAttachmentDownloadPreSignedUrl` | `LeadsFileAttachmentDownloadPresignedUrlType` |  | No | Pre-signed S3 URL for downloading the leads file attachment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `GenerateLeadsFileAttachmentsPreSignedUrl`

Generate a pre-signed URL for uploading a leads attachment file.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `leadsFileAttachmentPreSignedUrl` | `LeadsFileAttachmentPresignedPostType` |  | No | Input fields required to generate a presigned S3 post for leads file attachment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `GeneratePreSignedToken`

Mutation to generate a pre-signed token. The pre-signed, expiring and opaque tokens will be swapped for a limited scope JWT (Kraken Token). The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1120: The Kraken Token has expired. - KT-CT-1131: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `scope` | `PreSignedTokenScope` |  | No |  |
| `token` | `String` |  | No |  |
| `tokenExpiryDatetime` | `DateTime` |  | No |  |

## `GenericBackendScreen`

A generic backend screen that can be used to define any type of screen.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `name` | `String!` |  | No | The name of the screen. |
| `refreshFrequency` | `Int` |  | No | The refresh / polling frequency in milliseconds. |
| `screenData` | `String` |  | No | Serialized JSON representation of the screen. |

## `GetEmbeddedSecretForNewPaymentInstruction`

Get the client secret needed to create a new payment instruction using an embedded form. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3820: Received both ledger ID and number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `secretKey` | `String` |  | No |  |

## `GetEmbeddedSecretForNewPaymentInstructionWithoutAccount`

Get the client secret needed to create a new stored payment instruction using an embedded form. This mutation is specifically for saving payment methods for future use, without immediately creating a payment instruction tied to a specific ledger or account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `secretKey` | `String` |  | No | The client secret needed to create a new stored payment instruction. |

## `GetHostedUrlForNewPaymentInstruction`

Get external URL where the user can set up a payment instruction. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `url` | `String` |  | No | URL at which payment instruction can be set up. |

## `GetOrCreateAgreement`

The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-4910: No product exists with the given input. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1509: Unable to create agreement. - KT-CT-1511: Cannot create overlapping agreement. - KT-CT-1512: Account type does not support agreements. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreement` | `CommonAgreementType` |  | No | The agreement that was retrieved or created. |
| `created` | `Boolean` |  | No | Indicates whether a new agreement was created (true) or an existing agreement was returned (false). |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `GoodsGrant`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `currency` | `String` |  | No | Currency. |
| `grossAmount` | `Float` |  | No | Gross amount. |
| `netAmount` | `Float` |  | No | Net amount. |
| `type` | `String` |  | No | Grant type. |

## `GoodsProduct`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `availableFrom` | `Date` |  | No | Product available from. |
| `availableTo` | `Date` |  | No | Product available to. |
| `code` | `String` |  | No | Product code. |
| `currency` | `String` |  | No | Currency. |
| `customerName` | `String` |  | No | Product customer name. |
| `description` | `String` |  | No | Product description. |
| `grossPricePerUnit` | `Float` |  | No | Gross price per unit. |
| `id` | `Int` |  | No | Product ID. |
| `internalName` | `String` |  | No | Product internal name. |
| `marketName` | `String` |  | No | Market of the product. |
| `notes` | `String` |  | No | Product notes. |
| `pricePerUnit` | `Float` |  | No | Price per unit. |
| `productType` | `GoodsProductType` |  | No | Type of the product. |

## `GoodsProductConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[GoodsProductConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `GoodsProductConnectionTypeEdge`

A Relay edge containing a `GoodsProductConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `GoodsProduct` |  | No | The item at the end of the edge |

## `GoodsProductType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | Product type code. |
| `internalName` | `String` |  | No | Product type name. |

## `GoodsPurchase`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientParams` | `JSONString` |  | No | Client parameters of the purchase. |
| `code` | `String` |  | No | Purchase code. |
| `goodsGrants` | `[GoodsGrant]` |  | No | Grants that apply in this purchase. |
| `goodsSaleItems` | `[GoodsSaleItem]` |  | No | Sale items in this purchase. |
| `ledgerId` | `ID` |  | Yes (The 'ledgerId' field is deprecated. Please use 'ledgerNumber' instead. This is in the form of 'L-123456789A' - Marked as deprecated on 2024-10-22. - Scheduled for removal on or after 2025-06-25.) | Ledger ID associated to the purchase. |
| `ledgerNumber` | `String` |  | No | The ledger number associated to the purchase. |
| `marketName` | `String!` |  | No | Market name of the purchase. |
| `marketParams` | `JSONString` |  | No | Market parameters of the purchase. |

## `GoodsQuote`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | Code of the quote. |
| `goodsQuotedProducts` | `[GoodsQuotedProduct]` |  | No | Products of this quote. |
| `hasQuoteExpired` | `Boolean` |  | No | Indicates whether or not the quote is expired. |
| `id` | `ID` |  | No | ID of the quote. |
| `quotedAt` | `DateTime` |  | No | Date and time when the quote was created. |
| `totalNetAmount` | `Int` |  | No | Total net amount of the quote in cents. |

## `GoodsQuoteShare`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | The ID of the quote share. |

## `GoodsQuotedProduct`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `currency` | `String` |  | No | Currency. |
| `netAmount` | `Int` |  | No | Net amount. |
| `numberOfUnits` | `Int` |  | No | Number of units. |
| `pricePerUnit` | `Int` |  | No | Price per unit. |
| `product` | `String` |  | No | Product code. |

## `GoodsSaleItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `currency` | `String` |  | No | Currency. |
| `grossAmount` | `Float` |  | No | Gross amount. |
| `netAmount` | `Float` |  | No | Net amount. |
| `numberOfUnits` | `Int` |  | No | Number of units. |
| `pricePerUnit` | `Float` |  | No | Price per unit. |
| `product` | `String` |  | No | Product code. |

## `GrantUserAccessToBusiness`

The possible errors that can be raised are: - KT-CT-5463: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-13501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `GridTelemetry`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `powerInKw` | `Decimal` |  | No | The current power being imported from or exported to the grid in kW. A negative value indicates power is being imported from the grid; a positive value indicates power is being exported to the grid. |

## `GroupType`

Represents a group of components presented as a choice.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `customerDescription` | `String!` |  | No | Customer-facing description of the group. |
| `customerName` | `String!` |  | No | Customer-facing name for the group. |
| `identifier` | `ID!` |  | No | Unique identifier of the group. |
| `internalName` | `String!` |  | No | Internal name for the group. |
| `maxCardinality` | `Int!` |  | No | Maximum number of components that can be selected from this group. |
| `minCardinality` | `Int!` |  | No | Minimum number of components that must be selected from this group. |
| `offeringComponents` | `[OfferingComponentType]` |  | No | Nested offering components within this group. |
| `productComponents` | `[ProductComponentType]` |  | No | Product components within this group. |

## `GuaranteeOfOriginConfigurationType`

Configuration for Guarantee of Origin term, defining percentage of energy from renewable sources.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `guaranteeOfOriginPercentage` | `GuaranteeOfOriginPercentage` |  | No | The percentage of the guarantee of origin. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `HardshipAgreementType`

Represents a Hardship Agreement for a particular Account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `createdAt` | `DateTime!` |  | No |  |
| `endDate` | `Date` |  | No |  |
| `exitReason` | `HardshipAgreementExitReason` |  | No |  |
| `exitReasonDetails` | `String` |  | No | Extra details for the exit reason |
| `hardshipDetails` | `String!` |  | No | These are internal notes detailing the hardship. |
| `hardshipEntryReason` | `HardshipAgreementHardshipEntryReason` |  | No |  |
| `hardshipType` | `HardshipAgreementHardshipType!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `paymentPlanDetails` | `String!` |  | No |  |
| `startDate` | `Date!` |  | No |  |

## `HeldStatus`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isHeld` | `Boolean` |  | No | Whether a statement is currently held. |
| `reason` | `String` |  | No | Reason for statement being held. |

## `ImageType`

A media element containing an image.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accessibilityHidden` | `Boolean` |  | No | Whether the element is hidden from view. |
| `accessibilityLabel` | `String` |  | No | Accessible description of the element. |
| `horizontalAlignment` | `Alignment` |  | No | The horizontal alignment of the media. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `mediaUrl` | `String!` |  | No | The resource URL of the media. |
| `typename` | `String` |  | No | The name of the object's type. |
| `width` | `ItemSizeType` |  | No | The measurement of the element. |

## `ImportReadingsConnection`

Pagination for readings representing incoming utility flow e.g., usage or consumption..

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ImportReadingsEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ImportReadingsEdge`

A Relay edge containing a `ImportReadings` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `Reading` |  | No | The item at the end of the edge |

## `InboundCallAverageWaitTimeType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `recent` | `Int` |  | No | The average number of seconds passed before an inbound call is answered. This value represents the calls received in the last 30 minutes. |
| `yesterday` | `Int` |  | No | The average number of seconds passed before an inbound call is answered. This value represents the calls received on the previous day. |

## `InboundCallType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | If known, this is the account that a call is about. For inbound calls, we attempt to identify the account based on the phone number of the incoming call. For outbound calls, the account will be automatically set if the call was initiated from an account page. For all call types, the account can be updated, for example to correct a misidentification of an incoming call. |
| `id` | `ID!` |  | No | The ID of the call. |
| `initialCallerIdentification` | `PhoneNumberIdentificationType!` |  | No | When an inbound call is received, we identify all entities linked to the phone number of the caller. |
| `metadata` | `[CallMetadataItemType]!` |  | No | Metadata related to the call, for example metrics or data passed via an interactive voice response (IVR). |

## `IndexationOptionsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `escalationStartAt` | `DateTime` |  | No | The escalation start date for the product rate override configuration. |
| `indexCode` | `String` |  | No | The index code for the product rate override configuration. |

## `InitializeAccountResult`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | The account number of the newly created account or the existing account to be re-used. |
| `isNewAccount` | `Boolean` |  | No | Was a new account created. |

## `InitializeUserResult`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isNewUser` | `Boolean` |  | No | Was a new user created. |
| `userNumber` | `String` |  | No | The user number of the newly created user or the existing user to be re-used. |

## `InitiateHostedStandalonePayment`

Initiate a standalone payment and return the url where the customer can complete it. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3943: Invalid ledger. - KT-CT-3957: No collection method provided. - KT-CT-3958: Provide either ledger ID or ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payment` | `InitiateHostedStandalonePaymentOutput` |  | No | The details required to refer to and complete a hosted payment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `InitiateHostedStandalonePaymentOutput`

Tokens required to collect and retrieve a standalone payment.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `retrievalToken` | `String!` |  | No | The retrieval token for this standalone payment. |
| `url` | `String!` |  | No | The url for the customer to complete the payment. |

## `InitiateProductSwitch`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4619: Quote with given code not found. - KT-CT-4624: Unable to accept the given product code. - KT-CT-4924: Unauthorized. - KT-CT-4626: No product selected for the given quote code. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-1509: Unable to create agreement. - KT-CT-1507: Agreement product switch date is not within the acceptable range. - KT-CT-4640: Unable to get market or client params from quoted product. - KT-CT-4627: No products are available for this quote. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `productCode` | `String!` |  | No | The selected product for a specific product switch. |
| `switchDate` | `Date!` |  | No | The date at which the product switch becomes effective. |

## `InitiateStandalonePayment`

Initiate a standalone payment and return the client secret required to complete it. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3943: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payment` | `InitiateStandalonePaymentOutput` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `InitiateStandalonePaymentOutput`

Tokens required to collect and retrieve a standalone payment.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `retrievalToken` | `String!` |  | No | The retrieval token for this standalone payment. |
| `secretToken` | `String!` |  | No | The secret used to collect the payment. |

## `InkBucket`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `icon` | `String` |  | No | The icon code point. |
| `id` | `ID!` |  | No | The ID of the object |
| `name` | `String!` |  | No | The ink bucket name. |

## `InkContactChannelIdentities`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `all` | `[InkContactChannelIdentity!]!` |  | No | All contacts for this conversation. |
| `default` | `InkContactChannelIdentity` |  | No | The default contact for this conversation. |

## `InkContactChannelIdentity`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `channel` | `InkCommunicationChannel!` |  | No | The channel of the contact. |
| `displayName` | `String!` |  | No | The name to display to the user. |
| `handle` | `String!` |  | No | The handle. |

## `InkConversation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | The number of the Kraken account that the conversation is from. |
| `accountUsers` | `[EspAccountUserType!]` |  | No | The account users on the conversation. |
| `buckets` | `[InkBucket!]` |  | No | The buckets the conversation is currently in. |
| `contactChannelIdentities` | `InkContactChannelIdentities!` |  | No | The contact channel identities associated with this conversation. |
| `events` | `InkConversationEventsConnection!` | `before: String, after: String, first: Int, last: Int` | No | Conversation events. |
| `id` | `ID!` |  | No |  |
| `status` | `InkConversationStatus!` |  | No | The status of the conversation. |
| `tags` | `[InkTag!]` |  | No | The tags on the conversation. |

## `InkConversationEventsConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edges` | `[InkConversationEventsEdge!]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |

## `InkConversationEventsEdge`

A Relay edge containing a `InkConversationEvents` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `InkConversationEvent!` |  | No | The item at the end of the edge |

## `InkEmail`

This type wraps around the `Message` type for emails.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `[InkMessageAttachment!]!` |  | No | Attachments on the message. |
| `cc` | `[String!]!` |  | No | CC recipients on the message. |
| `contactChannelIdentity` | `InkContactChannelIdentity!` |  | No | The contact channel identity. |
| `conversationId` | `Int!` |  | No | The integer ID of the conversation this message belongs to. |
| `conversationRelayId` | `String!` |  | No | The relay ID of the conversation this message belongs to. |
| `delivery` | `InkMessageDelivery!` |  | No | The delivery status of the message. |
| `direction` | `InkMessageDirection!` |  | No | The direction of the email. |
| `displayContent` | `String!` |  | No | The content of the message. |
| `fromHandle` | `String!` |  | No | From email address. |
| `isChannelEmail` | `Boolean!` |  | No | Is this an message an email. |
| `occurredAt` | `DateTime!` |  | No | The time the message was sent/received. |
| `subject` | `String!` |  | No | The email subject. |
| `tags` | `[InkTag!]!` |  | No | All Tags associated with a message. |
| `toHandles` | `[String!]` |  | No | The addresses that the message was sent to. |

## `InkGenericMessage`

This message type is used for messages that belong to contact channels without a more granular message type.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contactChannelIdentity` | `InkContactChannelIdentity!` |  | No | The contact channel identity. |
| `conversationId` | `Int!` |  | No | The integer ID of the conversation this message belongs to. |
| `conversationRelayId` | `String!` |  | No | The relay ID of the conversation this message belongs to. |
| `delivery` | `InkMessageDelivery!` |  | No | The delivery status. |
| `direction` | `InkMessageDirection!` |  | No | The direction of the message. |
| `displayContent` | `String!` |  | No | The content of the message. |
| `fromHandle` | `String!` |  | No | The identity the message was sent from. |
| `id` | `ID!` |  | No | The ID of the object |
| `occurredAt` | `DateTime!` |  | No | The time the message was sent/received at. |
| `toHandle` | `String!` |  | No | The identity the message was sent to. |

## `InkLine`

This type wraps around the `Message` type for LINE message.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `[InkMessageAttachment!]!` |  | No | Attachments on the LINE message. |
| `contactChannelIdentity` | `InkContactChannelIdentity!` |  | No | The contact channel identity. |
| `delivery` | `InkMessageDelivery!` |  | No | The delivery status of the message. |
| `direction` | `InkMessageDirection!` |  | No | The direction of the message. |
| `fromHandle` | `String!` |  | No | From LINE id. |
| `isChannelLine` | `Boolean!` |  | No | Is this a LINE message. |
| `lineMessage` | `LineMessage!` |  | No | The line message content. |
| `occurredAt` | `DateTime!` |  | No | The time the message was sent/received. |
| `tags` | `[InkTag!]!` |  | No | All Tags associated with a message. |
| `toHandle` | `String!` |  | No | To LINE id. |

## `InkLiveChatConversation`

Ink live chat

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `relayId` | `ID!` |  | No | The relay ID of the live chat conversation. |

## `InkLiveChatMessage`

This type wraps around the `Message` type for a Live Chat message.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contactChannelIdentity` | `InkContactChannelIdentity!` |  | No | The contact channel identity. |
| `delivery` | `InkMessageDelivery!` |  | No | The delivery status. |
| `direction` | `InkMessageDirection!` |  | No | The direction of the message. |
| `displayContent` | `String!` |  | No | The content of the message. |
| `fromHandle` | `String!` |  | No | The identity the message was sent from. |
| `id` | `ID!` |  | No | The ID of the object |
| `occurredAt` | `DateTime!` |  | No | The time the message was sent/received at. |
| `toHandle` | `String!` |  | No | The identity the message was sent to. |

## `InkMessageAttachment`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fetchUrl` | `String` |  | No | The url for fetching the attachment. |
| `filename` | `String!` |  | No | The filename. |
| `sizeInBytes` | `Int` |  | No | The size in bytes. |

## `InkMessageAttributes`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountType` | `String` |  | No | The type of the account linked to the conversation of the message. |
| `accounts` | `[String!]!` |  | No | The list of accounts related to the message. |
| `buckets` | `[String!]` |  | No | The list of the buckets the message is in. |
| `conversationId` | `Int!` |  | No | The ID of the conversation this message belongs to. |
| `hourOccurredAt` | `Int!` |  | No | The hour at which the message arrived in Ink. |
| `hoursWaiting` | `Int!` |  | No | The number of hours the customer has been waiting for a response to their previous message. |
| `isAssignedToUserBucket` | `Boolean!` |  | No | Whether the conversation that the message belongs to is assigned to a user bucket. |
| `isFirstFromContact` | `Boolean!` |  | No | Whether the message is the first one sent by the contact. |
| `isNewThread` | `Boolean!` |  | No | Whether the message starts a new thread in its conversation. |
| `opsTeam` | `String` |  | No | The operation team that handles the message. |
| `recentlyReceivedAutoReplies` | `[String!]!` |  | No | The codes of the auto replies that have been sent to the contact in the last 6 months. |
| `replyToCommsSms` | `String` |  | No | The body of the latest comms SMS message sent to the customer, if the message is an sms. |
| `weekDayOccurredAt` | `Int!` |  | No | The week day at which the message arrived in Ink. |

## `InkMessageDelivery`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `status` | `InkMessageDeliveryStatus!` |  | No | Message delivery status. |

## `InkNewMessage`

This types is used for both the message-received and message-sent conversation events.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `InkMessage!` |  | No | The message. |
| `occurredAt` | `DateTime!` |  | No | The time the conversation event occurred. |

## `InkNote`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `content` | `String!` |  | No | The content of the ink note. |
| `id` | `ID!` |  | No | The ID of the object |
| `isPinned` | `Boolean!` |  | No | The note is pinned, so that it's always visible in the conversation. |
| `occurredAt` | `DateTime!` |  | No | The datetime at which the conversation note occurred. |

## `InkPost`

This type wraps around the `Message` type for Post.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contactChannelIdentity` | `InkContactChannelIdentity!` |  | No | The contact channel identity. |
| `conversationId` | `Int!` |  | No | The integer ID of the conversation this message belongs to. |
| `conversationRelayId` | `String!` |  | No | The relay ID of the conversation this message belongs to. |
| `displayContent` | `String!` |  | No | The notes left when a message was uploaded. |
| `fromHandle` | `String!` |  | No | The from property id. |
| `isChannelPost` | `Boolean!` |  | No | Determine if the message is a post message. |
| `rawPlainTextContent` | `String!` |  | No | The content of the message. |
| `toHandle` | `String!` |  | No | The to property id. |

## `InkSMS`

This type wraps around the `Message` type for SMS.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contactChannelIdentity` | `InkContactChannelIdentity!` |  | No | The contact channel identity. |
| `delivery` | `InkMessageDelivery!` |  | No | The delivery status. |
| `direction` | `InkMessageDirection!` |  | No | The direction of the message. |
| `displayContent` | `String!` |  | No | The content of the message. |
| `fromHandle` | `String!` |  | No | The phone number the message was sent from. |
| `isChannelSms` | `Boolean!` |  | No | Is this an SMS message. |
| `occurredAt` | `DateTime!` |  | No | The time the message was sent/received at. |
| `tags` | `[InkTag!]!` |  | No | All Tags associated with a message. |
| `toHandle` | `String!` |  | No | The phone number the message was sent to. |

## `InkStoryline`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `createdAt` | `DateTime!` |  | No |  |
| `entries` | `[InkStorylineEntry!]!` |  | No | The entries in the storyline. |
| `generatedAt` | `DateTime!` |  | No | When the storyline was generated. |
| `id` | `ID!` |  | No | The ID of the object |
| `knowledgeArticleIds` | `[BigInt!]` |  | No |  |
| `neuralinkRequestId` | `UUID!` |  | No |  |
| `summary` | `String!` |  | No |  |
| `topic` | `String!` |  | No |  |
| `updatedAt` | `DateTime!` |  | No |  |

## `InkStorylineEntry`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `content` | `String!` |  | No | The content of the storyline entry. |
| `contentId` | `BigInt` |  | No | The optional related object ID of the entry. |
| `entryType` | `String!` |  | No | The type of the storyline entry. |
| `id` | `ID!` |  | No | The ID of the object |
| `isRootCause` | `Boolean` |  | No | Whether this entry is identified as the root cause of the issue. |
| `occurredAt` | `DateTime!` |  | No | The time the storyline entry occurred. |
| `url` | `String` |  | No | Optional URL related to the storyline entry. |

## `InkTag`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No | The ID of the object |
| `name` | `String!` |  | No | Tag for a message. |

## `InkTwilioWhatsApp`

This type wraps around the `Message` type for a Twilio WhatsApp message.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contactChannelIdentity` | `InkContactChannelIdentity!` |  | No | Twilio WhatsApp message contact channel identity. |
| `delivery` | `InkMessageDelivery!` |  | No | Message delivery status. |
| `direction` | `InkMessageDirection!` |  | No | The direction of the message. |
| `fromHandle` | `String!` |  | No | From WhatsApp number. |
| `occurredAt` | `DateTime!` |  | No | Date when the conversation event was created. |
| `tags` | `[InkTag!]!` |  | No | All Tags associated with a message. |
| `toHandle` | `String!` |  | No | To WhatsApp number. |
| `vendorId` | `String` |  | No | The vendor id. |
| `whatsappContent` | `WhatsAppTextMessage!` |  | No | Whatsapp message content. |

## `InkWhatsApp`

This type wraps around the `Message` type for WhatsApp message.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contactChannelIdentity` | `InkContactChannelIdentity!` |  | No | Whatsapp message contact channel identity. |
| `delivery` | `InkMessageDelivery!` |  | No | Whatsapp message delivery status. |
| `direction` | `InkMessageDirection!` |  | No | The direction of the message. |
| `fromHandle` | `String!` |  | No | From WhatsApp phone number. |
| `isChannelWhatsapp` | `Boolean!` |  | No | Whether or not the message is a whatsapp message. |
| `occurredAt` | `DateTime!` |  | No | Date when the conversation event was created. |
| `tags` | `[InkTag!]!` |  | No | All Tags associated with a message. |
| `toHandle` | `String!` |  | No | Whatsapp contact phone number. |
| `vendorId` | `String` |  | No | The vendor id. |
| `whatsappContent` | `WhatsAppTextMessage!` |  | No | Whatsapp message content. |

## `InputFieldErrorType`

Represents a validation error for a specific input field.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `errorMessage` | `String!` |  | No | The error message to display for this field. |
| `inputFieldKey` | `String!` |  | No | The key of the input field with the error. |
| `inputFieldValue` | `String!` |  | No | The value that was submitted for the field. |

## `InstigateContractVariationOutput`

Output type for instigating a contract variation.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contract` | `Contract` |  | No | The contract with the varied terms. |

## `IntegerCharacteristicValueType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `characteristic` | `CharacteristicType` |  | No | The product characteristic. |
| `integerValue` | `Int!` |  | No | The integer value of the characteristic. |
| `value` | `String` |  | No | A string representation of a characteristic value, for convenience. |

## `IntegerType`

Graphene type object to represent integer values

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `integerValue` | `Int!` |  | No | Value of this field. |

## `InternalCompanyConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[InternalCompanyConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `InternalCompanyConnectionTypeEdge`

A Relay edge containing a `InternalCompanyConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `InternalCompanyType` |  | No | The item at the end of the edge |

## `InternalCompanyType`

Represents an internal company.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `displayableNumber` | `String!` |  | No | The internal company's displayable number, which is a human-friendly identifier. |
| `id` | `ID!` |  | No | The internal company's ID. |
| `legalAddress` | `RichAddressType` |  | No | The legal address of the internal company. |
| `name` | `String!` |  | No | The internal company's name. |
| `primaryRegistrationNumber` | `String` |  | No | The primary registration number of the internal company. |
| `primaryTaxIdentifierNumber` | `String` |  | No | The primary tax identifier number of the internal company. |
| `secondaryRegistrationNumber` | `String` |  | No | The secondary registration number of the internal company. |

## `IntervalMeasurementType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accumulation` | `Decimal` |  | Yes (The 'accumulation' field is deprecated. This field is no longer required. - Marked as deprecated on 2024-10-15. - Scheduled for removal on or after 2024-11-01.) |  |
| `durationInSeconds` | `Int!` |  | No | The duration of the measurement. |
| `endAt` | `DateTime!` |  | No | The end datetime of the measurement. |
| `metaData` | `MeasurementsMetadataOutput` |  | No | This type will return more granular data about the measurement. |
| `readAt` | `DateTime!` |  | No | The datetime the measurement was taken. |
| `source` | `String!` |  | No | The data source of the measurement. |
| `startAt` | `DateTime!` |  | No | The start datetime of the measurement. |
| `unit` | `String!` |  | No | The unit of the measurement. |
| `value` | `Decimal!` |  | No | The value of the measurement. |

## `InvalidatePaymentInstruction`

Invalidates a payment instruction. The possible errors that can be raised are: - KT-CT-3926: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `instruction` | `InvalidatePaymentInstructionOutput` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `InvalidatePaymentInstructionOutput`

Output for invalidating an arbitrary payment instruction.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `Int` |  | No |  |

## `InvalidatePreSignedToken`

Invalidate a previously issued expiring/pre-signed token. This mutation can be used to invalidate the token itself. To invalidate tokens issued to a particular user, use InvalidatePreSignedTokensForUser mutation. The possible errors that can be raised are: - KT-CT-1129: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `token` | `PreSignedToken` |  | No |  |

## `InvalidatePreSignedTokensForUser`

Invalidate pre-signed tokens previously issued to a particular user. This mutation can invalidate all pre-signed tokens issued to a customer, or only tokens of a given scope. The possible errors that can be raised are: - KT-CT-1129: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `tokens` | `[PreSignedToken]` |  | No |  |

## `InvalidateRefreshToken`

Invalidate a previously issued refresh token. This mutation can be used to invalidate the token itself. To invalidate tokens issued to a particular user, use InvalidateRefreshTokensForUser. The possible errors that can be raised are: - KT-CT-1130: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `token` | `RefreshToken` |  | No |  |

## `InvalidateRefreshTokensForUser`

Invalidate refresh tokens previously issued to a particular user. This mutation will invalidate all refresh tokens issued to a customer. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `tokens` | `[RefreshToken]` |  | No |  |

## `InverterTelemetry`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `connectionStatus` | `ConnectionStatus` |  | No | Whether the inverter is currently connected (online/offline). |
| `powerInKw` | `Decimal` |  | No | The current power flowing through the inverter in kW. A negative value indicates that power is being drawn in to charge the battery; a positive value indicates power is being exported to the property (and, possibly, the grid) from the battery and/or solar panels. |

## `InverterVariantType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `make` | `String` |  | No | The make (manufacturer) of the device. |

## `InvoiceBillingDocumentConnectionTypeConnection`

An invoice is a bill that contains individual transactions (i.e. charges, credits, payments, and repayments). These may come from any period of time.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[InvoiceBillingDocumentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `InvoiceBillingDocumentConnectionTypeEdge`

A Relay edge containing a `InvoiceBillingDocumentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `InvoiceBillingDocumentType` |  | No | The item at the end of the edge |

## `InvoiceBillingDocumentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `annulledBy` | `AnnulmentBillingDocumentType` |  | No | Billing document that annuls this invoice. |
| `documentDebtPosition` | `BillingDocumentPositionType` |  | No | Position of the billing document in the delinquent debt tracking system. |
| `earliestChargeAt` | `DateTime` |  | No | The earliest charge timestamp of the invoice. |
| `firstIssued` | `DateTime` |  | No | First time the invoice was issued. |
| `id` | `Int` |  | No | Unique identifier for the invoice billing document. |
| `invoicedAmount` | `Int` |  | No | The invoiced amount of the billing document. |
| `latestChargeAt` | `DateTime` |  | No | The latest charge timestamp of the invoice. |
| `number` | `String` |  | No | The unique billing document's reference that can be used for identifying it externally. |
| `paymentDueDate` | `Date` |  | No | The date due for payment for the invoice. |
| `pdfUrl` | `String` |  | No | URL to the PDF of the Invoice. |
| `totalCharges` | `InvoiceTotalType` |  | No | The total amounts for all charges on the invoice. |
| `totalCredits` | `InvoiceTotalType` |  | No | The total amounts for all credits on the invoice. |
| `transactions` | `BillTransactionConnectionTypeConnection` | `orderBy: TransactionsOrderBy = POSTED_DATE_DESC, before: String, after: String, first: Int, last: Int` | No | Transactions on the invoice |

## `InvoiceTotalType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `grossTotal` | `Int` |  | No | The gross total amount for the statement (in minor currency units). |
| `netTotal` | `Int` |  | No | The net total amount for the statement (in minor currency units). |
| `taxTotal` | `Int` |  | No | The total amount of tax on the statement (in minor currency units). |

## `InvoiceType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `BillingAttachmentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No |  |
| `billType` | `BillTypeEnum` |  | No | The type of the bill. |
| `fromDate` | `Date` |  | No | The date of the bill is covered from. |
| `grossAmount` | `Int` |  | No | This field returns the total gross amount of the bill in pence. |
| `id` | `ID` |  | No | The ID of the bill. |
| `identifier` | `String` |  | No | The unique identifier of a bill. It will usually be present on the billing document itself. Note: a bill that hasn't been issued yet will not have an identifier; and not all issued bills will have an identifier assigned to them, in which case this will be null. |
| `isAnnulled` | `Boolean!` |  | No | Whether the billing document has been annulled. |
| `issuedDate` | `Date` |  | No | The date the bill was sent to the customer. |
| `representations` | `BillRepresentationConnectionTypeConnection` | `code: String = null, before: String, after: String, first: Int, last: Int` | No |  |
| `reversalsAfterClose` | `StatementReversalsAfterClose!` |  | No | How many charges have been reversed after the close date. |
| `temporaryUrl` | `String` |  | Yes (The 'temporaryUrl' field is deprecated. This field is deprecated. Use the 'attachments' field instead. - Marked as deprecated on 2024-09-16. - Scheduled for removal on or after 2025-09-01.) | Requesting this field generates a temporary URL at which bill is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). This field can raise an error with errorClass NOT_FOUND if the bill document has not been created/issued yet. This field is deprecated use 'attachments' field instead. |
| `toDate` | `Date` |  | No | The date of the bill is covered to. |
| `totalCharges` | `InvoiceTotalType` |  | No | The total amounts for all charges on the invoice. |
| `totalCredits` | `InvoiceTotalType` |  | No | The total amounts for all credits on the invoice. |
| `totalPayments` | `Int` |  | No | The sum of all previous payments made that are included towards this invoice. |
| `transactions` | `BillTransactionConnectionTypeConnection` | `ledgerNumber: String = null, transactionTypes: [TransactionTypeFilter] = [], orderBy: TransactionsOrderBy = POSTED_DATE_DESC, before: String, after: String, first: Int, last: Int` | No | Transactions on the given billing document. |

## `JoinSupplierAcceptTermsAndConditions`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean` |  | No | Indicator that the mutation has completed successfully. |

## `JoinSupplierLedgerAssignmentConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[JoinSupplierLedgerAssignmentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `JoinSupplierLedgerAssignmentConnectionTypeEdge`

A Relay edge containing a `JoinSupplierLedgerAssignmentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `JoinSupplierLedgerAssignmentType` |  | No | The item at the end of the edge |

## `JoinSupplierLedgerAssignmentType`

A ledger with its associated supply points. Multiple supply points may be assigned to the same ledger. This type groups them for convenient querying.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `ledgerName` | `String` |  | No | The ledger name. |
| `ledgerNumber` | `String` |  | No | The ledger number. |
| `ledgerSupplyPoints` | `[LedgerSupplyPointType]` |  | No | The supply points associated with the ledger. |
| `ledgerType` | `String` |  | No | The ledger type. |

## `JoinSupplierProcessConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[JoinSupplierProcessConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `JoinSupplierProcessConnectionTypeEdge`

A Relay edge containing a `JoinSupplierProcessConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `JoinSupplierProcessType` |  | No | The item at the end of the edge |

## `JoinSupplierProcessDataType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `affiliateLink` | `AffiliateLinkType` |  | No | Affiliate link for the join supplier journey. |
| `note` | `String` |  | No | The note associated with this join supplier process data. |
| `offerGroupIdentifier` | `NonEmptyString` |  | No | Unique identifier for the offer group. |
| `requestedAt` | `DateTime!` |  | No | When the journey was requested. |
| `salesChannel` | `String` |  | No | Sales channel. |
| `salesSubchannel` | `String` |  | No | Sales subchannel. |
| `storedPaymentMethodDetailsReference` | `String` |  | No | Reference to the stored payment method details. |
| `supplyPointContexts` | `[SupplyPointContextDataInterface]` |  | No | The supply point context data. |

## `JoinSupplierProcessType`

Represents a Join Supplier process.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contractIdentifiers` | `[String]` |  | No | Contract identifiers associated with this join supplier process. |
| `currentProcessData` | `JoinSupplierProcessDataType` |  | No | The current process data associated with the Join Supplier process. |
| `id` | `ID` |  | No | The ID or the primary key of the lifecycle process. |
| `ledgerAssignments` | `JoinSupplierLedgerAssignmentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The ledgers associated with the supply points in the process. |
| `number` | `String` |  | No | The unique identifier of the process. |
| `status` | `LifecycleSupplyPointProcessStatus` |  | No | The status of the process. |
| `subtype` | `String` |  | No | The subtype of the process. |
| `supplyPoints` | `SupplyPointConnectionTypeConnection!` | `before: String, after: String, first: Int, last: Int` | No | The supply points associated with the process. |

## `KrakenDrivenSalesInfoType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `identifier` | `String` |  | No | The unique identifier for the sales record. |
| `opportunityNumber` | `String` |  | No | The opportunity code associated with the sales record. |

## `KrakenFlexDeviceType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `chargePointMake` | `String` |  | No |  |
| `chargePointModel` | `String` |  | No |  |
| `chargePointPowerInKw` | `Decimal` |  | No |  |
| `createdAt` | `DateTime` |  | No |  |
| `hasToken` | `Boolean` |  | No |  |
| `krakenflexDeviceId` | `String` |  | No |  |
| `provider` | `ProviderChoices` |  | No | The third party that provides control over this device. |
| `stateOfChargeLimit` | `StateOfChargeLimit` |  | No | Maximum state of charge (SoC) limit telemetry. |
| `status` | `String` |  | No |  |
| `suspended` | `Boolean` |  | No |  |
| `testDispatchFailureReason` | `TestDispatchAssessmentFailureReason` |  | No | The reason for the most recent failed test dispatch (if any). |
| `vehicleBatterySizeInKwh` | `Decimal` |  | No |  |
| `vehicleMake` | `String` |  | No |  |
| `vehicleModel` | `String` |  | No |  |

## `KrakenTrackedSalesInfoType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `affiliateOrganisationName` | `String` |  | No | The name of the affiliate organisation associated with the sales record. |
| `identifier` | `String` |  | No | The unique identifier for the sales record. |
| `salesChannel` | `String` |  | No | The sales channel associated with the sales record. |

## `KrakenVersionType`

Information about what version of Kraken is being executed by this service.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `SHA` | `String` |  | No | The git commit SHA that is being executed. |
| `isPinned` | `Boolean` |  | No | Whether this version is pinned to a specific version. |
| `number` | `String` |  | No | The version number that is being executed. |

## `LatePaymentFeesType`

Represents later payment fees to be applied in a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `flatFeeAmount` | `Decimal` |  | No | The flat fee amount for late payment. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `interestPolicyName` | `String` |  | No | The interest policy to use for late payment fee calculations. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `percentageFee` | `Decimal` |  | No | The percentage fee for late payment. |
| `percentageIntervalDays` | `Decimal` |  | No | The interval in days for the percentage fee (1=daily, 7=weekly, 30=monthly, 365=yearly). |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `Lead`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `assignedToOrganization` | `AffiliateOrganisationType` |  | No | Affiliate organization assigned to this lead. |
| `assignedToUsername` | `String` |  | No | The username of the user the lead is assigned to. |
| `consents` | `[ConsentOutput]` |  | No | List of consents for the lead. |
| `contacts` | `[LeadContactDetailsType]` | `input: LeadContactDetailsFiltersInput` | No | The contacts for the lead. |
| `leadType` | `String` |  | No | The type of the lead. |
| `nationalId` | `String` |  | No | National Identifier of the lead. |
| `number` | `String!` |  | No | Lead number. |
| `opportunities` | `[OpportunityOutput]` | `input: OpportunitiesQueryInput` | No | List of opportunities for the lead. |
| `salesChannel` | `SalesChannelType` |  | No | The sales channel that this lead was captured by. |
| `salesFunnel` | `SalesFunnel` |  | No | The sales funnel this lead is in. |
| `stage` | `SalesFunnelStage` |  | No | The current stage of the sales funnel that this lead is in. |

## `LeadBlockListValidationOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `blockListHits` | `[String]` |  | No | List of block list hits found. |
| `valid` | `Boolean` |  | No | Indicates if the block list validation passed. |

## `LeadContactDetailsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `email` | `String` |  | No | The email address of the contact. |
| `familyName` | `String` |  | No | The family name of the contact. |
| `givenName` | `String` |  | No | The given name of the contact. |
| `phoneNumber` | `String` |  | No | The phone number of the contact. |
| `roles` | `[LeadContactRoles]` |  | No | The roles of the contact. |

## `LeadIdType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `leadId` | `ID!` |  | Yes (The 'leadId' field is deprecated. Use `number` instead. - Marked as deprecated on 2025-11-24. - Scheduled for removal on or after 2026-02-01.) | The ID of the lead. |
| `number` | `String!` |  | No | The number of the lead. |

## `LeadOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | Lead's linked account number. |
| `assignedToAffiliateNumber` | `String` |  | No | The affiliate's name this opportunity is assigned to. |
| `assignedToTeam` | `String` |  | No | Team assigned to this lead. |
| `assignedToUser` | `String` |  | No | User assigned to this lead. |
| `billingAddress` | `AddressOutput` |  | No | Lead billing address. |
| `billingName` | `String` |  | No | Lead billing name. |
| `billingRichAddress` | `RichAddressType` |  | No | Lead billing rich address. |
| `brand` | `String` |  | No | Lead brand. |
| `consents` | `[ConsentOutput]` |  | No | List of consents for the lead. |
| `email` | `String` |  | No | Lead legal contact email. |
| `extraDetailItems` | `[ExtraDetail]` |  | No | Extra details about the lead as key/value pairs. |
| `extraDetails` | `JSONString` |  | Yes (The 'extraDetails' field is deprecated. Use `extraDetailsItems` instead, which provides a structured key/value format. - Marked as deprecated on 2026-01-14. - Scheduled for removal on or after 2026-07-14.) | Extra details about the lead. |
| `familyName` | `String` |  | No | Lead legal family name. |
| `funnel` | `SalesFunnel` |  | No | The lead funnel this lead is in. |
| `givenName` | `String` |  | No | Lead legal given name. |
| `leadId` | `ID` |  | No | Lead ID. |
| `leadType` | `String` |  | No | The type of the lead. |
| `nationalId` | `String` |  | No | National Identifier of the lead. |
| `number` | `String` |  | No | Lead number. |
| `phoneNumber` | `String` |  | No | Lead legal contact phone number. |
| `salesChannel` | `String` |  | No | Lead sales channel. |
| `stage` | `String` |  | No | Current stage in a funnel. |

## `LeadSupplyPointType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `externalIdentifier` | `String` |  | No | Supply point identifier. |
| `marketName` | `String` |  | No | Market code of the supply point. |

## `LeadsConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[LeadsEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `LeadsEdge`

A Relay edge containing a `Leads` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `Lead` |  | No | The item at the end of the edge |

## `LeadsFileAttachmentDownloadPresignedUrlType`

Metadata returned when generating a pre-signed download URL for a leads file attachment.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `preSignedUrl` | `String!` |  | No | The pre-signed S3 download URL. |

## `LeadsFileAttachmentPresignedPostType`

Metadata returned when generating a pre-signed post URL for a leads file attachment.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `bucket` | `String!` |  | No | The S3 bucket. |
| `fields` | `JSONString!` |  | No | The fields to be included in the pre-signed post. |
| `key` | `String!` |  | No | The S3 bucket key. |
| `preSignedUrl` | `String!` |  | No | The pre-signed S3 URL. |

## `LeavePropertyProcessConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[LeavePropertyProcessConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `LeavePropertyProcessConnectionTypeEdge`

A Relay edge containing a `LeavePropertyProcessConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `LeavePropertyProcessType` |  | No | The item at the end of the edge |

## `LeavePropertyProcessType`

Represents a Leave Property process.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | The ID or the primary key of the lifecycle process. |
| `status` | `LifecycleSupplyPointProcessStatus` |  | No | The status of the process. |
| `supplyPoints` | `SupplyPointConnectionTypeConnection!` | `before: String, after: String, first: Int, last: Int` | No | The supply points associated with the process. |

## `LeaveSupplierCancelled`

Output of a LeaveSupplier journey cancellation.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String!` |  | No | The message to display to the user on cancellation. |

## `LeaveSupplierInstigated`

Termination was successfully initiated.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `leaveSupplierProcessId` | `ID` |  | Yes (The 'leaveSupplierProcessId' field is deprecated. Process IDs are deprecated, please use 'number' instead. - Marked as deprecated on 2025-08-06. - Scheduled for removal on or after 2025-09-30.) | The ID of the newly created or existing leave supplier process. |
| `message` | `String!` |  | No | The message to display to the user on termination initiation. |
| `number` | `ID!` |  | No | The number of the newly created or existing leave supplier process. |

## `LeaveSupplierMarketOutputType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `electricitySupplyPointData` | `[ElectricityTerminationOutput]` |  | No | A list of Electricity leave supplier details. |
| `gasSupplyPointData` | `[GasTerminationOutput]` |  | No | A list of Gas leave supplier details. |

## `LeaveSupplierProcessConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[LeaveSupplierProcessConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `LeaveSupplierProcessConnectionTypeEdge`

A Relay edge containing a `LeaveSupplierProcessConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `LeaveSupplierProcessType` |  | No | The item at the end of the edge |

## `LeaveSupplierProcessDataType`

Represents data associated with a Leave Supplier process.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `futureBillingAddress` | `RichAddressType` |  | No | The future billing address for the customers account. |
| `marketData` | `LeaveSupplierMarketOutputType` |  | No | The market data associated with the process. |
| `requestedAt` | `DateTime` |  | No | The time at which the process was initiated. |
| `requestedSupplyEndDate` | `Date` |  | No | The requested supply end date. |
| `waiveExitFee` | `Boolean` |  | No | Whether the exit fee is to be waived. |

## `LeaveSupplierProcessType`

Represents a Leave Supplier process. Conceptually, it contains information related to supply points that are associated with a Leave Supplier journey.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | The ID or the primary key of the lifecycle process. |
| `number` | `String` |  | No | The unique identifier of the process. |
| `processData` | `LeaveSupplierProcessDataType` |  | No | Data associated with the Leave Supplier process. |
| `status` | `LifecycleSupplyPointProcessStatus` |  | No | The status of the process. |
| `subtype` | `String` |  | No | The subtype of the process. |
| `supplyEndDate` | `Date` |  | No | The supply end date for the Leave Supplier process. |
| `supplyPoints` | `SupplyPointConnectionTypeConnection!` | `before: String, after: String, first: Int, last: Int` | No | The supply points associated with the process. |

## `LeaveSupplierReversed`

Output of a LeaveSupplier journey reversal.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String!` |  | No | The message to display to the user on reversal. |

## `LeaveSupplierUpdated`

Leave supplier was successfully updated.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String!` |  | No | The message to display to the user on leave supplier update. |

## `LedgerSupplyPointType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `externalIdentifier` | `String` |  | No | Supply point external identifier. Empty string if not set. |
| `marketName` | `String` |  | No | Market name for the supply point. |

## `LedgerType`

Ledgers provide the foundation of Kraken’s bookkeeping functionality. Similar to a bank account, they allow us to keep track of financial activity on a particular Kraken account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptsPayments` | `Boolean` |  | No | Whether payments can be posted onto this ledger. |
| `affectsAccountBalance` | `Boolean` |  | No | Whether this ledger's balance contributes to the account's balance. |
| `agreements` | `AgreementConnection` | `before: String, after: String, first: Int, last: Int` | No | The charged supply agreements of the ledger. |
| `amountOwedByCustomer` | `Int` |  | No | The amount owed from the customer perspective. A positive value implies the customer owes the business, while a negative amount implies the customer is in credit. |
| `balance` | `Int` |  | No | The current balance on the ledger in minor units of currency. |
| `creditTransferPermissionsData` | `CreditTransferPermissionsDataType` |  | No | Permissions data for credit transfers involving the given ledger. |
| `currentDirectDebitInstructionInvalidatedWithVendor` | `Boolean` |  | No | True if the current direct debit instruction has been invalidated by vendor. False otherwise. |
| `debtLedger` | `LedgerType` |  | No | The debt ledger assigned to this ledger. |
| `id` | `ID` |  | Yes (The 'ledgerId' field is deprecated. Please use 'ledgerNumber' instead. This is in the form of 'L-123456789A' - Marked as deprecated on 2024-10-22. - Scheduled for removal on or after 2025-06-25.) |  |
| `invoices` | `InvoiceBillingDocumentConnectionTypeConnection` | `invoiceId: Int, orderBy: _BillingDocumentsOrderBy, excludeExternallyIssued: Boolean = false, before: String, after: String, first: Int, last: Int` | No | An invoice is a bill that contains individual transactions (i.e. charges, credits, payments, and repayments). These may come from any period of time. |
| `ledgerType` | `String` |  | No | The ledger type code. |
| `name` | `String` |  | No | The display name of the ledger. |
| `number` | `String` |  | No | The canonical name of the ledger. |
| `paymentAdequacy` | `PaymentAdequacyDetailsType` |  | No |  |
| `paymentPreferenceAtTime` | `PaymentPreferenceUnion` | `atTime: DateTime!` | No | The customer's preferred payment method at a point in time. The possible errors that can be raised are: - KT-CT-3976: The ledger has no configured payment preference. - KT-CT-3977: Ledger was not accepting payments at this time. - KT-CT-1113: Disabled GraphQL field requested. |
| `paymentPreferences` | `PaymentPreferenceConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The customer's preferred payment methods. |
| `paymentsWithNonConcludedRePresentation` | `PaymentWithNonConcludedRePresentationConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Payments with non-concluded re-presentation. |
| `refundRequests` | `RefundRequestConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Refund requests for a given ledger. |
| `repaymentRequests` | `RepaymentRequestConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Repayment requests for a given ledger. |
| `statements` | `StatementBillingDocumentConnectionTypeConnection` | `statementId: Int, orderBy: _BillingDocumentsOrderBy, before: String, after: String, first: Int, last: Int` | No | A statement is a billing document that contains all entries on a ledger during a period of time. A customer can understand how their ledger's balance has changed by looking at each statement in series. |
| `supportsInvoices` | `Boolean` |  | No | Is it possible for this ledger to contain invoices. |
| `supportsStatements` | `Boolean` |  | No | Is it possible for this ledger to contain statements. |
| `transactions` | `TransactionConnectionTypeConnection` | `transactionTypes: [TransactionTypeFilter] = [], fromDate: Date, toDate: Date, orderBy: TransactionsOrderBy = POSTED_DATE_DESC, before: String, after: String, first: Int, last: Int` | No | Transactions on the given ledger. |
| `usablePaymentInstructions` | `PaymentInstructionConnectionTypeConnection` | `usableAt: DateTime, before: String, after: String, first: Int, last: Int` | No | The usable payment instructions for this ledger. |

## `LedgerWithPaymentsInstructions`

Ledgers provide the foundation of Kraken’s bookkeeping functionality. Similar to a bank account, they allow us to keep track of financial activity on a particular Kraken account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptsPayments` | `Boolean` |  | No | Whether payments can be posted onto this ledger. |
| `activePaymentInstruction` | `PaymentInstructionType` |  | No | Currently active payment instruction for ledger. |
| `affectsAccountBalance` | `Boolean` |  | No | Whether this ledger's balance contributes to the account's balance. |
| `agreements` | `AgreementConnection` | `before: String, after: String, first: Int, last: Int` | No | The charged supply agreements of the ledger. |
| `amountOwedByCustomer` | `Int` |  | No | The amount owed from the customer perspective. A positive value implies the customer owes the business, while a negative amount implies the customer is in credit. |
| `balance` | `Int` |  | No | The current balance on the ledger in minor units of currency. |
| `creditTransferPermissionsData` | `CreditTransferPermissionsDataType` |  | No | Permissions data for credit transfers involving the given ledger. |
| `debtLedger` | `LedgerInterface` |  | No | The debt ledger assigned to this ledger. |
| `id` | `ID` |  | Yes (The 'ledgerId' field is deprecated. Please use 'ledgerNumber' instead. This is in the form of 'L-123456789A' - Marked as deprecated on 2024-10-22. - Scheduled for removal on or after 2025-06-25.) |  |
| `invoices` | `InvoiceBillingDocumentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | An invoice is a bill that contains individual transactions (i.e. charges, credits, payments, and repayments). These may come from any period of time. |
| `ledgerType` | `String` |  | No |  |
| `mustHaveActivePaymentInstruction` | `Boolean` |  | No | Whether the user has to create a payment instruction. |
| `name` | `String` |  | No | The display name of the ledger. |
| `number` | `String` |  | No | The canonical name of the ledger. |
| `paymentAdequacy` | `PaymentAdequacyDetailsType` |  | No |  |
| `paymentInstructions` | `[PaymentInstructionType]` |  | No | Payment instructions for ledger. |
| `paymentPreferenceAtTime` | `PaymentPreferenceUnion` | `atTime: DateTime!` | No | The customer's preferred payment method at a point in time. The possible errors that can be raised are: - KT-CT-3976: The ledger has no configured payment preference. - KT-CT-3977: Ledger was not accepting payments at this time. - KT-CT-1113: Disabled GraphQL field requested. |
| `paymentPreferences` | `PaymentPreferenceConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The customer's preferred payment methods. |
| `refundRequests` | `RefundRequestConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Refund requests for a given ledger. |
| `repaymentRequests` | `RepaymentRequestConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Repayment requests for a given ledger. |
| `solarWalletCreditLeft` | `Int` |  | No | The remaining solar wallet credit left in the ledger, only for electricity. |
| `statements` | `StatementBillingDocumentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A statement is a billing document that contains all entries on a ledger during a period of time. A customer can understand how their ledger's balance has changed by looking at each statement in series. |
| `statementsWithDetails` | `StatementDetailsBillingDocumentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A statement is a billing document that contains all entries on a ledger during a period of time. A customer can understand how their ledger's balance has changed by looking at each statement in series. |
| `transactions` | `TransactionConnectionTypeConnection` | `transactionTypes: [TransactionTypeFilter] = [], fromDate: Date, toDate: Date, orderBy: TransactionsOrderBy = POSTED_DATE_DESC, before: String, after: String, first: Int, last: Int` | No | Transactions on the given ledger. |
| `usablePaymentInstructions` | `PaymentInstructionConnectionTypeConnection` | `usableAt: DateTime, before: String, after: String, first: Int, last: Int` | No | The usable payment instructions for this ledger. |

## `LegacyItemProfileType`

Represents the characteristics and configuration of an ordered item.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `characteristics` | `JSONString` |  | No | The characteristic values for this item profile. |

## `LegacyOrderDetailsType`

Represents the details of an `Order`.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `order` | `LegacyOrderType` |  | No | The order details. The possible errors that can be raised are: - KT-CT-13101: Order not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `resources` | `[LegacyOrderResource]` |  | No | The resources associated with the order. The possible errors that can be raised are: - KT-CT-13101: Order not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `status` | `OrderStatus` |  | No | The current status of the order. The possible errors that can be raised are: - KT-CT-13101: Order not found. - KT-CT-1113: Disabled GraphQL field requested. |

## `LegacyOrderItemType`

Represents an item being ordered.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `NonEmptyString` |  | No | The code identifying the item. |
| `marketData` | `JSONString` |  | No | Market-specific data for the item. |
| `profile` | `LegacyItemProfileType` |  | No | The profile containing characteristics of the item. |

## `LegacyOrderLineDateRangeType`

Represents a period defined by specific start and end dates.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `end` | `DateTime` |  | No | The end date and time of the period. Null indicates an infinite/rolling period. |
| `start` | `DateTime!` |  | No | The start date and time of the period. |

## `LegacyOrderLineDurationType`

Represents a period defined by duration in seconds.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `duration` | `Float!` |  | No | The duration in seconds. |

## `LegacyOrderLineType`

Represents a line item in an order.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `item` | `LegacyOrderItemType` |  | No | The item being ordered. |
| `period` | `LegacyOrderLinePeriodType` |  | No | The period for which this order line is valid. Can be a range or a duration. |
| `target` | `Account` |  | No | The target customer for this order line. |
| `terms` | `[TermInterface]` |  | No | The terms applicable to this order line. |

## `LegacyOrderResource`

Represents a resource associated with an order.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `resourceIdentifier` | `NonEmptyString` |  | No | The unique identifier of the resource. |
| `resourceType` | `NonEmptyString` |  | No | The type of the resource. |

## `LegacyOrderType`

Represents an order in the system.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `customer` | `LegacyOrderCustomerType` |  | No | The customer who placed the order. |
| `identifier` | `NonEmptyString` |  | No | Unique identifier for the order. |
| `lines` | `[LegacyOrderLineType]` |  | No | The order lines in this order. |
| `orderedAt` | `DateTime` |  | No | The date and time when the order was placed. |
| `sale` | `SalesRecordType` |  | No | The sales record associated with this order, if any. |
| `source` | `String` |  | No | The source offering that generated this order. |
| `terms` | `[TermInterface]` |  | No | The terms applicable to this order. |

## `LegacyProcessOrderOutput`

Output type for the result of processing an order.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `identifier` | `NonEmptyString` |  | No | The unique identifier of the processed order. |
| `resources` | `[LegacyOrderResource!]` |  | No | The resources associated with the processed order. |
| `status` | `OrderStatus` |  | No | The status of the order processing. |

## `LifecycleProcessesType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `joinSupplierProcesses` | `JoinSupplierProcessConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of JoinSupplierProcess for an account. |
| `leavePropertyProcesses` | `LeavePropertyProcessConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of LeavePropertyProcess for an account. |
| `leaveSupplierProcesses` | `LeaveSupplierProcessConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of LeaveSupplierProcess for an account. |
| `occupyPropertyProcesses` | `OccupyPropertyProcessConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of OccupyPropertyProcess for an account. |

## `LifecycleType`

Represents the lifecycle of an offering.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `activatedAt` | `DateTime` |  | No | DateTime when the offering was activated. |
| `code` | `String!` |  | No | Unique lifecycle code. |
| `maxVersion` | `Int!` |  | No | Maximum version number reached. |
| `previousOffering` | `ID` |  | No | Identifier of the previous version of this offering. |
| `status` | `CatalogComponentStatus!` |  | No | Current status of the offering. |
| `version` | `Int!` |  | No | Current version of the offering. |

## `LineCommonError`

A base error type. Should be used for general application or lower level errors.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `field` | `String` |  | No | The field that for which this error should be associated. |
| `message` | `String!` |  | No | The error message to display to the user. |

## `LineEmoji`

A LINE specific emoji object. refs: https://developers.line.biz/en/reference/messaging-api/#text-message

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `emojiId` | `String!` |  | No | The emoji id. |
| `index` | `Int!` |  | No | The location of the emoji in the message. |
| `length` | `Int` |  | No | The length of the emoji string placeholder. |
| `productId` | `String!` |  | No | The product id. |

## `LineImageMessage`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No |  |

## `LineLinkRedirectResponse`

Link Successful. Complete link process with LINE.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `redirectUrl` | `String!` |  | No |  |

## `LineStickerMessage`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `keywords` | `[String!]!` |  | No | Keywords describing the sticker. |
| `packageId` | `String!` |  | No | Sticker package id. |
| `resourceType` | `String!` |  | No | Sticker resource type. |
| `stickerId` | `String!` |  | No | Sticker id. |
| `text` | `String!` |  | No | Text used to customize some stickers. |

## `LineTextMessage`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `displayContent` | `String!` |  | No | The display content. |
| `emojis` | `[LineEmoji!]` |  | No | The emojis in the message. |

## `LineUnlinkedResponse`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String!` |  | No |  |

## `LinkAccountToBusiness`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11104: Business role already allocated. - KT-CT-11105: Business role already allocated. - KT-CT-11106: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `business` | `BusinessType` |  | No | The business the account was linked to. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `LinkActionType`

An action which navigates to any URL.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | Unique identifier of the object. |
| `typeName` | `String` |  | No | The name of the action object's type. |
| `typename` | `String` |  | No | The name of the object's type. |
| `url` | `String!` |  | No | The URL to navigate to. |

## `LinkTokenNotFound`

Returned when no LineAccountLink record matching the parameters exists.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `type` | `LineLinkErrorType!` |  | No | The type of error that occurred. |

## `LivePaymentAdequacyCalculation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `averageMonthlyCharge` | `Int` |  | No | The combined average montly cost for all markets based on usage. |
| `balanceAdjustment` | `Int` |  | No | Suggested temporary adjustment to ongoing usage amount to cover debt or overpayment. |
| `consumption` | `ConsumptionBreakdownConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Breakdown of customer's estimated or real usage per market and per month. |
| `currentBalance` | `Int` |  | No | The balance the ledger has at the time of review. |
| `existingMonthlyAmount` | `Int` |  | No | The amount the customer is paying monthly at the time of the review. |
| `reviewedOn` | `Date` |  | No | The date that we used to calculate the review of the ledger. |
| `suggestedNewMonthlyAmount` | `Int` |  | No | The suggested monthly payment amount in minor currency following the payment adequacy review. |
| `targetBalance` | `Int` |  | No | The balance we expect the ledger to have at the end period of the review. |

## `LoyaltyCardType`

A loyalty card.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No |  |
| `number` | `String` |  | No | The number of the loyalty card. |
| `scheme` | `String` |  | No | The scheme of the loyalty card. |
| `status` | `String` |  | No | The status of the loyalty card. |

## `LoyaltyPointLedgerEntryType`

A Loyalty Point ledger entry.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | The account number associated with the entry. |
| `balanceBroughtForward` | `String` |  | No | Equal to the `balance_carried_forward` from the previous ledger entry or zero if this is the first one. |
| `balanceCarriedForward` | `String` |  | No | Equal to the `balance_brought_forward` plus or minus the value depending on the ledger_type. |
| `id` | `ID!` |  | No |  |
| `idempotencyKey` | `UUID` |  | No | A unique idempotency key for the operation. |
| `ledgerType` | `String` |  | No | The `LedgerEntryType`. Either CHARGE or CREDIT. |
| `postedAt` | `DateTime` |  | No | The date the points were added to the ledger. |
| `reasonCode` | `String` |  | No | The reason the entry was being added. |
| `value` | `String` |  | No | The value of the charge or credit. |

## `LoyaltyPointsProgramEligibilityType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isEligible` | `Boolean` |  | No | Whether the account is eligible to join the loyalty points program. |
| `primaryIneligibilityReason` | `String` |  | No | The primary reason for ineligibility, if any. |

## `MarkPrintBatchAsProcessed`

Mark a closed print batch as Processed The possible errors that can be raised are: - KT-CT-9011: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `printBatch` | `PrintBatchType` |  | No |  |

## `MarketSupplyQuoteRequestType`

A quote request.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptedAt` | `DateTime` |  | No |  |
| `code` | `String` |  | No | The code of the created quote. |
| `quotedSupplyPoints` | `MarketSupplyQuotedSupplyPointConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of quoted supply points. |
| `requestedAt` | `DateTime` |  | No |  |
| `termsAndConditions` | `TermsAndConditionsConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of terms and conditions applicable to the quote. |

## `MarketSupplyQuotedProductConnectionTypeConnection`

Pagination for quoted products.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[MarketSupplyQuotedProductConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `MarketSupplyQuotedProductConnectionTypeEdge`

A Relay edge containing a `MarketSupplyQuotedProductConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `MarketSupplyQuotedProductType` |  | No | The item at the end of the edge |

## `MarketSupplyQuotedProductType`

A product quoted for a supply point.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientParams` | `JSONString` |  | No | A JSON object containing client parameters on the quoted product. |
| `id` | `ID!` |  | No |  |
| `product` | `SupplyProductType` |  | No | The product associated with the quoted product. |
| `wasSelected` | `Boolean!` |  | No |  |

## `MarketSupplyQuotedSupplyPointConnectionTypeConnection`

Pagination for quoted supply points.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[MarketSupplyQuotedSupplyPointConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `MarketSupplyQuotedSupplyPointConnectionTypeEdge`

A Relay edge containing a `MarketSupplyQuotedSupplyPointConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `MarketSupplyQuotedSupplyPointType` |  | No | The item at the end of the edge |

## `MarketSupplyQuotedSupplyPointType`

A supply point quoted as part of a quote request.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientParams` | `JSONString` |  | No | A JSON object containing client parameters on the quoted product. |
| `id` | `ID` |  | No | The ID of the quoted supply point. |
| `identifier` | `String` |  | No | The identifier of the quoted supply point, if one exists. |
| `marketName` | `String` |  | No | The market this supply point belongs to. |
| `quotedProducts` | `MarketSupplyQuotedProductConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Details of all products quoted for this supply point. |
| `supplyPoint` | `SupplyPointType` |  | No | The supply point being quoted. |

## `MasqueradeAuthentication`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `errors` | `[ErrorType]` |  | No | A list of any errors that occurred while running this mutation. |
| `token` | `String` |  | No | A Kraken Token that can be used to authenticate to the API, masquerading as the desired user. |

## `MaximumRefundType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int` |  | No | The maximum amount available to be requested as a refund. |
| `reasonToRecommendAmount` | `MaximumRefundReasonChoices` |  | No | The reason why a specific amount is the maximum available to be requested as a refund. |
| `recommendedBalance` | `Int` |  | No | The recommended minimum balance an account should have when asking for a refund. |

## `MeasurementConnection`

Pagination for measurements.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[MeasurementEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `MeasurementEdge`

A Relay edge containing a `Measurement` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `MeasurementInterface` |  | No | The item at the end of the edge |

## `MeasurementType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `metaData` | `MeasurementsMetadataOutput` |  | No | This type will return more granular data about the measurement. |
| `readAt` | `DateTime!` |  | No | The datetime the measurement was taken. |
| `source` | `String!` |  | No | The data source of the measurement. |
| `unit` | `String!` |  | No | The unit of the measurement. |
| `value` | `Decimal!` |  | No | The value of the measurement. |

## `MeasurementsMetadataOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `extras` | `[ExtrasOutput]` |  | No | Extras relating to the parent measurement node. |
| `statistics` | `[StatisticOutput]` |  | No | Statistics relating to the parent measurement node. |
| `utilityFilters` | `UtilityFiltersOutput` |  | No | The source information relating to the parent measurement node. |

## `Message`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `channel` | `Channel!` |  | No | The channel that the message was sent through. |
| `dispatchedAt` | `DateTime` |  | No | The date/time that Kraken dispatched the message to the vendor. |
| `failedAt` | `DateTime` |  | No | The date/time that the message was confirmed as having failed to send. |

## `MessageConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[MessageEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `MessageEdge`

A Relay edge containing a `Message` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `Message` |  | No | The item at the end of the edge |

## `Metadata`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `key` | `String!` |  | No | The key for the metadata. |
| `value` | `JSONString` |  | No | The metadata value. |

## `MeterReadingEstimationReadingConnection`

Paginator for estimations of meter readings.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[MeterReadingEstimationReadingEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `MeterReadingEstimationReadingEdge`

A Relay edge containing a `MeterReadingEstimationReading` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `MeterReadingEstimationReadingType` |  | No | The item at the end of the edge |

## `MeterReadingEstimationReadingType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `estimatedByAlgorithm` | `String` |  | No | The algorithm used for the estimation. |
| `intervalEnd` | `DateTime!` |  | No | The end date of the reading interval. |
| `intervalStart` | `DateTime!` |  | No | The start date of the reading interval. |
| `isNewlyEstimated` | `Boolean!` |  | No | Denotes if the reading was estimated. |
| `value` | `Decimal!` |  | No | The value of the reading. |

## `MfaDevice`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceType` | `String` |  | No | The type of MFA device. |
| `isConfirmed` | `Boolean` |  | No | Whether the MFA device is confirmed or not. |

## `MinimumContractLengthType`

Represents the minimum term of a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `length` | `Int` |  | No | The minimum length of the contract. |
| `type` | `NonEmptyString` |  | No | The type of the term. |
| `unitOfTime` | `String` |  | No | The unit of time for the contract length. |

## `ModelYearRange`

Range of model years supported for a device model. If end year is null, all years after start year are supported.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `endYear` | `Int` |  | No | Latest year model is supported. If null, all years after start year are supported. |
| `startYear` | `Int!` |  | No | Earliest year model is supported. |

## `Money`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Decimal!` |  | No | The unit being in the smallest denomination of the currency (e.g. pence for GBP). |
| `currency` | `String!` |  | No | The ISO-4217 code for the currency. |

## `MoveToBucket`

The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `conversation` | `InkConversation!` |  | No | The conversation that was moved to the bucket. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `Mutation`

Mutations are the GraphQL equivalent of POST requests in REST. By convention, they are used when data is mutated on the server. To learn about how to form Mutations in graphql, see [GraphQL's documentation](https://graphql.org/learn/queries/#mutations). ⬅️ This interface will autocomplete, so just try typing what you want. You can also search these docs. Some mutations will require authentication. Check the documentation or search `Authentication` for details.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptGoodsQuote` | `AcceptGoodsQuote` | `input: AcceptGoodsQuoteInput!` | No | Accept a goods quote. The possible errors that can be raised are: - KT-CT-8223: Unauthorized. - KT-CT-8201: Received an invalid quoteId. - KT-CT-8224: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `acceptOfferForQuoting` | `AcceptOfferForQuoting` | `input: AcceptOfferForQuotingInput!` | No | Accept a quoting offer in an offer group. The possible errors that can be raised are: - KT-CT-12402: Unable to accept offer. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `actualizeContract` | `ActualizeContractOutput!` | `input: ActualizeContractInput!` | No | Actualize a contract for an account or business. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10007: Unable to terminate contract. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10022: Contract already terminated. - KT-CT-10023: Contract is already revoked. - KT-CT-10024: Contract already expired. - KT-CT-10026: Contract actualization implies breach. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addBusinessToSegment` | `AddBusinessToSegmentMutation` | `input: AddBusinessToSegmentInput!` | No | Add a business to a segment. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-11111: Segment does not exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addCampaignToAccount` | `AddCampaignToAccount` | `input: AddCampaignToAccountInput!` | No | The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-7427: No campaign found with given slug. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addChildToProperty` | `AddChildToProperty` | `input: AddChildToPropertyInput!` | No | Add a child property to a parent property in a hierarchy. If the child is already in the hierarchy with a different parent, it will be reparented. If the child is already a child of the specified parent, this operation is idempotent and does nothing. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-6622: Unauthorized. - KT-CT-6634: Unable to add child to property. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addItemsToRiskList` | `AddItemsToRiskList` | `input: [RiskListItemInputType]!` | No | Add items to the risk list. The possible errors that can be raised are: - KT-CT-12105: Risk list item addition failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addNoteToInkConversation` | `AddNoteToInkConversation` | `input: AddNoteToInkConversationInput` | No | The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addParentToProperty` | `AddParentToProperty` | `input: AddParentToPropertyInput!` | No | Add a parent property to a child property in a hierarchy. If the child is already in the hierarchy with a different parent, it will be reparented. If the child is already a child of the specified parent, this operation is idempotent and does nothing. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-6622: Unauthorized. - KT-CT-6635: Unable to add parent to property. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addPortfolioReference` | `AddPortfolioReference` | `input: AddPortfolioReferenceInput` | No | Mutation to add a reference to an existing portfolio. The possible errors that can be raised are: - KT-CT-9403: Received an invalid portfolioId. - KT-CT-9410: Conflicting portfolio reference. - KT-CT-9408: Invalid portfolio number format. - KT-CT-9409: Invalid portfolio reference. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addProperty` | `AddProperty` | `input: AddPropertyInput!` | No | Add a property to an account. The possible errors that can be raised are: - KT-CT-6623: Unauthorized. - KT-CT-6629: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addPropertyToHierarchy` | `AddPropertyToHierarchy` | `input: AddPropertyToHierarchyInput!` | No | Add a property to a hierarchy as a root node. If the property is already a root node in the hierarchy, this operation is idempotent. If the property is already in the hierarchy as a child, an error will be raised. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-6633: Property is already in the hierarchy as a child. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addSignupReferralOnAccount` | `AddSignupReferralOnAccount` | `input: AddSignupReferralOnAccountInput!` | No | Add a one-way signup reward to a referral. The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6729: This scheme cannot be applied to given account. - KT-CT-6710: Unable to create referral. - KT-CT-6728: This referral scheme's usage is at capacity. - KT-CT-6712: Invalid reference. - KT-CT-6713: Referring and referred account brands do not match. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addStorylineToInkConversation` | `AddStorylineToInkConversation` | `input: AddStorylineToInkConversationInput` | No | The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-7651: Only one storyline entry can be marked as the root cause. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `addUserToPortfolio` | `AddUserToPortfolio` | `input: AddUserToPortfolioInput!` | No | Add an user to a portfolio with a specified role. The possible errors that can be raised are: - KT-CT-5461: Invalid role code. - KT-CT-5462: Invalid user number format. - KT-CT-5463: Unauthorized. - KT-CT-9407: Unauthorized. - KT-CT-9408: Invalid portfolio number format. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `allowRepaymentSubmission` | `AllowRepaymentSubmission` | `input: RepaymentInput!` | No | Allow a repayment to be submitted. The possible errors that can be raised are: - KT-CT-3944: Account repayment does not exist. - KT-CT-3945: Unable to allow a repayment to be submitted. - KT-CT-3950: The provided reason text is too long. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `amendPayment` | `AmendPayment` | `input: AmendPaymentInput!` | No | Amend an existing payment. The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-3970: The account cannot amend payments. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `approveRepayment` | `ApproveRepayment` | `input: ApproveRepaymentInput!` | No | Approve a repayment. The possible errors that can be raised are: - KT-CT-3934: Repayment request already approved. - KT-CT-3935: Repayment request cannot be paid. - KT-CT-3959: Unauthorized. - KT-CT-3973: Repayment request is not in a state to be approved. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `assessCollectionProcessRecordForPause` | `AssessCollectionProcessRecordForPause` | `input: AssessCollectionProcessRecordForPauseInputType!` | No | Assess a collection process record for pause. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `assignInkBucket` | `AssignInkBucket` | `input: AssignInkBucketInput` | No | The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-7613: The Ink bucket was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `assignSupplyPointToEstimationGroup` | `AssignSupplyPointToEstimationGroup` | `input: AssignSupplyPointToEstimationGroupInput!` | No | The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-13601: Estimation Group does not exist. - KT-CT-13602: Supply Point already has an Estimation Group. - KT-CT-13603: Supply Point does not exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `associateCallWithAccount` | `AssociateCallWithAccount` | `input: AssociateCallWithAccountInput!` | No | The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-4178: No account found with given account number. - KT-CT-11808: Unable to associate account to call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `associateItemToCollectionProcess` | `AssociateItemToCollectionProcess` | `input: AssociateItemToCollectionProcessInputType!` | No | Associate item to a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11205: Item already associated to collection process. - KT-CT-11216: Invalid extra_details for associated item type. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `awardLoyaltyPoints` | `AwardLoyaltyPoints` | `input: AwardLoyaltyPointsInput!` | No | Award the passed number of Loyalty Points to the account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9202: Loyalty Points adapter not configured. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-9212: Points exceed maximum limit. - KT-CT-9219: Loyalty points user not found. - KT-CT-9221: Idempotency key already used on ledger entry. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `backendScreenEvent` | `BackendScreenEvent` | `input: BackendScreenEventInput!` | No | Look up an event to perform from its event_id, and return the next action to perform. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-8002: No event found. - KT-CT-8003: Event has no execute function. - KT-CT-8004: Error executing event in the backend. - KT-CT-8007: Incorrect or missing parameters for backend screen event. - KT-GB-9310: Account ineligible for joining Octoplus. - KT-CT-1113: Disabled GraphQL field requested. |
| `blockRepaymentSubmission` | `BlockRepaymentSubmission` | `input: RepaymentInput!` | No | Block a repayment from being submitted. The possible errors that can be raised are: - KT-CT-3944: Account repayment does not exist. - KT-CT-3946: Unable to block a repayment from being submitted. - KT-CT-3950: The provided reason text is too long. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `cancelEnrollment` | `EnrollmentCancelled!` | `input: CancelEnrollmentInput!` | No | Cancel an enrollment for an account and a set of supply points. The possible errors that can be raised are: - KT-CT-10312: Mutation not enabled in this environment. - KT-CT-10318: Enrollment process not found. - KT-CT-10319: Enrollment process failed to cancel. - KT-CT-10320: Enrollment process not cancellable. - KT-CT-10321: Enrollment cancellation workflow not defined. - KT-CT-10323: Enrollment process failed to cancel. - KT-CT-10338: Enrollment process cannot be cancelled. - KT-CT-10331: Missing required process number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `cancelLeaveSupplier` | `LeaveSupplierCancelled!` | `input: CancelLeaveSupplierInput!` | No | Cancel a leave supplier process. The possible errors that can be raised are: - KT-CT-10304: Mutation not enabled in this environment. - KT-CT-10302: Invalid data. - KT-CT-10305: Failed to cancel leave supplier process - market actions are no longer cancellable. - KT-CT-10306: Failed to cancel leave supplier process - the cancellation workflow has not been configured. - KT-CT-10307: Failed to cancel leave supplier process - failed to cancel market actions. - KT-CT-10308: Failed to cancel leave supplier process. - KT-CT-10311: Failed to cancel leave supplier process. The process status is not in cancellable status. - KT-CT-1607: Value cannot be empty. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `cancelOnSiteJobsAppointment` | `CancelOnSiteJobsAppointment` | `input: CancelOnSiteJobsAppointmentInputType!` | No | Cancel an Appointment. The possible errors that can be raised are: - KT-CT-13001: Appointment does not exist. - KT-CT-13019: Vendor not found. - KT-CT-13017: Appointment cancellation not supported. - KT-CT-13053: Failed to cancel the appointment with the agent. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13043: Cannot update appointment as it has terminal status. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `cancelPayment` | `CancelPayment` | `input: CancelPaymentInput!` | No | Cancel an in-flight payment. The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-3954: Payment cancellation failed. - KT-CT-3955: Payment cannot be cancelled. - KT-CT-3956: Temporary error occurred. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `cancelRepaymentRequest` | `CancelRepaymentRequest` | `input: CancelRepaymentRequestInputType!` | No | Cancel a repayment or refund request. The possible errors that can be raised are: - KT-CT-4231: Unauthorized. - KT-CT-3930: The repayment or refund request does not exist. - KT-CT-3931: This repayment or refund request cannot be cancelled. - KT-CT-1113: Disabled GraphQL field requested. |
| `cancelSmartFlexOnboarding` | `CancelSmartFlexOnboarding` | `input: CancelSmartFlexOnboardingInput!` | No | Cancel onboarding of a device with SmartFlex. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `checkCreditRisk` | `CheckCreditRisk` | `input: CheckCreditRiskInput!` | No | Check the credit risk for an account. The possible errors that can be raised are: - KT-CT-3921: Account not found. - KT-CT-5518: Account user not found. - KT-CT-5523: Invalid account or account user. - KT-ES-10701: Default property not found. - KT-ES-10702: Credit check only available for domestic accounts. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `closeDcaProceeding` | `CloseDCAProceeding` | `input: CloseDCAProceedingInputType!` | No | Close the DCA proceeding for an account. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11602: Could not find DCA with that name. - KT-CT-11603: Could not stop debt collection proceeding. - KT-CT-11604: Active debt collection proceeding does not exist for account. - KT-CT-11605: Multiple active Proceeding's found for same agency and campaign on account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `closeInkConversation` | `CloseInkConversation` | `input: CloseInkConversationInput` | No | The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `closeInkLiveChat` | `CloseInkLiveChatConversation` | `input: CloseInkLiveChaConversationtInput` | No | The possible errors that can be raised are: - KT-CT-7616: Not yet implemented. - KT-CT-7643: The Live Chat was not found. - KT-CT-7644: Ink Live Chat conversation not found. - KT-CT-7652: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `closeOpenPrintBatch` | `CloseOpenPrintBatch!` |  | No | Close the Open Print Batch if any. The possible errors that can be raised are: - KT-CT-9010: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `collectDeposit` | `CollectDeposit` | `input: CollectDepositInput!` | No | Collect deposit for the given account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-5711: No collection is required. - KT-CT-5712: Deposit agreement does not exist or has not been accepted. - KT-CT-5713: Payment instruction is not usable. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `collectPayment` | `CollectPayment` | `input: CollectPaymentInput!` | No | Attempt to collect a one-off payment. If an instruction type is provided and there is an existing payment instruction, the payment can be collected immediately. A request to collect a payment at a future date can also be made, in which case the instruction input type is not necessary, but an instruction must exist at the specified collection date for the payment to be collected successfully. The possible errors that can be raised are: - KT-CT-3932: Invalid data. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `commenceDcaProceeding` | `CommenceDCAProceeding` | `input: CommenceDCAProceedingInputType!` | No | Add commencement to an account. The possible errors that can be raised are: - KT-CT-11606: Debt Collection Agency cannot use campaign. - KT-CT-11601: Cannot start collection proceeding, proceeding for this account already exists. - KT-CT-11602: Could not find DCA with that name. - KT-CT-11607: Invalid ledger number for debt collection proceeding. - KT-CT-11608: Ledger does not belong to account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `completeAuthFlowForSmartFlexOnboarding` | `CompleteAuthFlowForSmartFlexOnboarding` | `input: CompleteAuthFlowInput!` | No | Complete the authentication flow to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `completeStandalonePayment` | `CompleteStandalonePayment` | `input: CompleteStandalonePaymentInput!` | No | Complete a standalone payment. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3823: Unauthorized. - KT-CT-3974: Unauthorized. - KT-CT-3975: Unable to complete standalone payment. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `completeTeslaSetupVirtualKeyForSmartFlexOnboarding` | `CompleteTeslaSetupVirtualKeyForSmartFlexOnboarding` | `input: CompleteSmartFlexOnboardingStepInput!` | No | Complete the Tesla virtual key setup onboarding step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `completeUserActionForSmartFlexOnboarding` | `CompleteUserActionRequiredForSmartFlexOnboarding` | `input: CompleteSmartFlexOnboardingStepInput!` | No | Complete the user action required step to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `completeUserInputRequiredForSmartFlexOnboarding` | `CompleteUserInputRequiredForSmartFlexOnboarding` | `input: UserInputRequiredInput!` | No | Complete the user input required step to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `confirmDoubleOptIn` | `ConfirmDoubleOptIn` | `input: ConfirmDoubleOptInInput` | No | Confirm a double opt in The possible errors that can be raised are: - KT-CT-9016: Consent management not enabled. - KT-CT-9020: Invalid consent expiring token. - KT-CT-9021: Consent expiring token not found. - KT-CT-9022: Consent for given token already accepted. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `connectAiAgentToCall` | `ConnectAiAgentToCall` | `input: ConnectAiAgentToCallInput!` | No | The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11815: Unable to connect a call to an AI agent. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAccountCharge` | `CreateAccountCharge` | `input: CreateAccountChargeInput!` | No | Add charge to an account. The possible errors that can be raised are: - KT-CT-5211: The charge reason with the requested code is deprecated. - KT-CT-5212: The charge reason with the requested code does not exist. - KT-CT-5213: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAccountCredit` | `CreateAccountCredit` | `input: CreateAccountCreditInput!` | Yes (The 'createAccountCredit' field is deprecated. Use postCredit mutation as it is ledger aware. - Marked as deprecated on 2022-07-04. - Scheduled for removal on or after 2026-03-30.) | Add credit to an account. The possible errors that can be raised are: - KT-CT-5315: Invalid data. - KT-CT-5314: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAccountFileAttachment` | `CreateAccountFileAttachmentPayload!` | `input: CreateAccountFileAttachmentInput!` | No |  |
| `createAccountNote` | `CreateAccountNote` | `input: CreateAccountNoteInput!` | No | Add a note to an account. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4180: Account note must be a valid string. - KT-CT-4196: Unpin at date provided is in the past. - KT-CT-4195: Unpin at date provided for an unpinned note. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAccountPaymentSchedule` | `CreateAccountPaymentSchedule` | `input: CreateAccountPaymentScheduleInput!` | No | Replace an existing payment schedule with a new one that updates either the payment amount or payment day. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3815: No active payment schedule found for this account. - KT-CT-3822: Unauthorized. - KT-CT-3923: Unauthorized. - KT-CT-3941: Invalid data. - KT-CT-3942: An unexpected error occurred. - KT-CT-3947: An unexpected error occurred. - KT-CT-3960: Invalid value for payment day. - KT-CT-3961: Cannot update plan-associated payment schedule. - KT-CT-3962: No new value provided to update payment schedule. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAccountReference` | `CreateAccountReference` | `input: AccountReferenceInput!` | No | Create an account reference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8311: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAccountReminder` | `CreateAccountReminder` | `input: CreateAccountReminderInput!` | Yes (The 'createAccountReminder' field is deprecated. This mutation rely on legacy reminder types. Please use the createReminder mutation which uses the new registry based reminder types instead. - Marked as deprecated on 2024-11-14. - Scheduled for removal on or after 2025-04-16.) | Create an account reminder. The possible errors that can be raised are: - KT-CT-1401: Invalid data. - KT-CT-1402: Unable to create account reminder. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAffiliateLink` | `CreateAffiliateLink!` | `input: CreateAffiliateLinkInputType!` | No | Create an affiliate link for a new sales agent. The possible errors that can be raised are: - KT-CT-7711: Invalid data. - KT-CT-7713: Invalid data. - KT-CT-7714: Invalid data. - KT-CT-7715: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAffiliateOrganisation` | `CreateAffiliateOrganisation!` | `input: CreateAffiliateOrganisationInputType!` | No | Create an affiliate organisation. The possible errors that can be raised are: - KT-CT-7716: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAffiliateSession` | `CreateAffiliateSession!` | `input: CreateAffiliateSessionInputType!` | No | Create a session for an affiliate link. |
| `createAgreement` | `CreateAgreement` | `input: CreateAgreementInput!` | No | Create a new agreement. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-4910: No product exists with the given input. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1509: Unable to create agreement. - KT-CT-1511: Cannot create overlapping agreement. - KT-CT-1512: Account type does not support agreements. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAgreementRollover` | `CreateAgreementRollover` | `input: CreateAgreementRolloverInput!` | No | Create an agreement rollover for a specific account and agreement. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-4910: No product exists with the given input. - KT-CT-4924: Unauthorized. - KT-CT-13701: An active agreement rollover already exists for this agreement. - KT-CT-13702: Expected send date cannot be in the past. - KT-CT-13703: Rollover date cannot be in the past. - KT-CT-13704: Unable to create agreement rollover. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createApiCall` | `CreateAPICall` | `input: CreateAPICallInput!` | No | Mutation to create a new APICall instance. The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createApiException` | `CreateAPIException` | `input: CreateAPIExceptionInput!` | No | Mutation to create a new APIException instance. The possible errors that can be raised are: - KT-CT-7801: Received an invalid operationsTeamId. - KT-CT-7802: The external identifier already exists. - KT-CT-7805: Too many tags associated with this API Exception. - KT-CT-7806: Cannot create duplicate tags for the same API exception. - KT-CT-7811: Received an invalid assignedUserId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createApiExceptionEvent` | `CreateAPIExceptionEvent` | `input: CreateAPIExceptionEventInput!` | No | Mutation to create a new APIExceptionEvent instance. The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createApiExceptionNote` | `CreateAPIExceptionNote` | `input: CreateAPIExceptionNoteInput!` | No | Mutation to create a new APIExceptionNote instance. The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createAudioRecording` | `CreateAudioRecording!` | `input: AudioRecordingInputType!` | No | Create an audio recording for an affiliate session. The possible errors that can be raised are: - KT-CT-7720: Invalid S3 key format. - KT-CT-7721: Link not found. - KT-CT-7722: Invalid input for audio recording upload. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createBusiness` | `CreateBusiness` | `input: CreateBusinessInput!` | No | Create a business. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11108: Invalid data. - KT-CT-11109: Invalid data. - KT-CT-11110: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createCallMetadata` | `CreateCallMetadata` | `input: CallMetadataInput!` | No | The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11806: Call metadata item key cannot be an empty string. - KT-CT-11807: A call metadata item with this key already exists for this call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createCampaignItems` | `CreateCampaignItems` | `input: CreateCampaignItemsInput!` | No | The possible errors that can be raised are: - KT-CT-11501: Voice campaign not found. - KT-CT-4178: No account found with given account number. - KT-CT-11503: One or more campaign items are invalid and cannot be created. - KT-CT-11504: The batch of campaign items is too large. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createCollectionProcessEvent` | `CreateCollectionProcessEvent` | `input: CreateCollectionProcessEventInputType!` | No | Create an event for a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1605: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createComplaint` | `CreateComplaint` | `complaint: CreateComplaintInputType!` | No | Create a complaint. The possible errors that can be raised are: - KT-CT-10801: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createContract` | `CreateContractOutput!` | `input: CreateContractInput!` | No | Create and actualize a new contract for an account or business. The possible errors that can be raised are: - KT-CT-10001: Party is already under contract. - KT-CT-10006: Account not found. - KT-CT-10021: Business not found. - KT-CT-10018: The provided contract subject is invalid. - KT-CT-10019: Contract creation implies breach. - KT-CT-10020: The provided contract party payload is invalid. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createContributionAgreement` | `CreateContributionAgreement` | `input: CreateContributionAgreementInput!` | No | Create a contribution agreement for an account. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-9601: Invalid data. - KT-CT-9602: Unable to create contribution agreement. - KT-CT-9605: Contribution amount cannot be 0 or negative. - KT-CT-9606: Scheme is not accepting contributions at this time. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createCreditTransferPermission` | `CreateCreditTransferPermission` | `input: CreateCreditTransferPermissionInput!` | No | Create a credit transfer permission. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3827: The ledger is not valid. - KT-CT-3828: At least one of the provided ledgers must be a credit storage ledger. - KT-CT-3829: The credit transfer permission already exists. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createCustomerFeedback` | `CreateCustomerFeedback` | `input: CreateCustomerFeedbackInputType!` | No | Create unsubmitted customer feedback object. The possible errors that can be raised are: - KT-CT-5516: Invalid data. - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createDepositAgreement` | `CreateDepositAgreement` | `input: CreateDepositAgreementInput!` | No | Create a new deposit agreement for the account if it needs one. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createEnergyAccount` | `CreateEnergyAccount` | `input: CreateEnergyAccountInput` | No | Create an account for either electricity or dual fuel. The possible errors that can be raised are: - KT-CT-4910: No product exists with the given input. - KT-CT-4911: Product not available. - KT-ES-4117: Invalid data. - KT-ES-4111: Supply point already exists. - KT-ES-4113: ATR not valid for contracting. - KT-ES-7701: The affiliate client failed to meet the requirements. - KT-ES-4121: Gas tariffs are not available. - KT-ES-4102: Account with multiple properties. - KT-ES-4122: Unable to create a referral. - KT-ES-4123: Nif not found. - KT-ES-4914: The received CUPS is invalid. - KT-ES-7819: The request to Chipiron to get SIPS data failed. - KT-ES-4917: The given supply point is not valid to contract. - KT-CT-7899: An internal error occurred. - KT-CT-1113: Disabled GraphQL field requested. |
| `createExternalAccountEvent` | `CreateExternalAccountEvent` | `input: CreateExternalAccountEventInput!` | No | Create an external account event. The possible errors that can be raised are: - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createExternalAccountUserEvent` | `CreateExternalAccountUserEvent` | `input: CreateExternalAccountUserEventInput!` | No | Create an external account user event. The possible errors that can be raised are: - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createExternalMessage` | `CreateExternalMessage` | `input: CreateExternalMessageInput!` | No | Create an external message to record communications sent by external vendors. This allows you to import messages, such as emails, sent using other tools into Kraken. The possible errors that can be raised are: - KT-CT-14201: Vendor is empty. - KT-CT-14202: Vendor message ID is empty. - KT-CT-14203: Account number is empty. - KT-CT-14204: Message already exists. - KT-CT-14205: Unable to create the external message. - KT-CT-14206: An email body is missing. - KT-CT-14207: To email is empty. - KT-CT-14208: To email is not a valid email address. - KT-CT-14209: From email is empty. - KT-CT-14210: From email is an invalid format. - KT-CT-14211: A reply to email address is empty. - KT-CT-14212: A reply to email address is not a valid email address. - KT-CT-14213: The external messaging API is not enabled. - KT-CT-14214: An account number was provided, but no corresponding account could be found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createFormSubmission` | `FormSubmissionOuput` | `input: FormSubmissionInput!` | No | Create a "form submission" entity. This is only meant to be used as a quick way of putting together a form and submit data for it, in the form of JSON - it is not expected that all form submissions will come through this path. This field requires the `Authorization` header to be set. |
| `createGoodsPurchase` | `CreateGoodsPurchase` | `input: CreatePurchaseInput!` | No | Create a goods purchase. The possible errors that can be raised are: - KT-CT-8206: Invalid data. - KT-CT-1131: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createGoodsQuote` | `CreateGoodsQuote` | `input: CreateGoodsQuoteInput!` | No | Create a goods quote. The possible errors that can be raised are: - KT-CT-8202: Invalid data. - KT-CT-8205: Unable to create quote. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createGoodsQuoteWithoutAccount` | `CreateGoodsQuoteWithoutAccount` | `input: CreateGoodsQuoteWithoutAccountInput!` | No | Create a goods quote without an account. The possible errors that can be raised are: - KT-CT-8202: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createInboundCall` | `CreateInboundCall` | `input: CreateInboundCallInput!` | No | The possible errors that can be raised are: - KT-CT-11805: Invalid input for creating an inbound call. - KT-CT-11810: Caller is blocked. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createInkInboundMessage` | `CreateInkInboundMessage` | `input: CreateInkInboundMessageInput` | No | Register an Ink inbound message. The possible errors that can be raised are: - KT-CT-7622: Attachment bucket is invalid. - KT-CT-7623: Attachment path is invalid. - KT-CT-7621: Attachment not found. - KT-CT-7618: Unable to process message. - KT-CT-7625: Invalid email address. - KT-CT-7630: Message with this message ID has already been processed. - KT-CT-7632: The text content of the Ink Inbound Generic Message is too long. - KT-CT-7620: Channel not supported. - KT-CT-7627: The 'email' object is missing from the payload. - KT-CT-7628: The 'generic' object is missing from the payload. - KT-CT-7629: The 'post' object is missing from the payload. - KT-CT-7653: Account numbers on the message and message type must match if both are supplied. - KT-CT-7654: An account number was provided, but no corresponding account could be found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createInkLiveChatMessage` | `CreateInkLiveChatMessage` | `input: CreateInkLiveChatMessageInput` | No | The possible errors that can be raised are: - KT-CT-7616: Not yet implemented. - KT-CT-1111: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-7642: No account user was found for the given fromHandle. - KT-CT-7641: Live Chat message with this message ID has already been processed. - KT-CT-7645: The user is not authorized to access this Live Chat. - KT-CT-7622: Attachment bucket is invalid. - KT-CT-7623: Attachment path is invalid. - KT-CT-7621: Attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createLead` | `CreateLead` | `input: CreateLeadInput!` | No | Create a lead with the provided details. The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8930: Unable to parse address. - KT-CT-8928: The funnel is not active and cannot be used to create this entity. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8919: Funnel initial stage not set. - KT-CT-9017: Consent type not found. - KT-CT-8932: Lead contact details missing legal contact. - KT-CT-8934: Lead contact details missing communications contact. - KT-CT-8935: National ID bad input. - KT-CT-4121: Invalid phone number. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createMetadata` | `CreateMetadata` | `input: MetadataInput!` | No | Create metadata on an object. The possible errors that can be raised are: - KT-CT-8412: Invalid data. - KT-CT-8414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createMfaDevice` | `CreateMfaDevice` | `input: CreateMfaDeviceInputType!` | No | Create MFA Device for user. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1151: MFA device not found. - KT-CT-1153: Unable to create MFA device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createNewAgreementFromProductSwitchProcess` | `CreateNewAgreementFromProductSwitchProcess` | `input: CreateNewAgreementFromProductSwitchProcessInput!` | No | Create a new agreement from an existing product switch process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4924: Unauthorized. - KT-CT-1509: Unable to create agreement. - KT-CT-1507: Agreement product switch date is not within the acceptable range. - KT-CT-1510: Product switch process not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOfferGroupForQuoting` | `CreateOfferGroupForQuoting` | `input: CreateOfferGroupForQuotingInput!` | No | Create a quoting Offer Group. The possible errors that can be raised are: - KT-CT-12401: Unable to create offer group. - KT-CT-12405: Missing rates for quoting. - KT-CT-12406: Product not configured correctly for quoting. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOnSiteJobsAppointment` | `CreateOnSiteJobsAppointment` | `appointmentBookingSessionId: UUID!, slotId: UUID!` | No | Create an Appointment. The possible errors that can be raised are: - KT-CT-13030: Booking session not found. - KT-CT-13025: Booking session has expired. - KT-CT-13033: Slot not found. - KT-CT-13028: Agent not found. - KT-CT-13019: Vendor not found. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13035: Request is inactive. - KT-CT-13032: Request does not exist. - KT-CT-13036: Booking service currently unavailable. - KT-CT-13037: Appointment reference not provided by booking service. - KT-CT-13031: Timeslot is no longer available. - KT-CT-13027: Booking system error occurred. - KT-CT-13056: Appointment cannot be rescheduled. - KT-CT-13044: Failed to update appointment slot. - KT-CT-13001: Appointment does not exist. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13006: No properties found for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOnSiteJobsAppointmentWithDate` | `CreateOnSiteJobsAppointmentWithDate` | `appointmentBookingDetails: OnSiteJobsAppointmentBookingDetailsInput!, deadlineDate: Date, overrideAppointmentCheckWarnings: Boolean = false, preferredDate: Date!, requestId: UUID!` | No | Create an Appointment using DATE booking mode. Used when the booking flow does not require selecting a specific timeslot. The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13020: Could not identify agent from property. - KT-CT-13021: Invalid job type. - KT-CT-13022: Work category not found for job type. - KT-CT-13057: Date booking mode is not applicable for this request. - KT-CT-13023: Appointment booking checks failed. - KT-CT-13024: Appointment booking checks returned warnings. - KT-CT-13028: Agent not found. - KT-CT-13019: Vendor not found. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13035: Request is inactive. - KT-CT-13036: Booking service currently unavailable. - KT-CT-13037: Appointment reference not provided by booking service. - KT-CT-13027: Booking system error occurred. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-13006: No properties found for the given supply points. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOnSiteJobsAppointmentWithoutBooking` | `CreateOnSiteJobsAppointmentWithoutBooking` | `input: OnSiteJobsCreateAppointmentInput!` | No | Create an Appointment on Kraken without making a booking via the booking vendor system. This is typically used by booking vendors to inform Kraken about appointments created on their system. The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13035: Request is inactive. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13021: Invalid job type. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13039: Cancellation fields require CANCELLED status. - KT-CT-13027: Booking system error occurred. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13062: Datetime field must be timezone-aware. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOnSiteJobsRequest` | `CreateOnSiteJobsRequest` | `input: CreateOnSiteJobsRequestInputType!` | No | Create a Request. The possible errors that can be raised are: - KT-CT-13002: Supply point not found. - KT-CT-13003: Supply points must belong to the same account. - KT-CT-13004: No account found for the given supply points. - KT-CT-13006: No properties found for the given supply points. - KT-CT-13028: Agent not found. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13007: At least one of the request checks failed. - KT-CT-13008: At least one of the request checks has warnings. - KT-CT-13009: On site jobs Request already exists. - KT-CT-13012: Viewer is not allowed to create a request. - KT-CT-13013: Reporter post init error. - KT-CT-13014: Request reason is not supported. - KT-CT-13015: Request sub_reason is not supported. - KT-CT-13041: User is not allowed to override request/appointment checks. - KT-CT-13042: Multiple supply points not supported by this booking adapter. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13047: Multiple supply points found. - KT-CT-13048: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_ids. - KT-CT-13049: Neither supply_point_identifier_to_market_name_mapping nor supply_point_internal_ids provided. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13058: Reason approval details are required when the reason requires approval. - KT-CT-13059: Emergency approval details are required when the emergency requires approval. - KT-CT-13060: Reason approval details should not be provided when the reason does not require approval. - KT-CT-13061: Emergency approval details should not be provided when the emergency does not require approval. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOpportunityAndLead` | `CreateOpportunityAndLead` | `input: CreateOpportunityAndLeadInput!` | No | Create an opportunity and lead with the provided details. The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8919: Funnel initial stage not set. - KT-CT-8930: Unable to parse address. - KT-CT-8907: Lead not found. - KT-CT-8901: Unable to create lead. - KT-CT-8902: Unable to create lead. - KT-CT-8935: National ID bad input. - KT-CT-4121: Invalid phone number. - KT-CT-8931: Extra detail value is invalid. - KT-CT-9017: Consent type not found. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-8936: Only one address is required to create an opportunity. - KT-CT-8937: One or more Supply Points cannot be validated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOpportunityFileAttachment` | `CreateOpportunityFileAttachment` | `input: CreateOpportunityFileAttachmentInput!` | No | Creates an Opportunity File Attachment. |
| `createOpportunityForLead` | `CreateOpportunityForLead` | `input: CreateOpportunityForLeadInput!` | No | Create an opportunity for a lead with the provided details. The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8919: Funnel initial stage not set. - KT-CT-8907: Lead not found. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-8924: Unable to create opportunity. - KT-CT-8925: Unable to create opportunity. - KT-CT-8926: Unable to create opportunity. - KT-CT-8928: The funnel is not active and cannot be used to create this entity. - KT-CT-8930: Unable to parse address. - KT-CT-8936: Only one address is required to create an opportunity. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8937: One or more Supply Points cannot be validated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOrUpdateLoyaltyCard` | `CreateOrUpdateLoyaltyCardMutation` | `input: CreateOrUpdateLoyaltyCardInput!` | No | Create or update a loyalty card for the given account user. The possible errors that can be raised are: - KT-CT-5412: No account user exists with the given id. - KT-CT-8610: Invalid data. - KT-CT-8611: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createOrUpdateTimeSeriesEntries` | `CreateOrUpdateTimeSeriesEntries!` | `input: CreateOrUpdateTimeSeriesEntriesInput!` | No | Create or update time series entries. The possible errors that can be raised are: - KT-CT-12014: Time series not found. - KT-CT-12015: Characteristics mismatch. - KT-CT-12016: Conflicting time series entries. - KT-CT-12017: Invalid time series entries period. - KT-CT-12038: Invalid time series entries granularity. - KT-CT-12040: Time series entries in use. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createPaymentActionIntent` | `CreatePaymentActionIntent` | `input: CreatePaymentActionIntentInput!` | No | Create a new payment action intent. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3980: Invalid ledger identifier. - KT-CT-3981: Unauthorized. - KT-CT-3982: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createPortfolio` | `CreatePortfolio` | `input: CreatePortfolioInput` | No | Mutation to create a new Portfolio instance. The possible errors that can be raised are: - KT-CT-9402: Received an invalid brandCode. - KT-CT-9401: Received an invalid operationsTeamId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createPortfolioUserRole` | `CreatePortfolioUserRole` | `input: CreatePortfolioUserRoleInput` | No | Mutation to create a new portfolio user role. This will effectively link the user to the portfolio giving them all the permissions enabled for the specific role. The possible errors that can be raised are: - KT-CT-9403: Received an invalid portfolioId. - KT-CT-9404: Received an invalid accountUserId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createPostEvents` | `CreatePostEvents` | `input: CreatePostEventsInput!` | No | Create post delivery events from external vendors. The possible errors that can be raised are: - KT-CT-9907: Post events batch size exceeded. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createProduct` | `CreateProductOutput!` | `input: CreateProductInput!` | No | Create a new product. The possible errors that can be raised are: - KT-CT-12003: Specified product brand does not exist. - KT-CT-12004: Invalid product tag type. - KT-CT-12005: A selection of a terms and conditions type does not exist. - KT-CT-12006: Provided product characteristic overrides are not in the correct format. - KT-CT-12007: Unable to create product. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createQuote` | `CreateQuote` | `input: CreateQuoteInput!` | No | Create a quote for the provided CUPS Or Estimation. The possible errors that can be raised are: - KT-CT-4639: Unable to quote for the provided market identifier. - KT-CT-1501: Agreement not found. - KT-CT-4131: Invalid brand. - KT-CT-7719: Session not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createQuoteForAccount` | `CreateQuoteForAccount` | `input: CreateQuoteForAccountInput!` | No | Create a quote for switching product. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. - KT-CT-4616: Unable to create a quote. - KT-CT-4631: Unable to quote for the chosen market. - KT-CT-4645: No supply point found belonging to the account for the provided identifier. - KT-CT-4924: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createQuoteForProducts` | `QuoteRequest` | `input: CreateQuoteForProductsInput!` | No | Create a quote. The possible errors that can be raised are: - KT-CT-4616: Unable to create a quote. - KT-ES-4601: Invalid product codes. - KT-CT-1113: Disabled GraphQL field requested. |
| `createReferral` | `CreateReferral` | `input: CreateReferralInput!` | No | Create an account referral using an email address, personal link or code.This is for customers to refer other customers so it only works with friend referrals and not partner referrals. The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6710: Unable to create referral. - KT-CT-6711: Accounts may not self-refer. - KT-CT-6713: Referring and referred account brands do not match. - KT-CT-6712: Invalid reference. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createReminder` | `CreateReminder` | `input: CreateReminderInput!` | No | Create an account reminder. The possible errors that can be raised are: - KT-CT-1401: Invalid data. - KT-CT-1402: Unable to create account reminder. - KT-CT-1403: Missing user or team assignee. - KT-CT-1404: This reminder type is deprecated. - KT-CT-1405: Both user and team assignee provided. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createScheduledTransactions` | `CreateScheduledTransactions` | `input: [CreateScheduledTransactionsInput]!` | No | Create scheduled transactions. The possible errors that can be raised are: - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3830: Invalid action. - KT-CT-3831: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createShellAccount` | `CreateShellAccountPayload` | `input: CreateShellAccountInput!` | No | Create a shell/payment account. |
| `createSolarWalletRelationship` | `CreateSolarWalletRelationship` | `input: CreateSolarWalletRelationshipType!` | Yes (The 'createSolarWalletRelationship' field is deprecated. Use 'createCreditTransferPermission' mutation instead. - Marked as deprecated on 2025-02-10. - Scheduled for removal on or after 2025-08-10.) | Create solar wallet sharing credit between a solar wallet credit ledger and spain electricity ledger. The possible errors that can be raised are: - KT-ES-7805: The request to create a solar wallet sharing credit between ledgers was incomplete or malformed. - KT-CT-4123: Unauthorized. - KT-ES-4116: Account not found. - KT-ES-7809: There is no ledger of this type on this account.. - KT-ES-7806: Couldn't create sharing credit between ledgers because credit sharing ledger already exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `createTimeSeriesPrices` | `CreateTimeSeriesPrices!` | `input: CreateTimeSeriesPricesInput!` | Yes (The 'createTimeSeriesPrices' field is deprecated. Please use the 'createOrUpdateTimeSeriesEntries' mutation instead. - Marked as deprecated on 2025-02-03. - Scheduled for removal on or after 2025-03-01.) | Create time series prices. The possible errors that can be raised are: - KT-CT-12014: Time series not found. - KT-CT-12015: Characteristics mismatch. - KT-CT-12016: Conflicting time series entries. - KT-CT-12017: Invalid time series entries period. - KT-CT-12038: Invalid time series entries granularity. - KT-CT-12040: Time series entries in use. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `deauthenticateDevice` | `DeauthenticateDevice` | `input: DeAuthenticationInput` | Yes (The 'deauthenticateDevice' field is deprecated. Please use 'deauthenticateFlexDevice' instead. - Marked as deprecated on 2025-05-12. - Scheduled for removal on or after 2026-01-16. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/606/) | De-authenticate a device. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4350: Unable to de-authenticate device. - KT-CT-4352: This device cannot currently be de-authenticated. - KT-CT-1113: Disabled GraphQL field requested. |
| `deauthenticateFlexDevice` | `DeauthenticateFlexDevice` | `input: DeauthenticateFlexDeviceInput` | No | De-authenticate a device by device id. The possible errors that can be raised are: - KT-CT-4350: Unable to de-authenticate device. - KT-CT-4352: This device cannot currently be de-authenticated. - KT-CT-1113: Disabled GraphQL field requested. |
| `deductLoyaltyPoints` | `DeductLoyaltyPoints` | `input: DeductLoyaltyPointsInput!` | No | Deduct the passed number of Loyalty Points from the account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-5420: Unauthorized. - KT-CT-9211: Invalid reason for loyalty points award. - KT-CT-9219: Loyalty points user not found. - KT-CT-9204: Negative or zero points set. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9221: Idempotency key already used on ledger entry. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `deleteAccountReference` | `DeleteAccountReference` | `input: DeleteAccountReferenceInput!` | No | Delete an account reference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8312: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `deleteBoostCharge` | `DeleteBoostCharge` | `input: DeleteBoostChargeInput` | Yes (The 'deleteBoostCharge' field is deprecated. Please use 'updateBoostCharge' instead. - Marked as deprecated on 2025-05-12. - Scheduled for removal on or after 2026-01-26. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/607/) | Stop any active boost charging. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4354: Unable to cancel boost charge. - KT-CT-1113: Disabled GraphQL field requested. |
| `deleteMfaDevice` | `DeleteMfaDevice` | `input: DeleteMfaDeviceInputType!` | No | Delete MFA Device for user. The possible errors that can be raised are: - KT-CT-1150: MFA device not found. - KT-CT-1154: Unable to delete MFA device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `deletePropertyDescendants` | `DeletePropertyDescendants` | `input: DeletePropertyDescendantsInput!` | No | Delete all descendants of a property in a hierarchy. This permanently deletes all descendant nodes (children, grandchildren, etc.) but keeps the property node itself in the hierarchy. This operation is idempotent - if the property is not in the hierarchy or has no descendants, it will succeed without error. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `deletePushNotificationBinding` | `DeletePushNotificationBinding` | `input: DeletePushNotificationBindingInput!` | No | Delete a device token used for push notifications. This field requires the `Authorization` header to be set. The possible errors that can be raised are: - KT-CT-5411: Invalid token or no push notification binding found for the given account user. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `detachSupplyPointFromEstimationGroup` | `DetachSupplyPointFromEstimationGroup` | `input: DetachSupplyPointFromEstimationGroupInput!` | No | The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-13603: Supply Point does not exist. - KT-CT-13604: Supply point has no estimation group assigned. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `deviceRegistration` | `DeviceRegistration` | `input: DeviceRegistrationInput` | Yes (The 'deviceRegistration' field is deprecated. Please use 'startSmartFlexOnboarding' instead. - Marked as deprecated on 2025-09-08. - Scheduled for removal on or after 2026-03-01. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/678/) | Register a device (EV, battery or heat pump) for smart control. The possible errors that can be raised are: - KT-CT-4324: Device already registered error. - KT-CT-4321: Serializer validation error. - KT-CT-4312: Unable to register device. - KT-CT-4363: No capable devices found. - KT-CT-4364: Multiple devices found. - KT-CT-1113: Disabled GraphQL field requested. |
| `endContributionAgreement` | `EndContributionAgreement` | `input: EndContributionAgreementInput!` | No | End a contribution agreement for an account. The possible errors that can be raised are: - KT-CT-9603: Unable to find contribution agreement. - KT-CT-4123: Unauthorized. - KT-CT-9604: Unable to end contribution agreement. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `enqueueInboundCall` | `EnqueueInboundCall` | `input: EnqueueInboundCallInput!` | No | The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11803: Unable to enqueue the call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `enrollAccountInLoyaltyProgram` | `EnrollAccountInLoyaltyProgram` | `input: EnrollAccountInLoyaltyProgramInput!` | No | Enroll users account in Loyalty program. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9213: ineligible loyalty points enrollment. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `enrollment` | `EnrollmentInitiated!` | `input: EnrollmentInput!` | No | Initiate an enrollment for an account and a set of supply points. The possible errors that can be raised are: - KT-CT-1602: Serializer validation error. - KT-CT-4410: Invalid postcode. - KT-CT-4412: The supplied address is not valid. - KT-CT-4501: Unauthorized. - KT-CT-7719: Session not found. - KT-CT-10312: Mutation not enabled in this environment. - KT-CT-10313: Failed to enroll account. - KT-CT-10314: This supply point is already on supply. - KT-CT-10315: Unable to begin enrollment journey due to invalid data. - KT-CT-6622: Unauthorized. - KT-CT-10340: House move enrollment is not enabled. - KT-CT-10302: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `fetchGeneratePaymentFingerprint` | `FetchGeneratePaymentFingerprint` | `input: FetchGeneratePaymentFingerprintInput!` | No | Fetch or generate payment fingerprint from vendor. The possible errors that can be raised are: - KT-CT-12101: Payment instruction not found. - KT-CT-12102: Payment vendor not supported. - KT-CT-12103: Missing payment metadata from vendor. - KT-CT-12104: Unable to fetch or generate payment fingerprint. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `fetchPreSignedLinkForOpportunityAttachment` | `FetchPreSignedLinkForOpportunityAttachment` | `input: FetchPreSignedLinkForOpportunityAttachmentInput!` | No | Fetch a pre-signed link for an opportunity file attachment. The possible errors that can be raised are: - KT-CT-8933: Opportunity file attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `forceReauthentication` | `ForceReauthentication` | `input: ForceReauthenticationInput!` | No | Force users of Kraken Tokens and refresh tokens issued to the viewer to reauthenticate. Calling this mutation will cause all Kraken Tokens and refresh tokens issued to the authenticated viewer before the mutation was called to become invalid. |
| `generateAffiliatesAudioRecordingPreSignedUrl` | `GenerateAffiliatesAudioRecordingPreSignedUrl!` | `input: GenerateAffiliatesAudioRecordingPreSignedUrlInput!` | No | Generate a pre signed url for uploading a file for use with affiliates. |
| `generateInkPresignedUrl` | `GenerateInkPresignedUrl` | `input: GenerateInkPresignedUrlInput` | No | The possible errors that can be raised are: - KT-CT-7620: Channel not supported. - KT-CT-7618: Unable to process message. - KT-CT-7624: Error when generating the presigned URL. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `generateLeadsFileAttachmentDownloadPreSignedUrl` | `GenerateLeadsFileAttachmentDownloadPreSignedUrl` | `input: GenerateLeadsFileAttachmentDownloadPreSignedUrlInput!` | No | Generate a pre-signed URL for downloading a leads attachment file. The possible errors that can be raised are: - KT-CT-8933: Opportunity file attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `generateLeadsFileAttachmentPreSignedUrl` | `GenerateLeadsFileAttachmentsPreSignedUrl` | `input: GenerateLeadsFileAttachmentPreSignedUrlInput!` | No | Generate a pre signed url for uploading a leads attachment file. |
| `generatePreSignedToken` | `GeneratePreSignedToken` | `email: String!, numberOfDaysAllowed: Int!, scope: PreSignedTokenScope!` | No | Generate a pre-signed token with a set expiry time. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1120: The Kraken Token has expired. - KT-CT-1131: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `getEmbeddedSecretForNewPaymentInstruction` | `GetEmbeddedSecretForNewPaymentInstruction` | `input: GetEmbeddedSecretForNewPaymentInstructionInput!` | No | Get the client secret needed to create a new payment instruction using an embedded form. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3820: Received both ledger ID and number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `getEmbeddedSecretForNewPaymentInstructionWithoutAccount` | `GetEmbeddedSecretForNewPaymentInstructionWithoutAccount` | `input: GetEmbeddedSecretForNewPaymentInstructionWithoutAccountInput!` | No | Get the client secret needed to create a new payment instruction using an embedded form without tying it to a customer. |
| `getHostedUrlForNewPaymentInstruction` | `GetHostedUrlForNewPaymentInstruction` | `input: GetHostedUrlForNewPaymentInstructionInput!` | No | Get the external URL where the user can set up a payment instruction. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `getOrCreateAgreement` | `GetOrCreateAgreement` | `input: CreateAgreementInput!` | No | Get an existing agreement or create a new one if it doesn't exist. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-4910: No product exists with the given input. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1509: Unable to create agreement. - KT-CT-1511: Cannot create overlapping agreement. - KT-CT-1512: Account type does not support agreements. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `grantUserAccessToBusiness` | `GrantUserAccessToBusiness` | `input: GrantUserAccessToBusinessInput!` | No | Grant user access to the business using the provided role. The possible errors that can be raised are: - KT-CT-5463: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-13501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `initializeAccount` | `InitializeAccountResult!` | `input: BaseInitializeAccountInput!` | No | Initialize account for sign up. Returns the existing account if matching datafound for the provided input, otherwise creates a new account. The possible errors that can be raised are: - KT-CT-10324: Mutation not enabled in this environment. - KT-CT-10325: Input data has invalid format. - KT-CT-10326: An error occurred when trying to initialize the account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `initializeUser` | `InitializeUserResult!` | `input: BaseInitializeUserInput!` | No | Initialize user for sign up. Returns an existing user if matching datafound for the provided input, otherwise creates a new one. The possible errors that can be raised are: - KT-CT-10327: Mutation not enabled in this environment. - KT-CT-10328: Input data has invalid format. - KT-CT-10329: An error occurred when trying to initialize the user. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `initiateHostedStandalonePayment` | `InitiateHostedStandalonePayment` | `input: InitiateHostedStandalonePaymentInput!` | No | Initiate a standalone payment and return the url where the customer can complete it. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3943: Invalid ledger. - KT-CT-3957: No collection method provided. - KT-CT-3958: Provide either ledger ID or ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `initiateProductSwitch` | `InitiateProductSwitch` | `input: InitiateProductSwitchInput!` | No | Do a product switch for a user. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4619: Quote with given code not found. - KT-CT-4624: Unable to accept the given product code. - KT-CT-4924: Unauthorized. - KT-CT-4626: No product selected for the given quote code. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-1509: Unable to create agreement. - KT-CT-1507: Agreement product switch date is not within the acceptable range. - KT-CT-4640: Unable to get market or client params from quoted product. - KT-CT-4627: No products are available for this quote. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `initiateStandalonePayment` | `InitiateStandalonePayment` | `input: InitiateStandalonePaymentInput!` | No | Initiate a standalone payment and return the client secret required to complete it. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3943: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `instigateContractTermination` | `ContractTerminationInstigated!` | `input: BaseInstigateContractTerminationInput!` | No | Instigate a contract termination journey. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10004: Supply loss process instigation has failed. - KT-CT-10007: Unable to terminate contract. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10013: Requested termination date is invalid. - KT-CT-10014: The provided contract termination input data is invalid. - KT-CT-10015: Supply point termination context is not serializable. - KT-CT-10016: Error building contract termination engine. - KT-CT-10022: Contract already terminated. - KT-CT-10023: Contract is already revoked. - KT-CT-10024: Contract already expired. - KT-CT-10025: Contract has not started yet. - KT-CT-10037: Contract notes feature is disabled. - KT-CT-10038: Contract note reason not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `instigateContractVariation` | `InstigateContractVariationOutput!` | `input: InstigateContractVariationInput!` | Yes (The 'instigateContractVariation' field is deprecated. This is a legacy mutation. The varyContractTerms should be used instead. - Marked as deprecated on 2026-03-05. - Scheduled for removal on or after 2026-04-11.) | Instigate a contract variation journey. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10011: Unable to vary contract terms. - KT-CT-10033: Unable to save term. - KT-CT-10012: Contract variation implies breach. - KT-CT-10034: Unknown contract journey type. - KT-CT-10035: Cannot process a non-active contract journey. - KT-CT-10036: The contract journey manager is not found. - KT-CT-10037: Contract notes feature is disabled. - KT-CT-10038: Contract note reason not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `instigateLeaveSupplier` | `LeaveSupplierInstigated!` | `input: LeaveSupplierInput!` | No | Instigate a leave supplier process or update an existing process. The possible errors that can be raised are: - KT-CT-10304: Mutation not enabled in this environment. - KT-CT-4501: Unauthorized. - KT-CT-10301: Unable to instigate leave supplier process. - KT-CT-10330: Unsupported leave supplier type. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `invalidatePaymentInstruction` | `InvalidatePaymentInstruction` | `input: InvalidatePaymentInstructionInput!` | No | Invalidate an existing instruction. The possible errors that can be raised are: - KT-CT-3926: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `invalidatePreSignedToken` | `InvalidatePreSignedToken` | `input: InvalidatePreSignedTokenInput!` | No | Invalidate a previously-issued pre-signed token. The possible errors that can be raised are: - KT-CT-1129: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `invalidatePreSignedTokensForUser` | `InvalidatePreSignedTokensForUser` | `input: InvalidatePreSignedTokensForUserInput!` | No | Invalidate pre-signed tokens issued to a particular user. The possible errors that can be raised are: - KT-CT-1129: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `invalidateRefreshToken` | `InvalidateRefreshToken` | `input: InvalidateRefreshTokenInput!` | No | Invalidate a previously-issued refresh token. The possible errors that can be raised are: - KT-CT-1130: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `invalidateRefreshTokensForUser` | `InvalidateRefreshTokensForUser` | `input: InvalidateRefreshTokensForUserInput!` | No | Invalidate refresh tokens issued to a particular user. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `joinSupplierAcceptTermsAndConditions` | `JoinSupplierAcceptTermsAndConditions` | `input: JoinSupplierAcceptTermsAndConditionsInput!` | No | Accept terms and conditions for a join supplier process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `legacyProcessOrder` | `LegacyProcessOrderOutput!` | `input: LegacyProcessOrderInput!` | No | Process an Order (legacy) The possible errors that can be raised are: - KT-CT-1605: Invalid input. - KT-CT-7701: The affiliate organisation was not found. - KT-CT-8906: Opportunity not found. - KT-CT-12701: Invalid sales channel code. - KT-CT-13102: Invalid order data. - KT-CT-13103: Unprocessable order. - KT-CT-13104: Conflicting order. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `linkAccountToBusiness` | `LinkAccountToBusiness` | `input: LinkAccountToBusinessInput!` | No | Link an account to a business. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11104: Business role already allocated. - KT-CT-11105: Business role already allocated. - KT-CT-11106: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `linkUserToLine` | `LinkUserToLineResponse!` | `input: LinkUserToLineInput!` | No | Link an account user and line user together. |
| `markPrintBatchAsProcessed` | `MarkPrintBatchAsProcessed!` | `printBatchId: ID!` | No | Mark the print batch as processed. The possible errors that can be raised are: - KT-CT-9011: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `masqueradeAuthentication` | `MasqueradeAuthentication` | `masqueradeToken: String!, userId: String!` | No | Provide a temporary token to get an auth token. This is intended to allow support users to view customer data through the brand interface. |
| `moveToBucket` | `MoveToBucket` | `input: MoveToBucketInput` | No | The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `nextOperationsTeamRoundRobin` | `NextOperationsTeamRoundRobin` | `teamGroupName: String!` | No |  |
| `obtainKrakenToken` | `ObtainKrakenJSONWebToken` | `input: ObtainJSONWebTokenInput!` | No | Create a Kraken Token (JWT) for authentication. Provide the required input fields to obtain the token. The token should be used as the `Authorization` header for any authenticated requests. The possible errors that can be raised are: - KT-CT-1135: Invalid data. - KT-CT-1134: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. |
| `obtainLongLivedRefreshToken` | `ObtainLongLivedRefreshToken` | `input: ObtainLongLivedRefreshTokenInput!` | No | For authorized third-party organizations only. The possible errors that can be raised are: - KT-CT-1120: The Kraken Token has expired. - KT-CT-1121: Please use Kraken Token to issue long-lived refresh tokens. - KT-CT-1132: Unauthorized. - KT-CT-1122: Long-lived refresh tokens can only be issued for account users. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `ocppAuthentication` | `OCPPAuthentication` | `input: OCPPAuthenticationInput` | No | Trigger OCPP authentication. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4310: Unable to register OCPP authentication details. - KT-CT-1113: Disabled GraphQL field requested. |
| `pauseCollectionProcess` | `PauseCollectionProcess` | `input: PauseCollectionProcessInput!` | No | Pause a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11214: Invalid pause length for collection process. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `pauseDunning` | `PauseDunning` | `input: PauseDunningInputType!` | No | Pause the dunning process for an account. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11301: Account not in a dunning process for the given path name. - KT-CT-11302: No active dunning process found. - KT-CT-11303: Multiple active dunning processes found. - KT-CT-11304: Dunning pause process failed verifying the dates. - KT-CT-11305: Pausing the dunning process failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `payoutReferralForAccount` | `PayoutReferralForAccount` | `input: PayoutReferralForAccountInput!` | No | Pay out a referral reward for an account. The possible errors that can be raised are: - KT-CT-6712: Invalid reference. - KT-CT-6723: Unauthorized. - KT-CT-6730: Referral cannot be paid out. - KT-CT-6731: The account is unrelated to the referral. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `postCredit` | `PostCredit` | `input: PostCreditInput!` | No | Post credit to a ledger. The possible errors that can be raised are: - KT-CT-5316: Invalid data. - KT-CT-5311: The credit reason with the requested code is deprecated. - KT-CT-5312: The credit reason with the requested code does not exist. - KT-CT-5313: An error occurred whilst posting the credit. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `prepareAccount` | `PrepareAccountResult!` | `input: PrepareAccountInput!` | No | Prepare account for sign up. Returns the existing account and/or user if matching datafound for the provided input, otherwise creates a new account and account user. The possible errors that can be raised are: - KT-CT-10303: Mutation not enabled in this environment. - KT-CT-10316: Input data has invalid format. - KT-CT-10317: An error occured when trying to prepare the account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `publishApprovalApprovedEvent` | `PublishApprovalApprovedEvent` | `input: PublishApprovalApprovedEventInput!` | No | Publish an approval approved external event. The possible errors that can be raised are: - KT-CT-14501: Invalid event parameters. - KT-CT-14502: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `publishTransactionalMessagingExternalTrigger` | `PublishTransactionalMessagingExternalTrigger` | `input: PublishTransactionalMessagingExternalTriggerInput!` | No | Publish an externally defined transactional messaging trigger. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-5421: Account user not found. - KT-CT-9901: Invalid trigger type code. - KT-CT-9905: Top-level context fields are missing. - KT-CT-9906: Template variables do not match the defined schema. - KT-CT-9908: Invalid recipient information. - KT-CT-9909: Invalid recipient information. - KT-CT-9910: Invalid input field combination. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `publishTransactionalMessagingTrigger` | `PublishTransactionalMessagingTrigger` | `input: PublishTransactionalMessagingTriggerInput!` | No | Publish a trigger within the transactional messaging service. The possible errors that can be raised are: - KT-CT-9901: Invalid trigger type code. - KT-CT-9902: Invalid trigger type params. - KT-CT-9903: Trigger type cannot be published externally. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `purchaseVoucher` | `PurchaseVoucher` | `input: PurchaseVoucherInput!` | No | Purchase a voucher. |
| `reactivateCollectionProcessRecord` | `ReactivateCollectionProcessRecord` | `input: ReactivateCollectionProcessRecordInputType!` | No | Reactivate a Collection Process Record that was previously activated. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11217: Invalid collection process record status for reactivation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `recordDepositAgreementAccepted` | `RecordDepositAgreementAccepted` | `input: DepositAgreementInput!` | No | Record the customer's acceptance of a deposit agreement. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `recordFailedPayment` | `RecordFailedPayment` | `input: RecordFailedPaymentInput!` | No | Record one or more failed payments. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `recordPendingPayment` | `RecordPendingPayment` | `input: RecordPendingPaymentInput!` | No | Record one or more pending payments. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `recordSuccessfulPayment` | `RecordSuccessfulPayment` | `input: RecordSuccessfulPaymentInput!` | No | Record one or more successful payments. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `redeemLoyaltyPointsForAccountCredit` | `RedeemLoyaltyPointsForAccountCredit` | `input: RedeemLoyaltyPointsInput!` | No | Redeem the passed number of Loyalty Points as account credit. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9201: No Loyalty Point ledger found for the user. - KT-CT-9202: Loyalty Points adapter not configured. - KT-CT-9203: No ledger entries for the ledger. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9206: Indivisible points. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9209: Negative Loyalty Points balance. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `redeemReferralClaimCode` | `RedeemReferralClaimCode` | `input: RedeemReferralClaimCodeInput!` | No | Redeem the referral claim code from certain referral scheme. The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6724: Referral claim code not found. - KT-CT-6725: Referral claim code redeeming error. - KT-CT-6726: Referral claim code has already been redeemed. - KT-CT-6727: Referral claim code is not available. - KT-CT-1113: Disabled GraphQL field requested. |
| `refundPayment` | `RefundPayment` | `input: RefundPaymentInput!` | No | Refund a cleared payment. The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-3928: Idempotency key used for another repayment request. - KT-CT-3929: The payment is not in a refundable state. - KT-CT-3933: Refund amount greater than payment amount. - KT-CT-3937: Payment not eligible for refund. - KT-CT-3938: Partial refund not allowed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `regenerateSecretKey` | `RegenerateSecretKey` |  | No | Regenerate the live secret key for the authenticated user. |
| `registerEvChargerLead` | `RegisterEVChargerLead` | `lead: EVChargerLeadZohoType` | No | Register an EV Charger lead to Zoho. The possible errors that can be raised are: - KT-ES-7803: The request to Chipiron was incomplete or malformed. - KT-ES-7804: The request to Chipiron caused a conflict - might you be trying to create a duplicate? - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested. |
| `registerLeadFlowStatusEvent` | `RegisterLeadFlowStatusEvent` | `input: RegisterLeadFlowStatusEventInput!` | No | Register a flow status event for a lead. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `registerOpportunityFlowStatusEvent` | `RegisterOpportunityFlowStatusEvent` | `input: RegisterOpportunityFlowStatusEventInput!` | No | Register a flow status event for an opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `registerPhoneLead` | `RegisterPhoneLead` | `input: TelephoneLeadType` | No | Register a phone lead The possible errors that can be raised are: - KT-ES-8910: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `registerPushNotificationBinding` | `RegisterPushNotificationBinding` | `input: RegisterPushNotificationBindingInput!` | No | Register a device token to be used for push notifications for an app. This field requires the `Authorization` header to be set. |
| `registerSolarSimulatorDirectSale` | `SolarSimulatorDirectSaleOutput` | `input: SolarSimulatorDirectSaleInput` | No | Create a solar direct sale. The possible errors that can be raised are: - KT-ES-7803: The request to Chipiron was incomplete or malformed. - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested. |
| `registerSolarSimulatorLead` | `SolarSimulatorLeadOutput` | `input: SolarSimulatorLeadInput` | No | Create a solar lead. The possible errors that can be raised are: - KT-ES-7803: The request to Chipiron was incomplete or malformed. - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested. |
| `removeCampaignFromAccount` | `RemoveCampaignFromAccount` | `input: RemoveCampaignFromAccountInput!` | No | The possible errors that can be raised are: - KT-CT-7424: Failed to remove campaign from account. - KT-CT-7426: The account is not part of the given campaign. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `removeCampaignItems` | `RemoveCampaignItems` | `input: RemoveCampaignItemsInput!` | No | The possible errors that can be raised are: - KT-CT-11501: Voice campaign not found. - KT-CT-11502: Cannot remove items from multiple campaigns at once. - KT-CT-11505: Voice campaign item not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `removeItemsFromRiskList` | `RemoveItemsFromRiskList` | `input: [RiskListItemInputType]!` | No | Remove items from the risk list. The possible errors that can be raised are: - KT-CT-12106: Risk list item removal failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `removePropertyFromHierarchy` | `RemovePropertyFromHierarchy` | `input: RemovePropertyFromHierarchyInput!` | No | Remove a property from a hierarchy. This operation is idempotent - if the property is not in the hierarchy, it will succeed without error. When a property is removed, its descendants are reparented to the removed property's parent. If removing a root node, its children become new root nodes. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `requestDoubleOptIn` | `RequestDoubleOptIn` | `input: DoubleOptInInput` | No | Request a double opt in The possible errors that can be raised are: - KT-CT-9019: Invalid input. - KT-CT-9018: Account not found. - KT-CT-1111: Unauthorized. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-9023: Consent already accepted. - KT-CT-1199: Too many requests. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `requestPasswordReset` | `RequestPasswordResetOutputType` | `input: RequestPasswordResetInput!` | No | Provide the email address of an account user to send them an email with instructions on how to reset their password. The possible errors that can be raised are: - KT-CT-11331: Invalid input data. - KT-CT-11332: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. |
| `requestPrintedBill` | `RequestPrintedBill` | `input: RequestPrintedBillInput!` | No | Request an issued bill to be printed and (re)posted to billing address of the account. The possible errors that can be raised are: - KT-CT-3824: Unauthorized. - KT-CT-9705: The billing document has not been issued. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `resetPassword` | `ResetPasswordMutationPayload` | `input: ResetPasswordMutationInput!` | Yes (The 'resetPassword' field is deprecated. Please use `resetUserPassword` instead. - Marked as deprecated on 2024-12-04. - Scheduled for removal on or after 2025-06-01. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/81/) | Reset the password of an account user indicated by the userId to the value supplied. |
| `resetUserPassword` | `ResetUserPasswordOutput` | `input: ResetUserPasswordInput!` | No | Reset the password of an account user. Raises `KT-CT-5450` if password validation fails. Inspect the `validationErrors` extension to get the exact validation error: ```json { "data": {"resetUserPassword": null}, "errors": [ { "message": "Password is invalid.", "path": ["resetUserPassword"], "extensions": { "errorType": "VALIDATION", "errorCode": "KT-CT-5450", "errorDescription": "Given password fails password policy requirements.", "validationErrors": [ { "code": "password_too_short", "message": "This password is too short. It must contain at least 7 characters.", "inputPath": ["input", "password"] }, { "code": "password_too_common", "message": "This password is too common.", "inputPath": ["input", "password"] } ] } } ] } ``` The validation error's `code` can be any of - `password_too_short` - `password_too_common` - `password_reused` - `password_matches_current` - `password_has_too_few_numeric_characters` - `password_has_too_few_special_characters` - `password_has_too_few_lowercase_characters` - `password_has_too_few_uppercase_characters` - `password_contains_account_number` - `password_contains_part_of_email_address` The possible errors that can be raised are: - KT-CT-4125: Unauthorized. - KT-CT-1132: Unauthorized. - KT-CT-5450: Password is invalid. - KT-CT-1113: Disabled GraphQL field requested. |
| `resumeCollectionProcess` | `ResumeCollectionProcess` | `input: ResumeCollectionProcessInput!` | No | Resume a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11215: Unable to resume, collection process is not paused. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `resumeControl` | `ResumeDeviceControl` | `input: AccountNumberInput` | Yes (The 'resumeControl' field is deprecated. Please use 'updateDeviceSmartControl' instead. - Marked as deprecated on 2024-09-17. - Scheduled for removal on or after 2025-12-11. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/468/) | Resume control of the device. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4359: Unable to resume device control. - KT-CT-1113: Disabled GraphQL field requested. |
| `reverseEnrollment` | `EnrollmentReversed!` | `input: ReverseEnrollmentInput!` | No | Reverse an enrollment (Join Supplier process). The possible errors that can be raised are: - KT-CT-10312: Mutation not enabled in this environment. - KT-CT-10318: Enrollment process not found. - KT-CT-10349: Enrollment process is not reversible. - KT-CT-10350: Enrollment process can still be cancelled. - KT-CT-10351: Enrollment process being cancelled cannot be reversed. - KT-CT-10352: Market actions cannot be reversed for this enrollment process. - KT-CT-10353: Failed to reverse enrollment process. - KT-CT-10354: Enrollment reversal cut-off has passed. - KT-CT-10355: Enrollment reversal is not allowed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `reverseLeaveSupplier` | `LeaveSupplierReversed!` | `input: ReverseLeaveSupplierInput!` | No | Reverse a leave supplier process. The possible errors that can be raised are: - KT-CT-10304: Mutation not enabled in this environment. - KT-CT-10302: Invalid data. - KT-CT-10341: Leave supplier process is not reversible. - KT-CT-10342: Leave supplier process can still be cancelled. - KT-CT-10343: Leave supplier process being cancelled cannot be reversed. - KT-CT-10344: Leave supplier reversal cut-off has passed. - KT-CT-10345: Occupier leave with real join cannot be reversed. - KT-CT-10346: Market action reversal is not supported for this leave supplier process. - KT-CT-10347: Failed to reverse leave supplier process. - KT-CT-10348: Leave supplier reversal is missing required dependencies. - KT-CT-1607: Value cannot be empty. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `revokeAgreement` | `RevokeAgreement` | `input: RevokeAgreementInput!` | No | Revoke an agreement. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1501: Agreement not found. - KT-CT-1502: Billed agreements cannot be revoked. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `revokeContract` | `RevokeContractOutput!` | `input: RevokeContractInput!` | No | Revoke an existing contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10022: Contract already terminated. - KT-CT-10023: Contract is already revoked. - KT-CT-10024: Contract already expired. - KT-CT-10032: Contract has already started. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `revokeUserAccessFromBusiness` | `RevokeUserAccessFromBusiness` | `input: RevokeUserAccessFromBusinessInput!` | No | Revoke the selected role from the user for the business. The possible errors that can be raised are: - KT-CT-5463: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-13501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `runAgreementRollover` | `RunAgreementRollover` | `input: RunAgreementRolloverInput!` | No | Run an agreement rollover. The possible errors that can be raised are: - KT-CT-13705: Agreement rollover not found. - KT-CT-13706: Agreement rollover has an invalid status for this operation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `scheduleQuoteFollowUp` | `ScheduleQuoteFollowUp` | `input: QuoteShareInput!` | No | Schedule a quote follow-up to the provided recipient. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4632: Invalid recipient information. - KT-CT-4633: Mutation not enabled in this environment. - KT-CT-1113: Disabled GraphQL field requested. |
| `selectChargePointMakeForSmartFlexOnboarding` | `SelectChargePointMakeForSmartFlexOnboarding` | `input: SelectChargePointMakeInput!` | Yes (The 'selectChargePointMakeForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Select the charge point make to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectChargePointVariantForSmartFlexOnboarding` | `SelectChargePointVariantForSmartFlexOnboarding` | `input: SelectChargePointVariantInput!` | Yes (The 'selectChargePointVariantForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Select the charge point model variant to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectDeviceTypeForSmartFlexOnboarding` | `SelectDeviceTypeForSmartFlexOnboarding` | `input: SelectDeviceTypeInput!` | Yes (The 'selectDeviceTypeForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Select the device type to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectFromListForSmartFlexOnboarding` | `SelectFromListForSmartFlexOnboarding` | `input: SelectFromListInput!` | No | Select from a list of options presented. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectInverterMakeForSmartFlexOnboarding` | `SelectInverterMakeForSmartFlexOnboarding` | `input: SelectInverterMakeInput!` | Yes (The 'selectInverterMakeForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Select the inverter make to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectProducts` | `SelectProducts` | `input: SelectProductsInput!` | No | Mark quoted products on a quote request as selected. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4634: Quoted product with given id not found. - KT-CT-4626: No product selected for the given quote code. - KT-CT-4635: Missing a quoted product for at least one quoted supply point on the quote request. - KT-CT-4636: Quoted product not linked to a product. - KT-CT-4646: Attempted to select multiple products for the same quoted supply point. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectUserVehicleForSmartFlexOnboarding` | `SelectUserVehicleForSmartFlexOnboarding` | `input: SelectUserVehicleInput!` | Yes (The 'selectUserVehicleForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Select the user's vehicle to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectVehicleMakeForSmartFlexOnboarding` | `SelectVehicleMakeForSmartFlexOnboarding` | `input: SelectVehicleMakeInput!` | Yes (The 'selectVehicleMakeForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Select the vehicle make to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectVehicleOrChargePointForSmartFlexOnboarding` | `CompleteSelectVehicleOrChargePointForSmartFlexOnboarding` | `input: SelectVehicleOrChargePointInput!` | No | Select the vehicle or charge point for the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `selectVehicleVariantForSmartFlexOnboarding` | `SelectVehicleVariantForSmartFlexOnboarding` | `input: SelectVehicleVariantInput!` | Yes (The 'selectVehicleVariantForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Select the vehicle model variant to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `sendOfferQuoteSummary` | `SendOfferQuoteSummary` | `input: OfferQuoteSummaryInput!` | No | Send an offer quote summary to all active account users. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4178: No account found with given account number. - KT-CT-12407: The offer group does not contain an accepted offer. - KT-CT-5518: Account user not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `sendQuoteSummary` | `SendQuoteSummary` | `input: QuoteShareInput!` | No | Send a quote summary to the provided recipient. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4178: No account found with given account number. - KT-CT-4632: Invalid recipient information. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `sendVerificationEmail` | `SendVerificationEmail` | `input: SendVerificationEmailInput!` | No | Verify user's email address. The possible errors that can be raised are: - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `setDevicePreferences` | `SmartFlexDeviceInterface` | `input: SmartFlexDevicePreferencesInput!` | No | Set the user preferences for a device. The possible errors that can be raised are: - KT-CT-4314: Unable to get provider details. - KT-CT-4321: Serializer validation error. - KT-CT-4374: An error occurred while trying to set your device preferences. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `setLoyaltyPointsUser` | `SetLoyaltyPointsUser` | `input: SetLoyaltyPointsUserInput!` | No | Set the Loyalty Point user for the account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-9214: Couldn't assign user loyalty points role. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `setOpportunityOutcome` | `SetOpportunityOutcome` | `input: SetOpportunityOutcomeInput!` | No | Update the opportunity outcome to mark the opportunity as won or lost. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `setPaymentPreference` | `SetPaymentPreference` | `input: SetPaymentPreferenceInput!` | No | Set a preference to collect payments from a specific payment method. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3967: Payment method is not valid. - KT-CT-3968: Preference cannot be set this soon. - KT-CT-3969: Preferences must change on a specific day of the week for weekly schedules. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `setUpDirectDebitInstruction` | `SetUpDirectDebitInstruction` | `input: SetUpDirectDebitInstructionInput!` | No | Set up a new direct debit instruction. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3940: Invalid data. - KT-CT-5415: Account user not found. - KT-CT-11103: Business not found. - KT-CT-3971: Instruction owners are not valid. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `setUpDirectDebitInstructionForBusiness` | `SetUpDirectDebitInstructionForBusiness` | `input: SetUpDirectDebitInstructionForBusinessInput!` | No | Set up a new direct debit instruction for a business. The possible errors that can be raised are: - KT-CT-3940: Invalid data. - KT-CT-3956: Temporary error occurred. - KT-CT-11107: Unauthorized. - KT-CT-3948: Could not set up direct debit instruction. - KT-CT-3971: Instruction owners are not valid. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `setUpDirectDebitInstructionFromStoredDetails` | `SetUpDirectDebitInstructionFromStoredDetails` | `input: SetUpDirectDebitInstructionFromStoredDetailsInput!` | No | Set up a new direct debit instruction from stored details. The possible errors that can be raised are: - KT-CT-3956: Temporary error occurred. - KT-CT-3948: Could not set up direct debit instruction. - KT-CT-3971: Instruction owners are not valid. - KT-CT-5415: Account user not found. - KT-CT-11103: Business not found. - KT-CT-4123: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `setVehicleChargePreferences` | `SetVehicleChargingPreferences` | `input: VehicleChargingPreferencesInput` | Yes (The 'setVehicleChargePreferences' field is deprecated. Please use `setDevicePreferences` instead of this endpoint. - Marked as deprecated on 2024-09-18. - Scheduled for removal on or after 2026-01-26. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/469/) | Set charging preferences for your electric vehicle. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4321: Serializer validation error. - KT-CT-4353: An error occurred while trying to update your charging preferences. - KT-CT-1113: Disabled GraphQL field requested. |
| `shareGoodsQuote` | `ShareGoodsQuote` | `input: ShareGoodsQuoteInput!` | No | Share a goods quote. The possible errors that can be raised are: - KT-CT-4122: Invalid email. - KT-CT-8203: Received an invalid quote code. - KT-CT-1113: Disabled GraphQL field requested. |
| `startCollectionProcess` | `StartCollectionProcess` | `input: StartCollectionProcessInput!` | No | Start a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11208: Invalid billing document identifier for collection process. - KT-CT-11209: Collection process configuration does not have published version. - KT-CT-11210: Active collection process for entity already exists. - KT-CT-11211: Too many active collection processes for config. - KT-CT-11212: Invalid collection process config code. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `startCustomerVerification` | `StartCustomerVerification` | `input: StartCustomerVerificationInput!` | No | Start the customer verification using the provided verification method. The possible errors that can be raised are: - KT-CT-1701: Brand does not exist. - KT-CT-4194: Verification type not supported yet. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `startOnSiteJobsAppointmentBookingSession` | `StartOnSiteJobsAppointmentBookingSession` | `appointmentBookingDetails: OnSiteJobsAppointmentBookingDetailsInput!, appointmentIdToReschedule: UUID, overrideAppointmentCheckWarnings: Boolean = false, requestId: UUID!` | No | Start the appointment booking process for an on-site jobs request. The possible errors that can be raised are: - KT-CT-13010: No booking adapter found for agent. - KT-CT-13020: Could not identify agent from property. - KT-CT-13021: Invalid job type. - KT-CT-13022: Work category not found for job type. - KT-CT-13023: Appointment booking checks failed. - KT-CT-13024: Appointment booking checks returned warnings. - KT-CT-13032: Request does not exist. - KT-CT-13054: Appointment not found for rescheduling. - KT-CT-13055: Appointment does not belong to the specified request. - KT-CT-13056: Appointment cannot be rescheduled. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `startReAuthentication` | `StartReAuthentication` | `input: StartReAuthenticationInput!` | No | Create a wizard for re-authenticating a device with SmartFlex. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4385: Re-authentication is not supported for this device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `startSmartFlexOnboarding` | `StartSmartFlexOnboarding` | `input: StartSmartFlexOnboardingInput!` | No | Create a wizard for onboarding a device with SmartFlex. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4385: Re-authentication is not supported for this device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `startTestChargeForSmartFlexOnboarding` | `StartTestChargeForSmartFlexOnboarding` | `input: CompleteSmartFlexOnboardingStepInput!` | Yes (The 'startTestChargeForSmartFlexOnboarding' field is deprecated. This functionality will no longer be available. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Attempt to start a test charge. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `stopAutomatedPayments` | `StopAutomatedPayments` | `input: StopAutomatedPaymentsInput!` | No | Set a preference to not collect automated payments. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3968: Preference cannot be set this soon. - KT-CT-3969: Preferences must change on a specific day of the week for weekly schedules. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `storeDirectDebitPaymentMethodDetails` | `StoreDirectDebitPaymentMethodDetails` | `input: StoreDirectDebitPaymentMethodDetailsInput!` | No | Store bank details with the vendor. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3940: Invalid data. - KT-CT-3956: Temporary error occurred. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `storePaymentInstruction` | `StorePaymentInstruction` | `input: StorePaymentInstructionInput!` | No | Store a new payment instruction created through the embedded process. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `submitCustomerFeedback` | `SubmitCustomerFeedback` | `input: CustomerFeedbackInputType!` | No | Submit customer feedback. The possible errors that can be raised are: - KT-CT-5514: Unable to submit feedback. - KT-CT-5511: The feedback_id should be provided for feedback source. - KT-CT-5512: The feedback doesn't match the account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `submitGasSelfReading` | `SubmitGasSelfReading` | `input: GasSelfReadingSubmissionInput!` | No | Submit a self-reading for a supply point. The possible errors that can be raised are: - KT-ES-4508: Self-reading input is invalid. - KT-ES-4509: Self-reading submission failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `submitRepaymentRequest` | `SubmitRepaymentRequest` | `input: RequestRepaymentInputType!` | No | Submit a repayment request. The possible errors that can be raised are: - KT-CT-1132: Unauthorized. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3823: Unauthorized. - KT-CT-3926: Unauthorized. - KT-CT-3927: Invalid Amount. - KT-CT-3928: Idempotency key used for another repayment request. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `suspendControl` | `SuspendDeviceControl` | `input: AccountNumberInput` | Yes (The 'suspendControl' field is deprecated. Please use 'updateDeviceSmartControl' instead. - Marked as deprecated on 2024-09-17. - Scheduled for removal on or after 2025-12-11. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/468/) | Suspend control of the device. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4358: Unable to suspend device control. - KT-CT-1113: Disabled GraphQL field requested. |
| `switchAccountToVariablePaymentSchedule` | `SwitchAccountToVariablePaymentSchedule` | `input: SwitchAccountToVariablePaymentScheduleInput!` | No | Switch account to variable payment schedule. Current schedule type will be preserved. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3921: Account not found. - KT-CT-3922: Ledger not found for the account. - KT-CT-3947: An unexpected error occurred. - KT-CT-3984: Could not delete conflicting future payment schedule. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `terminateAgreement` | `TerminateAgreement` | `input: TerminateAgreementInput!` | No | Terminate an agreement. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-1513: Unable to terminate agreement. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `terminateContract` | `TerminateContractOutput!` | `input: TerminateContractInput!` | No | Terminate an existing contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10007: Unable to terminate contract. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10013: Requested termination date is invalid. - KT-CT-10022: Contract already terminated. - KT-CT-10023: Contract is already revoked. - KT-CT-10024: Contract already expired. - KT-CT-10025: Contract has not started yet. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `terminateCreditTransferPermission` | `TerminateCreditTransferPermission` | `input: TerminateCreditTransferPermissionInput!` | No | Terminate credit transfer permission. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3825: Credit transfer permission not found. - KT-CT-3827: The ledger is not valid. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `terminateSolarWalletRelationship` | `TerminateSolarWalletRelationship` | `input: TerminateSolarWalletRelationshipType!` | Yes (The 'terminateSolarWalletRelationship' field is deprecated. Use 'terminateCreditTransferPermission' mutation instead. - Marked as deprecated on 2025-02-10. - Scheduled for removal on or after 2025-08-10.) | Terminate solar wallet sharing credit between a solar wallet credit ledger and spain electricity ledger. The possible errors that can be raised are: - KT-ES-4116: Account not found. - KT-ES-7807: The request to terminate a solar wallet sharing credit between ledgers was incomplete or malformed. - KT-ES-7808: Couldn't stop sharing credit between ledgers because credit sharing ledger doesn't exist. - KT-ES-7809: There is no ledger of this type on this account.. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `thirdPartyCompleteDeviceRegistration` | `ThirdPartyCompleteDeviceRegistration` | `input: CompleteDeviceRegistrationInput` | Yes (The 'thirdPartyCompleteDeviceRegistration' field is deprecated. This functionality will no longer be available. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.) | Completes the registration of a device if the contract is eligible and the device registration valid. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4322: Unable to complete registration error. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `transferLeadOpportunities` | `TransferLeadOpportunities` | `input: TransferLeadOpportunitiesInput!` | No | Transfer opportunities across leads. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `transferLedgerBalance` | `TransferLedgerBalance` | `input: TransferLedgerBalanceInputType!` | No | Transfer value from a source ledger to a destination ledger. This decreases the balance of the source ledger by the given amount and increases the balance of the destination ledger by the same amount. If the amount is negative, the effect is reversed (the source ledger's balance increases and the destination ledger's balance decreases). This field requires the `Authorization` header to be set. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3823: Unauthorized. - KT-CT-9701: Balance transfer to same account is not allowed. - KT-CT-9702: Balance transfer is not support for debit account with Zero balance. - KT-CT-9703: Balance transfer is not supported for debit account. - KT-CT-9704: Balance transfer amount should be non-zero. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `transferLoyaltyPointsBetweenUsers` | `TransferLoyaltyPointsBetweenUsers` | `input: TransferLoyaltyPointsBetweenUsersInput!` | No | Transfer Loyalty Point from one account user to another. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9209: Negative Loyalty Points balance. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `triggerBoostCharge` | `PerformBoostCharge` | `input: AccountNumberInput` | Yes (The 'triggerBoostCharge' field is deprecated. Please use 'updateBoostCharge' instead. - Marked as deprecated on 2025-05-12. - Scheduled for removal on or after 2026-01-26. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/607/) | Initiate a boost charge for an electric vehicle (EV). This will start charging the EV and will not stop until the battery reaches 100% charged. If it is not possible to initiate a boost charge, a KT-CT-4357 error will be returned. It may have a `boostChargeRefusalReasons` extension which lists the reasons why the boost charge was refused. Possible reasons include: - `BC_DEVICE_NOT_YET_LIVE` (device is not yet live) - `BC_DEVICE_RETIRED` (device is retired) - `BC_DEVICE_SUSPENDED` (device is suspended) - `BC_DEVICE_DISCONNECTED` (device is disconnected) - `BC_DEVICE_NOT_AT_HOME` (device is not at home) - `BC_BOOST_CHARGE_IN_PROGRESS` (boost charge already in progress) - `BC_DEVICE_FULLY_CHARGED` (device is already fully charged) The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4356: A boost charge cannot currently be performed. - KT-CT-4357: Unable to trigger boost charge. - KT-CT-1113: Disabled GraphQL field requested. |
| `triggerCollectionProcessMessage` | `TriggerCollectionProcessMessage` | `input: TriggerCollectionProcessMessageInput!` | No | Trigger a collection process message with safety checks. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `triggerPostUploadOperations` | `TriggerPostUploadOperations!` | `s3Key: String!` | No | The possible errors that can be raised are: - KT-CT-8710: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `triggerTestCharge` | `PerformTestCharge` | `input: AccountNumberInput` | No | Initiate a test charge of an electric vehicle (EV). This is to ensure that the EV or EVSE (charge point) can be controlled remotely and successfully charged for a short period. If it is not possible to initiate a test charge, a KT-CT-4355 error will be returned. It may have a `testChargeRefusalReasons` extension which lists the reasons why the test charge was refused. Possible reasons include: - `TC_DEVICE_LIVE` (device is already live) - `TC_DEVICE_ONBOARDING_IN_PROGRESS` (test dispatch already in progress) - `TC_DEVICE_RETIRED` (device is retired) - `TC_DEVICE_SUSPENDED` (device is suspended) - `TC_DEVICE_DISCONNECTED` (device is disconnected) - `TC_DEVICE_ALREADY_CHARGING` (device is already charging) - `TC_DEVICE_AWAY_FROM_HOME` (device is away from home) - `TC_DEVICE_NO_LOCATION_CONFIGURED` (device has no location configured) - `TC_DEVICE_LOCATION_UNABLE_TO_IDENTIFY` (unable to identify device location) - `TC_DEVICE_LOCATION_MISSING` (device location is missing) The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4362: Device not ready for test charge. - KT-CT-4355: Unable to trigger charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `unenrollAccountFromLoyaltyProgram` | `UnenrollAccountFromLoyaltyProgram` | `input: UnenrollAccountFromLoyaltyProgramInput!` | No | Unenroll users account from Loyalty program. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9220: Ineligible loyalty points unenrollment. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `unlinkUserFromLine` | `UnlinkUserFromLineResponse!` |  | No | Unlink an account user and line together. |
| `updateAccountBillingAddress` | `UpdateAccountBillingAddress` | `input: AccountBillingAddressInput!` | No | Update the account billing address. The possible errors that can be raised are: - KT-CT-4145: Invalid address. - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAccountBillingEmail` | `UpdateAccountBillingEmail` | `input: UpdateAccountBillingEmailInput!` | No | Update account billing email. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4122: Invalid email. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAccountConsents` | `UpdateAccountConsents` | `accountNumber: String!, consents: [ConsentInput]!` | No | Update the consents of an account The possible errors that can be raised are: - KT-CT-9014: Duplicate consent. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-9018: Account not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAccountReference` | `UpdateAccountReference` | `input: AccountReferenceInput!` | No | Update an account reference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8311: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAccountReferralStatus` | `UpdateAccountReferralStatus` | `input: UpdateAccountReferralStatusInput!` | No | Update the status of an account referral. The possible errors that can be raised are: - KT-CT-6712: Invalid reference. - KT-CT-6732: Invalid referral status transition. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAccountUser` | `UpdateAccountUser` | `input: UpdateAccountUserInput` | No | Update an account. The possible errors that can be raised are: - KT-ES-5410: Invalid data. - KT-CT-5414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAccountUserConsents` | `UpdateAccountUserConsents` | `consents: [ConsentTypeInput], userNumber: String` | No | Update the consents of an account user (the authenticated user) The possible errors that can be raised are: - KT-CT-9014: Duplicate consent. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-1111: Unauthorized. - KT-CT-5421: Account user not found. - KT-CT-5422: Invalid data. - KT-CT-1605: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateActivePurchase` | `UpdateActivePurchase` | `input: UpdatePurchaseInput!` | No | Update an active purchase. The possible errors that can be raised are: - KT-CT-8225: Received an invalid purchaseId. - KT-CT-8226: The provided purchase is not active. - KT-CT-8206: Invalid data. - KT-CT-8227: Available grants could not be applied. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAffiliateLink` | `UpdateAffiliateLink!` | `input: UpdateAffiliateLinkInputType!` | No | Update an existing affiliate link. The possible errors that can be raised are: - KT-CT-7711: Invalid data. - KT-CT-7713: Invalid data. - KT-CT-7714: Invalid data. - KT-CT-7715: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAffiliateOrganisation` | `UpdateAffiliateOrganisation!` | `input: UpdateAffiliateOrganisationInputType!` | No | Update an existing affiliate organisation. The possible errors that can be raised are: - KT-CT-7717: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAgentAuxiliaryStatus` | `UpdateAgentAuxiliaryStatus` | `input: UpdateAgentAuxiliaryStatusInput!` | No | The possible errors that can be raised are: - KT-CT-7813: Support user not found with that username. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAgreementPeriod` | `UpdateAgreementPeriod` | `input: UpdateAgreementPeriodInput!` | No | Update the period of an agreement. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-1501: Agreement not found. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1504: Account does not match with the agreement. - KT-CT-1505: Unable to edit agreement. - KT-CT-1506: Agreement period is not within the supply and property period. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAgreementRescission` | `UpdateAgreementRescission` | `input: UpdateAgreementRescissionInput!` | No | Update an agreement rescission. The possible errors that can be raised are: - KT-CT-14101: Agreement rescission not found. - KT-CT-14102: Cannot update completed agreement rescission. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAgreementRollover` | `UpdateAgreementRollover` | `input: UpdateAgreementRolloverInput!` | No | Update an agreement rollover. The possible errors that can be raised are: - KT-CT-4910: No product exists with the given input. - KT-CT-13705: Agreement rollover not found. - KT-CT-13706: Agreement rollover has an invalid status for this operation. - KT-CT-13707: Agreement rollover has an invalid type for this operation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateApiException` | `UpdateAPIException` | `input: UpdateAPIExceptionInput!` | No | Mutation to update an existing APIException instance. The possible errors that can be raised are: - KT-CT-7804: No fields present in the input for updating the APIException. - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-7809: Update results in no changes to API Exception. - KT-CT-7805: Too many tags associated with this API Exception. - KT-CT-7806: Cannot create duplicate tags for the same API exception. - KT-CT-7801: Received an invalid operationsTeamId. - KT-CT-7811: Received an invalid assignedUserId. - KT-CT-7812: Support user is inactive. - KT-CT-7814: Received an invalid accountNumber. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateApiExceptionNote` | `UpdateAPIExceptionNote` | `input: UpdateAPIExceptionNoteInput!` | No | Mutation to update an existing APIExceptionNote instance. The possible errors that can be raised are: - KT-CT-7807: Received an invalid apiExceptionNoteId. - KT-CT-7808: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateAutoTopUpAmount` | `UpdateAutoTopUpAmount` | `input: UpdateAutoTopUpAmountInput!` | No | Change the auto top up amount for the payment schedule. The possible errors that can be raised are: - KT-CT-3815: No active payment schedule found for this account. - KT-CT-3941: Invalid data. - KT-CT-3942: An unexpected error occurred. - KT-CT-3947: An unexpected error occurred. - KT-CT-3953: The payment schedule is not a balance triggered schedule. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3822: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateBillingAddress` | `UpdateBillingAddress` | `input: UpdateAccountBillingAddressInput` | No | Updates billing address details. The possible errors that can be raised are: - KT-ES-4118: Invalid data. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateBillingDetails` | `UpdateBillingDetails` | `input: UpdateAccountBillingDetailsInput` | No | Updates billing details. The possible errors that can be raised are: - KT-ES-4119: Invalid data. - KT-ES-1130: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateBoostCharge` | `SmartFlexDeviceInterface` | `input: UpdateBoostChargeInput` | No | Update the boost charge for a specific device. If it is not possible to initiate a boost charge, a KT-CT-4357 error will be returned. It may have a `boostChargeRefusalReasons` extension which lists the reasons why the boost charge was refused. Possible reasons include: - `BC_DEVICE_NOT_YET_LIVE` (device is not yet live) - `BC_DEVICE_RETIRED` (device is retired) - `BC_DEVICE_SUSPENDED` (device is suspended) - `BC_DEVICE_DISCONNECTED` (device is disconnected) - `BC_DEVICE_NOT_AT_HOME` (device is not at home) - `BC_BOOST_CHARGE_IN_PROGRESS` (boost charge already in progress) - `BC_DEVICE_FULLY_CHARGED` (device is already fully charged) The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4354: Unable to cancel boost charge. - KT-CT-4356: A boost charge cannot currently be performed. - KT-CT-4357: Unable to trigger boost charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateCollectionProcessRecordToActive` | `UpdateCollectionProcessRecordToActive` | `input: UpdateCollectionProcessRecordToActiveInputType!` | No | Update the Collection Process Record from raised status to active. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11202: No External reference provided. - KT-CT-11207: Unsupported external source for collection process. - KT-CT-11218: External reference cannot be updated once it has been set. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateCollectionProcessRecordToComplete` | `UpdateCollectionProcessRecordToComplete` | `input: UpdateCollectionProcessRecordToCompleteInputType!` | No | Update the Collection Process Record from raised status to complete. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11203: No Completion reason provided. - KT-CT-11204: No Completion details provided. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateCommsDeliveryPreference` | `UpdateCommsDeliveryPreference` | `input: UpdateCommsDeliveryPreferenceInput!` | No | Update account communication delivery preference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4136: Cannot set comms preference to email when account has no email. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateCommsPreferences` | `UpdateAccountUserCommsPreferencesMutationPayload` | `input: UpdateAccountUserCommsPreferencesMutationInput!` | No | Update the comms preferences of the account user (the authenticated user). |
| `updateDcaProceeding` | `UpdateDCAProceeding` | `input: UpdateDCAProceedingInputType!` | No | Update the status of a DCA proceeding. The possible errors that can be raised are: - KT-CT-11610: unable to edit the debt collection proceeding. - KT-CT-11604: Active debt collection proceeding does not exist for account. - KT-CT-11605: Multiple active Proceeding's found for same agency and campaign on account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateDeviceGridExport` | `SmartFlexDeviceInterface` | `input: UpdateDeviceGridExportInput` | No | Update the grid export preference for a device. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4386: An error occurred while trying to update your device's grid export status. - KT-CT-1113: Disabled GraphQL field requested. |
| `updateDeviceSmartControl` | `SmartFlexDeviceInterface` | `input: SmartControlInput!` | No | Suspends or resumes the smart control of a specific device. For some devices, this will also adjust smart control of related devices. e.g. suspending one zone in a multi-zone heat pump system will suspend all zones in that system. The possible errors that can be raised are: - KT-CT-4313: Could not find KrakenFlex device. - KT-CT-4314: Unable to get provider details. - KT-CT-4387: Could not find the KrakenFlex controller device. - KT-CT-4358: Unable to suspend device control. - KT-CT-4359: Unable to resume device control. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateDocumentAccessibilityPreference` | `UpdateDocumentAccessibilityPreference!` | `input: UpdateDocumentAccessibilityPreferenceInput!` | No | Update the document accessibility preference for an account. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateIsChargingDurationCapped` | `SmartFlexDeviceInterface` | `input: UpdateIsChargingDurationCappedInput` | No | Update the charging duration cap preference for a device. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4389: An error occurred while trying to update your device's isChargingDurationCapped setting. - KT-CT-4390: An error occurred while trying to update your device's preference. - KT-CT-1113: Disabled GraphQL field requested. |
| `updateLeadAssignment` | `UpdateLeadAssignment` | `input: UpdateLeadAssignmentInput!` | No | Update assignment fields for a Lead. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateLeadDetails` | `UpdateLeadDetails` | `input: UpdateLeadDetailsInput!` | No | Update the details of a lead. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-8912: Funnel not found. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8935: National ID bad input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateLeadStage` | `UpdateLeadStage` | `input: UpdateLeadStageInput!` | No | Update the stage of a lead. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-8914: Stage not found. - KT-CT-8915: Stages are not in the same funnel. - KT-CT-8916: Current stage mismatch. - KT-CT-8917: Stage transition not allowed. - KT-CT-8918: Stage precondition not met. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateLeaveSupplier` | `LeaveSupplierUpdated!` | `input: UpdateLeaveSupplierInput!` | No | Update an existing leave supplier process. The possible errors that can be raised are: - KT-CT-10304: Mutation not enabled in this environment. - KT-CT-10302: Invalid data. - KT-CT-10309: Failed to update leave supplier process - the service is not enabled. - KT-CT-10310: Failed to update leave supplier process. The process status is not in updatable status. - KT-CT-1607: Value cannot be empty. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateMessageTags` | `UpdateMessageTags` | `input: UpdateMessageTagsInput` | No | The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-7614: The Ink tag was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateMetadata` | `UpdateMetadata` | `input: MetadataInput!` | No | Update metadata on an object. The possible errors that can be raised are: - KT-CT-4323: Unauthorized. - KT-CT-8413: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateNotesOnOpportunity` | `UpdateNotesOnOpportunity` | `input: UpdateNotesOnOpportunityInput!` | No | Update the notes of an opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateOfferGroupOnOpportunity` | `UpdateOfferGroupOnOpportunity` | `input: UpdateOfferGroupOnOpportunityInput!` | No | Update the offer group of an opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateOnSiteJobsAppointment` | `UpdateOnSiteJobsAppointment` | `input: OnSiteJobsUpdateAppointmentInput!` | No | Update an Appointment. The possible errors that can be raised are: - KT-CT-13001: Appointment does not exist. - KT-CT-13043: Cannot update appointment as it has terminal status. - KT-CT-13044: Failed to update appointment slot. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13039: Cancellation fields require CANCELLED status. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13062: Datetime field must be timezone-aware. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateOnSiteJobsRequest` | `UpdateOnSiteJobsRequest` | `input: OnSiteJobsUpdateRequestInput!` | No | Update an On Site Jobs Request. The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13035: Request is inactive. - KT-CT-13038: Invalid request status. - KT-CT-13040: Agent not set on request. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateOpportunityAssignment` | `UpdateOpportunityAssignment` | `input: UpdateOpportunityAssignmentInput!` | No | Update assignment fields for an Opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8903: Unable to update opportunity. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateOpportunityDetails` | `UpdateOpportunityDetails` | `input: UpdateOpportunityDetailsInput!` | No | Update the details of an opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8930: Unable to parse address. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8912: Funnel not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateOpportunityExtraDetails` | `UpdateOpportunityExtraDetails` | `input: UpdateExtraDetailsInput!` | No | Update the extra details of a opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8926: Unable to create opportunity. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateOpportunityStage` | `UpdateOpportunityStage` | `input: UpdateOpportunityStageInput!` | No | Update the stage of a opportunity. The possible errors that can be raised are: - KT-CT-8903: Unable to update opportunity. - KT-CT-8910: Received opportunity current stage is not valid. - KT-CT-8914: Stage not found. - KT-CT-8915: Stages are not in the same funnel. - KT-CT-8916: Current stage mismatch. - KT-CT-8917: Stage transition not allowed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updatePassword` | `UpdatePassword` | `input: UpdatePasswordInput` | No | Update password of the authenticated user This field requires the `Authorization` header to be set. The possible errors that can be raised are: - KT-CT-5460: Old password is invalid. - KT-CT-5450: Password is invalid. - KT-CT-1113: Disabled GraphQL field requested. |
| `updatePaymentDetails` | `UpdatePaymentDetails` | `newPaymentDetails: UpdateAccountPaymentInput` | No | Updates payment details. The possible errors that can be raised are: - KT-ES-4120: Invalid data. - KT-ES-1130: Unauthorized. - KT-ES-3910: Payment instruction couldn't be created or was cancelled. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateProductPrices` | `UpdateProductPricesOutput!` | `input: UpdateProductPricesInput!` | No | Update the prices of a product. The possible errors that can be raised are: - KT-CT-12008: Unable to find the product. - KT-CT-12009: Specified product does not have a specification. - KT-CT-12010: Unable to find the product's specification. - KT-CT-12011: The list of provided prices contains validation errors. - KT-CT-12012: Product prices start date is in the past. - KT-CT-12013: Product prices would overwrite existing prices. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateSiteworksRequest` | `UpdateSiteworksRequest` | `input: UpdateSiteworksRequestInputType!` | Yes (The 'updateSiteworksRequest' field is deprecated. Please use updateOnSiteJobsRequest instead. - Marked as deprecated on 2026-03-01. - Scheduled for removal on or after 2026-09-01.) | Update a Request. The possible errors that can be raised are: - KT-CT-4231: Unauthorized. - KT-CT-4232: Status passed is not valid. - KT-CT-4233: Request does not exist. - KT-CT-4234: Terminated Request cannot be updated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateUser` | `UpdateUserMutation` | `input: UpdateUserInput!` | No | Update the account user details of the authenticated user. Only one name field can be updated per day, other fields can be updated freely. This prevents users from switching accounts to someone else (usually when moving homes). All account changes should be handled by operations or the move out journey. New customers are exempt from this rule for the first 31 days. This field requires the `Authorization` header to be set. The possible errors that can be raised are: - KT-CT-5413: Invalid data. - KT-CT-5414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `updateUserDetails` | `UpdateAccountUserMutationPayload` | `input: UpdateAccountUserMutationInput!` | Yes (The 'updateUserDetails' field is deprecated. Please use the 'updateUser' mutation instead. - Marked as deprecated on 2020-10-02. - Scheduled for removal on or after 2023-04-06.) | **DEPRECATED: Please use updateUser instead** Update the account user details of the authenticated user. Only one field can be updated per day. This prevents users from switching accounts to someone else (usually when moving homes) All account changes should be handled by operations or the move out journey. New customers are exempt from this rule for the first 31 days. |
| `validateEmail` | `ValidateEmail` | `input: ValidateEmailInput!` | No | Validate user's email address. |
| `validateMfaDevice` | `ValidateMfaDevice` | `input: ValidateMfaDeviceInputType!` | No | Validate MFA Device for user. The possible errors that can be raised are: - KT-CT-1150: MFA device not found. - KT-CT-1151: MFA device not found. - KT-CT-1152: Invalid MFA token. - KT-CT-1155: Enabled backup device is needed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `validatePhone` | `ValidatePhone` | `input: ValidatePhoneNumberInput!` | No | Validate user's phone number. |
| `varyContractTerms` | `VaryContractTermsOutput!` | `input: VaryContractTermsInput!` | No | Vary the terms of a contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10011: Unable to vary contract terms. - KT-CT-10033: Unable to save term. - KT-CT-10012: Contract variation implies breach. - KT-CT-10034: Unknown contract journey type. - KT-CT-10035: Cannot process a non-active contract journey. - KT-CT-10036: The contract journey manager is not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `verifyCustomer` | `VerifyCustomer` | `input: VerifyCustomerInput!` | No | Verify a customer using the provided verification code and type. The possible errors that can be raised are: - KT-CT-4191: Error while verifying the customer. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `verifyEmail` | `VerifyEmail` | `input: VerifyEmailInput!` | No | Verify user's email address. The possible errors that can be raised are: - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |
| `verifyIdentity` | `VerifyIdentity` | `input: VerifyIdentityInput!` | No | Provide identifying information about an account and user to get a scoped token that will permit access to associate an email address with the account's user. The possible errors that can be raised are: - KT-CT-1145: Account/user details do not match. - KT-CT-1113: Disabled GraphQL field requested. |
| `withdrawDunning` | `WithdrawDunning` | `input: WithdrawDunningInputType!` | No | Withdraw a dunning process for an account The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11301: Account not in a dunning process for the given path name. - KT-CT-11302: No active dunning process found. - KT-CT-11303: Multiple active dunning processes found. - KT-CT-11306: Withdrawing the dunning process failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. |

## `NetworkOperator`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `String` |  | No | The network operator description. |
| `emergencyNumber` | `String` |  | No | The network operator emergency contact number. |

## `NextOperationsTeamRoundRobin`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `allInferredRoutingAttributes` | `[String]!` |  | No | All inferred routing attributes for team, location, and team groups (e.g., ['OPERATIONS_GROUP.TEAM.Team_A', 'OPERATIONS_GROUP.LOCATION.London', 'OPERATIONS_GROUP.GROUP_B']). Recommended for IVR usage. |
| `location` | `TeamLocation!` |  | No | Location routing information for the selected team. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `team` | `Team!` |  | No | The next operations team assigned in round-robin sequence. |
| `teamGroups` | `[TeamGroup]!` |  | No | All operations team groups that the selected team belongs to. |

## `NifCupsCorrelationValidation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `nifCupsCorrelate` | `Boolean` |  | No | Whether the given cups is correlated with the nif. |
| `validResponse` | `Boolean` |  | No | Whether the response is valid. |

## `NotifiableApplicationType`

Represents an application that can receive push notifications.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `bundleId` | `String!` |  | No | Bundle ID or package name of the app. |
| `description` | `String!` |  | No |  |
| `externalProjectId` | `String!` |  | No | Project ID used in push notification delivery service. (Currently: AWS Pinpoint) |
| `externalProvider` | `NotifiableApplicationExternalProvider!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `name` | `String!` |  | No | Human readable name for the app. |
| `pushNotificationBindings` | `[PushNotificationBindingType!]!` |  | No |  |
| `service` | `NotifiableApplicationService!` |  | No |  |

## `OCPPAuthentication`

Open Charge Point Protocol (OCPP) authentication. Take the given OCPP authentication details and trigger OCPP authentication. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4310: Unable to register OCPP authentication details. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `KrakenFlexDeviceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `OCPPConnectionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isConnected` | `Boolean` |  | No |  |

## `OCPPDetailsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `url` | `String` |  | No |  |
| `username` | `String` |  | No |  |

## `ObtainKrakenJSONWebToken`

The unifying approach used to get a Kraken token (JWT: JSON Web Token) with different types of input. The currently supported inputs are: - account user email/password combination - account user API key - organization live secret key - pre-signed key - refresh token The possible errors that can be raised are: - KT-CT-1135: Invalid data. - KT-CT-1134: Invalid data. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payload` | `GenericScalar!` |  | No | The body payload of the Kraken Token. The same information can be obtained by using JWT decoding tools on the value of the `token` field. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `refreshExpiresIn` | `Int` |  | No | A Unix timestamp representing the point in time at which the refresh token will expire. |
| `refreshToken` | `String` |  | No | A token that can be used in a subsequent call to `obtainKrakenToken` to get a new Kraken Token with the same access conditions after the previous one has expired. |
| `token` | `String!` |  | No | The Kraken Token. Can be used in the `Authorization` header for subsequent calls to the API to access protected resources. |

## `ObtainLongLivedRefreshToken`

Obtain a long-lived refresh token. This mutation is limited to authorized third-party organizations only. Account users can only generate short-lived refresh tokens. The short-lived refresh tokens (for account users) can be obtained from the 'refreshToken' field in 'obtainKrakenToken' mutation. The possible errors that can be raised are: - KT-CT-1120: The Kraken Token has expired. - KT-CT-1121: Please use Kraken Token to issue long-lived refresh tokens. - KT-CT-1132: Unauthorized. - KT-CT-1122: Long-lived refresh tokens can only be issued for account users. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `refreshExpiresIn` | `Int!` |  | No |  |
| `refreshToken` | `String` |  | No |  |

## `OccupancyPeriodType`

An occupancy period for a property.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | Account number associated with this occupancy period. |
| `effectiveFrom` | `DateTime` |  | No | Date the occupancy period is effective from. |
| `effectiveTo` | `DateTime` |  | No | Date the occupancy period is effective to. |
| `id` | `ID` |  | No | The unique ID of the occupancy period. |
| `isOccupier` | `Boolean` |  | No | Whether the account associated with the occupancy period is an occupier account type. |
| `numberOfOccupants` | `Int` |  | No | Number of occupants associated with this occupancy period. |

## `OccupyPropertyProcessConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[OccupyPropertyProcessConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `OccupyPropertyProcessConnectionTypeEdge`

A Relay edge containing a `OccupyPropertyProcessConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `OccupyPropertyProcessType` |  | No | The item at the end of the edge |

## `OccupyPropertyProcessType`

Represents a Occupy Property process.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | The ID or the primary key of the lifecycle process. |
| `occupyAt` | `DateTime!` |  | No |  |
| `status` | `LifecycleSupplyPointProcessStatus` |  | No | The status of the process. |
| `supplyPoints` | `SupplyPointConnectionTypeConnection!` | `before: String, after: String, first: Int, last: Int` | No | The supply points associated with the process. |

## `OfferGroupType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `createdAt` | `DateTime` |  | No | The date and time when Offer Group was created. |
| `createdBy` | `ActorType` |  | No | The Actor who created the Offer Group. |
| `identifier` | `ID` |  | No | Identifier of the Offer Group. |
| `offers` | `[OfferType]` |  | No | One or more Offers contained in the Offer Group. |

## `OfferType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptedAt` | `DateTime` |  | No | The date and time when Offer was accepted. |
| `createdBy` | `ActorType` |  | No | The Actor who created the Offer. |
| `description` | `String` |  | No | Description of the Offer. |
| `identifier` | `ID` |  | No | Identifier of the Offer. |
| `quote` | `QuoteType_` |  | No | The Quote this Offer is related to. |
| `rejectedAt` | `DateTime` |  | No | The date and time when Offer was rejected. |
| `validFrom` | `DateTime` |  | No | The date and time from which the Offer becomes valid. |
| `validTo` | `DateTime` |  | No | The date and time until which the Offer remains valid. |

## `OfferingComponentType`

Represents a nested offering component within an offering.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `component` | `OfferingType!` |  | No | The offering associated with this component. |
| `identifier` | `ID!` |  | No | Unique identifier of the component. |
| `initialQuantity` | `Int!` |  | No | Initial/default quantity for this component. |
| `maximumQuantity` | `Int!` |  | No | Maximum quantity of this component that can be selected. |
| `minimumQuantity` | `Int!` |  | No | Minimum quantity of this component that can be selected. |

## `OfferingType`

Represents a product offering in the catalog.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `customerDescription` | `String!` |  | No | Customer-facing description of the offering. |
| `customerName` | `String!` |  | No | Customer-facing name of the offering. |
| `groups` | `[GroupType]` |  | No | Groups of components with cardinality constraints. |
| `identifier` | `ID!` |  | No | Unique identifier of the offering. |
| `internalName` | `String!` |  | No | Internal name used to identify the offering. |
| `isActive` | `Boolean!` |  | No | Whether this offering is currently active. |
| `isAmendable` | `Boolean!` |  | No | Whether this offering can be amended (only DRAFT offerings). |
| `isDraft` | `Boolean!` |  | No | Whether this offering is in draft status. |
| `isExpired` | `Boolean!` |  | No | Whether this offering has expired. |
| `isFirstDraft` | `Boolean!` |  | No | Whether this is the first draft version (version 1, not yet activated). |
| `isLatestVersion` | `Boolean!` |  | No | Whether this is the latest version of the offering. |
| `isSellable` | `Boolean!` |  | No | Whether this offering can be sold stand-alone. |
| `lifecycle` | `LifecycleType!` |  | No | Lifecycle information for this offering. |
| `offeringComponents` | `[OfferingComponentType]` |  | No | Nested offering components included in this offering. |
| `productComponents` | `[ProductComponentType]` |  | No | Product components included in this offering. |
| `tags` | `[TagType]` |  | No | Tags associated with this offering. |
| `termTemplateComponents` | `[TermTemplateComponentType]` |  | No | Contract term template components included in this offering. |

## `OnSiteJobsAppointmentActionConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[OnSiteJobsAppointmentActionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `OnSiteJobsAppointmentActionConnectionTypeEdge`

A Relay edge containing a `OnSiteJobsAppointmentActionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `OnSiteJobsAppointmentActionType` |  | No | The item at the end of the edge |

## `OnSiteJobsAppointmentActionType`

An action linked to an On-Site Jobs Appointment.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `actionTriggerStage` | `OnSiteJobsAppointmentActionTriggerStage` |  | No | The appointment stage at which this action is triggered. |
| `workflowName` | `String` |  | No | The name of the workflow. |
| `workflowStatus` | `OnSiteJobsWorkflowStatus` |  | No | The current status of the workflow. |

## `OnSiteJobsAppointmentConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[OnSiteJobsAppointmentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `OnSiteJobsAppointmentConnectionTypeEdge`

A Relay edge containing a `OnSiteJobsAppointmentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `OnSiteJobsAppointmentType` |  | No | The item at the end of the edge |

## `OnSiteJobsAppointmentSlotResultsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isComplete` | `Boolean!` |  | No | Indicates whether all available appointment slots have been fetched. This is only relevant for booking adapters that support async timeslot fetching. For sync, it will always be True. If false, empty list of slots will be returned. |
| `slots` | `[OnSiteJobsAppointmentSlotType]!` |  | No | List of available appointment slots. |

## `OnSiteJobsAppointmentSlotType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `endDatetime` | `DateTime!` |  | No | The end datetime of the appointment slot. |
| `slotId` | `UUID!` |  | No | The unique identifier for this appointment slot. |
| `startDatetime` | `DateTime!` |  | No | The start datetime of the appointment slot. |

## `OnSiteJobsAppointmentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agent` | `OnSiteJobsAgent` |  | No | The agent assigned to the appointment. |
| `appointmentActions` | `OnSiteJobsAppointmentActionConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A list of actions triggered by this appointment, across stages. |
| `assets` | `OnSiteJobsAssetConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A list of assets attached to this request. |
| `cancellationCategory` | `OnSiteJobsCancellationCategory` |  | No | The cancellation category for this appointment. |
| `cancellationSubCategory` | `String!` |  | No |  |
| `comments` | `String!` |  | No |  |
| `commsStrategy` | `OnSiteJobsCommsStrategy` |  | No | The communication strategy for this appointment. |
| `createdAt` | `DateTime!` |  | No |  |
| `deadlineDate` | `Date` |  | No |  |
| `endAt` | `DateTime` |  | No |  |
| `externalJobType` | `String!` |  | Yes (The 'externalJobType' field is deprecated. Please use externalJobTypeMapping instead. - Marked as deprecated on 2026-03-17. - Scheduled for removal on or after 2026-04-17.) | Appointment job type. |
| `externalJobTypeMapping` | `OnSiteJobsExternalJobTypeMappingType` |  | No | Mapping of appointment job type value to its human-friendly label. |
| `externalReference` | `String!` |  | No |  |
| `id` | `UUID!` |  | No |  |
| `jobDetails` | `JSONString!` |  | No |  |
| `jobNotes` | `JSONString!` |  | No |  |
| `krakenWorkCategory` | `OnSiteJobsWorkCategory` |  | No | The work category for this appointment. |
| `preferredStartDate` | `Date` |  | No |  |
| `startAt` | `DateTime` |  | No |  |
| `status` | `OnSiteJobsAppointmentStatus` |  | No | The current status of the appointment. |

## `OnSiteJobsAssetConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[OnSiteJobsAssetConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `OnSiteJobsAssetConnectionTypeEdge`

A Relay edge containing a `OnSiteJobsAssetConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `OnSiteJobsAssetType` |  | No | The item at the end of the edge |

## `OnSiteJobsAssetType`

An On-Site Jobs Asset

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `additionalDetails` | `JSONString!` |  | No |  |
| `externalIdentifier` | `String!` |  | No |  |
| `fuelType` | `OnSiteJobsAssetFuelType` |  | No | The fuel type of the asset. |
| `kind` | `OnSiteJobsAssetKind!` |  | No | The kind of the asset. |
| `status` | `OnSiteJobsAssetStatus!` |  | No | The status of the asset. |
| `supplyPointIdentifier` | `String` |  | Yes (The 'supplyPointIdentifier' field is deprecated. Use 'supplyPointInternalIdentifier' instead. This field is being removed as the underlying model field is being removed. - Marked as deprecated on 2026-01-16. - Scheduled for removal on or after 2026-03-01.) | The internal identifier of the supply point associated with the asset. |
| `supplyPointInternalIdentifier` | `Int` |  | No |  |

## `OnSiteJobsCheckResultsType`

Check results for creating On-Site Jobs requests and appointments.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `appointmentCheckResults` | `[CheckResultType]` |  | No | Results of appointment checks. |
| `canCreateAppointment` | `Boolean` |  | No | Whether an appointment can be created (overall appointment check is PASS/WARNING). |
| `canCreateRequest` | `Boolean` |  | No | Whether a request can be created (overall request check is PASS/WARNING). |
| `hasAppointmentWarnings` | `Boolean` |  | No | Whether any of the appointment checks have warnings. |
| `hasRequestWarnings` | `Boolean` |  | No | Whether any of the request checks have warnings. |
| `requestCheckResults` | `[CheckResultType]` |  | No | Results of request checks. |

## `OnSiteJobsExternalJobTypeMappingType`

Mapping of a job type value to its human-friendly label.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `label` | `String` |  | No | The human-friendly name of the job type. |
| `value` | `String` |  | No | The job type value set on the appointment. |

## `OnSiteJobsJobTypeType`

Represents a job type available for on-site jobs requests.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `String!` |  | No | The unique identifier for the job type. |
| `name` | `String!` |  | No | The human-readable name of the job type. |

## `OnSiteJobsRequestActionConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[OnSiteJobsRequestActionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `OnSiteJobsRequestActionConnectionTypeEdge`

A Relay edge containing a `OnSiteJobsRequestActionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `OnSiteJobsRequestActionType` |  | No | The item at the end of the edge |

## `OnSiteJobsRequestActionType`

An action linked to an On Site Jobs Request.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `actionTriggerStage` | `OnSiteJobsRequestActionTriggerStage` |  | No | The request stage at which this action is triggered. |
| `workflowName` | `String` |  | No | The name of the workflow. |
| `workflowStatus` | `Status` |  | No | The current status of the workflow. |

## `OnSiteJobsRequestConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[OnSiteJobsRequestConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `OnSiteJobsRequestConnectionTypeEdge`

A Relay edge containing a `OnSiteJobsRequestConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `OnSiteJobsRequestType` |  | No | The item at the end of the edge |

## `OnSiteJobsRequestType`

An On Site Jobs Request

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `String` |  | No | Request account. |
| `agent` | `String!` |  | No |  |
| `appointments` | `OnSiteJobsAppointmentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A list of appointments associated to this request. |
| `assets` | `OnSiteJobsAssetConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A list of assets attached to this request. |
| `comment` | `String!` |  | No |  |
| `createdBy` | `Int` |  | No | The ID of the support user who created the request. |
| `externalReference` | `String!` |  | No |  |
| `id` | `UUID!` |  | No |  |
| `isEmergency` | `Boolean!` |  | No |  |
| `marketSupplyPoints` | `SupplyPointConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | List of supply points on request. |
| `overallActionsStatus` | `Status` |  | No | The overall priority status of all actions linked to the request and its appointments. |
| `property` | `PropertyType` |  | No | Request property. |
| `reason` | `String!` |  | No |  |
| `requestActions` | `OnSiteJobsRequestActionConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A list of actions attached directly to this request. |
| `status` | `OnSiteJobsRequestStatus` |  | No | Request status. |
| `subReason` | `String!` |  | No |  |

## `OnboardingReferralAllowedType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `referralValid` | `Boolean` |  | No | Determines whether, at this time, we think this referral will be valid. |

## `OperationsTeamType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | ID for the Operations Team. |
| `name` | `String` |  | No | Name for the Operations Team. |

## `OpportunitiesConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[OpportunitiesEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `OpportunitiesEdge`

A Relay edge containing a `Opportunities` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `OpportunityOutput` |  | No | The item at the end of the edge |

## `OpportunityAttachment`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `category` | `OpportunityAttachmentCategory` |  | No | Attachment category. |
| `filename` | `String` |  | No | Attachment filename. |
| `id` | `ID` |  | No | Attachment ID. |

## `OpportunityFileAttachment`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `expiresAt` | `DateTime` |  | No | The date and time the file attachment will expire. |
| `presignedUrl` | `String` |  | No | Presigned URL for the file attachment. |

## `OpportunityOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `assignedToAffiliateNumber` | `String` |  | No | The affiliate's name this opportunity is assigned to. |
| `assignedToTeam` | `String` |  | No | Team assigned to this opportunity. |
| `assignedToUser` | `String` |  | No | User assigned to this opportunity. |
| `attachments` | `[OpportunityAttachment]` |  | No | Attachments for the opportunity. |
| `consents` | `[ConsentOutput]` |  | No | List of consents for the opportunity. |
| `email` | `String` |  | No | Lead legal contact email. |
| `extraDetailItems` | `[ExtraDetail]` |  | No | Extra details about the opportunity as key/value pairs. |
| `extraDetails` | `JSONString` |  | Yes (The 'extraDetails' field is deprecated. Use `extraDetailsItems` instead, which provides a structured key/value format. - Marked as deprecated on 2026-01-14. - Scheduled for removal on or after 2026-07-14.) | Extra details about the opportunity. |
| `funnel` | `SalesFunnel` |  | No | The sales funnel this opportunity is in. |
| `leadNumber` | `String` |  | No | Lead number. |
| `leadType` | `String` |  | No | Lead type. |
| `name` | `String` |  | No | Lead legal name. |
| `notes` | `String` |  | No | Notes for the opportunity. |
| `number` | `String` |  | No | Opportunity number. |
| `offerGroupId` | `String` |  | No | Offer group ID. |
| `opportunityAddress` | `AddressOutput` |  | No | Opportunity address. |
| `opportunityId` | `ID` |  | Yes (The 'opportunityId' field is deprecated. Use `number` instead. - Marked as deprecated on 2025-12-16. - Scheduled for removal on or after 2026-02-16.) | Opportunity ID. |
| `opportunityRichAddress` | `RichAddressType` |  | No | Opportunity rich address. |
| `phoneNumber` | `String` |  | No | Lead legal contact phone number. |
| `productOffering` | `OfferingType` |  | No | The product offering of the opportunity. |
| `productOfferingId` | `String` |  | No | Product offering ID. |
| `salesChannel` | `String` |  | No | Sales channel. |
| `stage` | `String` |  | No | Current stage in a funnel. |
| `supplyPoints` | `[LeadSupplyPointType]` | `input: LeadSupplyPointFiltersInput` | No | List of supply points associated with the opportunity. |

## `OpportunityProductSummary`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `market` | `String` |  | No | The market for the Product. |
| `productCharacteristics` | `GenericScalar` |  | No | The characteristics of the product. |
| `productCode` | `String` |  | No | The code of the Product. |
| `productIdentifier` | `String` |  | No | The UUID for the Product. |
| `productOfferingIdentifier` | `String` |  | No | The UUID for the Product Offering. |

## `OutboundCallType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | If known, this is the account that a call is about. For inbound calls, we attempt to identify the account based on the phone number of the incoming call. For outbound calls, the account will be automatically set if the call was initiated from an account page. For all call types, the account can be updated, for example to correct a misidentification of an incoming call. |
| `id` | `ID!` |  | No | The ID of the call. |
| `metadata` | `[CallMetadataItemType]!` |  | No | Metadata related to the call, for example metrics or data passed via an interactive voice response (IVR). |

## `OutcomeType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `category` | `AppSessionOutcomeCategory` |  | No |  |
| `reason` | `String` |  | No |  |
| `type` | `AppSessionOutcomeType!` |  | No |  |

## `P0DetailsAcceptance`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accessRights` | `Decimal` |  | No | Access rights in kW. |
| `atrTariff` | `String` |  | No | ATR tariff code. |
| `cau` | `String` |  | No | Self-consumption administrative code (CAU). |
| `cieCode` | `String` |  | No | CIE certificate code. |
| `cieExpiryDate` | `Date` |  | No | CIE certificate expiry date. |
| `cieIssueDate` | `Date` |  | No | CIE certificate issue date. |
| `clientValidationResult` | `String` |  | No | Result of client validation (S/N). |
| `cnae` | `String` |  | No | CNAE economic activity code. |
| `contractTypeAtr` | `String` |  | No | ATR contract type code. |
| `contractedPowers` | `ContractedPower` |  | No | Contracted powers for all 6 periods. |
| `cupsType` | `String` |  | No | Type of CUPS. |
| `essentialIndicator` | `String` |  | No | Essential supply point indicator code. |
| `extensionRights` | `Decimal` |  | No | Extension rights in kW. |
| `hasWarrantyDeposit` | `Boolean` |  | No | Whether there is an associated warranty deposit. |
| `installationType` | `String` |  | No | Type of installation. |
| `installedGenerationPower` | `Decimal` |  | No | Installed generation power in kW. |
| `isActive` | `Boolean` |  | No | Whether the supply point is currently active. |
| `isCollective` | `Boolean` |  | No | Whether it's a collective self-consumption. |
| `isContractual` | `Boolean` |  | No | Whether the supply point can be contracted. |
| `isSocialBonus` | `Boolean` |  | No | Whether social bonus indicator is active. |
| `maxAuthorizedPower` | `Decimal` |  | No | Maximum authorized power in kW. |
| `meterPhaseCode` | `String` |  | No | Meter equipment phase code. |
| `nonContractualReason` | `String` |  | No | Reason code if supply point cannot be contracted. |
| `powerControlMode` | `String` |  | No | Power control mode code. |
| `remoteManagementType` | `String` |  | No | Type of remote management system. |
| `requestInProgressType` | `String` |  | No | Type of the request in progress. |
| `requestIsInProgress` | `Boolean` |  | No | Whether the request is in progress (S/N). |
| `selfConsumptionType` | `String` |  | No | Type of self-consumption configuration. |
| `subsectionType` | `String` |  | No | Subsection type for self-consumption. |

## `P0DetailsRejection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `comments` | `String` |  | No | Rejection comments. |
| `reasonCode` | `String` |  | No | Rejection reason code. |

## `PageInfo`

The Relay compliant `PageInfo` type, containing data necessary to paginate this connection.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `endCursor` | `String` |  | No | When paginating forwards, the cursor to continue. |
| `hasNextPage` | `Boolean!` |  | No | When paginating forwards, are there more items? |
| `hasPreviousPage` | `Boolean!` |  | No | When paginating backwards, are there more items? |
| `startCursor` | `String` |  | No | When paginating backwards, the cursor to continue. |

## `PauseCollectionProcess`

Manually pause a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11214: Invalid pause length for collection process. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessPaused` | `PauseCollectionProcessOutput` |  | No | Collection process pause output. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `PauseCollectionProcessOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `pauseRecords` | `[CollectionProcessPauseStatusRecord]` |  | No | Pause records on the collection process. |

## `PauseDunning`

Pause the dunning process for an account. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11301: Account not in a dunning process for the given path name. - KT-CT-11302: No active dunning process found. - KT-CT-11303: Multiple active dunning processes found. - KT-CT-11304: Dunning pause process failed verifying the dates. - KT-CT-11305: Pausing the dunning process failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `pauseCreated` | `Boolean` |  | No | Whether the pause has been successfully created. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `Payment`

A payment from the customer to the supplier.

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
| `isLateFailedPayment` | `Boolean!` |  | No | Whether a payment has been reversed due to a late failure.Sometimes a payment is marked cleared, only for Kraken to be notified days/weeks later that the payment has failed. |
| `isReversed` | `Boolean!` |  | No |  |
| `note` | `String` |  | No | Returns the note field value for the transaction, which contains additional info. |
| `paymentTransactionType` | `AccountPaymentTransactionTypeChoices` |  | No | The transaction type of the payment. |
| `postedDate` | `Date` |  | No | Date when the transaction was posted to the account. |
| `reasonCode` | `String` |  | No | Returns the reason. |
| `statementId` | `ID` |  | Yes (The 'statementId' field is deprecated. Use `billingDocumentIdentifier` instead. - Marked as deprecated on 2023-11-30. - Scheduled for removal on or after 2024-06-01.) | Returns None if a statement is not linked with the transaction. |
| `title` | `String` |  | No | Human-readable title describing the transaction. |

## `PaymentAdequacyDetailsType`

Payment adequacy adjusts fixed payment schedules to maintain a healthy ledger balance over a year.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isCurrentlyExempt` | `Boolean` |  | No | This ledger will be exempt from default Payment Adequacy. This may mean that it is completely exempt, or handled with special rules. |

## `PaymentFingerPrintCheckType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fingerprint` | `String` |  | No | Fingerprint. |
| `isFound` | `Boolean` |  | No | Returns True if the fingerprint exists, False otherwise. |
| `isRiskListed` | `Boolean` |  | No | Returns True if the fingerprint is risk-listed, False otherwise. |

## `PaymentForecastConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PaymentForecastConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PaymentForecastConnectionTypeEdge`

A Relay edge containing a `PaymentForecastConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PaymentForecastType` |  | No | The item at the end of the edge |

## `PaymentForecastType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int` |  | No |  |
| `date` | `Date` |  | No |  |
| `method` | `ScheduleType` |  | No | The payment method used for the forecasted payment. |
| `paymentNumber` | `Int` |  | No |  |

## `PaymentInstructionConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PaymentInstructionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PaymentInstructionConnectionTypeEdge`

A Relay edge containing a `PaymentInstructionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PaymentInstructionType` |  | No | The item at the end of the edge |

## `PaymentInstructionOwnerType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountUser` | `EspAccountUserType` |  | No | The account user who is an owner of this payment instruction. |
| `business` | `BusinessType` |  | No | The business who is an owner of this payment instruction. |

## `PaymentInstructionType`

Payment Instructions

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountHolder` | `String!` |  | No |  |
| `accountType` | `String` |  | No |  |
| `bankCode` | `String` |  | No |  |
| `cardExpiryMonth` | `Int` |  | No |  |
| `cardExpiryYear` | `Int` |  | No |  |
| `cardNumber` | `String!` |  | No |  |
| `cardPaymentNetwork` | `String` |  | No |  |
| `cardType` | `String` |  | No |  |
| `iban` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `instructionType` | `String!` |  | No |  |
| `maskedAccountIdentifier` | `String` |  | No | A masked reference to a recurring payment method. |
| `owners` | `[PaymentInstructionOwnerType]` |  | No | The owners of the financial account this instruction represents. |
| `sortCode` | `String!` |  | No |  |
| `status` | `String!` |  | No |  |
| `supplementaryLedger` | `SupplementaryLedgerType` |  | No | The supplementary ledger for this payment instruction. |
| `validFrom` | `DateTime!` |  | No |  |
| `vendor` | `String!` |  | No |  |

## `PaymentPlanConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PaymentPlanConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PaymentPlanConnectionTypeEdge`

A Relay edge containing a `PaymentPlanConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PaymentPlanType` |  | No | The item at the end of the edge |

## `PaymentPlanPaymentType`

An object that represents a planned payment for a payment plan.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int!` |  | No |  |
| `payableDate` | `Date!` |  | No |  |
| `paymentType` | `String` |  | No |  |

## `PaymentPlanType`

An object that represents a payment plan.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `acceptedAt` | `DateTime` |  | No |  |
| `account` | `Account!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `initialScheduleType` | `String!` |  | No |  |
| `ledgerNumber` | `String` |  | No | The ledger number for this payment plan or None if one does not exist. |
| `nextPayment` | `PaymentPlanPaymentType` |  | No | The next planned payment for this payment plan. |
| `offerExpiresAt` | `DateTime` |  | No |  |
| `offeredAt` | `DateTime` |  | No |  |
| `payments` | `[PaymentPlanPaymentType!]!` |  | No |  |
| `status` | `String!` |  | No |  |
| `strategyDisplayName` | `String` |  | No | The display name of the strategy used for this payment plan or None if one does not exist. |
| `strategyName` | `String!` |  | No |  |
| `updatedAt` | `DateTime!` |  | No |  |

## `PaymentPreferenceConnectionTypeConnection`

Pagination object for PaymentPreferenceUnion

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PaymentPreferenceConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PaymentPreferenceConnectionTypeEdge`

A Relay edge containing a `PaymentPreferenceConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PaymentPreferenceUnion` |  | No | The item at the end of the edge |

## `PaymentRequestConnectionTypeConnection`

This field is a connection type. Connections are used to implement [cursor based pagination](https://graphql.org/learn/pagination/#pagination-and-edges).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PaymentRequestConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PaymentRequestConnectionTypeEdge`

A Relay edge containing a `PaymentRequestConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PaymentRequestType` |  | No | The item at the end of the edge |

## `PaymentRequestType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `customerAmount` | `Int` |  | No | The amount the customer is expected to pay in minor currency. |
| `expectedPaymentDate` | `Date` |  | No | The date the payment is expected to be made. |
| `fundingSourceAmounts` | `FundingSourceAmountConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The amount that was funded by each funding source. |
| `paymentStatus` | `String` |  | No | The status of the payment. |
| `totalAmount` | `Int` |  | No | The total amount of the payment in minor currency. |

## `PaymentRequestsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `paymentRequest` | `PaymentRequestConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | A list of payment requests for a given ledger. |

## `PaymentScheduleConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PaymentScheduleConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PaymentScheduleConnectionTypeEdge`

A Relay edge containing a `PaymentScheduleConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PaymentScheduleType` |  | No | The item at the end of the edge |

## `PaymentScheduleDelayConfigurationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `args` | `JSONString` |  | No | The arguments of the delay configuration. |
| `code` | `String` |  | No | The code of the delay configuration. |

## `PaymentSchedulePaymentDayDetailsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `String` |  | No | A human-readable description of the value. |
| `direction` | `PaymentDayDirectionType` |  | No | Direction of payment day. |

## `PaymentScheduleType`

An object that represents when we have agreed to take payments from a payment instruction.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `delayConfiguration` | `PaymentScheduleDelayConfigurationType` |  | No | The delay configuration for this payment schedule. |
| `id` | `ID!` |  | No |  |
| `isExemptFromPaymentAdequacy` | `Boolean` |  | No | If the payment schedule is exempt from payment adequacy. |
| `isPaymentHoliday` | `Boolean` |  | No |  |
| `isVariablePaymentAmount` | `Boolean!` |  | No |  |
| `ledgerNumber` | `String` |  | No | The ledger number of the payment schedule. |
| `paymentAdequacyAdjustment` | `Int` |  | No |  |
| `paymentAdequacyAdjustmentExpiryDate` | `Date` |  | No |  |
| `paymentAmount` | `Int!` |  | No |  |
| `paymentDay` | `Int` |  | No |  |
| `paymentDayDetails` | `PaymentSchedulePaymentDayDetailsType` |  | No | Details of the payment_day value. |
| `paymentFrequency` | `PaymentFrequencyOptions` |  | No | The frequency of the payment schedule. |
| `paymentFrequencyMultiplier` | `Int!` |  | No |  |
| `paymentHolidayReason` | `String!` |  | No |  |
| `reason` | `PaymentScheduleReasonOptions` |  | No | The reason the payment schedule was created. |
| `scheduleType` | `ScheduleType` |  | Yes (The 'scheduleType' field is deprecated. Use paymentPreferences query instead. - Marked as deprecated on 2025-07-07. - Scheduled for removal on or after 2026-07-07.) | The method of payment for the schedule. |
| `supplementaryLedger` | `SupplementaryLedgerType` |  | No | The supplementary ledger for this payment schedule, if it is on one. |
| `totalDebtAmount` | `Int` |  | No | The sum of the payment adequacy contributions on the payment schedule that are expected to be taken before the debt repayment is complete. |
| `trigger` | `ScheduleTrigger` |  | No | The cause for requesting payment on a schedule. |
| `validFrom` | `Date!` |  | No |  |
| `validTo` | `Date` |  | No |  |

## `PaymentWithNonConcludedRePresentationConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PaymentWithNonConcludedRePresentationConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PaymentWithNonConcludedRePresentationConnectionTypeEdge`

A Relay edge containing a `PaymentWithNonConcludedRePresentationConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PaymentWithNonConcludedRePresentationType` |  | No | The item at the end of the edge |

## `PaymentWithNonConcludedRePresentationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amountPayable` | `Int` |  | No | The amount expected for this payment in minor currency units. |
| `payableDate` | `Date` |  | No | The date this payment is scheduled to be debited. |

## `PayoutReferralForAccount`

The possible errors that can be raised are: - KT-CT-6712: Invalid reference. - KT-CT-6723: Unauthorized. - KT-CT-6730: Referral cannot be paid out. - KT-CT-6731: The account is unrelated to the referral. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `payoutResult` | `PayoutReferralForAccountResultType` |  | No | The result of the payout. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `PayoutReferralForAccountResultType`

The result of the payout of a referral for an account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountCreditAmount` | `Int` |  | No | The amount of the account credit paid out to the referring account. |

## `PaysByDirectDebitType`

Represents a restriction for if an account should pay only by direct debit in a contract. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `paysByDirectDebit` | `Boolean!` |  | No | Whether the account is paying by direct debit or not. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `PerformBoostCharge`

Initiate a boost charge for an electric vehicle (EV). This will start charging the EV and will not stop until the battery reaches 100% charged. If it is not possible to initiate a boost charge, a KT-CT-4357 error will be returned. It may have a `boostChargeRefusalReasons` extension which lists the reasons why the boost charge was refused. Possible reasons include: - `BC_DEVICE_NOT_YET_LIVE` (device is not yet live) - `BC_DEVICE_RETIRED` (device is retired) - `BC_DEVICE_SUSPENDED` (device is suspended) - `BC_DEVICE_DISCONNECTED` (device is disconnected) - `BC_DEVICE_NOT_AT_HOME` (device is not at home) - `BC_BOOST_CHARGE_IN_PROGRESS` (boost charge already in progress) - `BC_DEVICE_FULLY_CHARGED` (device is already fully charged) The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4356: A boost charge cannot currently be performed. - KT-CT-4357: Unable to trigger boost charge. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `KrakenFlexDeviceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `PerformTestCharge`

Initiate a test charge of an electric vehicle (EV). This is to ensure that the EV or EVSE (charge point) can be controlled remotely and successfully charged for a short period. If it is not possible to initiate a test charge, a KT-CT-4355 error will be returned. It may have a `testChargeRefusalReasons` extension which lists the reasons why the test charge was refused. Possible reasons include: - `TC_DEVICE_LIVE` (device is already live) - `TC_DEVICE_ONBOARDING_IN_PROGRESS` (test dispatch already in progress) - `TC_DEVICE_RETIRED` (device is retired) - `TC_DEVICE_SUSPENDED` (device is suspended) - `TC_DEVICE_DISCONNECTED` (device is disconnected) - `TC_DEVICE_ALREADY_CHARGING` (device is already charging) - `TC_DEVICE_AWAY_FROM_HOME` (device is away from home) - `TC_DEVICE_NO_LOCATION_CONFIGURED` (device has no location configured) - `TC_DEVICE_LOCATION_UNABLE_TO_IDENTIFY` (unable to identify device location) - `TC_DEVICE_LOCATION_MISSING` (device location is missing) The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4362: Device not ready for test charge. - KT-CT-4355: Unable to trigger charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `KrakenFlexDeviceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `Period`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `end` | `DateTime!` |  | No | The period end. |
| `start` | `DateTime!` |  | No | The period start. |

## `PeriodBasedDocumentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `BillingAttachmentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No |  |
| `billType` | `BillTypeEnum` |  | No | The type of the bill. |
| `closingBalance` | `Int!` | `ledgerNumber: String = null` | No | The closing balance of an issued billing document. |
| `documentDebtPosition` | `BillingDocumentPositionType` |  | No | Position of the billing document in the delinquent debt tracking system. |
| `fromDate` | `Date` |  | No | The date of the constituent bill covered from. |
| `id` | `ID` |  | No | The ID of the constituent bill. |
| `identifier` | `ID` |  | No | The unique identifier for the billing document. Note: a pending billing document will not have an identifier yet; and not all finalized billing documents will have an identifier assigned to them, in which case this will be null. |
| `isAnnulled` | `Boolean!` |  | No | Whether the billing document has been annulled. |
| `issuedDate` | `Date` |  | No | The date the bill was sent to the customer. |
| `openingBalance` | `Int` | `ledgerNumber: String = null` | No | This field returns the opening balance of a statement. |
| `printedCopyRequests` | `[Date]` |  | No | List of dates when a printed copy of this bill was requested. |
| `representations` | `BillRepresentationConnectionTypeConnection` | `code: String = null, before: String, after: String, first: Int, last: Int` | No |  |
| `reversalsAfterClose` | `StatementReversalsAfterClose!` |  | No | How many charges have been reversed after the close date. |
| `temporaryUrl` | `String` |  | Yes (The 'temporaryUrl' field is deprecated. This field is deprecated. Use the 'attachments' field instead. - Marked as deprecated on 2024-09-16. - Scheduled for removal on or after 2025-09-01.) | Requesting this field generates a temporary URL at which bill is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). This field can raise an error with errorClass NOT_FOUND if the bill document has not been created/issued yet. This field is deprecated use 'attachments' field instead. |
| `toDate` | `Date` |  | No | The date of the constituent bill covered to. |
| `totalCharges` | `StatementTotalType` |  | No | The total amounts for all charges on the billing document. |
| `totalCredits` | `StatementTotalType` |  | No | The total amounts for all credits on the statement. |
| `transactions` | `BillTransactionConnectionTypeConnection` | `ledgerNumber: String = null, transactionTypes: [TransactionTypeFilter] = [], orderBy: TransactionsOrderBy = POSTED_DATE_DESC, before: String, after: String, first: Int, last: Int` | No | Transactions on the given billing document. |

## `PersonalInformation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `firstFamilyName` | `String` |  | No | The first family name for a user. |
| `givenName` | `String` |  | No | The given name for a user. |
| `mobile` | `String` |  | No | The mobile for a user. |
| `nif` | `String` |  | No | The nif for a user. |
| `secondFamilyName` | `String` |  | No | The first family name for a user. |

## `PhoneNumberIdentificationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountAllMatches` | `AccountConnectionTypeConnection!` | `before: String, after: String, first: Int, last: Int` | No | All accounts that are linked to this phone number. A maximum of 26 results are returned. Results are ordered by most likely first. |
| `accountBestMatch` | `Account` |  | No | Our best guess for which account a call with this phone number would be about. |
| `accountUserAllMatches` | `AccountUserConnectionTypeConnection!` | `before: String, after: String, first: Int, last: Int` | No | All account users that are linked to this phone number. A maximum of 26 results are returned. Results are ordered by most likely first. |
| `accountUserBestMatch` | `EspAccountUserType` |  | No | Our best guess for which account user would be calling from this phone number. |

## `PillButtonType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `buttonAction` | `ActionType!` |  | No | The action to perform when the button is pressed. |
| `buttonStyle` | `ButtonStyle` |  | No | The button style. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `title` | `String!` |  | No | Title text of the button. |
| `typename` | `String` |  | No | The name of the object's type. |

## `PointsAllowanceRateLimitInformation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isBlocked` | `Boolean` |  | No | Whether the viewer has been blocked due to spending all its allowed points. |
| `limit` | `Int` |  | No | The maximum number of points the viewer gets for requests per hour. |
| `remainingPoints` | `Int` |  | No | The remaining points for the viewer in one hour time limit. |
| `ttl` | `Int` |  | No | Time To Live: UNIX timestamp when the viewer will get a new allowance of points. |
| `usedPoints` | `Int` |  | No | The points used so far in one hour time limit. |

## `PointsSizeType`

A measurement in points.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | Unique identifier of the object. |
| `points` | `Int!` |  | No | The points value. |
| `typename` | `String` |  | No | The name of the object's type. |

## `PortfolioConnectionTypeConnection`

Paginator of Operations Team

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PortfolioConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PortfolioConnectionTypeEdge`

A Relay edge containing a `PortfolioConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PortfolioType` |  | No | The item at the end of the edge |

## `PortfolioType`

An object that represents a portfolio.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accounts` | `AccountConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The accounts associated with this portfolio. |
| `ancestors` | `PortfolioConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The ancestors of the given portfolio. |
| `billingName` | `String` |  | No |  |
| `brand` | `String` |  | No | The brand code associated with the portfolio. |
| `collectiveBilling` | `Boolean!` |  | No |  |
| `createdAt` | `DateTime!` |  | No |  |
| `depth` | `Int` |  | No | The depth of the portfolio in the hierarchy. |
| `descendants` | `PortfolioConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The descendants of the given portfolio. |
| `id` | `ID!` |  | No |  |
| `leadAccountNumber` | `String` |  | No | The lead account for this portfolio. |
| `name` | `String` |  | No | The name of the portfolio. |
| `number` | `String!` |  | No |  |
| `operationsTeam` | `OperationsTeamType` |  | No | Operations team for this portfolio. |
| `parent` | `PortfolioType` |  | No | The parent portfolio of the given portfolio, if any. |
| `updatedAt` | `DateTime!` |  | No |  |

## `PortfolioUserRoleType`

The role a user has in association with one portfolio.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No |  |
| `portfolio` | `PortfolioType!` |  | No | Portfolio object. |
| `role` | `RoleString` |  | No | The portfolio role. |
| `user` | `EspAccountUserType!` |  | No |  |

## `PossibleErrorType`

The GraphQL error type for displaying information about GraphQL errors that might be raised from the API.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The error code that might be returned from the query/mutation. |
| `description` | `String` |  | No | The error description that might be returned from the query/mutation. |
| `message` | `String` |  | No | The error message that might be returned from the query/mutation. |
| `type` | `String` |  | No | The error type that might be returned from the query/mutation. |

## `PossibleErrorsOutputType`

Information and possible errors of the requested query/mutation.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `authErrors` | `Boolean` |  | No | Whether the possible authentication errors are included. |
| `name` | `String` |  | No | Name of the query/mutation whose possible errors are returned. |
| `possibleErrors` | `[PossibleErrorType]` |  | No | List of the errors the query/mutation is susceptible of raising. |
| `type` | `query_type` |  | No | Type of the query (query or mutation). |

## `PostCredit`

The possible errors that can be raised are: - KT-CT-5316: Invalid data. - KT-CT-5311: The credit reason with the requested code is deprecated. - KT-CT-5312: The credit reason with the requested code does not exist. - KT-CT-5313: An error occurred whilst posting the credit. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `credit` | `Credit` |  | No | Posted account credit. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `PowerAndEnergyPrices`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `adjustmentMechanism` | `AdjustmentMechanism` |  | No | Adjustment mechanism. |
| `dailyFee` | `Float` |  | No | Daily fee for indexed tariffs. |
| `dailyFeeWithTaxes` | `Float` |  | No | Daily fee with taxes. |
| `energy` | `[Float]` |  | Yes (The 'energy' field is deprecated. Change to a more descriptive field name. Use 'variable_term' instead. - Marked as deprecated on 2024-08-02. - Scheduled for removal on or after 2024-12-01.) | The energy prices. |
| `energyUnits` | `String` |  | Yes (The 'energyUnits' field is deprecated. Change to a more descriptive field name. Use 'variable_term_with_taxes' instead. - Marked as deprecated on 2024-08-02. - Scheduled for removal on or after 2024-12-01.) | Units of energy measurement. |
| `fixedTerm` | `[Float]` |  | No | Fixed term. |
| `fixedTermUnits` | `String` |  | No | Units of fixed term. Same for all terms. |
| `fixedTermWithTaxes` | `[Float]` |  | No | Fixed term with taxes. |
| `marginTerm` | `Float` |  | No | Margin term quantity. |
| `marginTermUnits` | `String` |  | No | Units of margin term. |
| `marginTermWithTaxes` | `Float` |  | No | Margin term with taxes. |
| `power` | `[Float]` |  | Yes (The 'power' field is deprecated. Change to a more descriptive field name. Use 'fixed_term' instead. - Marked as deprecated on 2024-08-02. - Scheduled for removal on or after 2024-12-01.) | The power prices. |
| `powerUnits` | `String` |  | Yes (The 'powerUnits' field is deprecated. Change to a more descriptive field name. Use 'fixed_term_with_taxes' instead. - Marked as deprecated on 2024-08-02. - Scheduled for removal on or after 2024-12-01.) | Units of power measurement. |
| `surplusRate` | `Float` |  | No | Rate at which solar surplus is compensated. |
| `surplusRateUnits` | `String` |  | No | Units of the surplus rate. |
| `variableTerm` | `[Float]` |  | No | Variable term. |
| `variableTermUnits` | `String` |  | No | Units of variable term. Same for all terms. |
| `variableTermWithTaxes` | `[Float]` |  | No | Variable term with taxes. |

## `PreKrakenBillType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `BillingAttachmentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No |  |
| `billType` | `BillTypeEnum` |  | No | The type of the bill. |
| `fromDate` | `Date` |  | No | The date of the bill is covered from. |
| `grossAmount` | `BigInt` |  | No | The gross amount of the historical bill. |
| `id` | `ID` |  | No | The ID of the bill. |
| `identifier` | `String` |  | No | The unique identifier of a historical bill. It will usually be present on the billing document itself. |
| `issuedDate` | `Date` |  | No | The date the bill was sent to the customer. |
| `params` | `JSONString` |  | No | The params associated with the historical bill. |
| `reversalsAfterClose` | `StatementReversalsAfterClose!` |  | No | How many charges have been reversed after the close date. |
| `temporaryUrl` | `String` |  | Yes (The 'temporaryUrl' field is deprecated. This field is deprecated. Use the 'attachments' field instead. - Marked as deprecated on 2024-09-16. - Scheduled for removal on or after 2025-09-01.) | Requesting this field generates a temporary URL at which bill is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). This field can raise an error with errorClass NOT_FOUND if the bill document has not been created/issued yet. This field is deprecated use 'attachments' field instead. |
| `toDate` | `Date` |  | No | The date of the bill is covered to. |

## `PreSignedToken`

A pre-signed, expiring and opaque tokens that can be swapped for a limited scope JWT (Kraken Token).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isValid` | `Boolean` |  | No |  |
| `key` | `String!` |  | No |  |
| `scope` | `ExpiringTokenScope!` |  | No | The scope that the token will grant to the account user. |

## `PreferredInstruction`

Represents the preference of the user to be charged using a specific payment instruction.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `forPaymentsAfter` | `String` |  | No | The start time of the payment preference. |
| `paymentMethod` | `PaymentInstructionType` |  | No | The payment instruction preferred by the user. |
| `status` | `String` |  | No | The status of the payment preference. |

## `PrepareAccountResult`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | The account number of the newly created account or the existing account to be re-used. |
| `isNewAccount` | `Boolean` |  | No | Was a new account created. |
| `isNewUser` | `Boolean` |  | No | Was a new user created. |
| `userId` | `ID` |  | No | The ID of the newly created or existing account user. |
| `userNumber` | `String` |  | No | The user number of the newly created or existing account user. |

## `PriceForStream`

Rate group prices for a product.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `characteristicMapping` | `JSONString!` |  | No | The characteristic mapping for the price. |
| `price` | `Decimal!` |  | No | The price per unit. |
| `schemeLabels` | `JSONString` |  | No | The scheme labels for the price. |

## `PricePerUnit`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Decimal!` |  | No | Monetary value of a single unit of the measurement. This is the smallest unit of currency e.g. cents for USD or yen for JPY. |
| `unit` | `Unit` |  | No | Unit that monetary amount relates to eg. 27 cents per kwh. |

## `PrintAttachmentType`

Represents a print attachment

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `filename` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `s3Bucket` | `String!` |  | No |  |
| `s3Key` | `String!` |  | No |  |
| `temporaryUrl` | `String` |  | No | Temporary URL at which the attachment is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). |

## `PrintBatchType`

Represents print batch details

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No |  |
| `messages` | `PrintMessageTypeConnection` | `isHighPriority: Boolean = null, offset: Int, before: String, after: String, first: Int, last: Int` | No | Messages in a print batch. |
| `status` | `PrintBatchStatus` |  | No | The status of the print batch. |

## `PrintEventType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `eventType` | `String!` |  | No |  |
| `id` | `ID!` |  | No | The ID of the object |
| `message` | `PrintMessageType` |  | No | Print message of the print event. |
| `occurredAt` | `DateTime!` |  | No |  |

## `PrintMessageType`

Represents a print communication.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No |  |
| `attachments` | `[PrintAttachmentType]` |  | No | Attachments of the message. |
| `highPriority` | `Boolean` |  | No | Comms that are marked as high priority. |
| `id` | `ID!` |  | No | The ID of the object |
| `templateCode` | `String!` |  | No |  |

## `PrintMessageTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PrintMessageTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PrintMessageTypeEdge`

A Relay edge containing a `PrintMessageType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PrintMessageType` |  | No | The item at the end of the edge |

## `Product`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `atr` | `String` |  | No | The ATR of the product. |
| `availabilityStatus` | `ProductAvailabilityStatus!` |  | No |  |
| `availableFrom` | `DateTime!` |  | No |  |
| `availableTo` | `DateTime` |  | No |  |
| `brand` | `Brand` |  | No | Brand details. |
| `code` | `String!` |  | No |  |
| `description` | `String!` |  | No | This will be shown to customers during sign-up |
| `displayName` | `String!` |  | No | This name will be shown to customers during sign-up |
| `endsAt` | `DateTime` |  | No | This is when end-dated products expire |
| `fullName` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `isHidden` | `Boolean!` |  | No | Use this field to temporarily make a product unavailable |
| `marketName` | `String!` |  | No |  |
| `notes` | `String!` |  | No | These are internal notes to explain why this product exists |
| `params` | `JSONString!` |  | No |  |
| `prices` | `PowerAndEnergyPrices` | `powerDecimalPlaces: Int` | No | Active power and energy prices for this product. |
| `term` | `Int` |  | No | Duration of agreements using this product in months |
| `termsContractType` | `String!` |  | No |  |

## `ProductComponentType`

Represents a product component within an offering.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `component` | `CatalogProductType!` |  | No | The product associated with this component. |
| `identifier` | `ID!` |  | No | Unique identifier of the component. |
| `initialQuantity` | `Int!` |  | No | Initial/default quantity for this component. |
| `maximumQuantity` | `Int!` |  | No | Maximum quantity of this component that can be selected. |
| `minimumQuantity` | `Int!` |  | No | Minimum quantity of this component that can be selected. |

## `ProductParams`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fixedType` | `String` |  | No | How many periods the price is fixed for. |
| `isDefaultGasTariff` | `Boolean` |  | No | Determines whether this is the default gas tariff. |
| `mostPopular` | `Boolean` |  | No | Determines whether this is the most popular product. |
| `productType` | `String` |  | No | Product type. |

## `ProductPrices`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `adjustmentMechanism` | `AdjustmentMechanism` |  | No | Adjustment mechanism. |
| `dailyFee` | `Float` |  | No | Daily fee for indexed tariffs. |
| `dailyFeeWithTaxes` | `Float` |  | No | Daily fee with taxes. |
| `fixedTerm` | `[Float]` |  | No | Fixed term. |
| `fixedTermUnits` | `String` |  | No | Units of fixed term. Same for all terms. |
| `fixedTermWithTaxes` | `[Float]` |  | No | Fixed term with taxes. |
| `marginTerm` | `Float` |  | No | Margin term quantity. |
| `marginTermUnits` | `String` |  | No | Units of margin term. |
| `marginTermWithTaxes` | `Float` |  | No | Margin term with taxes. |
| `surplusRate` | `Float` |  | No | Rate at which solar surplus is compensated. |
| `surplusRateUnits` | `String` |  | No | Units of the surplus rate. |
| `variableTerm` | `[Float]` |  | No | Variable term. |
| `variableTermUnits` | `String` |  | No | Units of variable term. Same for all terms. |
| `variableTermWithTaxes` | `[Float]` |  | No | Variable term with taxes. |

## `ProductPricesWithExcess`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `adjustmentMechanism` | `AdjustmentMechanism` |  | No | Adjustment mechanism. |
| `excessPrice` | `ExcessPrice` |  | No | Adjustment mechanism. |
| `fixedTerm` | `[Float]` |  | No | Fixed term. |
| `fixedTermUnits` | `String` |  | No | Units of fixed term. Same for all terms. |
| `fixedTermWithTaxes` | `[Float]` |  | No | Fixed term with taxes. |
| `marginTerm` | `Float` |  | No | Margin term quantity. |
| `marginTermUnits` | `String` |  | No | Units of margin term. |
| `marginTermWithTaxes` | `Float` |  | No | Margin term with taxes. |
| `variableTerm` | `[Float]` |  | No | Variable term. |
| `variableTermUnits` | `String` |  | No | Units of variable term. Same for all terms. |
| `variableTermWithTaxes` | `[Float]` |  | No | Variable term with taxes. |

## `ProductRateOverrideConfigurationType`

Configuration for Product Rate Override Configuration term.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `indexationOptions` | `IndexationOptionsType` |  | No | The indexation options for the product rate override configuration. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `schedules` | `[ProductRateOverrideScheduleType]` |  | No | The schedules for the product rate override configuration. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `ProductRateOverrideItemType`

Item for Product Rate Override Configuration term.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `pricePerUnit` | `Decimal` |  | No | The price per unit for the product rate override item. |
| `productCode` | `String` |  | No | The product code for the product rate override item. |
| `rateBand` | `String` |  | No | The rate band for the product rate override item. |

## `ProductRateOverrideScheduleType`

Schedule for Product Rate Override Configuration term.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `effectiveFrom` | `DateTime` |  | No | The effective from date for the product rate override schedule. |
| `items` | `[ProductRateOverrideItemType]` |  | No | The items for the product rate override schedule. |

## `ProductWithEstimates`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dualFuel` | `[DualFuelProductQuote]` |  | No | Dual fuel quoting. |
| `singleFuel` | `[SingleFuelProductQuote]` |  | No | Electricity market quoting. |

## `ProductWithoutEstimates`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `availableFrom` | `DateTime` |  | No | The available from datetime in industry time. |
| `availableTo` | `DateTime` |  | No | The available to datetime in industry time. |
| `brand` | `Brand` |  | No | Brand details. |
| `code` | `String!` |  | No |  |
| `currentAgreementCount` | `Int` |  | No | Amount of active agreements with this product. |
| `description` | `String!` |  | No | This will be shown to customers during sign-up |
| `displayName` | `String!` |  | No | This name will be shown to customers during sign-up |
| `dualFuelDescription` | `String` |  | No | Product details dual fuel description. |
| `fullName` | `String!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `isHidden` | `Boolean!` |  | No | Use this field to temporarily make a product unavailable |
| `marketName` | `String!` |  | No |  |
| `notes` | `String!` |  | No | These are internal notes to explain why this product exists |
| `params` | `ProductParams` |  | No | Kraken product params. |
| `prices` | `ProductPrices` |  | No | List of market prices. |
| `term` | `Int` |  | No | Duration of agreements using this product in months |

## `PromotionAssignmentScheduleType`

Represents a schedule for promotion assignment within a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `discountTargets` | `JSONString` |  | No | A mapping from discount codes to lists of targets. Each target is represented as {'target_type': {'domain': ..., 'type': ...}, 'identifier': ...}. |
| `promotionCode` | `String` |  | No | The promotion code for this schedule. |

## `PromotionAssignmentTermType`

Represents a promotion assignment term in a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `schedules` | `[PromotionAssignmentScheduleType]` |  | No | A list of promotion assignment schedules associated with the contract. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `PropertyConnection`

Paginated list of properties.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[PropertyEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `PropertyEdge`

A Relay edge containing a `Property` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `PropertyInterface` |  | No | The item at the end of the edge |

## `PropertyRichAddressType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `administrativeArea` | `String` |  | No | Top-level administrative subdivision, e.g. US state, AU state/territory, NZ, region, IT region, JP prefecture. ### `AU`: Australia This must be one of `NSW`, `VIC`, `QLD`, `TAS`, `ACT`, `SA`, `NT`, `WA`. For addresses not within these locations, use the value that Australia Post uses, e.g. `ACT` for the Jervis Bay Territory or `WA` for Christmas Island. |
| `asString` | `String` | `showCountry: Boolean = true, showName: Boolean = true, showPostalCode: Boolean = true` | No | The entire formatted address represented as a single string, as it would be written on an envelope. The formatting of this field may vary according to the country of the address (which may not match this Kraken installation's home country). It may also change if we update our address-formatting code or if our understanding of the correct formatting for a given country changes. Avoid parsing individual components of an address out of this field's value; use the other fields on this type instead. |
| `country` | `String` |  | No | ISO 3166-1 alpha-2 code of the country this address belongs to, e.g. `AU`, `GB`, `NZ`. |
| `deliveryPointIdentifier` | `String` |  | No | Identifier used by the local postal service for this address, e.g. AU DPID, GB postcode + Delivery Point Suffix, US Zip-9 + Delivery Point. This is the value that gets encoded in the barcode printed on the envelope by large-volume bulk mail providers. |
| `dependentLocality` | `String` |  | No | UK dependent localities, or neighbourhoods or boroughs in some other locations. |
| `locality` | `String` |  | No | City or town portion of an address, e.g. US city, AU suburb/town, NZ suburb and city/town, IT comune, UK post town. |
| `name` | `String` |  | No | A personal name. |
| `organization` | `String` |  | No | The name of a business or organisation. |
| `postalCode` | `String` |  | No | Postal code (ZIP code in the US). |
| `sortingCode` | `String` |  | No | Sorting code, e.g. FR CEDEX code. This field is not used in many countries. |
| `streetAddress` | `String` |  | No | The 'street address' component. This value can (and often will) contain newline characters when appropriate. In some cases, data may appear in this field instead of the below fields; e.g. a UK post town name may appear here instead of in the `dependent_locality` field. This happens when data has been migrated from a legacy format, and that format had insufficient metadata to determine the appropriate field. If `structured_street_address` is also set, the value of this field will be a string generated from that value. |
| `structuredStreetAddress` | `GenericScalar` |  | No | The 'street address' component, in a structured format. This field stores the same value as `street_address`, but with more detail; for instance, instead of `123 Example Street` it might be `{'street_number': '123', 'street_name': 'Example', 'street_type': 'Street'}`. In many cases this will be blank; we only use this field for Krakens where we need to supply this level of granularity to some third-party service, like a bulk mail provider. The exact structure of this value depends on the country _of the address_, which is not necessarily the same as the country this Kraken is configured to serve. For addresses outside of the countries listed below, this field will be left blank. ### `AU`: Australia The following keys may be present; all are optional. All keys have string values, and their meaning is the same as their aseXML counterparts. (Note that, unlike aseXML, all keys are provided at the top level, rather than being nested.) - `flat_or_unit_type` - `flat_or_unit_number` - `floor_or_level_type` - `floor_or_level_number` - `building_or_property_name` - `location_descriptor` - `lot_number` - `house_number_1` - `house_number_suffix_1` - `house_number_2` - `house_number_suffix_2` - `street_name` - `street_type` - `street_suffix` - `postal_delivery_type` - `postal_delivery_number_prefix` - `postal_delivery_number_value` - `postal_delivery_number_suffix` ### `JP`: Japan The following keys may be present; all are optional. If keys are empty, they may be omitted from the response entirely. - `chome` - `banchi` - `go` - `edaban` - `kana_building_name` - `kanji_building_name` - `building_number` - `room_number` - `address_code` - `physical_location_identifier` - `kana_company_name` - `kanji_company_name` ### `NZ`: New Zealand The following keys may be present; all are optional. If keys are empty, they may be omitted from the response entirely. - `flat_or_unit_type` - `flat_or_unit_number` - `floor_or_level_type` - `floor_or_level_number` - `property_name` - `building_name` - `house_number_1` - `house_number_suffix_1` - `house_number_2` - `house_number_suffix_2` - `street_prefix` - `street_name` - `street_type` - `street_suffix` - `rural_delivery_number` - `mailtown` - `postal_delivery_type` - `postal_delivery_location` - `postal_delivery_number_prefix` - `postal_delivery_number_value` - `postal_delivery_number_suffix` |

## `PropertySearchResult`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `property` | `PropertyType!` |  | No | The matched property. |
| `score` | `Decimal!` |  | No | A score representing the degree of confidence for a match. |

## `PropertyType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `address` | `String` |  | No | The address of the property, formatted into a single string. |
| `ancestors` | `PropertyConnection` | `hierarchyName: String = "default", before: String, after: String, first: Int, last: Int` | No | Ancestor properties in the specified hierarchy, ordered from root to immediate parent. Returns empty list if the property is not in the hierarchy. |
| `coordinates` | `CoordinatesType` |  | No | Coordinates for the property, useful for displaying the property on a map. |
| `descendants` | `PropertyConnection` | `hierarchyName: String = "default", depth: Int = 1, before: String, after: String, first: Int, last: Int` | No | Descendant properties in the specified hierarchy. Returns empty list if the property is not in the hierarchy. |
| `electricitySupplyPoints` | `[ElectricitySupplyPoint]` |  | No | All the electricity supply points at this property. |
| `embeddedNetwork` | `EmbeddedNetworkType` |  | No | The embedded network this property belongs to, if any. |
| `gasSupplyPoints` | `[GasSupplyPoint]` |  | No | All the gas supply points at this property. |
| `id` | `String` |  | No |  |
| `label` | `String` |  | No | An optional label for the property. |
| `measurements` | `MeasurementConnection` | `startAt: DateTime = "0001-01-03T00:00:00-00:14:44", endAt: DateTime = "9999-12-29T23:59:59.999999+01:00", startOn: Date, endOn: Date, timezone: String = "Europe/Madrid", utilityFilters: [UtilityFiltersInput] = [], before: String, after: String, first: Int, last: Int` | No | Measurements at a property |
| `occupancyPeriods` | `[OccupancyPeriodType]` |  | No | Time periods during which the property is associated with an account. Useful to display information about house-moves, as performing a move out of a property will set the end date for the occupancy period. |
| `parent` | `PropertyInterface` | `hierarchyName: String = "default"` | No | The parent property in the specified hierarchy. Returns null if the property has no parent or is not in the hierarchy. |
| `postcode` | `String` |  | No | The postcode of the property. |
| `richAddress` | `PropertyRichAddressType` |  | No | Property rich address. |
| `splitAddress` | `[String]` |  | No | List of address lines. |

## `ProviderAuthDetailsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `oauthUri` | `String!` |  | No | OAuth 2.0 URI for the provider. |

## `ProviderVirtualKeyDetailsType`

Details of a public key that can be added to devices for end-to-end authentication or encryption. E.g. for Tesla the user visits a URL and the name can be used to show what the key is called. https://github.com/teslamotors/vehicle-command#distributing-your-public-key

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `virtualKeyName` | `String!` |  | No | Friendly human-readable name for the virtual key. |
| `virtualKeyUri` | `String!` |  | No | URI for the virtual key. |

## `Province`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `label` | `String` |  | No | Province name. |
| `value` | `String` |  | No | The province postal code. |

## `ProvisionalTransactionConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ProvisionalTransactionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ProvisionalTransactionConnectionTypeEdge`

A Relay edge containing a `ProvisionalTransactionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ProvisionalTransactionType` |  | No | The item at the end of the edge |

## `ProvisionalTransactionType`

A provisional transaction represents some debit or credit to or from a customer's account which we cannot yet finalise for some reason, but which is still useful to keep a note of, and display to the customer. Provisional transactions are purely to give guidance in the absence of finalised information. We therefore only return provisional transactions that have not been finalised. When a transaction is finalised, it is available through the `transactions` field.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int` |  | No | The amount in pence for this provisional transaction. It will be negative for charges, positive for credits. |
| `date` | `Date` |  | No | The date at which the charge should be applied to the account. |
| `id` | `ID!` |  | No |  |
| `title` | `String` |  | No | A user readable string that indicates what this transaction relates to. |

## `PublicChargingSession`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cost` | `Money` |  | No | The cost for the charge added during a charging session. |
| `end` | `DateTime!` |  | No | The end time of a charging session. |
| `energyAdded` | `Energy` |  | No | The energy added during a charging session. |
| `location` | `String!` |  | No | Location of the charging session. |
| `operatorImageUrl` | `String` |  | No | URL of the operator image. |
| `start` | `DateTime!` |  | No | The start time of a charging session. |
| `stateOfChargeChange` | `Decimal` |  | No | The change in state of charge during a charging session. The value will be between 0 and 100, if not null. |
| `stateOfChargeFinal` | `Decimal` |  | No | The final state of charge after a charging session. The value will be between 0 and 100, if not null. |

## `PublishApprovalApprovedEvent`

The possible errors that can be raised are: - KT-CT-14501: Invalid event parameters. - KT-CT-14502: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `eventId` | `ID` |  | No | The ID of the created approval approved event. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `PublishTransactionalMessagingExternalTrigger`

Publish an externally defined transactional messaging trigger. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-5421: Account user not found. - KT-CT-9901: Invalid trigger type code. - KT-CT-9905: Top-level context fields are missing. - KT-CT-9906: Template variables do not match the defined schema. - KT-CT-9908: Invalid recipient information. - KT-CT-9909: Invalid recipient information. - KT-CT-9910: Invalid input field combination. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `trigger` | `Trigger` |  | No | The trigger that has been published. |

## `PublishTransactionalMessagingTrigger`

Publish a trigger within the transactional messaging service. The possible errors that can be raised are: - KT-CT-9901: Invalid trigger type code. - KT-CT-9902: Invalid trigger type params. - KT-CT-9903: Trigger type cannot be published externally. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `trigger` | `Trigger` |  | No | The trigger that has been published. |

## `PurchaseVoucher`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `voucherPurchase` | `VoucherPurchaseType` |  | No | The voucher purchase created from the mutation. |

## `PushNotificationBindingType`

Represents a pairing of a single app installation to an account user.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `application` | `NotifiableApplicationType!` |  | No |  |
| `expiresAt` | `DateTime!` |  | No |  |
| `id` | `ID!` |  | No |  |
| `messages` | `PrintMessageTypeConnection!` | `offset: Int, before: String, after: String, first: Int, last: Int` | No |  |
| `registeredAt` | `DateTime!` |  | No |  |
| `token` | `String!` |  | No |  |
| `user` | `EspAccountUserType!` |  | No |  |

## `QuantityType`

Graphene type object to represent Quantity(magnitude, unit)

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `magnitude` | `Float!` |  | No | The numeric value of this field. |
| `unit` | `String!` |  | No | Unit of this field. |

## `Query`

Queries are the GraphQL equivalent of GET requests in REST. By convention, they do not mutate data. To learn about how to form Queries in graphql, see [GraphQL's documentation](https://graphql.org/learn/queries/). ⬅️ This interface will autocomplete, so just try typing what you want. You can also search these docs. Some queries will require authentication. Check the documentation or search `Authentication` for details.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `a629Details` | `A629Details` | `cups: String!, nif: String` | No | Retrieve A629 supply point information including acceptance, rejection or error details. The possible errors that can be raised are: - KT-ES-4504: A529 requests are currently not implemented for the provided DNO. - KT-ES-4505: A529 requests are currently not configured for the provided DNO. - KT-ES-4506: Unauthorized A529 call. - KT-ES-4507: Unexpected error retrieving A529 details. - KT-CT-1113: Disabled GraphQL field requested. |
| `account` | `Account` | `accountNumber: String!` | No | Get details about an account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `accountBillingInfo` | `AccountBillingInfo` | `accountNumber: String!` | No | Get details about an account's billing info. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `accountChargeReasons` | `[ChargeReasonType]` |  | No | Available reasons for use in account charge mutations. |
| `accountContract` | `Contract` | `identifier: String, accountNumber: String, version: Int` | No | Get details about an account contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10005: Missing required parameter: either identifier or accountNumber must be provided. - KT-CT-10006: Account not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `accountCreditReasons` | `[CreditReasonType]` |  | No | Available reasons for use in account credit mutations. |
| `accountIoEligibility` | `AccountIoEligibility` | `accountNumber: String!, propertyId: Int` | No | Determines whether an account is eligible to register devices with SmartFlex. |
| `accountPaymentInfo` | `AccountPaymentInfo` | `accountNumber: String!` | No | Get details about an account's payments info. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `accountReference` | `[AccountReferenceType]` | `value: String` | No | List of matching account references. The possible errors that can be raised are: - KT-CT-8310: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. |
| `accountUser` | `EspAccountUserType` | `email: String, number: ID, externalId: ID` | No | Retrieve an account user. The possible errors that can be raised are: - KT-CT-5418: Account user not found. - KT-CT-5415: Account user not found. - KT-CT-5423: Account user not found. - KT-CT-5424: Invalid data. - KT-CT-5421: Account user not found. - KT-CT-5425: Account user not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `accounts` | `[Account]` | `phoneNumber: String, portfolioNumber: String` | No | Get details about multiple accounts. The possible errors that can be raised are: - KT-CT-4184: Exactly one of phoneNumber or portfolioNumber must be provided. - KT-CT-1113: Disabled GraphQL field requested. |
| `accountsSearch` | `[AccountSearchItemType]` | `searchTerms: AccountSearchInputType, maxResults: Int = 20` | No | Search for account that are already in Kraken and match the search terms. The possible errors that can be raised are: - KT-CT-4183: One of more search terms failed validations. - KT-CT-1113: Disabled GraphQL field requested. |
| `activeAffiliateReferralScheme` | `ReferralSchemeType` | `subdomain: String!, accountType: ReferralSchemeAccountTypeOptions` | No | Return the current active referral reward scheme of a given affiliate organisation, if any exists. |
| `activeDomesticSignupRewardScheme` | `ReferralSchemeType` |  | No | Return the current active signup referral reward scheme with the given code, if any exists. |
| `activeSalesChannels` | `[SalesChannelType]` | `activeFrom: DateTime, activeTo: DateTime` | No | A list of active sales channels. The possible errors that can be raised are: - KT-CT-12702: Invalid datetime range. - KT-CT-1113: Disabled GraphQL field requested. |
| `addressSearch` | `[CadastreRichAddressType!]` | `address: String!, postcode: String` | No | Search for addresses in the cadastre that match the search term. The possible errors that can be raised are: - KT-ES-4403: Address search service not enabled. - KT-ES-4404: Address search service unavailable. - KT-CT-1113: Disabled GraphQL field requested. |
| `affiliateLink` | `AffiliateLinkType!` | `subdomain: String!` | No | Link object for an affiliate organization. The possible errors that can be raised are: - KT-CT-7713: Invalid data. - KT-CT-7718: Affiliate link is expired. - KT-CT-1113: Disabled GraphQL field requested. |
| `affiliateLinks` | `[AffiliateLinkType!]!` | `agentContactEmail: String!` | No | Links (urls) for the affiliate organizations. |
| `affiliateOrganisation` | `AffiliateOrganisationType` | `id: Int, number: String` | No | Return the details of a given affiliate organization, if any exists. The possible errors that can be raised are: - KT-CT-7701: The affiliate organisation was not found. - KT-CT-7702: Either id or number must be provided. - KT-CT-1113: Disabled GraphQL field requested. |
| `affiliateProducts` | `[AffiliateProductType]` | `organizationName: String!` | No | Information on products for affiliate organizations. The possible errors that can be raised are: - KT-ES-7813: Affiliate product information not available. - KT-CT-1113: Disabled GraphQL field requested. |
| `agentCallCenterStatus` | `AgentCallCenterStatusType!` | `supportUserName: String!` | No | Get the call center status for a given agent. The possible errors that can be raised are: - KT-CT-7813: Support user not found with that username. - KT-CT-1113: Disabled GraphQL field requested. |
| `agreement` | `Agreement` | `id: ID!` | No | Get an agreement by id. |
| `agreementRollover` | `AgreementRolloverType` | `number: String!` | No | Get an agreement rollover by its number. The possible errors that can be raised are: - KT-CT-13705: Agreement rollover not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `agreementsForRollover` | `[CommonAgreementType]` | `daysBeforeExpiration: Int!, windowSize: Int!` | No | Get agreements eligible for the rollover process. |
| `apiBrownouts` | `APIBrownoutConnection` | `input: APIBrownoutInput, before: String, after: String, first: Int, last: Int` | No | Get brownouts by status. |
| `apiExceptions` | `APIExceptionConnectionTypeConnection` | `input: APIExceptionQueryInput, before: String, after: String, first: Int, last: Int` | No | Get a connection containing API Exceptions. |
| `appSessions` | `AppSessionConnectionTypeConnection!` | `postcode: String, subdomain: String, before: String, after: String, first: Int, last: Int` | No | App sessions recorded at the specified postcode or for the specified affiliate link subdomain. |
| `authorizedApplications` | `[AuthorizedApplication]` |  | No | Get all the confidential-client applications the current user has authorized. |
| `availableOfferings` | `[OfferingType]` |  | No | Get a list of actively available offerings from the catalog. |
| `availableProductSwitchDates` | `[Date]` | `agreementId: Int!, maxRange: Int = 365` | No | Get available dates for product switch. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `availableProducts` | `[SupplyProductType]` | `marketName: String!` | No | Get available products for the given market. The possible errors that can be raised are: - KT-CT-4930: Unsupported market. - KT-CT-1113: Disabled GraphQL field requested. |
| `backendScreen` | `BackendScreenType` | `screenId: ID!, params: [BackendScreenParamInputType], maxVersionSupported: Int = 1` | No | Get mobile screen details to render. The possible errors that can be raised are: - KT-CT-8001: No backend screen available. - KT-CT-8005: Backend screen does not support parameters. - KT-CT-8008: Incorrect or missing data necessary to build the screen. - KT-CT-8006: Error applying parameters to backend screen. - KT-CT-8009: Error translating screen content. - KT-CT-8010: Invalid step ID. - KT-CT-8011: Cannot rewind past a previous irreversible step. - KT-CT-1113: Disabled GraphQL field requested. |
| `backendScreenEventIds` | `[String]` |  | No | Get all registered backend screen event IDs. |
| `backendScreenIds` | `[String]` |  | No | Get all registered backend screen IDs. |
| `bankDetailsValidation` | `BankDetailsValidationResult` | `iban: NonEmptyString!` | No |  |
| `business` | `BusinessType` | `id: ID, details: [BusinessDetailInput]` | No | Get details about a business. The possible errors that can be raised are: - KT-CT-11101: The viewer is not authorized to execute the query/mutation. Check the ownership/permissions of provided data. - KT-CT-11107: Unauthorized. - KT-CT-1605: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. |
| `businessAccountReferralRewardScheme` | `ReferralSchemeType` | `code: String!` | No | Return a business referral reward scheme for the given account referral code. |
| `businessContract` | `Contract` | `identifier: String, accountNumber: String, version: Int` | No | Get details about an account contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10005: Missing required parameter: either identifier or accountNumber must be provided. - KT-CT-10006: Account not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `call` | `CallInterface!` | `id: ID!` | No | Get a call for a given ID. The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `callTag` | `CallTagType!` | `id: ID!` | No | Get the call tag for a given ID. The possible errors that can be raised are: - KT-CT-11809: Call tag not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `callTags` | `CallTagConnectionTypeConnection!` | `name: String, isActive: Boolean, before: String, after: String, first: Int, last: Int` | No | Get call tags. |
| `campaigns` | `AccountCampaignConnectionTypeConnection` | `accountNumber: String!, before: String, after: String, first: Int, last: Int` | No | The campaigns associated with this account. |
| `canRescindAgreement` | `Boolean` | `agreementId: Int!` | No | Check if an agreement can be rescinded. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `chargePointVariants` | `[ChargePointVariantType]` |  | No | All charge points variants. |
| `collectionProcessDetails` | `CollectionProcessDetailsType` | `collectionProcessRecordNumber: String!` | No | Collection process record details. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11206: Unable to retrieve disconnection related data for collection process. - KT-CT-1113: Disabled GraphQL field requested. |
| `complaint` | `ComplaintType` | `complaintId: Int!` | No | Get a complaint. The possible errors that can be raised are: - KT-CT-12301: Complaint not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `completedDispatches` | `[UpsideDispatchType]` | `accountNumber: String!` | No | All completed device dispatches 12 hours behind, in reverse time order. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4341: Unable to fetch completed dispatches. - KT-CT-1113: Disabled GraphQL field requested. |
| `consentTypes` | `[ConsentTypeType]` |  | No | A list of the consent types available. |
| `contractCreationJourney` | `ContractCreationJourneyType` | `number: String!` | No | Get details about a contract creation journey. The possible errors that can be raised are: - KT-CT-10017: The contract journey could not be found. - KT-CT-1113: Disabled GraphQL field requested. |
| `contractNoteReasons` | `[ContractNoteReasonType]` | `activityTypes: [ContractActivityTypeOptions]` | No | Get a list of contract note reasons, optionally filtered by activity types. |
| `contracts` | `[Contract]` | `filters: ContractFiltersInput!` | No | Get a list of contracts filtered by party or subject. The possible errors that can be raised are: - KT-CT-10029: Missing contract filters. - KT-CT-10030: Filter by subject is not implemented. - KT-CT-10031: Invalid party filter. - KT-CT-1113: Disabled GraphQL field requested. |
| `contributionSchemes` | `[ContributionSchemeType]` |  | No | Get contribution schemes. |
| `costOfCharge` | `[CostOfChargeType]` | `accountNumber: String!, frequency: DataFrequency!, startDate: Date` | Yes (The 'costOfCharge' field is deprecated. Use `cost` field on `SmartFlexChargingSession` instead. - Marked as deprecated on 2025-05-13. - Scheduled for removal on or after 2026-01-16. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/605/) | Aggregated cost of charge for an EV device. The possible errors that can be raised are: - KT-CT-4326: Could not get consumption cost data. - KT-CT-1113: Disabled GraphQL field requested. |
| `cupsRegion` | `String` | `cups: String!` | No | Gets the region where a CUPS is physically located. |
| `cupsValidationToContractAtrBased` | `CupsValidationToContract` | `cupsAndProductInput: CupsValidationToContractInput!` | No | Get confirmation if cups is valid to make a contract. The possible errors that can be raised are: - KT-ES-7812: Product ID does not exist. - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested. |
| `cupsValidationToContractAtrBasedV2` | `CupsValidationToContract` | `input: CupsValidationToContractInput!` | Yes (The 'cupsValidationToContractAtrBasedV2' field is deprecated. Never used. Use 'cupsValidationToContractAtrBased' instead. - Marked as deprecated on 2024-05-27. - Scheduled for removal on or after 2024-07-01.) | Get confirmation if cups is valid to contract the products. The possible errors that can be raised are: - KT-ES-7812: Product ID does not exist. - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested. |
| `customerFeedbackForms` | `CustomerFeedbackFormConnectionTypeConnection` | `accountNumber: String!, feedbackSource: CustomerFeedbackSourceChoices, before: String, after: String, first: Int, last: Int` | No | Returns all active customer feedback forms for the account's brand. |
| `dailyWholesalePrices` | `[DailyWholesalePrice]` | `start: Date, end: Date` | Yes (The 'dailyWholesalePrices' field is deprecated. Migrated to OE Backend API. - Marked as deprecated on 2025-10-27. - Scheduled for removal on or after 2025-11-10.) | Get the daily wholesale prices per hour for the given dates. |
| `dashboardScreen` | `Dashboard` | `dashboardId: ID!, accountNumber: String!, maxVersionSupported: Int! = 1, ledgerNumber: String, propertyId: String, params: [BackendScreenParamInputType]` | No | Get a dashboard screen to render in the form of a json list of sections containing cards or grouped cards each with an order attribute. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-8001: No backend screen available. - KT-CT-8005: Backend screen does not support parameters. - KT-CT-8008: Incorrect or missing data necessary to build the screen. - KT-CT-8006: Error applying parameters to backend screen. - KT-CT-8009: Error translating screen content. - KT-CT-8010: Invalid step ID. - KT-CT-8011: Cannot rewind past a previous irreversible step. - KT-CT-1113: Disabled GraphQL field requested. |
| `defaultPaymentInstruction` | `PaymentInstructionType` | `accountNumber: String!, instructionType: PaymentType` | Yes (The 'defaultPaymentInstruction' field is deprecated. Please use 'usablePaymentInstructions' on the Ledger type to get all usable instructions, or 'paymentPreferenceAtTime' on the Ledger type to get a specific one. Both require explicitly requesting a ledger. - Marked as deprecated on 2026-01-28. - Scheduled for removal on or after 2026-07-28.) | Get the default payment instruction for the account's main ledger. |
| `defaultRawScore` | `Int` | `formId: Int!` | No | Get default raw score for a customer feedback form. The possible errors that can be raised are: - KT-CT-5513: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. |
| `depositAgreements` | `[DepositAgreementOutput]` | `accountNumber: String!` | No | Get deposit agreements for a given account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `devices` | `[SmartFlexDeviceInterface!]` | `accountNumber: String!, propertyId: ID, deviceId: String, integrationDeviceId: String` | No | A list of devices registered to an account. |
| `domesticAccountReferralRewardScheme` | `ReferralSchemeType` | `code: String!` | No | Return a domestic referral reward scheme for the given account referral code. |
| `domesticJoiningRewardScheme` | `ReferralSchemeType` | `code: String!` | No | Return a joining reward scheme with the given code, if it's active. A joining reward can be a signup reward or a promotional reward. |
| `domesticSignupRewardScheme` | `ReferralSchemeType` | `code: String!` | No | Return a signup referral reward scheme with the given code, if it's active. |
| `electricVehicles` | `[ElectricVehicleType]` | `make: String, supportedProvider: ProviderChoices, isIntegrationLive: Boolean` | No | All electric vehicle types and their details. The possible errors that can be raised are: - KT-CT-4343: Unable to fetch electric vehicles list for make. - KT-CT-4344: Make is not supported by provider. - KT-CT-1113: Disabled GraphQL field requested. |
| `electricitySupplyPoint` | `ElectricitySupplyPoint` | `id: ID!` | No | Get information about a supply point by its ID. |
| `eligibilityToJoinLoyaltyPointsProgram` | `LoyaltyPointsProgramEligibilityType` | `input: LoyaltyPointsProgramEligibilityInput!` | No | Check if an account is eligible to join the loyalty points program. The possible errors that can be raised are: - KT-CT-9202: Loyalty Points adapter not configured. - KT-CT-9218: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `eligibleDeviceTypes` | `[KrakenFlexDeviceTypes]` | `accountNumber: String!, propertyId: Int` | No | A list of device types that are eligible for registration. |
| `embeddedNetwork` | `EmbeddedNetworkType` | `id: ID!` | No | Get details about an embedded network. |
| `energyMixData` | `EnergyMixDataType` |  | No | The current energy generation mix. |
| `enodeLinkSession` | `EnodeLinkSessionType` | `accountNumber: String, vendor: EnodeVendors` | Yes (The 'enodeLinkSession' field is deprecated. Please use 'startSmartFlexOnboarding' instead. - Marked as deprecated on 2025-10-30. - Scheduled for removal on or after 2026-04-30. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/608/) | The user specific Enode link session details. The possible errors that can be raised are: - KT-CT-4328: Invalid data. - KT-CT-1111: Unauthorized. - KT-CT-4319: Unable to get Enode link session. - KT-CT-1113: Disabled GraphQL field requested. |
| `estimateMeterReadings` | `MeterReadingEstimationReadingConnection` | `periodStart: DateTime!, periodEnd: DateTime!, marketIdentifier: ID!, deviceId: ID, registerId: ID, before: String, after: String, first: Int, last: Int` | No | Estimated meter readings. |
| `externalAccountEvents` | `ExternalAccountEventConnectionTypeConnection` | `accountNumber: String!, before: String, after: String, first: Int, last: Int` | No | Get a list of audit account events, of type external, for a given account. |
| `flexPlannedDispatches` | `[SmartFlexDispatch]` | `deviceId: String!` | No | All planned device dispatches in time order. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4340: Unable to fetch planned dispatches. - KT-CT-1113: Disabled GraphQL field requested. |
| `flexSupportedDevices` | `FlexSupportedDevices` | `deviceType: KrakenFlexDeviceTypes!` | No | Devices capable of being registered with SmartFlex. |
| `fraudMeterPointChecks` | `FraudMeterPointCheckType` | `meterPointId: String!` | No | Check if a given meter point ID is in suspicious meter point IDs list. |
| `fraudRiskLevel` | `FinancialRiskLevelType` | `identifierValue: String!, identifierType: String!` | No | Check if a given ID and type have a financial risk level. |
| `gasSupplyPoint` | `GasSupplyPoint` | `id: ID!` | No | Get information about a supply point by its ID. |
| `getOnSiteJobsAppointmentByExternalReference` | `OnSiteJobsAppointmentType` | `externalReference: String!, agent: OnSiteJobsAgent!` | No | Get appointment by external reference and agent. |
| `getOnSiteJobsAppointmentById` | `OnSiteJobsAppointmentType` | `appointmentId: UUID` | No | Get a specific appointment by Kraken ID. |
| `getOnSiteJobsAppointmentSlots` | `OnSiteJobsAppointmentSlotResultsType` | `appointmentBookingSessionId: UUID!, appointmentDate: Date!` | No | Get appointment slot results using appointment booking session ID. |
| `getOnSiteJobsCheckResults` | `OnSiteJobsCheckResultsType` | `supplyPointIdentifierToMarketNameMapping: [SupplyPointIdentifierToMarketNameMappingInput], supplyPointInternalIds: [Int], jobType: String` | No | Get check results for creating requests and appointments. |
| `getOnSiteJobsJobTypes` | `[OnSiteJobsJobTypeType]` | `requestId: UUID!, workCategory: OnSiteJobsWorkCategory` | No | Get available job types for an on-site jobs request. |
| `getOnSiteJobsRequestById` | `OnSiteJobsRequestType` | `requestId: UUID` | No | Get a specific request by ID. |
| `getOnSiteJobsRequests` | `OnSiteJobsRequestConnectionTypeConnection` | `supplyPointsToMarketNamesMapping: [SupplyPointIdentifierToMarketNameMappingInput], supplyPointInternalIds: [Int], statuses: [OnSiteJobsRequestStatus], before: String, after: String, first: Int, last: Int` | No | Filter On-Site Jobs Requests. |
| `goodsProducts` | `GoodsProductConnectionTypeConnection` | `marketName: String!, productType: [String], code: [String], before: String, after: String, first: Int, last: Int` | No | List Goods products given a market. |
| `goodsPurchases` | `[GoodsPurchase]` | `accountNumber: String!` | No | List purchases for an account. |
| `goodsQuotes` | `[GoodsQuote]` | `accountNumber: String, quoteCode: String` | No | List quotes given an account number or retrieve a Goods quote given a quote code. The possible errors that can be raised are: - KT-CT-8204: Invalid arguments. - KT-CT-8223: Unauthorized. - KT-CT-8201: Received an invalid quoteId. - KT-CT-8204: Invalid arguments. - KT-CT-1113: Disabled GraphQL field requested. |
| `inboundCallAverageWaitTime` | `InboundCallAverageWaitTimeType` |  | No | Get the average wait time for an inbound call. |
| `inkCommsTemplate` | `String!` | `templateIdentifier: String!` | No | Fetch the content of a given comms template name. The possible errors that can be raised are: - KT-CT-7648: The comms template was not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `inkConversation` | `InkConversation!` | `accountNumber: String, conversationRelayId: String` | No | Get the Ink conversation for a given account. The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-4177: Unauthorized. - KT-CT-7610: No Ink conversation for account. - KT-CT-7617: Must supply account number or relay id to get a conversation. - KT-CT-7638: Invalid conversation ID. - KT-CT-1113: Disabled GraphQL field requested. |
| `inkMessage` | `InkMessage!` | `messageRelayId: String!` | No | Get the content for a given message. The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-7638: Invalid conversation ID. - KT-CT-1113: Disabled GraphQL field requested. |
| `inkMessageAttributes` | `InkMessageAttributes!` | `vendor: String!, vendorId: String!` | No | Get attributes of a message at time of query. The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `inkMessageTextContent` | `String!` | `messageId: ID!` | No | Fetch the text content of a given message. The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `internalCompanies` | `InternalCompanyConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Get all internal companies. |
| `internalCompany` | `InternalCompanyType` | `criteria: SearchCriteriaInput!` | No | Get an internal company by a set of criteria. Criteria will be added as needed, check documentation for the criteria object to see what is currently supported. The possible errors that can be raised are: - KT-CT-14401: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `isCustomerEligibleToGiveFeedbackFollowingCall` | `Boolean` | `accountNumber: String!, accountUserNumber: String!, callId: Int!` | No | Check if customer is eligible to give feedback following a phone call. The possible errors that can be raised are: - KT-CT-5519: Voice call not found. - KT-CT-5521: Eligibility configuration not found. - KT-CT-5522: Invalid eligibility configuration. - KT-CT-5523: Invalid account or account user. - KT-CT-1113: Disabled GraphQL field requested. |
| `isCustomerEligibleToGiveFeedbackFollowingEmail` | `Boolean` | `accountNumber: String!, accountUserNumber: String!, inkConversationId: Int!, conversationClosedAt: DateTime!` | No | Check if customer is eligible to give feedback following an email conversation. The possible errors that can be raised are: - KT-CT-5520: Ink conversation not found. - KT-CT-5521: Eligibility configuration not found. - KT-CT-5522: Invalid eligibility configuration. - KT-CT-5523: Invalid account or account user. - KT-CT-1113: Disabled GraphQL field requested. |
| `isPasswordResetTokenValid` | `Boolean` | `userId: String!, token: String!` | No | Check validity of a password reset token. |
| `joinSupplierProcess` | `JoinSupplierProcessType` | `number: String!` | No | The possible errors that can be raised are: - KT-CT-10332: Join supplier process not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `krakenVersion` | `KrakenVersionType` |  | No | The current version of kraken. |
| `leadBlocklistValidations` | `LeadBlockListValidationOutput` | `blockListEntries: LeadBlockListValidationInput` | No | Run a blocklist validation out of some dynamic client entry types. |
| `leadByNumber` | `LeadOutput` | `number: String` | No | Get lead details by number. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `leads` | `LeadsConnection` | `input: LeadsQueryInput, offset: Int, before: String, after: String, first: Int, last: Int` | No | Fetch all leads for this Kraken, with optional filtering. |
| `leaveSupplierProcess` | `LeaveSupplierProcessType` | `number: String` | No | Details associated with a LeaveSupplier process. The possible errors that can be raised are: - KT-CT-10302: Invalid data. - KT-CT-10333: Missing either number of leave supplier process id. - KT-CT-1113: Disabled GraphQL field requested. |
| `legacyOrderDetails` | `LegacyOrderDetailsType` | `identifier: String!` | No | The possible errors that can be raised are: - KT-CT-13101: Order not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `lifecycleProcesses` | `LifecycleProcessesType` | `onlyActive: Boolean, sortOrder: LifecycleProcessesSortOrder, accountNumber: String!` | No | Get all lifecycle processes associated with an account. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `livePaymentAdequacyCalculation` | `LivePaymentAdequacyCalculation` | `ledgerNumber: String!` | No | Get payment adequacy data with an up to date calculation. The possible errors that can be raised are: - KT-CT-3963: Could not calculate live PA data. - KT-CT-1113: Disabled GraphQL field requested. |
| `loyaltyCards` | `[LoyaltyCardType]` | `accountUserId: String!` | No | Get all loyalty cards for the given account user. The possible errors that can be raised are: - KT-CT-5412: No account user exists with the given id. - KT-CT-1113: Disabled GraphQL field requested. |
| `loyaltyPointLedgerEntry` | `LoyaltyPointLedgerEntryType` | `input: LoyaltyPointLedgerEntryInput!` | No | Resolve a loyalty point ledger entry. The possible errors that can be raised are: - KT-CT-9215: Loyalty points balance query disabled. - KT-CT-9223: Loyalty points ledger entry not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `loyaltyPointLedgers` | `[LoyaltyPointLedgerEntryType]` | `input: LoyaltyPointLedgersInput` | No | Get the Loyalty Point ledger entries for the passed user. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `loyaltyPointsBalance` | `AccountLoyaltyPointsType` | `input: LoyaltyPointsBalanceInput` | No | Get the loyalty points balance for an account. The possible errors that can be raised are: - KT-CT-9218: Unauthorized. - KT-CT-9217: Unauthorized. - KT-CT-9215: Loyalty points balance query disabled. - KT-CT-9216: Unauthorized. - KT-CT-9222: Loyalty points balance query requires either accountNumber field (deprecated) or input object (preferred) with account number and optional account user id. - KT-CT-1113: Disabled GraphQL field requested. |
| `metadata` | `[Metadata]` | `linkedObjectType: LinkedObjectType, identifier: String!` | No | Metadata for a linked object. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4124: Unauthorized. - KT-CT-8411: Invalid data. - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `metadataForKey` | `Metadata` | `linkedObjectType: LinkedObjectType, identifier: String!, key: String!` | No | Metadata for a linked object with key. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4124: Unauthorized. - KT-CT-8411: Invalid data. - KT-CT-4179: No metadata found with given key. - KT-CT-4155: Invalid data. - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `mfaDevices` | `[MfaDevice]` |  | No | Get all MFA devices for the current user. |
| `node` | `Node` | `id: ID!` | No |  |
| `ocppConnection` | `OCPPConnectionType` | `accountNumber: String!` | No | To confirm whether a device is connected to OCPP. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4311: Unable to confirm OCPP connection. - KT-CT-1113: Disabled GraphQL field requested. |
| `ocppDetails` | `OCPPDetailsType` | `accountNumber: String!` | No | The user specific generated OCPP details. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `ocuCollectivePurchaseCanContract` | `Boolean` | `customerId: String!` | No | Resolves whether an OCU collective purchase customer can contract or not. The possible errors that can be raised are: - KT-ES-7810: Customer has reached its max amount of agreements for the OCU collective purchase product. - KT-ES-7811: Customer isn't allowed to contract OCU collective purchase product. - KT-CT-1113: Disabled GraphQL field requested. |
| `offerForQuoting` | `OfferType` | `identifier: ID` | No |  |
| `offerGroupForQuoting` | `OfferGroupType` | `identifier: ID` | No |  |
| `offering` | `OfferingType` | `identifier: String` | No | Get details about a product offering. The possible errors that can be raised are: - KT-CT-12001: Product catalogue offering with given identifier not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `onboardingReferralCurrentlyAllowed` | `OnboardingReferralAllowedType` | `referralCode: String!` | No | Gives a prediction on whether a referral will be valid. The possible errors that can be raised are: - KT-ES-6701: Referral currently not allowed. - KT-CT-1113: Disabled GraphQL field requested. |
| `opportunities` | `OpportunitiesConnection` | `input: OpportunitiesQueryInput, offset: Int, before: String, after: String, first: Int, last: Int` | No | Fetch all opportunities for this Kraken, with optional filtering. |
| `opportunityByNumber` | `OpportunityOutput` | `number: String` | No | Get opportunity details by number. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `opportunityProductSummary` | `[OpportunityProductSummary!]!` | `number: String` | No | Return summaries of all products in opportunity's accepted offer. Supports multi-product offerings like dual fuel. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8923: The opportunity does not have a linked offer group. - KT-CT-8922: The opportunity does not have an accepted offer. - KT-CT-1113: Disabled GraphQL field requested. |
| `opportunityValueByKey` | `String` | `opportunityId: ID, key: String` | No | Get the value of a given key that is stored in an opportunity's related JSONFields. The possible errors that can be raised are: - KT-CT-8903: Unable to update opportunity. - KT-CT-1113: Disabled GraphQL field requested. |
| `p0Details` | `P0Details` | `cups: String!, nif: String` | No | Retrieve P0 supply point information including acceptance, rejection, or error details. The possible errors that can be raised are: - KT-ES-4501: Unexpected error retrieving P0 details. - KT-ES-4502: P0 requests are currently not supported for the provided DNO. - KT-ES-4503: The DNO sent a malformed P0 response that could not be processed. - KT-CT-1113: Disabled GraphQL field requested. |
| `p0Validation` | `NifCupsCorrelationValidation` | `cups: String!, nif: String!` | No | Call to P0 endpoint crosschecking that a customer with a given NIF is the current owner of the given cups. |
| `passwordValidatorHelpTexts` | `[String]` | `asHtml: Boolean = false` | No | The help text of all configured password validators as plain-text or html. Defaults to plain-text. |
| `paymentFingerprintChecks` | `PaymentFingerPrintCheckType` | `fingerprint: String!` | No | Check if a given payment fingerprint already exists and/or is risk-listed. |
| `paymentRequests` | `PaymentRequestsType` | `ledgerNumber: String!` | No | Get all payment requests for the given ledger. |
| `plannedDispatches` | `[UpsideDispatchType]` | `accountNumber: String!` | Yes (The 'plannedDispatches' field is deprecated. Please use 'flexPlannedDispatches' instead. - Marked as deprecated on 2025-05-27. - Scheduled for removal on or after 2026-01-16. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/604/) | All planned device dispatches 24 hours ahead, (usually) in time order. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4340: Unable to fetch planned dispatches. - KT-CT-1113: Disabled GraphQL field requested. |
| `portfolio` | `PortfolioType` | `portfolioNumber: String!` | No | Get details about a portfolio, using its portfolio number. The possible errors that can be raised are: - KT-CT-9403: Received an invalid portfolioId. - KT-CT-1113: Disabled GraphQL field requested. |
| `portfolioByReference` | `PortfolioType` | `portfolioReference: PortfolioReferenceInput!` | No | Get details about a portfolio, using its reference. The possible errors that can be raised are: - KT-CT-9409: Invalid portfolio reference. - KT-CT-1113: Disabled GraphQL field requested. |
| `possibleErrors` | `PossibleErrorsOutputType` | `input: PossibleErrorsInputType!` | No | Possible errors of the requested query/mutation. The possible errors that can be raised are: - KT-CT-1606: Query/Mutation not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `printBatch` | `PrintBatchType!` | `batchId: ID` | No | Get print batch details, including messages in the batch. The possible errors that can be raised are: - KT-CT-9013: Invalid data. - KT-CT-9012: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. |
| `productsWithEstimates` | `ProductWithEstimates` | `electricityCups: String, electricityAnnualConsumption: Int, gasCups: String, gasAnnualConsumption: Int, brand: String = "OCTOPUS_ENERGY_SPAIN", date: Date, organizationName: String, isHidden: Boolean` | No | Get all products providing an estimate, either CUPS or annualConsumption. The possible errors that can be raised are: - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested. |
| `productsWithoutEstimates` | `[ProductWithoutEstimates]` | `brand: String = "OCTOPUS_ENERGY_SPAIN", date: Date, organizationName: String, isHidden: Boolean` | No | Get all active non-hidden products without providing any estimate. |
| `propertiesSearch` | `[PropertySearchResult!]!` | `searchTerm: String!` | No | Search for properties that are already in Kraken and match the search term. |
| `property` | `PropertyType` | `id: ID!` | No | A property with the given ID. Usually associated with supply points. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `propertySearch` | `[PropertyType]` | `searchTerm: String!` | Yes (The 'propertySearch' field is deprecated. This query is being deprecated in favour of `propertiesSearch`. The latter returns not only the matched properties but the level of confidence in the results through the `score` field. - Marked as deprecated on 2023-05-23. - Scheduled for removal on or after 2024-01-01.) | Search for properties that are already in Kraken and match the search term. |
| `providerAuthDetails` | `ProviderAuthDetailsType` | `provider: ProviderChoices!, deviceType: KrakenFlexDeviceTypes!, clientType: ClientType = APP, accountNumber: String, propertyId: Int` | Yes (The 'providerAuthDetails' field is deprecated. Please use 'startSmartFlexOnboarding' instead. - Marked as deprecated on 2025-10-30. - Scheduled for removal on or after 2026-04-30. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/608/) | Auth details (e.g. OAuth 2.0 URI) for the provider (if available). |
| `providerVirtualKeyDetails` | `ProviderVirtualKeyDetailsType` | `provider: ProviderChoices!, deviceType: KrakenFlexDeviceTypes!` | No | Virtual key details (e.g. certificate public key) for the provider (if available). |
| `provinces` | `[Province]` |  | No | Spanish provinces. |
| `queryComplexity` | `QueryComplexityOutputType` | `input: QueryComplexityInputType!` | No | Get the complexity of a query. |
| `question` | `String` | `formId: Int!` | No | Get the customer feedback survey question. The possible errors that can be raised are: - KT-CT-5513: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. |
| `quoteRequest` | `QuoteRequest` | `code: String!` | No | The quote request with a list of quoted supply points and their products. |
| `quotingParamDefinitionsForProductOffering` | `QuotedOfferingParamsType` | `productOfferingIdentifier: ID` | No | The possible errors that can be raised are: - KT-CT-12403: Product offering not found. - KT-CT-12404: Product offering has expired. - KT-CT-1113: Disabled GraphQL field requested. |
| `rateLimitInfo` | `CombinedRateLimitInformation` |  | No | Combined information about points-allowance rate limiting and request-specific rate limiting. |
| `registeredKrakenflexDevice` | `KrakenFlexDeviceType` | `accountNumber: String!` | Yes (The 'registeredKrakenflexDevice' field is deprecated. Please use 'devices' instead. - Marked as deprecated on 2024-04-23. - Scheduled for removal on or after 2026-03-01. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/677/) | A device registered with KrakenFlex for a given account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `returnSchedule` | `[DepositReturnScheduleOutput]` | `accountNumber: String!` | No | Get deposit agreement related return schedules for a given account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `routingAttributes` | `[RoutingAttributeType]!` | `category: String, search: String` | No | Get routing attributes available for call routing configuration. The possible errors that can be raised are: - KT-CT-11816: Invalid routing attribute category. - KT-CT-1113: Disabled GraphQL field requested. |
| `salesFunnelByCode` | `SalesFunnel` | `input: SalesFunnelInput!` | No | Get the sales funnel by input. The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `salesFunnels` | `[SalesFunnel]` | `input: SalesFunnelsInput` | No | Get all sales funnels. |
| `searchLead` | `LeadIdType` | `filters: SearchLeadFilters!` | No | Search and return the identifiers of a lead. The possible errors that can be raised are: - KT-CT-8920: Search filters are invalid. - KT-CT-1113: Disabled GraphQL field requested. |
| `simpleQuoteLevels` | `[QuoteEstimatimation]` |  | Yes (The 'simpleQuoteLevels' field is deprecated. Migrated to OE Backend API. - Marked as deprecated on 2025-10-27. - Scheduled for removal on or after 2025-11-10.) | Get quote estimation list. |
| `sipsData` | `SIPSData` | `cups: String!, market: String!` | No | Get SIPS (Sistema Información Puntos Suministro) data for a given CUPS. The possible errors that can be raised are: - KT-ES-7820: SIPS data not available for the given supply point. - KT-ES-7821: An unexpected error occurred while attempting to retrieve SIPS data. - KT-CT-1113: Disabled GraphQL field requested. |
| `siteworksRequests` | `CoreSiteworksRequestConnectionTypeConnection` | `ids: [UUID], createdAfter: DateTime, statuses: [RequestStatus], before: String, after: String, first: Int, last: Int` | Yes (The 'siteworksRequests' field is deprecated. Please use getOnSiteJobsRequests instead. - Marked as deprecated on 2026-03-01. - Scheduled for removal on or after 2026-09-01.) | A query to get a subset of Requests. |
| `smartFlexDeviceSupplyPoint` | `SmartFlexDeviceSupplyPointType` | `smartFlexDeviceId: String` | No | The supply point linked to the SmartFlex device. |
| `smartFlexOnboardingWizards` | `[SmartFlexOnboardingWizard!]` | `accountNumber: String!, propertyId: Int, wizardId: ID, includeCancelled: Boolean, includeCompleted: Boolean, isResumable: Boolean` | No | A list of wizards for onboarding devices for an account and property. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. |
| `solarSimulatorQuote` | `SolarSimulationQuote` | `roofSize: Float!, consumption: Int!` | Yes (The 'solarSimulatorQuote' field is deprecated. Migrated to OE Backend API. - Marked as deprecated on 2025-10-27. - Scheduled for removal on or after 2025-11-10.) | Get solar simulator response data. |
| `solarTariff` | `SpecialTariff` |  | No | Send information about the current solar tariff. The possible errors that can be raised are: - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested. |
| `standardisedAddressInfo` | `StandardAddressInfo` | `postcode: String` | No | Get standardised address information from the postcode. The possible errors that can be raised are: - KT-CT-4410: Invalid postcode. - KT-ES-4401: Unexpected Chipiron vendor response. - KT-ES-4402: Error while calling Chipiron vendor. - KT-CT-1113: Disabled GraphQL field requested. |
| `streetTypes` | `[StreetType]` |  | No | Street types. |
| `supplyPoint` | `SupplyPointType` | `externalIdentifier: String!, marketName: String!` | No | Get a supply point by its market specific id. The possible errors that can be raised are: - KT-CT-4722: Supply point readings API not configured. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-4723: Invalid market name provided. - KT-CT-1113: Disabled GraphQL field requested. |
| `supplyPoints` | `SupplyPointConnectionTypeConnection` | `accountNumber: String, portfolioNumber: String, before: String, after: String, first: Int, last: Int` | No | Get list of supply points. |
| `taskResult` | `TaskResult` | `taskId: String!, accountNumber: String!` | No | Get the status of a background task. The possible errors that can be raised are: - KT-CT-10401: Task not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `termsAndConditionsForProduct` | `[TermsAndConditionsType]` | `productCode: String!` | No | Get the active terms and conditions for a market supply product. The possible errors that can be raised are: - KT-CT-8501: No active terms and conditions found for product. - KT-CT-1113: Disabled GraphQL field requested. |
| `thirdPartyViewer` | `ThirdPartyOrganizationType` |  | No | The currently authenticated third party. This field requires the `Authorization` header to be set. |
| `trigger` | `Trigger!` | `triggerId: ID!` | No | Get the details of a published trigger with a given ID. The possible errors that can be raised are: - KT-CT-9904: Trigger not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `userVehicles` | `[UserVehiclesType]` | `accountNumber: String, supportedProvider: ProviderChoices, authentication: AuthenticationInput` | Yes (The 'userVehicles' field is deprecated. Please use 'startSmartFlexOnboarding' instead. - Marked as deprecated on 2025-10-30. - Scheduled for removal on or after 2026-04-30. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/608/) | A list of vehicles available to the user. Note: If the API returns an empty list, there might be a delay between the vehicle being registered in the provider's system, and data being fetched from the vehicle's manufacturer. In such cases, the query should be retried after a few seconds. The possible errors that can be raised are: - KT-CT-4314: Unable to get provider details. - KT-CT-1113: Disabled GraphQL field requested. |
| `validateReferralCode` | `ReferralClaimCodeType` | `value: String!` | No | Validate referral claim code. |
| `vehicleChargingPreferences` | `VehicleChargingPreferencesType` | `accountNumber: String!` | Yes (The 'vehicleChargingPreferences' field is deprecated. Please use 'devices.preferences' instead. - Marked as deprecated on 2024-04-23. - Scheduled for removal on or after 2026-03-01. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/675/) | Vehicle charging preference details. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4339: Your device charging preferences could not be fetched. - KT-CT-1113: Disabled GraphQL field requested. |
| `verificationStatus` | `EmailVerificationStatus` | `email: String!` | No | Check the verification status of a given email address. |
| `viewer` | `EspAccountUserType` |  | No | The currently authenticated user. This field requires the `Authorization` header to be set. |
| `voiceCampaign` | `VoiceCampaignType!` | `campaignId: String!` | No | Get the voice campaign for a given ID. The possible errors that can be raised are: - KT-CT-11501: Voice campaign not found. - KT-CT-1113: Disabled GraphQL field requested. |
| `voiceCampaigns` | `VoiceCampaignConnectionTypeConnection!` | `status: CampaignStatus, campaignType: TypeOfVoiceCampaign, name: String, before: String, after: String, first: Int, last: Int` | No | Get voice campaigns. |
| `vouchersBalanceDetail` | `VouchersBalanceDetail` | `accountNumber: ID!` | No | Query the detail of vouchers balance for an account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4178: No account found with given account number. - KT-CT-1113: Disabled GraphQL field requested. |
| `vouchersForAccount` | `VoucherPurchaseConnectionTypeConnection` | `accountNumber: ID!, redeemableOnly: Boolean!, purchasedFromDate: Date, purchasedBeforeDate: Date, availableFromDate: Date, availableBeforeDate: Date, excludeRefunded: Boolean = false, before: String, after: String, first: Int, last: Int` | No | Query the voucher purchases for an account. |
| `workSchedule` | `WorkScheduleType!` | `identifier: String!` | No | Get the work schedule with the given identifier. The possible errors that can be raised are: - KT-CT-11804: Work schedule not found. - KT-CT-1113: Disabled GraphQL field requested. |

## `QueryComplexityOutputType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `complexityValue` | `Int` |  | No | The complexity of the query. |

## `QuoteComponentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `costs` | `[QuoteCostType]` |  | No | The cost for quoting this product. |
| `createdAt` | `DateTime` |  | No | The date and time when the quote component was created. |
| `identifier` | `ID` |  | No | Identifier of the Quote. |
| `productComponentIdentifier` | `ID` |  | No | Identifier of the Product Component. |
| `quotingParamsInputData` | `[QuotingParamType]` |  | No | The input data used for quoting this product component. |
| `termsAndConditionsS3Urls` | `[TermsAndConditionsS3UrlType]` | `expireIn: Int = 3600` | No | S3 URLs for terms and conditions linked to this quote component. |

## `QuoteCostType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `key` | `String!` |  | No | Name of the cost field. |
| `value` | `QuoteCostUnionType` |  | No | Value of the cost field. |

## `QuoteEstimatimation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `annualConsumption` | `Int!` |  | No |  |
| `consumptionDetails` | `[String!]!` |  | No |  |
| `consumptionLevel` | `String!` |  | No |  |
| `estimates` | `EstimationType` |  | No | The annual consumption estimation for both dual-fuel and electricity only. |

## `QuoteInfo`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `annualConsumption` | `Int` |  | No | Estimated annual consumption for fuel. |
| `annualFee` | `Float` |  | No | Annual fee for fuel. |
| `annualFeeUnits` | `String` |  | No | Annual fee units for fuel. |
| `annualFeeWithTaxes` | `Float` |  | No | Annual fee with taxes for fuel. |
| `monthlyFee` | `Float` |  | No | Monthly fee for fuel. |
| `monthlyFeeUnits` | `String` |  | No | Monthly fee units for fuel. |
| `monthlyFeeWithTaxes` | `Float` |  | No | Monthly fee with taxes for fuel. |
| `prices` | `QuotedProductPrice` |  | No | Product prices. |
| `pricesWithTaxes` | `QuotedProductPrice` |  | No | Product prices. |

## `QuoteRequest`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | The code of the created quote. |
| `id` | `ID!` |  | No | The ID of the quote request. |
| `quotedSupplyPoints` | `[QuotedSupplyPoint]!` |  | No | List of quoted supply points. |

## `QuoteType_`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `createdAt` | `DateTime` |  | No | The date and time when the quote was created. |
| `createdBy` | `ActorType` |  | No | The Actor who created the Quote. |
| `identifier` | `ID` |  | No | Identifier of the Quote. |
| `productOfferingIdentifier` | `ID` |  | No | The product offering identifier this Quote is related to. |
| `quoteComponents` | `[QuoteComponentType]` |  | No | Quote components of this quote. |

## `QuotedAdjustmentMechanism`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `end` | `Date` |  | No | End date of Adjustment mechanism period. |
| `period` | `String` |  | No | Adjustment mechanism month period. |
| `priceMean` | `Float` |  | No | Adjustment mechanism mean. |
| `start` | `Date` |  | No | Start date of Adjustment mechanism period. |
| `units` | `String` |  | No | Adjustment mechanism units. |

## `QuotedOfferingParamsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `offeringComponents` | `[QuotedOfferingParamsType]` |  | No | Quoting components of this quote. |
| `offeringIdentifier` | `ID` |  | No | Product offering identifier. |
| `productComponents` | `[QuotedProductComponentType]` |  | No | Product component data including its quoting parameters. |

## `QuotedProduct`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No | The ID of the quoted product. |
| `monthlyEstimate` | `Int!` |  | No | The estimated monthly cost in cents. |
| `product` | `Product!` |  | No | The product associated with the quoted product. |
| `quoteInfo` | `QuoteInfo` |  | No | Quote info. |

## `QuotedProductComponentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `productCode` | `ID` |  | No | Product code. |
| `quotingParams` | `[QuotingParamType]` |  | No | Quoting parameter definitions for this product. |

## `QuotedProductPrice`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `adjustmentMechanismData` | `QuotedAdjustmentMechanism` |  | No | Adjustment mechanism. |
| `fixedTerm` | `[Float]` |  | No | Fixed term. |
| `fixedTermUnits` | `String` |  | No | Units of fixed term. Same for all terms. |
| `marginTerm` | `Float` |  | No | Margin term quantity. |
| `marginTermUnits` | `String` |  | No | Units of margin term. |
| `surplusRate` | `Float` |  | No | Rate at which solar surplus is compensated. |
| `surplusRateUnits` | `String` |  | No | Units of the surplus rate. |
| `variableTerm` | `[Float]` |  | No | Variable term. |
| `variableTermUnits` | `String` |  | No | Units of variable term. Same for all terms. |

## `QuotedSupplyPoint`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No | The ID of the quoted supply point. |
| `marketName` | `String!` |  | No | The market this supply point belongs to. |
| `quotedProducts` | `[QuotedProduct]!` |  | No | Details of all products quoted for this supply point. |

## `QuotingParamType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `choices` | `[String]` |  | No | Choices of the quoting parameter if present. |
| `name` | `String` |  | No | Name of the quoting parameter. |
| `source` | `String` |  | No | Source of the quoting parameter. |
| `type` | `String` |  | No | Type of the quoting parameter. |
| `value` | `String` |  | No | Value of the quoting parameter. |

## `RateGroupEligibilityConfigurationType`

Represents a rate group eligibility term of in a contract. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `schedules` | `[RateGroupEligibilityScheduleType]` |  | No | A list of rate group eligibility schedules associated with the contract. |
| `timeSeriesSpecificationSchedules` | `[TimeSeriesSpecificationEligibilityScheduleType]` |  | No | A list of time series specification eligibility schedules associated with the contract. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `RateGroupEligibilityPeriodType`

Represents a period with a start and optional end date. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `end` | `DateTime` |  | No | The end date and time of the period. |
| `start` | `DateTime` |  | No | The start date and time of the period. |

## `RateGroupEligibilityScheduleType`

Represents a schedule for rate group eligibility within a contract. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `effectivePeriod` | `RateGroupEligibilityPeriodType` |  | No | The period during which this eligibility is effective. |
| `isEligible` | `Boolean` |  | No | Indicates if the rate group is eligible. |
| `productCode` | `String` |  | No | The product code associated with the rate group. |
| `rateGroupCode` | `String` |  | No | The rate group code. |

## `RateGroupPrices`

Rate group prices for a product.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `prices` | `[PriceForStream!]!` |  | No | The prices for the rate group. |
| `rateGroup` | `String!` |  | No | The rate group code. |

## `ReactivateCollectionProcessRecord`

Reactivate a Collection Process Record that was previously activated. Unlike UpdateCollectionProcessRecordToActive, this mutation does not require or update the external_reference field. Use this when reactivating a collection process that already has an external_reference set from its initial activation. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11217: Invalid collection process record status for reactivation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessReactivated` | `ReactivateCollectionProcessRecordOutputType` |  | No | The reactivated collection process record. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `ReactivateCollectionProcessRecordOutputType`

Output for reactivating a Collection process Record.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `number` | `String` |  | No | The number of the collection process record. |
| `status` | `CollectionProcessRecordStatusTypes` |  | No | The current status of the collection process record. |

## `Reading`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `intervalEnd` | `DateTime` |  | No | The exclusive end of this reading's interval. |
| `intervalStart` | `DateTime` |  | No | The inclusive start of this reading's interval. |
| `quality` | `String` |  | No | The quality of this reading if applicable. |
| `source` | `String` |  | No | The source of this reading if applicable. |
| `units` | `String` |  | No | This reading's units. |
| `value` | `Decimal` |  | No | The recorded value for this reading. |

## `Readings`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `exportReadings` | `ExportReadingsConnection` | `before: String, after: String, first: Int, last: Int` | No | Readings representing outgoing utility flow e.g., solar generation. |
| `importReadings` | `ImportReadingsConnection` | `before: String, after: String, first: Int, last: Int` | No | Readings representing incoming utility flow e.g., usage or consumption.. |

## `RecordDepositAgreementAccepted`

Record the customer's acceptance of a deposit agreement. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isRecorded` | `Boolean` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RecordFailedPayment`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `noticeBatchIdentifier` | `String!` |  | No | The unique identifier of the notice batch created from the input. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RecordPendingPayment`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `noticeBatchIdentifier` | `String!` |  | No | The unique identifier of the notice batch created from the input. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RecordSuccessfulPayment`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `noticeBatchIdentifier` | `String!` |  | No | The unique identifier of the notice batch created from the input. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RectangularButtonType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `buttonAction` | `ActionType!` |  | No | The action to perform when the button is pressed. |
| `buttonStyle` | `ButtonStyle` |  | No | The button style. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `title` | `String!` |  | No | Title text of the button. |
| `typename` | `String` |  | No | The name of the object's type. |
| `variant` | `ButtonVariance` |  | No | Colour style of button eg. filled, outlined, text_only. |

## `RedeemLoyaltyPointsForAccountCredit`

Redeem Loyalty Points as account credit. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9201: No Loyalty Point ledger found for the user. - KT-CT-9202: Loyalty Points adapter not configured. - KT-CT-9203: No ledger entries for the ledger. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9206: Indivisible points. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9209: Negative Loyalty Points balance. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `pointsRedeemed` | `Int` |  | No | The number of loyalty points that were redeemed. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RedeemReferralClaimCode`

The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6724: Referral claim code not found. - KT-CT-6725: Referral claim code redeeming error. - KT-CT-6726: Referral claim code has already been redeemed. - KT-CT-6727: Referral claim code is not available. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean!` |  | No | Whether or not the request was successful. |

## `ReferralClaimCodeType`

Referral claim code is a way of claiming promotional benefit coming from the partner-reward referral schemes.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountReferral` | `ReferralType` |  | No | Account referral associated with the claim code. |
| `createdAt` | `DateTime` |  | No | Datetime when claim code was generated. |
| `id` | `Int` |  | No | Id of claim code instance. |
| `isValid` | `Boolean` |  | No | Whether the referral claim code is valid and available for use. |
| `referralScheme` | `ReferralSchemeType` |  | No | Referral scheme claim code belongs to. |
| `value` | `String` |  | No | Value of claim code. |

## `ReferralConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[ReferralConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `referringUserTotalPaymentAmount` | `Int!` |  | No | Total payment amount given to the referring account in the smallest unit. of the client's currency. If you filter the referrals by `status`, this will only return the total payment amount of referrals with the specified status. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `ReferralConnectionTypeEdge`

A Relay edge containing a `ReferralConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `ReferralType` |  | No | The item at the end of the edge |

## `ReferralSchemeType`

A referral scheme is a way for one account to earn a reward for referring another. This is achieved by the referred account using a url (provided by the referring account) to sign up.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `canBeReferred` | `Boolean` |  | No | Whether the current account is eligible to be referred under this scheme. |
| `code` | `String` |  | No | The unique code for the scheme. |
| `combinedRewardAmount` | `Int` |  | No | The reward amount received by the referrer and the referee combined. |
| `isUsageAtCapacity` | `Boolean` |  | No | True if the the scheme has limit of uses, and if the usage is at capacity. |
| `loyaltyPointsBonus` | `Int` |  | No | The number of loyalty points to be awarded to the referrer in addition to the reward amount. |
| `maxRecurrence` | `Int` |  | No | Max number of times this referral code can be credited to a given account. |
| `referralDisplayUrl` | `String` |  | No | A referral url for display purposes. |
| `referralUrl` | `String` |  | No | A fully qualified url give people to create accounts referred by this scheme. |
| `referredRewardAmount` | `Int` |  | No | The reward amount received by the referred party. |
| `referrerFamilyName` | `String` |  | Yes (The 'referrerFamilyName' field is deprecated. Only make use of the referrerGivenName for privacy reasons. - Marked as deprecated on 2022-11-07. - Scheduled for removal on or after 2023-01-07.) | The family name of the person making the referral. |
| `referrerGivenName` | `String` |  | No | The given name of the person making the referral. |
| `referrerRewardAmount` | `Int` |  | No | The reward amount received by the referrer. |
| `schemeType` | `String` |  | No | Scheme type of the referral scheme. |

## `ReferralSchemeTypes`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `business` | `ReferralSchemeType` |  | No | A business scheme type. |
| `domestic` | `ReferralSchemeType` |  | No | A domestic scheme type. |
| `friendsAndFamily` | `ReferralSchemeType` |  | Yes (The 'friendsAndFamily' field is deprecated. Please use domestic instead. - Marked as deprecated on 2020-03-05. - Scheduled for removal on or after 2024-01-01.) | A friends and family scheme type. |

## `ReferralType`

Details of an account referral

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The referral code. |
| `combinedPaymentAmount` | `Int` |  | No | The payment amount in the smallest unit of the clients currency received by the referrer and the referee combined. |
| `id` | `ID!` |  | No |  |
| `paymentDate` | `Date` |  | No | The date when the payment was made. |
| `paymentStatus` | `String` |  | No | The status of the payment. |
| `referredUserJoinDate` | `DateTime` |  | No | The date the referred user joined. |
| `referredUserName` | `String` |  | No | The name of the referred user. |
| `referredUserPaymentAmount` | `Int` |  | No | Payment amount given to the referred account in the smallest unit of the client's currency. |
| `referringUserPaymentAmount` | `Int` |  | No | Payment amount given to the referring account in the clients fractional currency unit. |
| `schemeType` | `ReferralSchemeTypeChoices` |  | No | The type of reward scheme. |

## `RefreshToken`

An opaque token that can be used to renew a Kraken Token.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `expiryDt` | `DateTime!` |  | No | The datetime when the token will expire. |
| `isValid` | `Boolean` |  | No |  |
| `key` | `String!` |  | No |  |

## `Refund`

A refund to the customer from the energy supplier.

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

## `RefundPayment`

The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-3928: Idempotency key used for another repayment request. - KT-CT-3929: The payment is not in a refundable state. - KT-CT-3933: Refund amount greater than payment amount. - KT-CT-3937: Payment not eligible for refund. - KT-CT-3938: Partial refund not allowed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `repayment` | `AccountRepaymentType` |  | No | The repayment for the requested refund. |

## `RefundPaymentRequestType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int` |  | No | The amount of money requested. |
| `payment` | `AccountPaymentType` |  | No | The payment which is being refunded. |
| `reasonCode` | `String` |  | No | Internal code for the reason the refund is being requested. |
| `requestId` | `ID` |  | No | The ID of the refund request. |
| `status` | `RepaymentRequestStatus` |  | No | The current status of the refund request. |

## `RefundRequestConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[RefundRequestConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `RefundRequestConnectionTypeEdge`

A Relay edge containing a `RefundRequestConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `RefundPaymentRequestType` |  | No | The item at the end of the edge |

## `RegenerateSecretKey`

Regenerate the user's API key.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `key` | `String!` |  | No | The generated key value, which is only ever available once (here). |
| `viewer` | `EspAccountUserType` |  | No | The currently authenticated user. |

## `RegisterEVChargerLead`

Sends a EV Charger Lead to Chipiron for it to save it in Zoho. The possible errors that can be raised are: - KT-ES-7803: The request to Chipiron was incomplete or malformed. - KT-ES-7804: The request to Chipiron caused a conflict - might you be trying to create a duplicate? - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean` |  | No | True if the lead was registered successfully. |

## `RegisterLeadFlowStatusEvent`

The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RegisterOpportunityFlowStatusEvent`

The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RegisterPhoneLead`

Creates an Account instance. The possible errors that can be raised are: - KT-ES-8910: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `partnerReference` | `String!` |  | No | Lead's partner reference. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `source` | `String` |  | No | Lead's source. |
| `telephoneLead` | `String!` |  | No | Lead's telephone number. |

## `RegisterPushNotificationBinding`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `pushNotificationBinding` | `PushNotificationBindingType` |  | No |  |

## `RegistersConnection`

Pagination for device registers.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[RegistersEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `RegistersEdge`

A Relay edge containing a `Registers` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `DeviceRegister` |  | No | The item at the end of the edge |

## `Reminder`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `assigneeId` | `ID` |  | No | The id of the user responsible for completing the reminder. |
| `assigneeTeamId` | `ID` |  | No | The id of the team responsible for completing the reminder. |
| `assigneeTeamName` | `String` |  | No | The name of the team responsible for completing the reminder. |
| `assigneeUsername` | `String` |  | No | The username of the user responsible for completing the reminder. |
| `content` | `String` |  | No | Reminder content. |
| `createdAt` | `DateTime` |  | No | The date and time the account reminder was created. |
| `dueAt` | `DateTime` |  | No | When the reminder is due. |
| `id` | `Int` |  | No | The unique ID of the reminder. |
| `isKrakenManaged` | `Boolean` |  | No | If the reminder is managed by Kraken. |
| `reminderTypeName` | `String` |  | No | The reminder type name. |
| `reopenInkConversation` | `Boolean` |  | No | Reopen ink conversation. |

## `RemoveCampaignFromAccount`

The possible errors that can be raised are: - KT-CT-7424: Failed to remove campaign from account. - KT-CT-7426: The account is not part of the given campaign. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `campaignRemoved` | `Boolean` |  | No | Whether the campaign was successfully removed from the account. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RemoveCampaignItems`

The possible errors that can be raised are: - KT-CT-11501: Voice campaign not found. - KT-CT-11502: Cannot remove items from multiple campaigns at once. - KT-CT-11505: Voice campaign item not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `campaignItems` | `[VoiceCampaignItemType]` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RemoveItemsFromRiskList`

Remove existing items from risk list. The possible errors that can be raised are: - KT-CT-12106: Risk list item removal failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `riskIdentifiers` | `[RiskListItemType]` |  | No | List of successfully removed risk identifiers. |

## `RemovePropertyFromHierarchy`

Remove a property from a hierarchy. This operation is idempotent - if the property is not in the hierarchy, it will succeed without error. When a property is removed, its descendants are reparented to the removed property's parent. If removing a root node, its children become new root nodes. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `property` | `PropertyType` |  | No | The property that was removed from the hierarchy. |

## `RepaymentInterventionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `outcome` | `String` |  | No | The repayment intervention outcome. |
| `reason` | `String` |  | No | The repayment intervention reason. |

## `RepaymentRequestConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[RepaymentRequestConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `RepaymentRequestConnectionTypeEdge`

A Relay edge containing a `RepaymentRequestConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `RepaymentRequestType` |  | No | The item at the end of the edge |

## `RepaymentRequestType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Int` |  | No | The amount of money requested. |
| `instruction` | `PaymentInstructionType` |  | No | The payment instruction, if any, associated with the repayment request. |
| `method` | `RepaymentMethod` |  | No | The method by which the money will be transferred to the customer. |
| `reasonCode` | `String` |  | No | Classifier code for repayment reason. |
| `requestId` | `String` |  | No | The ID of the repayment request. |
| `status` | `RepaymentRequestStatus` |  | No | The current status of the repayment request. |

## `RequestDoubleOptIn`

Request a double opt in for a consent. This mutation will create a consent with a value of PENDING and publish a double opt-in requested transactional messaging trigger. The possible errors that can be raised are: - KT-CT-9019: Invalid input. - KT-CT-9018: Account not found. - KT-CT-1111: Unauthorized. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-9023: Consent already accepted. - KT-CT-1199: Too many requests. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `consent` | `ConsentType` |  | No | The consent that was created or updated. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RequestPasswordResetOutputType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `email` | `String` |  | No | The email that requested a password reset email. |
| `userNumber` | `String` |  | No | The number of the user that requested a password reset email. |

## `RequestPrintedBill`

Request an issued bill to be printed and (re)posted to billing address of the account. The possible errors that can be raised are: - KT-CT-3824: Unauthorized. - KT-CT-9705: The billing document has not been issued. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean` |  | No | Whether the request was successful. |

## `RequestRefundEligibilityType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `canRequestRefund` | `Boolean!` |  | No | Whether the account can request a refund. |
| `reason` | `String` |  | No | The reason why a refund cannot be requested. |

## `RequestRepaymentOutputType`

Output for creating a repayment request.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `requestId` | `String` |  | No | The ID of the repayment request. |
| `status` | `RepaymentRequestStatus` |  | No | The current status of the repayment request. |

## `ResetPasswordMutationPayload`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientMutationId` | `String` |  | No |  |
| `errors` | `[SerializerFieldErrorsType]` |  | No |  |

## `ResetUserPasswordOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `failureCodes` | `[String]` |  | Yes (The 'failureCodes' field is deprecated. Please handle the KT-CT-5450 error and inspect the `validationErrors[].code` extension instead. Note that the KT-CT-5450 error will not be raised if you request any of the `failureCodes`, `failureReasons`, or `passwordUpdated` fields. - Marked as deprecated on 2025-04-07. - Scheduled for removal on or after 2025-10-04.) | A list of codes of which password validation the new password failed against if applicable. One of: - `password_too_short` - `password_too_common` - `password_reused` - `password_matches_current` - `password_has_too_few_numeric_characters` - `password_has_too_few_special_characters` - `password_has_too_few_lowercase_characters` - `password_has_too_few_uppercase_characters` - `password_contains_account_number` - `password_contains_part_of_email_address` |
| `failureReasons` | `[String]` |  | Yes (The 'failureReasons' field is deprecated. Please handle the KT-CT-5450 error and inspect the `validationErrors[].message` extension instead. Note that the KT-CT-5450 error will not be raised if you request any of the `failureCodes`, `failureReasons`, or `passwordUpdated` fields. - Marked as deprecated on 2025-04-07. - Scheduled for removal on or after 2025-10-04.) | A list of messages of which password validations the new password failed against if applicable. |
| `passwordUpdated` | `Boolean` |  | Yes (The 'passwordUpdated' field is deprecated. Please handle the KT-CT-5450 error instead. Note that the KT-CT-5450 error will not be raised if you request any of the `failureCodes`, `failureReasons`, or `passwordUpdated` fields. - Marked as deprecated on 2025-04-07. - Scheduled for removal on or after 2025-10-04.) | True if the password update was successful, false otherwise. |
| `userId` | `ID!` |  | No | The ID of the user whose password was changed. |

## `ResumeCollectionProcess`

Manually resume a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11215: Unable to resume, collection process is not paused. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessResumed` | `ResumeCollectionProcessOutput` |  | No | Collection process resume output. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `ResumeCollectionProcessOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `pauseRecords` | `[CollectionProcessPauseStatusRecord]` |  | No | Pause records on the collection process. |

## `ResumeDeviceControl`

Resume control of a device after having been away from home. This is so that the device can be charged again according to the set preferences. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4359: Unable to resume device control. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `KrakenFlexDeviceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RevokeAgreement`

The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1501: Agreement not found. - KT-CT-1502: Billed agreements cannot be revoked. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | Account responsible for the revoked agreement. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RevokeContractOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contract` | `Contract` |  | No | The contract revoked. |

## `RevokeUserAccessFromBusiness`

The possible errors that can be raised are: - KT-CT-5463: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-13501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `RewardType`

A reward is based on a scheme that an account has applied for in order to be eligible for a discount. Examples can include signup, promo, or partner codes that were applied to an account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The referral code. |
| `id` | `ID!` |  | No |  |
| `paymentDate` | `Date` |  | No | The date when the payment was made. |
| `paymentStatus` | `ReferralStatusChoices` |  | No | The status of the reward payment. |
| `rewardAmount` | `Int` |  | No | Reward amount given to the account in the smallest unit of the clients currency. |
| `schemeType` | `ReferralSchemeTypeChoices` |  | No | The type of reward scheme. |

## `RichAddressType`

A postal address. This data model is based on the structure used by Google's [libaddressinput library](https://github.com/google/libaddressinput)&mdash;so you can use it, or other libraries that use its data model and reference data, to accept input. All fields can be blank, except for ``country`` which must always be supplied. If you only need the address in a single string, use the ``asString`` property. If you need the address as a list of lines, use the ``asString`` property, then use ``.splitlines()`` (or your programming language's equivalent) on the resulting value.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `administrativeArea` | `String` |  | No | Top-level administrative subdivision, e.g. US state, AU state/territory, NZ, region, IT region, JP prefecture. ### `AU`: Australia This must be one of `NSW`, `VIC`, `QLD`, `TAS`, `ACT`, `SA`, `NT`, `WA`. For addresses not within these locations, use the value that Australia Post uses, e.g. `ACT` for the Jervis Bay Territory or `WA` for Christmas Island. |
| `asString` | `String` | `showCountry: Boolean = true, showName: Boolean = true, showPostalCode: Boolean = true` | No | The entire formatted address represented as a single string, as it would be written on an envelope. The formatting of this field may vary according to the country of the address (which may not match this Kraken installation's home country). It may also change if we update our address-formatting code or if our understanding of the correct formatting for a given country changes. Avoid parsing individual components of an address out of this field's value; use the other fields on this type instead. |
| `country` | `String` |  | No | ISO 3166-1 alpha-2 code of the country this address belongs to, e.g. `AU`, `GB`, `NZ`. |
| `deliveryPointIdentifier` | `String` |  | No | Identifier used by the local postal service for this address, e.g. AU DPID, GB postcode + Delivery Point Suffix, US Zip-9 + Delivery Point. This is the value that gets encoded in the barcode printed on the envelope by large-volume bulk mail providers. |
| `dependentLocality` | `String` |  | No | UK dependent localities, or neighbourhoods or boroughs in some other locations. |
| `locality` | `String` |  | No | City or town portion of an address, e.g. US city, AU suburb/town, NZ suburb and city/town, IT comune, UK post town. |
| `name` | `String` |  | No | A personal name. |
| `organization` | `String` |  | No | The name of a business or organisation. |
| `postalCode` | `String` |  | No | Postal code (ZIP code in the US). |
| `sortingCode` | `String` |  | No | Sorting code, e.g. FR CEDEX code. This field is not used in many countries. |
| `streetAddress` | `String` |  | No | The 'street address' component. This value can (and often will) contain newline characters when appropriate. In some cases, data may appear in this field instead of the below fields; e.g. a UK post town name may appear here instead of in the `dependent_locality` field. This happens when data has been migrated from a legacy format, and that format had insufficient metadata to determine the appropriate field. If `structured_street_address` is also set, the value of this field will be a string generated from that value. |
| `structuredStreetAddress` | `GenericScalar` |  | No | The 'street address' component, in a structured format. This field stores the same value as `street_address`, but with more detail; for instance, instead of `123 Example Street` it might be `{'street_number': '123', 'street_name': 'Example', 'street_type': 'Street'}`. In many cases this will be blank; we only use this field for Krakens where we need to supply this level of granularity to some third-party service, like a bulk mail provider. The exact structure of this value depends on the country _of the address_, which is not necessarily the same as the country this Kraken is configured to serve. For addresses outside of the countries listed below, this field will be left blank. ### `AU`: Australia The following keys may be present; all are optional. All keys have string values, and their meaning is the same as their aseXML counterparts. (Note that, unlike aseXML, all keys are provided at the top level, rather than being nested.) - `flat_or_unit_type` - `flat_or_unit_number` - `floor_or_level_type` - `floor_or_level_number` - `building_or_property_name` - `location_descriptor` - `lot_number` - `house_number_1` - `house_number_suffix_1` - `house_number_2` - `house_number_suffix_2` - `street_name` - `street_type` - `street_suffix` - `postal_delivery_type` - `postal_delivery_number_prefix` - `postal_delivery_number_value` - `postal_delivery_number_suffix` ### `JP`: Japan The following keys may be present; all are optional. If keys are empty, they may be omitted from the response entirely. - `chome` - `banchi` - `go` - `edaban` - `kana_building_name` - `kanji_building_name` - `building_number` - `room_number` - `address_code` - `physical_location_identifier` - `kana_company_name` - `kanji_company_name` ### `NZ`: New Zealand The following keys may be present; all are optional. If keys are empty, they may be omitted from the response entirely. - `flat_or_unit_type` - `flat_or_unit_number` - `floor_or_level_type` - `floor_or_level_number` - `property_name` - `building_name` - `house_number_1` - `house_number_suffix_1` - `house_number_2` - `house_number_suffix_2` - `street_prefix` - `street_name` - `street_type` - `street_suffix` - `rural_delivery_number` - `mailtown` - `postal_delivery_type` - `postal_delivery_location` - `postal_delivery_number_prefix` - `postal_delivery_number_value` - `postal_delivery_number_suffix` |

## `RiskListItemType`

Represents the result of importing/removing risk identifiers into the risk list with detailed information.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `riskIdentifierId` | `ID` |  | No | The unique identifier of the edited risk identifier. |

## `RoutingAttributeType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `category` | `String!` |  | No | The category of the attribute (LANGUAGE, OPERATIONS_GROUP, SKILL). |
| `friendlyName` | `String!` |  | No | Human-readable name for the attribute. |
| `isActive` | `Boolean!` |  | No | Whether this attribute is currently active and can be used for routing. |
| `ref` | `String!` |  | No | The reference string used to identify this attribute (e.g., SKILL.ENERGY, LANGUAGE.ENGLISH). |
| `subcategory` | `String` |  | No | Optional subcategory (e.g., TEAM, LOCATION). |

## `RunAgreementRollover`

The possible errors that can be raised are: - KT-CT-13705: Agreement rollover not found. - KT-CT-13706: Agreement rollover has an invalid status for this operation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreementRollover` | `AgreementRolloverType` |  | No | The executed agreement rollover. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SIPSElectricityData`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientData` | `GenericScalar` |  | No | Client-specific data fields. |
| `contractedPowerWP1` | `Float` |  | No | Contracted power in Watts for period 1. |
| `contractedPowerWP2` | `Float` |  | No | Contracted power in Watts for period 2. |
| `contractedPowerWP3` | `Float` |  | No | Contracted power in Watts for period 3. |
| `contractedPowerWP4` | `Float` |  | No | Contracted power in Watts for period 4. |
| `contractedPowerWP5` | `Float` |  | No | Contracted power in Watts for period 5. |
| `contractedPowerWP6` | `Float` |  | No | Contracted power in Watts for period 6. |
| `cups` | `String!` |  | No | The supply point CUPS identifier. |
| `currentAtrTariffCode` | `String` |  | No | Current ATR tariff code in force. |
| `monthlyConsumptions` | `[SIPSElectricityMonthlyConsumption]` |  | No | Monthly consumption data. |
| `postalCode` | `String` |  | No | Supply point postal code. |

## `SIPSElectricityMonthlyConsumption`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `activeEnergyConsumptionWhP1` | `Float` |  | No | Active energy consumption in Watt hour for period 1. |
| `activeEnergyConsumptionWhP2` | `Float` |  | No | Active energy consumption in Watt hour for period 2. |
| `activeEnergyConsumptionWhP3` | `Float` |  | No | Active energy consumption in Watt hour for period 3. |
| `endDate` | `Date` |  | No | End date of the consumption month. |
| `startDate` | `Date` |  | No | Start date of the consumption month. |

## `SIPSGasData`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cups` | `String!` |  | No | The supply point CUPS identifier. |
| `currentTollCode` | `String` |  | No | Current toll code in force. |
| `monthlyConsumptions` | `[SIPSGasMonthlyConsumption]` |  | No | Monthly consumption data. |
| `postalCode` | `String` |  | No | Supply point postal code. |

## `SIPSGasMonthlyConsumption`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `consumptionWhP1` | `Float` |  | No | Consumption in Watt hour for period 1. |
| `consumptionWhP2` | `Float` |  | No | Consumption in Watt hour for period 2. |
| `endDate` | `Date` |  | No | End date of the consumption month. |
| `startDate` | `Date` |  | No | Start date of the consumption month. |

## `SMSEventType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `eventType` | `String!` |  | No |  |
| `id` | `ID!` |  | No | The ID of the object |
| `message` | `SMSMessageType` |  | No | SMS message of the SMS event. |
| `occurredAt` | `DateTime!` |  | No |  |

## `SMSMessageType`

Represents a SMS communication.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | The account found. |
| `attachments` | `[AttachmentType]` |  | No | Attachments of the message. |
| `id` | `ID!` |  | No | The ID of the SMS. |
| `recipient` | `String` |  | No | SMS recipient. |
| `sender` | `String` |  | No | SMS sender. |
| `sentAt` | `DateTime` |  | No | The date and time the SMS was sent. |
| `textBody` | `String` |  | No | SMS body. |

## `SalesChannelType`

A sales channel.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The sales channel code. |
| `description` | `String` |  | No | The sales channel description. |
| `hierarchicalName` | `String` |  | No | The hierarchical name of the sales channel. |
| `name` | `String` |  | No | The name of the sales channel. |

## `SalesFunnel`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The code of this sales funnel. |
| `collections` | `[Collection]` |  | No | The collections of this sales funnel. |
| `funnelType` | `FunnelTypeChoices` |  | No | The type of this sales funnel. |
| `name` | `String` |  | No | The name of this sales funnel. |
| `rules` | `[SalesFunnelRule]` |  | No | The rules of this sales funnel. |
| `stages` | `[SalesFunnelStage]` |  | No | The stages of this sales funnel, in order. |
| `status` | `FunnelStatusChoices` |  | No | The status of this sales funnel. |
| `uncollectedFields` | `[FunnelField]` |  | No | Fields not associated with a collection. |

## `SalesFunnelRule`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `funnelCode` | `String!` |  | No | The code of the funnel. |
| `productOffering` | `OfferingType` |  | No | The product offering of the rule. |
| `productOfferingIdentifier` | `String!` |  | No | The identifier of the product offering of the rule. |
| `salesChannel` | `String!` |  | No | The code of the sales channel of the rule. |

## `SalesFunnelStage`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | The per-funnel unique code for this stage. |
| `name` | `String!` |  | No | The human-readable name for this stage. |
| `order` | `Int` |  | No | The order of the stage. |

## `ScheduleQuoteFollowUp`

Schedule a quote follow up message to the provided recipient. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4632: Invalid recipient information. - KT-CT-4633: Mutation not enabled in this environment. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean!` |  | No | Whether the message was scheduled successfully. |

## `ScheduledTransactionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `action` | `String` |  | No | Whether the scheduled transaction is a 'charge' or a 'credit'. |
| `ancillaryData` | `JSONString` |  | No | Additional data that is consumed and associated with the scheduled transaction. |
| `displayNote` | `String` |  | No | Optional short note about the scheduled transaction for customer display. |
| `grossAmount` | `BigInt` |  | No | The gross amount of the scheduled transaction. |
| `internalNote` | `String` |  | No | Optional short note about the scheduled transaction for internal use. |
| `ledgerNumber` | `String` |  | No | The ledger the scheduled transaction is for. |
| `metadata` | `JSONString` |  | No | Any extra data that is associated with scheduled transaction. |
| `netAmount` | `BigInt` |  | No | The net amount of the scheduled transaction. |
| `postedAfter` | `DateTime` |  | No | The datetime after which the scheduled transaction can be added to the ledger. |
| `reason` | `String` |  | No | The reason why the scheduled transaction is added to the account. |
| `salesTaxAmount` | `BigInt` |  | No | The tax amount of the scheduled transaction. |
| `salesTaxRate` | `Decimal` |  | No | The tax rate of the scheduled transaction. |

## `ScreenActionType`

An action which calls another backend screen via its screen id.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `allowBack` | `Boolean!` |  | No | Whether to allow returning to the original caller screen. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `params` | `[BackendScreenParam]!` |  | No | Map of the parameters (key-value pairs) to pass to the next backend screen. |
| `screenId` | `String!` |  | No | The ID of the screen to navigate to. |
| `typeName` | `String` |  | No | The name of the action object's type. |
| `typename` | `String` |  | No | The name of the object's type. |

## `SectionType`

A section containing a list of cards or carousel items

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `content` | `SectionContent!` |  | No | The content of the section. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `order` | `Int!` |  | No | The order of the section. |
| `typename` | `String` |  | No | The name of the object's type. |

## `SegmentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `name` | `String!` |  | No | The segment name. |

## `SelectChargePointMake`

Options for selecting a charge point's make from a list of options.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SelectChargePointMakeForSmartFlexOnboarding`

Complete the select charge point make step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `SelectChargePointMakeListItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `chargePointMake` | `ChargePointVariantType` |  | No | The make of the charge point, e.g. myenergi. |
| `id` | `ID` |  | No | A unique identifier for this list item. |

## `SelectChargePointVariant`

Options for selecting a charge point's variant from a list of options.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SelectChargePointVariantForSmartFlexOnboarding`

Complete the select charge point variant step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `SelectChargePointVariantListItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `chargePointVariant` | `ChargePointVariantType` |  | No | The model variant of the charge point, e.g. Zappi. |
| `id` | `ID` |  | No | A unique identifier for this list item. |

## `SelectDeviceType`

A type where the user must select the type of device to onboard.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SelectDeviceTypeForSmartFlexOnboarding`

Select the type of device to start the onboarding process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `SelectDeviceTypeListItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this list item. |
| `label` | `String` |  | No | The device type, e.g. Electric Vehicle. |

## `SelectFromListForSmartFlexOnboarding`

Select from a list of options presented (in a step that inherits from SelectFromList). The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `SelectInverterMake`

Options for selecting an inverter's make from a list of options.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SelectInverterMakeForSmartFlexOnboarding`

Complete the select inverter make step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `SelectInverterMakeListItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this list item. |
| `inverterMake` | `InverterVariantType` |  | No | The make (manufacturer) of the inverter. |

## `SelectProducts`

Mark chosen quoted products for quoted supply points on quote request as selected. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4634: Quoted product with given id not found. - KT-CT-4626: No product selected for the given quote code. - KT-CT-4635: Missing a quoted product for at least one quoted supply point on the quote request. - KT-CT-4636: Quoted product not linked to a product. - KT-CT-4646: Attempted to select multiple products for the same quoted supply point. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean!` |  | No | Whether we successfully marked the chosen quoted products as selected. |

## `SelectSessionDevice`

A type where the user must select a device from a list of session devices.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SelectSessionDeviceListItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this list item. |
| `sessionDevice` | `SessionDeviceType` |  | No | A device associated with the onboarding session. |

## `SelectUserVehicle`

Options for selecting a user's vehicle from a list of options.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SelectUserVehicleForSmartFlexOnboarding`

Complete the select user vehicle step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `SelectUserVehicleListItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this list item. |
| `userVehicle` | `ElectricVehicleType` |  | Yes (The 'userVehicle' field is deprecated. Please use 'SelectUserVehicleListItem.vehicle' instead. - Marked as deprecated on 2025-04-10. - Scheduled for removal on or after 2025-07-10.) | The selected electric vehicle when multiple vehicles were available. |
| `vehicle` | `VehicleInformationType` |  | No | A vehicle associated with the user's OEM account. |

## `SelectVehicleMake`

Options for selecting a vehicle's make from a list of options.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SelectVehicleMakeForSmartFlexOnboarding`

Complete the select vehicle make step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `SelectVehicleMakeListItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this list item. |
| `vehicleMake` | `ElectricVehicleType` |  | No | The make of the electric vehicle make, e.g. Tesla. |

## `SelectVehicleOrChargePoint`

A step to prompt users to select between their vehicle or charge point.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `selectedIntegration` | `SelectIntegrationChoices` |  | No |  |

## `SelectVehicleVariant`

Options for selecting a vehicle's variant from a list of options.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `options` | `[SmartFlexListItemInterface]` |  | No | The options the user can select. |
| `selectedOptionId` | `ID` |  | No | The ID of the option that has been selected, if any. |

## `SelectVehicleVariantForSmartFlexOnboarding`

Complete the select vehicle variant step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `SelectVehicleVariantListItem`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this list item. |
| `vehicleVariant` | `ElectricVehicleType` |  | No | The model variant of the electric vehicle, e.g. Model Y. |

## `SelectedProductType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | The selected product code. |
| `displayName` | `String` |  | No | The selected product display name. |

## `SendOfferQuoteSummary`

Trigger the sending of an offer quote summary to all active account users. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4178: No account found with given account number. - KT-CT-12407: The offer group does not contain an accepted offer. - KT-CT-5518: Account user not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean!` |  | No | Whether the triggering of the offer quote summary was successful. |

## `SendQuoteSummary`

Trigger the sending of a quote summary to the provided recipient. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4178: No account found with given account number. - KT-CT-4632: Invalid recipient information. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean!` |  | No | Whether the triggering of the quote summary was successful. |

## `SendVerificationEmail`

The possible errors that can be raised are: - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `verificationStatus` | `Boolean` |  | No | If the verification email was sent. |

## `SerializerErrorType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No |  |
| `message` | `String` |  | No |  |

## `SerializerFieldErrorsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `errors` | `[ErrorTypeUnion!]` |  | No |  |
| `field` | `String` |  | No |  |

## `SessionDeviceType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `String` |  | No | A unique session device identifier. |
| `make` | `String` |  | No | The make (manufacturer) of the device. |
| `model` | `String` |  | No | The model of the device. |
| `name` | `String` |  | No | The name of the device. |

## `SetLoyaltyPointsUser`

Set the Loyalty Points user for the account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-9214: Couldn't assign user loyalty points role. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `newLoyaltyPointsUserId` | `String` |  | No | ID of the new Loyalty Points user. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SetOpportunityOutcome`

The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String` |  | No | Success message for now. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SetPaymentPreference`

Choose how automatic payments will be collected. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3967: Payment method is not valid. - KT-CT-3968: Preference cannot be set this soon. - KT-CT-3969: Preferences must change on a specific day of the week for weekly schedules. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SetUpDirectDebitInstruction`

The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3940: Invalid data. - KT-CT-5415: Account user not found. - KT-CT-11103: Business not found. - KT-CT-3971: Instruction owners are not valid. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `paymentInstruction` | `DirectDebitInstructionType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SetUpDirectDebitInstructionForBusiness`

The possible errors that can be raised are: - KT-CT-3940: Invalid data. - KT-CT-3956: Temporary error occurred. - KT-CT-11107: Unauthorized. - KT-CT-3948: Could not set up direct debit instruction. - KT-CT-3971: Instruction owners are not valid. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `paymentInstruction` | `DirectDebitInstructionType` |  | No | The created direct debit instruction. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SetUpDirectDebitInstructionFromStoredDetails`

The possible errors that can be raised are: - KT-CT-3956: Temporary error occurred. - KT-CT-3948: Could not set up direct debit instruction. - KT-CT-3971: Instruction owners are not valid. - KT-CT-5415: Account user not found. - KT-CT-11103: Business not found. - KT-CT-4123: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `paymentInstruction` | `DirectDebitInstructionType` |  | No | The payment instruction that was created from stored details. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SetVehicleChargingPreferences`

Allow customers to set/update their vehicle's charging preferences. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4321: Serializer validation error. - KT-CT-4353: An error occurred while trying to update your charging preferences. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `KrakenFlexDeviceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `ShareGoodsQuote`

The possible errors that can be raised are: - KT-CT-4122: Invalid email. - KT-CT-8203: Received an invalid quote code. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `share` | `GoodsQuoteShare` |  | No | Goods quote shared. |

## `ShowInputFieldErrorsActionType`

An action that instructs the app to display validation errors on input fields.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `errors` | `[InputFieldErrorType]!` |  | No | List of field-level validation errors to display. |
| `id` | `ID` |  | No | Unique identifier of the object. |
| `screenId` | `String` |  | No | Optional ID of the form screen these errors apply to. |
| `typeName` | `String` |  | No | The name of the action object's type. |
| `typename` | `String` |  | No | The name of the object's type. |

## `SingleFuelConsumption`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `elecAnnualConsumption` | `Int` |  | No | Estimated annual consumption for electricity. |

## `SingleFuelProductQuote`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `annualFee` | `Float` |  | No | Annual fee for dual fuel. |
| `annualFeeUnits` | `String` |  | No | Annual fee units for dual fuel. |
| `annualFeeWithTaxes` | `Float` |  | No | Annual fee with taxes for dual fuel. |
| `electricity` | `SummaryProductInfo` |  | No | Quotation for electricity. |
| `monthlyFee` | `Float` |  | No | Monthly fee for dual fuel. |
| `monthlyFeeUnits` | `String` |  | No | Monthly fee units for dual fuel. |
| `monthlyFeeWithTaxes` | `Float` |  | No | Monthly fee with taxes for dual fuel. |

## `SiteTelemetry`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `consumptionInKw` | `Decimal` |  | No | The current power in kW being consumed by the property from the solar panels, battery and grid. If power is being exported to the grid, that is offset againstconsumption. If power is being used to charge the battery, that doesn't count towards consumption; that'll only count as consumed when it is later used to power the property (this avoids double-counting it). |
| `exportInKw` | `Decimal` |  | No | The current power being exported from the property to the grid in kW. This will be 0 if no export is occurring, or otherwise a positive value. |

## `SmartFlexChargePoint`

Information about a charge point that has been registered with Kraken Flex.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `alerts` | `[SmartFlexDeviceAlertInterface]` |  | No | Active alert message(s) for a device, showing the latest first. |
| `chargePointVariant` | `ChargePointVariantModelType` |  | No | This contains more detail about the variant of the charge point model. |
| `chargingPreferences` | `SmartFlexVehicleChargingPreferences` |  | No | The user's preferences for charging using this charge point. |
| `chargingSessions` | `DeviceChargingSessionConnection` | `before: DateTime, after: DateTime, sessionTypes: [ChargingSessionType], first: Int, last: Int` | No | History of charging sessions for a SmartFlex device. |
| `deviceType` | `KrakenFlexDeviceTypes!` |  | No | The type of device. |
| `id` | `ID!` |  | No | A UUID that identifies this device registration. Re-registering this device will result in a different ID. |
| `integrationDeviceId` | `String` |  | No | The third-party integration device ID. |
| `make` | `String` |  | No | The make of the charge point, e.g. myenergi. |
| `model` | `String` |  | No | The model of the charge point, e.g. Zappi. |
| `name` | `String` |  | No | The user-friendly name for the device. |
| `onboardingWizard` | `SmartFlexOnboardingWizard` |  | No | The current onboarding wizard for a device. |
| `preferenceSetting` | `FlexDevicePreferenceSettingInterface` |  | No | The preference setting for this device. |
| `preferences` | `SmartFlexDevicePreferencesInterface` |  | No | The device's preference details. |
| `propertyId` | `String` |  | No | The id of the property linked to the device. |
| `provider` | `ProviderChoices!` |  | No | The third-party that enables control of this device. |
| `reAuthenticationState` | `DeviceReAuthenticationInterface` |  | No | The re-authentication state of this device, if applicable. |
| `status` | `SmartFlexDeviceStatusInterface!` |  | No | Information about the current status of this device. |
| `vehicleVariant` | `ElectricVehicleModelType` |  | No | This contains more detail about the variant of the vehicle model. |

## `SmartFlexChargePointStatus`

The current status of a registered charge point.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `current` | `SmartFlexDeviceLifecycleStatus` |  | No | The current status of the device. |
| `currentState` | `SmartFlexDeviceState` |  | No | The current state of this SmartFlex device state machine. |
| `isSuspended` | `Boolean` |  | No | Whether control of the device is currently disabled. |
| `stateOfCharge` | `DecimalReading` |  | No | The latest SoC received from the vehicle. It has a value between 0-100. |
| `stateOfChargeLimit` | `StateOfChargeLimit` |  | No | Information about the limits for the SoC. |
| `testDispatchFailureReason` | `TestDispatchAssessmentFailureReason` |  | No | The reason for the most recent failed test dispatch (if any). |

## `SmartFlexChargingError`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cause` | `SmartFlexChargingErrorCause!` |  | No | Possible cause of the charging error. |

## `SmartFlexChargingSession`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cost` | `Money` |  | No | The cost for the charge added during a charging session. |
| `dispatches` | `[SmartFlexDispatch]` |  | No | The charging session dispatch. |
| `end` | `DateTime!` |  | No | The end time of a charging session. |
| `energyAdded` | `Energy` |  | No | The energy added during a charging session. |
| `problems` | `[SmartFlexChargingProblem]` |  | No | Charging problem(s) encountered during the session due to an error or truncation. |
| `start` | `DateTime!` |  | No | The start time of a charging session. |
| `stateOfChargeChange` | `Decimal` |  | No | The change in state of charge during a charging session. The value will be between 0 and 100, if not null. |
| `stateOfChargeFinal` | `Decimal` |  | No | The final state of charge after a charging session. The value will be between 0 and 100, if not null. |
| `targetType` | `PreferencesTargetType!` |  | No | The target type for a user's preferences. |
| `type` | `SmartFlexChargingType!` |  | No | The type of charge, i.e. `SMART` or `BOOST`. |

## `SmartFlexChargingTruncation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `achievableStateOfCharge` | `Decimal!` |  | No | The state of charge (in percent) that was possible, given the truncation. |
| `originalAchievableStateOfCharge` | `Decimal!` |  | No | The state of charge (in percent) that could have been achieved, if not for truncation of the charging session. |
| `truncationCause` | `SmartFlexChargingTruncationCause!` |  | No | The cause for the truncation of a charging session. |

## `SmartFlexDevice`

Information about a device that has been registered for Smart Flex.

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

## `SmartFlexDeviceAlert`

Information about an alert relevant to a device registered for Smart Flex.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String` |  | No | A device alert message. |
| `publishedAt` | `DateTime` |  | No | When a device alert message is published. |

## `SmartFlexDevicePreferenceSchedule`

A schedule entry for device preferences specifying target values for a specific day and time. For information about valid value ranges, time constraints, and step increments, query the device's `preferenceSettings` field which provides bounds and validation rules.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dayOfWeek` | `DayOfWeek!` |  | No | Day of week schedule applies to. |
| `max` | `Float` |  | No | Maximum value for the schedule. Usage depends on the `targetType` and `mode` - e.g. target state of charge for EVs, or cooling set point for heat pumps.For valid bounds and step increments, see the device's `preferenceSettings` field. |
| `min` | `Float` |  | No | Minimum value for the schedule when applicable. Usage depends on the `targetType` and `mode` - e.g. heating set point temperature for heat pumps. May be null for device types that don't require a lower bound. For valid bounds and step increments, see the device's `preferenceSettings` field. |
| `time` | `Time!` |  | No | Time of day the preference applies. |
| `upperLimit` | `Float` |  | No | Upper limit value for the schedule when applicable.Usage depends on the targetType - e.g., charge level to never be exceeded for V2G EVs.May be null for device types that don't require an upper bound. |

## `SmartFlexDevicePreferences`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `gridExport` | `FlexGridExportStatus!` |  | No | The status of the device's grid export capability. |
| `isChargingDurationCapped` | `FlexIsChargingDurationCapped!` |  | No | The status of the device's charging duration cap. |
| `mode` | `PreferencesModeChoices!` |  | No | The device's preference mode. |
| `schedules` | `[SmartFlexDevicePreferenceSchedule]` |  | No | The schedules of the device's preference. |
| `targetType` | `PreferencesTargetType!` |  | No | The target type of the preference. |
| `unit` | `PreferencesUnitChoices!` |  | No | The unit of the preference schedules' min and max values. |

## `SmartFlexDeviceStatus`

Information about the current status of a device registered for Smart Flex.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `current` | `SmartFlexDeviceLifecycleStatus` |  | No | The current status of the device. |
| `currentState` | `SmartFlexDeviceState` |  | No | The current state of this SmartFlex device state machine. |
| `isSuspended` | `Boolean` |  | No | Whether control of the device is currently disabled. |

## `SmartFlexDeviceSupplyPointType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `importSupplyPointId` | `String!` |  | No | Import supply point ID. |
| `smartFlexDeviceId` | `String!` |  | No | SmartFlex device ID. |

## `SmartFlexDispatch`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `end` | `DateTime!` |  | No | The end time of the dispatch. |
| `energyAddedKwh` | `Decimal` |  | No | The energy added in kWh of the dispatch. |
| `start` | `DateTime!` |  | No | The start time of the dispatch. |
| `type` | `SmartFlexChargingType!` |  | No | The type of charge. |

## `SmartFlexInverter`

Information about an inverter that has been registered with KrakenFlex.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `alerts` | `[SmartFlexDeviceAlertInterface]` |  | No | Active alert message(s) for a device, showing the latest first. |
| `deviceType` | `KrakenFlexDeviceTypes!` |  | No | The type of device. |
| `id` | `ID!` |  | No | A UUID that identifies this device registration. Re-registering this device will result in a different ID. |
| `integrationDeviceId` | `String` |  | No | The third-party integration device ID. |
| `make` | `String` |  | No | The make of the inverter. |
| `model` | `String` |  | No | The model of the inverter. |
| `name` | `String` |  | No | The user-friendly name for the device. |
| `onboardingWizard` | `SmartFlexOnboardingWizard` |  | No | The current onboarding wizard for a device. |
| `preferenceSetting` | `FlexDevicePreferenceSettingInterface` |  | No | The preference setting for this device. |
| `preferences` | `SmartFlexDevicePreferencesInterface` |  | No | The device's preference details. |
| `propertyId` | `String` |  | No | The id of the property linked to the device. |
| `provider` | `ProviderChoices!` |  | No | The third-party that enables control of this device. |
| `reAuthenticationState` | `DeviceReAuthenticationInterface` |  | No | The re-authentication state of this device, if applicable. |
| `status` | `SmartFlexDeviceStatusInterface!` |  | No | Information about the current status of this device. |
| `telemetry` | `SmartFlexInverterTelemetry` |  | No | Telemetry data for the inverter. |

## `SmartFlexInverterTelemetry`

Telemetry data for a registered inverter.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `battery` | `BatteryTelemetry` |  | No | Information about the battery. |
| `grid` | `GridTelemetry` |  | No | Information about the grid. |
| `inverter` | `InverterTelemetry` |  | No | Information about the inverter. |
| `site` | `SiteTelemetry` |  | No | Information about the site. |
| `solar` | `SolarTelemetry` |  | No | Information about the solar panels. |

## `SmartFlexOnboardingDeviceRegistration`

A type that returns True if the device(s) were successfully registered.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceRegistered` | `Boolean` |  | No | Returns true if the device(s) were successfully registered. |
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |

## `SmartFlexOnboardingWizard`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `backendScreen` | `BackendScreenType` | `maxVersionSupported: Int = 1` | No | A Backend Screen that renders the SmartFlex onboarding wizard. |
| `completedSteps` | `[SmartFlexOnboardingStepInterface]` |  | No | The completed steps for all onboarding wizards that are currently in progress. Note: - The last step is the most recent one. - If an onboarding journey is completed, it will not be included in this list. |
| `currentStep` | `SmartFlexOnboardingStepInterface` |  | No | The next step of the SmartFlex onboarding wizard. Returns `None` if the onboarding journey is completed. |
| `deviceType` | `KrakenFlexDeviceTypes` |  | No | The onboarding wizard's selected device type to be onboarded. |
| `displayName` | `String` |  | No | The onboarding wizard's display name extracted from the wizard's selected device attributes. |
| `id` | `ID!` |  | No | A unique identifier for this SmartFlex onboarding wizard. |
| `resumable` | `SmartFlexResumable` |  | No | Determines whether the wizard's onboarding journey can be resumed. |

## `SmartFlexResumable`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isResumable` | `Boolean` |  | No | A boolean to determine whether the wizard's onboarding journey can be resumed. |
| `resumableReasons` | `[String]` |  | No | Reasons why a wizard cannot be resumed. |

## `SmartFlexVehicle`

Information about a vehicle that has been registered with Kraken Flex.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `alerts` | `[SmartFlexDeviceAlertInterface]` |  | No | Active alert message(s) for a device, showing the latest first. |
| `chargePointVariant` | `ChargePointVariantModelType` |  | No | This contains more detail about the variant of the charge point model. |
| `chargingPreferences` | `SmartFlexVehicleChargingPreferences` |  | Yes (The 'chargingPreferences' field is deprecated. Please use 'devices.preferences' instead. - Marked as deprecated on 2024-11-01. - Scheduled for removal on or after 2025-05-06.) | The user's preferences for charging this vehicle. |
| `chargingSessions` | `DeviceChargingSessionConnection` | `before: DateTime, after: DateTime, sessionTypes: [ChargingSessionType], first: Int, last: Int` | No | History of charging sessions for a SmartFlex device. |
| `deviceType` | `KrakenFlexDeviceTypes!` |  | No | The type of device. |
| `id` | `ID!` |  | No | A UUID that identifies this device registration. Re-registering this device will result in a different ID. |
| `integrationDeviceId` | `String` |  | No | The third-party integration device ID. |
| `make` | `String` |  | No | The make of the vehicle, e.g. Tesla. |
| `model` | `String` |  | No | The model of the vehicle, e.g. Model 3. |
| `name` | `String` |  | No | The user-friendly name for the device. |
| `onboardingWizard` | `SmartFlexOnboardingWizard` |  | No | The current onboarding wizard for a device. |
| `preferenceSetting` | `FlexDevicePreferenceSettingInterface` |  | No | The preference setting for this device. |
| `preferences` | `SmartFlexDevicePreferencesInterface` |  | No | The device's preference details. |
| `propertyId` | `String` |  | No | The id of the property linked to the device. |
| `provider` | `ProviderChoices!` |  | No | The third-party that enables control of this device. |
| `reAuthenticationState` | `DeviceReAuthenticationInterface` |  | No | The re-authentication state of this device, if applicable. |
| `status` | `SmartFlexDeviceStatusInterface!` |  | No | Information about the current status of this device. |
| `vehicleVariant` | `ElectricVehicleModelType` |  | No | This contains more detail about the variant of the vehicle model. |

## `SmartFlexVehicleChargingPreferences`

The user's preferences for charging, e.g. target SoC (State of Charge).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `maximumSoc` | `Int` |  | No | The maximum SoC (percentage). |
| `minimumSoc` | `Int` |  | No | The minimum SoC (percentage). |
| `weekdayTargetSoc` | `Int!` |  | No | The target SoC to achieve on a weekday (percentage). |
| `weekdayTargetTime` | `Time!` |  | No | The time at which the target SoC should be achieved on a weekday. |
| `weekendTargetSoc` | `Int!` |  | No | The target SoC to achieve on a weekend (percentage). |
| `weekendTargetTime` | `Time!` |  | No | The time at which the target SoC should be achieved on a weekend. |

## `SmartFlexVehicleStatus`

The current status of a registered vehicle.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `current` | `SmartFlexDeviceLifecycleStatus` |  | No | The current status of the device. |
| `currentState` | `SmartFlexDeviceState` |  | No | The current state of this SmartFlex device state machine. |
| `isSuspended` | `Boolean` |  | No | Whether control of the device is currently disabled. |
| `stateOfCharge` | `DecimalReading` |  | No | The latest SoC received from the vehicle. It has a value between 0-100. |
| `stateOfChargeLimit` | `StateOfChargeLimit` |  | No | Information about the limits for the SoC. |
| `testDispatchFailureReason` | `TestDispatchAssessmentFailureReason` |  | No | The reason for the most recent failed test dispatch (if any). |

## `SolarSimulationCO2Savings`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `carKms` | `Int` |  | No | Estimated number of CO2 saved in car kms. |
| `flightsAvoided` | `Int` |  | No | Estimated number of CO2 saved in flights avoided. |
| `treesPlanted` | `Int` |  | No | Estimated number of CO2 saved in trees planted. |

## `SolarSimulationFinancedPrices`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `financing` | `MonthlyFinancingScalar` |  | No | Prices for the quote if financed. |
| `withBattery` | `MonthlyFinancingScalar` |  | No | Prices for the quote if financed with battery installation. |
| `withCharger` | `MonthlyFinancingScalar` |  | No | Prices for the quote if financed with charger installation. |
| `withChargerAndBattery` | `MonthlyFinancingScalar` |  | No | Prices for the quote if financed with charger and battery installation. |

## `SolarSimulationPostInstallationMultipliers`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `basicInstallation` | `Float` |  | No | Multiplier for estimated monthly spending after basic installation. |
| `monthly15` | `Float` |  | No | Multiplier for estimated monthly spending after installation - 15%. |
| `monthly25` | `Float` |  | No | Multiplier for estimated monthly spending after installation - 25%. |
| `monthly40` | `Float` |  | No | Multiplier for estimated monthly spending after installation - 40%. |
| `monthly7` | `Float` |  | No | Multiplier for estimated monthly spending after installation - 7%. |
| `withBattery` | `Float` |  | No | Multiplier for estimated monthly spending after installation with battery. |
| `withBatteryAndSolarWallet` | `Float` |  | No | Multiplier for estimated monthly spending after installation with battery and saller wallet. |
| `withSolarWallet` | `Float` |  | No | Multiplier for estimated monthly spending after installation with sollar Wallet. |

## `SolarSimulationQuote`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `batteryPrice` | `Float` |  | No | Price of the battery for the quote. |
| `cashPaymentPrice` | `Float` |  | No | Price of the quote if paid in cash, upfront. |
| `cashPaymentPriceWithBattery` | `Float` |  | No | Price of the quote if paid in cash, upfront, with battery installation. |
| `cashPrice` | `Float` |  | No | Price of the quote if paid in cash, upfront. |
| `chargerPrice` | `Float` |  | No | Price of the vehicle charger for the quote. |
| `co2Emissions` | `SolarSimulationCO2Savings` |  | No | Estimated CO2 emissions saved by the quote. |
| `financePaymentPrices` | `MonthlyFinancingScalar` |  | No | Prices for financing the quote, in months. |
| `financePaymentPricesWithBattery` | `MonthlyFinancingScalar` |  | No | Prices for financing the quote, in months, with battery installation. |
| `financedPrices` | `SolarSimulationFinancedPrices` |  | No | Prices for financing the quote, with and without battery installation. |
| `governmentSubsidiesMultiplier` | `Float` |  | No | Multiplier for government subsidies. |
| `message` | `String` |  | No | Message to be displayed to the frontend team. |
| `numberOfPanels` | `Int` |  | No | Number of panels of panels for the quote. |
| `panelPower` | `Float` |  | No | Power of each panel for the quote. |
| `panelPowerUnit` | `String` |  | No | Unit of the power of each panel for the quote. |
| `postInstalationMonthlySpending` | `Float` |  | No | Estimated monthly spending after installation of items in the quote. |
| `postInstallationMultipliers` | `SolarSimulationPostInstallationMultipliers` |  | No | Estimated monthly spending after installation of items in the quote. |
| `priceUnit` | `String` |  | No | Unit of the price of the quote. |
| `totalPower` | `Float` |  | No | Total power produced by the panels in the quote. |
| `totalPowerUnit` | `String` |  | No | Unit of the total power produced by the panels in the quote. |
| `twentyFiveYearSavings` | `Float` |  | No | Estimated savings over 25 years. |
| `twentyFiveYearSavingsMultipliers` | `SolarSimulationTwentyFiveYearSavingsMultipliers` |  | No | Estimated savings over 25 years with different multipliers. |
| `twentyFiveYearSavingsWithBattery` | `Float` |  | No | Estimated savings over 25 years with battery installation. |

## `SolarSimulationTwentyFiveYearSavingsMultipliers`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `savings` | `Int` |  | No | Multiplier for estimated savings over 25 years. |
| `withBattery` | `Int` |  | No | Multiplier for estimated savings over 25 years with battery installation. |
| `withSolarWallet` | `Int` |  | No | Multiplier for estimated savings over 25 years with solar wallet. |
| `withSolarWalletAndBattery` | `Int` |  | No | Multiplier for estimated savings over 25 years with solar wallet and battery installation. |

## `SolarSimulatorDirectSaleDirectSale`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cups` | `String` |  | No | CUPS of the direct sale as saved in Chipiron. |
| `dni` | `String` |  | No | DNI of the direct sale as saved in Chipiron. |
| `financedYears` | `Int` |  | No | Financed years of the direct sale as saved in Chipiron. Required if payment_type is 'financed'. |

## `SolarSimulatorDirectSaleOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `address` | `SolarSimulatorLeadAddress` |  | No | Address of the lead saved in chipiron. |
| `details` | `SolarSimulatorLeadDetails` |  | No | Details of the lead saved in chipiron. |
| `directSale` | `SolarSimulatorDirectSaleDirectSale` |  | No | Direct sale details saved in chipiron. |
| `email` | `String` |  | No | Email of the lead as saved in Chipiron. |
| `firstName` | `String` |  | No | Name of the lead as saved in Chipiron. |
| `fullAddress` | `String` |  | No | Street of the lead as saved in Chipiron. |
| `lastName` | `String` |  | No | Surname of the lead as saved in Chipiron. |
| `phone` | `String` |  | No | Phone number of the lead as saved in Chipiron. |

## `SolarSimulatorLeadAddress`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fullAddress` | `String` |  | No | Street of the lead as saved in Chipiron. |
| `houseType` | `String` |  | No | House type of the lead as saved in Chipiron. |

## `SolarSimulatorLeadDetails`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `battery` | `String` |  | No | Battery of the lead as saved in Chipiron. |
| `consumption` | `Int` |  | No | Consumption of the lead as saved in Chipiron. |
| `numberOfPanels` | `Int` |  | No | Number of panels of the lead as saved in Chipiron. |
| `paymentType` | `String` |  | No | Payment type of the lead as saved in Chipiron. |
| `roofSize` | `Float` |  | No | Roof size of the lead as saved in Chipiron. |
| `solarWallet` | `String` |  | No | Solar wallet of the lead as saved in Chipiron. |
| `vehicleCharger` | `String` |  | No | Vehicle charger of the lead as saved in Chipiron. |

## `SolarSimulatorLeadOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `address` | `SolarSimulatorLeadAddress` |  | No | Address of the lead saved in chipiron. |
| `details` | `SolarSimulatorLeadDetails` |  | No | Details of the lead saved in chipiron. |
| `email` | `String` |  | No | Email of the lead as saved in Chipiron. |
| `firstName` | `String` |  | No | Name of the lead as saved in Chipiron. |
| `fullAddress` | `String` |  | No | Street of the lead as saved in Chipiron. |
| `lastName` | `String` |  | No | Surname of the lead as saved in Chipiron. |
| `phone` | `String` |  | No | Phone number of the lead as saved in Chipiron. |

## `SolarTelemetry`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `powerInKw` | `Decimal` |  | No | The current power being generated by the solar panels in kW. This will be null if there are no solar panels, 0 if there are solar panels but they are not generating, or a positive value if they are generating. |

## `SolarWalletLedgers`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `targetGivenName` | `String` |  | No | The name of the receiver of the credit. |
| `targetLedger` | `String` |  | No | The target ledger to which the credit is shared. |
| `validFrom` | `DateTime!` |  | No | Datetime when the solar wallet credit sharing ledger begins. |
| `validTo` | `DateTime` |  | No | Datetime when the solar wallet credit sharing ledger ends. |

## `SpecialCircumstanceRecordType`

Any special circumstances that the user has notified us about, which may entitle them to some specialist services.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `createdAt` | `DateTime` |  | No | The date and time the special circumstance record was created. |
| `id` | `ID` |  | No |  |
| `internalCode` | `String` |  | No |  |
| `summary` | `String` |  | No |  |

## `SpecialCircumstancesType`

Information about the special circumstances that relate to a user.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isSharingConsentGiven` | `Boolean` |  | No | Whether the user has consented for their data to be given to the appropriate industry or regulatory bodies. We typically only ask for this once, so this field can be used to decide whether to ask the user for their initial consent. |
| `records` | `[SpecialCircumstanceRecordUnion]` |  | No |  |

## `SpecialTariff`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | Kraken product code. |
| `description` | `String` |  | No | Kraken product description. |
| `displayName` | `String` |  | No | Kraken product display name. |
| `id` | `Int` |  | No | Kraken product id. |
| `marketName` | `String` |  | No | Kraken product market name. |
| `params` | `ProductParams` |  | No | Kraken product params. |
| `prices` | `ProductPricesWithExcess` |  | No | Product prices. |

## `StandardAddressInfo`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `postcode` | `String` |  | No | The area postcode. |
| `provinceCode` | `String` |  | No | The province code. |
| `provinceName` | `String` |  | No | The province name. |
| `streetDetails` | `[StreetDetails]` |  | No | List of streets with their city codes and names. |

## `StartCollectionProcess`

Start a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11208: Invalid billing document identifier for collection process. - KT-CT-11209: Collection process configuration does not have published version. - KT-CT-11210: Active collection process for entity already exists. - KT-CT-11211: Too many active collection processes for config. - KT-CT-11212: Invalid collection process config code. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessStarted` | `StartCollectionProcessOutput` |  | No | Details of collection process that has been started. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `StartCollectionProcessOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountNumber` | `String` |  | No | Account number associated to the collection process. |
| `number` | `String` |  | No | The number of the collection process record. |

## `StartCustomerVerification`

Start the customer verification using the provided verification method. The possible errors that can be raised are: - KT-CT-1701: Brand does not exist. - KT-CT-4194: Verification type not supported yet. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `verificationProcess` | `VerificationProcess` |  | No | The newly created verification process. |

## `StartOnSiteJobsAppointmentBookingSession`

The possible errors that can be raised are: - KT-CT-13010: No booking adapter found for agent. - KT-CT-13020: Could not identify agent from property. - KT-CT-13021: Invalid job type. - KT-CT-13022: Work category not found for job type. - KT-CT-13023: Appointment booking checks failed. - KT-CT-13024: Appointment booking checks returned warnings. - KT-CT-13032: Request does not exist. - KT-CT-13054: Appointment not found for rescheduling. - KT-CT-13055: Appointment does not belong to the specified request. - KT-CT-13056: Appointment cannot be rescheduled. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `appointmentBookingSessionId` | `UUID` |  | No | The Kraken booking ID for the appointment booking session. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `StartReAuthentication`

Create a wizard for re-authenticating a device with SmartFlex. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4385: Re-authentication is not supported for this device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for re-authenticating the device with SmartFlex. |

## `StartSmartFlexOnboarding`

Create a wizard for onboarding a device with SmartFlex. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4385: Re-authentication is not supported for this device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `StartTestChargeForSmartFlexOnboarding`

Attempt to start a test charge. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `wizard` | `SmartFlexOnboardingWizard` |  | No | The wizard created for onboarding the device with SmartFlex. |

## `StateOfChargeLimit`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isLimitViolated` | `Boolean` |  | No | Whether or not target SoC exceeds upper SoC limit. |
| `timestamp` | `String` |  | No | Time of the latest SoC limit reading. |
| `upperSocLimit` | `Int` |  | No | Maximum level of charge allowed by the battery relative to its capacity (in percent). |

## `StatementBillingDocumentConnectionTypeConnection`

A statement is a billing document that contains all entries on a ledger during a period of time. A customer can understand how their ledger's balance has changed by looking at each statement in series.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[StatementBillingDocumentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `StatementBillingDocumentConnectionTypeEdge`

A Relay edge containing a `StatementBillingDocumentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `StatementBillingDocumentType` |  | No | The item at the end of the edge |

## `StatementBillingDocumentType`

A statement is a billing document that contains all entries on a ledger during a period of time. A customer can understand how their ledger's balance has changed by looking at each statement in series.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `annulledBy` | `AnnulmentBillingDocumentType` |  | No | Billing document that annuls this statement. |
| `documentDebtPosition` | `BillingDocumentPositionType` |  | No | Position of the billing document in the delinquent debt tracking system. |
| `earliestChargeAt` | `DateTime` |  | No | The earliest charge date of the statement. |
| `endAt` | `DateTime!` |  | No | The end of the statement's period. |
| `firstIssuedAt` | `DateTime` |  | No | The date and time the statement was sent to the customer. |
| `id` | `Int` |  | No | ID for the statement billing document. |
| `identifier` | `String` |  | No | The unique reference of the statement that can be used for identifying the statement externally. |
| `latestChargeAt` | `DateTime` |  | No | The latest charge date of the statement. |
| `paymentDueDate` | `Date` |  | No | The date due for payment for the statement. |
| `pdfUrl` | `String` |  | No | URL to the PDF of the statement. |
| `startAt` | `DateTime!` |  | No | The start of the statement's period. |
| `totalCharges` | `StatementTotalType` |  | No | The total amounts for all charges on the statement. |
| `totalCredits` | `StatementTotalType` |  | No | The total amounts for all credits on the statement. |
| `transactions` | `BillTransactionConnectionTypeConnection` | `orderBy: TransactionsOrderBy = POSTED_DATE_DESC, before: String, after: String, first: Int, last: Int` | No | Transactions on the statement |

## `StatementDetailsBillingDocumentConnectionTypeConnection`

A statement is a billing document that contains all entries on a ledger during a period of time. A customer can understand how their ledger's balance has changed by looking at each statement in series.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[StatementDetailsBillingDocumentConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `StatementDetailsBillingDocumentConnectionTypeEdge`

A Relay edge containing a `StatementDetailsBillingDocumentConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `StatementDetailsBillingDocumentType` |  | No | The item at the end of the edge |

## `StatementDetailsBillingDocumentType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Decimal` |  | No | Bill total amount. |
| `annulledBy` | `AnnulmentBillingDocumentType` |  | No | Billing document that annuls this statement. |
| `consumptionEndDate` | `DateTime` |  | No | The end of the consumption's period. |
| `consumptionStartDate` | `DateTime` |  | No | The start of the consumption's period. |
| `documentDebtPosition` | `BillingDocumentPositionType` |  | No | Position of the billing document in the delinquent debt tracking system. |
| `earliestChargeAt` | `DateTime` |  | No | The earliest charge date of the statement. |
| `endAt` | `DateTime!` |  | No | The end of the statement's period. |
| `firstIssuedAt` | `DateTime` |  | No | The date and time the statement was sent to the customer. |
| `id` | `Int` |  | No | ID for the statement billing document. |
| `identifier` | `String` |  | No | Bill identifier. |
| `issuedDate` | `DateTime` |  | No | Bill issued date. |
| `latestChargeAt` | `DateTime` |  | No | The latest charge date of the statement. |
| `number` | `Int` |  | No | Bill number. |
| `paymentDueDate` | `Date` |  | No | The date due for payment for the statement. |
| `pdfUrl` | `String` |  | No | URL to the PDF of the statement. |
| `startAt` | `DateTime!` |  | No | The start of the statement's period. |
| `totalCharges` | `StatementTotalType` |  | No | The total amounts for all charges on the statement. |
| `totalCredits` | `StatementTotalType` |  | No | The total amounts for all credits on the statement. |
| `transactions` | `BillTransactionConnectionTypeConnection` | `orderBy: TransactionsOrderBy = POSTED_DATE_DESC, before: String, after: String, first: Int, last: Int` | No | Transactions on the statement |

## `StatementTotalType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `grossTotal` | `Int` |  | No | The gross total amount for the statement (in minor currency units). |
| `netTotal` | `Int` |  | No | The net total amount for the statement (in minor currency units). |
| `taxTotal` | `Int` |  | No | The total amount of tax on the statement (in minor currency units). |

## `StatementType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `attachments` | `BillingAttachmentConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No |  |
| `billType` | `BillTypeEnum` |  | No | The type of the bill. |
| `closingBalance` | `Int` |  | No | This field returns the closing balance of an issued statement. |
| `consumptionEndDate` | `Date` |  | No | The last day of consumption that this statement includes. |
| `consumptionStartDate` | `Date` |  | No | The first day of consumption that this statement includes. |
| `fromDate` | `Date` |  | No | The date of the constituent bill covered from. |
| `heldStatus` | `HeldStatus` |  | No | Retrieve the held status of a account statement. |
| `id` | `ID` |  | No | The ID of the constituent bill. |
| `isExternalBill` | `Boolean` |  | No | Whether the bill originated in Kraken or externally. |
| `issuedDate` | `Date` |  | No | The date the bill was sent to the customer. |
| `openingBalance` | `Int` |  | No | This field returns the opening balance of a statement. |
| `paymentDueDate` | `Date` |  | No | The date the bill is due to be paid. |
| `reversalsAfterClose` | `StatementReversalsAfterClose!` |  | No | How many charges have been reversed after the close date. |
| `status` | `AccountStatementStatus` |  | No | Current status of the associated statement. |
| `temporaryUrl` | `String` |  | Yes (The 'temporaryUrl' field is deprecated. This field is deprecated. Use the 'attachments' field instead. - Marked as deprecated on 2024-09-16. - Scheduled for removal on or after 2025-09-01.) | Requesting this field generates a temporary URL at which bill is available. This URL will expire after approximately an hour. It is intended for redirection purposes, NOT persistence in any form (e.g. inclusion in emails or the body of a web page). This field can raise an error with errorClass NOT_FOUND if the bill document has not been created/issued yet. This field is deprecated use 'attachments' field instead. |
| `toAddress` | `String` |  | No | Email recipient address. |
| `toDate` | `Date` |  | No | The date of the constituent bill covered to. |
| `totalCharges` | `StatementTotalType` |  | No | The total amounts for all charges on the statement. |
| `totalCredits` | `StatementTotalType` |  | No | The total amounts for all credits on the statement. |
| `transactions` | `TransactionConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | Transactions on the bill. |
| `userId` | `Int` |  | No | Email recipient user ID. |

## `StatisticOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `costExclTax` | `EstimatedMoneyType` |  | No | Monetary cost of the statistic (excluding tax), if applicable. |
| `costInclTax` | `EstimatedMoneyType` |  | No | Monetary cost of the statistic (including tax), if applicable. |
| `description` | `String` |  | No | Description of the statistic for the parent node. |
| `label` | `String` |  | No | Display label of the statistic for the parent node. |
| `type` | `ReadingStatisticTypeEnum` |  | No | The type of statistic being measured for the parent node. |
| `value` | `Decimal` |  | No | Consumption / generation value of the statistic, if applicable. |

## `StopAutomatedPayments`

Choose how automatic payments will be collected. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3968: Preference cannot be set this soon. - KT-CT-3969: Preferences must change on a specific day of the week for weekly schedules. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `StoreDirectDebitPaymentMethodDetails`

The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3940: Invalid data. - KT-CT-3956: Temporary error occurred. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `storedPaymentMethodDetailsReference` | `String` |  | No |  |

## `StorePaymentInstruction`

Store a new payment instruction created through the embedded process. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `paymentInstruction` | `PaymentInstructionType` |  | No | The stored payment instruction. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `StreetDetails`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cityCode` | `String` |  | No | The city code. |
| `cityName` | `String` |  | No | The city name. |
| `streetName` | `String` |  | No | The street name. |

## `StreetType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `label` | `String` |  | No | Street type name. |
| `value` | `String` |  | No | Street type abbreviation code. |

## `StringCharacteristicValueType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `characteristic` | `CharacteristicType` |  | No | The product characteristic. |
| `stringValue` | `String!` |  | No | The string value of the characteristic. |
| `value` | `String` |  | No | A string representation of a characteristic value, for convenience. |

## `StringType`

Graphene type object to represent string values

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `stringValue` | `String!` |  | No | Value of this field. |

## `SubmitCustomerFeedback`

The possible errors that can be raised are: - KT-CT-5514: Unable to submit feedback. - KT-CT-5511: The feedback_id should be provided for feedback source. - KT-CT-5512: The feedback doesn't match the account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `customerFeedback` | `CustomerFeedbackType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SubmitGasSelfReading`

The possible errors that can be raised are: - KT-ES-4508: Self-reading input is invalid. - KT-ES-4509: Self-reading submission failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cups` | `String` |  | No | The CUPS identifier for the supply point. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SubmitRepaymentRequest`

Mutation for executing the repayment request use case. The possible errors that can be raised are: - KT-CT-1132: Unauthorized. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3823: Unauthorized. - KT-CT-3926: Unauthorized. - KT-CT-3927: Invalid Amount. - KT-CT-3928: Idempotency key used for another repayment request. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `repaymentRequest` | `RequestRepaymentOutputType` |  | No | The newly created repayment request. |

## `SummaryProductInfo`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `availableFrom` | `String` |  | No | Kraken product availability from. |
| `availableTo` | `String` |  | No | Kraken product availability to. |
| `code` | `String` |  | No | Kraken product code. |
| `description` | `String` |  | No | Kraken product description. |
| `displayName` | `String` |  | No | Kraken product display name. |
| `dualFuelDescription` | `String` |  | No | Product details dual fuel description. |
| `id` | `Int` |  | No | Kraken product id. |
| `marketName` | `String` |  | No | Kraken product market name. |
| `monthlyFeeWithTaxes` | `Int` |  | No | Monthly fee with taxes for product in cents. |
| `params` | `ProductParams` |  | No | Kraken product params. |
| `prices` | `ProductPrices` |  | No | Product prices. |
| `term` | `Int` |  | No | Kraken product term. |

## `SupplementaryLedgerType`

Ledgers provide the foundation of Kraken’s bookkeeping functionality. Similar to a bank account, they allow us to keep track of financial activity on a particular Kraken account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `currentBalance` | `Int` |  | No | The current final balance of the ledger in pence. |
| `id` | `ID` |  | Yes (The 'ledgerId' field is deprecated. Please use 'ledgerNumber' instead. This is in the form of 'L-123456789A' - Marked as deprecated on 2024-10-22. - Scheduled for removal on or after 2025-06-25.) |  |
| `ledgerType` | `String` |  | No |  |
| `name` | `String` |  | No | The display name of the ledger. |
| `number` | `String` |  | No | The canonical name of the ledger. |
| `paymentAdequacy` | `PaymentAdequacyDetailsType` |  | No |  |

## `SupplyOrServiceCharge`

Supporting information for a customer charge resulting from a supply or service agreement

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreements` | `AgreementConnection` | `before: String, after: String, first: Int, last: Int` | No | Agreements which were charged |
| `period` | `Period!` |  | No | The period that was charged. |

## `SupplyPeriodConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[SupplyPeriodConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `SupplyPeriodConnectionTypeEdge`

A Relay edge containing a `SupplyPeriodConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `SupplyPeriodType` |  | No | The item at the end of the edge |

## `SupplyPeriodType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No |  |
| `isBillable` | `Boolean!` |  | No | Should this period be billed? False for accepted erroneous gains. |
| `supplyEndAt` | `DateTime` |  | No |  |
| `supplyStartAt` | `DateTime!` |  | No |  |

## `SupplyPointConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[SupplyPointConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `SupplyPointConnectionTypeEdge`

A Relay edge containing a `SupplyPointConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `SupplyPointType` |  | No | The item at the end of the edge |

## `SupplyPointContextDataType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `externalIdentifier` | `String` |  | No | Supply point external identifier. |
| `marketName` | `String` |  | No | Supply point market name. |
| `requestedSupplyStartDate` | `Date` |  | No | Requested supply start date. |
| `selectedProduct` | `SelectedProductType` |  | No | The selected product information for this supply point or None if no product is selected. |

## `SupplyPointTaxAdjustmentType`

Represents a tax adjustment for a specific supply point.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `adjustmentType` | `String` |  | No | The type of tax adjustment (e.g., EXEMPTION, REDUCTION). |
| `effectiveFrom` | `DateTime` |  | No | When this adjustment becomes effective. |
| `effectiveTo` | `DateTime` |  | No | When this adjustment ends (null if open-ended). |
| `qualifyingUsage` | `Decimal` |  | No | The proportion of usage that qualifies for the adjustment (0-1). |
| `supplyPointId` | `ID` |  | No | The ID of the supply point. |
| `taxCategory` | `String` |  | No | The tax category for this adjustment. |
| `taxSubcategory` | `String` |  | No | The tax subcategory for this adjustment. |

## `SupplyPointType`

Represents a SupplyPoint.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `devices` | `DevicesConnection` | `deviceIdentifiers: [String], before: String, after: String, first: Int, last: Int` | No | Get list of devices under a supply point. |
| `externalIdentifier` | `String` |  | No | The external identifier of the supply point. |
| `id` | `ID!` |  | No | The ID of the supply point. |
| `marketName` | `String!` |  | No | The market this supply point belongs to. |
| `property` | `PropertyType` |  | No | The supply point's property. |
| `readings` | `Readings` | `startAt: DateTime!, endAt: DateTime!, readingType: ReadingTypes!, timeGranularity: TimeGranularities, timezone: String = "Europe/Madrid", units: [Units]` | No | Get readings from a readable device e.g., a supply point, device, or register. |

## `SupplyProductTagType`

A product tag.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String` |  | No | Tag code. |
| `displayName` | `String` |  | No | Tag display name. |

## `SupplyProductType`

GraphQL type for a supply product.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `availabilityStatus` | `ProductAvailability` |  | No | The product availability status. |
| `availableFrom` | `DateTime` |  | No | The date and time the product is available from. |
| `availableTo` | `DateTime` |  | No | The date and time the product is available to. |
| `brandCode` | `String` |  | No | The brand code of the product. |
| `code` | `String` |  | No | The product code. |
| `description` | `String` |  | No | The product description. |
| `displayName` | `String` |  | No | The product description. |
| `endsAt` | `DateTime` |  | No | The date the product ends. |
| `fullName` | `String` |  | No | The product title. |
| `id` | `ID!` |  | No |  |
| `isHidden` | `Boolean` |  | No | Whether the product is hidden. |
| `marketName` | `String` |  | No | The name of the market the product belongs to. |
| `notes` | `String` |  | No | The product notes. |
| `params` | `JSONString` |  | No | The product parameters. |
| `tags` | `[SupplyProductTagType!]!` |  | No | Tags associated with the product. |
| `term` | `Int` |  | No | The product term in months. |
| `termsAndConditionsTypes` | `[TermsAndConditionsType!]!` |  | No | Active terms and conditions for a market supply product. |
| `termsContractType` | `String` |  | No | The product contract type. |

## `SuspendDeviceControl`

Suspend control of a device while away from home, e.g. on holiday. This is to prevent charging during that period. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4358: Unable to suspend device control. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `krakenflexDevice` | `KrakenFlexDeviceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `SwitchAccountToVariablePaymentSchedule`

The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3921: Account not found. - KT-CT-3922: Ledger not found for the account. - KT-CT-3947: An unexpected error occurred. - KT-CT-3984: Could not delete conflicting future payment schedule. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `schedule` | `PaymentScheduleType!` |  | No | New payment schedule. |

## `TagType`

Represents a tag used for classifying offerings and products.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `String!` |  | No | Unique tag code. |
| `displayName` | `String!` |  | No | Display name of the tag. |

## `TaskResult`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `error` | `String` |  | No | The error message if the task failed. |
| `result` | `JSONString` |  | No | The result of the task. |
| `status` | `TaskStatusEnum` |  | No | The status of the task. |

## `TaxAdjustmentConfigurationType`

Represents a tax adjustment configuration term in a contract. This term stores tax adjustment details for supply points associated with the contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `adjustments` | `[SupplyPointTaxAdjustmentType]` |  | No | List of supply point tax adjustments. |
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `TaxTypes`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `code` | `TaxTypesCode!` |  | No |  |
| `displayName` | `String!` |  | No |  |
| `endDateAt` | `DateTime` |  | No |  |
| `rate` | `Decimal!` |  | No |  |
| `startDateAt` | `DateTime!` |  | No |  |
| `unitType` | `TaxTypesUnitType!` |  | No |  |

## `Team`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID!` |  | No | The ID of the operations team. |
| `name` | `String!` |  | No | The name of the operations team. |
| `ref` | `String!` |  | No | The team reference for routing (e.g., 'OPERATIONS_GROUP.TEAM.TEAM_A'). |

## `TeamGroup`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `name` | `String!` |  | No | The name of the team group (e.g., 'GROUP_A'). |
| `ref` | `String!` |  | No | The team group reference for routing (e.g., 'OPERATIONS_GROUP.GROUP.GROUP_A'). |

## `TeamLocation`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `friendlyName` | `String!` |  | No | The human-readable location name (e.g., 'London'). |
| `ref` | `String!` |  | No | The location reference for routing (e.g., 'OPERATIONS_GROUP.LOCATION.London'). |

## `TemporarySpecialCircumstanceRecordType`

Any special circumstances that the user has notified us about, which may entitle them to some specialist services. These circumstances have an end date, after which they will not longer apply. Having young children is an example of this in the UK.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `createdAt` | `DateTime` |  | No | The date and time the special circumstance record was created. |
| `expiryDate` | `Date` |  | No |  |
| `id` | `ID` |  | No |  |
| `internalCode` | `String` |  | No |  |
| `summary` | `String` |  | No |  |

## `TermTemplateComponentType`

Represents a contract term template component within an offering.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `component` | `TermTemplateType!` |  | No | The contract term template associated with this component. |
| `identifier` | `ID!` |  | No | Unique identifier of the component. |
| `initialQuantity` | `Int!` |  | No | Initial/default quantity for this component. |
| `maximumQuantity` | `Int!` |  | No | Maximum quantity of this component that can be selected. |
| `minimumQuantity` | `Int!` |  | No | Minimum quantity of this component that can be selected. |

## `TermTemplateType`

Represents a contract term template in the catalog.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `String!` |  | No | The description of this contract term template. |
| `name` | `String!` |  | No | The name of this contract term template. |
| `templateData` | `JSONString!` |  | No | The data associated with this contract term template. |
| `termType` | `String!` |  | No | The type of contract term. |

## `TerminateAgreement`

Terminate an agreement. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-1513: Unable to terminate agreement. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreement` | `CommonAgreementType` |  | No | The created agreement. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `TerminateContractOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contract` | `Contract` |  | No | The contract terminated. |

## `TerminateCreditTransferPermission`

Mutation to terminate a credit transfer permission. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3825: Credit transfer permission not found. - KT-CT-3827: The ledger is not valid. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `validTo` | `DateTime` |  | No | Datetime when the credit transfer permission ends. |

## `TerminateSolarWalletRelationship`

Terminate the solar wallet credit sharing ledger validation date range between a solar wallet ledger source and an electricity ledger target. The possible errors that can be raised are: - KT-ES-4116: Account not found. - KT-ES-7807: The request to terminate a solar wallet sharing credit between ledgers was incomplete or malformed. - KT-ES-7808: Couldn't stop sharing credit between ledgers because credit sharing ledger doesn't exist. - KT-ES-7809: There is no ledger of this type on this account.. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `creditSharingLedgerId` | `Int` |  | No | Credit sharing ledgers id. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `sourceAccountNumber` | `String` |  | No | Source account number of the solar wallet ledger. |
| `success` | `Boolean` |  | No | A flag that ensures changes have been made. |
| `targetAccountNumber` | `String` |  | No | Target account number of the electricity ledger. |
| `targetGivenName` | `String` |  | No | Target account given name. |
| `validTo` | `DateTime` |  | No | Datetime when the solar wallet credit sharing ledger ends. |

## `TerminationFeeType`

Represents the termination term of a contract.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `amount` | `Decimal` |  | No | The amount of the termination fee. |
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `feeType` | `TerminationFeeType` |  | No | The type of termination fee. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `marketName` | `NonEmptyString` |  | No | The market associated with the termination fee. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `TermsAndConditionsConnectionTypeConnection`

Pagination for terms and conditions.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[TermsAndConditionsConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `TermsAndConditionsConnectionTypeEdge`

A Relay edge containing a `TermsAndConditionsConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `TermsAndConditionsType` |  | No | The item at the end of the edge |

## `TermsAndConditionsS3UrlType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `name` | `String` |  | No | The display name of the terms and conditions. |
| `s3Url` | `String` |  | No | The S3 URL to the terms and conditions file. |

## `TermsAndConditionsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `brandCode` | `String` |  | No |  |
| `effectiveFrom` | `DateTime` |  | No |  |
| `html` | `String` |  | No | The html of the terms and conditions document rendered as a JSON string. |
| `markdown` | `String` |  | No | The markdown text of the terms and conditions. |
| `name` | `String` |  | No |  |
| `pdfUrl` | `String` |  | No |  |
| `version` | `String` |  | No |  |

## `TeslaModifyScopes`

A step which indicates that the Tesla permission scopes need to be granted by the user in order to register their vehicle.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `modifyScopesUri` | `String` |  | No | Returns the URI to update the permission scopes. |
| `redirectUri` | `String` |  | No | The redirect URI to return to after updating the permission scopes. |

## `TeslaRegistrationFailed`

A step which indicates that the Tesla registration failed and the user must re-grant permission scopes to register their vehicle.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `modifyScopesSelected` | `Boolean` |  | No | Returns:- `true` if user wants to update permissions scopes.- `false` if user wants to retry the OAuth journey.- `null` if user has not made a decision. |

## `TeslaSetupVirtualKey`

A step which indicates that the user must add the given URI as a virtual key in their Tesla account.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `key` | `String` |  | No | The name of the key to add. |
| `uri` | `String` |  | No | The URI to add as a virtual key in the user's Tesla account. |

## `TestCharge`

A step which indicates if we're able to test charge the user's vehicle(s).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `error` | `TestChargeError` |  | No | Returns the error raised from a failed test charge. |
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `isReady` | `Boolean` |  | No | Returns `true` if the device is ready for a test charge. |
| `isStarted` | `Boolean` |  | No | Returns `true` if the test charge has started. |
| `status` | `TestDispatchStatus` |  | Yes (The 'status' field is deprecated. Please use 'isStarted' and 'error' instead. - Marked as deprecated on 2024-12-12. - Scheduled for removal on or after 2025-02-12.) | Returns the dispatch status of test charge. |

## `TestChargeError`

Errors can be of two kinds (assuming the user is querying this type with `message`, `reasons`, `errorType`, and `descriptions` fields): 1. If we were unable to start a test charge, the response will be: ``` { "message": "TestChargeRefused", "reasons": [Returns a list of values from `TestChargeRefusalReason`], "errorType": "UNABLE_TO_INITIATE_TEST_CHARGE", "descriptions": [Returns a list of descriptions for the refusal reasons] } ``` Where `descriptions` can be: - `DEVICE_LIVE`: "device is already live" - `DEVICE_ONBOARDING_IN_PROGRESS`: "test dispatch already in progress" - `DEVICE_RETIRED`: "device is retired" - `DEVICE_SUSPENDED`: "device is suspended" - `DEVICE_DISCONNECTED`: "device is disconnected" - `DEVICE_ALREADY_CHARGING`: "device is already charging" - `DEVICE_AWAY_FROM_HOME`: "device is away from home" - `DEVICE_NO_LOCATION_CONFIGURED`: "device has no location configured" - `DEVICE_LOCATION_UNABLE_TO_IDENTIFY`: "unable to identify device location" - `DEVICE_LOCATION_MISSING`: "device location is missing" 2. If an error occurred during a test charge, the response will be: ``` { "message": "Test dispatch failed", "reasons": [Returns a list of values from `TestDispatchAssessmentFailureReason`], "errorType": "UNABLE_TO_COMPLETE_TEST_CHARGE", "descriptions": [Returns a list of descriptions for the refusal reasons] } ``` Where `descriptions` can be: - `ASSESSMENTS_FAILED`: "Both power-based and charge status-based assessments failed" - `NOT_AT_HOME`: "Device location not at home" - `UNKNOWN`: "Unknown failure" - `UNABLE_TO_COMMUNICATE`: "Unable to communicate with device" - `DEVICE_DISCONNECTED`: "Device disconnected" - `SOC_LIMIT_REACHED`: "State of charge limit reached" - `ERROR`: "Could not fetch the test charge failure reason" - `NONE`: "No failure reason"

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `descriptions` | `[String]` |  | No | A list of error descriptions for a failed test charge attempt. |
| `errorType` | `TestChargeErrorType` |  | No | The type of test charge error. |
| `message` | `String` |  | No | A human readable error message. |
| `reasons` | `[String]` |  | No | A list of reasons for a failed test charge attempt. |
| `refusalReasons` | `[TestChargeRefusalReason]` |  | Yes (The 'refusalReasons' field is deprecated. Please use `errorType` and `reasons` instead. - Marked as deprecated on 2025-01-07. - Scheduled for removal on or after 2025-01-29.) | A list of refusal reasons from the failed test charge attempt. |

## `TextType`

A block of text.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | Unique identifier of the object. |
| `textAlignment` | `Alignment` |  | No | The text alignment. |
| `textStyle` | `TextStyleV1` |  | No | The text style, i.e. header, body. |
| `typename` | `String` |  | No | The name of the object's type. |
| `value` | `String!` |  | No | The text content. |

## `ThirdPartyCompleteDeviceRegistration`

Complete the registration of a device. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4322: Unable to complete registration error. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `ThirdPartyCompleteDeviceRegistrationType` |  | No | The response showing account validity and optional tariff information. |

## `ThirdPartyCompleteDeviceRegistrationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isAccountValid` | `Boolean!` |  | No | If the account is valid. |
| `isTariffSwitchInProgress` | `Boolean!` |  | No | If a switch to the required tariff is in progress. |
| `tariff` | `ThirdPartyTariffsType` |  | No | The tariff the account is on, if the switch is complete. |

## `ThirdPartyOrganizationType`

Type for the third party organization.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `name` | `String!` |  | No | The name of the third party. |
| `permissions` | `[ThirdPartyPermission]` |  | No | Holds information about the permissions of the current viewer. |

## `ThirdPartyPermission`

Holds information about a specific permission.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `permission` | `String` |  | No | The short name of the permission. |

## `ThirdPartyTariffIntervalType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `daysOfWeek` | `[String]!` |  | No | Day(s) of the week of the tariff interval. |
| `endTime` | `String!` |  | No | Local 24hr end time of the tariff interval (format hh:mm). |
| `startTime` | `String!` |  | No | Local 24hr start time of the tariff interval (format hh:mm). |
| `tariffType` | `String!` |  | No | The type of tariff this is (e.g. peak or offPeak). |

## `ThirdPartyTariffType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `currency` | `String!` |  | No | Currency according to the ISO 4217 standard. |
| `price` | `Decimal!` |  | No | Price per kWh in the given currency. |
| `type` | `String!` |  | No | The type of tariff this is (e.g. peak or offPeak). |

## `ThirdPartyTariffsType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `tariffIntervals` | `[ThirdPartyTariffIntervalType]!` |  | No | Tariff intervals of the charging location. |
| `tariffs` | `[ThirdPartyTariffType]!` |  | No | Tariff rates of the charging location. |

## `TimeOfUseOverrideType`

Represents a time-of-use override to be applied in a contract. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `NonEmptyString` |  | No | The description of the term. |
| `displayName` | `NonEmptyString` |  | No | The display name of the term. |
| `identifier` | `NonEmptyString` |  | No | The identifier of the term. |
| `isVariable` | `Boolean` |  | No | Whether the term is variable. |
| `type` | `NonEmptyString` |  | No | The type of the term. |

## `TimeSeriesSpecificationEligibilityScheduleType`

Represents a schedule for time series specification eligibility within a contract. Note: This type is a stub, and will be fleshed out in the future.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `effectivePeriod` | `RateGroupEligibilityPeriodType` |  | No | The period during which this eligibility is effective. |
| `isEligible` | `Boolean` |  | No | Indicates if the time series specification is eligible. |
| `productCode` | `String` |  | No | The product code associated with the time series specification. |
| `timeSeriesSpecificationCode` | `String` |  | No | The time series specification code. |

## `TransactionAmountType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `gross` | `Int` |  | No | The gross amount (in minor currency units). |
| `net` | `Int` |  | No | The net amount (in minor currency units). |
| `tax` | `Int` |  | No | The amount of tax (in minor currency units). |

## `TransactionConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[TransactionConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `TransactionConnectionTypeEdge`

A Relay edge containing a `TransactionConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `TransactionType` |  | No | The item at the end of the edge |

## `TransferLeadOpportunities`

The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `opportunitiesTransferred` | `Int` |  | No | Number of opportunities transferred. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `TransferLedgerBalance`

Trigger balance transfer between accounts. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3823: Unauthorized. - KT-CT-9701: Balance transfer to same account is not allowed. - KT-CT-9702: Balance transfer is not support for debit account with Zero balance. - KT-CT-9703: Balance transfer is not supported for debit account. - KT-CT-9704: Balance transfer amount should be non-zero. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `balanceTransfer` | `AccountBalanceTransferType` |  | No | Balance transfer details. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `TransferLoyaltyPointsBetweenUsers`

Transfer Loyalty Points between users. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9209: Negative Loyalty Points balance. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `pointsTransferred` | `Int` |  | No | The number of loyalty points that were transferred. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `Trigger`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accounts` | `AccountConnectionTypeConnection!` | `before: String, after: String, first: Int, last: Int` | No | The accounts related to this trigger. |
| `accountsLinkedAt` | `DateTime` |  | No | The datetime that account linking was completed for this trigger. If null, the accounts field will be empty because linking hasn't occurred yet. |
| `createdAt` | `DateTime!` |  | No | The date/time that the trigger was created. |
| `id` | `String!` |  | No | The ID of the trigger. |
| `messages` | `MessageConnection!` | `before: String, after: String, first: Int, last: Int` | No | The messages created in response to this trigger. |
| `processingStatus` | `TriggerProcessingStatus!` |  | No | The current processing status of this trigger. |
| `triggerTypeCode` | `String!` |  | No | The trigger type code for this trigger. |

## `TriggerCollectionProcessMessage`

Send a communication for a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `triggerResult` | `TriggerCollectionProcessMessageOutput` |  | No | Details of the triggered communication. |

## `TriggerCollectionProcessMessageOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fuguTriggerId` | `String` |  | No | The unique identifier of the triggered communication. |

## `TriggerPostUploadOperations`

The possible errors that can be raised are: - KT-CT-8710: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `operationsTriggered` | `Boolean` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UnenrollAccountFromLoyaltyProgram`

Unenroll an account from the loyalty program. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9220: Ineligible loyalty points unenrollment. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `outcome` | `UnenrollAccountFromLoyaltyProgramOutcome` |  | No | Outcome of the loyalty points campaign enrollment. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UnenrollAccountFromLoyaltyProgramOutcome`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `hasUnenrolled` | `Boolean` |  | No | Indicates whether the account has been unenrolled from the loyalty points campaign. |

## `UnsupportedCombination`

A step that indicates the selected device is not compatible with the users existing devices. This step cannot be completed and the user must select different device options to continue.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |

## `UpdateAPIException`

The possible errors that can be raised are: - KT-CT-7804: No fields present in the input for updating the APIException. - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-7809: Update results in no changes to API Exception. - KT-CT-7805: Too many tags associated with this API Exception. - KT-CT-7806: Cannot create duplicate tags for the same API exception. - KT-CT-7801: Received an invalid operationsTeamId. - KT-CT-7811: Received an invalid assignedUserId. - KT-CT-7812: Support user is inactive. - KT-CT-7814: Received an invalid accountNumber. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `apiException` | `APIExceptionType` |  | No | The updated APIException. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAPIExceptionNote`

The possible errors that can be raised are: - KT-CT-7807: Received an invalid apiExceptionNoteId. - KT-CT-7808: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `apiException` | `APIExceptionType` |  | No | The updates APIExceptionNote. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAccountBillingAddress`

The possible errors that can be raised are: - KT-CT-4145: Invalid address. - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | The updated account. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAccountBillingEmail`

Update the billing email for the input account number to the received email value. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4122: Invalid email. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `AccountInterface` |  | No | Account that was changed. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAccountConsents`

Update the consents for an account using consent management system The possible errors that can be raised are: - KT-CT-9014: Duplicate consent. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-9018: Account not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `consents` | `[ConsentType!]!` |  | No | Consents linked to this account. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAccountReference`

Update a reference for a particular account and namespace. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8311: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountReference` | `AccountReferenceType` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAccountReferralStatus`

Update the status of an AccountReferral. Status transitions can only move forward: - Pending -> Paid (allowed) - Pending -> Cancelled (allowed) - Paid -> any (not allowed) - Cancelled -> any (not allowed) The possible errors that can be raised are: - KT-CT-6712: Invalid reference. - KT-CT-6732: Invalid referral status transition. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountReferral` | `ReferralType` |  | No | The updated account referral instance. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAccountUser`

Update AccountUser and ESP AccountUserDetails The possible errors that can be raised are: - KT-ES-5410: Invalid data. - KT-CT-5414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `viewer` | `EspAccountUserType` |  | No | Updated user. |

## `UpdateAccountUserCommsPreferencesMutationPayload`

Update the account user comms preferences.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientMutationId` | `String` |  | No |  |
| `commsPreferences` | `AccountUserCommsPreferences` |  | No |  |
| `emailFormat` | `String` |  | No |  |
| `errors` | `[ErrorType]` |  | No |  |
| `fontSizeMultiplier` | `Float` |  | No |  |
| `isOptedInMeterReadingConfirmations` | `Boolean` |  | No |  |
| `isOptedInToClientMessages` | `Boolean` |  | No |  |
| `isOptedInToOfferMessages` | `Boolean` |  | No |  |
| `isOptedInToRecommendedMessages` | `Boolean` |  | No |  |
| `isOptedInToSmsMessages` | `Boolean` |  | No |  |
| `isOptedInToThirdPartyMessages` | `Boolean` |  | No |  |
| `isOptedInToUpdateMessages` | `Boolean` |  | No |  |
| `isUsingInvertedEmailColours` | `Boolean` |  | No |  |
| `preferredHoldMusic` | `String` |  | No |  |

## `UpdateAccountUserConsents`

Update the consents from an account user using consent management system The possible errors that can be raised are: - KT-CT-9014: Duplicate consent. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-1111: Unauthorized. - KT-CT-5421: Account user not found. - KT-CT-5422: Invalid data. - KT-CT-1605: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountUserConsents` | `AccountUserConsents` |  | No | All the consents for an account user. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAccountUserMutationPayload`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `clientMutationId` | `String` |  | No |  |
| `dateOfBirth` | `Date` |  | No |  |
| `email` | `String` |  | No |  |
| `errors` | `[ErrorType]` |  | No |  |
| `familyName` | `String` |  | No |  |
| `givenName` | `String` |  | No |  |
| `landline` | `String` |  | No |  |
| `mobile` | `String` |  | No |  |
| `pronouns` | `String` |  | No |  |

## `UpdateActivePurchase`

The possible errors that can be raised are: - KT-CT-8225: Received an invalid purchaseId. - KT-CT-8226: The provided purchase is not active. - KT-CT-8206: Invalid data. - KT-CT-8227: Available grants could not be applied. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `goodsPurchase` | `GoodsPurchase` |  | No | Goods purchase updated. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAffiliateLink`

Update an affiliate link of an existing sales agent. The possible errors that can be raised are: - KT-CT-7711: Invalid data. - KT-CT-7713: Invalid data. - KT-CT-7714: Invalid data. - KT-CT-7715: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `affiliateLink` | `AffiliateLinkType` |  | No | The updated affiliate link. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAffiliateOrganisation`

Update an affiliate organisation. The possible errors that can be raised are: - KT-CT-7717: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `affiliateOrganisation` | `AffiliateOrganisationType` |  | No | The updated affiliate organisation. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAgentAuxiliaryStatus`

The possible errors that can be raised are: - KT-CT-7813: Support user not found with that username. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean` |  | No | Whether the auxiliary status was successfully updated. |

## `UpdateAgreementPeriod`

Update the period of an agreement. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-1501: Agreement not found. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1504: Account does not match with the agreement. - KT-CT-1505: Unable to edit agreement. - KT-CT-1506: Agreement period is not within the supply and property period. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | Account responsible for the update agreement. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAgreementRescission`

Update an agreement rescission. This mutation allows updating the status and tracking information for an agreement rescission process. Updates are not allowed if the rescission has already been completed. The possible errors that can be raised are: - KT-CT-14101: Agreement rescission not found. - KT-CT-14102: Cannot update completed agreement rescission. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreementRescission` | `AgreementRescissionType` |  | No | The updated agreement rescission instance. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAgreementRollover`

The possible errors that can be raised are: - KT-CT-4910: No product exists with the given input. - KT-CT-13705: Agreement rollover not found. - KT-CT-13706: Agreement rollover has an invalid status for this operation. - KT-CT-13707: Agreement rollover has an invalid type for this operation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `agreementRollover` | `AgreementRolloverType` |  | No | The update agreement rollover. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateAutoTopUpAmount`

The possible errors that can be raised are: - KT-CT-3815: No active payment schedule found for this account. - KT-CT-3941: Invalid data. - KT-CT-3942: An unexpected error occurred. - KT-CT-3947: An unexpected error occurred. - KT-CT-3953: The payment schedule is not a balance triggered schedule. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3822: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `schedule` | `PaymentScheduleType` |  | No | The new schedule created. |

## `UpdateBillingAddress`

This new mutation updates the user billing address. The possible errors that can be raised are: - KT-ES-4118: Invalid data. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean` |  | No | A flag that ensures changes have been made. |

## `UpdateBillingDetails`

This mutation updates the user billing details. The possible errors that can be raised are: - KT-ES-4119: Invalid data. - KT-ES-1130: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean` |  | No | A flag that ensures changes have been made. |

## `UpdateCollectionProcessRecordToActive`

Update the Collection Process Record from raised status to active The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11202: No External reference provided. - KT-CT-11207: Unsupported external source for collection process. - KT-CT-11218: External reference cannot be updated once it has been set. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessActivated` | `UpdateCollectionProcessRecordToActiveOutputType` |  | No | Whether the collection process was successfully updated. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateCollectionProcessRecordToActiveOutputType`

Output for updating a Collection process Record to Active.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `number` | `String` |  | No | The number of the collection process record. |
| `status` | `CollectionProcessRecordStatusTypes` |  | No | The current status of the collection process record. |

## `UpdateCollectionProcessRecordToComplete`

Update the Collection Process Record from raised status to complete The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11203: No Completion reason provided. - KT-CT-11204: No Completion details provided. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `collectionProcessComplete` | `UpdateCollectionProcessRecordToCompleteOutputType` |  | No | Whether the collection process was successfully updated. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateCollectionProcessRecordToCompleteOutputType`

Output for updating a Collection process Record to Complete.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `number` | `String` |  | No | The number of the collection process record. |
| `status` | `CollectionProcessRecordStatusTypes` |  | No | The current status of the repayment request. |

## `UpdateCommsDeliveryPreference`

Update the comms delivery preference for the input account number to the received commsDeliveryPreference value. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4136: Cannot set comms preference to email when account has no email. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `AccountInterface` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateDCAProceeding`

The possible errors that can be raised are: - KT-CT-11610: unable to edit the debt collection proceeding. - KT-CT-11604: Active debt collection proceeding does not exist for account. - KT-CT-11605: Multiple active Proceeding's found for same agency and campaign on account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `dcaProceedingUpdateStatus` | `DCAProceedingUpdateStatus` |  | No | Whether the update has been applied. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateDocumentAccessibilityPreference`

Update the document accessibility preference for the input account number to the received documentAccessibilityPreference value. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `account` | `Account` |  | No | Account that was changed. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateLeadAssignment`

The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `updatedLeadData` | `JSONString` |  | No | Arguments passed. |

## `UpdateLeadDetails`

The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-8912: Funnel not found. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8935: National ID bad input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `updatedLeadData` | `JSONString` |  | No | Arguments passed. |

## `UpdateLeadStage`

The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-8914: Stage not found. - KT-CT-8915: Stages are not in the same funnel. - KT-CT-8916: Current stage mismatch. - KT-CT-8917: Stage transition not allowed. - KT-CT-8918: Stage precondition not met. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `updatedLeadData` | `JSONString` |  | No | Arguments passed. |

## `UpdateMessageTags`

The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-7614: The Ink tag was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `tags` | `[InkTag!]!` |  | No | Confirmed tags. |

## `UpdateMetadata`

Update existing metadata on an object. The possible errors that can be raised are: - KT-CT-4323: Unauthorized. - KT-CT-8413: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `metadata` | `Metadata` |  | No |  |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateNotesOnOpportunity`

The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `opportunityNumber` | `String` |  | No | The number of the opportunity. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateOfferGroupOnOpportunity`

The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `opportunityNumber` | `String` |  | No | The number of the opportunity. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateOnSiteJobsAppointment`

The possible errors that can be raised are: - KT-CT-13001: Appointment does not exist. - KT-CT-13043: Cannot update appointment as it has terminal status. - KT-CT-13044: Failed to update appointment slot. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13039: Cancellation fields require CANCELLED status. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13062: Datetime field must be timezone-aware. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `onSiteJobsAppointment` | `OnSiteJobsAppointmentType` |  | No | The Appointment that was updated. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateOnSiteJobsRequest`

The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13035: Request is inactive. - KT-CT-13038: Invalid request status. - KT-CT-13040: Agent not set on request. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `onSiteJobsRequest` | `OnSiteJobsRequestType` |  | No | The updated request. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateOpportunityAssignment`

The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8903: Unable to update opportunity. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `updatedOpportunityData` | `JSONString` |  | No | Arguments passed. |

## `UpdateOpportunityDetails`

The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8930: Unable to parse address. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8912: Funnel not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `updatedData` | `JSONString` |  | No | Arguments updated. |

## `UpdateOpportunityExtraDetails`

The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8926: Unable to create opportunity. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `extraDetails` | `JSONString` |  | No | The opportunity's extra details to be added or updated. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdateOpportunityStage`

The possible errors that can be raised are: - KT-CT-8903: Unable to update opportunity. - KT-CT-8910: Received opportunity current stage is not valid. - KT-CT-8914: Stage not found. - KT-CT-8915: Stages are not in the same funnel. - KT-CT-8916: Current stage mismatch. - KT-CT-8917: Stage transition not allowed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `message` | `String` |  | No | Placeholder success message for now. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `UpdatePassword`

Update user's password. Note this is different from the ResetPassword mutation, which is used to reset a password when the user has forgotten it. This mutation is used to update the password when the user is already authenticated and wants to change their password. Ideally, this mutation would simply receive a "new_password" and use the current password update usecase, but, until we're ready for a breaking change, we'll need to use the Django form to also validate the old password and two new passwords. The possible errors that can be raised are: - KT-CT-5460: Old password is invalid. - KT-CT-5450: Password is invalid. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `viewer` | `EspAccountUserType` |  | No | The currently authenticated user. This field requires the `Authorization` header to be set. |

## `UpdatePaymentDetails`

This mutation updates the user payment details. The possible errors that can be raised are: - KT-ES-4120: Invalid data. - KT-ES-1130: Unauthorized. - KT-ES-3910: Payment instruction couldn't be created or was cancelled. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `success` | `Boolean` |  | No | A flag that ensures changes have been made. |

## `UpdateProductPricesOutput`

Rate group prices for a product.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `prices` | `[RateGroupPrices!]!` |  | No | The rate group prices. |

## `UpdateSiteworksRequest`

The possible errors that can be raised are: - KT-CT-4231: Unauthorized. - KT-CT-4232: Status passed is not valid. - KT-CT-4233: Request does not exist. - KT-CT-4234: Terminated Request cannot be updated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `siteworksRequest` | `CoreSiteworksRequestType` |  | No | The siteworks request after the update. |

## `UpdateUserMutation`

The possible errors that can be raised are: - KT-CT-5413: Invalid data. - KT-CT-5414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `viewer` | `EspAccountUserType` |  | No |  |

## `UploadPostRequest`

Information that should be used in the POST request to the S3 API. For more details please see [this](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file).

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `fields` | `JSONString!` |  | No |  |
| `key` | `String!` |  | No |  |
| `url` | `String!` |  | No |  |

## `UpsideDispatchMetaType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `location` | `String` |  | No | Present for completed dispatches, otherwise `null`. The only relevant value is `AT_HOME` if present. |
| `source` | `String` |  | No | Present for planned dispatches, otherwise `null`. Value can be `smart-charge`, `test-charge` or `bump-charge`. |

## `UpsideDispatchType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `delta` | `Decimal` |  | No | Energy in kWh (import has a negative value). |
| `deltaKwh` | `Int` |  | Yes (The 'deltaKwh' field is deprecated. `delta` has replaced `deltaKwh` for increased precision. - Marked as deprecated on 2024-04-19. - Scheduled for removal on or after 2025-01-01.) | This field has been replaced by `delta`. |
| `end` | `DateTime!` |  | No | The end time of the dispatch. |
| `endDt` | `String` |  | Yes (The 'endDt' field is deprecated. `end` has replaced `end_dt` for improved typing. - Marked as deprecated on 2024-04-19. - Scheduled for removal on or after 2025-01-01.) | This field has been replaced by `end`. |
| `meta` | `UpsideDispatchMetaType` |  | No |  |
| `start` | `DateTime!` |  | No | The start time of the dispatch. |
| `startDt` | `String` |  | Yes (The 'startDt' field is deprecated. `start` has replaced `start_dt` for improved typing. - Marked as deprecated on 2024-04-19. - Scheduled for removal on or after 2025-01-01.) | This field has been replaced by `start`. |

## `UserActionReason`

A type that returns a user action that needs to be completed for the device to be successfully registered.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `String` |  | No | Description of the required user action. |
| `uri` | `String` |  | No | An optional uri that, if provided, can navigate the user to where they can resolve this required action. |
| `userAction` | `String` |  | No | Reference key to the required user action. |

## `UserActionRequired`

A type that returns user actions that need to be completed for the device to be successfully registered

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `userActions` | `[UserActionReason]` |  | No | List of actions the user must resolve in order for the device to be registered. |

## `UserInputRequired`

A type that returns user inputs that need to be provided for the device to be successfully registered

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `userInputs` | `[UserInputType]` |  | No | A list of requested inputs for a user to provide in order for the onboarding journey to continue. |

## `UserInputType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `description` | `String` |  | No | Human friendly description of the requested input. |
| `isRequired` | `Boolean` |  | No | True if the requested user input is required. |
| `isValidated` | `Boolean` |  | No | True if the submitted user input has been successfully validated. |
| `key` | `String` |  | No | Identifier for the requested user input. |
| `value` | `String` |  | No | The value that has been submitted for this input. Can be a string, integer, or boolean. |

## `UserManagedPayment`

Represents the preference of the user to pay himself, instead of get charged.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `forPaymentsAfter` | `String` |  | No | The start time of the payment preference. |

## `UserVehiclesType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `information` | `VehicleInformationType` |  | No |  |
| `vehicleId` | `String` |  | No |  |

## `ValidateEmail`

Validate whether a user's email is a valid email via the Kickbox API.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isValid` | `Boolean` |  | No | Whether the email is valid or not. |

## `ValidateMfaDevice`

Validate multi-factor authentication (MFA) devices for user. The possible errors that can be raised are: - KT-CT-1150: MFA device not found. - KT-CT-1151: MFA device not found. - KT-CT-1152: Invalid MFA token. - KT-CT-1155: Enabled backup device is needed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceIsValid` | `Boolean` |  | No | Flag to indicate if the device has been verified, so it can be used for MFA. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `ValidatePhone`

Validate whether a user's phone number is a valid phone number.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isValid` | `Boolean` |  | No | Whether the phone number is valid or not. |

## `ValidityPeriod`

Represents a validity period defined by specific start and end date times.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `end` | `DateTime` |  | No | The end date and time of the period. Null indicates an open-ended period. |
| `start` | `DateTime` |  | No | The start date and time of the period. |

## `VariantProfile`

Object representing a variant profile.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `characteristicValues` | `JSONString!` |  | No | The characteristic values for the variant. |
| `schemeLabels` | `JSONString` |  | No | The scheme labels for the variant. |

## `VaryContractTermsOutput`

Output type for varying contract terms.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `contract` | `Contract` |  | No | The contract with the varied terms. |

## `VehicleChargingPreferencesType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `maximumSocPercentage` | `Int` |  | No | The maximum state of charge (soc) %, if available. |
| `minimumSocPercentage` | `Int` |  | No | The minimum state of charge (soc) %, if available. |
| `weekdayTargetSoc` | `Int` |  | No |  |
| `weekdayTargetTime` | `String` |  | No |  |
| `weekendTargetSoc` | `Int` |  | No |  |
| `weekendTargetTime` | `String` |  | No |  |

## `VehicleInformationType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `brand` | `String` |  | No |  |
| `displayName` | `String` |  | No | The (user chosen) display name of the vehicle, if available. |
| `model` | `String` |  | No | The model name of the vehicle, if available (e.g. i3s 120). |
| `vin` | `String` |  | No |  |
| `year` | `Int` |  | No | The year of the vehicle model, if available. |

## `VerificationProcess`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `status` | `String` |  | No | Verification process status. |
| `type` | `String` |  | No | Verification type. |
| `userNumber` | `String` |  | No | Customer with pending verification. |

## `VerifyCustomer`

Verify a customer using the provided code and verification type. The possible errors that can be raised are: - KT-CT-4191: Error while verifying the customer. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `user` | `EspAccountUserType` |  | No | The currently authenticated user. |

## `VerifyEmail`

The possible errors that can be raised are: - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `isVerified` | `Boolean` |  | No | Whether the email is verified. |
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |

## `VerifyIdentity`

The possible errors that can be raised are: - KT-CT-1145: Account/user details do not match. - KT-CT-1113: Disabled GraphQL field requested.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `token` | `String!` |  | No | An expiring token that can be used to request to update the user's email address. |

## `VoiceCampaignConnectionTypeConnection`

Paginator of Voice Campaigns

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[VoiceCampaignConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `VoiceCampaignConnectionTypeEdge`

A Relay edge containing a `VoiceCampaignConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `VoiceCampaignType` |  | No | The item at the end of the edge |

## `VoiceCampaignItemConnectionTypeConnection`

Paginator of Campaign Items

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[VoiceCampaignItemConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `VoiceCampaignItemConnectionTypeEdge`

A Relay edge containing a `VoiceCampaignItemConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `VoiceCampaignItemType` |  | No | The item at the end of the edge |

## `VoiceCampaignItemType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `accountId` | `ID` |  | No | The account ID associated with the item. If the phone number for the item is not set, the account ID will be used to determine the phone number to call. |
| `callWindowEnd` | `DateTime` |  | No | Together with `call_window_start`, this determines the time window in which the item should be called. Specified as ISO 8601 format. |
| `callWindowStart` | `DateTime` |  | No | Together with `call_window_end`, this determines the time window in which the item should be called. Specified as ISO 8601 format. |
| `id` | `ID` |  | No | The ID of the campaign item. |
| `metadata` | `JSONString` |  | No | Metadata about the item. This enables items to be filtered based on additional information such as location. It is a dictionary of key-value pairs, with both keys and values being strings. |
| `phoneNumber` | `String` |  | No | The phone number of the campaign item. This is used to determine the phone number to call when the item is processed. If it is not set, the account ID will be used instead to call the phone number associated with the account. |
| `status` | `CampaignItemStatus!` |  | No | The status of the campaign item that determines what actions can be taken on it. "UNASSIGNED": An item that is ready to be assigned to an agent "ASSIGNED": An item that is assigned to an agent and ready to contact "IN_PROGRESS": An item where a call is currently in progress "COMPLETE": An item has been contacted, and does not need to be re-contacted "REMOVED": An item that was removed without being contacted |

## `VoiceCampaignType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `campaignItems` | `VoiceCampaignItemConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The items that are part of the campaign. These are the items that contain information about what phone numbers or accounts to call while this campaign is active. |
| `campaignType` | `TypeOfVoiceCampaign` |  | No | The type of campaign, e.g. preview or predictive. |
| `customOutboundPhoneNumber` | `String` |  | No | If appropriate, a custom number to use as the caller id for calls from this campaign. |
| `description` | `String` |  | No | Additional information to describe the purpose of the campaign. |
| `id` | `ID` |  | No | The ID of the campaign. |
| `name` | `String!` |  | No | The name of the campaign. This is used to identify the campaign in the system, and must be unique. |
| `preventDuplicateRecords` | `Boolean` |  | No | Flag to indicate whether not to create a duplicate record when uploading campaign items that already exist for a given account number and/or phone number |
| `status` | `CampaignStatus` |  | No | The status of the campaign. Indicates whether calls can be made for items in the campaign or not. |
| `tags` | `CallTagConnectionTypeConnection` | `before: String, after: String, first: Int, last: Int` | No | The call tags that can be used within this campaign. |

## `VoucherPurchaseConnectionTypeConnection`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `edgeCount` | `Int!` |  | No | Number of nodes in the edge. |
| `edges` | `[VoucherPurchaseConnectionTypeEdge]!` |  | No | Contains the nodes in this connection. |
| `pageInfo` | `PageInfo!` |  | No | Pagination data for this connection. |
| `totalCount` | `Int!` |  | No | Total number of nodes. |

## `VoucherPurchaseConnectionTypeEdge`

A Relay edge containing a `VoucherPurchaseConnectionType` and its cursor.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `cursor` | `String!` |  | No | A cursor for use in pagination |
| `node` | `VoucherPurchaseType` |  | No | The item at the end of the edge |

## `VoucherPurchaseType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `availableFrom` | `Date` |  | No | When the voucher becomes available to be redeemed. |
| `balance` | `Int` |  | No | The current balance left in the voucher. |
| `charge` | `AccountChargeType` |  | No | The amount charged for the voucher. |
| `chargeBalanceTransfer` | `AccountBalanceTransferType` |  | No | A balance transfer for the voucher charge, if any. |
| `clientParams` | `JSONString` |  | No | Additional metadata from client sources stored against the voucher. This data is not structural and won't be relied on by Kraken internally. |
| `displayName` | `String` |  | No | Display name for the voucher purchase. |
| `id` | `ID` |  | No | The purchase ID. |
| `payment` | `AccountPaymentType` |  | No | The payment associated with the voucher purchase, if any. |
| `purchasedAt` | `DateTime` |  | No | When the purchase was performed. |
| `redemptions` | `[VoucherRedemptionType]` |  | No | Fetch the redemptions for this voucher. |
| `refundedAt` | `DateTime` |  | No | When the voucher was refunded, if it was refunded. |
| `voucherValue` | `Int` |  | No | The value of the voucher in cents. |

## `VoucherRedemptionType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `claimedAt` | `DateTime` |  | No | When the redemption was claimed. |
| `credit` | `AccountCreditType` |  | No | The amount credited for the voucher redemption. |
| `id` | `ID` |  | No | The redemption ID. |

## `VouchersBalanceDetail`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `redeemableInFuture` | `Int` |  | No | The balance from vouchers that will be redeemable in future. |
| `redeemableToday` | `Int` |  | No | The balance from vouchers that can be redeemable today. |

## `WaitForLiveIntegration`

Indicates a step where the integration is pending activation. Progress to the next onboarding step is blocked until the integration becomes active.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |
| `isLive` | `Boolean` |  | No | Returns `true` if the device integration is supported by us, `false` otherwise. |

## `WaitForTransition`

A generic step that can be used to hold an onboarding wizard until the device has transitioned from one onboarding state to another. Generally, this step should be completed via a KF AMI event handler after the device has been registered and transitioned to the desired state.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `id` | `ID` |  | No | A unique identifier for this onboarding step. |

## `WaterFiltersOutput`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `deviceId` | `String` |  | No | Serial number. |
| `marketSupplyPointId` | `String` |  | No | Meter point reference. |
| `readingFrequencyType` | `ReadingFrequencyType` |  | No | The frequency of the reading. |

## `WhatsAppTextMessage`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `body` | `String!` |  | No | Whatsapp text message body. |

## `WithdrawDunning`

The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11301: Account not in a dunning process for the given path name. - KT-CT-11302: No active dunning process found. - KT-CT-11303: Multiple active dunning processes found. - KT-CT-11306: Withdrawing the dunning process failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `possibleErrors` | `[PossibleErrorType]` |  | Yes (The 'possibleErrors' field is deprecated. Please use the 'possibleErrors' query or the 'X-Kraken-Possible-Errors' header instead. - Marked as deprecated on 2025-01-31. - Scheduled for removal on or after 2025-03-01.) | Field with the possible errors of the query/mutation. |
| `withdrawSuccessful` | `Boolean` |  | No | Whether the dunning process was withdrawn successfully. |

## `WorkScheduleType`

| Field | Type | Args | Deprecated | Description |
|---|---|---|---|---|
| `identifier` | `String!` |  | No | The identifier of the work schedule (also known as the 'slug'). |
| `isOpen` | `Boolean!` |  | No | Whether the work schedule is currently open. |
| `isPublicHoliday` | `Boolean!` |  | No | Whether today is a public holiday, according to the work schedule. |
| `name` | `String!` |  | No | Name of the work schedule. |
| `openOrClosedReason` | `WorkScheduleOpenOrClosedReason!` |  | No | The reason the Work Schedule is open or closed. |

