# Queries

Total `Query` operations: **183**

## `a629Details(cups: String!, nif: String)`

- Return type: `A629Details`
- Description: Retrieve A629 supply point information including acceptance, rejection or error details. The possible errors that can be raised are: - KT-ES-4504: A529 requests are currently not implemented for the provided DNO. - KT-ES-4505: A529 requests are currently not configured for the provided DNO. - KT-ES-4506: Unauthorized A529 call. - KT-ES-4507: Unexpected error retrieving A529 details. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `cups` | `String!` |  | Universal Supply Point code. |
| `nif` | `String` |  | Spanish tax identification number. |

## `account(accountNumber: String!)`

- Return type: `Account`
- Description: Get details about an account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `accountBillingInfo(accountNumber: String!)`

- Return type: `AccountBillingInfo`
- Description: Get details about an account's billing info. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number to retrieve the billing info. |

## `accountChargeReasons`

- Return type: `[ChargeReasonType]`
- Description: Available reasons for use in account charge mutations.

## `accountContract(identifier: String, accountNumber: String, version: Int)`

- Return type: `Contract`
- Description: Get details about an account contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10005: Missing required parameter: either identifier or accountNumber must be provided. - KT-CT-10006: Account not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `identifier` | `String` |  | The identifier of the contract. |
| `accountNumber` | `String` |  | The account number to find the contract for. |
| `version` | `Int` |  | The version of the contract. |

## `accountCreditReasons`

- Return type: `[CreditReasonType]`
- Description: Available reasons for use in account credit mutations.

## `accountIoEligibility(accountNumber: String!, propertyId: Int)`

- Return type: `AccountIoEligibility`
- Description: Determines whether an account is eligible to register devices with SmartFlex.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |
| `propertyId` | `Int` |  | The property's id where the device will be registered to. Note: in future, eligibility checks will be dependent on the property id and it will be a required input. |

## `accountPaymentInfo(accountNumber: String!)`

- Return type: `AccountPaymentInfo`
- Description: Get details about an account's payments info. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number to retrieve the payment info. |

## `accountReference(value: String)`

- Return type: `[AccountReferenceType]`
- Description: List of matching account references. The possible errors that can be raised are: - KT-CT-8310: Invalid data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `value` | `String` |  | Filter account references by this value. |

## `accountUser(email: String, number: ID, externalId: ID)`

- Return type: `EspAccountUserType`
- Description: Retrieve an account user. The possible errors that can be raised are: - KT-CT-5418: Account user not found. - KT-CT-5415: Account user not found. - KT-CT-5423: Account user not found. - KT-CT-5424: Invalid data. - KT-CT-5421: Account user not found. - KT-CT-5425: Account user not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `email` | `String` |  | Email associated with an account user. |
| `number` | `ID` |  | Kraken number associated with an account user. |
| `externalId` | `ID` |  | External ID associated with an account user. |

## `accounts(phoneNumber: String, portfolioNumber: String)`

- Return type: `[Account]`
- Description: Get details about multiple accounts. The possible errors that can be raised are: - KT-CT-4184: Exactly one of phoneNumber or portfolioNumber must be provided. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `phoneNumber` | `String` |  | A phone number to find accounts associated with. |
| `portfolioNumber` | `String` |  | A portfolio number to find accounts associated with. |

## `accountsSearch(searchTerms: AccountSearchInputType, maxResults: Int = 20)`

- Return type: `[AccountSearchItemType]`
- Description: Search for account that are already in Kraken and match the search terms. The possible errors that can be raised are: - KT-CT-4183: One of more search terms failed validations. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `searchTerms` | `AccountSearchInputType` |  | Search operators. |
| `maxResults` | `Int` | `20` | The maximum number of results to return. |

## `activeAffiliateReferralScheme(subdomain: String!, accountType: ReferralSchemeAccountTypeOptions)`

- Return type: `ReferralSchemeType`
- Description: Return the current active referral reward scheme of a given affiliate organisation, if any exists.

| Arg | Type | Default | Description |
|---|---|---|---|
| `subdomain` | `String!` |  | The affiliate link subdomain. |
| `accountType` | `ReferralSchemeAccountTypeOptions` |  | The account type for which to get the referral scheme. |

## `activeDomesticSignupRewardScheme`

- Return type: `ReferralSchemeType`
- Description: Return the current active signup referral reward scheme with the given code, if any exists.

## `activeSalesChannels(activeFrom: DateTime, activeTo: DateTime)`

- Return type: `[SalesChannelType]`
- Description: A list of active sales channels. The possible errors that can be raised are: - KT-CT-12702: Invalid datetime range. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `activeFrom` | `DateTime` |  | The datetime from which to filter active sales channels. |
| `activeTo` | `DateTime` |  | The datetime up to which to filter active sales channels. |

## `addressSearch(address: String!, postcode: String)`

- Return type: `[CadastreRichAddressType!]`
- Description: Search for addresses in the cadastre that match the search term. The possible errors that can be raised are: - KT-ES-4403: Address search service not enabled. - KT-ES-4404: Address search service unavailable. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `address` | `String!` |  | The partial address, which will be fuzzy-matched against the cadastre. |
| `postcode` | `String` |  | The postcode to filter the search results by. |

## `affiliateLink(subdomain: String!)`

- Return type: `AffiliateLinkType!`
- Description: Link object for an affiliate organization. The possible errors that can be raised are: - KT-CT-7713: Invalid data. - KT-CT-7718: Affiliate link is expired. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `subdomain` | `String!` |  | The affiliate link subdomain. |

## `affiliateLinks(agentContactEmail: String!)`

- Return type: `[AffiliateLinkType!]!`
- Description: Links (urls) for the affiliate organizations.

| Arg | Type | Default | Description |
|---|---|---|---|
| `agentContactEmail` | `String!` |  | Email address of the affiliate agent. |

## `affiliateOrganisation(id: Int, number: String)`

- Return type: `AffiliateOrganisationType`
- Description: Return the details of a given affiliate organization, if any exists. The possible errors that can be raised are: - KT-CT-7701: The affiliate organisation was not found. - KT-CT-7702: Either id or number must be provided. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `Int` |  | The affiliate organisation ID. |
| `number` | `String` |  | The affiliate organisation number. |

## `affiliateProducts(organizationName: String!)`

- Return type: `[AffiliateProductType]`
- Description: Information on products for affiliate organizations. The possible errors that can be raised are: - KT-ES-7813: Affiliate product information not available. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `organizationName` | `String!` |  | Organization name. |

## `agentCallCenterStatus(supportUserName: String!)`

- Return type: `AgentCallCenterStatusType!`
- Description: Get the call center status for a given agent. The possible errors that can be raised are: - KT-CT-7813: Support user not found with that username. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `supportUserName` | `String!` |  | The support user name. |

## `agreement(id: ID!)`

