# Input Objects

Total `INPUT_OBJECT` types: **461**

## `APIBrownoutInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `statuses` | `[APIBrownoutStatus]` |  | Return brownouts with these statuses. |

## `APIExceptionQueryInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID` |  | The account number to filter for. |
| `category` | `APIExceptionCategories` | `null` | The category to filter for. |
| `channel` | `String` |  | The channel to filter for. |
| `customerContact` | `String` |  | The customer contact to filter for. |
| `externalIdentifier` | `String` |  | The external identifier to filter for. |
| `priority` | `APIExceptionPriority` | `null` | The priority to filter for. |
| `resolutionStatus` | `APIExceptionResolutionStatus` | `null` | The resolution status to filter for. |
| `resolutionType` | `APIExceptionResolutionType` | `null` | The resolution type to filter for. |
| `supplyPointIdentifier` | `ID` |  | The supply point identifier to filter for. |
| `tags` | `[APIExceptionTags]` |  | Tags to filter for. |
| `userId` | `ID` |  | The user ID to filter for. |

## `AcceptGoodsQuoteInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `clientParams` | `JSONString` |  | A JSON object containing client parameters to store on the quote. |
| `marketParams` | `JSONString` |  | A JSON object containing market parameters to store on the purchase. |
| `quoteId` | `ID!` |  | ID of the accepted quote. |

## `AcceptOfferForQuotingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `identifier` | `ID` |  | Identifier of the Offer. |

## `AccountBillingAddressInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number of the account to update. |
| `billingAddress` | `BillingAddressDetailsInput` | `null` | Billing address details. |

## `AccountLedgerInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID!` |  | The account number. |
| `ledgerNumber` | `String` |  | The ledger number for the account. |

## `AccountNumberInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |

## `AccountReferenceInput`

The input type for the account reference.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `namespace` | `String!` |  | The namespace for the reference. |
| `value` | `String!` |  | The reference value. |

## `AccountSearchInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `account` | `String` |  | Internal account id (not account number). |
| `accountNumber` | `String` |  | The account number eg. A-FF15AE70. |
| `accountReferences` | `String` |  | Account Reference. |
| `bill` | `String` |  | Bills (Shortcut). |
| `billingName` | `String` |  | Account or Billing name. |
| `businessName` | `String` |  | Business name. |
| `businessNumber` | `String` |  | Business identifier or number. |
| `cups` | `String` |  | CUPS of supply points. |
| `email` | `String` |  | Email of the account user. |
| `location` | `String` |  | Location (Supply or Billing, full or partial, address or post code). |
| `meterSerialNumber` | `String` |  | Meter Serial Number. |
| `nif` | `String` |  | NIF of the account user. |
| `phone` | `String` |  | Phone number of the account user. |
| `portfolioNumber` | `String` |  | The portfolio number eg. P-A123B456. |
| `statements` | `String` |  | Statements (Alias for bills). |
| `urn` | `String` |  | URN Number. |
| `user` | `String` |  | The Account User ID (not account number). |

## `ActualizeContractInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `identifier` | `NonEmptyString!` |  | The unique identifier of the contract to actualize. |
| `validFrom` | `DateTime!` |  | The day and time from when the contract actualization is valid. |

## `AddBusinessToSegmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `businessId` | `ID!` |  | The business ID. |
| `segmentName` | `String!` |  | The segment name. |

## `AddCampaignToAccountInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `campaign` | `String!` |  | The slug of the campaign we want to assign. |
| `expiryDate` | `Date` |  | The date in which the link between the campaing and the account is meant to expire. If null, no specific expiring date will be set. |
| `startDate` | `Date` |  | The date in which the link between the campaing and the account is meant to start. If null, no specific start date will be set. |

## `AddChildToPropertyInput`

Input for adding a child property to a parent property in a hierarchy.

| Field | Type | Default | Description |
|---|---|---|---|
| `childId` | `ID!` |  | The ID of the child property to add to the parent. |
| `hierarchyName` | `String` | `"default"` | The name of the hierarchy. |
| `parentId` | `ID!` |  | The ID of the parent property. |

## `AddNoteToInkConversationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `addedAt` | `DateTime` |  | The time at which the note will appear to have been added (defaults to now). |
| `content` | `String!` |  | The content of the note. |
| `conversationRelayId` | `ID!` |  | The relay id of the conversation that will be assigned to the bucket. |
| `isPinned` | `Boolean` | `false` | Is the note pinned, to make it clearer to the support user. |

## `AddParentToPropertyInput`

Input for adding a parent property to a child property in a hierarchy.

| Field | Type | Default | Description |
|---|---|---|---|
| `childId` | `ID!` |  | The ID of the child property. |
| `hierarchyName` | `String` | `"default"` | The name of the hierarchy. |
| `parentId` | `ID!` |  | The ID of the parent property to add to the child. |

## `AddPortfolioReferenceInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `portfolioNumber` | `String!` |  | The portfolio number to which the reference will be added. |
| `referenceNamespace` | `String!` |  | The namespace of the portfolio reference. |
| `referenceValue` | `String!` |  | The value of the portfolio reference. |

## `AddPropertyInput`

Input type for adding a new property to an account.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number to add the property to. |
| `address` | `RichAddressInput!` |  | The address of the property using the rich address format. |

## `AddPropertyToHierarchyInput`

Input for adding a property to a hierarchy as a root node.

| Field | Type | Default | Description |
|---|---|---|---|
| `hierarchyName` | `String` | `"default"` | The name of the hierarchy to add the property to. |
| `propertyId` | `ID!` |  | The ID of the property to add to the hierarchy. |

## `AddSignupReferralOnAccountInput`

Required information for creating a referral reward for an organization

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number for the referred account. |
| `schemeCode` | `String!` |  | The referral scheme code for the organization. |

## `AddStorylineToInkConversationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `conversationRelayId` | `ID!` |  | The relay id of the conversation that will be assigned to the bucket. |
| `entries` | `[InkStorylineEntryInput!]!` |  | A list of entries to add to the storyline. |
| `generatedAt` | `DateTime!` |  | The time the storyline was generated. |
| `knowledgeArticleIds` | `[Int!]` |  | A list of knowledge article IDs to associate with the storyline. |
| `neuralinkRequestId` | `UUID!` |  | The Neuralink request ID. |
| `summary` | `String` |  | The summary of the storyline. |
| `topic` | `String` |  | The topic of the storyline. |

## `AddUserToPortfolioInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `portfolioNumber` | `String!` |  | The portfolio number for the portfolio to add the user to. |
| `roleCode` | `String!` |  | The role code to assign to the user. |
| `userNumber` | `String!` |  | The user number for the user to add to the portfolio. |

## `AmendPaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `amount` | `Int!` |  | The new amount for the amended payment. |
| `paymentDate` | `Date!` |  | The new date to collect the payment. |
| `paymentId` | `Int!` |  | The ID of the payment to amend. |
| `reason` | `String` |  | Reason for amending the payment. |

## `ApproveRepaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID!` |  | The account number for the requested repayment. |
| `repaymentId` | `ID!` |  | The id of the account repayment to be approved. |

## `AssessCollectionProcessRecordForPauseInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `allowUnpausing` | `Boolean` |  | Whether the assessment should unpause the collection process when applicable. |
| `number` | `String!` |  | The collection process number to run pause assessment against. |

## `AssignInkBucketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `bucketName` | `String!` |  | The name of the bucket to assign the conversation to. |
| `conversationRelayId` | `ID!` |  | The relay id of the conversation that will be assigned to the bucket. |

## `AssignSupplyPointToEstimationGroupInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `estimationGroupCode` | `String!` |  | Unique slug identifier for the estimation group. |
| `supplyPointExternalId` | `String!` |  | Supply point external identifier. |
| `supplyPointPeriodStart` | `DateTime` | `null` | Datetime period start to look for supply point. |

## `AssociateCallWithAccountInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number to associate to the call. |
| `callId` | `ID!` |  | The ID of the call. |

## `AssociateItemToCollectionProcessInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `extraDetails` | `JSONString` |  | A JSON object of additional details regarding the item. |
| `itemReference` | `String!` |  | Unique reference to look up the associated item (ex. UUID or primary key). |
| `itemType` | `CollectionProcessAssociatedItemType!` |  | Associated item type. |
| `number` | `String!` |  | The Collection Process Record Number. |
| `occurredAt` | `DateTime` |  | The datetime when action that resulted in the associated item happened. |

## `AudioRecordingInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` | `null` | Account number. |
| `addressLine1` | `String` | `""` | Address line 1. |
| `addressLine2` | `String` | `""` | Address line 2. |
| `addressLine3` | `String` | `""` | Address line 3. |
| `addressLine4` | `String` | `""` | Address line 4. |
| `addressLine5` | `String` | `""` | Address line 5. |
| `contentType` | `String!` |  | Content type of the recording. |
| `duration` | `String!` |  | Duration of the recording in seconds. |
| `fileSize` | `Int!` |  | Size of the file in bytes. |
| `id` | `UUID` |  | UUID of the audio recording. |
| `locationAt` | `DateTime` | `null` | Timestamp of the recorded location. |
| `locationHorizontalAccuracy` | `Int` | `null` | Horizontal accuracy of the location. |
| `locationLatitude` | `Decimal` | `null` | Latitude of the recorded location. |
| `locationLongitude` | `Decimal` | `null` | Longitude of the recorded location. |
| `outcomes` | `[OutcomeInput]` | `[]` | List of outcomes for the session. |
| `photos` | `[PhotoInput]` | `[]` | List of uploaded photos. |
| `postcode` | `String` | `""` | Postal code. |
| `s3Bucket` | `String!` |  | S3 bucket where the audio file is stored. |
| `s3Key` | `String!` |  | S3 key for the audio recording. |
| `salesMode` | `String` | `""` | Sales mode of the session. |
| `scans` | `[String]` | `[]` | List of scan values. |
| `startedAt` | `DateTime!` |  | Start time of the session. |
| `stoppedAt` | `DateTime!` |  | End time of the session. |
| `subdomain` | `String!` |  | Subdomain of the affiliate link. |
| `type` | `String` | `null` | Type of the session. |

## `AuthenticationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accessToken` | `String` |  | SSO access token for the chosen provider authentication. |
| `authorizationCode` | `String` |  | Provider code from user login used for SSO. |
| `expiresIn` | `Int` |  | SSO token expiry for the provider's authentication (integer in seconds). |
| `providerDeviceId` | `String` |  | ID of the device in the external provider system. |
| `redirectUri` | `String` |  | Full redirect URI (including all query string parameters) from the result of an OAuth 2.0 flow. |
| `refreshToken` | `String` |  | SSO refresh token for the chosen provider authentication. |
| `state` | `String` |  | State from user login used for SSO. |

## `AwardLoyaltyPointsInput`

The input type for awarding Loyalty Points.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `idempotencyKey` | `UUID` |  | A unique idempotency key for the award operation. |
| `note` | `String` |  | A note about the award. |
| `points` | `Int!` |  | The number of Loyalty Points to award. |
| `reasonCode` | `LoyaltyPointAwardEntryReasonCode` | `null` | The reason code associated with the award. |

## `BackendScreenEventInput`

Input for a backend action.

| Field | Type | Default | Description |
|---|---|---|---|
| `eventId` | `ID!` |  | The ID of the action to perform. |
| `params` | `[BackendScreenParamInputType]` |  | List of key-value pairs (strings) to pass as parameters to the mutation. |

## `BackendScreenParamInputType`

A key-value pair (both Strings) which is passed in parameters to a backend action.

| Field | Type | Default | Description |
|---|---|---|---|
| `key` | `String!` |  |  |
| `value` | `String!` |  |  |

## `BalanceTriggeredScheduleInput`

A payment schedule which triggers a payment the balance of a ledger drops below a certain value.

| Field | Type | Default | Description |
|---|---|---|---|
| `balanceThreshold` | `Int!` |  | The ledger balance (in the minor currency unit) which when passed will trigger a payment to be taken. |
| `targetBalance` | `Int` | `0` | The target balance (in the minor currency unit) for the ledger; used to calculate the payment amount. Defaults to zero. |

## `BankDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountHolder` | `String` |  |  |
| `accountNumber` | `String` |  |  |
| `accountType` | `String` |  |  |
| `bankCode` | `String` |  |  |
| `branchCode` | `String` |  |  |
| `iban` | `String` |  |  |

## `BaseInitializeAccountInput`

Minimum input required to initiate the Initialize Account step prior to sign up. This type should be extended by clients/territories in order to define the input required by the specific client/territory for account preparation. Either the preferred rich_billing_address or the legacy billing_address must be provided.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountType` | `AccountTypeChoices` | `DOMESTIC` | The type of account to create. |
| `billingAddress` | `LifecycleAddressInput` | `null` | The billing address in legacy format. Must be provided if rich_billing_address is not provided. |
| `billingName` | `String!` |  | The billing name. |
| `brandCode` | `String!` |  | The brand of the created account. |
| `chosenPaymentDay` | `Int` |  | The chosen payment day. |
| `dateOfSale` | `Date` |  | The date of sale, defaults to today if not provided. |
| `portfolioNumber` | `String` |  | The number of the portfolio that the account will be associated with. |
| `preferredSsd` | `Date` |  | The preferred supply start date. |
| `richBillingAddress` | `RichAddressInput` | `null` | The billing address in the preferred RichAddress format. Must be provided if billing_address is not provided. |
| `salesInfo` | `SalesInformationInput!` |  | Sales information. |
| `supplyPointInfoList` | `[PrepareAccountSupplyPointInput]` |  | Information of the supply points that the customer is intending to sign up for supply. |
| `userNumber` | `String!` |  | The number of the user that owns the account. |

## `BaseInitializeUserInput`

Minimum input required to initiate the Initialize User step prior to sign up. This type should be extended by clients/territories in order to define the input required by the specific client/territory for user preparation.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountType` | `AccountTypeChoices` | `DOMESTIC` | The type of account this user is associated with initially. |
| `brandCode` | `String!` |  | The brand of the created portfolio. |
| `customerDetails` | `CustomerDetailsInput!` |  | The customer's details. |
| `details` | `[DetailsInputType]` |  | Optional user details to set on the user (e.g. namespace-based values like SSN last 4, PIN). |
| `portfolioNumber` | `String` |  | The number of portfolio this user will be linked to. |
| `role` | `RoleString` | `null` | The user's role for the portfolio. |

## `BaseInstigateContractTerminationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `contractIdentifier` | `ID!` |  | The ID of the contract. |
| `contractNote` | `ContractNoteInput` |  | Optional note to capture at the point of termination. |
| `requestedTerminationDate` | `Date!` |  | The requested date of the termination. |
| `waiveExitFee` | `Boolean` | `false` | Whether to waive any exit fees associated with the contract or not. |

## `BespokeRateConfigurationInput`

Input type for the BespokeRateConfigurationType.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `schedules` | `[BespokeRateScheduleInput]` |  | The schedules for the bespoke rate configuration. |

## `BespokeRateItemInput`

Item for the BespokeRateConfiguration term.

| Field | Type | Default | Description |
|---|---|---|---|
| `pricePerUnit` | `Decimal` |  | The price per unit for the bespoke rate item. |
| `rateSpecificationCode` | `String` |  | The rate specification code for the bespoke rate item. |
| `variantProfile` | `VariantProfileInput` |  | The variant profile for the bespoke rate item. |

## `BespokeRateScheduleInput`

Schedule for the BespokeRateConfiguration term.

| Field | Type | Default | Description |
|---|---|---|---|
| `items` | `[BespokeRateItemInput]` |  | The items for the bespoke rate schedule. |
| `productCode` | `String` |  | The product code for the bespoke rate schedule. |
| `supplyPointIdentifier` | `String` | `null` | The external identifier of the supply point that this bespoke rate schedule targets. |
| `validFrom` | `DateTime` |  | The datetime the schedule of bespoke rates is valid from. |
| `validTo` | `DateTime` |  | The datetime the schedule of bespoke rates is valid to. |

## `BillDueDateInput`

Input type for BillDueDateTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |

## `BillTriggeredBalanceTargetScheduleInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `targetBalance` | `Int` | `0` | The target balance (in the minor currency unit) for the ledger; used to calculate the payment amount. Defaults to zero. |

## `BillTriggeredScheduleInput`

A payment schedule which triggers a payment when a bill is issued. Optionally a payment day frequency multiplier can be specified in which case the payment is taken on the first occurrence of the payment day after a bill has been issued.

| Field | Type | Default | Description |
|---|---|---|---|
| `frequencyMultiplier` | `Int` |  | The multiple of months at which payment are taken. Required when a payment day is chosen, ignored if payment day not set. |
| `paymentDay` | `Int` |  | The day of the month at which to take payment; allowed values -28 to 28 (excl. 0). Negative values count backwards from the end of the month. If not provided payment is taken whenever a bill is issued. |

## `BillingAddressDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `administrativeArea` | `String` |  | Administrative area. |
| `country` | `String` |  | Billing country. |
| `deliveryPointIdentifier` | `String` |  | Billing delivery point identifier. |
| `dependentLocality` | `String` |  | Billing dependent locality. |
| `locality` | `String` |  | Billing locality. |
| `postalCode` | `String` |  | Billing postal code. |
| `sortingCode` | `String` |  | Billing sorting code. |
| `streetAddress` | `String` |  | Billing street address. |
| `structuredStreetAddress` | `GenericScalar` |  | Billing structured street address. |

## `BillingDocumentIssuanceFrequencyInput`

Input type for the BillingDocumentIssuanceFrequencyTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |

## `BusinessDetailInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `key` | `String!` |  | The key of the business detail. |
| `value` | `String!` |  | The value of the business detail. |

## `CallMetadataInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `callId` | `ID!` |  | The ID of the call to add the metadata to. |
| `metadata` | `[CallMetadataItemInput!]!` |  | List of metadata items to add to the call. |

## `CallMetadataItemInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `hideOnSupportSite` | `Boolean` | `false` | Whether this metadata item should be hidden on the support site and kraken phone. |
| `key` | `String!` |  | The key of the metadata item. |
| `value` | `String!` |  | The value of the metadata item. |

## `CampaignItemInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number of the item. |
| `callWindowEnd` | `DateTime` |  | The end of the call window for the item. |
| `callWindowStart` | `DateTime` |  | The start of the call window for the item. |
| `metadata` | `JSONString` |  | The metadata of the item. |
| `phoneNumber` | `String` |  | The phone number of the item. |

## `CancelEnrollmentInput`

Input required to cancel an enrollment.

| Field | Type | Default | Description |
|---|---|---|---|
| `number` | `String` |  | The identifier of the process to cancel. |
| `reason` | `String` |  | The reason for the cancellation. |

## `CancelLeaveSupplierInput`

Input required to cancel a LeaveSupplier journey.

| Field | Type | Default | Description |
|---|---|---|---|
| `marketData` | `CancelLeaveSupplierMarketInputType` | `null` |  |
| `number` | `NonEmptyID` |  | The ID of the LeaveSupplier process to cancel. |
| `reason` | `String` |  | The reason for the cancellation. |

## `CancelLeaveSupplierMarketInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `voidField` | `String` | `null` | Input types cannot be without fields. And because no market cancellation input type is defined, we must have a void field. |

## `CancelOnSiteJobsAppointmentInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `alignRequestStatus` | `Boolean` | `false` | When true, automatically updates the request status to match the appointment if no active appointments remain. Example: Cancelling the last active appointment on a request will also cancel the request. |
| `appointmentId` | `UUID!` |  | The ID of the appointment. |
| `cancellationCategory` | `OnSiteJobsAppointmentCancellationCategory` | `null` | The cancellation reason for this appointment. |

## `CancelPaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID!` |  | The account number. |
| `paymentId` | `ID!` |  | The ID of the payment to cancel. |
| `reason` | `String` |  | Reason for cancelling the payment. |

## `CancelRepaymentRequestInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `requestId` | `String!` |  | The id of the request to be cancelled. |

## `CancelSmartFlexOnboardingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard to cancel. |

## `CharacteristicOverride`

Override for a product characteristic.

| Field | Type | Default | Description |
|---|---|---|---|
| `code` | `String!` |  | The code of the characteristic to override. |
| `values` | `JSONString!` |  | Override the characteristic with a list of values. |

## `CharacteristicOverrideConfigurationInput`

Input type for the CharacteristicOverrideConfigurationTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `overrides` | `[CharacteristicOverrideInputType!]!` |  | List of characteristic overrides. |

## `CharacteristicOverrideInputType`

Input type for overriding a product characteristic.

| Field | Type | Default | Description |
|---|---|---|---|
| `characteristicCode` | `NonEmptyString!` |  | The code of the characteristic to override. |
| `overrideValue` | `JSONString!` |  | Override the characteristic with a list of values. |
| `productCode` | `String` |  | Optional product code. If specified, the override applies only to this product. |

## `CharacteristicValueInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `characteristicCode` | `String!` |  | The characteristic code. |
| `value` | `String!` |  | The value for the characteristic. |

## `CheckCreditRiskInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountId` | `Int!` |  | The account ID for which the credit risk is being checked. |
| `accountUserId` | `Int!` |  | The account user ID for which the credit risk is being checked. |

## `CloseDCAProceedingInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `agency` | `String!` |  | The DCA agency owning the proceeding. |
| `campaign` | `String` |  | The campaign for the proceeding. |
| `ledgerNumber` | `String` |  | The ledger identifier. |
| `notifyDca` | `Boolean` |  | Whether to send a notification to the DCA. |
| `stopReason` | `String!` |  | The reason for stopping. |
| `stoppedDate` | `Date!` |  | The date where dca proceeding stopped. |

## `CloseInkConversationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `closeReason` | `ConversationClosedReasonChoices!` |  | The reason for closing the conversation. |
| `conversationRelayId` | `ID!` |  | The relay id of the conversation to close. |

## `CloseInkLiveChaConversationtInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The number of the Kraken account that the conversation is from. Required for Account User authorization. |
| `liveChatConversationRelayId` | `ID!` |  | The relay id of the live chat conversation. |

## `CollateralRequiredInput`

Input type for CollateralRequiredTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |

## `CollectDepositInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `depositKey` | `String!` |  | The deposit agreement key (unique). |
| `idempotencyKey` | `String!` |  | The token used to identify this payment (unique). |
| `instructionId` | `String` |  | The ID of the payment instruction to use for this payment. |

## `CollectPaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `amount` | `Int!` |  | The payment amount (in cents). |
| `collectionMethod` | `PaymentType` | `null` | The type of the payment instruction. |
| `description` | `String!` |  | The reason a payment is being collected, for internal audit purposes. |
| `idempotencyKey` | `String!` |  |  |
| `ledgerNumber` | `String` |  | The number of the ledger on which to collect the payment. |
| `paymentDate` | `Date!` |  | The date to attempt to take the payment. Cannot be a date in the past. Payment will be collected on the requested date or as soon as possible after that date. |