- Return type: `Agreement`
- Description: Get an agreement by id.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` |  | The agreement id. |

## `agreementRollover(number: String!)`

- Return type: `AgreementRolloverType`
- Description: Get an agreement rollover by its number. The possible errors that can be raised are: - KT-CT-13705: Agreement rollover not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `number` | `String!` |  | Number of the agreement rollover. |

## `agreementsForRollover(daysBeforeExpiration: Int!, windowSize: Int!)`

- Return type: `[CommonAgreementType]`
- Description: Get agreements eligible for the rollover process.

| Arg | Type | Default | Description |
|---|---|---|---|
| `daysBeforeExpiration` | `Int!` |  | Days before the agreement expiration. |
| `windowSize` | `Int!` |  | Window size in days. |

## `apiBrownouts(input: APIBrownoutInput, before: String, after: String, first: Int, last: Int)`

- Return type: `APIBrownoutConnection`
- Description: Get brownouts by status.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `APIBrownoutInput` |  | Statuses to filter for. Otherwise return active and upcoming brownouts. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `apiExceptions(input: APIExceptionQueryInput, before: String, after: String, first: Int, last: Int)`

- Return type: `APIExceptionConnectionTypeConnection`
- Description: Get a connection containing API Exceptions.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `APIExceptionQueryInput` |  | Fields to filter for. Otherwise don't filter at all. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `appSessions(postcode: String, subdomain: String, before: String, after: String, first: Int, last: Int)`

- Return type: `AppSessionConnectionTypeConnection!`
- Description: App sessions recorded at the specified postcode or for the specified affiliate link subdomain.

| Arg | Type | Default | Description |
|---|---|---|---|
| `postcode` | `String` |  | The postcode of the address at which the app session was recorded. |
| `subdomain` | `String` |  | The affiliate link subdomain to filter app sessions by. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `authorizedApplications`

- Return type: `[AuthorizedApplication]`
- Description: Get all the confidential-client applications the current user has authorized.

## `availableOfferings`

- Return type: `[OfferingType]`
- Description: Get a list of actively available offerings from the catalog.

## `availableProductSwitchDates(agreementId: Int!, maxRange: Int = 365)`

- Return type: `[Date]`
- Description: Get available dates for product switch. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `agreementId` | `Int!` |  | Agreement ID. |
| `maxRange` | `Int` | `365` | The maximum number of days to look for available dates. |

## `availableProducts(marketName: String!)`

- Return type: `[SupplyProductType]`
- Description: Get available products for the given market. The possible errors that can be raised are: - KT-CT-4930: Unsupported market. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `marketName` | `String!` |  | Products available for the target market. |

## `backendScreen(screenId: ID!, params: [BackendScreenParamInputType], maxVersionSupported: Int = 1)`

- Return type: `BackendScreenType`
- Description: Get mobile screen details to render. The possible errors that can be raised are: - KT-CT-8001: No backend screen available. - KT-CT-8005: Backend screen does not support parameters. - KT-CT-8008: Incorrect or missing data necessary to build the screen. - KT-CT-8006: Error applying parameters to backend screen. - KT-CT-8009: Error translating screen content. - KT-CT-8010: Invalid step ID. - KT-CT-8011: Cannot rewind past a previous irreversible step. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `screenId` | `ID!` |  | The ID of the screen to return. |
| `params` | `[BackendScreenParamInputType]` |  | List of key-value pairs (strings) to pass as parameters to the screen. |
| `maxVersionSupported` | `Int` | `1` | The maximum version of backend screens supported by the client. |

## `backendScreenEventIds`

- Return type: `[String]`
- Description: Get all registered backend screen event IDs.

## `backendScreenIds`

- Return type: `[String]`
- Description: Get all registered backend screen IDs.

## `bankDetailsValidation(iban: NonEmptyString!)`

- Return type: `BankDetailsValidationResult`

| Arg | Type | Default | Description |
|---|---|---|---|
| `iban` | `NonEmptyString!` |  | The IBAN of the bank account. |

## `business(id: ID, details: [BusinessDetailInput])`

- Return type: `BusinessType`
- Description: Get details about a business. The possible errors that can be raised are: - KT-CT-11101: The viewer is not authorized to execute the query/mutation. Check the ownership/permissions of provided data. - KT-CT-11107: Unauthorized. - KT-CT-1605: Invalid input. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID` |  | The business ID. |
| `details` | `[BusinessDetailInput]` |  | List of business detail key-value pairs to filter by. |

## `businessAccountReferralRewardScheme(code: String!)`

- Return type: `ReferralSchemeType`
- Description: Return a business referral reward scheme for the given account referral code.

| Arg | Type | Default | Description |
|---|---|---|---|
| `code` | `String!` |  | Friend referral code. |

## `businessContract(identifier: String, accountNumber: String, version: Int)`

- Return type: `Contract`
- Description: Get details about an account contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10005: Missing required parameter: either identifier or accountNumber must be provided. - KT-CT-10006: Account not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `identifier` | `String` |  | The identifier of the contract. |
| `accountNumber` | `String` |  | The account number to find the business contract for. |
| `version` | `Int` |  | The version of the contract. |

## `call(id: ID!)`

- Return type: `CallInterface!`
- Description: Get a call for a given ID. The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` |  | The call ID. |

## `callTag(id: ID!)`

- Return type: `CallTagType!`
- Description: Get the call tag for a given ID. The possible errors that can be raised are: - KT-CT-11809: Call tag not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` |  | The call tag ID. |

## `callTags(name: String, isActive: Boolean, before: String, after: String, first: Int, last: Int)`

- Return type: `CallTagConnectionTypeConnection!`
- Description: Get call tags.

| Arg | Type | Default | Description |
|---|---|---|---|
| `name` | `String` |  | Filter by call tag name. |
| `isActive` | `Boolean` |  | Filter by active status. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `campaigns(accountNumber: String!, before: String, after: String, first: Int, last: Int)`

- Return type: `AccountCampaignConnectionTypeConnection`
- Description: The campaigns associated with this account.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `canRescindAgreement(agreementId: Int!)`

- Return type: `Boolean`
- Description: Check if an agreement can be rescinded. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `agreementId` | `Int!` |  | The ID of the agreement to check. |

## `chargePointVariants`

- Return type: `[ChargePointVariantType]`
- Description: All charge points variants.

## `collectionProcessDetails(collectionProcessRecordNumber: String!)`

- Return type: `CollectionProcessDetailsType`
- Description: Collection process record details. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11206: Unable to retrieve disconnection related data for collection process. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `collectionProcessRecordNumber` | `String!` |  | The collection process record number. |

## `complaint(complaintId: Int!)`

- Return type: `ComplaintType`
- Description: Get a complaint. The possible errors that can be raised are: - KT-CT-12301: Complaint not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `complaintId` | `Int!` |  |  |

## `completedDispatches(accountNumber: String!)`

- Return type: `[UpsideDispatchType]`
- Description: All completed device dispatches 12 hours behind, in reverse time order. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4341: Unable to fetch completed dispatches. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `consentTypes`

- Return type: `[ConsentTypeType]`
- Description: A list of the consent types available.

## `contractCreationJourney(number: String!)`

- Return type: `ContractCreationJourneyType`
- Description: Get details about a contract creation journey. The possible errors that can be raised are: - KT-CT-10017: The contract journey could not be found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `number` | `String!` |  | The number of the contract journey. |

## `contractNoteReasons(activityTypes: [ContractActivityTypeOptions])`

- Return type: `[ContractNoteReasonType]`
- Description: Get a list of contract note reasons, optionally filtered by activity types.

| Arg | Type | Default | Description |
|---|---|---|---|
| `activityTypes` | `[ContractActivityTypeOptions]` |  | Filter reasons applicable to any of the given contract activity types. |

## `contracts(filters: ContractFiltersInput!)`

- Return type: `[Contract]`
- Description: Get a list of contracts filtered by party or subject. The possible errors that can be raised are: - KT-CT-10029: Missing contract filters. - KT-CT-10030: Filter by subject is not implemented. - KT-CT-10031: Invalid party filter. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `filters` | `ContractFiltersInput!` |  | Filters to apply when querying contracts. At least one filter must be provided. |

## `contributionSchemes`

- Return type: `[ContributionSchemeType]`
- Description: Get contribution schemes.

## `costOfCharge(accountNumber: String!, frequency: DataFrequency!, startDate: Date)`

- Return type: `[CostOfChargeType]`
- Deprecated: Yes (The 'costOfCharge' field is deprecated. Use `cost` field on `SmartFlexChargingSession` instead. - Marked as deprecated on 2025-05-13. - Scheduled for removal on or after 2026-01-16. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/605/)
- Description: Aggregated cost of charge for an EV device. The possible errors that can be raised are: - KT-CT-4326: Could not get consumption cost data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |
| `frequency` | `DataFrequency!` |  | Frequency by day, week, month or year. |
| `startDate` | `Date` |  | The start date of the results required. Overrides report date (end date) if provided. |

## `cupsRegion(cups: String!)`

- Return type: `String`
- Description: Gets the region where a CUPS is physically located.

| Arg | Type | Default | Description |
|---|---|---|---|
| `cups` | `String!` |  | The CUPS to obtain information for. |

## `cupsValidationToContractAtrBased(cupsAndProductInput: CupsValidationToContractInput!)`

- Return type: `CupsValidationToContract`
- Description: Get confirmation if cups is valid to make a contract. The possible errors that can be raised are: - KT-ES-7812: Product ID does not exist. - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `cupsAndProductInput` | `CupsValidationToContractInput!` |  | Input arguments validate in chipiron. |

## `cupsValidationToContractAtrBasedV2(input: CupsValidationToContractInput!)`

- Return type: `CupsValidationToContract`
- Deprecated: Yes (The 'cupsValidationToContractAtrBasedV2' field is deprecated. Never used. Use 'cupsValidationToContractAtrBased' instead. - Marked as deprecated on 2024-05-27. - Scheduled for removal on or after 2024-07-01.)
- Description: Get confirmation if cups is valid to contract the products. The possible errors that can be raised are: - KT-ES-7812: Product ID does not exist. - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CupsValidationToContractInput!` |  | Electricity and gas cups and products to contract. |

## `customerFeedbackForms(accountNumber: String!, feedbackSource: CustomerFeedbackSourceChoices, before: String, after: String, first: Int, last: Int)`

- Return type: `CustomerFeedbackFormConnectionTypeConnection`
- Description: Returns all active customer feedback forms for the account's brand.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `feedbackSource` | `CustomerFeedbackSourceChoices` |  | Feedback sources currently supported. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `dailyWholesalePrices(start: Date, end: Date)`

- Return type: `[DailyWholesalePrice]`
- Deprecated: Yes (The 'dailyWholesalePrices' field is deprecated. Migrated to OE Backend API. - Marked as deprecated on 2025-10-27. - Scheduled for removal on or after 2025-11-10.)
- Description: Get the daily wholesale prices per hour for the given dates.

| Arg | Type | Default | Description |
|---|---|---|---|
| `start` | `Date` |  | The start date from which to get the daily wholesale prices. |
| `end` | `Date` |  | The end date until which to get the daily wholesale prices. |

## `dashboardScreen(dashboardId: ID!, accountNumber: String!, maxVersionSupported: Int! = 1, ledgerNumber: String, propertyId: String, params: [BackendScreenParamInputType])`

- Return type: `Dashboard`
- Description: Get a dashboard screen to render in the form of a json list of sections containing cards or grouped cards each with an order attribute. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-8001: No backend screen available. - KT-CT-8005: Backend screen does not support parameters. - KT-CT-8008: Incorrect or missing data necessary to build the screen. - KT-CT-8006: Error applying parameters to backend screen. - KT-CT-8009: Error translating screen content. - KT-CT-8010: Invalid step ID. - KT-CT-8011: Cannot rewind past a previous irreversible step. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `dashboardId` | `ID!` |  | The ID of the dashboard type screen to return. |
| `accountNumber` | `String!` |  | The account number of the user. |
| `maxVersionSupported` | `Int!` | `1` | The maximum version of dahshboard type screens supported by the client. |
| `ledgerNumber` | `String` |  | The ledger number associated to the account. |
| `propertyId` | `String` |  | The property id associated to the account. |
| `params` | `[BackendScreenParamInputType]` |  | List of key-value pairs (strings) to pass as parameters to the screen. |

## `defaultPaymentInstruction(accountNumber: String!, instructionType: PaymentType)`

- Return type: `PaymentInstructionType`
- Deprecated: Yes (The 'defaultPaymentInstruction' field is deprecated. Please use 'usablePaymentInstructions' on the Ledger type to get all usable instructions, or 'paymentPreferenceAtTime' on the Ledger type to get a specific one. Both require explicitly requesting a ledger. - Marked as deprecated on 2026-01-28. - Scheduled for removal on or after 2026-07-28.)
- Description: Get the default payment instruction for the account's main ledger.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `instructionType` | `PaymentType` |  | Provide an option to get either a CARD or DIRECT_DEBIT instruction. |

## `defaultRawScore(formId: Int!)`

- Return type: `Int`
- Description: Get default raw score for a customer feedback form. The possible errors that can be raised are: - KT-CT-5513: Invalid data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `formId` | `Int!` |  |  |

## `depositAgreements(accountNumber: String!)`

- Return type: `[DepositAgreementOutput]`
- Description: Get deposit agreements for a given account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `devices(accountNumber: String!, propertyId: ID, deviceId: String, integrationDeviceId: String)`

- Return type: `[SmartFlexDeviceInterface!]`
- Description: A list of devices registered to an account.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number, e.g. A-12345678. |
| `propertyId` | `ID` |  | Only list devices registered to this property. |
| `deviceId` | `String` |  | Only list the device with this ID. |
| `integrationDeviceId` | `String` |  | Only list the device with this integration device ID. |

## `domesticAccountReferralRewardScheme(code: String!)`

- Return type: `ReferralSchemeType`
- Description: Return a domestic referral reward scheme for the given account referral code.

| Arg | Type | Default | Description |
|---|---|---|---|
| `code` | `String!` |  | Friend referral code. |

## `domesticJoiningRewardScheme(code: String!)`

- Return type: `ReferralSchemeType`
- Description: Return a joining reward scheme with the given code, if it's active. A joining reward can be a signup reward or a promotional reward.

| Arg | Type | Default | Description |
|---|---|---|---|
| `code` | `String!` |  | Reward code for the scheme. |

## `domesticSignupRewardScheme(code: String!)`

- Return type: `ReferralSchemeType`
- Description: Return a signup referral reward scheme with the given code, if it's active.

| Arg | Type | Default | Description |
|---|---|---|---|
| `code` | `String!` |  | Reward code for the scheme. |

## `electricVehicles(make: String, supportedProvider: ProviderChoices, isIntegrationLive: Boolean)`

- Return type: `[ElectricVehicleType]`
- Description: All electric vehicle types and their details. The possible errors that can be raised are: - KT-CT-4343: Unable to fetch electric vehicles list for make. - KT-CT-4344: Make is not supported by provider. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `make` | `String` |  | Only return vehicle types for the specified make. |
| `supportedProvider` | `ProviderChoices` |  | Only return vehicle types supported by the specified provider, e.g. Tesla. |
| `isIntegrationLive` | `Boolean` |  | Only return vehicles that are currently integrated. |

## `electricitySupplyPoint(id: ID!)`

- Return type: `ElectricitySupplyPoint`
- Description: Get information about a supply point by its ID.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` |  | The ID of the supply point to obtain information for. |

## `eligibilityToJoinLoyaltyPointsProgram(input: LoyaltyPointsProgramEligibilityInput!)`

- Return type: `LoyaltyPointsProgramEligibilityType`
- Description: Check if an account is eligible to join the loyalty points program. The possible errors that can be raised are: - KT-CT-9202: Loyalty Points adapter not configured. - KT-CT-9218: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LoyaltyPointsProgramEligibilityInput!` |  |  |

## `eligibleDeviceTypes(accountNumber: String!, propertyId: Int)`

- Return type: `[KrakenFlexDeviceTypes]`
- Description: A list of device types that are eligible for registration.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number, e.g. A-12345678. |
| `propertyId` | `Int` |  | The property's id where the device will be registered to. Note: in future, eligible device types will be dependent on the property id and it will be a required input. |

## `embeddedNetwork(id: ID!)`

- Return type: `EmbeddedNetworkType`
- Description: Get details about an embedded network.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` |  |  |

## `energyMixData`

- Return type: `EnergyMixDataType`
- Description: The current energy generation mix.

## `enodeLinkSession(accountNumber: String, vendor: EnodeVendors)`

- Return type: `EnodeLinkSessionType`
- Deprecated: Yes (The 'enodeLinkSession' field is deprecated. Please use 'startSmartFlexOnboarding' instead. - Marked as deprecated on 2025-10-30. - Scheduled for removal on or after 2026-04-30. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/608/)
- Description: The user specific Enode link session details. The possible errors that can be raised are: - KT-CT-4328: Invalid data. - KT-CT-1111: Unauthorized. - KT-CT-4319: Unable to get Enode link session. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  |  |
| `vendor` | `EnodeVendors` |  |  |

## `estimateMeterReadings(periodStart: DateTime!, periodEnd: DateTime!, marketIdentifier: ID!, deviceId: ID, registerId: ID, before: String, after: String, first: Int, last: Int)`

- Return type: `MeterReadingEstimationReadingConnection`
- Description: Estimated meter readings.