## `CommenceDCAProceedingInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `agency` | `String!` |  | The agency. |
| `amount` | `Int` |  | Amount of debt. |
| `campaign` | `String!` |  | The campaign. |
| `dateStarted` | `String!` |  | The date where commencement started. |
| `isWhiteLabel` | `Boolean!` |  | If the commencement is white label. |
| `ledgerNumber` | `String` |  | The ledger identifier. |
| `notes` | `String` |  | Notes for the commencement. |

## `CompleteAuthFlowInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `continuationUri` | `String!` |  | The entire continuation URI returned by the vendor. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `CompleteDeviceRegistrationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number that the device is registered to. |
| `externalDeviceIdentifier` | `String!` |  | External reference in the third-party system to identify the device. |
| `postalCode` | `String!` |  | Postcode of the property (linked to the account) that the device is registered to. |

## `CompleteSmartFlexOnboardingStepInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `CompleteStandalonePaymentInput`

Input fields for completing a standalone payment.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `completionToken` | `String!` |  | The vendor's token used to complete the operation. |
| `idempotencyKey` | `String!` |  | The token used to identify this payment to ensure it is only processed once. |
| `ledgerNumber` | `String!` |  | The number of the specific ledger against which this payment should be applied. |
| `retrievalToken` | `String!` |  | The retrieval token for this standalone payment. |

## `ConfirmDoubleOptInInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `ipAddress` | `String` |  | The IP address of the customer confirming the double opt-in, if applicable. |
| `token` | `String!` |  | The token for the consent to be updated. |

## `ConnectAiAgentToCallInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `callId` | `ID!` |  | The ID of the call to connect the AI agent to. |
| `inferLanguageAttribute` | `Boolean` | `true` | Whether to infer the preferred language of the calling account. |
| `inferOperationsGroupAttributes` | `Boolean` | `true` | Whether to infer the operations group attributes of the calling account. |
| `priority` | `Int` | `0` | The priority with which the call should be routed. A higher number corresponds to a higher routing priority. |
| `routingAttributes` | `[String!]` |  | List of routing attribute references to add to the call. For example, 'SKILL.ENERGY'. Each attribute should already have been created in Kraken. |
| `waitingBehaviourUrl` | `String` |  | A URL that defines the behaviour of the call when it is in the conference. If not set, audio configured in Kraken will be played to the caller. The URL must return a response that can be interpreted by the vendor handling the call. For example, if the call is handled by Twilio, TwiML supported by a <Conference> waitUrl must be returned. |

## `ConsentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `code` | `String!` |  | The code of the consent type. |
| `value` | `ConsentValue!` |  | The value to update the consent to. |

## `ConsentTypeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `consentTypeCode` | `String!` |  | The code of the consent type. |
| `source` | `ConsentEventSource` |  | The source of the consent event. |
| `value` | `ConsentValue` |  | The value to update the consent to. |

## `ContractFiltersInput`

Input type for filtering contracts by party or subject.

| Field | Type | Default | Description |
|---|---|---|---|
| `party` | `PartyInput` |  | Filter contracts by party (the entity that signed the contract). Provide either an account number or business ID. |
| `subject` | `NonEmptyString` |  | Filter contracts by subject (the account impacted by the contract). Provide the account number. |

## `ContractMetaDataInput`

Input type for the ContractMetaDataTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `metadata` | `JSONString!` |  | The additional metadata of the contract. |

## `ContractNoteInput`

Input for capturing a note alongside a contract journey mutation.

| Field | Type | Default | Description |
|---|---|---|---|
| `note` | `String` |  | Optional free-text note (max 1,000 characters). |
| `reasonSlug` | `NonEmptyString!` |  | The slug of the reason for this note. |

## `ContractedVolumeConfigurationInput`

Input type for the ContractedVolumeConfigurationType.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `periods` | `[ContractedVolumePeriodInput]` |  | The periods for the contracted volume configuration. |

## `ContractedVolumePeriodInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `marketName` | `String` |  | The market name the contracted volume applies to. |
| `unit` | `String` |  | The unit for the commodity provided by the contracted volume. |
| `validFrom` | `DateTime` |  | The datetime the period the contracted volume is valid from. |
| `validTo` | `DateTime` |  | The datetime the period the contracted volume is valid to. |
| `value` | `Decimal` |  | The decimal value of the quantity provided by the contracted volume. |

## `CreateAPICallInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `apiExceptionId` | `Int` |  | The ID of the associated API exception, if any. |
| `context` | `JSONString` |  | Any optional useful context involved in the API call. |
| `correlationId` | `String!` |  | The correlation id header from the HTTP request. |
| `inputData` | `JSONString` |  | The input data provided to the API, if any. |
| `operationName` | `String!` |  | The name of the operation associated with this call. |
| `response` | `JSONString!` |  | The response returned by the API. |

## `CreateAPIExceptionEventInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `apiExceptionId` | `Int` |  | The ID of the associated API exception, if any. |
| `category` | `String!` |  | The event category. |
| `context` | `JSONString` |  | Any optional useful context involved in the event. |
| `description` | `String!` |  | Any useful event description. |
| `eventType` | `String!` |  | The event type. |

## `CreateAPIExceptionInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID` |  | The account number associated with the exception, if available. |
| `assignedUserId` | `Int` |  | The ID of the user assigned to handle this exception.If no user is provided, no user will be assigned to the exception. |
| `category` | `APIExceptionCategories` | `UNKNOWN` | Category associated with this exception. Uses the default category if not provided. |
| `channel` | `String!` |  | The API client channel where the exception was triggered from. |
| `context` | `JSONString` |  | Contextual information about the exception, if any. |
| `customerContact` | `String` |  | The customer contact associated with the exception, if available. |
| `externalIdentifier` | `String!` |  | External identifier mapping an entity on the client's database. |
| `keyDate` | `Date` |  | The key date associated with the exception, if available. |
| `operationsTeamId` | `Int` |  | The ID of an operations team to handle this exception. If no team is provided, no team will be assigned to the exception. |
| `priority` | `APIExceptionPriority` | `null` | The priority. Defaults to LOW if not provided. |
| `resolutionStatus` | `APIExceptionResolutionStatus` | `null` | The resolution status. Defaults to UNASSIGNED if not provided. |
| `resolutionType` | `APIExceptionResolutionType` | `null` | The resolution type. Defaults to UNASSIGNED if not provided. |
| `supplyPointIdentifier` | `String` |  | The supply point identifier associated with the exception, if available. |
| `tags` | `[APIExceptionTags]` |  | Tags associated with this exception if any. |
| `userId` | `Int` |  | The user ID associated with the exception, if available. |

## `CreateAPIExceptionNoteInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `apiExceptionId` | `ID!` |  | The ID of the associated API exception. |
| `body` | `String!` |  | The body of the note. |

## `CreateAccountChargeInput`

The input type for the account charge.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `displayNote` | `String` |  | Optional short note about account charge for customer display. |
| `grossAmount` | `Int!` |  | The gross amount of the charge to be added. |
| `metadata` | `JSONString` |  | Any extra data that will be associated with account charge. |
| `note` | `String` |  | Optional short note about account charge for internal use. |
| `reason` | `String!` |  | The reason why the charge is added to the account. This should be a valid charge reason code. |

## `CreateAccountCreditInput`

The input type for the account credit.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `grossAmount` | `Int!` |  | The gross amount of the credit to be created. |
| `metadata` | `JSONString` |  | Any extra data that will be associated with account credit. |
| `netAmount` | `Int!` |  | The net amount of the credit to be created. |
| `note` | `String` |  | Optional short note about account credit. |
| `reason` | `AccountCreditReasonType!` |  | The reason why the credit is added to the account. |
| `salesTaxAmount` | `Int!` |  | The sales tax amount of the credit to be created. |

## `CreateAccountFileAttachmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |
| `category` | `Category!` |  |  |
| `clientMutationId` | `String` |  |  |
| `filename` | `String!` |  |  |

## `CreateAccountNoteInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `isPinned` | `Boolean!` |  | Pin the note to account. |
| `note` | `String!` |  | The note to add. |
| `unpinAt` | `DateTime` |  | When to unpin the note from the account. |

## `CreateAccountPaymentScheduleInput`

Input type for updating the payment schedule on a ledger. Requires an `account_number`, `ledger_number` and at least one of `payment_day` or `payment_amount` to be provided. `trigger` and `amount_strategy` should be provided when updating the payment amount of a variable payment schedule.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Number of the account for which to update the schedule. |
| `amountStrategy` | `AmountStrategy` |  | How the payment value is determined. |
| `ledgerNumber` | `String!` |  | Number of the ledger associated with the current payment schedule. |
| `paymentAmount` | `Int` |  | The new fixed payment amount. |
| `paymentDay` | `Int` |  | The new day of the month at which to take payment; ranges from 1 to 28. |
| `trigger` | `ScheduleTrigger` |  | When a payment is due. |

## `CreateAccountReminderInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `content` | `String!` |  | Reminder content. |
| `dueAt` | `DateTime!` |  | When the reminder is due. |
| `reminderType` | `AccountReminderTypes!` |  | The reminder type. |

## `CreateAddressData`

| Field | Type | Default | Description |
|---|---|---|---|
| `addressExtraInfo` | `String` |  | The extra infomation of the address like building clarifier. |
| `block` | `String` |  | Block. |
| `city` | `String` |  | City. |
| `cityCode` | `String` |  | The municipality city code. |
| `country` | `String` |  | Country. |
| `door` | `String` |  | Door. |
| `floor` | `String` |  | Floor. |
| `gate` | `String` |  | Gate. |
| `postcode` | `String` |  | Postcode. |
| `provinceCode` | `String` |  | The first numbers of the province code. |
| `stair` | `String` |  | Stair. |
| `streetName` | `String` |  | Street name. |
| `streetNumber` | `String` |  | Street number. |
| `streetType` | `String` |  | Street type. |

## `CreateAffiliateLinkInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `contactEmail` | `String!` |  | The contact email for the link. |
| `contactName` | `String!` |  | The contact name for the link. |
| `organisationId` | `ID!` |  | The organisation for whom to create the affiliate link for. |
| `subdomain` | `String!` |  | Will be validated as follows: - should be at least two characters - should only contain (letters, numbers, and Hyphen) - should not contain bad words - should not contain any of the reserved words including: affiliates, api, business, click, consul, developer, friends, kraken, mail, sendgrid, tech, webhooks, www, www2 |

## `CreateAffiliateOrganisationInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `allowAlternativePaymentMethods` | `Boolean` |  | Is this partner allowed to specify payment methods other than Direct Debit in the import csv or API. |
| `canRegisterBusinessMeterPoints` | `Boolean` |  | Are meter point registrations limited for profile classes 1 and 2 for registrations from csv or API. |
| `canRegisterCustomersWithoutEmailAddress` | `Boolean` |  | Allow registration requests with customers without an email address. |
| `canRegisterPortfolioAccounts` | `Boolean` |  | Allow registration requests with exiting account user emails to add to the portfolio belonging to the account user. |
| `canRenewTariffs` | `Boolean` |  | Allow performing tariff renewals via API. |
| `canUseIvrSupportApi` | `Boolean` |  | Allow this partner access to the IVR support API (modify their own IVR handling through third party 'IVR Flow Editor'). |
| `contactEmail` | `String` |  | The primary contact email for the organisation. |
| `defaultAccountType` | `AccountTypeChoices!` |  | Default Account Type. |
| `isFieldSalesOnlyProduct` | `Boolean` |  | Restrict to field-sales-only products? This is only allowed for the 'field-sales' and 'events' sales channels. |
| `name` | `String!` |  | The name of the organisation that is going to be created. |
| `salesChannelCode` | `String` |  | Sales Channel Code. |
| `skipMeterPointAddressValidation` | `Boolean` |  | Allow this partner to skip validation that ensures all meter points belong to the same address. |

## `CreateAffiliateSessionInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `ipAddress` | `String` |  | The IP Address of the user. |
| `linkId` | `ID!` |  | The affiliate link for whom to create the session for. |
| `queryParams` | `JSONString` |  | Additional query parameters to attach to this session. |
| `quoteShareId` | `ID` |  | The quote share that led to this session. |
| `userAgent` | `String` |  | The HTTP user agent. |

## `CreateAgreementInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | A code that uniquely identifies the account. |
| `agreedAt` | `DateTime!` |  | The date and time when the agreement was made. |
| `params` | `GenericScalar` |  | A dictionary of additional parameters for the agreement. |
| `productCode` | `String!` |  | A code that uniquely identifies the product. |
| `rescissionDeadlineAt` | `DateTime` |  | The deadline date and time for rescinding the agreement. |
| `supplyPointExternalIdentifier` | `String!` |  | The external identifier of the supply point. |
| `validFrom` | `DateTime!` |  | The start date of the agreement. |
| `validTo` | `DateTime` |  | The end date of the agreement (exclusive). |

## `CreateAgreementRolloverInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Identification of the account that is requesting the agreement rollover. |
| `currentAgreementId` | `ID!` |  | Identification of the agreement that is being rolled over. |
| `expectedSendDate` | `Date` |  | The expected date when the agreement rollover will be executed.If not provided, will calculate it taking into account the valid to date of the agreement. |
| `params` | `GenericScalar` |  | A JSON object containing additional parameters for the agreement rollover. Ensure it's properly encoded. |
| `renewProductCode` | `String!` |  | The product code for the new agreement. |
| `rolloverDate` | `Date` |  | If the agreement is open-ended, will terminate the agreement on this date. |
| `suppressComms` | `Boolean` | `false` | Suppress Agreement Rollover communications. |
| `tags` | `[String]` |  | List of comma-separated tags to be added to the rollover. |

## `CreateBillingAddress`

| Field | Type | Default | Description |
|---|---|---|---|
| `addressLine1` | `String` |  | Billing address 1. |
| `addressLine2` | `String` |  | Billing address 2. |
| `addressLine3` | `String` |  | Billing address 3. |
| `city` | `String` |  | Billing address city. |
| `postcode` | `String` |  | Billing postcode. |

## `CreateBillingData`

| Field | Type | Default | Description |
|---|---|---|---|
| `addressLine1` | `String` |  | Billing address 1. |
| `addressLine2` | `String` |  | Billing address 2. |
| `addressLine3` | `String` |  | Billing address 3. |
| `city` | `String` |  | Billing address city. |
| `email` | `String` |  | Billing email. |
| `fullName` | `String` |  | Billing full name. |
| `iban` | `String` |  | Account holder iban. |
| `nif` | `String` |  | Billing NIF. |
| `postcode` | `String` |  | Billing postcode. |

## `CreateBillingDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `String` |  | Billing email. |
| `fullName` | `String` |  | Billing full name. |
| `iban` | `String` |  | Account holder iban. |
| `nif` | `String` |  | Billing NIF. |

## `CreateBusinessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `businessBillingAddress` | `RichAddressInput` | `null` | The billing address for the business. |
| `businessDetails` | `[BusinessDetailInput]` |  | Additional details for the business. |
| `businessLegalAddress` | `RichAddressInput` | `null` | The legal address for the business. |
| `businessName` | `String!` |  | The business' name. |
| `businessNumber` | `String!` |  | The business' number. |
| `businessSectors` | `[BusinessSectorString!]` |  | The list of sectors the business operates in. |
| `businessType` | `BusinessTypeOptions!` |  | The company type of a business account. |

## `CreateCampaignItemsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `campaignId` | `String!` |  | The campaign ID. |
| `campaignItems` | `[CampaignItemInput]!` |  | The items to add. |

## `CreateCollectionProcessEventInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `data` | `JSONString` |  | Additional data about the event (e.g., error details, reactivation reason). |
| `eventType` | `CollectionProcessEventTypeEnum!` |  | The type of event that occurred. |
| `number` | `String!` |  | The Collection Process Record Number. |
| `occurredAt` | `DateTime` |  | When the event actually occurred. If not provided, uses current time. |

## `CreateComplaintInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number of the account the complaint is for. |
| `brand` | `String!` |  | The brand associated with the complaint. |
| `communicationSource` | `ComplaintSourceChoices!` |  | Source of the complaint. |
| `preferredContactMethod` | `String` |  | The complainant's preferred contact method. |
| `status` | `String!` |  | The complaint status. |
| `subtype` | `String` |  | Complaint subtype. |
| `summary` | `String` |  | A summary of the complaint. |
| `type` | `String!` |  | Complaint type. |

## `CreateContractInput`

Input type for creating a contract.

| Field | Type | Default | Description |
|---|---|---|---|
| `party` | `PartyInput!` |  | The party for the contract. |
| `sale` | `SalesDetailsInput!` |  | The sale metadata associated with the contract. |
| `signedAt` | `DateTime!` |  | Date when the contract was signed. |
| `subject` | `[NonEmptyString!]` |  | The accounts impacted by this contract, supplied as a list of account numbers. This field is only applicable when the party is a business. |
| `terms` | `[OneOfTermInput!]!` |  | The terms of the contract. |
| `title` | `NonEmptyString` |  | Title of the contract. |
| `validFrom` | `DateTime!` |  | Date from which the contract is valid. |
| `validTo` | `DateTime` |  | Date until which the contract is valid. Leave null for open-ended contracts. |

## `CreateContributionAgreementInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `activeFrom` | `DateTime!` |  | The start datetime of the agreement. |
| `activeTo` | `DateTime` |  | The end datetime of the agreement, if any. |
| `amount` | `Int!` |  | The amount contributed per interval. Note, this is in the smallest domination that the currency supports. e.g. Pence, Cents, Yen, etc. |
| `interval` | `Interval!` |  | The frequency of contributions. |
| `schemeCode` | `String!` |  | The code of the scheme to contribute to. |

## `CreateCreditTransferPermissionInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `sourceLedgerNumber` | `String!` |  | Source ledger number. |
| `targetLedgerNumber` | `String!` |  | Target ledger number. |

## `CreateCustomerFeedbackInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The number of the affected account. |
| `accountUserId` | `Int` |  | The id of the affected user. |
| `accountUserNumber` | `String` |  | The number of the affected user. |
| `feedbackSource` | `String!` |  | The source of the feedback. |
| `inkConversationId` | `Int` |  | The id of the ink conversation that triggered this feedback request. |
| `lastContactedSupportUserId` | `Int` |  | The id of the support user who last contacted the customer. |
| `voiceCallId` | `Int` |  | The id of the voice call (new call system) that triggered this feedback request. |

## `CreateDepositAgreementInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |
| `depositKey` | `String!` |  |  |
| `reason` | `String!` |  |  |

## `CreateEnergyAccountInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `affiliateSessionId` | `String` |  | Affiliate session id. |
| `billingInfo` | `CreateBillingData!` |  | Account details. |
| `dateOfBirth` | `Date` |  | Birth date. |
| `electricitySupplyPoint` | `SupplyPoint` | `null` | The electricity supply point data. |
| `email` | `String!` |  | Account email. |
| `firstFamilyName` | `String!` |  | Spanish first family name. |
| `gasSupplyPoint` | `SupplyPoint` | `null` | The gas supply point data. |
| `gettingInTouch` | `Boolean` |  | Whether to receive promotional mail. |
| `givenName` | `String!` |  | Birth name. |
| `mobile` | `String!` |  | Account mobile phone number. |
| `nif` | `String!` |  | Customer's national ID number. |
| `propertyInfo` | `CreateAddressData!` |  | Property address Data. |
| `referralCode` | `String` |  | Referral code the signing-up customer might have. |
| `salesChannel` | `String` |  | Sales channel. |
| `salesSubchannel` | `String` |  | Sales subchannel. |
| `secondFamilyName` | `String` |  | Spanish second family name. |
| `urn` | `String` |  | Unique reference number. |

## `CreateExternalAccountEventInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The number of the account that the event should be created for. |
| `category` | `ExternalAccountEventCategory!` |  | The category of the event. |
| `content` | `[ExternalAccountEventContent]!` |  | An array of content data associated with the event. |
| `description` | `String` |  | A human-readable description of the event. |
| `occurredAt` | `DateTime` |  | The time the event occurred. |
| `subcategory` | `ExternalAccountEventSubCategory` |  | The subcategory of the event. |

## `CreateExternalAccountUserEventInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `category` | `ExternalAccountEventCategory!` |  | The category of the event. |
| `content` | `[ExternalAccountEventContent]!` |  | An array of content data associated with the event. |
| `description` | `String` |  | A human-readable description of the event. |
| `occurredAt` | `DateTime` |  | The time the event occurred. |
| `subcategory` | `ExternalAccountEventSubCategory` |  | The subcategory of the event. |
| `userId` | `String!` |  | The user that the event should be created for. |

## `CreateExternalMessageInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number of the account to link this message to. |
| `emailContent` | `EmailContentInput!` |  | Content specific for emails. If the message sent was an email, then this should be provided. |
| `sentAt` | `DateTime!` |  | The date and time this message was sent. |
| `vendor` | `String!` |  | The name of the external messaging vendor that sent this message (for example, 'SENDGRID'). |
| `vendorMessageId` | `String!` |  | The unique ID of the message in the external vendor's system. |

## `CreateGoodsQuoteInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `clientParams` | `JSONString` |  | A JSON object containing client parameters to store on the quote. |
| `marketParams` | `JSONString` |  | A JSON object containing market parameters to store on the quote. |
| `productsToQuote` | `[ProductToQuoteInput]!` |  | Products to get a quote for. |

## `CreateGoodsQuoteWithoutAccountInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `clientParams` | `JSONString` |  | A JSON object containing client parameters to store on the quote. |
| `customerProfile` | `CustomerProfileInput!` |  | Customer profile. |
| `marketParams` | `JSONString` |  | A JSON object containing market parameters to store on the quote. |
| `productsToQuote` | `[ProductToQuoteInput]!` |  | Products to get a quote for. |

## `CreateInboundCallInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `fromPhoneNumber` | `String!` |  | The phone number that the call is from. |
| `toPhoneNumber` | `String!` |  | The phone number that the call is to. |
| `vendor` | `VoiceVendor!` |  | The Voice vendor managing the call. |
| `vendorCallId` | `String!` |  | The ID of the call in the vendor's system. |

## `CreateInkInboundMessageInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The number of the Kraken account that the message was from. |
| `channel` | `InkCommunicationChannel!` |  | The channel type the posted message should be treated as in Ink. It is used to determine how the message should be processed and what channel-specific features are available for this message. |
| `messageHeaders` | `JSONString` |  | An optional parameter where we can pass the generic message headers if it has one Email channel tries to get the value `conversation-relay-id` from this parameter |
| `messageId` | `String!` |  | An arbitrary, unique ID for this message. This must be unique for each message that is supplied using the same organisation; collisions between messages provided by different organisations are tolerated. Stored as vendor_id. |
| `newMessage` | `InkMessageInput!` |  |  |
| `occurredAt` | `DateTime` |  | When the message occurred in the system of origin. |
| `vendor` | `String` |  | An optional vendor value to denote which system it originated from. If no vendor is passed, we will get the default generic vendor from the setting called INK_DEFAULT_GENERIC_MESSAGE_API_VENDOR. |

## `CreateInkLiveChatMessageInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The number of the Kraken account that the message was from. |
| `messageId` | `String!` |  | An arbitrary, unique ID for this message. Used in combination with vendor to guarantee uniqueness of the message in Ink. Stored as vendor_id. |
| `newMessage` | `InkMessageInput!` |  |  |
| `occurredAt` | `DateTime` |  | When the message occurred in the system of origin. |
| `vendor` | `String` |  | An optional value that is used in conjunction with message_id to guarantee uniqueness of a message in Ink. It is usually name of the system the message originated from. If not supplied, Ink provides a default system value. |

## `CreateLeadInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` | `null` | Account number's external identifier. |
| `address` | `RichAddressInput` |  | The address for the lead. |
| `assignedToAffiliateNumber` | `String` | `null` | The number of the affiliate organisation assigned to the lead. |
| `assignedToTeamName` | `String` | `null` | The team associated with the lead. |
| `assignedToUsername` | `String` | `null` | The username of the user assigned to the lead. |
| `consents` | `[ConsentTypeInput]` |  | Consents to be associated with the lead. |
| `extraDetailsItems` | `[ExtraDetailsItem]` |  | The extra details for the lead. |
| `leadContacts` | `[LeadContactDetailsInput]!` |  | A list of contact details for the lead. |
| `leadType` | `LeadTypeChoices` | `null` | The type of the lead. |
| `nationalId` | `String` | `null` | The national ID. |
| `salesChannel` | `String` | `null` | The sales channel of the lead. |

## `CreateMfaDeviceInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `mfaMethod` | `MFAMethodChoices!` |  | MFA enrolment method. |

## `CreateNewAgreementFromProductSwitchProcessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `productSwitchProcessId` | `ID!` |  | ID of the product switch process model already initiated. |

## `CreateOfferGroupForQuotingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `productOfferings` | `[OfferingForQuotingInput]!` |  | List of Offerings. |

## `CreateOnSiteJobsRequestInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `assets` | `[OnSiteJobsAssetInput!]!` |  | Request related assets. |
| `comment` | `String` |  | Comment for the request. |
| `emergencyApprovalDetails` | `String` | `""` | Details to be reviewed by the approver when the request is an emergency requiring approval. |
| `isEmergency` | `Boolean` | `false` | Is emergency. |
| `overrideRequestCheckWarnings` | `Boolean` | `false` | Ignore any warnings raised by the request checks. |
| `reporter` | `ReporterInput` | `null` | Request reporter. |
| `runRequestChecks` | `Boolean` | `true` | Run validation checks before creating the request. Cannot be false when using AccountUser authentication. |
| `status` | `OnSiteJobsRequestStatus` | `PENDING` | Request status. This value may be overridden to APPROVAL_PENDING if the reason or emergency requires approval. |
| `supplyPointIdentifierToMarketNameMapping` | `[SupplyPointIdentifierToMarketNameMappingInput!]` |  | Supply point external identifier to market name mappings to associate with the request. If this is provided, `supply_point_internal_ids` cannot be provided. |
| `supplyPointInternalIds` | `[Int!]` |  | List of internal IDs of supply points to associate with the request. If this is provided, `supply_point_identifier_to_market_name_mapping` cannot be provided. |

## `CreateOpportunityAndLeadInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `address` | `RichAddressInput!` |  | The billing address for the lead. |
| `assignedToAffiliateNumber` | `String` | `null` | The number of the affiliate organisation the opportunity is assigned to. |
| `assignedToTeamName` | `String` | `null` | The name of the team the opportunity is assigned to. |
| `assignedToUsername` | `String` | `null` | The username of the user to assign the opportunity to. |
| `consents` | `[ConsentTypeInput]` |  | Consents to be associated with the opportunity. |
| `extraDetailsItems` | `[_CreateOpportunityExtraDetailsItem]` |  | The extra details for the opportunity. |
| `funnelCode` | `String!` |  | The code of the funnel. |
| `leadContactDetails` | `LeadContactDetailsInput!` |  | The contact details for the lead. |
| `leadType` | `String!` |  | The type of the lead. |
| `nationalId` | `String` |  | The national ID. |
| `notes` | `String!` |  | Notes about the opportunity. |
| `opportunityAddress` | `RichAddressInput` |  | The address for the opportunity. |
| `productOfferingId` | `String` |  | The ID of the product offering. |
| `salesChannel` | `String!` |  | The sales channel of the opportunity. |
| `supplyPoints` | `[LeadSupplyPoint]` |  | Supply points for the opportunity. |
| `useSameAddressAsBilling` | `Boolean` | `false` | Whether to use the same address for billing. |

## `CreateOpportunityFileAttachmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `category` | `OpportunityAttachmentCategory!` |  | The category of the file being created. |
| `opportunityNumber` | `String` |  | The unique number of the opportunity. |
| `s3Key` | `String!` |  | S3 key for the file attachment. |

## `CreateOpportunityForLeadInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `address` | `RichAddressInput` |  | The address for the opportunity. |
| `assignedToAffiliateNumber` | `String` | `null` | The number of the affiliate organisation the opportunity is assigned to. |
| `assignedToTeamName` | `String` | `null` | The name of the team the opportunity is assigned to. |
| `assignedToUsername` | `String` | `null` | The username of the user to assign the opportunity to. |
| `extraDetailsItems` | `[_CreateOpportunityExtraDetailsItem]` |  | The extra details for the opportunity. |
| `funnelCode` | `String!` |  | The code of the funnel. |
| `leadNumber` | `String!` |  | The number of the lead. |
| `notes` | `String!` |  | Notes about the opportunity. |
| `productOfferingIdentifier` | `String` |  | The ID of the product offering. |
| `salesChannel` | `String!` |  | The sales channel of the opportunity. |
| `supplyPoints` | `[LeadSupplyPoint]` |  | Supply points for the opportunity. |
| `useSameAddressAsBilling` | `Boolean` | `false` | Whether to use the same address for billing. |

## `CreateOrUpdateLoyaltyCardInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountUserId` | `String` |  | The id of the account user. |
| `number` | `String` |  | The number of the loyalty card. |
| `scheme` | `String` |  | The scheme of the loyalty card. |

## `CreateOrUpdateTimeSeriesEntriesInput`

All information provided in order to create or update time series entries associated with an existing time series.

| Field | Type | Default | Description |
|---|---|---|---|
| `code` | `NonEmptyString!` |  | The time series code. |
| `entries` | `[TimeSeriesEntryInput!]!` |  | The time series entries. |
| `productCode` | `NonEmptyString` |  | The product code associated to the time series. |

## `CreatePaymentActionIntentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `idempotencyKey` | `String!` |  | The unique string used to identify this intent to ensure it is only processed once. |
| `targetIdentifier` | `String!` |  | The unique identifier for the target the payment should be associated with. |
| `targetType` | `PaymentActionIntentTargetType!` |  | The type of target the payment should be associated with. |

## `CreatePortfolioInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `brandCode` | `String` | `"OCTOPUS_ENERGY_SPAIN"` | The brand to associate with this portfolio, if not provided the default brand will be used. |
| `collectiveBilling` | `Boolean` | `false` | Whether collective bills should be issued for the portfolio's accounts. The default value is False. |
| `operationsTeamId` | `ID` |  | The ID of the operations team to associate with this portfolio.If no team is provided, no team will be assigned to the portfolio. |

## `CreatePortfolioUserRoleInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountUserId` | `ID!` |  | The user to associate with the portfolio. |
| `portfolioId` | `ID!` |  | The portfolio to associate the user with. |
| `role` | `RoleString` | `null` | The role to assign to the user. If not provided the default role will be used. |

## `CreatePostEventsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `events` | `[PostEventInput]!` |  | List of post events to create. |

## `CreateProductInput`

Input type for creating a product.

| Field | Type | Default | Description |
|---|---|---|---|
| `availabilityStatus` | `ProductAvailability!` |  | The product availability status. |
| `availableFrom` | `DateTime!` |  | The date the product is available from. |
| `availableTo` | `DateTime` |  | The date the product is available to. |
| `brandCode` | `NonEmptyString!` |  | The brand code. |
| `characteristicOverrides` | `[CharacteristicOverride!]` |  | Overrides for product characteristics. |
| `code` | `NonEmptyString!` |  | The product code. |
| `description` | `String!` |  | The product description. |
| `displayName` | `NonEmptyString!` |  | The product description. |
| `endsAt` | `DateTime` |  | The date the product ends. |
| `fullName` | `NonEmptyString!` |  | The product title. |
| `isHidden` | `Boolean!` |  | Whether the product is hidden. |
| `marketName` | `NonEmptyString!` |  | The name of the market the product belongs to. |
| `notes` | `String!` |  | The product notes. |
| `params` | `JSONString` |  | The product parameters. |
| `specificationCode` | `String` |  | The product specification code. |
| `tags` | `[String!]!` |  | Tags associated with the product. |
| `term` | `Int` |  | The product term in months. |
| `termsAndConditionsTypes` | `[String!]!` |  | A list of terms and conditions specified by codes to associate with the product. |
| `termsContractType` | `String!` |  | The product contract type. |

## `CreatePurchaseInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `clientParams` | `JSONString` |  | A JSON object containing client parameters to store on the purchase. |
| `marketParams` | `JSONString` |  | A JSON object containing client parameters to store on the purchase. |
| `saleItems` | `[ProductToPurchaseInput]!` |  | Products being purchased. |

## `CreateQuoteForAccountInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |
| `asOf` | `Date!` |  | Date as of when the quote is applicable. |
| `identifiers` | `[String]!` |  | List of supply point identifiers to be quoted. |

## `CreateQuoteForProductsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `products` | `[ProductInput]!` |  | The list of products to create a quote for. |

## `CreateQuoteInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountType` | `AccountTypeChoices!` |  | The type of account. |
| `affiliateSessionId` | `ID` |  | The affiliate session ID for the quote. |
| `agreementId` | `ID` |  | The agreement ID for the quote. To be used if we are requoting for an existing supply point. |
| `brand` | `String` | `"OCTOPUS_ENERGY_SPAIN"` | The market brand code. |
| `date` | `Date!` |  | The date when product must be available. |
| `identifier` | `ID!` |  | The identifier for the quote (CUPS / Annual consumption ). |
| `isHidden` | `Boolean!` |  | Get products based on its hidden attribute. |
| `marketName` | `MarketName!` |  | The market name. |

## `CreateReferralInput`

Required information for creating a referral

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number for the referred account. |
| `reference` | `String!` |  | A referral code, e.g. grey-badger-47. |

## `CreateReminderInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number. |
| `assigneeId` | `ID` |  | The id of the user responsible for completing the reminder. |
| `assigneeTeamId` | `ID` |  | The id of the team responsible for completing the reminder. |
| `assigneeTeamName` | `String` |  | The name of the team responsible for completing the reminder. |
| `assigneeUsername` | `String` |  | The username of the user responsible for completing the reminder. |
| `businessId` | `Int` |  | The business ID. |
| `content` | `String!` |  | Reminder content. |
| `dueAt` | `DateTime!` |  | When the reminder is due. |
| `reminderTypeName` | `String!` |  | The reminder type name. |
| `reopenInkConversation` | `Boolean` |  | Reopen ink conversation. |

## `CreateScheduledTransactionsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `action` | `String!` |  | Whether the scheduled transaction is a 'CHARGE' or a 'CREDIT'. |
| `ancillaryData` | `JSONString` | `"{}"` | Additional data that will be consumed and associated with the scheduled transaction. |
| `displayNote` | `String` | `""` | Optional short note about the scheduled transaction for customer display. |
| `grossAmount` | `Int!` |  | The gross amount of the scheduled transaction. |
| `idempotencyKey` | `String!` |  | Unique identifier for the scheduled transaction. |
| `internalNote` | `String` | `""` | Optional short note about the scheduled transaction for internal use. |
| `ledgerNumber` | `String!` |  | The number of the ledger the scheduled transaction is for. |
| `metadata` | `JSONString` | `"{}"` | Any extra data that will be associated with scheduled transaction. |
| `netAmount` | `Int!` |  | The net amount of the scheduled transaction. |
| `postedAfter` | `DateTime!` |  | The schedule on which the scheduled transaction will be posted. |
| `reason` | `String!` |  | The reason why the scheduled transaction is added to the account. Based on the input this should be a valid charge or a valid credit reason code. |
| `taxAmount` | `Int!` |  | The tax amount of the scheduled transaction. |
| `taxRate` | `Decimal!` |  | The tax rate of the scheduled transaction. |

## `CreateShellAccountInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `billingAddressLine1` | `String` |  |  |
| `billingAddressLine2` | `String` |  |  |
| `billingAddressLine3` | `String` |  |  |
| `billingAddressLine4` | `String` |  |  |
| `billingAddressLine5` | `String` |  |  |
| `billingName` | `String` |  |  |
| `billingPeriodDay` | `Int` |  | Day to fixed bill on if billing_period_length set. |
| `billingPeriodLength` | `String` |  | For fixed billing accounts only, the length of their billing period. Can be MONTHLY or QUARTERLY. |
| `billingPeriodMonth` | `Int` |  | Month to start billing from if billing_period_length set to QUARTERLY or the multiplier is > 1. |
| `billingPeriodMultiplier` | `Int` |  | For fixed billing accounts only, the number the period length is to be multiplied by to get the total period length, i.e. for billing every second month, select 2 combined with a billing period length MONTHLY. Can't be > 1 for quarterly billing. |
| `billingPostcode` | `String` |  |  |
| `billingRichAddress` | `String` |  | This must be a string-ified version of the JSON representation of RichAddressInput type. |
| `brand` | `String` |  |  |
| `businessType` | `String` |  |  |
| `clientMutationId` | `String` |  |  |
| `companyName` | `String` |  |  |
| `companyNumber` | `String` |  |  |
| `dateOfBirth` | `Date` |  |  |
| `email` | `String!` |  |  |
| `familyName` | `String!` |  |  |
| `givenName` | `String!` |  |  |
| `isBusinessAccount` | `Boolean` |  |  |
| `landline` | `String` |  |  |
| `mobile` | `String` |  |  |
| `password` | `String` |  |  |
| `passwordUpdateToken` | `String` |  |  |
| `portfolioNumber` | `String` |  |  |
| `urn` | `String` |  |  |

## `CreateSolarWalletRelationshipType`

| Field | Type | Default | Description |
|---|---|---|---|
| `sourceAccountNumber` | `String` |  | Source account number of the solar wallet ledger. |
| `targetAccountNumber` | `String` |  | Target account number of the electricity ledger. |
| `validFrom` | `DateTime!` |  | Datetime when the solar wallet credit sharing ledger begins. |
| `validTo` | `DateTime` |  | Datetime when the solar wallet credit sharing ledger ends. |

## `CreateTimeSeriesPricesInput`

Input data to create prices associated with the time series represented by the code.

| Field | Type | Default | Description |
|---|---|---|---|
| `code` | `NonEmptyString!` |  | The time series code. |
| `entries` | `[TimeSeriesEntryInput!]!` |  | The time series entries. |
| `productCode` | `NonEmptyString` |  | The product code associated to the time series. |

## `CupsValidationToContractInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `electricityCups` | `String!` |  | The electricity cups to validate. |
| `electricityProductId` | `ID!` |  | The electricity product id to validate. |
| `gasCups` | `String` |  | The gas cups to validate. |
| `gasProductId` | `ID` |  | The gas product id to validate. |

## `CustomerDetailsInput`

Details about the customer.

| Field | Type | Default | Description |
|---|---|---|---|
| `dateOfBirth` | `Date` |  | The customer's date of birth. |
| `email` | `String` |  | Account email. |
| `familyName` | `String!` |  | Family name. |
| `givenName` | `String!` |  | Given name. |
| `label` | `String` |  | A free text field to help identifying the customer (e.g. for a job title). |
| `landline` | `String` |  | Account landline number. |
| `mobile` | `String` |  | Account mobile phone number. |
| `preferences` | `UpdateAccountUserCommsPreferencesInput` | `null` | The customer's communication preferences. |
| `pronouns` | `String` |  | The customer's pronouns. |
| `title` | `String` |  | The customer's title. |

## `CustomerFeedbackInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |
| `answer` | `String` |  |  |
| `feedbackId` | `Int!` |  |  |
| `formId` | `Int!` |  |  |
| `issueResolved` | `Boolean!` |  |  |

## `CustomerProfileInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `addressLine1` | `String!` |  | Line 1 of customer's address. |
| `addressLine2` | `String` |  | Line 2 of customer's address. |
| `addressLine3` | `String` |  | Line 3 of customer's address. |
| `addressLine4` | `String` |  | Line 4 of customer's address. |
| `addressLine5` | `String` |  | Line 5 of customer's address. |
| `email` | `String!` |  | Customer's email. |
| `familyName` | `String!` |  | Customer's family name. |
| `givenName` | `String!` |  | Customer's given name. |
| `phoneNumber` | `String!` |  | Customer's phone number. |
| `postcode` | `String!` |  | Customer's postcode. |

## `DeAuthenticationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |
| `deviceType` | `KrakenFlexDeviceTypes` | `null` | The most recently registered device of this type will be de-authenticated. |

## `DeauthenticateFlexDeviceInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `deviceId` | `String!` |  | Device ID. |

## `DeductLoyaltyPointsInput`

The input type for deducting Loyalty Points.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `accountUserId` | `String` |  | The related user id to deduct points from. The primary account user will have their points deducted if this isn't present. |
| `idempotencyKey` | `UUID` |  | A unique idempotency key for the deduction operation. |
| `note` | `String` |  | A note about the deduction. |
| `points` | `Int!` |  | The number of Loyalty Points to deduct. |
| `reasonCode` | `LoyaltyPointDeductionEntryReasonCode` | `null` | The reason code associated with the deduction. |

## `DelayerDaysInput`

Input type for the PaysByDirectDebitTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `days` | `Int!` |  | Number of days to delay based on delay strategy. |
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `strategy` | `DelayerDaysStrategy!` |  | Defines the method for calculating the delay period. |

## `DeleteAccountReferenceInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number associated with the removed AccountReference. |
| `namespace` | `String!` |  | The namespace associated with the removed AccountReference. |

## `DeleteBoostChargeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |

## `DeleteMfaDeviceInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `mfaMethod` | `MFAMethodChoices!` |  | MFA method. |

## `DeletePropertyDescendantsInput`

Input for deleting all descendants of a property in a hierarchy.

| Field | Type | Default | Description |
|---|---|---|---|
| `hierarchyName` | `String` | `"default"` | The name of the hierarchy. |
| `propertyId` | `ID!` |  | The ID of the property whose descendants should be deleted. |

## `DeletePushNotificationBindingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `token` | `String!` |  | Device push notification token. |

## `DepositAgreementInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |
| `depositKey` | `String!` |  |  |

## `DetachSupplyPointFromEstimationGroupInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `supplyPointExternalId` | `String!` |  | Supply point external identifier. |
| `supplyPointPeriodStart` | `DateTime` | `null` | Datetime period start to look for supply point. |

## `DetailsInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `namespace` | `String!` |  | Namespace of the detail. |
| `value` | `String` |  | Value of the detail. |

## `DeviceDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `auxDeviceVariantId` | `ID` |  | Auxiliary device variant id. |
| `deviceVariantId` | `ID` |  | Unique device variant id. |

## `DeviceRegistrationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |
| `authentication` | `AuthenticationInput` |  | The authentication details required given the chosen provider. |
| `deviceDetails` | `DeviceDetailsInput` |  | The device type specific details required for registering a device. |
| `deviceType` | `KrakenFlexDeviceTypes!` |  | The device type to be registered - batteries, electric vehicles, heat pumps or thermostats. |
| `propertyId` | `Int!` |  | The ID of the property the device belongs to. |
| `provider` | `ProviderChoices!` |  | The provider used to authenticate the device. |

## `DoubleOptInInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The number of the account requesting the double opt-in. |
| `consentTypeCode` | `String!` |  | The consent type code to create a consent for. |
| `emailAddress` | `String` |  | The email address of the customer requesting the double opt-in. |
| `ipAddress` | `String!` |  | The IP address of the customer requesting the double opt-in. |
| `mobileNumber` | `String` |  | The mobile number of the customer requesting the double opt-in. |

## `EVChargerLeadZohoType`

| Field | Type | Default | Description |
|---|---|---|---|
| `chargerModel` | `String` |  | Charger model of the lead. |
| `email` | `String` |  | Email of the lead. |
| `extraCable` | `Boolean` |  | Extra cable of the lead. |
| `firstName` | `String` |  | First name of the lead. |
| `garage` | `String` |  | Garage of the lead. |
| `lastName` | `String` |  | Last name of the lead. |
| `phoneNumber` | `String` |  | Phone number of the lead. |
| `postcode` | `String` |  | Postcode of the lead. |
| `powerBalance` | `Boolean` |  | Power balance of the lead. |
| `triphasic` | `Boolean` |  | Triphasic of the lead. |

## `ElectricityAgreementTransferEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `changeOfTenancyType` | `ChangeOfTenancyType!` |  | Change of tenancy type (subrogation or transfer). |
| `externalIdentifier` | `String!` |  | The market supply point identification number. |
| `requestedSupplyStartDate` | `Date` |  | The requested supply start date for the supply point. |
| `requestedSupplyStartDateType` | `RequestedDateType` | `null` | The requested supply start date type for the supply point. |

## `ElectricityEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `agreementTransferData` | `ElectricityAgreementTransferEnrollmentMarketInput` |  | Data required for agreement transfer enrollment (move in with change of tenancy by subrogation or transfer, without new product selection). |
| `productCatalogData` | `ElectricityProductCatalogEnrollmentMarketInput` |  | Data required for enrollment with product catalogue. |

## `ElectricityFiltersInput`

Filter measurements by electricity parameters.

| Field | Type | Default | Description |
|---|---|---|---|
| `deviceId` | `String` |  | The identifier of the specific device associated to this reading. |
| `marketSupplyPointId` | `String` |  | The identifier of the market supply point associated to this reading. |
| `readingDirection` | `ReadingDirectionType` | `CONSUMPTION` | Reading direction is based on the utility generated or consumed by the customer. |
| `readingFrequencyType` | `ReadingFrequencyType` | `RAW_INTERVAL` | The frequency of the reading. |
| `readingQuality` | `ReadingQualityType` | `COMBINED` |  |
| `registerId` | `String` |  | The identifier of the register associated to this reading. |