| Arg | Type | Default | Description |
|---|---|---|---|
| `periodStart` | `DateTime!` |  | The start of the period estimated. |
| `periodEnd` | `DateTime!` |  | The end of the period estimated. |
| `marketIdentifier` | `ID!` |  | This is the unique identifier used by the market to identify the supply point. |
| `deviceId` | `ID` |  | The meter id to perform estimation on. |
| `registerId` | `ID` |  | The meter's register identifier. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `externalAccountEvents(accountNumber: String!, before: String, after: String, first: Int, last: Int)`

- Return type: `ExternalAccountEventConnectionTypeConnection`
- Description: Get a list of audit account events, of type external, for a given account.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number to filter by. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `flexPlannedDispatches(deviceId: String!)`

- Return type: `[SmartFlexDispatch]`
- Description: All planned device dispatches in time order. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4340: Unable to fetch planned dispatches. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `deviceId` | `String!` |  | The SmartFlex device ID to get the planned dispatches for. |

## `flexSupportedDevices(deviceType: KrakenFlexDeviceTypes!)`

- Return type: `FlexSupportedDevices`
- Description: Devices capable of being registered with SmartFlex.

| Arg | Type | Default | Description |
|---|---|---|---|
| `deviceType` | `KrakenFlexDeviceTypes!` |  | The device type to get the supported devices for. |

## `fraudMeterPointChecks(meterPointId: String!)`

- Return type: `FraudMeterPointCheckType`
- Description: Check if a given meter point ID is in suspicious meter point IDs list.

| Arg | Type | Default | Description |
|---|---|---|---|
| `meterPointId` | `String!` |  | The meter point ID. |

## `fraudRiskLevel(identifierValue: String!, identifierType: String!)`

- Return type: `FinancialRiskLevelType`
- Description: Check if a given ID and type have a financial risk level.

| Arg | Type | Default | Description |
|---|---|---|---|
| `identifierValue` | `String!` |  | The ID to be checked. |
| `identifierType` | `String!` |  | The type of object the ID represents. |

## `gasSupplyPoint(id: ID!)`

- Return type: `GasSupplyPoint`
- Description: Get information about a supply point by its ID.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` |  | The ID of the supply point to obtain information for. |

## `getOnSiteJobsAppointmentByExternalReference(externalReference: String!, agent: OnSiteJobsAgent!)`

- Return type: `OnSiteJobsAppointmentType`
- Description: Get appointment by external reference and agent.

| Arg | Type | Default | Description |
|---|---|---|---|
| `externalReference` | `String!` |  | The external reference of the appointment to return. |
| `agent` | `OnSiteJobsAgent!` |  | The agent for the appointment. |

## `getOnSiteJobsAppointmentById(appointmentId: UUID)`

- Return type: `OnSiteJobsAppointmentType`
- Description: Get a specific appointment by Kraken ID.

| Arg | Type | Default | Description |
|---|---|---|---|
| `appointmentId` | `UUID` |  | The Kraken ID of the appointment to return. |

## `getOnSiteJobsAppointmentSlots(appointmentBookingSessionId: UUID!, appointmentDate: Date!)`

- Return type: `OnSiteJobsAppointmentSlotResultsType`
- Description: Get appointment slot results using appointment booking session ID.

| Arg | Type | Default | Description |
|---|---|---|---|
| `appointmentBookingSessionId` | `UUID!` |  | Appointment booking session ID to fetch slots for. ID can be obtained via `startOnSiteJobsAppointmentBookingSession` mutation. |
| `appointmentDate` | `Date!` |  | Appointment date (inclusive) to fetch slots from. |

## `getOnSiteJobsCheckResults(supplyPointIdentifierToMarketNameMapping: [SupplyPointIdentifierToMarketNameMappingInput], supplyPointInternalIds: [Int], jobType: String)`

- Return type: `OnSiteJobsCheckResultsType`
- Description: Get check results for creating requests and appointments.

| Arg | Type | Default | Description |
|---|---|---|---|
| `supplyPointIdentifierToMarketNameMapping` | `[SupplyPointIdentifierToMarketNameMappingInput]` |  | Supply point identifier to market name mapping. If this is provided, `supplyPointInternalIds` cannot be provided. Either one of them must be provided. |
| `supplyPointInternalIds` | `[Int]` |  | List of internal IDs of supply points. If this is provided, `supplyPointIdentifierToMarketNameMapping` cannot be provided. Either one of them must be provided. |
| `jobType` | `String` |  | Job type for appointment checks. |

## `getOnSiteJobsJobTypes(requestId: UUID!, workCategory: OnSiteJobsWorkCategory)`

- Return type: `[OnSiteJobsJobTypeType]`
- Description: Get available job types for an on-site jobs request.

| Arg | Type | Default | Description |
|---|---|---|---|
| `requestId` | `UUID!` |  | The ID of the request for which to fetch available job types. |
| `workCategory` | `OnSiteJobsWorkCategory` |  | Work category to filter job types by. If it's left as blank, all job types will be returned. |

## `getOnSiteJobsRequestById(requestId: UUID)`

- Return type: `OnSiteJobsRequestType`
- Description: Get a specific request by ID.

| Arg | Type | Default | Description |
|---|---|---|---|
| `requestId` | `UUID` |  | The ID of the request to return. |

## `getOnSiteJobsRequests(supplyPointsToMarketNamesMapping: [SupplyPointIdentifierToMarketNameMappingInput], supplyPointInternalIds: [Int], statuses: [OnSiteJobsRequestStatus], before: String, after: String, first: Int, last: Int)`

- Return type: `OnSiteJobsRequestConnectionTypeConnection`
- Description: Filter On-Site Jobs Requests.

| Arg | Type | Default | Description |
|---|---|---|---|
| `supplyPointsToMarketNamesMapping` | `[SupplyPointIdentifierToMarketNameMappingInput]` |  | A list of supply point identifiers to filter requests by. If this is provided, `supplyPointInternalIds` cannot be provided. |
| `supplyPointInternalIds` | `[Int]` |  | List of internal IDs of supply points to filter requests by. If this is provided, `supplyPointsToMarketNamesMapping` cannot be provided. |
| `statuses` | `[OnSiteJobsRequestStatus]` |  | A list of statuses to filter requests by. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `goodsProducts(marketName: String!, productType: [String], code: [String], before: String, after: String, first: Int, last: Int)`

- Return type: `GoodsProductConnectionTypeConnection`
- Description: List Goods products given a market.

| Arg | Type | Default | Description |
|---|---|---|---|
| `marketName` | `String!` |  | Market name of the products to list. |
| `productType` | `[String]` |  | Types of the products to filter by. |
| `code` | `[String]` |  | Code of the products to filter by. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `goodsPurchases(accountNumber: String!)`

- Return type: `[GoodsPurchase]`
- Description: List purchases for an account.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |

## `goodsQuotes(accountNumber: String, quoteCode: String)`

- Return type: `[GoodsQuote]`
- Description: List quotes given an account number or retrieve a Goods quote given a quote code. The possible errors that can be raised are: - KT-CT-8204: Invalid arguments. - KT-CT-8223: Unauthorized. - KT-CT-8201: Received an invalid quoteId. - KT-CT-8204: Invalid arguments. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number. |
| `quoteCode` | `String` |  | The quote code. |

## `inboundCallAverageWaitTime`

- Return type: `InboundCallAverageWaitTimeType`
- Description: Get the average wait time for an inbound call.

## `inkCommsTemplate(templateIdentifier: String!)`

- Return type: `String!`
- Description: Fetch the content of a given comms template name. The possible errors that can be raised are: - KT-CT-7648: The comms template was not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `templateIdentifier` | `String!` |  | The identifier of the comms template. |

## `inkConversation(accountNumber: String, conversationRelayId: String)`

- Return type: `InkConversation!`
- Description: Get the Ink conversation for a given account. The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-4177: Unauthorized. - KT-CT-7610: No Ink conversation for account. - KT-CT-7617: Must supply account number or relay id to get a conversation. - KT-CT-7638: Invalid conversation ID. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number. |
| `conversationRelayId` | `String` |  | The conversation's relay id. |

## `inkMessage(messageRelayId: String!)`

- Return type: `InkMessage!`
- Description: Get the content for a given message. The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-7638: Invalid conversation ID. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `messageRelayId` | `String!` |  | The message's relay id. |

## `inkMessageAttributes(vendor: String!, vendorId: String!)`

- Return type: `InkMessageAttributes!`
- Description: Get attributes of a message at time of query. The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `vendor` | `String!` |  | The message's vendor. |
| `vendorId` | `String!` |  | The message's vendor id. |

## `inkMessageTextContent(messageId: ID!)`

- Return type: `String!`
- Description: Fetch the text content of a given message. The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `messageId` | `ID!` |  | The message's id or relay id. |

## `internalCompanies(before: String, after: String, first: Int, last: Int)`

- Return type: `InternalCompanyConnectionTypeConnection`
- Description: Get all internal companies.

| Arg | Type | Default | Description |
|---|---|---|---|
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `internalCompany(criteria: SearchCriteriaInput!)`

- Return type: `InternalCompanyType`
- Description: Get an internal company by a set of criteria. Criteria will be added as needed, check documentation for the criteria object to see what is currently supported. The possible errors that can be raised are: - KT-CT-14401: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `criteria` | `SearchCriteriaInput!` |  | Criteria to identify the internal company. |

## `isCustomerEligibleToGiveFeedbackFollowingCall(accountNumber: String!, accountUserNumber: String!, callId: Int!)`

- Return type: `Boolean`
- Description: Check if customer is eligible to give feedback following a phone call. The possible errors that can be raised are: - KT-CT-5519: Voice call not found. - KT-CT-5521: Eligibility configuration not found. - KT-CT-5522: Invalid eligibility configuration. - KT-CT-5523: Invalid account or account user. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Number of the account. |
| `accountUserNumber` | `String!` |  | Number of the account user. |
| `callId` | `Int!` |  | ID of the voice call. |

## `isCustomerEligibleToGiveFeedbackFollowingEmail(accountNumber: String!, accountUserNumber: String!, inkConversationId: Int!, conversationClosedAt: DateTime!)`

- Return type: `Boolean`
- Description: Check if customer is eligible to give feedback following an email conversation. The possible errors that can be raised are: - KT-CT-5520: Ink conversation not found. - KT-CT-5521: Eligibility configuration not found. - KT-CT-5522: Invalid eligibility configuration. - KT-CT-5523: Invalid account or account user. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Number of the account. |
| `accountUserNumber` | `String!` |  | Number of the account user. |
| `inkConversationId` | `Int!` |  | ID of the Ink conversation. |
| `conversationClosedAt` | `DateTime!` |  | Datetime when the conversation was closed. |

## `isPasswordResetTokenValid(userId: String!, token: String!)`

- Return type: `Boolean`
- Description: Check validity of a password reset token.

| Arg | Type | Default | Description |
|---|---|---|---|
| `userId` | `String!` |  | Base64 encoded user id. |
| `token` | `String!` |  | Password reset token to check. |

## `joinSupplierProcess(number: String!)`

- Return type: `JoinSupplierProcessType`
- Description: The possible errors that can be raised are: - KT-CT-10332: Join supplier process not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `number` | `String!` |  | The join supplier process number, e.g. JS-12345678. |

## `krakenVersion`

- Return type: `KrakenVersionType`
- Description: The current version of kraken.

## `leadBlocklistValidations(blockListEntries: LeadBlockListValidationInput)`

- Return type: `LeadBlockListValidationOutput`
- Description: Run a blocklist validation out of some dynamic client entry types.

| Arg | Type | Default | Description |
|---|---|---|---|
| `blockListEntries` | `LeadBlockListValidationInput` |  | List of client-configured black list entry types. |

## `leadByNumber(number: String)`

- Return type: `LeadOutput`
- Description: Get lead details by number. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `number` | `String` |  | Lead number. |

## `leads(input: LeadsQueryInput, offset: Int, before: String, after: String, first: Int, last: Int)`

- Return type: `LeadsConnection`
- Description: Fetch all leads for this Kraken, with optional filtering.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LeadsQueryInput` |  | Input fields for retrieving leads. |
| `offset` | `Int` |  |  |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `leaveSupplierProcess(number: String)`

- Return type: `LeaveSupplierProcessType`
- Description: Details associated with a LeaveSupplier process. The possible errors that can be raised are: - KT-CT-10302: Invalid data. - KT-CT-10333: Missing either number of leave supplier process id. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `number` | `String` |  | The leave supplier process number, e.g. LS-12345678. |

## `legacyOrderDetails(identifier: String!)`

- Return type: `LegacyOrderDetailsType`
- Description: The possible errors that can be raised are: - KT-CT-13101: Order not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `identifier` | `String!` |  | Order identifier. |

## `lifecycleProcesses(onlyActive: Boolean, sortOrder: LifecycleProcessesSortOrder, accountNumber: String!)`

- Return type: `LifecycleProcessesType`
- Description: Get all lifecycle processes associated with an account. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `onlyActive` | `Boolean` |  | A flag to filter out only active/current processes. |
| `sortOrder` | `LifecycleProcessesSortOrder` |  | The chronological order in which the lifecycle processes are sorted. |
| `accountNumber` | `String!` |  | The account number, e.g. A-12345678. |

## `livePaymentAdequacyCalculation(ledgerNumber: String!)`

- Return type: `LivePaymentAdequacyCalculation`
- Description: Get payment adequacy data with an up to date calculation. The possible errors that can be raised are: - KT-CT-3963: Could not calculate live PA data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `ledgerNumber` | `String!` |  | Kraken ledger number. |

## `loyaltyCards(accountUserId: String!)`

- Return type: `[LoyaltyCardType]`
- Description: Get all loyalty cards for the given account user. The possible errors that can be raised are: - KT-CT-5412: No account user exists with the given id. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountUserId` | `String!` |  | Account user id. |

## `loyaltyPointLedgerEntry(input: LoyaltyPointLedgerEntryInput!)`

- Return type: `LoyaltyPointLedgerEntryType`
- Description: Resolve a loyalty point ledger entry. The possible errors that can be raised are: - KT-CT-9215: Loyalty points balance query disabled. - KT-CT-9223: Loyalty points ledger entry not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LoyaltyPointLedgerEntryInput!` |  |  |

## `loyaltyPointLedgers(input: LoyaltyPointLedgersInput)`

- Return type: `[LoyaltyPointLedgerEntryType]`
- Description: Get the Loyalty Point ledger entries for the passed user. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LoyaltyPointLedgersInput` |  | The input object for retrieving a loyalty point ledger entry. |

## `loyaltyPointsBalance(input: LoyaltyPointsBalanceInput)`

- Return type: `AccountLoyaltyPointsType`
- Description: Get the loyalty points balance for an account. The possible errors that can be raised are: - KT-CT-9218: Unauthorized. - KT-CT-9217: Unauthorized. - KT-CT-9215: Loyalty points balance query disabled. - KT-CT-9216: Unauthorized. - KT-CT-9222: Loyalty points balance query requires either accountNumber field (deprecated) or input object (preferred) with account number and optional account user id. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LoyaltyPointsBalanceInput` |  |  |

## `metadata(linkedObjectType: LinkedObjectType, identifier: String!)`

- Return type: `[Metadata]`
- Description: Metadata for a linked object. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4124: Unauthorized. - KT-CT-8411: Invalid data. - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `linkedObjectType` | `LinkedObjectType` |  |  |
| `identifier` | `String!` |  |  |

## `metadataForKey(linkedObjectType: LinkedObjectType, identifier: String!, key: String!)`

- Return type: `Metadata`
- Description: Metadata for a linked object with key. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4124: Unauthorized. - KT-CT-8411: Invalid data. - KT-CT-4179: No metadata found with given key. - KT-CT-4155: Invalid data. - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `linkedObjectType` | `LinkedObjectType` |  |  |
| `identifier` | `String!` |  |  |
| `key` | `String!` |  |  |

## `mfaDevices`

- Return type: `[MfaDevice]`
- Description: Get all MFA devices for the current user.