## `ElectricityProductCatalogEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `externalIdentifier` | `String!` |  | The market supply point identification number. |
| `monthlyPaymentAmount` | `Int` |  | The monthly payment amount to set for a regular payment schedule. |
| `moveInData` | `ElectricityProductCatalogMoveInEnrollmentMarketInput` |  | Data required for move-in enrollment with change of tenancy by transfer and a new product. |
| `product` | `String!` |  | The code of the product to be enrolled. |
| `productCharacteristics` | `GenericScalar` |  | A JSON object containing the product characteristics for the selected product. |
| `ratesAgreedAt` | `DateTime` |  | The datetime when the rates of the product were agreed. This is usually the datetime corresponding to when the quote/offer was generated. |
| `requestedSupplyStartDate` | `Date` |  | The requested supply start date for the supply point. |
| `requestedSupplyStartDateType` | `RequestedDateType` | `null` | The requested supply start date type for the supply point. |
| `retailerSwitchData` | `ElectricityProductCatalogRetailerSwitchEnrollmentMarketInput` |  | Data required for retailer switch enrollment without change of tenancy. |
| `retailerSwitchWithChangeOfTenancyData` | `ElectricityProductCatalogRetailerSwitchWithChangeOfTenancyEnrollmentMarketInput` |  | Data required for retailer switch enrollment with change of tenancy. |
| `supplyPointCharacteristicsList` | `[CharacteristicValueInput]` |  | List of supply point characteristics. |

## `ElectricityProductCatalogMoveInEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `changeOfTenancyType` | `ChangeOfTenancyType!` |  | Change of tenancy type (must be transfer for product catalog enrollment). |

## `ElectricityProductCatalogRetailerSwitchEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `dismissDebtRejections` | `Boolean!` |  | Whether to dismiss debt-related rejections during enrollment. |
| `dismissSocialBonusRejections` | `Boolean!` |  | Whether to dismiss social bonus-related rejections during enrollment. |
| `essentialIndicator` | `EssentialIndicator!` |  | Indicates if the supply is not essential, essential for electrodependency or essential without electrodependency. |
| `essentialIndicatorLastMovementDate` | `Date` |  | The date the essential supply was changed at. |
| `reeCode` | `String` |  | Identifies the DNO. |

## `ElectricityProductCatalogRetailerSwitchWithChangeOfTenancyEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `atrContractType` | `ATRType!` |  | The ATR contract type. |
| `atrTariff` | `ElectricityATRChoices!` |  | The ATR tariff type. |
| `changeOfTenancyType` | `ChangeOfTenancyType!` |  | Change of tenancy type. |
| `cnae` | `String!` |  | The CNAE code associated with the supply point. |
| `dismissDebtRejections` | `Boolean!` |  | Whether to dismiss debt-related rejections during enrollment. |
| `dismissSocialBonusRejections` | `Boolean!` |  | Whether to dismiss social bonus-related rejections during enrollment. |
| `essentialIndicator` | `EssentialIndicator!` |  | Indicates if the supply is not essential, essential for electrodependency or essential without electrodependency. |
| `essentialIndicatorLastMovementDate` | `Date` |  | The date the essential supply was changed at. |
| `estimatedAnnualConsumption` | `Int` |  | The estimated annual consumption. |
| `power` | `[Float]!` |  | List of power values (provide a maximum of 6). |
| `reeCode` | `String` |  | Identifies the DNO. |
| `selfConsumptionType` | `SelfConsumptionType!` |  | The self consumption type. |
| `subsectionType` | `SubsectionType` | `null` | The subsection type. |

## `ElectricityTerminationInput`

Input required to initiate a LeaveSupplier journey for the electricity market.

| Field | Type | Default | Description |
|---|---|---|---|
| `additionalInformation` | `String` |  | The declared additional information for the request. |
| `contactName` | `String` | `null` | The declared contact name for the request. |
| `contactTelephoneNumber` | `String!` |  | The contact phone number for the request. |
| `cutReason` | `CutReason!` |  | The declared reason for the request. |
| `desiredEffectiveDate` | `Date` |  | The requested last day of supply. |
| `desiredEffectiveDateType` | `RequestedDateType!` |  | The requested supply end date type for the leave supplier. |
| `supplyPointIdentifier` | `String!` |  | The market supply point identification number. |

## `EmailContentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `bodyHtml` | `String` |  | An HTML email body. At least one of bodyTxt or bodyHtml must be provided. |
| `bodyTxt` | `String` |  | A plain text email body. At least one of bodyTxt or bodyHtml must be provided. |
| `fromEmail` | `String!` |  | Either the sender's email address or the sender's name and email address (for example, 'sender@example.com' or 'Sender Name <sender@example.com>'). |
| `replyToEmails` | `[String]` |  | List of reply-to email addresses (for example, 'reply@example.com'). |
| `subjectTxt` | `String!` |  | The email subject line. |
| `toEmail` | `String!` |  | The recipient email address (for example, 'user@example.com'). |

## `EndContributionAgreementInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `contributionAgreementId` | `ID!` |  | The ID of the Contribution Agreement to end. |
| `endAt` | `DateTime` |  | The future end datetime of the agreement. If not given, terminate now. |

## `EnqueueInboundCallInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `callId` | `ID!` |  | The ID of the call to enqueue. |
| `inferLanguageAttribute` | `Boolean` | `true` | Whether to infer the preferred language of the calling account. |
| `inferOperationsGroupAttributes` | `Boolean` | `true` | Whether to infer the operations group attributes of the calling account. |
| `priority` | `Int` | `0` | The priority with which the call should be routed. A higher number corresponds to a higher routing priority. |
| `routingAttributes` | `[String!]` |  | List of routing attribute references to add to the call. For example, 'SKILL.ENERGY'. Each attribute should already have been created in Kraken. |
| `waitingBehaviourUrl` | `String` |  | A URL that defines the behaviour of the call when it is enqueued and the caller is waiting. If not set, audio configured in Kraken will be played to the caller. The URL must return a response that can be interpreted by the vendor handling the call. For example, if the call is handled by Twilio, TwiML supported by a <Conference> waitUrl must be returned. |

## `EnrollAccountInLoyaltyProgramInput`

The input type for enrolling an account in loyalty program.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number to enroll. |
| `accountUserId` | `ID` |  | The account user id to enroll. |

## `EnrollmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The Kraken account number. |
| `bankDetails` | `BankDetailsInput` | `null` | Bank details for setting up a payment instruction as part of the enrollment. |
| `contractIdentifiers` | `[String]` |  | Contract identifiers for contracts that this journey's account is subject to. |
| `instructionDetails` | `InstructionDetailsInput` | `null` | Details of an externally created payment instruction to be recorded in Kraken. |
| `leaveSupplierNumber` | `String` |  | If this is a house move, the number of the leave supplier process associated with the move out. |
| `note` | `String` |  | Enrollment note. |
| `paymentSchedule` | `PaymentScheduleDetailsInput` | `null` | Details of the payment schedule(s) to be created as part of enrollment. |
| `paymentSlipDetails` | `PaymentSlipDetailsInput` | `null` | Payment slip details for setting up a payment instruction in the vendor's system as part of the enrollment. |
| `salesInfo` | `SalesInformationInput` | `null` | Sales info for this enrollment. |
| `securityDeposit` | `SecurityDepositInput` | `null` | Details of the security deposit to be created as part of enrollment. |

## `ExternalAccountEventContent`

A piece of content associated with an external account event.

| Field | Type | Default | Description |
|---|---|---|---|
| `contentType` | `ExternalAccountEventContentType!` |  | The content type of the content. |
| `description` | `String!` |  | A human-readable description of the content. |
| `value` | `String!` |  | The value of the content. |

## `ExtraDetailsItem`

| Field | Type | Default | Description |
|---|---|---|---|
| `key` | `String` | `null` | The key of the extra detail item to be added or modified. |
| `value` | `GenericScalar` | `null` | The value of the extra detail item to be added or modified. |

## `FailedPaymentDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `actionIntent` | `PaymentActionIntentOneOfInput!` |  | The payment action intent details that identify the target for this payment. |
| `amount` | `Int!` |  | The payment amount in the minor unit of currency. |
| `customerReference` | `String!` |  | The description of the payment, as shown to the customer. |
| `failedAt` | `DateTime!` |  | The datetime when the payment failed. |
| `failureDescription` | `String` |  | The customer-facing description of the failure. |
| `failureReason` | `FailureReason!` |  | The reason for the failure. |
| `paymentDate` | `Date!` |  | The date when the payment was made. |
| `paymentMethod` | `PaymentMethodInput!` |  | The details of the payment method used for this payment. |
| `reference` | `String!` |  | The reference used to uniquely identify this payment. |
| `vendorFailureCode` | `String` |  | The code the payment provider specified. |

## `FetchGeneratePaymentFingerprintInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `paymentInstructionId` | `Int!` |  | Payment instruction ID. |

## `FetchPreSignedLinkForOpportunityAttachmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `attachmentId` | `ID` | `null` | File attachment ID. |
| `opportunityNumber` | `String` | `null` | Opportunity number. |

## `ForceReauthenticationInput`

The input type for repudiating previously issued Kraken Tokens and refresh tokens.

| Field | Type | Default | Description |
|---|---|---|---|
| `includeThirdParties` | `Boolean!` |  | Also force third-party applications you have authorized to use your account to reauthenticate. |

## `FormSubmissionInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |
| `content` | `JSONString!` |  | Form content. |
| `formType` | `FormType` | `null` | Form type. |

## `GasAgreementTransferEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `changeOfTenancyType` | `ChangeOfTenancyType!` |  | Change of tenancy type (subrogation or transfer) for the supply point. |
| `externalIdentifier` | `String!` |  | The market supply point identification number. |
| `isNewRegularAddress` | `NoYes!` |  | New use of the supply point address. |
| `requestedSupplyStartDate` | `Date` |  | The requested supply start date for the supply point. |
| `requestedSupplyStartDateType` | `RequestedDateType!` |  | The requested supply start date type for the supply point. |

## `GasEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `agreementTransferData` | `GasAgreementTransferEnrollmentMarketInput` |  | Data required for agreement transfer enrollment. |
| `productCatalogData` | `GasProductCatalogEnrollmentMarketInput` |  | Data required for enrollment with product catalogue. |

## `GasFiltersInput`

Filter measurements by gas parameters.

| Field | Type | Default | Description |
|---|---|---|---|
| `deviceId` | `String` |  | The identifier of the specific device associated to this reading. |
| `marketSupplyPointId` | `String` |  | The identifier of the market supply point associated to this reading. |
| `readingFrequencyType` | `ReadingFrequencyType` | `RAW_INTERVAL` | The frequency of the reading. |
| `registerId` | `String` |  | The identifier of the register associated to this reading. |

## `GasProductCatalogEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `externalIdentifier` | `String!` |  | The market supply point identification number. |
| `monthlyPaymentAmount` | `Int` |  | The monthly payment amount to set for a regular payment schedule. |
| `product` | `String!` |  | The code of the product to be enrolled. |
| `productCharacteristics` | `GenericScalar` |  | A JSON object containing the product characteristics for the selected product. |
| `ratesAgreedAt` | `DateTime` |  | The datetime when the rates of the product were agreed. This is usually the datetime corresponding to when the quote/offer was generated. |
| `requestedSupplyStartDate` | `Date` |  | The requested supply start date for the supply point. |
| `requestedSupplyStartDateType` | `RequestedDateType` | `null` | The requested supply start date type for the supply point. |
| `retailerSwitchData` | `GasProductCatalogueRetailerSwitchEnrollmentMarketInput` |  | Data required for retailer switch enrollment without change of tenancy. |
| `retailerSwitchWithChangeOfTenancyData` | `GasProductCatalogueRetailerSwitchWithChangeOfTenancyEnrollmentMarketInput` |  | Data required for retailer switch enrollment with change of tenancy. |
| `supplyPointCharacteristicsList` | `[CharacteristicValueInput]` |  | List of supply point characteristics. |

## `GasProductCatalogueRetailerSwitchEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `dismissDebtRejections` | `Boolean!` |  | Whether to dismiss debt-related rejections during enrollment. |
| `estimatedAnnualFlow` | `String!` |  | The estimated annual flow. |

## `GasProductCatalogueRetailerSwitchWithChangeOfTenancyEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `changeOfTenancyType` | `ChangeOfTenancyType!` |  | Change of tenancy type (subrogation or transfer) for the supply point. |
| `city` | `String!` |  | The city of the supply property. |
| `dismissDebtRejections` | `Boolean!` |  | Whether to dismiss debt-related rejections during enrollment. |
| `door` | `String` |  | The door of the supply property. |
| `estimatedAnnualFlow` | `String!` |  | The estimated annual flow. |
| `floor` | `String` |  | The floor of the supply property. |
| `isPrincipalHouse` | `Boolean!` |  | Whether the supply property is the principal house of the customer. |
| `postalCode` | `String!` |  | The postal code of the supply property. |
| `province` | `Provinces!` |  | The province of the supply property. |
| `streetName` | `String!` |  | The street name of the supply property. |
| `streetNumber` | `String!` |  | The street number of the supply property. |
| `streetType` | `String!` |  | The street type of the supply property. |

## `GasSelfReadingSubmissionInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `cups` | `String!` |  | The CUPS identifier for the supply point. |
| `extraInfo` | `String` |  | Optional additional information about the reading. |
| `readingDate` | `Date!` |  | Date when the reading was taken. |
| `readingValue` | `Decimal!` |  | The meter reading value. |

## `GasTerminationInput`

Input required to initiate a LeaveSupplier journey for the gas market.

| Field | Type | Default | Description |
|---|---|---|---|
| `additionalInformation` | `String` |  | The declared additional information for the request. |
| `contactTelephoneNumber` | `String!` |  | The contact phone number for the request. |
| `cutReason` | `CutReason!` |  | The declared reason for the request. |
| `desiredEffectiveDate` | `Date` |  | The requested last day of supply. |
| `desiredEffectiveDateType` | `RequestedDateType!` |  | The requested supply end date type for the leave supplier. |
| `desiredEffectiveTime` | `Time` | `null` | The requested suppy end time for the leave supplier. |
| `supplyPointIdentifier` | `String!` |  | The market supply point identification number. |
| `typeOfPerson` | `PersonType` | `null` | The declared reason for the request. |

## `GenerateAffiliatesAudioRecordingPreSignedUrlInput`

Input fields to generate a pre-signed upload URL for an affiliates audio recording.

| Field | Type | Default | Description |
|---|---|---|---|
| `filename` | `String!` |  | The name of the file to be uploaded. |

## `GenerateInkPresignedUrlInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `channel` | `InkCommunicationChannel!` |  | The channel of the contact. |
| `filename` | `String!` |  | The name of the file. |

## `GenerateLeadsFileAttachmentDownloadPreSignedUrlInput`

Input fields to generate a pre-signed download URL for a leads file attachment.

| Field | Type | Default | Description |
|---|---|---|---|
| `attachmentId` | `ID!` |  | The ID of the opportunity file attachment. |
| `opportunityNumber` | `String!` |  | The unique opportunity number to which the file attachment belongs. |

## `GenerateLeadsFileAttachmentPreSignedUrlInput`

Input fields to generate a pre-signed upload URL for a leads file attachment.

| Field | Type | Default | Description |
|---|---|---|---|
| `category` | `OpportunityAttachmentCategory!` |  | The category of the file. The list of allowed values is specified by the client. |
| `filename` | `String!` |  | The name of the file to be uploaded. |
| `opportunityNumber` | `String!` |  | The unique opportunity number to which the file is related. |

## `GetEmbeddedSecretForNewPaymentInstructionInput`

The input for getting the client secret for an embedded new card payment method form.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `instructionType` | `PaymentType!` |  | The type of the new payment instruction. |
| `ledgerNumber` | `String` |  | **WARNING: Will be mandatory in future versions** The number of the ledger. |

## `GetEmbeddedSecretForNewPaymentInstructionWithoutAccountInput`

The input for getting the client secret for an embedded new stored payment method form.

| Field | Type | Default | Description |
|---|---|---|---|
| `instructionType` | `PaymentType!` |  | The type of the new payment instruction. |

## `GetHostedUrlForNewPaymentInstructionInput`

The input needed for getting the external URL for setting up a payment instruction.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `instructionType` | `PaymentType!` |  | The type of the new payment instruction. |
| `ledgerNumber` | `String` |  | The ledger number. |
| `returnUrlCancel` | `String` |  | The URL to redirect the user to after the action was cancelled. |
| `returnUrlError` | `String` |  | The URL to redirect the user to after the action resulted in an error. |
| `returnUrlFailure` | `String` |  | The URL to redirect the user to after the action resulted in a failure. |
| `returnUrlSuccess` | `String` |  | The URL to redirect the user to after the action was completed successfuly. |

## `GrantUserAccessToBusinessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `businessId` | `ID!` |  | The ID of the business that will grant access. |
| `roleCode` | `String!` |  | The code of the role that will be granted. |
| `userNumber` | `String!` |  | The number of the user that will gain access. |

## `GuaranteeOfOriginConfigurationInput`

Input type for the GuaranteeOfOriginConfigurationTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `guaranteeOfOriginPercentage` | `GuaranteeOfOriginPercentage` | `null` | The percentage of the guarantee of origin. |
| `isVariable` | `Boolean` |  | Whether the term is variable. |

## `IndexationOptionsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `escalationStartAt` | `DateTime` |  | The escalation start date for the product rate override configuration. |
| `indexCode` | `String` |  | The index code for the product rate override configuration. |

## `InitiateHostedStandalonePaymentInput`

Input fields for initiating a hosted standalone payment. The amount should always be provided in the minor unit of currency (e.g., pence not pounds, cents not dollars, etc.). A standalone payment can be made against a specific ledger (e.g., a debt ledger) by providing the ledger number (or ledger id, please see deprecated fields).

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `amount` | `Int!` |  | The amount to be collected in the minor unit of currency. |
| `collectionMethod` | `CollectionMethod!` |  | The method by which the payment is being collected. |
| `description` | `String!` |  | A description of the purpose of the payment. |
| `ledgerNumber` | `String` |  | The number of the specific ledger against which this payment should be applied. |
| `returnUrlCancel` | `String` |  | The URL to redirect the user to after the action was cancelled. |
| `returnUrlError` | `String` |  | The URL to redirect the user to after the action resulted in an error. |
| `returnUrlExpired` | `String` |  | The URL to redirect the user to if the url is not longer valid. |
| `returnUrlFailure` | `String` |  | The URL to redirect the user to after the action resulted in a failure. |
| `returnUrlPending` | `String` |  | The URL to redirect the user to after the action was completed but the payment is still being processed. |
| `returnUrlSuccess` | `String` |  | The URL to redirect the user to after the action was completed successfuly. |

## `InitiateProductSwitchInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Identification of the account that requesting the product switch. |
| `quotedProductId` | `ID!` |  | ID of the selected quoted product, obtain from quoting that supply point. |
| `suppressCommunications` | `Boolean` | `true` | Suppress Product Switch communications. |
| `switchDate` | `Date!` |  | The date at which the product switch becomes effective. |
| `userId` | `ID` |  | The user for whom to perform the update. This is only needed when using an Organisation role. |

## `InitiateStandalonePaymentInput`

Input fields for initiating a standalone payment. The amount should always be provided in the minor unit of currency (e.g., pence not pounds, cents not dollars, etc.). A standalone payment can be made against a specific ledger (e.g., a debt ledger) by providing the ledger number. Accounts have a default ledger that will be used if not provided.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `amount` | `Int!` |  | The amount to be collected in the minor unit of currency. |
| `collectionMethod` | `CollectionMethod` | `null` | The method by which the payment is being collected. |
| `description` | `String!` |  | A description of the purpose of the payment. |
| `isTelephoneInitiated` | `Boolean` |  | Whether the authorisation to initiate the payment was given over the phone. |
| `ledgerNumber` | `String` |  | The number of the specific ledger against which this payment should be applied. |

## `InkEmailMessageInput`

This type is used to create an inbound email.

| Field | Type | Default | Description |
|---|---|---|---|
| `attachments` | `[InkGenericMessageAttachmentInput!]` |  | Message attachments. |
| `ccAddresses` | `[Email!]` |  | The carbon copy (cc) email addresses the message was sent to. |
| `fromAddress` | `Email!` |  | The email address the message was sent from. |
| `plainTextContent` | `String!` |  | The content of the message, as plain text. |
| `s3Bucket` | `String` |  | The S3 bucket in which the original email is stored. |
| `s3Key` | `String` |  | The S3 key of the original email. |
| `subject` | `String!` |  | The email subject/title. |
| `toAddresses` | `[Email!]!` |  | The email addresses the message was sent to. |

## `InkGenericMessageAttachmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `s3Bucket` | `String!` |  | The S3 bucket of the attachment. |
| `s3Key` | `String!` |  | The S3 key of the attachment. |

## `InkGenericMessageInput`

This type is used to create an generic message.

| Field | Type | Default | Description |
|---|---|---|---|
| `attachments` | `[InkGenericMessageAttachmentInput!]` |  | Message attachments. |
| `fromHandle` | `String!` |  | The identity the message was sent from. |
| `plainTextContent` | `String!` |  | The content of the message, as plain text. |
| `toHandle` | `String!` |  | The identity the message was sent to. |

## `InkLiveChatMessageInput`

This type is used to create a live chat message.

| Field | Type | Default | Description |
|---|---|---|---|
| `attachments` | `[InkGenericMessageAttachmentInput!]` |  | Message attachments. |
| `fromHandle` | `String!` |  | The identity the message was sent from. |
| `plainTextContent` | `String!` |  | The content of the message, as plain text. |

## `InkMessageInput`

An Ink message used as an input. This is intended to be morally equivalent to a tagged union; exactly one of the properties provided here is expected to be provided. At current, only a few channels are provided. This is intended to be a backwards-compatible extension point to allow other message input types to be added in the future.

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `InkEmailMessageInput` |  |  |
| `generic` | `InkGenericMessageInput` |  |  |
| `liveChat` | `InkLiveChatMessageInput` |  |  |
| `post` | `InkPostMessageInput` |  |  |

## `InkPostMessageInput`

This type is used to create an inbound post.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number that the letter was sent from. |
| `attachments` | `[InkGenericMessageAttachmentInput!]` |  | Message attachments. |
| `notes` | `String` |  | Notes on the letter. |
| `plainTextContent` | `String!` |  | The content of the message, as plain text. |

## `InkStorylineEntryInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `content` | `String!` |  | The content of the storyline entry. |
| `contentId` | `BigInt` |  | The optional related object ID of the entry. |
| `entryType` | `StorylineEntryTypes!` |  | The type of the storyline entry. |
| `isRootCause` | `Boolean` | `false` | Whether this entry is identified as the root cause of the issue. |
| `occurredAt` | `DateTime!` |  | The datetime when the storyline entry occurred. |
| `url` | `String` |  | Optional URL related to the storyline entry. |