## `node(id: ID!)`

- Return type: `Node`

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` |  | The ID of the object |

## `ocppConnection(accountNumber: String!)`

- Return type: `OCPPConnectionType`
- Description: To confirm whether a device is connected to OCPP. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4311: Unable to confirm OCPP connection. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `ocppDetails(accountNumber: String!)`

- Return type: `OCPPDetailsType`
- Description: The user specific generated OCPP details. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `ocuCollectivePurchaseCanContract(customerId: String!)`

- Return type: `Boolean`
- Description: Resolves whether an OCU collective purchase customer can contract or not. The possible errors that can be raised are: - KT-ES-7810: Customer has reached its max amount of agreements for the OCU collective purchase product. - KT-ES-7811: Customer isn't allowed to contract OCU collective purchase product. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `customerId` | `String!` |  | OCU customer id to check. |

## `offerForQuoting(identifier: ID)`

- Return type: `OfferType`

| Arg | Type | Default | Description |
|---|---|---|---|
| `identifier` | `ID` |  | The identifier of the offer to query. |

## `offerGroupForQuoting(identifier: ID)`

- Return type: `OfferGroupType`

| Arg | Type | Default | Description |
|---|---|---|---|
| `identifier` | `ID` |  | The identifier of the offer group to query. |

## `offering(identifier: String)`

- Return type: `OfferingType`
- Description: Get details about a product offering. The possible errors that can be raised are: - KT-CT-12001: Product catalogue offering with given identifier not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `identifier` | `String` |  | The identifier of the offering to query. |

## `onboardingReferralCurrentlyAllowed(referralCode: String!)`

- Return type: `OnboardingReferralAllowedType`
- Description: Gives a prediction on whether a referral will be valid. The possible errors that can be raised are: - KT-ES-6701: Referral currently not allowed. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `referralCode` | `String!` |  | Referral code to be checked. |

## `opportunities(input: OpportunitiesQueryInput, offset: Int, before: String, after: String, first: Int, last: Int)`

- Return type: `OpportunitiesConnection`
- Description: Fetch all opportunities for this Kraken, with optional filtering.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `OpportunitiesQueryInput` |  | Input fields for retrieving opportunities. |
| `offset` | `Int` |  |  |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `opportunityByNumber(number: String)`

- Return type: `OpportunityOutput`
- Description: Get opportunity details by number. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `number` | `String` |  | Opportunity number identifier. |

## `opportunityProductSummary(number: String)`

- Return type: `[OpportunityProductSummary!]!`
- Description: Return summaries of all products in opportunity's accepted offer. Supports multi-product offerings like dual fuel. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8923: The opportunity does not have a linked offer group. - KT-CT-8922: The opportunity does not have an accepted offer. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `number` | `String` |  | Opportunity number. |

## `opportunityValueByKey(opportunityId: ID, key: String)`

- Return type: `String`
- Description: Get the value of a given key that is stored in an opportunity's related JSONFields. The possible errors that can be raised are: - KT-CT-8903: Unable to update opportunity. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `opportunityId` | `ID` |  | The identifier of the opportunity to query. |
| `key` | `String` |  | The key the a funnel-specific value you wish to obtain. |

## `p0Details(cups: String!, nif: String)`

- Return type: `P0Details`
- Description: Retrieve P0 supply point information including acceptance, rejection, or error details. The possible errors that can be raised are: - KT-ES-4501: Unexpected error retrieving P0 details. - KT-ES-4502: P0 requests are currently not supported for the provided DNO. - KT-ES-4503: The DNO sent a malformed P0 response that could not be processed. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `cups` | `String!` |  | Universal Supply Point code. |
| `nif` | `String` |  | Spanish tax identification number (optional). |

## `p0Validation(cups: String!, nif: String!)`

- Return type: `NifCupsCorrelationValidation`
- Description: Call to P0 endpoint crosschecking that a customer with a given NIF is the current owner of the given cups.

| Arg | Type | Default | Description |
|---|---|---|---|
| `cups` | `String!` |  | Universal Supply Point code. |
| `nif` | `String!` |  | Spanish tax identification number. |

## `passwordValidatorHelpTexts(asHtml: Boolean = false)`

- Return type: `[String]`
- Description: The help text of all configured password validators as plain-text or html. Defaults to plain-text.

| Arg | Type | Default | Description |
|---|---|---|---|
| `asHtml` | `Boolean` | `false` | Return the results as html instead of plain-text. Defaults to False. |

## `paymentFingerprintChecks(fingerprint: String!)`

- Return type: `PaymentFingerPrintCheckType`
- Description: Check if a given payment fingerprint already exists and/or is risk-listed.

| Arg | Type | Default | Description |
|---|---|---|---|
| `fingerprint` | `String!` |  | Fingerprint. |

## `paymentRequests(ledgerNumber: String!)`

- Return type: `PaymentRequestsType`
- Description: Get all payment requests for the given ledger.

| Arg | Type | Default | Description |
|---|---|---|---|
| `ledgerNumber` | `String!` |  | Kraken ledger number. |

## `plannedDispatches(accountNumber: String!)`

- Return type: `[UpsideDispatchType]`
- Deprecated: Yes (The 'plannedDispatches' field is deprecated. Please use 'flexPlannedDispatches' instead. - Marked as deprecated on 2025-05-27. - Scheduled for removal on or after 2026-01-16. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/604/)
- Description: All planned device dispatches 24 hours ahead, (usually) in time order. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4340: Unable to fetch planned dispatches. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `portfolio(portfolioNumber: String!)`

- Return type: `PortfolioType`
- Description: Get details about a portfolio, using its portfolio number. The possible errors that can be raised are: - KT-CT-9403: Received an invalid portfolioId. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `portfolioNumber` | `String!` |  | Portfolio number to be retrieved. |

## `portfolioByReference(portfolioReference: PortfolioReferenceInput!)`

- Return type: `PortfolioType`
- Description: Get details about a portfolio, using its reference. The possible errors that can be raised are: - KT-CT-9409: Invalid portfolio reference. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `portfolioReference` | `PortfolioReferenceInput!` |  | Portfolio reference namespace-value pair to filter by. |

## `possibleErrors(input: PossibleErrorsInputType!)`

- Return type: `PossibleErrorsOutputType`
- Description: Possible errors of the requested query/mutation. The possible errors that can be raised are: - KT-CT-1606: Query/Mutation not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PossibleErrorsInputType!` |  | Query or Mutation for which to get the possible errors list. |

## `printBatch(batchId: ID)`

- Return type: `PrintBatchType!`
- Description: Get print batch details, including messages in the batch. The possible errors that can be raised are: - KT-CT-9013: Invalid data. - KT-CT-9012: Invalid data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `batchId` | `ID` |  | The print batch ID. |

## `productsWithEstimates(electricityCups: String, electricityAnnualConsumption: Int, gasCups: String, gasAnnualConsumption: Int, brand: String = "OCTOPUS_ENERGY_SPAIN", date: Date, organizationName: String, isHidden: Boolean)`

- Return type: `ProductWithEstimates`
- Description: Get all products providing an estimate, either CUPS or annualConsumption. The possible errors that can be raised are: - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `electricityCups` | `String` |  | Supply point electricity CUPS. |
| `electricityAnnualConsumption` | `Int` |  | Estimated electricity annual consumption. |
| `gasCups` | `String` |  | Supply point gas CUPS. |
| `gasAnnualConsumption` | `Int` |  | Estimated gas annual consumption. |
| `brand` | `String` | `"OCTOPUS_ENERGY_SPAIN"` | The market brand code. |
| `date` | `Date` |  | The date when product must be available. |
| `organizationName` | `String` |  | The organization from which filter the products. |
| `isHidden` | `Boolean` |  | Get products based on its hidden attribute. |

## `productsWithoutEstimates(brand: String = "OCTOPUS_ENERGY_SPAIN", date: Date, organizationName: String, isHidden: Boolean)`

- Return type: `[ProductWithoutEstimates]`
- Description: Get all active non-hidden products without providing any estimate.