## `InstigateContractVariationInput`

Input type for instigating a contract variation.

| Field | Type | Default | Description |
|---|---|---|---|
| `applicableAt` | `DateTime` |  | The date from which the varied terms will apply. |
| `contractNote` | `ContractNoteInput` |  | Optional note to capture at the point of variation. |
| `identifier` | `NonEmptyString!` |  | The unique identifier of the contract to vary. |
| `terms` | `[OneOfTermInput!]!` |  | The terms to be varied in the contract. |

## `InstructionDetailsInput`

Input type for instruction details that was created using the embedded process. This means it was set up in the vendor system, and we only need to store a representation of the instruction in Kraken, but not make any calls to the vendor. This method of instruction creation must always be used for creating card instructions.

| Field | Type | Default | Description |
|---|---|---|---|
| `instructionType` | `PaymentType!` |  | The type of the payment instruction. |
| `validFrom` | `DateTime!` |  | The datetime from which the instruction is vaild. |
| `vendorName` | `Vendor!` |  | The name of the vendor the payment instruction was set up with. |
| `vendorReference` | `String!` |  | The vendor's reference for this payment instruction. |

## `InvalidatePaymentInstructionInput`

Input for invalidating an arbitrary payment instruction.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |
| `id` | `String!` |  | The id of the payment instruction to be invalidated. |

## `InvalidatePreSignedTokenInput`

Input type for the InvalidatePreSignedToken mutation.

| Field | Type | Default | Description |
|---|---|---|---|
| `token` | `String!` |  |  |

## `InvalidatePreSignedTokensForUserInput`

Input type for the InvalidatePreSignedTokensForUser mutation.

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `String!` |  | The email address of the user whose tokens should be invalidated. |
| `scope` | `PreSignedTokenScope` | `null` | The scope of the token to invalidate. If this argument is not specified, all pre-signed tokens issued to the user are invalidated. |

## `InvalidateRefreshTokenInput`

Input type for the InvalidateRefreshToken mutation.

| Field | Type | Default | Description |
|---|---|---|---|
| `refreshToken` | `String!` |  |  |

## `InvalidateRefreshTokensForUserInput`

Input type for the InvalidateRefreshTokensForUser mutation.

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `String!` |  | The email address of the user whose tokens should be invalidated. |

## `JoinSupplierAcceptTermsAndConditionsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number of the join supplier process (e.g. A-12345678). |
| `joinSupplierProcessNumber` | `NonEmptyID` |  | The JoinSupplierProcess number. |

## `LatePaymentFeesInput`

Input type for the LatePaymentFeesTerm. This type is used to create or update late payment fees terms in contracts. If `percentage_fee` is provided, `percentage_interval_days` must also be provided.

| Field | Type | Default | Description |
|---|---|---|---|
| `flatFeeAmount` | `Decimal` |  | The flat fee amount for late payment. |
| `interestPolicyName` | `String` |  | The interest policy to use for late payment fee calculations. |
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `percentageFee` | `Decimal` |  | The percentage fee for late payment. |
| `percentageIntervalDays` | `Decimal` |  | The interval in days for the percentage fee (1=daily, 7=weekly, 30=monthly, 365=yearly). |

## `LeadBlockListValidationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `emailDomain` | `String` |  | email_domain |
| `iban` | `String` |  | iban |
| `nameKeyword` | `String` |  | name_keyword |

## `LeadContactDetailsFiltersInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `role` | `LeadContactRoles` | `null` | The role of the contact. |

## `LeadContactDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `String` |  | The email address of the contact. |
| `extraDetailItems` | `[ExtraDetailsItem]` |  | Extra details for the contact as key/value pairs. |
| `familyName` | `String` |  | The family name of the contact. |
| `givenName` | `String` |  | The given name of the contact. |
| `phoneNumber` | `String` |  | The phone number of the contact. |
| `roles` | `[LeadContactRoles]` | `null` | The roles of the contact. |

## `LeadSupplyPoint`

| Field | Type | Default | Description |
|---|---|---|---|
| `externalIdentifier` | `String!` |  | The supply point ID. |
| `marketName` | `String!` |  | The product's market name. |

## `LeadSupplyPointFiltersInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `marketCodes` | `[SupplyPointMarketNameEnum]` |  | Supply points market codes to filter opportunities. |

## `LeadsQueryInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `assignedToAffiliateNumber` | `String` | `"NotSupplied"` | Filter opportunities by assigned to affiliate number. |
| `assignedToTeam` | `String` | `"NotSupplied"` | The name of the team the leads are assigned to. |
| `assignedToUsername` | `String` | `"NotSupplied"` | The username of the user the leads are assigned to. |
| `freeText` | `String` | `null` | Free text field that will search against different identifiers of the lead. Currently supported include: lead number, phone number, email, name. |
| `leadType` | `LeadTypeChoices` | `null` | Filter leads by type. |
| `stageCode` | `String` | `null` | Filter leads by stage code. |

## `LeaveSupplierInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The Kraken account number. |
| `futureBillingAddress` | `RichAddressInput` | `null` | Future billing address. |
| `marketData` | `LeaveSupplierMarketInputType` | `null` |  |
| `requestedSupplyEndDate` | `Date!` |  | The requested last day of supply. |
| `subtype` | `LeaveSupplierSubType` | `null` | The type of leave supplier process to initiate. |

## `LeaveSupplierMarketInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `electricitySupplyPointData` | `[ElectricityTerminationInput]` |  | A list of Electricity leave supplier details. |
| `gasSupplyPointData` | `[GasTerminationInput]` |  | A list of Gas leave supplier details. |

## `LegacyCustomerOrderInput`

Input type for specifying a customer, either an account or a business (legacy).

| Field | Type | Default | Description |
|---|---|---|---|
| `account` | `NonEmptyString` |  | The account number. |
| `business` | `Int` |  | The business identifier. |

## `LegacyItemProfileInput`

Input type for item profile (legacy).

| Field | Type | Default | Description |
|---|---|---|---|
| `characteristics` | `JSONString!` |  | The characteristic values for this item profile. |

## `LegacyMarketDataInput`

Input type combining base supply point group fields with market-specific enrollment data (legacy). Inherits address/property fields from BaseSupplyPointGroupInput and adds a single `context` field whose type is a dynamically constructed InputObjectType containing one field per configured market (morally a oneOf – callers should supply exactly one).

| Field | Type | Default | Description |
|---|---|---|---|
| `addressDetails` | `LifecycleAddressInput` | `null` | The address where the supply points to be supplied are located. |
| `context` | `OneOfMarketEnrollmentInputType!` |  | Market-specific enrollment details. Provide exactly one of the configured market input objects inside this container. |
| `property` | `ID` |  | The ID of the property where the supply points are located. |

## `LegacyOrderInput`

Input type for creating or updating an order (legacy).

| Field | Type | Default | Description |
|---|---|---|---|
| `customer` | `LegacyCustomerOrderInput!` |  | The customer identifier who is placing the order. |
| `lines` | `[LegacyOrderLineInput!]!` |  | The order lines for this order. |
| `sale` | `SalesRecordInput!` |  | The sales record associated with this order. |
| `signedAt` | `DateTime` |  | The date and time at which the order was signed. A contract signing date, for example. This is required if the order contains terms. |
| `source` | `String` |  | The source Offering identifier that generated this Order. |
| `terms` | `[OneOfTermInput!]` |  | The terms applicable to this order. |

## `LegacyOrderItemInput`

Input type for order item (legacy).

| Field | Type | Default | Description |
|---|---|---|---|
| `code` | `NonEmptyString!` |  | The code identifying the item. |
| `marketData` | `LegacyMarketDataInput!` |  | Market-specific data for the item. |
| `profile` | `LegacyItemProfileInput` |  | The profile containing characteristics of the item. |

## `LegacyOrderLineInput`

Input type for `OrderLine` (legacy).

| Field | Type | Default | Description |
|---|---|---|---|
| `item` | `LegacyOrderItemInput!` |  | The item being ordered. |
| `period` | `LegacyOrderLinePeriodInput!` |  | The period for which this order line is valid. Can be a range or a duration. |
| `target` | `NonEmptyString` |  | The target customer identifier for this order line. |
| `terms` | `[OneOfTermInput!]` |  | The terms applicable to this order line. |

## `LegacyOrderLinePeriodInput`

Input type for order line period - either explicit dates or duration (legacy). Use either (start + end) OR duration, not both.

| Field | Type | Default | Description |
|---|---|---|---|
| `end` | `DateTime` |  | The end date and time of the period. |
| `start` | `DateTime` |  | The start date and time of the period. |

## `LegacyProcessOrderInput`

Input type for processing an order (legacy).

| Field | Type | Default | Description |
|---|---|---|---|
| `order` | `LegacyOrderInput!` |  | The order to be processed. |

## `LifecycleAddressInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `countryCode` | `String` |  | Country code. |
| `line1` | `String!` |  | Line 1 of address. |
| `line2` | `String` | `""` | Line 2 of address. |
| `line3` | `String` | `""` | Line 3 of address. |
| `line4` | `String` | `""` | Line 4 of address. |
| `line5` | `String` | `""` | Line 5 of address. |
| `postalCode` | `String!` |  | Postal code. |

## `LinkAccountToBusinessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountId` | `ID!` |  | The account ID. |
| `businessId` | `ID!` |  | The business ID. |
| `roleCode` | `BusinessRoleString` | `null` | The business role code of the linked account (default to OWNER). |
| `shouldOverwrite` | `Boolean` |  | Whether the business should be overwritten (default to false). |

## `LinkUserToLineInput`

Link an AccountUser to a LINE account.

| Field | Type | Default | Description |
|---|---|---|---|
| `linkToken` | `String!` |  |  |

## `LoyaltyPointLedgerEntryInput`

The input type for retrieving a loyalty point ledger entry.

| Field | Type | Default | Description |
|---|---|---|---|
| `idempotencyKey` | `UUID!` |  | The unique idempotency key for the ledger entry. |

## `LoyaltyPointLedgersInput`

The input type for retrieving a loyalty point ledger entry.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountUserId` | `ID!` |  | The account user id. |

## `LoyaltyPointsBalanceInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `accountUserId` | `String` |  | Optional account user id for more granular balance. |

## `LoyaltyPointsProgramEligibilityInput`

The input type for checking eligibility to join the loyalty points program.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number to check. |

## `MetadataInput`

The metadata input type for mutations.

| Field | Type | Default | Description |
|---|---|---|---|
| `identifier` | `String!` |  | An identifier for the associated object, e.g. account_number for the Account linked object type or email for the Account User linked object type. |
| `key` | `String!` |  | The key for the metadata. |
| `linkedObjectType` | `LinkedObjectType!` |  | The object that the metadata is associated with. |
| `value` | `JSONString!` |  | The metadata value which should be a valid JSON string. |

## `MinimumContractLengthInput`

Input type for the MinimumContractLengthTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `length` | `Int!` |  | The minimum length of the contract. |
| `unitOfTime` | `String!` |  | The unit of time for the contract length. |

## `MoveToBucketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `bucketName` | `String!` |  | The name of the bucket to move the conversation to. |
| `conversationRelayId` | `ID!` |  | The relay id of the conversation that will be moved to the bucket. |
| `unassignFromUsers` | `Boolean` | `false` | Whether to unassign from user buckets. Defaults to False (only unassign from team buckets). |

## `NonAccountRecipient`

| Field | Type | Default | Description |
|---|---|---|---|
| `brandCode` | `String` |  | The brand code of the company/entity sending the comm. If provided as empty string or the field is not included, it will default to the 'primary' brand. |
| `email` | `Email` |  | The email address of the recipient. |
| `familyName` | `String` |  | The family name of the recipient. |
| `givenName` | `String` |  | The given name of the recipient. |
| `mobile` | `String` |  | The mobile phone number of the recipient. |

## `OCPPAuthenticationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |
| `details` | `String!` |  | The OCPP authentication details. |

## `ObtainJSONWebTokenInput`

The input type for obtaining a Kraken Token (JWT). The currently supported inputs are: - account user email/password combination - account user API key - organization live secret key - pre-signed key - refresh token