| Arg | Type | Default | Description |
|---|---|---|---|
| `brand` | `String` | `"OCTOPUS_ENERGY_SPAIN"` | The market brand code. |
| `date` | `Date` |  | The date when product must be available. |
| `organizationName` | `String` |  | The organization from which filter the products. |
| `isHidden` | `Boolean` |  | Get products based on its hidden attribute, only for organizations. |

## `propertiesSearch(searchTerm: String!)`

- Return type: `[PropertySearchResult!]!`
- Description: Search for properties that are already in Kraken and match the search term.

| Arg | Type | Default | Description |
|---|---|---|---|
| `searchTerm` | `String!` |  | The search term. It can be an address or a meter point identifier. |

## `property(id: ID!)`

- Return type: `PropertyType`
- Description: A property with the given ID. Usually associated with supply points. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `id` | `ID!` |  | The property ID. |

## `propertySearch(searchTerm: String!)`

- Return type: `[PropertyType]`
- Deprecated: Yes (The 'propertySearch' field is deprecated. This query is being deprecated in favour of `propertiesSearch`. The latter returns not only the matched properties but the level of confidence in the results through the `score` field. - Marked as deprecated on 2023-05-23. - Scheduled for removal on or after 2024-01-01.)
- Description: Search for properties that are already in Kraken and match the search term.

| Arg | Type | Default | Description |
|---|---|---|---|
| `searchTerm` | `String!` |  | The search term. It can be an address or a meter point identifier. |

## `providerAuthDetails(provider: ProviderChoices!, deviceType: KrakenFlexDeviceTypes!, clientType: ClientType = APP, accountNumber: String, propertyId: Int)`

- Return type: `ProviderAuthDetailsType`
- Deprecated: Yes (The 'providerAuthDetails' field is deprecated. Please use 'startSmartFlexOnboarding' instead. - Marked as deprecated on 2025-10-30. - Scheduled for removal on or after 2026-04-30. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/608/)
- Description: Auth details (e.g. OAuth 2.0 URI) for the provider (if available).

| Arg | Type | Default | Description |
|---|---|---|---|
| `provider` | `ProviderChoices!` |  | The provider to get the auth details for. |
| `deviceType` | `KrakenFlexDeviceTypes!` |  | The device type to get the auth details for (as providers may support multiple). |
| `clientType` | `ClientType` | `APP` | The client type the request originated from. Used when oauth_uri is different between web and app. |
| `accountNumber` | `String` |  | The account number that will be associated with the device. Required for some providers. |
| `propertyId` | `Int` |  | The ID of the property the device belongs to. |

## `providerVirtualKeyDetails(provider: ProviderChoices!, deviceType: KrakenFlexDeviceTypes!)`

- Return type: `ProviderVirtualKeyDetailsType`
- Description: Virtual key details (e.g. certificate public key) for the provider (if available).

| Arg | Type | Default | Description |
|---|---|---|---|
| `provider` | `ProviderChoices!` |  | The provider to get the virtual key details for. |
| `deviceType` | `KrakenFlexDeviceTypes!` |  | The device type to get the virtual key details for (as providers may support multiple). |

## `provinces`

- Return type: `[Province]`
- Description: Spanish provinces.

## `queryComplexity(input: QueryComplexityInputType!)`

- Return type: `QueryComplexityOutputType`
- Description: Get the complexity of a query.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `QueryComplexityInputType!` |  | Query and relevant variables required to calculate the complexity. |

## `question(formId: Int!)`

- Return type: `String`
- Description: Get the customer feedback survey question. The possible errors that can be raised are: - KT-CT-5513: Invalid data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `formId` | `Int!` |  |  |

## `quoteRequest(code: String!)`

- Return type: `QuoteRequest`
- Description: The quote request with a list of quoted supply points and their products.

| Arg | Type | Default | Description |
|---|---|---|---|
| `code` | `String!` |  | The quote request code. |

## `quotingParamDefinitionsForProductOffering(productOfferingIdentifier: ID)`

- Return type: `QuotedOfferingParamsType`
- Description: The possible errors that can be raised are: - KT-CT-12403: Product offering not found. - KT-CT-12404: Product offering has expired. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `productOfferingIdentifier` | `ID` |  | The identifier of the product offering. |

## `rateLimitInfo`

- Return type: `CombinedRateLimitInformation`
- Description: Combined information about points-allowance rate limiting and request-specific rate limiting.

## `registeredKrakenflexDevice(accountNumber: String!)`

- Return type: `KrakenFlexDeviceType`
- Deprecated: Yes (The 'registeredKrakenflexDevice' field is deprecated. Please use 'devices' instead. - Marked as deprecated on 2024-04-23. - Scheduled for removal on or after 2026-03-01. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/677/)
- Description: A device registered with KrakenFlex for a given account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `returnSchedule(accountNumber: String!)`

- Return type: `[DepositReturnScheduleOutput]`
- Description: Get deposit agreement related return schedules for a given account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `routingAttributes(category: String, search: String)`

- Return type: `[RoutingAttributeType]!`
- Description: Get routing attributes available for call routing configuration. The possible errors that can be raised are: - KT-CT-11816: Invalid routing attribute category. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `category` | `String` |  | Filter by category (LANGUAGE, OPERATIONS_GROUP, SKILL). |
| `search` | `String` |  | Filter by friendly name (case-insensitive). |

## `salesFunnelByCode(input: SalesFunnelInput!)`

- Return type: `SalesFunnel`
- Description: Get the sales funnel by input. The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SalesFunnelInput!` |  | Input fields for retrieving the sales funnel. |

## `salesFunnels(input: SalesFunnelsInput)`

- Return type: `[SalesFunnel]`
- Description: Get all sales funnels.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SalesFunnelsInput` |  | Input fields for retrieving the sales funnels. |

## `searchLead(filters: SearchLeadFilters!)`

- Return type: `LeadIdType`
- Description: Search and return the identifiers of a lead. The possible errors that can be raised are: - KT-CT-8920: Search filters are invalid. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `filters` | `SearchLeadFilters!` |  | Filters to search for leads. All passed filters will be checked against the lead. |

## `simpleQuoteLevels`

- Return type: `[QuoteEstimatimation]`
- Deprecated: Yes (The 'simpleQuoteLevels' field is deprecated. Migrated to OE Backend API. - Marked as deprecated on 2025-10-27. - Scheduled for removal on or after 2025-11-10.)
- Description: Get quote estimation list.

## `sipsData(cups: String!, market: String!)`

- Return type: `SIPSData`
- Description: Get SIPS (Sistema Información Puntos Suministro) data for a given CUPS. The possible errors that can be raised are: - KT-ES-7820: SIPS data not available for the given supply point. - KT-ES-7821: An unexpected error occurred while attempting to retrieve SIPS data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `cups` | `String!` |  | The CUPS identifier to retrieve SIPS data for. |
| `market` | `String!` |  | The market type: 'electricity' or 'gas'. |

## `siteworksRequests(ids: [UUID], createdAfter: DateTime, statuses: [RequestStatus], before: String, after: String, first: Int, last: Int)`

- Return type: `CoreSiteworksRequestConnectionTypeConnection`
- Deprecated: Yes (The 'siteworksRequests' field is deprecated. Please use getOnSiteJobsRequests instead. - Marked as deprecated on 2026-03-01. - Scheduled for removal on or after 2026-09-01.)
- Description: A query to get a subset of Requests.

| Arg | Type | Default | Description |
|---|---|---|---|
| `ids` | `[UUID]` |  | A list of request IDs. If provided, only these requests will be returned. |
| `createdAfter` | `DateTime` |  | Only requests created after this datetime will be included. |
| `statuses` | `[RequestStatus]` |  | Only requests with a status in this list will be included. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `smartFlexDeviceSupplyPoint(smartFlexDeviceId: String)`

- Return type: `SmartFlexDeviceSupplyPointType`
- Description: The supply point linked to the SmartFlex device.

| Arg | Type | Default | Description |
|---|---|---|---|
| `smartFlexDeviceId` | `String` |  | The SmartFlex device ID to get the supply point details for. |

## `smartFlexOnboardingWizards(accountNumber: String!, propertyId: Int, wizardId: ID, includeCancelled: Boolean, includeCompleted: Boolean, isResumable: Boolean)`