| Field | Type | Default | Description |
|---|---|---|---|
| `APIKey` | `String` |  | API key of the account user. Use standalone, don't provide a second input field. |
| `captchaResponse` | `String` |  | The response from the CAPTCHA challenge. Use with 'email' and 'password' fields. |
| `organizationSecretKey` | `String` |  | Live secret key of an third-party organization. Use standalone, don't provide a second input field. |
| `preSignedKey` | `String` |  | Short-lived, temporary key (that's pre-signed). Use standalone, don't provide a second input field. |
| `refreshToken` | `String` |  | The refresh token that can be used to extend the expiry claim of a Kraken token. Use standalone, don't provide a second input field. |

## `ObtainLongLivedRefreshTokenInput`

The input type for obtaining a long-lived refresh token.

| Field | Type | Default | Description |
|---|---|---|---|
| `krakenToken` | `String!` |  | The Kraken Token that will be used to generate the long-lived refresh token. |

## `OfferQuoteSummaryInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |
| `offerGroupIdentifier` | `ID!` |  | Offer group identifier. |

## `OfferingForQuotingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `productComponents` | `[ProductComponentForQuotingInput]!` |  | Product components. |
| `productOfferingIdentifier` | `ID!` |  | Product offering identifier. |
| `quotePeriodEndDatetime` | `DateTime` |  | End datetime for the quote period for all products in this offering. Defaults to 1 year from start if not provided. |
| `quotePeriodStartDatetime` | `DateTime` |  | Start datetime for the quote period for all products in this offering. Defaults to current datetime if not provided. |

## `OnSiteJobsAppointmentBookingDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `comments` | `String` |  | The comments for this appointment. |
| `commsStrategy` | `OnSiteJobsCommsStrategy!` |  | The communication strategy for this appointment. |
| `jobType` | `NonEmptyString!` |  | The type of job being booked for the appointment. |

## `OnSiteJobsAssetInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `additionalDetails` | `JSONString` |  | Additional details about the asset. |
| `externalIdentifier` | `NonEmptyString` |  | Asset external identifier. |
| `fuelType` | `OnSiteJobsAssetFuelType` | `null` | The current asset fuel type. |
| `kind` | `OnSiteJobsAssetKind!` |  | Asset kind. |
| `status` | `OnSiteJobsAssetStatus!` |  | Asset status. |
| `supplyPointIdentifierToMarketNameMapping` | `SupplyPointIdentifierToMarketNameMappingInput` |  | Supply point external identifier to market name mapping to associate with the asset. If this is provided, `supply_point_internal_id` cannot be provided. |
| `supplyPointInternalId` | `Int` |  | Internal ID of the supply point to associate with the asset. If this is provided, `supply_point_identifier_to_market_name_mapping` cannot be provided. |

## `OnSiteJobsCreateAppointmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `appointmentStatus` | `OnSiteJobsAppointmentStatus!` |  | The current status of the appointment. |
| `assets` | `[OnSiteJobsAssetInput!]` |  | List of assets associated with the appointment. |
| `cancellationCategory` | `OnSiteJobsAppointmentCancellationCategory` | `null` | The cancellation reason for this appointment. |
| `comments` | `String` |  | Appointment related comments. |
| `commsStrategy` | `OnSiteJobsCommsStrategy!` |  | The comms strategy. |
| `endAt` | `DateTime` |  | The end date/time of this appointment. |
| `externalReference` | `String!` |  | The external reference provided by the vendor/contractor for the appointment. |
| `jobNotes` | `JSONString` |  | The job notes. |
| `jobType` | `String!` |  | The type of job this appointment is for. |
| `requestId` | `UUID!` |  | The UUID of the On-Site Jobs request appointment is for. |
| `runActionsBasedOnStatus` | `Boolean` | `true` | Whether to run the side-effect action based on the new appointment status. Only applicable if a value was provided in the `status` field. Defaults to true. |
| `startAt` | `DateTime!` |  | The start date/time of this appointment. |

## `OnSiteJobsUpdateAppointmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `alignRequestStatusWithAppointment` | `Boolean` | `true` | When true, automatically updates the request status to match its appointments. Defaults to true. |
| `appointmentId` | `UUID!` |  | The Kraken ID of the appointment to update. |
| `assets` | `[OnSiteJobsAssetInput!]` |  | List of assets associated with the appointment. |
| `bypassTerminalAppointmentStatus` | `Boolean` | `false` | When true, allows updating an appointment that is already in a terminal status. Defaults to false. |
| `cancellationCategory` | `OnSiteJobsAppointmentCancellationCategory` | `null` | The cancellation category, if applicable. |
| `comments` | `String` |  | Optional comments about the appointment. |
| `commsStrategy` | `OnSiteJobsCommsStrategy` | `null` | The communication strategy to apply to this appointment. |
| `endAt` | `DateTime` |  | The new end datetime for the appointment. For open-ended appointments, set to None. |
| `jobNotes` | `JSONString` |  | Optional job notes as a JSON object. |
| `runActionsBasedOnStatus` | `Boolean` | `true` | Whether to run the side-effect action based on the new appointment status. Only applicable if a value was provided in the `status` field. Defaults to true. |
| `startAt` | `DateTime` |  | The new start datetime for the appointment. |
| `status` | `OnSiteJobsAppointmentStatus` | `null` | The new status for the appointment. |

## `OnSiteJobsUpdateRequestInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `assets` | `[OnSiteJobsAssetInput!]` |  | List of assets associated with the request. |
| `comment` | `String` |  | Comment for the request. |
| `requestId` | `UUID!` |  | The UUID of the OnSite Jobs request to update. |
| `status` | `OnSiteJobsRequestStatus` | `null` | Request status. |

## `OneOfMarketEnrollmentInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `electricitySupplyPointData` | `ElectricityEnrollmentMarketInput` | `null` | Electricity enrollment details. |
| `gasSupplyPointData` | `GasEnrollmentMarketInput` | `null` | Gas enrollment details. |
| `services` | `SimpleServicesEnrollmentMarketInput` | `null` | Simple Service enrollment details. |

## `OneOfTermInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `bespokerateconfiguration` | `BespokeRateConfigurationInput` | `null` | Input type for contract term. |
| `billduedate` | `BillDueDateInput` | `null` | Input type for contract term. |
| `billingdocumentissuancefrequency` | `BillingDocumentIssuanceFrequencyInput` | `null` | Input type for contract term. |
| `characteristicoverrideconfiguration` | `CharacteristicOverrideConfigurationInput` | `null` | Input type for contract term. |
| `collateralrequired` | `CollateralRequiredInput` | `null` | Input type for contract term. |
| `contractedvolumeconfiguration` | `ContractedVolumeConfigurationInput` | `null` | Input type for contract term. |
| `contractmetadata` | `ContractMetaDataInput` | `null` | Input type for contract term. |
| `delayerdays` | `DelayerDaysInput` | `null` | Input type for contract term. |
| `guaranteeoforiginconfiguration` | `GuaranteeOfOriginConfigurationInput` | `null` | Input type for contract term. |
| `latepaymentfees` | `LatePaymentFeesInput` | `null` | Input type for contract term. |
| `minimumcontractlength` | `MinimumContractLengthInput` | `null` | Input type for contract term. |
| `paysbydirectdebit` | `PaysByDirectDebitInput` | `null` | Input type for contract term. |
| `productrateoverrideconfiguration` | `ProductRateOverrideConfigurationInput` | `null` | Input type for contract term. |
| `promotionassignmentterm` | `PromotionAssignmentTermInput` | `null` | Input type for contract term. |
| `rategroupeligibilityconfiguration` | `RateGroupEligibilityConfigurationInput` | `null` | Input type for contract term. |
| `taxadjustmentconfiguration` | `TaxAdjustmentConfigurationInput` | `null` | Input type for contract term. |
| `terminationfee` | `TerminationFeeInput` | `null` | Input type for contract term. |
| `timeofuseoverride` | `TimeOfUseOverrideInput` | `null` | Input type for contract term. |

## `OpportunitiesQueryInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `assignedToAffiliateNumber` | `String` | `null` | Filter opportunities by assigned to affiliate number. |
| `assignedToTeam` | `String` | `null` | Filter opportunities by assigned to team. |
| `funnelCode` | `String` | `null` | Filter opportunities by funnel code. |
| `leadNumber` | `String` | `null` | Filter opportunities by lead number. |
| `productOfferingId` | `String` | `null` | Filter opportunities by product offering identifier. |
| `salesChannel` | `String` | `null` | Filter opportunities by sales channel. |
| `stageCode` | `String` | `null` | Filter opportunities by stage. |
| `supplyPointMarkets` | `[SupplyPointMarketNameEnum]` |  | Filter opportunities by supply point markets. |

## `OutcomeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `category` | `AppSessionOutcomeCategories!` |  | Outcome category. |
| `reason` | `String` | `""` | Optional reason for the outcome. |
| `type` | `AppSessionTypeChoices!` |  | Type of the app session. |

## `OwnerInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `ownerId` | `ID` |  | The ID of the owner. |
| `ownerType` | `PaymentInstructionOwnerTypeChoices` | `null` | The type of owner entity. |

## `PartyInput`

Input type for specifying a contract party, either an account or a business.

| Field | Type | Default | Description |
|---|---|---|---|
| `account` | `NonEmptyString` |  | The account number. |
| `business` | `Int` |  | The business identifier. |

## `PauseCollectionProcessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `number` | `String!` |  | Collection process number to pause. |
| `pauseLength` | `Int!` |  | Number of calendar days to pause collection process. |
| `pauseStartAt` | `DateTime!` |  | Start datetime for pause. |
| `reason` | `String!` |  | Reason for pausing collection process. |

## `PauseDunningInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number for which to pause the dunning process. |
| `note` | `String` |  | An optional note for the pause. |
| `pathName` | `String!` |  | The dunning process path name to pause. |
| `startDate` | `Date!` |  | The date from which the pause to take effect. |
| `stopDate` | `Date!` |  | The date at which the pause should stop. |

## `PaymentActionIntentOneOfInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `options` | `PaymentActionIntentOptionsInput` |  | Ad-hoc details of a payment action intent. |
| `token` | `String` |  | The token of an existing payment action intent. |

## `PaymentActionIntentOptionsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `targetIdentifier` | `String!` |  | The unique identifier for the target the payment should be associated with. |
| `targetType` | `PaymentActionIntentTargetType!` |  | The type of target the payment should be associated with. |

## `PaymentDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `actionIntent` | `PaymentActionIntentOneOfInput!` |  | The payment action intent details that identify the target for this payment. |
| `amount` | `Int!` |  | The payment amount in the minor unit of currency. |
| `customerReference` | `String!` |  | The description of the payment, as shown to the customer. |
| `paymentDate` | `Date!` |  | The date when the payment was made. |
| `paymentMethod` | `PaymentMethodInput!` |  | The details of the payment method used for this payment. |
| `reference` | `String!` |  | The reference used to uniquely identify this payment. |

## `PaymentMethodInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `type` | `String!` |  | The code of the payment method type used for this payment. |

## `PaymentScheduleDetailsInput`

Input type for payment schedule details. This enables us to collect information to create 4 different types of schedules during enrollment: - Payment on receipt of bill - Payment at a fixed day of the month once a receipt of bill has been issued - Payment when a ledger balance drops below a certain value - Payment at regular intervals for a fixed amount This is intended to be morally equivalent to a "union" input type.

| Field | Type | Default | Description |
|---|---|---|---|
| `balanceTriggered` | `BalanceTriggeredScheduleInput` |  |  |
| `billTriggered` | `BillTriggeredScheduleInput` |  |  |
| `billTriggeredBalanceTarget` | `BillTriggeredBalanceTargetScheduleInput` |  |  |
| `regularTriggered` | `RegularTriggeredScheduleInput` |  |  |

## `PaymentSlipDetailsInput`

Input type for payment slip details. This is used to set up a new payment instruction in the vendor's system as part of the enrollment process.

| Field | Type | Default | Description |
|---|---|---|---|
| `payerIsCustomer` | `Boolean!` |  | True if the customer also the payer. |

## `PayoutReferralForAccountInput`

Required information for paying out a referral for an account

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number of the referring/referred account. |
| `note` | `String` |  | Optional custom note to override the default display note and private note on the account credit. |
| `referralId` | `Int!` |  | The ID of the referral to payout. |

## `PaysByDirectDebitInput`

Input type for the PaysByDirectDebitTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `paysByDirectDebit` | `Boolean!` |  | Whether the account is paying by direct debit or not. |

## `PhotoInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `contentType` | `String!` |  | Content type of the photo. |
| `fileSize` | `Int!` |  | Size of the file in bytes. |
| `id` | `UUID!` |  | UUID for the photo. |
| `s3Bucket` | `String!` |  | S3 bucket where the photo is stored. |
| `s3Key` | `String!` |  | S3 key for the photo. |

## `PortfolioReferenceInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `namespace` | `String!` |  | The namespace of the portfolio reference. |
| `value` | `String!` |  | The value of the portfolio reference. |

## `PossibleErrorsInputType`

Information about the query/mutation for which one wants to know the possible errors.

| Field | Type | Default | Description |
|---|---|---|---|
| `authErrors` | `Boolean` |  | Whether to include possible authentication errors. |
| `name` | `String!` |  | Name of the query/mutation for which to get the possible errors. |
| `type` | `query_type!` |  | Type of the query (query or mutation). |

## `PostCreditInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `displayNote` | `String` |  | Optional short note about the credit, to be displayed to the user. |
| `ledgerNumber` | `String` |  | The number of the ledger where the credit will be posted. |
| `netAmount` | `Int!` |  | The net amount of the credit to be posted. Amount should be posted in the smallest unit of currency. |
| `note` | `String` |  | Optional short note about the credit, to be displayed to internal systems. |
| `reason` | `String!` |  | The reason why the credit is posted. This should be a valid credit reason code. |
| `taxAmount` | `Int!` |  | The tax amount of the credit to be posted. Amount should be posted in the smallest unit of currency. |

## `PostEventInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `description` | `String!` |  | Explanation or context for the event. |
| `eventId` | `String` |  | Unique identifier for this event from the external vendor, if provided. Used for deduplication so that requests can be safely retried without creating duplicate events. |
| `eventType` | `String!` |  | Type of post event (ie. 'delivered', 'returned', 'failed'). |
| `messageId` | `String!` |  | Unique ID of the message (ie. letter or document) that this post event relates to. |
| `timestamp` | `DateTime!` |  | The date/time that the post event occurred, if provided. |

## `PreferencesScheduleInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `dayOfWeek` | `DayOfWeek!` |  | The day of the week. |
| `max` | `Decimal!` |  | The maximum value. |
| `min` | `Decimal` |  | The minimum value. |
| `time` | `Time!` |  | Time of day this change should apply. Format: HH:MM. |

## `PrepareAccountInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountType` | `AccountTypeChoices` | `DOMESTIC` | The type of account to create. |
| `billingAddress` | `LifecycleAddressInput!` |  | The billing address. |
| `billingName` | `String!` |  | The billing name. |
| `brandCode` | `String!` |  | The brand of the created account. |
| `chosenPaymentDay` | `Int` |  | The chosen payment day. |
| `customerDetails` | `CustomerDetailsInput!` |  | The customer's details. |
| `dateOfSale` | `Date` |  | The date of sale, defaults to today if not provided. |
| `preferredSsd` | `Date` |  | The preferred supply start date. |
| `salesInfo` | `SalesInformationInput!` |  | Sales information. |
| `supplyPointInfoList` | `[PrepareAccountSupplyPointInput]` |  | Information of the supply points that the customer is intending to sign up for supply. |

## `PrepareAccountSupplyPointInput`

Input that can be provided to prepare account in order to identify previous accounts. This can be either the id of an actual supply point, or its market name and external_identifier. Only one of these should be provided. If both are present we give preference to the object id.

| Field | Type | Default | Description |
|---|---|---|---|
| `supplyPointId` | `ID` |  | The ID of the supply point to be enrolled. |
| `supplyPointInfo` | `SupplyPointInfoInput` |  | The details of the supply point to be enrolled. |

## `PriceForStreamInput`

Rate group prices for a product.

| Field | Type | Default | Description |
|---|---|---|---|
| `characteristicMapping` | `JSONString!` |  | The characteristic mapping for the price. |
| `price` | `Decimal!` |  | The price per unit. |
| `schemeLabels` | `JSONString` |  | The scheme labels for the price. |

## `ProductComponentForQuotingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `productCode` | `ID!` |  | Product code. |
| `quotingParams` | `[_QuotingParam]!` |  | Quoting parameter list for this product. |

## `ProductInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `code` | `String!` |  | The product code. |
| `monthlyEstimate` | `Int!` |  | The estimated cost per month in cents. |

## `ProductRateOverrideConfigurationInput`

Input type for the ProductRateOverrideConfigurationTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `indexationOptions` | `IndexationOptionsInput` | `null` | The indexation options for the product rate override configuration. |
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `schedules` | `[ProductRateOverrideScheduleInput]` | `null` | The schedules for the product rate override configuration. |

## `ProductRateOverrideItemBandInput`

Item input for Product Rate Override Configuration term by rate band.

| Field | Type | Default | Description |
|---|---|---|---|
| `band` | `String` |  | The rate band for the product rate override item. |
| `characteristicValues` | `[CharacteristicValueInput]` |  | The characteristic values for the product rate override item. |
| `rateSpecificationCode` | `String` |  | The rate specification code for the product rate override item. |
| `schemeLabels` | `[SchemeLabelInput]` |  | The scheme label mapping for the given rate override item. |

## `ProductRateOverrideItemInput`

Item input for Product Rate Override Configuration term.

| Field | Type | Default | Description |
|---|---|---|---|
| `pricePerUnit` | `Decimal` |  | The price per unit for the product rate override item. |
| `productCode` | `String` |  | The product code for the product rate override item. |
| `rate` | `ProductRateOverrideItemBandInput` | `null` | The rate band for the product rate override item. |

## `ProductRateOverrideScheduleInput`

Schedule for Product Rate Override Configuration term.

| Field | Type | Default | Description |
|---|---|---|---|
| `effectiveFrom` | `DateTime` |  | The effective from date for the product rate override schedule. |
| `items` | `[ProductRateOverrideItemInput]` | `null` | The items for the product rate override schedule. |

## `ProductToPurchaseInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `numberOfUnits` | `Int!` |  | Number of units. |
| `pricePerUnit` | `Int` |  | Price per unit in smallest sub-unit of the currency. Only used if the product accepts arbitrary prices. |
| `productCode` | `String!` |  | Products code to purchase. |

## `ProductToQuoteInput`

Represents a product and the quantity to quote for a customer.

| Field | Type | Default | Description |
|---|---|---|---|
| `currency` | `String!` |  | Currency. |
| `numberOfUnits` | `Int!` |  | Number of units. |
| `pricePerUnit` | `Int` |  | Price per unit in smallest sub-unit of the currency. |
| `productId` | `ID!` |  | ID of the product to quote. |

## `PromotionAssignmentScheduleInput`

Input type for defining a promotion assignment schedule.

| Field | Type | Default | Description |
|---|---|---|---|
| `discountTargets` | `JSONString!` |  | A mapping from discount codes to lists of targets. Each target is represented as {'target_type': {'domain': ..., 'type': ...}, 'identifier': ...}. |
| `promotionCode` | `String!` |  | The promotion code for this schedule. |

## `PromotionAssignmentTermInput`

Input type for the PromotionAssignmentTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `schedules` | `[PromotionAssignmentScheduleInput]!` |  | A list of promotion assignment schedules to be associated with the contract. |

## `PublishApprovalApprovedEventInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `approvalId` | `ID!` |  | The ID of the approval. |
| `approvedAt` | `DateTime!` |  | The datetime when the approval was approved. |
| `processType` | `String!` |  | The underlying process requiring an approval. |

## `PublishTransactionalMessagingExternalTriggerInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number of the recipient of this trigger. |
| `accountUserNumber` | `String` |  | Account user number of the recipient of this trigger. |
| `idempotencyKey` | `String` |  | An optional unique identifier for the trigger. If provided and there is an existing trigger with the same idempotency key, a new trigger will not be created. |
| `recipient` | `NonAccountRecipient` | `null` | The non-account recipient of this trigger. Cannot be used in combination with account_number or account_user_number. |
| `templateVariables` | `GenericScalar!` |  | The variables that will be passed through to message templates. |
| `triggerTypeCode` | `String!` |  | The code of the trigger type to be published. |

## `PublishTransactionalMessagingTriggerInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `params` | `JSONString!` |  | The params of the trigger type, as a JSON string. These are defined in the Params class for a trigger type. |
| `triggerTypeCode` | `String!` |  | The code of the trigger type to be published. |

## `PurchaseVoucherInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID!` |  | The account to purchase a voucher for. |
| `availableFrom` | `Date!` |  | When the voucher becomes available to be redeemed. |
| `chargeAmountInCents` | `Int` |  | How much to charge the account for in cents. Excludes tax. |
| `chargeAmountInCentsWithTax` | `Int` |  | How much to charge the account for in cents. Includes tax. |
| `clientParams` | `JSONString` | `"{}"` | Additional metadata from client sources to be stored against the voucher. This data is not structural and won't be relied on by Kraken internally. |
| `displayName` | `String!` |  | Display name for the voucher purchase. Maximum length is 255 characters. |
| `paymentId` | `ID` |  | The ID of the payment, if any. |
| `purchasedAt` | `DateTime!` |  | When the purchase was performed. |
| `transferChargeLedgerNumber` | `ID` |  | The ledger number of the ledger to transfer the charge to, if any. |
| `voucherType` | `String!` |  | The type of voucher. |
| `voucherValueInCents` | `Int!` |  | How much to credit the account for this voucher in cents. |

## `QueryComplexityInputType`

Information about the complexity of the query.

| Field | Type | Default | Description |
|---|---|---|---|
| `operationName` | `String` |  | The operation name of the query to calculate complexity for if more than one is provided. |
| `query` | `String!` |  | The query to calculate complexity for. |
| `variables` | `JSONString` |  | Any variables to include for the query. Pagination variables should be included as they will affect the overall weight of the query. |

## `QuoteShareInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | Account for which the quote was created. |
| `quoteCode` | `String!` |  | Quote code. |
| `recipient` | `Recipient!` |  | Recipient information. |

## `RateGroupEligibilityConfigurationInput`

Input type for the RateGroupEligibilityTerm. Callers must provide at least one schedule (schedules / timeSeriesSpecificationSchedules).

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `schedules` | `[RateGroupEligibilityScheduleInput]` |  | A list of rate group eligibility schedules to be associated with the contract. |
| `timeSeriesSpecificationSchedules` | `[TimeSeriesSpecificationEligibilityScheduleInput]` |  | A list of time series specification eligibility schedules to be associated with the contract. |

## `RateGroupEligibilityPeriodInput`

Input type representing a period with optional start and end dates.

| Field | Type | Default | Description |
|---|---|---|---|
| `end` | `DateTime` |  | The end date and time of the period. |
| `start` | `DateTime!` |  | The start date and time of the period. |

## `RateGroupEligibilityScheduleInput`

Input type for defining a rate group eligibility schedule. This input type is used to specify the details of a rate group eligibility schedule, including the associated product code, rate group code, eligibility status, and effective period.

| Field | Type | Default | Description |
|---|---|---|---|
| `effectivePeriod` | `RateGroupEligibilityPeriodInput!` |  | The period during which this eligibility is effective. |
| `isEligible` | `Boolean!` |  | Indicates if the rate group is eligible. |
| `productCode` | `String!` |  | The product code associated with the rate group. |
| `rateGroupCode` | `String!` |  | The rate group code. |

## `RateGroupPricesInput`

Rate group prices for a product.

| Field | Type | Default | Description |
|---|---|---|---|
| `prices` | `[PriceForStreamInput!]!` |  | The prices for the rate group. |
| `rateGroup` | `String!` |  | The rate group code. |

## `ReactivateCollectionProcessRecordInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `number` | `String!` |  | The Collection Process Record Number. |

## `Recipient`

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `String` |  | Email address of the recipient. |
| `familyName` | `String` |  | Family name of the recipient. |
| `givenName` | `String` |  | Given name of the recipient. |
| `mobile` | `String` |  | Mobile number of the recipient. |

## `RecordFailedPaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `noticePriority` | `NoticePriority!` |  | The priority with which this information needs to be resolved. |
| `payments` | `[FailedPaymentDetailsInput]!` |  | A list of payments that have failed. The list may contain at most 250 items. |

## `RecordPendingPaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `noticePriority` | `NoticePriority!` |  | The priority with which this information needs to be resolved. |
| `payments` | `[PaymentDetailsInput]!` |  | A list of payments that are pending. |

## `RecordSuccessfulPaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `noticePriority` | `NoticePriority!` |  | The priority with which this information needs to be resolved. |
| `payments` | `[SuccessfulPaymentDetailsInput]!` |  | A list of payments that have succeeded. The list may contain at most 250 items. |

## `RedeemLoyaltyPointsInput`

The input type for redeeming Loyalty Points.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `accountUserId` | `ID` |  | The account user id. |
| `points` | `Int!` |  | The number of Loyalty Points to redeem. |

## `RedeemReferralClaimCodeInput`

Required payload to redeem the benefit for partner reward referral scheme

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number for the referred account. |
| `code` | `String!` |  | Referral scheme claim code value. |

## `RefundPaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `ID!` |  | The account number. |
| `amountInMinorUnit` | `Int!` |  | The amount to be repaid. |
| `idempotencyKey` | `String!` |  | Unique constraint to prevent duplicate requests. |
| `paymentId` | `ID!` |  | The ID of the payment to refund. |
| `reason` | `String!` |  | Reason for refunding the payment. |

## `RegisterLeadFlowStatusEventInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `description` | `String` |  | A descriptive text about the flow event. |
| `flowId` | `String!` |  | The ID of the flow. |
| `leadNumber` | `String!` |  | The unique number of the lead. |
| `name` | `String!` |  | The name of the flow event. It will be the label to show. |
| `status` | `String!` |  | The status of the flow. |

## `RegisterOpportunityFlowStatusEventInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `description` | `String` |  | A descriptive text about the flow event. |
| `flowId` | `String!` |  | The ID of the flow. |
| `name` | `String!` |  | The name of the flow event. It will be the label to show. |
| `opportunityNumber` | `String!` |  | The unique number of the opportunity. |
| `status` | `String!` |  | The status of the flow. |

## `RegisterPushNotificationBindingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `bundleId` | `String!` |  | Register a push notification binding. A push notification binding connects an account user to a specific application running on a specific device through a 'registration token' (Android) or 'device token' (iOS). Using this binding we can send push notifications to the account user's devices. |
| `expiresAt` | `DateTime` |  | The time at which the push notification binding expires. |
| `service` | `String` |  | The push notification service the application is registered with. For iOS applications this will be 'APNS' and for Android applications this will be 'GCM'. For iOS Sandbox applications, the value is 'APNS_SANDBOX'. |
| `token` | `String!` |  | Device push notification token. |

## `RegularTriggeredScheduleInput`

A payment schedule which triggers a payment at regular intervals.

| Field | Type | Default | Description |
|---|---|---|---|
| `frequency` | `ScheduleFrequencyEnum` | `MONTHLY` | The based unit of frequency at which payments are to be taken. |
| `frequencyMultiplier` | `Int` | `1` | The multiple of the frequency at which payment are taken; should be between 1 and 11. |
| `paymentDay` | `Int` | `1` | The day of the month/week at which to take payment; allowed values: -28 to 28 (excl. 0) for 'MONTHLY', -7 to 7 (excl. 0) for 'WEEKLY'. Negative values count backwards from the end of the month/week. |

## `RemoveCampaignFromAccountInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `campaignName` | `String!` |  | The name of the campaign to be removed. |
| `expireAt` | `Date` |  | The expiry date of the campaign to be removed if prior to today's date. Defaults to today. |

## `RemoveCampaignItemsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `campaignId` | `String!` |  | The campaign ID. |
| `campaignItemIds` | `[String]!` |  | The IDs of the items to remove. |

## `RemovePropertyFromHierarchyInput`

Input for removing a property from a hierarchy.

| Field | Type | Default | Description |
|---|---|---|---|
| `hierarchyName` | `String` | `"default"` | The name of the hierarchy to remove the property from. |
| `propertyId` | `ID!` |  | The ID of the property to remove from the hierarchy. |

## `RepaymentInput`

Input fields for Repayment Intervention.

| Field | Type | Default | Description |
|---|---|---|---|
| `reason` | `String` |  | The Repayment Intervention reason. |
| `repaymentId` | `ID!` |  | The repayment ID. |

## `ReporterInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `category` | `OnSiteJobsReporterCategory!` |  | Reporter category. |
| `email` | `String` |  | Reporter email address. Must be blank if category='customer'. |
| `name` | `String` |  | Reporter name. Must be blank if category='customer'. |
| `phoneNumber` | `String` |  | Reporter phone number. Must be blank if category='customer'. |

## `RequestPasswordResetInput`

Input type for the RequestPasswordReset mutation.

| Field | Type | Default | Description |
|---|---|---|---|
| `baseUrl` | `String` |  | The URL from which the reset was requested. If supported, it is used as the base URL to generate the reset link in the email sent to the user. |
| `email` | `String` |  | The email requesting a password reset email. Provide either this or the userNumber. |
| `userNumber` | `String` |  | The number of the user requesting a password reset email. Provide either this or the email. |

## `RequestPrintedBillInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `billingDocumentId` | `ID!` |  | The ID of the billing document to request a printed bill for. |

## `RequestRepaymentInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number for the requested ledger's account. |
| `amountInMinorUnit` | `Int!` |  | The amount to be repaid. |
| `idempotencyKey` | `String!` |  | Unique constraint to prevent duplicate requests. |
| `instructionReference` | `String` |  | Optional. The instruction that should be used for transferring money to the customer. Note if specified, this will be preferred over the `method` input if both are given. |
| `ledgerNumber` | `String` |  | The ledger number from which the repayment will be requested. |
| `method` | `RequestableRepaymentMethod` | `null` | The method by which the money will be transferred to the customer. |
| `reason` | `String` |  | The reason for the repayment. |

## `ResetPasswordMutationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `clientMutationId` | `String` |  |  |
| `password` | `String!` |  |  |
| `token` | `String!` |  |  |
| `userId` | `String!` |  |  |

## `ResetUserPasswordInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `newPassword` | `String!` |  | The new password. |
| `token` | `String!` |  | The token from the presigned url. |
| `userId` | `String!` |  | A base64 bytestring representing the user's unique id. |

## `ResumeCollectionProcessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `number` | `String!` |  | Collection process number to resume. |
| `reason` | `String!` |  | Reason for resuming collection process. |

## `ReverseEnrollmentInput`

Input required to reverse an enrollment (Join Supplier process).

| Field | Type | Default | Description |
|---|---|---|---|
| `number` | `String!` |  | The identifier of the enrollment process to reverse. |
| `reversalReason` | `String` |  | The reason for the reversal. |

## `ReverseLeaveSupplierInput`

Input required to reverse a LeaveSupplier journey.

| Field | Type | Default | Description |
|---|---|---|---|
| `number` | `NonEmptyID` |  | The ID of the LeaveSupplier process to reverse. |
| `reversalReason` | `String` |  | The reason for the reversal. |

## `RevokeAgreementInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `agreementId` | `ID!` |  | The ID of the agreement to be revoked. |
| `reason` | `String` |  | The reason for revoking the agreement. |

## `RevokeContractInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `identifier` | `NonEmptyString!` |  | The unique identifier of the contract to revoke. |

## `RevokeUserAccessFromBusinessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `businessId` | `ID!` |  | The ID of the business that will revoke access. |
| `roleCode` | `String!` |  | The code of the role that will be revoked. |
| `userNumber` | `String!` |  | The number of the user that will lose access. |

## `RichAddressInput`

A postal address. This data model is based on the structure used by Google's [libaddressinput library](https://github.com/google/libaddressinput)&mdash;so you can use it, or other libraries that use its data model and reference data, to accept input. All fields can be blank, except for ``country`` which must always be supplied. This type is the input equivalent of `RichAddressType`; all the fields here are semantically equivalent to fields there, except where documented.

| Field | Type | Default | Description |
|---|---|---|---|
| `administrativeArea` | `String` |  | Top-level administrative subdivision, e.g. US state, AU state/territory, NZ region, IT region, JP prefecture. |
| `country` | `String` |  | ISO 3166-1 alpha-2 code of the country this address belongs to, e.g. `AU`, `GB`, `JP`, `NZ`. |
| `deliveryPointIdentifier` | `String` |  | Identifier used by the local postal service for this address, e.g. AU DPID, GB postcode + Delivery Point Suffix, US Zip-9 + Delivery Point. This is the value that gets encoded in the barcode printed on the envelope by large-volume bulk mail providers. |
| `dependentLocality` | `String` |  | UK dependent localities, or neighbourhoods or boroughs in some other locations. |
| `locality` | `String` |  | City or town portion of an address, e.g. US city, AU suburb/town, NZ suburb and city/town, IT comune, UK post town. |
| `name` | `String` |  | A personal name. |
| `organization` | `String` |  | The name of a business or organisation. |
| `postalCode` | `String` |  | Postal code (ZIP code in the US). |
| `sortingCode` | `String` |  | Sorting code, e.g. FR CEDEX code. This field is not used in many countries. |
| `streetAddress` | `String` |  | At most one of this field and `structured_street_address` can be supplied. This is a divergence from `RichAddressType.street_address`, where the field is always supplied; if `structured_street_address` is present, it's generated from that. |
| `structuredStreetAddress` | `GenericScalar` |  | At most one of this field and `street_address` can be supplied. ### `AU`: Australia The following keys may be present; all are optional. All keys have string values, and their meaning is the same as their aseXML counterparts. (Note that, unlike aseXML, all keys are provided at the top level, rather than being nested.) - `flat_or_unit_type` - `flat_or_unit_number` - `floor_or_level_type` - `floor_or_level_number` - `building_or_property_name` - `location_descriptor` - `lot_number` - `house_number_1` - `house_number_suffix_1` - `house_number_2` - `house_number_suffix_2` - `street_name` - `street_type` - `street_suffix` - `postal_delivery_type` - `postal_delivery_number_prefix` - `postal_delivery_number_value` - `postal_delivery_number_suffix` ### `JP`: Japan The following keys may be present; all are optional. If keys are empty, they may be omitted from the response entirely. - `chome` - `banchi` - `go` - `edaban` - `kana_building_name` - `kanji_building_name` - `building_number` - `room_number` - `address_code` - `physical_location_identifier` - `kana_company_name` - `kanji_company_name` ### `NZ`: New Zealand The following keys may be present; all are optional. If keys are empty, they may be omitted from the response entirely. - `flat_or_unit_type` - `flat_or_unit_number` - `floor_or_level_type` - `floor_or_level_number` - `property_name` - `building_name` - `house_number_1` - `house_number_suffix_1` - `house_number_2` - `house_number_suffix_2` - `street_prefix` - `street_name` - `street_type` - `street_suffix` - `rural_delivery_number` - `mailtown` - `postal_delivery_type` - `postal_delivery_location` - `postal_delivery_number_prefix` - `postal_delivery_number_value` - `postal_delivery_number_suffix` |

## `RiskListItemInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `identifierTypeName` | `String!` |  | The type of the risk identifier to be added or removed from the risk list. |
| `identifierValue` | `String!` |  | The value of the risk identifier to be added or removed from the risk list. |
| `validTo` | `DateTime` |  | The date and time until which the risk identifier is valid. If not provided, the risk identifier will be valid indefinitely. |

## `RunAgreementRolloverInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `agreementRolloverNumber` | `String!` |  | Number of the agreement rollover that is going to be executed. |

## `SalesDetailsInput`

Input type for specifying sales details.

| Field | Type | Default | Description |
|---|---|---|---|
| `salesRecord` | `SalesRecordInput!` |  | The sales record associated with the contract. |

## `SalesFunnelInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `funnelCode` | `String!` |  | The code of the funnel to get the schema for. |
| `includeDeprecatedFields` | `Boolean` | `false` | Whether to include deprecated fields in the schema. |

## `SalesFunnelsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `funnelType` | `FunnelTypeChoices!` |  | The type of the funnels to get the schema for. |
| `includeDeprecated` | `Boolean` | `false` | Whether to include deprecated fields in the schema. |

## `SalesInformationInput`

Information about the sale to associate with the account.

| Field | Type | Default | Description |
|---|---|---|---|
| `affiliateSessionId` | `String` |  | Optional ID of the affiliate session. |
| `offerGroupIdentifier` | `NonEmptyString` |  | Unique identifier for the offer group. |
| `organisationNumber` | `String` |  | Optional number of the affiliate organisation. |
| `referralCode` | `String` |  | The referral code used by the customer when signing up. |
| `salesChannel` | `String` |  | Sales channel. |
| `urn` | `String` |  | Unique reference number. |

## `SalesRecordInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `affiliateOrganisationName` | `String` |  | The name of the affiliate organisation associated with the sales record. |
| `opportunityNumber` | `String` |  | The opportunity code associated with the sales record. |
| `salesChannel` | `String` |  | The sales channel associated with the sales record. |

## `SchemeLabelInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `reference` | `String!` |  | The unique reference to the scheme. |
| `value` | `String!` |  | The value for the scheme. |

## `SearchCriteriaInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `id` | `ID` |  | The ID of the internal company to retrieve. |

## `SearchLeadFilters`

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `String` |  | The email address to be used for the lead. |
| `nationalId` | `String` |  | The national ID of the lead. |
| `telephone` | `String` |  | The telephone number to be used for the lead. |

## `SecurityDepositInput`

Input type for security deposit details. This is used to set up a security deposit as part of the enrollment process.

| Field | Type | Default | Description |
|---|---|---|---|
| `amount` | `Int!` |  | The amount of the security deposit. |
| `key` | `NonEmptyString!` |  | The idempotency key used to identify the security deposit. |
| `reason` | `NonEmptyString!` |  | The reason for the security deposit. |

## `SelectChargePointMakeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedOption` | `ID!` |  | The ID of the selected option from the list. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SelectChargePointVariantInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedOption` | `ID!` |  | The ID of the selected option from the list. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SelectDeviceTypeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedOption` | `ID!` |  | The ID of the selected option from the list. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SelectFromListInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedOption` | `ID!` |  | The ID of the selected option from the list. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SelectInverterMakeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedOption` | `ID!` |  | The ID of the selected option from the list. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SelectProductsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `partial` | `Boolean` |  | Whether the `selectedQuotedProductIds` only contain a subset of all quoted supply points for the given `quoteCode`. Defaults to `false`, i.e. `selectedQuotedProductIds` must contain a quoted product ID for every quoted supply point in the quote. |
| `quoteCode` | `String!` |  | Quote code. |
| `selectedQuotedProductIds` | `[ID]!` |  | IDs of the quoted products to be selected. |

## `SelectUserVehicleInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedOption` | `ID!` |  | The ID of the selected option from the list. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SelectVehicleMakeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedOption` | `ID!` |  | The ID of the selected option from the list. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SelectVehicleOrChargePointInput`

Options for selecting the user's vehicle or charge point.

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedIntegration` | `SelectIntegrationChoices` | `null` | User selected integration option. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SelectVehicleVariantInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `selectedOption` | `ID!` |  | The ID of the selected option from the list. |
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `SendVerificationEmailInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `String!` |  | The email address to be verified. |

## `SetLoyaltyPointsUserInput`

The input type for setting the Loyalty Points user.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `newLoyaltyPointsUserId` | `String!` |  | The account user receiving the points. |

## `SetOpportunityOutcomeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `opportunityNumber` | `ID` |  | The unique number of the opportunity. |
| `outcome` | `OpportunityOutcome` | `null` | The opportunity final outcome. |

## `SetPaymentPreferenceInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `fromDate` | `Date!` |  | The date from which this method is preferred. |
| `ledgerNumbers` | `[String]!` |  | The ledgers for which this is the preference. |
| `paymentMethod` | `String!` |  | The ID of the preferred payment method for automatic preferences. |

## `SetUpDirectDebitInstructionForBusinessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `bankDetails` | `BankDetailsInput!` |  | The details with which to set up the instruction (these will be sent to the vendor). |
| `businessId` | `ID!` |  | The business ID. |
| `validFrom` | `DateTime!` |  | The date-time that the instruction is valid from. |

## `SetUpDirectDebitInstructionFromStoredDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The number of the account. |
| `ledgerNumber` | `String!` |  | The number of the ledger on which the instruction should be created. |
| `owners` | `[OwnerInput]` |  | The owners of the financial account this instruction represents. |
| `storedPaymentMethodDetailsReference` | `String!` |  | Reference returned when storing bank details (StoredPaymentMethodDetails.reference). |
| `validFrom` | `DateTime!` |  | The date-time that the instruction is valid from. |

## `SetUpDirectDebitInstructionInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The number of the account. |
| `bankDetails` | `BankDetailsInput!` |  | The details with which to set up the instruction (these will be sent to the vendor). |
| `ledgerNumber` | `String` |  | The number of the ledger on which the instruction should be created. |
| `owners` | `[OwnerInput]` |  | The owners of the financial account this instruction represents. |
| `useForAutomatedPayments` | `Boolean` |  | Set newly created payment instruction as the active payment preference. |
| `validFrom` | `DateTime!` |  | The date-time that the instruction is valid from. |

## `ShareGoodsQuoteInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `email` | `String!` |  | The email to share the quote with. |
| `quoteCode` | `String!` |  | The quote to share. |

## `SimpleServicesAgreementTransferInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number to transfer agreements from. |
| `productCode` | `String!` |  | The product code for the agreement to be transferred. |

## `SimpleServicesEnrollmentMarketInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `externalIdentifier` | `String` |  | The market supply point identification number. |
| `marketDataSource` | `SimpleServicesMarketDataSourceInput` |  | The source of market data for the enrollment. |
| `requestedSupplyStartDate` | `Date!` |  | The requested supply start date for the enrollment. |

## `SimpleServicesMarketDataSourceInput`

Source of market data for Simple Services enrollment. Exactly one of the following must be provided: - quoted_supply_point_data: Use a pre-created QuotedSupplyPoint - product_catalog_data: Use product catalog characteristics - agreement_transfer_data: Transfer existing agreements from another account

| Field | Type | Default | Description |
|---|---|---|---|
| `agreementTransferData` | `SimpleServicesAgreementTransferInput` |  | Data for enrollment via agreement transfer. Callers must include an associated account number and product code. If the account spans multiple properties, the group header property identifies the target property. |
| `productCatalogData` | `SimpleServicesProductCatalogInput` |  | Data for enrollment using product catalog characteristics. |
| `quotedSupplyPointData` | `SimpleServicesQuotedSupplyPointInput` |  | Data for enrollment using a pre-created QuotedSupplyPoint. |

## `SimpleServicesProductCatalogInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `monthlyPaymentAmount` | `Int` |  | The monthly payment amount to set for a regular payment schedule. |
| `product` | `String!` |  | The code of the product to be enrolled. |
| `productCharacteristicsList` | `[CharacteristicValueInput]` |  | List of product characteristics for the selected product. |
| `ratesAgreedAt` | `DateTime` |  | The datetime when the rates of the product were agreed. This is usually the datetime corresponding to when the quote/offer was generated. |
| `supplyPointCharacteristicsList` | `[CharacteristicValueInput]` |  | List of supply point characteristics. |

## `SimpleServicesQuotedSupplyPointInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `quotedSupplyPointId` | `ID!` |  | The id of the QuotedSupplyPoint created for the supply point. |

## `SmartControlInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `action` | `SmartControlAction!` |  | The smart control action, i.e. suspend or unsuspend. |
| `deviceId` | `ID!` |  | The ID of the device. |

## `SmartFlexDevicePreferencesInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `deviceId` | `ID!` |  | The ID of the device. |
| `mode` | `PreferencesModeChoices!` |  | The mode of the schedule. |
| `schedules` | `[PreferencesScheduleInput]!` |  | The schedule with the preference details. |
| `unit` | `PreferencesUnitChoices!` |  | The unit of the min and max values in the preferences schedule. |

## `SolarSimulatorDirectSaleDirectSaleInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `cups` | `String` |  | CUPS of the direct sale as saved in Chipiron. |
| `dni` | `String` |  | DNI of the direct sale as saved in Chipiron. |
| `financedYears` | `Int` |  | Financed years of the direct sale as saved in Chipiron. Required if payment_type is 'financed'. |

## `SolarSimulatorDirectSaleInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `address` | `SolarSimulatorLeadAddressInput` | `null` | Address of the lead saved in chipiron. |
| `details` | `SolarSimulatorLeadDetailsInput` | `null` | Details of the lead saved in chipiron. |
| `directSale` | `SolarSimulatorDirectSaleDirectSaleInput` | `null` | Direct sale details saved in chipiron. |
| `email` | `String` |  | Email of the lead as saved in Chipiron. |
| `firstName` | `String` |  | Name of the lead as saved in Chipiron. |
| `lastName` | `String` |  | Surname of the lead as saved in Chipiron. |
| `phone` | `String` |  | Phone number of the lead as saved in Chipiron. |

## `SolarSimulatorLeadAddressInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `fullAddress` | `String` |  | Street of the lead as saved in Chipiron. |
| `houseType` | `String` |  | House type of the lead as saved in Chipiron. |

## `SolarSimulatorLeadDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `battery` | `String` |  | Battery of the lead as saved in Chipiron. |
| `consumption` | `Int` |  | Consumption of the lead as saved in Chipiron. |
| `numberOfPanels` | `Int` |  | Number of panels of the lead as saved in Chipiron. |
| `paymentType` | `String` |  | Payment type of the lead as saved in Chipiron. |
| `roofSize` | `Float` |  | Roof size of the lead as saved in Chipiron. |
| `solarWallet` | `String` |  | Solar wallet of the lead as saved in Chipiron. |
| `vehicleCharger` | `String` |  | Vehicle charger of the lead as saved in Chipiron. |

## `SolarSimulatorLeadInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `address` | `SolarSimulatorLeadAddressInput` | `null` | Address of the lead saved in chipiron. |
| `details` | `SolarSimulatorLeadDetailsInput` | `null` | Details of the lead saved in chipiron. |
| `email` | `String` |  | Email of the lead as saved in Chipiron. |
| `firstName` | `String` |  | Name of the lead as saved in Chipiron. |
| `lastName` | `String` |  | Surname of the lead as saved in Chipiron. |
| `phone` | `String` |  | Phone number of the lead as saved in Chipiron. |

## `StartCollectionProcessInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number for the collection process. |
| `billingDocumentIdentifier` | `String` |  | Identifier for billing document, required only for billing document level collection process. |
| `configCode` | `String!` |  | Collection process config code. |
| `ledgerNumber` | `String` |  | Ledger number, required only for ledger level collection process. |

## `StartCustomerVerificationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `brandCode` | `String!` |  | The code for the brand that transactional trigger will use. |
| `userNumber` | `String!` |  | The number of the user that needs verification. |
| `verificationType` | `CustomerVerificationType!` |  | The type of verification to start. |

## `StartReAuthenticationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number associated with the device. |
| `deviceId` | `String!` |  | The ID of the device to re-authenticate. |
| `propertyId` | `Int!` |  | The property where the device is located/charged. |

## `StartSmartFlexOnboardingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account to which the device should be registered. |
| `propertyId` | `Int!` |  | The property where the device is located/charged. |

## `StopAutomatedPaymentsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `fromDate` | `Date!` |  | The date from which automated payments should not be collected. |
| `ledgerNumbers` | `[String]!` |  | The ledgers for which this is the preference. |

## `StoreDirectDebitPaymentMethodDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `bankDetails` | `BankDetailsInput!` |  | The details with which to set up the instruction (these will be sent to the vendor). |
| `ledgerNumber` | `String` |  | The number of the ledger on which the instruction should be created. |

## `StorePaymentInstructionInput`

The input for storing a new payment instruction created through the embedded process.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `instructionType` | `PaymentType!` |  | The type of the new payment instruction. |
| `ledgerNumber` | `String` |  | **WARNING: Will be mandatory in future versions** The number of the ledger to which the instructions will be linked. |
| `useForAutomatedPayments` | `Boolean` |  | Set newly created payment instruction as the active payment preference. |
| `validFrom` | `DateTime` |  | The datetime from which the instruction is vaild. If not specified, defaults to the current datetime. |
| `vendorReference` | `String!` |  | The vendor's reference for this payment method. |

## `SuccessfulPaymentDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `actionIntent` | `PaymentActionIntentOneOfInput!` |  | The payment action intent details that identify the target for this payment. |
| `amount` | `Int!` |  | The payment amount in the minor unit of currency. |
| `customerReference` | `String!` |  | The description of the payment, as shown to the customer. |
| `paymentDate` | `Date!` |  | The date when the payment was made. |
| `paymentMethod` | `PaymentMethodInput!` |  | The details of the payment method used for this payment. |
| `reference` | `String!` |  | The reference used to uniquely identify this payment. |
| `succeededAt` | `DateTime!` |  | The datetime when the payment succeeded. |

## `SupplyPoint`

| Field | Type | Default | Description |
|---|---|---|---|
| `annualConsumption` | `Float` |  | Last year energy consumption. |
| `contractualMaxPower` | `[Decimal]` |  | List max power values per each period. |
| `cups` | `String` |  | Supply point CUD code. |
| `estimatedMonthlyFeeInCents` | `Int` |  | The estimated cost of energy/gas per month in eurocents. |
| `productId` | `Int` |  | Chosen product id. |
| `type` | `String` |  | Whether supply point is gas or electricity. |

## `SupplyPointIdentifierToMarketNameMappingInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `marketName` | `NonEmptyString!` |  | Name of the market (GBR_ELECTRICITY, AUS_ELECTRICITY, etc...). |
| `supplyPointExternalIdentifier` | `NonEmptyString!` |  | Supply point identifier (NMI, MPAN, MPRN, etc...). |

## `SupplyPointInfoInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `externalIdentifier` | `String!` |  | The supply points external identifier. |
| `marketName` | `String!` |  | The market of the supply point. |

## `SupplyPointTaxAdjustmentInput`

Input type for a supply point tax adjustment.

| Field | Type | Default | Description |
|---|---|---|---|
| `adjustmentType` | `String!` |  | The type of tax adjustment (e.g., EXEMPTION, REDUCTION). |
| `effectiveFrom` | `DateTime!` |  | When this adjustment becomes effective. |
| `effectiveTo` | `DateTime` |  | When this adjustment ends (null if open-ended). |
| `qualifyingUsage` | `Decimal!` |  | The proportion of usage that qualifies for the adjustment (0-1). |
| `supplyPointId` | `ID!` |  | The ID of the supply point. |
| `taxCategory` | `String!` |  | The tax category for this adjustment. |
| `taxSubcategory` | `String` |  | The tax subcategory for this adjustment. |

## `SwitchAccountToVariablePaymentScheduleInput`

Input type for switching an account to a variable payment schedule. Requires an `account_number` and `ledger_number` to be provided.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Number of the account for which to update the schedule. |
| `cancelConflictingSchedules` | `Boolean` | `false` | If true, any conflicting future payment schedules on the ledger will be deleted before creating the new variable schedule. |
| `ledgerNumber` | `String!` |  | Number of the ledger associated with the current payment schedule. |
| `note` | `String` |  | A note to be added to the payment schedule to explain the change. |
| `targetChangeDate` | `Date` |  | The date from which the variable payment schedule should start. Defaults to today. |

## `TaxAdjustmentConfigurationInput`

Input type for the TaxAdjustmentConfiguration term.

| Field | Type | Default | Description |
|---|---|---|---|
| `adjustments` | `[SupplyPointTaxAdjustmentInput]` |  | List of supply point tax adjustments. |
| `isVariable` | `Boolean` |  | Whether the term is variable. |

## `TelephoneLeadType`

| Field | Type | Default | Description |
|---|---|---|---|
| `partnerReference` | `String` |  | the partner reference. |
| `source` | `String` |  | the name of the partner sending the lead. |
| `telephoneLead` | `String` |  | the telephone lead. |

## `TerminateAgreementInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `agreementId` | `ID!` |  | The ID of the agreement to be terminated. |
| `reason` | `String` |  | The reason for terminating the agreement. |
| `terminateAt` | `DateTime!` |  | The date and time when the agreement should be terminated. |
| `terminatedAt` | `DateTime` |  | The datetime when the request to terminate was filed. Defaults to 'now'. |

## `TerminateContractInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `identifier` | `NonEmptyString!` |  | The unique identifier of the contract to terminate. |
| `validTo` | `DateTime!` |  | The day and time until the contract remains valid. Must not be beyond the current contract end date. |
| `waiveExitFee` | `Boolean` | `false` | Whether to waive any exit fees associated with the contract or not. |

## `TerminateCreditTransferPermissionInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `activeAt` | `DateTime` |  | Datetime when the credit transfer permission is valid. |
| `sourceLedgerNumber` | `String!` |  | Source ledger number of the credit transfer permission. |
| `targetLedgerNumber` | `String!` |  | Target ledger number of the credit transfer permission. |

## `TerminateSolarWalletRelationshipType`

| Field | Type | Default | Description |
|---|---|---|---|
| `sourceAccountNumber` | `String` |  | Source account number of the solar wallet ledger. |
| `targetAccountNumber` | `String` |  | Target account number of the electricity ledger. |
| `validTo` | `DateTime!` |  | Datetime when the solar wallet credit sharing ledger ends. |

## `TerminationFeeInput`

Input type for the TerminationFeeTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `amount` | `Decimal!` |  | The amount of the termination fee. |
| `feeType` | `NonEmptyString!` |  | The type of termination fee. |
| `isVariable` | `Boolean` |  | Whether the term is variable. |
| `marketName` | `NonEmptyString!` |  | The market associated with the termination fee. |

## `TimeOfUseOverrideInput`

Input type for the TimeOfUseOverrideTerm.

| Field | Type | Default | Description |
|---|---|---|---|
| `isVariable` | `Boolean` |  | Whether the term is variable. |

## `TimeSeriesEntryInput`

Input data to represent prices for particular moments and characteristics values.

| Field | Type | Default | Description |
|---|---|---|---|
| `params` | `JSONString` |  | All params that can be associated to the value. |
| `periodEnd` | `DateTime` |  | The value end of validity. |
| `periodStart` | `DateTime!` |  | The value start of validity. |
| `value` | `Decimal!` |  | The time series value. |
| `variant` | `VariantProfileInput` |  | All characteristics and schemes that can be associated to the value. |

## `TimeSeriesSpecificationEligibilityScheduleInput`

Input type for defining a time series specification eligibility schedule. This input type is used to specify the details of a time series specification eligibility schedule, including the associated product code, time series specification code, eligibility status, and effective period.

| Field | Type | Default | Description |
|---|---|---|---|
| `effectivePeriod` | `RateGroupEligibilityPeriodInput!` |  | The period during which this eligibility is effective. |
| `isEligible` | `Boolean!` |  | Indicates if the time series specification is eligible. |
| `productCode` | `String!` |  | The product code associated with the time series specification. |
| `timeSeriesSpecificationCode` | `String!` |  | The time series specification code. |

## `TransferLeadOpportunitiesInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `destinationLeadNumber` | `String!` |  | The number of the destination lead. |
| `sourceLeadNumber` | `String!` |  | The number of the source lead. |

## `TransferLedgerBalanceInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `amount` | `Int!` |  | The amount ( in lowest unit ) to transfer. If the amount is negative,the effect is reversed (the source ledger's balance increases and the destination ledger's balance decreases). |
| `note` | `String` |  | Optional short note about transfer reason. |
| `sourceAccountLedger` | `AccountLedgerInput!` |  | Account's ledger from which the requested amount is debited. |
| `targetAccountLedger` | `AccountLedgerInput!` |  | Account's ledger to which the requested amount is credited. |

## `TransferLoyaltyPointsBetweenUsersInput`

The input type for transferring Loyalty Points.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `points` | `Int!` |  | The number of Loyalty Points to transfer. |
| `receivingUserId` | `String!` |  | The account user receiving the points. |
| `sendingUserId` | `String` |  | The account user sending the points. If not provided, the current viewer will be used. |

## `TriggerCollectionProcessMessageInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `collectionProcessNumber` | `String!` |  | The unique number of the collection process. |
| `runAssessments` | `Boolean!` |  | Whether to run withdrawal and pause assessments just before sending. |
| `stepIdentifier` | `String!` |  | The identifier for the specific communication step. |

## `UnenrollAccountFromLoyaltyProgramInput`

The input type used to unenroll an account from the loyalty program.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number to enroll. |

## `UpdateAPIExceptionInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number associated with this exception. If none is provided, the field won't be updated. |
| `assignedUserId` | `Int` |  | The ID of the user assigned to handle this exception.If no user is provided, no user will be assigned to the exception. |
| `category` | `APIExceptionCategories` | `null` | The new category. If none is provided, the field won't be updated. |
| `context` | `JSONString` |  | The new context. If none is provided, the field won't be updated. This will completely replace the existing context by the new one. |
| `id` | `Int!` |  | The ID of the API Exception that will be updated. |
| `keyDate` | `Date` |  | The new key date. If none is provided, the field won't be updated. |
| `operationsTeamId` | `Int` |  | The ID of an operations team to handle this exception. If no team is provided, no team will be assigned to the exception. |
| `priority` | `APIExceptionPriority` | `null` | The new priority. If none is provided, the field won't be updated. |
| `resolutionStatus` | `APIExceptionResolutionStatus` | `null` | The new resolution status. If none is provided, the field won't be updated. |
| `resolutionType` | `APIExceptionResolutionType` | `null` | The new resolution type. If none is provided, the field won't be updated. |
| `tags` | `[APIExceptionTags]` |  | The updated list of tags. If none is provided, the field won't be updated. |

## `UpdateAPIExceptionNoteInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `apiExceptionNoteId` | `ID!` |  | The ID of the API Exception note being updated. |
| `body` | `String!` |  | The body of the note. |

## `UpdateAccountBillingAddressInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number to be updated. |
| `billingInfo` | `CreateBillingAddress` | `null` | Billing details. |

## `UpdateAccountBillingDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number to be updated. |
| `billingInfo` | `CreateBillingDetailsInput` | `null` | Billing details. |

## `UpdateAccountBillingEmailInput`

Input fields for updating billing email for an account.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number for account. |
| `billingEmail` | `String` |  | The billing_email which can be up to 512 characters. Use null to unset billing_email. |

## `UpdateAccountPaymentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number to be updated. |
| `address1` | `String` |  | Billing address line 1. |
| `address2` | `String` |  | Billing address line 2. |
| `address3` | `String` |  | Billing address line 3. |
| `city` | `String` |  | Billing address city. |
| `electricityIban` | `String` |  | Electricity payment instruction IBAN details. |
| `gasIban` | `String` |  | Gas payment instruction IBAN details. |
| `holderName` | `String` |  | The payment instruction holder's name. |
| `postcode` | `String` |  | Billing address postcode. |

## `UpdateAccountReferralStatusInput`

Required information for updating the status of an account referral

| Field | Type | Default | Description |
|---|---|---|---|
| `referralId` | `Int!` |  | The ID of the account referral to update. |
| `status` | `ReferralStatus!` |  | The new status for the account referral. Status can only move forward: Pending -> Paid or Cancelled. |

## `UpdateAccountUserCommsPreferencesInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `emailFormat` | `EmailFormats` |  |  |
| `fontSizeMultiplier` | `Float` |  |  |
| `isOptedInMeterReadingConfirmations` | `Boolean` |  |  |
| `isOptedInToClientMessages` | `Boolean` |  |  |
| `isOptedInToOfferMessages` | `Boolean` |  |  |
| `isOptedInToRecommendedMessages` | `Boolean` |  |  |
| `isOptedInToSmsMessages` | `Boolean` |  |  |
| `isOptedInToThirdPartyMessages` | `Boolean` |  |  |
| `isOptedInToUpdateMessages` | `Boolean` |  |  |
| `isUsingInvertedEmailColours` | `Boolean` |  |  |
| `preferredHoldMusic` | `Songs` |  |  |

## `UpdateAccountUserCommsPreferencesMutationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `clientMutationId` | `String` |  |  |
| `emailFormat` | `String` |  |  |
| `fontSizeMultiplier` | `Float` |  |  |
| `isOptedInMeterReadingConfirmations` | `Boolean` |  |  |
| `isOptedInToClientMessages` | `Boolean` |  |  |
| `isOptedInToOfferMessages` | `Boolean` |  |  |
| `isOptedInToRecommendedMessages` | `Boolean` |  |  |
| `isOptedInToSmsMessages` | `Boolean` |  |  |
| `isOptedInToThirdPartyMessages` | `Boolean` |  |  |
| `isOptedInToUpdateMessages` | `Boolean` |  |  |
| `isUsingInvertedEmailColours` | `Boolean` |  |  |
| `preferredHoldMusic` | `String` |  |  |

## `UpdateAccountUserInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `dateOfBirth` | `Date` |  |  |
| `details` | `[DetailsInputType]` |  | User details. |
| `email` | `String` |  |  |
| `familyName` | `String` |  |  |
| `firstFamilyName` | `String` |  | Customer's first family name. |
| `givenName` | `String` |  |  |
| `label` | `String` |  | A free text field to help identifying the customer (e.g. for a job title). |
| `landline` | `String` |  | Because this field is clearable, null and the empty string are treated differently; passing null or omitting the field leaves the value as-is, but explicitly passing an empty string clears this value. |
| `mobile` | `String` |  | Because this field is clearable, null and the empty string are treated differently; passing null or omitting the field leaves the value as-is, but explicitly passing an empty string clears this value. |
| `nif` | `String` |  | Customer's national ID number. |
| `pronouns` | `String` |  | How the user would like us to address them (e.g. 'she/her', 'they/them'). Because this field is clearable, null and the empty string are treated differently; passing null or omitting the field leaves the value as-is, but explicitly passing an empty string clears this value. |
| `secondFamilyName` | `String` |  | Customer's second family name. |
| `title` | `String` |  | The user's title. |
| `userId` | `String` |  | The user for whom to perform the update. This is only needed when using an Organisation role. |

## `UpdateAccountUserMutationInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `clientMutationId` | `String` |  |  |
| `dateOfBirth` | `Date` |  |  |
| `email` | `String` |  |  |
| `familyName` | `String` |  |  |
| `givenName` | `String` |  |  |
| `landline` | `String` |  |  |
| `mobile` | `String` |  |  |
| `pronouns` | `String` |  |  |

## `UpdateAffiliateLinkInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `contactEmail` | `String` |  | The contact email for the link. |
| `contactName` | `String` |  | The contact name for the link. |
| `isBusiness` | `Boolean` |  | Is this link for business customers. |
| `landingUrl` | `String` |  | The landing URL for the link. |
| `linkId` | `ID!` |  | The id of the affiliate link that is going to be edited. |
| `organisationId` | `ID` |  | The organisation for whom to update the affiliate link for. |
| `subdomain` | `String` |  | Will be validated as follows: - should be at least two characters - should only contain (letters, numbers, and Hyphen) - should not contain bad words - should not contain any of the reserved words including: affiliates, api, business, click, consul, developer, friends, kraken, mail, sendgrid, tech, webhooks, www, www2 |
| `trainingStatus` | `String` |  | The training status for the link. |

## `UpdateAffiliateOrganisationInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `allowAlternativePaymentMethods` | `Boolean` |  | Is this partner allowed to specify payment methods other than Direct Debit in the import csv or API. |
| `canRegisterBusinessMeterPoints` | `Boolean` |  | Are meter point registrations limited for profile classes 1 and 2 for registrations from csv or API. |
| `canRegisterCustomersWithoutEmailAddress` | `Boolean` |  | Allow registration requests with customers without an email address. |
| `canRegisterPortfolioAccounts` | `Boolean` |  | Allow registration requests with exiting account user emails to add to the portfolio belonging to the account user. |
| `canRenewTariffs` | `Boolean` |  | Allow performing tariff renewals via API. |
| `canUseIvrSupportApi` | `Boolean` |  | Allow this partner access to the IVR support API (modify their own IVR handling through third party 'IVR Flow Editor'). |
| `contactEmail` | `String` |  | The primary contact email for the organisation, used to send notifications about API usage such as authentication and permissions. |
| `defaultAccountType` | `AccountTypeChoices` | `null` | Default Account Type. |
| `isFieldSalesOnlyProduct` | `Boolean` |  | Restrict to field-sales-only products? This is only allowed for the 'field-sales' and 'events' sales channels. |
| `name` | `String` |  | The name of the organisation. |
| `organisationId` | `ID!` |  | The organisation that is going to be edited. |
| `salesChannelCode` | `String` | `null` | Sales Channel Code. |
| `skipMeterPointAddressValidation` | `Boolean` |  | Allow this partner to skip validation that ensures all meter points belong to the same address. |

## `UpdateAgentAuxiliaryStatusInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `auxiliaryStatus` | `String!` |  | The auxiliary status string. |
| `supportUserEmail` | `String!` |  | The email address of the support user. |

## `UpdateAgreementPeriodInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | A code that uniquely identifies the account. |
| `agreementId` | `ID!` |  | A code that uniquely identifies the agreement. |
| `reason` | `String` |  | The reason for the change. |
| `validFrom` | `Date!` |  | The start date of the agreement. |
| `validTo` | `Date` |  | The end date of the agreement (exclusive). The agreement will end on midnight of this date, such that the previous day is the last day covered by this agreement. |

## `UpdateAgreementRescissionInput`

Required information for updating an agreement rescission.

| Field | Type | Default | Description |
|---|---|---|---|
| `failureReason` | `String` |  | The reason for failure if the rescission failed. |
| `id` | `ID!` |  | The ID of the agreement rescission to update. |
| `status` | `AgreementRescissionStatus` |  | The new status for the agreement rescission. |
| `stepName` | `String` |  | The name of the current step in the rescission process. |
| `stepSlug` | `String` |  | The slug of the current step in the rescission process. |

## `UpdateAgreementRolloverInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `agreementRolloverNumber` | `String!` |  | Number of the agreement rollover that is going to be updated. |
| `expectedSendDate` | `Date` |  | The new expected send date for the agreement rollover. |
| `params` | `GenericScalar` |  | A JSON object containing additional parameters for the agreement rollover. Ensure it's properly encoded. |
| `renewProductCode` | `String` |  | The new product code for the agreement rollover. |
| `rolloverDate` | `Date` |  | The new rollover date for the agreement rollover. |
| `status` | `RolloverStatus` |  | The new status for the agreement rollover. |
| `suppressComms` | `Boolean` |  | Suppress Agreement Rollover communications. |
| `tags` | `[String]` |  | List of comma-separated tags to be set on the rollover. |

## `UpdateAutoTopUpAmountInput`

Input type for updating the schedule auto top up amount for for an account. Requires an `account_number`, `ledger_id` or `ledger_number`, and `payment_amount` to be provided.

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number to update the schedule auto top up amount for. |
| `ledgerNumber` | `String` |  | Specifies the ledger number associated with the current schedule for updates. |
| `paymentAmount` | `Int!` |  | The new auto-top-up amount for the payment schedule. |

## `UpdateBoostChargeInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `action` | `UpdateBoostChargeAction!` |  | The boost action. |
| `deviceId` | `String!` |  | Device ID. |

## `UpdateCollectionProcessRecordToActiveInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `externalReference` | `String` |  | The reference code for the active flow. |
| `externalSourceName` | `String` |  | External system name. |
| `number` | `String!` |  | The Collection Process Record Number. |

## `UpdateCollectionProcessRecordToCompleteInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `completionDetails` | `String` |  | The Completion details for the Collection Process. |
| `completionReason` | `CollectionProcessRecordCompletionTypeChoices` |  | The Completion reason for the Collection Process. |
| `number` | `String!` |  | The Collection Process Record Number. |

## `UpdateCommsDeliveryPreferenceInput`

Input fields for updating comms delivery preferences for an account

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  |  |
| `commsDeliveryPreference` | `CommsDeliveryPreference!` |  |  |

## `UpdateDCAProceedingInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `amount` | `Int` |  | Amount of debt. |
| `campaign` | `String` |  | The campaign. |
| `notes` | `String` |  | Notes for the commencement. |

## `UpdateDeviceGridExportInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `deviceId` | `String!` |  | Device ID. |
| `enabled` | `Boolean!` |  | Whether or not the device grid export is enabled. |

## `UpdateDocumentAccessibilityPreferenceInput`

Input fields for updating document accessibility preference for an account

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number for account. |
| `documentAccessibilityPreference` | `DocumentAccessibilityChoices` |  | Document accessibility preference option. Use null to reset to standard format. |

## `UpdateExtraDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `items` | `[ExtraDetailsItem]` |  | The keys and values to be updated. |
| `opportunityNumber` | `String!` |  | The unique number of the opportunity to update. |

## `UpdateIsChargingDurationCappedInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `deviceId` | `String!` |  | The ID of the device to update. |
| `enabled` | `Boolean!` |  | Whether to enable charging duration capping. |

## `UpdateLeadAssignmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `assignedToTeamName` | `String` |  | The name of th team the lead is assigned to. |
| `assignedToUsername` | `String` |  | The username of the user to assign the lead to. |
| `leadNumber` | `String!` |  | The unique number of the lead to update. |

## `UpdateLeadDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String` |  | The account number for the lead. |
| `billingAddress` | `RichAddressInput` |  | The billing address for the lead. |
| `extraDetails` | `[ExtraDetailsItem]` |  | The funnel fields for the lead. |
| `leadNumber` | `String!` |  | The unique number of the lead to update. |
| `nationalId` | `String` |  | The national ID for the lead. |

## `UpdateLeadStageInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `currentStage` | `NonEmptyString!` |  | The current stage of the lead to validate the transition. |
| `leadNumber` | `String!` |  | The unique number of the lead to update. |
| `stage` | `String!` |  | The stage that the lead should be updated to. |

## `UpdateLeaveSupplierInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `futureBillingAddress` | `RichAddressInput` | `null` | Future billing address. |
| `marketData` | `LeaveSupplierMarketInputType` | `null` |  |
| `number` | `NonEmptyID` |  | The number of the LeaveSupplier process to update. |
| `requestedSupplyEndDate` | `Date!` |  | The requested last day of supply. |
| `subtype` | `LeaveSupplierSubType` | `null` | The type of leave supplier process to initiate. |

## `UpdateMessageTagsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `messageRelayId` | `ID!` |  | The message to set the tags on. |
| `tagNames` | `[String!]!` |  | The tag names to set on the message. |
| `taggerCode` | `String!` |  | The tag code to set on the message. |
| `taggerVersion` | `String!` |  | The tag version to set on the message. |

## `UpdateNotesOnOpportunityInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `notes` | `String!` |  | The note to update on the opportunity. |
| `opportunityNumber` | `String!` |  | The unique number of the opportunity to update the notes for. |

## `UpdateOfferGroupOnOpportunityInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `offerGroupId` | `String!` |  | The identifier of the offer group for the opportunity. |
| `opportunityNumber` | `String!` |  | The unique number of the opportunity. |

## `UpdateOpportunityAssignmentInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `assignedToTeamName` | `String` |  | The name of th team the opportunity is assigned to. |
| `assignedToUsername` | `String` |  | The username of the user to assign the opportunity to. |
| `opportunityNumber` | `String!` |  | The unique number of the opportunity to update. |

## `UpdateOpportunityDetailsInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `addSupplyPoints` | `[LeadSupplyPoint]` |  | New supply points on the opportunity. |
| `address` | `RichAddressInput` |  | The new address for the opportunity. |
| `extraDetails` | `[ExtraDetailsItem]` |  | The funnel fields for the opportunity. |
| `opportunityNumber` | `String!` |  | The unique number of the opportunity to update. |
| `removeSupplyPoints` | `[LeadSupplyPoint]` |  | Remove supply points on the opportunity. |

## `UpdateOpportunityStageInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `currentStage` | `NonEmptyString!` |  | The current stage of the opportunity. |
| `opportunityNumber` | `String!` |  | The unique number of the opportunity to update. |
| `stage` | `String!` |  | The stage that the opportunity should be updated to. |

## `UpdatePasswordInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `newPassword` | `String!` |  | New password. |
| `newPasswordConfirmed` | `String!` |  | Confirm new password. |
| `oldPassword` | `String!` |  | Old password. |

## `UpdateProductPricesInput`

Rate group prices for a product.

| Field | Type | Default | Description |
|---|---|---|---|
| `periodEnd` | `DateTime` |  | The period for the price. |
| `periodStart` | `DateTime!` |  | The period for the price. |
| `prices` | `[RateGroupPricesInput!]!` |  | The rate group prices. |
| `product` | `String!` |  | The product code. |

## `UpdatePurchaseInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number. |
| `clientParams` | `JSONString` |  | A JSON object containing client parameters to store on the purchase. |
| `marketParams` | `JSONString` |  | A JSON object containing market parameters to store on the purchase. |
| `purchaseId` | `ID!` |  | The purchase ID. |
| `saleItems` | `[ProductToPurchaseInput]!` |  | Products being purchased. |

## `UpdateSiteworksRequestInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `id` | `UUID!` |  | ID of the request. |
| `status` | `RequestStatus!` |  | Request status. |

## `UpdateUserInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `dateOfBirth` | `Date` |  |  |
| `details` | `[DetailsInputType]` |  | User details. |
| `email` | `String` |  |  |
| `familyName` | `String` |  |  |
| `givenName` | `String` |  |  |
| `label` | `String` |  | A free text field to help identifying the customer (e.g. for a job title). |
| `landline` | `String` |  | Because this field is clearable, null and the empty string are treated differently; passing null or omitting the field leaves the value as-is, but explicitly passing an empty string clears this value. |
| `mobile` | `String` |  | Because this field is clearable, null and the empty string are treated differently; passing null or omitting the field leaves the value as-is, but explicitly passing an empty string clears this value. |
| `pronouns` | `String` |  | How the user would like us to address them (e.g. 'she/her', 'they/them'). Because this field is clearable, null and the empty string are treated differently; passing null or omitting the field leaves the value as-is, but explicitly passing an empty string clears this value. |
| `title` | `String` |  | The user's title. |
| `userId` | `String` |  | The user for whom to perform the update. This is only needed when using an Organisation role. |

## `UserInputRequiredInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `stepId` | `ID!` |  | The ID of the SmartFlex onboarding step to complete. |
| `userInputs` | `JSONString!` |  | A json object of user input key-value pairs where the key should match the key of the requested input. |
| `wizardId` | `ID!` |  | The ID of the SmartFlex onboarding wizard. |

## `UtilityFiltersInput`

Filter measurements by the given utility parameters.

| Field | Type | Default | Description |
|---|---|---|---|
| `electricityFilters` | `ElectricityFiltersInput` | `null` | Filter measurements by electricity parameters. |
| `gasFilters` | `GasFiltersInput` | `null` | Filter measurements by gas parameters. |

## `ValidateEmailInput`

Input required to validate email address via Kickbox

| Field | Type | Default | Description |
|---|---|---|---|
| `checkUniqueness` | `Boolean` | `false` | Check if an email is already in use. |
| `email` | `String!` |  | The user's email address. |

## `ValidateMfaDeviceInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `mfaMethod` | `MFAMethodChoices!` |  | MFA method. |
| `token` | `String!` |  | Token sent to the user via the MFA method. |

## `ValidatePhoneNumberInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `phoneNumber` | `String!` |  | The user's phone number. |

## `VariantProfileInput`

Object representing a variant profile.

| Field | Type | Default | Description |
|---|---|---|---|
| `characteristicValues` | `JSONString!` |  | The characteristic values for the variant. |
| `schemeLabels` | `JSONString` |  | The scheme labels for the variant. |

## `VaryContractTermsInput`

Input type for varying contract terms.

| Field | Type | Default | Description |
|---|---|---|---|
| `applicableAt` | `DateTime` |  | The date from which the varied terms will apply. |
| `identifier` | `NonEmptyString` |  | The unique identifier of the contract to vary. |
| `terms` | `[OneOfTermInput!]!` |  | The terms to be varied in the contract. |

## `VehicleChargingPreferencesInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number. |
| `targetType` | `String` |  |  |
| `weekdayTargetSoc` | `Int!` |  |  |
| `weekdayTargetTime` | `String!` |  |  |
| `weekendTargetSoc` | `Int!` |  |  |
| `weekendTargetTime` | `String!` |  |  |

## `VerifyCustomerInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `verificationCode` | `String!` |  | The verification code sent to the customer. |
| `verificationType` | `CustomerVerificationType!` |  | The type of verification to be checked. |

## `VerifyEmailInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `token` | `String!` |  | Token string that will be used to verify the email. |

## `VerifyIdentityInput`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The number of the account belonging to the user (e.g. A-12345678). |
| `firstLineOfAddress` | `String!` |  | The first line of the user's address (this could be the energy supply property address or the billing address on the account). |
| `fullName` | `String!` |  | The user's full name. |
| `postcode` | `String!` |  | The user's postcode (this could be the postcode of the energy supply property address or of the billing address on the account). |

## `WithdrawDunningInputType`

| Field | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | Account number for which to withdraw the dunning process. |
| `note` | `String` |  | An optional note for the withdraw. |
| `pathName` | `String!` |  | The dunning process path name to withdraw. |

## `_CreateOpportunityExtraDetailsItem`

| Field | Type | Default | Description |
|---|---|---|---|
| `key` | `String` |  | The key of the extra detail item. |
| `value` | `GenericScalar` |  | The value of the extra detail item. Can be a string or an integer. |

## `_DateTimeParam`

| Field | Type | Default | Description |
|---|---|---|---|
| `value` | `DateTime!` |  | Quoting parameter value. |

## `_FloatParam`

| Field | Type | Default | Description |
|---|---|---|---|
| `value` | `Float!` |  | Quoting parameter value. |

## `_IntegerParam`

| Field | Type | Default | Description |
|---|---|---|---|
| `value` | `Int!` |  | Quoting parameter value. |

## `_QuotingParam`

| Field | Type | Default | Description |
|---|---|---|---|
| `datetime` | `_DateTimeParam` |  | Quoting parameter value of type DateTime. |
| `integer` | `_IntegerParam` |  | Quoting parameter value of type Integer. |
| `name` | `String!` |  | Quoting parameter name. |
| `number` | `_FloatParam` |  | Quoting parameter value of type Float. |
| `string` | `_StringParam` |  | Quoting parameter value of type String. |

## `_StringParam`

| Field | Type | Default | Description |
|---|---|---|---|
| `value` | `String!` |  | Quoting parameter value. |