- Return type: `[SmartFlexOnboardingWizard!]`
- Description: A list of wizards for onboarding devices for an account and property. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number, e.g. A-12345678. |
| `propertyId` | `Int` |  | Only list wizards for this property. |
| `wizardId` | `ID` |  | To get a specific wizard by ID, if it exists. |
| `includeCancelled` | `Boolean` |  | Include cancelled wizards. |
| `includeCompleted` | `Boolean` |  | Include completed wizards. |
| `isResumable` | `Boolean` |  | Filters for onboarding wizards that can be resumed. List limits to one resumable wizard. |

## `solarSimulatorQuote(roofSize: Float!, consumption: Int!)`

- Return type: `SolarSimulationQuote`
- Deprecated: Yes (The 'solarSimulatorQuote' field is deprecated. Migrated to OE Backend API. - Marked as deprecated on 2025-10-27. - Scheduled for removal on or after 2025-11-10.)
- Description: Get solar simulator response data.

| Arg | Type | Default | Description |
|---|---|---|---|
| `roofSize` | `Float!` |  | Roof size in square meters. |
| `consumption` | `Int!` |  | High-range monthly consumption in EUR. |

## `solarTariff`

- Return type: `SpecialTariff`
- Description: Send information about the current solar tariff. The possible errors that can be raised are: - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested.

## `standardisedAddressInfo(postcode: String)`

- Return type: `StandardAddressInfo`
- Description: Get standardised address information from the postcode. The possible errors that can be raised are: - KT-CT-4410: Invalid postcode. - KT-ES-4401: Unexpected Chipiron vendor response. - KT-ES-4402: Error while calling Chipiron vendor. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `postcode` | `String` |  | Postcode used to retrieve standard address info. |

## `streetTypes`

- Return type: `[StreetType]`
- Description: Street types.

## `supplyPoint(externalIdentifier: String!, marketName: String!)`

- Return type: `SupplyPointType`
- Description: Get a supply point by its market specific id. The possible errors that can be raised are: - KT-CT-4722: Supply point readings API not configured. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-4723: Invalid market name provided. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `externalIdentifier` | `String!` |  | The market specific supply point id. |
| `marketName` | `String!` |  | The name of the market in which this supply point exists. |

## `supplyPoints(accountNumber: String, portfolioNumber: String, before: String, after: String, first: Int, last: Int)`

- Return type: `SupplyPointConnectionTypeConnection`
- Description: Get list of supply points.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | Filter meter points by account. |
| `portfolioNumber` | `String` |  | Filter meter points by portfolio. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `taskResult(taskId: String!, accountNumber: String!)`

- Return type: `TaskResult`
- Description: Get the status of a background task. The possible errors that can be raised are: - KT-CT-10401: Task not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `taskId` | `String!` |  |  |
| `accountNumber` | `String!` |  |  |

## `termsAndConditionsForProduct(productCode: String!)`

- Return type: `[TermsAndConditionsType]`
- Description: Get the active terms and conditions for a market supply product. The possible errors that can be raised are: - KT-CT-8501: No active terms and conditions found for product. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `productCode` | `String!` |  | The product code of the market supply product. |

## `thirdPartyViewer`

- Return type: `ThirdPartyOrganizationType`
- Description: The currently authenticated third party. This field requires the `Authorization` header to be set.

## `trigger(triggerId: ID!)`

- Return type: `Trigger!`
- Description: Get the details of a published trigger with a given ID. The possible errors that can be raised are: - KT-CT-9904: Trigger not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `triggerId` | `ID!` |  | The ID of the trigger. |

## `userVehicles(accountNumber: String, supportedProvider: ProviderChoices, authentication: AuthenticationInput)`

- Return type: `[UserVehiclesType]`
- Deprecated: Yes (The 'userVehicles' field is deprecated. Please use 'startSmartFlexOnboarding' instead. - Marked as deprecated on 2025-10-30. - Scheduled for removal on or after 2026-04-30. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/608/)
- Description: A list of vehicles available to the user. Note: If the API returns an empty list, there might be a delay between the vehicle being registered in the provider's system, and data being fetched from the vehicle's manufacturer. In such cases, the query should be retried after a few seconds. The possible errors that can be raised are: - KT-CT-4314: Unable to get provider details. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  |  |
| `supportedProvider` | `ProviderChoices` |  | The provider used to authenticate the device (default Enode). |
| `authentication` | `AuthenticationInput` |  | The authentication details required given the chosen provider. |

## `validateReferralCode(value: String!)`

- Return type: `ReferralClaimCodeType`
- Description: Validate referral claim code.

| Arg | Type | Default | Description |
|---|---|---|---|
| `value` | `String!` |  | Referral claim code value. |

## `vehicleChargingPreferences(accountNumber: String!)`

- Return type: `VehicleChargingPreferencesType`
- Deprecated: Yes (The 'vehicleChargingPreferences' field is deprecated. Please use 'devices.preferences' instead. - Marked as deprecated on 2024-04-23. - Scheduled for removal on or after 2026-03-01. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/675/)
- Description: Vehicle charging preference details. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4339: Your device charging preferences could not be fetched. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |

## `verificationStatus(email: String!)`

- Return type: `EmailVerificationStatus`
- Description: Check the verification status of a given email address.

| Arg | Type | Default | Description |
|---|---|---|---|
| `email` | `String!` |  | The email address to be checked. |

## `viewer`

- Return type: `EspAccountUserType`
- Description: The currently authenticated user. This field requires the `Authorization` header to be set.

## `voiceCampaign(campaignId: String!)`

- Return type: `VoiceCampaignType!`
- Description: Get the voice campaign for a given ID. The possible errors that can be raised are: - KT-CT-11501: Voice campaign not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `campaignId` | `String!` |  | The campaign ID. |

## `voiceCampaigns(status: CampaignStatus, campaignType: TypeOfVoiceCampaign, name: String, before: String, after: String, first: Int, last: Int)`

- Return type: `VoiceCampaignConnectionTypeConnection!`
- Description: Get voice campaigns.

| Arg | Type | Default | Description |
|---|---|---|---|
| `status` | `CampaignStatus` |  | Filter by campaign status. |
| `campaignType` | `TypeOfVoiceCampaign` |  | Filter by campaign type. |
| `name` | `String` |  | Filter by campaign name. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `vouchersBalanceDetail(accountNumber: ID!)`

- Return type: `VouchersBalanceDetail`
- Description: Query the detail of vouchers balance for an account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4178: No account found with given account number. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID!` |  | The account number. |

## `vouchersForAccount(accountNumber: ID!, redeemableOnly: Boolean!, purchasedFromDate: Date, purchasedBeforeDate: Date, availableFromDate: Date, availableBeforeDate: Date, excludeRefunded: Boolean = false, before: String, after: String, first: Int, last: Int)`

- Return type: `VoucherPurchaseConnectionTypeConnection`
- Description: Query the voucher purchases for an account.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID!` |  | The account number. |
| `redeemableOnly` | `Boolean!` |  | Whether to only return vouchers that can be redeemable. |
| `purchasedFromDate` | `Date` |  | An optional date to limit the response to vouchers that have been purchased from the particular date (inclusive) onwards. |
| `purchasedBeforeDate` | `Date` |  | An optional date to limit the response to vouchers that have been purchased before the particular date (exclusive). |
| `availableFromDate` | `Date` |  | An optional date to limit the response to vouchers that are available from the particular date (inclusive) onwards. |
| `availableBeforeDate` | `Date` |  | An optional date to limit the response to vouchers that are available before the particular date (exclusive). |
| `excludeRefunded` | `Boolean` | `false` | Whether to exclude refunded vouchers from the response. By default, refunded vouchers will be included in the response. |
| `before` | `String` |  |  |
| `after` | `String` |  |  |
| `first` | `Int` |  |  |
| `last` | `Int` |  |  |

## `workSchedule(identifier: String!)`

- Return type: `WorkScheduleType!`
- Description: Get the work schedule with the given identifier. The possible errors that can be raised are: - KT-CT-11804: Work schedule not found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `identifier` | `String!` |  | The identifier of the work schedule (also known as the 'slug'). |

