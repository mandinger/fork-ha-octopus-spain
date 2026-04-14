# Mutations

Total `Mutation` operations: **314**

## `acceptGoodsQuote(input: AcceptGoodsQuoteInput!)`

- Return type: `AcceptGoodsQuote`
- Description: Accept a goods quote. The possible errors that can be raised are: - KT-CT-8223: Unauthorized. - KT-CT-8201: Received an invalid quoteId. - KT-CT-8224: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AcceptGoodsQuoteInput!` |  | Input fields for accepting a quote. |

## `acceptOfferForQuoting(input: AcceptOfferForQuotingInput!)`

- Return type: `AcceptOfferForQuoting`
- Description: Accept a quoting offer in an offer group. The possible errors that can be raised are: - KT-CT-12402: Unable to accept offer. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AcceptOfferForQuotingInput!` |  | Input fields for accepting a quoting offer. |

## `actualizeContract(input: ActualizeContractInput!)`

- Return type: `ActualizeContractOutput!`
- Description: Actualize a contract for an account or business. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10007: Unable to terminate contract. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10022: Contract already terminated. - KT-CT-10023: Contract is already revoked. - KT-CT-10024: Contract already expired. - KT-CT-10026: Contract actualization implies breach. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ActualizeContractInput!` |  |  |

## `addBusinessToSegment(input: AddBusinessToSegmentInput!)`

- Return type: `AddBusinessToSegmentMutation`
- Description: Add a business to a segment. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-11111: Segment does not exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddBusinessToSegmentInput!` |  | Input fields for adding a business to a segment. |

## `addCampaignToAccount(input: AddCampaignToAccountInput!)`

- Return type: `AddCampaignToAccount`
- Description: The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-7427: No campaign found with given slug. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddCampaignToAccountInput!` |  | Input variables needed for adding a campaign to an account. |

## `addChildToProperty(input: AddChildToPropertyInput!)`

- Return type: `AddChildToProperty`
- Description: Add a child property to a parent property in a hierarchy. If the child is already in the hierarchy with a different parent, it will be reparented. If the child is already a child of the specified parent, this operation is idempotent and does nothing. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-6622: Unauthorized. - KT-CT-6634: Unable to add child to property. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddChildToPropertyInput!` |  | Input fields for adding a child to a parent property. |

## `addItemsToRiskList(input: [RiskListItemInputType]!)`

- Return type: `AddItemsToRiskList`
- Description: Add items to the risk list. The possible errors that can be raised are: - KT-CT-12105: Risk list item addition failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `[RiskListItemInputType]!` |  | A list of risk list items to add. |

## `addNoteToInkConversation(input: AddNoteToInkConversationInput)`

- Return type: `AddNoteToInkConversation`
- Description: The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddNoteToInkConversationInput` |  |  |

## `addParentToProperty(input: AddParentToPropertyInput!)`

- Return type: `AddParentToProperty`
- Description: Add a parent property to a child property in a hierarchy. If the child is already in the hierarchy with a different parent, it will be reparented. If the child is already a child of the specified parent, this operation is idempotent and does nothing. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-6622: Unauthorized. - KT-CT-6635: Unable to add parent to property. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddParentToPropertyInput!` |  | Input fields for adding a parent to a child property. |

## `addPortfolioReference(input: AddPortfolioReferenceInput)`

- Return type: `AddPortfolioReference`
- Description: Mutation to add a reference to an existing portfolio. The possible errors that can be raised are: - KT-CT-9403: Received an invalid portfolioId. - KT-CT-9410: Conflicting portfolio reference. - KT-CT-9408: Invalid portfolio number format. - KT-CT-9409: Invalid portfolio reference. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddPortfolioReferenceInput` |  | Input fields for adding a reference to a portfolio. |

## `addProperty(input: AddPropertyInput!)`

- Return type: `AddProperty`
- Description: Add a property to an account. The possible errors that can be raised are: - KT-CT-6623: Unauthorized. - KT-CT-6629: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddPropertyInput!` |  | Input fields for adding a property to an account. |

## `addPropertyToHierarchy(input: AddPropertyToHierarchyInput!)`

- Return type: `AddPropertyToHierarchy`
- Description: Add a property to a hierarchy as a root node. If the property is already a root node in the hierarchy, this operation is idempotent. If the property is already in the hierarchy as a child, an error will be raised. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-6633: Property is already in the hierarchy as a child. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddPropertyToHierarchyInput!` |  | Input fields for adding a property to a hierarchy. |

## `addSignupReferralOnAccount(input: AddSignupReferralOnAccountInput!)`

- Return type: `AddSignupReferralOnAccount`
- Description: Add a one-way signup reward to a referral. The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6729: This scheme cannot be applied to given account. - KT-CT-6710: Unable to create referral. - KT-CT-6728: This referral scheme's usage is at capacity. - KT-CT-6712: Invalid reference. - KT-CT-6713: Referring and referred account brands do not match. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddSignupReferralOnAccountInput!` |  | Input fields for creating a signup reward for an organization. |

## `addStorylineToInkConversation(input: AddStorylineToInkConversationInput)`

- Return type: `AddStorylineToInkConversation`
- Description: The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-7651: Only one storyline entry can be marked as the root cause. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddStorylineToInkConversationInput` |  |  |

## `addUserToPortfolio(input: AddUserToPortfolioInput!)`

- Return type: `AddUserToPortfolio`
- Description: Add an user to a portfolio with a specified role. The possible errors that can be raised are: - KT-CT-5461: Invalid role code. - KT-CT-5462: Invalid user number format. - KT-CT-5463: Unauthorized. - KT-CT-9407: Unauthorized. - KT-CT-9408: Invalid portfolio number format. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AddUserToPortfolioInput!` |  | Input fields for adding a user to a portfolio. |

## `allowRepaymentSubmission(input: RepaymentInput!)`

- Return type: `AllowRepaymentSubmission`
- Description: Allow a repayment to be submitted. The possible errors that can be raised are: - KT-CT-3944: Account repayment does not exist. - KT-CT-3945: Unable to allow a repayment to be submitted. - KT-CT-3950: The provided reason text is too long. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RepaymentInput!` |  | Input variable needed for allowing repayment submission. |

## `amendPayment(input: AmendPaymentInput!)`

- Return type: `AmendPayment`
- Description: Amend an existing payment. The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-3970: The account cannot amend payments. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AmendPaymentInput!` |  | Input fields for amending an existing payment. |

## `approveRepayment(input: ApproveRepaymentInput!)`

- Return type: `ApproveRepayment`
- Description: Approve a repayment. The possible errors that can be raised are: - KT-CT-3934: Repayment request already approved. - KT-CT-3935: Repayment request cannot be paid. - KT-CT-3959: Unauthorized. - KT-CT-3973: Repayment request is not in a state to be approved. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ApproveRepaymentInput!` |  | Input fields for approving a repayment. |

## `assessCollectionProcessRecordForPause(input: AssessCollectionProcessRecordForPauseInputType!)`

- Return type: `AssessCollectionProcessRecordForPause`
- Description: Assess a collection process record for pause. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AssessCollectionProcessRecordForPauseInputType!` |  | Details of collection process to run the pause assessment. |

## `assignInkBucket(input: AssignInkBucketInput)`

- Return type: `AssignInkBucket`
- Description: The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-7613: The Ink bucket was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AssignInkBucketInput` |  |  |

## `assignSupplyPointToEstimationGroup(input: AssignSupplyPointToEstimationGroupInput!)`

- Return type: `AssignSupplyPointToEstimationGroup`
- Description: The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-13601: Estimation Group does not exist. - KT-CT-13602: Supply Point already has an Estimation Group. - KT-CT-13603: Supply Point does not exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AssignSupplyPointToEstimationGroupInput!` |  | Input fields for assigning a supply point to an estimation group. |

## `associateCallWithAccount(input: AssociateCallWithAccountInput!)`

- Return type: `AssociateCallWithAccount`
- Description: The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-4178: No account found with given account number. - KT-CT-11808: Unable to associate account to call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AssociateCallWithAccountInput!` |  |  |

## `associateItemToCollectionProcess(input: AssociateItemToCollectionProcessInputType!)`

- Return type: `AssociateItemToCollectionProcess`
- Description: Associate item to a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11205: Item already associated to collection process. - KT-CT-11216: Invalid extra_details for associated item type. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AssociateItemToCollectionProcessInputType!` |  | Input variables needed for associating an item to collection process. |

## `awardLoyaltyPoints(input: AwardLoyaltyPointsInput!)`

- Return type: `AwardLoyaltyPoints`
- Description: Award the passed number of Loyalty Points to the account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9202: Loyalty Points adapter not configured. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-9212: Points exceed maximum limit. - KT-CT-9219: Loyalty points user not found. - KT-CT-9221: Idempotency key already used on ledger entry. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AwardLoyaltyPointsInput!` |  | Input fields for awarding Loyalty Points. |

## `backendScreenEvent(input: BackendScreenEventInput!)`

- Return type: `BackendScreenEvent`
- Description: Look up an event to perform from its event_id, and return the next action to perform. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-8002: No event found. - KT-CT-8003: Event has no execute function. - KT-CT-8004: Error executing event in the backend. - KT-CT-8007: Incorrect or missing parameters for backend screen event. - KT-GB-9310: Account ineligible for joining Octoplus. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `BackendScreenEventInput!` |  | Input fields for performing a backend action. |

## `blockRepaymentSubmission(input: RepaymentInput!)`

- Return type: `BlockRepaymentSubmission`
- Description: Block a repayment from being submitted. The possible errors that can be raised are: - KT-CT-3944: Account repayment does not exist. - KT-CT-3946: Unable to block a repayment from being submitted. - KT-CT-3950: The provided reason text is too long. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RepaymentInput!` |  | Input variable needed for blocking repayment submission. |

## `cancelEnrollment(input: CancelEnrollmentInput!)`

- Return type: `EnrollmentCancelled!`
- Description: Cancel an enrollment for an account and a set of supply points. The possible errors that can be raised are: - KT-CT-10312: Mutation not enabled in this environment. - KT-CT-10318: Enrollment process not found. - KT-CT-10319: Enrollment process failed to cancel. - KT-CT-10320: Enrollment process not cancellable. - KT-CT-10321: Enrollment cancellation workflow not defined. - KT-CT-10323: Enrollment process failed to cancel. - KT-CT-10338: Enrollment process cannot be cancelled. - KT-CT-10331: Missing required process number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CancelEnrollmentInput!` |  |  |

## `cancelLeaveSupplier(input: CancelLeaveSupplierInput!)`

- Return type: `LeaveSupplierCancelled!`
- Description: Cancel a leave supplier process. The possible errors that can be raised are: - KT-CT-10304: Mutation not enabled in this environment. - KT-CT-10302: Invalid data. - KT-CT-10305: Failed to cancel leave supplier process - market actions are no longer cancellable. - KT-CT-10306: Failed to cancel leave supplier process - the cancellation workflow has not been configured. - KT-CT-10307: Failed to cancel leave supplier process - failed to cancel market actions. - KT-CT-10308: Failed to cancel leave supplier process. - KT-CT-10311: Failed to cancel leave supplier process. The process status is not in cancellable status. - KT-CT-1607: Value cannot be empty. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CancelLeaveSupplierInput!` |  |  |

## `cancelOnSiteJobsAppointment(input: CancelOnSiteJobsAppointmentInputType!)`

- Return type: `CancelOnSiteJobsAppointment`
- Description: Cancel an Appointment. The possible errors that can be raised are: - KT-CT-13001: Appointment does not exist. - KT-CT-13019: Vendor not found. - KT-CT-13017: Appointment cancellation not supported. - KT-CT-13053: Failed to cancel the appointment with the agent. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13043: Cannot update appointment as it has terminal status. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CancelOnSiteJobsAppointmentInputType!` |  | The input objects required to cancel an Appointment. |

## `cancelPayment(input: CancelPaymentInput!)`

- Return type: `CancelPayment`
- Description: Cancel an in-flight payment. The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-3954: Payment cancellation failed. - KT-CT-3955: Payment cannot be cancelled. - KT-CT-3956: Temporary error occurred. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CancelPaymentInput!` |  | Input fields for cancelling a pending payment. |

## `cancelRepaymentRequest(input: CancelRepaymentRequestInputType!)`

- Return type: `CancelRepaymentRequest`
- Description: Cancel a repayment or refund request. The possible errors that can be raised are: - KT-CT-4231: Unauthorized. - KT-CT-3930: The repayment or refund request does not exist. - KT-CT-3931: This repayment or refund request cannot be cancelled. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CancelRepaymentRequestInputType!` |  | Input fields for cancelling a repayment request. |

## `cancelSmartFlexOnboarding(input: CancelSmartFlexOnboardingInput!)`

- Return type: `CancelSmartFlexOnboarding`
- Description: Cancel onboarding of a device with SmartFlex. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CancelSmartFlexOnboardingInput!` |  |  |

## `checkCreditRisk(input: CheckCreditRiskInput!)`

- Return type: `CheckCreditRisk`
- Description: Check the credit risk for an account. The possible errors that can be raised are: - KT-CT-3921: Account not found. - KT-CT-5518: Account user not found. - KT-CT-5523: Invalid account or account user. - KT-ES-10701: Default property not found. - KT-ES-10702: Credit check only available for domestic accounts. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CheckCreditRiskInput!` |  |  |

## `closeDcaProceeding(input: CloseDCAProceedingInputType!)`

- Return type: `CloseDCAProceeding`
- Description: Close the DCA proceeding for an account. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11602: Could not find DCA with that name. - KT-CT-11603: Could not stop debt collection proceeding. - KT-CT-11604: Active debt collection proceeding does not exist for account. - KT-CT-11605: Multiple active Proceeding's found for same agency and campaign on account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CloseDCAProceedingInputType!` |  |  |

## `closeInkConversation(input: CloseInkConversationInput)`

- Return type: `CloseInkConversation`
- Description: The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CloseInkConversationInput` |  | Input for closing an Ink conversation. |

## `closeInkLiveChat(input: CloseInkLiveChaConversationtInput)`

- Return type: `CloseInkLiveChatConversation`
- Description: The possible errors that can be raised are: - KT-CT-7616: Not yet implemented. - KT-CT-7643: The Live Chat was not found. - KT-CT-7644: Ink Live Chat conversation not found. - KT-CT-7652: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CloseInkLiveChaConversationtInput` |  |  |

## `closeOpenPrintBatch`

- Return type: `CloseOpenPrintBatch!`
- Description: Close the Open Print Batch if any. The possible errors that can be raised are: - KT-CT-9010: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

## `collectDeposit(input: CollectDepositInput!)`

- Return type: `CollectDeposit`
- Description: Collect deposit for the given account. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-5711: No collection is required. - KT-CT-5712: Deposit agreement does not exist or has not been accepted. - KT-CT-5713: Payment instruction is not usable. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CollectDepositInput!` |  |  |

## `collectPayment(input: CollectPaymentInput!)`

- Return type: `CollectPayment`
- Description: Attempt to collect a one-off payment. If an instruction type is provided and there is an existing payment instruction, the payment can be collected immediately. A request to collect a payment at a future date can also be made, in which case the instruction input type is not necessary, but an instruction must exist at the specified collection date for the payment to be collected successfully. The possible errors that can be raised are: - KT-CT-3932: Invalid data. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CollectPaymentInput!` |  | Input fields for collecting a payment. |

## `commenceDcaProceeding(input: CommenceDCAProceedingInputType!)`

- Return type: `CommenceDCAProceeding`
- Description: Add commencement to an account. The possible errors that can be raised are: - KT-CT-11606: Debt Collection Agency cannot use campaign. - KT-CT-11601: Cannot start collection proceeding, proceeding for this account already exists. - KT-CT-11602: Could not find DCA with that name. - KT-CT-11607: Invalid ledger number for debt collection proceeding. - KT-CT-11608: Ledger does not belong to account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CommenceDCAProceedingInputType!` |  |  |

## `completeAuthFlowForSmartFlexOnboarding(input: CompleteAuthFlowInput!)`

- Return type: `CompleteAuthFlowForSmartFlexOnboarding`
- Description: Complete the authentication flow to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CompleteAuthFlowInput!` |  |  |

## `completeStandalonePayment(input: CompleteStandalonePaymentInput!)`

- Return type: `CompleteStandalonePayment`
- Description: Complete a standalone payment. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3823: Unauthorized. - KT-CT-3974: Unauthorized. - KT-CT-3975: Unable to complete standalone payment. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CompleteStandalonePaymentInput!` |  | Input fields for completing a standalone payment. |

## `completeTeslaSetupVirtualKeyForSmartFlexOnboarding(input: CompleteSmartFlexOnboardingStepInput!)`

- Return type: `CompleteTeslaSetupVirtualKeyForSmartFlexOnboarding`
- Description: Complete the Tesla virtual key setup onboarding step. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CompleteSmartFlexOnboardingStepInput!` |  |  |

## `completeUserActionForSmartFlexOnboarding(input: CompleteSmartFlexOnboardingStepInput!)`

- Return type: `CompleteUserActionRequiredForSmartFlexOnboarding`
- Description: Complete the user action required step to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CompleteSmartFlexOnboardingStepInput!` |  |  |

## `completeUserInputRequiredForSmartFlexOnboarding(input: UserInputRequiredInput!)`

- Return type: `CompleteUserInputRequiredForSmartFlexOnboarding`
- Description: Complete the user input required step to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UserInputRequiredInput!` |  |  |

## `confirmDoubleOptIn(input: ConfirmDoubleOptInInput)`

- Return type: `ConfirmDoubleOptIn`
- Description: Confirm a double opt in The possible errors that can be raised are: - KT-CT-9016: Consent management not enabled. - KT-CT-9020: Invalid consent expiring token. - KT-CT-9021: Consent expiring token not found. - KT-CT-9022: Consent for given token already accepted. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ConfirmDoubleOptInInput` |  |  |

## `connectAiAgentToCall(input: ConnectAiAgentToCallInput!)`

- Return type: `ConnectAiAgentToCall`
- Description: The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11815: Unable to connect a call to an AI agent. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ConnectAiAgentToCallInput!` |  |  |

## `createAccountCharge(input: CreateAccountChargeInput!)`

- Return type: `CreateAccountCharge`
- Description: Add charge to an account. The possible errors that can be raised are: - KT-CT-5211: The charge reason with the requested code is deprecated. - KT-CT-5212: The charge reason with the requested code does not exist. - KT-CT-5213: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAccountChargeInput!` |  | Input fields for creating an account charge. |

## `createAccountCredit(input: CreateAccountCreditInput!)`

- Return type: `CreateAccountCredit`
- Deprecated: Yes (The 'createAccountCredit' field is deprecated. Use postCredit mutation as it is ledger aware. - Marked as deprecated on 2022-07-04. - Scheduled for removal on or after 2026-03-30.)
- Description: Add credit to an account. The possible errors that can be raised are: - KT-CT-5315: Invalid data. - KT-CT-5314: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAccountCreditInput!` |  | Input fields for creating an account credit. |

## `createAccountFileAttachment(input: CreateAccountFileAttachmentInput!)`

- Return type: `CreateAccountFileAttachmentPayload!`

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAccountFileAttachmentInput!` |  |  |

## `createAccountNote(input: CreateAccountNoteInput!)`

- Return type: `CreateAccountNote`
- Description: Add a note to an account. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4180: Account note must be a valid string. - KT-CT-4196: Unpin at date provided is in the past. - KT-CT-4195: Unpin at date provided for an unpinned note. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAccountNoteInput!` |  | Input variables needed for adding a note to an account. |

## `createAccountPaymentSchedule(input: CreateAccountPaymentScheduleInput!)`

- Return type: `CreateAccountPaymentSchedule`
- Description: Replace an existing payment schedule with a new one that updates either the payment amount or payment day. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3815: No active payment schedule found for this account. - KT-CT-3822: Unauthorized. - KT-CT-3923: Unauthorized. - KT-CT-3941: Invalid data. - KT-CT-3942: An unexpected error occurred. - KT-CT-3947: An unexpected error occurred. - KT-CT-3960: Invalid value for payment day. - KT-CT-3961: Cannot update plan-associated payment schedule. - KT-CT-3962: No new value provided to update payment schedule. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAccountPaymentScheduleInput!` |  | Input fields for updating a payment schedule. |

## `createAccountReference(input: AccountReferenceInput!)`

- Return type: `CreateAccountReference`
- Description: Create an account reference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8311: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AccountReferenceInput!` |  | Input fields for creating an account reference. |

## `createAccountReminder(input: CreateAccountReminderInput!)`

- Return type: `CreateAccountReminder`
- Deprecated: Yes (The 'createAccountReminder' field is deprecated. This mutation rely on legacy reminder types. Please use the createReminder mutation which uses the new registry based reminder types instead. - Marked as deprecated on 2024-11-14. - Scheduled for removal on or after 2025-04-16.)
- Description: Create an account reminder. The possible errors that can be raised are: - KT-CT-1401: Invalid data. - KT-CT-1402: Unable to create account reminder. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAccountReminderInput!` |  | Input variables needed for creating an account reminder. |

## `createAffiliateLink(input: CreateAffiliateLinkInputType!)`

- Return type: `CreateAffiliateLink!`
- Description: Create an affiliate link for a new sales agent. The possible errors that can be raised are: - KT-CT-7711: Invalid data. - KT-CT-7713: Invalid data. - KT-CT-7714: Invalid data. - KT-CT-7715: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAffiliateLinkInputType!` |  | Input fields for creating an affiliate link for an organisation. |

## `createAffiliateOrganisation(input: CreateAffiliateOrganisationInputType!)`

- Return type: `CreateAffiliateOrganisation!`
- Description: Create an affiliate organisation. The possible errors that can be raised are: - KT-CT-7716: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAffiliateOrganisationInputType!` |  | Input fields for creating an affiliate organisation. |

## `createAffiliateSession(input: CreateAffiliateSessionInputType!)`

- Return type: `CreateAffiliateSession!`
- Description: Create a session for an affiliate link.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAffiliateSessionInputType!` |  | Input fields for creating a session for an affiliate link. |

## `createAgreement(input: CreateAgreementInput!)`

- Return type: `CreateAgreement`
- Description: Create a new agreement. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-4910: No product exists with the given input. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1509: Unable to create agreement. - KT-CT-1511: Cannot create overlapping agreement. - KT-CT-1512: Account type does not support agreements. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAgreementInput!` |  | Input fields for creating an agreement. |

## `createAgreementRollover(input: CreateAgreementRolloverInput!)`

- Return type: `CreateAgreementRollover`
- Description: Create an agreement rollover for a specific account and agreement. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-4910: No product exists with the given input. - KT-CT-4924: Unauthorized. - KT-CT-13701: An active agreement rollover already exists for this agreement. - KT-CT-13702: Expected send date cannot be in the past. - KT-CT-13703: Rollover date cannot be in the past. - KT-CT-13704: Unable to create agreement rollover. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAgreementRolloverInput!` |  | Create an agreement rollover for a specific account and agreement. |

## `createApiCall(input: CreateAPICallInput!)`

- Return type: `CreateAPICall`
- Description: Mutation to create a new APICall instance. The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAPICallInput!` |  | Input fields for creating an API call. |

## `createApiException(input: CreateAPIExceptionInput!)`

- Return type: `CreateAPIException`
- Description: Mutation to create a new APIException instance. The possible errors that can be raised are: - KT-CT-7801: Received an invalid operationsTeamId. - KT-CT-7802: The external identifier already exists. - KT-CT-7805: Too many tags associated with this API Exception. - KT-CT-7806: Cannot create duplicate tags for the same API exception. - KT-CT-7811: Received an invalid assignedUserId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAPIExceptionInput!` |  | Input fields for creating an API exception. |

## `createApiExceptionEvent(input: CreateAPIExceptionEventInput!)`

- Return type: `CreateAPIExceptionEvent`
- Description: Mutation to create a new APIExceptionEvent instance. The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAPIExceptionEventInput!` |  | Input fields for creating an API exception event. |

## `createApiExceptionNote(input: CreateAPIExceptionNoteInput!)`

- Return type: `CreateAPIExceptionNote`
- Description: Mutation to create a new APIExceptionNote instance. The possible errors that can be raised are: - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAPIExceptionNoteInput!` |  | Input fields for creating an API exception note. |

## `createAudioRecording(input: AudioRecordingInputType!)`

- Return type: `CreateAudioRecording!`
- Description: Create an audio recording for an affiliate session. The possible errors that can be raised are: - KT-CT-7720: Invalid S3 key format. - KT-CT-7721: Link not found. - KT-CT-7722: Invalid input for audio recording upload. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AudioRecordingInputType!` |  | Input fields required to create an audio recording. |

## `createBusiness(input: CreateBusinessInput!)`

- Return type: `CreateBusiness`
- Description: Create a business. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11108: Invalid data. - KT-CT-11109: Invalid data. - KT-CT-11110: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateBusinessInput!` |  | Input for creating a business. |

## `createCallMetadata(input: CallMetadataInput!)`

- Return type: `CreateCallMetadata`
- Description: The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11806: Call metadata item key cannot be an empty string. - KT-CT-11807: A call metadata item with this key already exists for this call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CallMetadataInput!` |  |  |

## `createCampaignItems(input: CreateCampaignItemsInput!)`

- Return type: `CreateCampaignItems`
- Description: The possible errors that can be raised are: - KT-CT-11501: Voice campaign not found. - KT-CT-4178: No account found with given account number. - KT-CT-11503: One or more campaign items are invalid and cannot be created. - KT-CT-11504: The batch of campaign items is too large. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateCampaignItemsInput!` |  |  |

## `createCollectionProcessEvent(input: CreateCollectionProcessEventInputType!)`

- Return type: `CreateCollectionProcessEvent`
- Description: Create an event for a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1605: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateCollectionProcessEventInputType!` |  | Input variables needed for creating a collection process event. |

## `createComplaint(complaint: CreateComplaintInputType!)`

- Return type: `CreateComplaint`
- Description: Create a complaint. The possible errors that can be raised are: - KT-CT-10801: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `complaint` | `CreateComplaintInputType!` |  |  |

## `createContract(input: CreateContractInput!)`

- Return type: `CreateContractOutput!`
- Description: Create and actualize a new contract for an account or business. The possible errors that can be raised are: - KT-CT-10001: Party is already under contract. - KT-CT-10006: Account not found. - KT-CT-10021: Business not found. - KT-CT-10018: The provided contract subject is invalid. - KT-CT-10019: Contract creation implies breach. - KT-CT-10020: The provided contract party payload is invalid. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateContractInput!` |  |  |

## `createContributionAgreement(input: CreateContributionAgreementInput!)`

- Return type: `CreateContributionAgreement`
- Description: Create a contribution agreement for an account. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-9601: Invalid data. - KT-CT-9602: Unable to create contribution agreement. - KT-CT-9605: Contribution amount cannot be 0 or negative. - KT-CT-9606: Scheme is not accepting contributions at this time. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateContributionAgreementInput!` |  | Input variables needed for creating a contribution agreement on an account. |

## `createCreditTransferPermission(input: CreateCreditTransferPermissionInput!)`

- Return type: `CreateCreditTransferPermission`
- Description: Create a credit transfer permission. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3827: The ledger is not valid. - KT-CT-3828: At least one of the provided ledgers must be a credit storage ledger. - KT-CT-3829: The credit transfer permission already exists. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateCreditTransferPermissionInput!` |  | Input fields to create a credit transfer permission. |

## `createCustomerFeedback(input: CreateCustomerFeedbackInputType!)`

- Return type: `CreateCustomerFeedback`
- Description: Create unsubmitted customer feedback object. The possible errors that can be raised are: - KT-CT-5516: Invalid data. - KT-CT-1111: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateCustomerFeedbackInputType!` |  |  |

## `createDepositAgreement(input: CreateDepositAgreementInput!)`

- Return type: `CreateDepositAgreement`
- Description: Create a new deposit agreement for the account if it needs one. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateDepositAgreementInput!` |  |  |

## `createEnergyAccount(input: CreateEnergyAccountInput)`

- Return type: `CreateEnergyAccount`
- Description: Create an account for either electricity or dual fuel. The possible errors that can be raised are: - KT-CT-4910: No product exists with the given input. - KT-CT-4911: Product not available. - KT-ES-4117: Invalid data. - KT-ES-4111: Supply point already exists. - KT-ES-4113: ATR not valid for contracting. - KT-ES-7701: The affiliate client failed to meet the requirements. - KT-ES-4121: Gas tariffs are not available. - KT-ES-4102: Account with multiple properties. - KT-ES-4122: Unable to create a referral. - KT-ES-4123: Nif not found. - KT-ES-4914: The received CUPS is invalid. - KT-ES-7819: The request to Chipiron to get SIPS data failed. - KT-ES-4917: The given supply point is not valid to contract. - KT-CT-7899: An internal error occurred. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateEnergyAccountInput` |  |  |

## `createExternalAccountEvent(input: CreateExternalAccountEventInput!)`

- Return type: `CreateExternalAccountEvent`
- Description: Create an external account event. The possible errors that can be raised are: - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateExternalAccountEventInput!` |  | Input fields for creating an external account event. |

## `createExternalAccountUserEvent(input: CreateExternalAccountUserEventInput!)`

- Return type: `CreateExternalAccountUserEvent`
- Description: Create an external account user event. The possible errors that can be raised are: - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateExternalAccountUserEventInput!` |  | Input fields for creating an external account event. |

## `createExternalMessage(input: CreateExternalMessageInput!)`

- Return type: `CreateExternalMessage`
- Description: Create an external message to record communications sent by external vendors. This allows you to import messages, such as emails, sent using other tools into Kraken. The possible errors that can be raised are: - KT-CT-14201: Vendor is empty. - KT-CT-14202: Vendor message ID is empty. - KT-CT-14203: Account number is empty. - KT-CT-14204: Message already exists. - KT-CT-14205: Unable to create the external message. - KT-CT-14206: An email body is missing. - KT-CT-14207: To email is empty. - KT-CT-14208: To email is not a valid email address. - KT-CT-14209: From email is empty. - KT-CT-14210: From email is an invalid format. - KT-CT-14211: A reply to email address is empty. - KT-CT-14212: A reply to email address is not a valid email address. - KT-CT-14213: The external messaging API is not enabled. - KT-CT-14214: An account number was provided, but no corresponding account could be found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateExternalMessageInput!` |  | Input variables needed for creating an external message. |

## `createFormSubmission(input: FormSubmissionInput!)`

- Return type: `FormSubmissionOuput`
- Description: Create a "form submission" entity. This is only meant to be used as a quick way of putting together a form and submit data for it, in the form of JSON - it is not expected that all form submissions will come through this path. This field requires the `Authorization` header to be set.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `FormSubmissionInput!` |  |  |

## `createGoodsPurchase(input: CreatePurchaseInput!)`

- Return type: `CreateGoodsPurchase`
- Description: Create a goods purchase. The possible errors that can be raised are: - KT-CT-8206: Invalid data. - KT-CT-1131: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreatePurchaseInput!` |  | Input fields for creating a purchase without a quote. |

## `createGoodsQuote(input: CreateGoodsQuoteInput!)`

- Return type: `CreateGoodsQuote`
- Description: Create a goods quote. The possible errors that can be raised are: - KT-CT-8202: Invalid data. - KT-CT-8205: Unable to create quote. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateGoodsQuoteInput!` |  | Input fields for creating a goods quote. |

## `createGoodsQuoteWithoutAccount(input: CreateGoodsQuoteWithoutAccountInput!)`

- Return type: `CreateGoodsQuoteWithoutAccount`
- Description: Create a goods quote without an account. The possible errors that can be raised are: - KT-CT-8202: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateGoodsQuoteWithoutAccountInput!` |  | Input fields for creating a goods quote without an existing account. |

## `createInboundCall(input: CreateInboundCallInput!)`

- Return type: `CreateInboundCall`
- Description: The possible errors that can be raised are: - KT-CT-11805: Invalid input for creating an inbound call. - KT-CT-11810: Caller is blocked. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateInboundCallInput!` |  |  |

## `createInkInboundMessage(input: CreateInkInboundMessageInput)`

- Return type: `CreateInkInboundMessage`
- Description: Register an Ink inbound message. The possible errors that can be raised are: - KT-CT-7622: Attachment bucket is invalid. - KT-CT-7623: Attachment path is invalid. - KT-CT-7621: Attachment not found. - KT-CT-7618: Unable to process message. - KT-CT-7625: Invalid email address. - KT-CT-7630: Message with this message ID has already been processed. - KT-CT-7632: The text content of the Ink Inbound Generic Message is too long. - KT-CT-7620: Channel not supported. - KT-CT-7627: The 'email' object is missing from the payload. - KT-CT-7628: The 'generic' object is missing from the payload. - KT-CT-7629: The 'post' object is missing from the payload. - KT-CT-7653: Account numbers on the message and message type must match if both are supplied. - KT-CT-7654: An account number was provided, but no corresponding account could be found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateInkInboundMessageInput` |  |  |

## `createInkLiveChatMessage(input: CreateInkLiveChatMessageInput)`

- Return type: `CreateInkLiveChatMessage`
- Description: The possible errors that can be raised are: - KT-CT-7616: Not yet implemented. - KT-CT-1111: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-7642: No account user was found for the given fromHandle. - KT-CT-7641: Live Chat message with this message ID has already been processed. - KT-CT-7645: The user is not authorized to access this Live Chat. - KT-CT-7622: Attachment bucket is invalid. - KT-CT-7623: Attachment path is invalid. - KT-CT-7621: Attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateInkLiveChatMessageInput` |  |  |

## `createLead(input: CreateLeadInput!)`

- Return type: `CreateLead`
- Description: Create a lead with the provided details. The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8930: Unable to parse address. - KT-CT-8928: The funnel is not active and cannot be used to create this entity. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8919: Funnel initial stage not set. - KT-CT-9017: Consent type not found. - KT-CT-8932: Lead contact details missing legal contact. - KT-CT-8934: Lead contact details missing communications contact. - KT-CT-8935: National ID bad input. - KT-CT-4121: Invalid phone number. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateLeadInput!` |  | Input fields for creating a lead. |

## `createMetadata(input: MetadataInput!)`

- Return type: `CreateMetadata`
- Description: Create metadata on an object. The possible errors that can be raised are: - KT-CT-8412: Invalid data. - KT-CT-8414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `MetadataInput!` |  | Input fields for creating metadata. |

## `createMfaDevice(input: CreateMfaDeviceInputType!)`

- Return type: `CreateMfaDevice`
- Description: Create MFA Device for user. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1151: MFA device not found. - KT-CT-1153: Unable to create MFA device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateMfaDeviceInputType!` |  | Input fields for creating a new multi-factor authentication device for the logged user. |

## `createNewAgreementFromProductSwitchProcess(input: CreateNewAgreementFromProductSwitchProcessInput!)`

- Return type: `CreateNewAgreementFromProductSwitchProcess`
- Description: Create a new agreement from an existing product switch process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4924: Unauthorized. - KT-CT-1509: Unable to create agreement. - KT-CT-1507: Agreement product switch date is not within the acceptable range. - KT-CT-1510: Product switch process not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateNewAgreementFromProductSwitchProcessInput!` |  | Validate the product switch flow data and creates a ProcessSwitchProcess model. |

## `createOfferGroupForQuoting(input: CreateOfferGroupForQuotingInput!)`

- Return type: `CreateOfferGroupForQuoting`
- Description: Create a quoting Offer Group. The possible errors that can be raised are: - KT-CT-12401: Unable to create offer group. - KT-CT-12405: Missing rates for quoting. - KT-CT-12406: Product not configured correctly for quoting. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateOfferGroupForQuotingInput!` |  | Input fields for creating an offer group from a list of offers. |

## `createOnSiteJobsAppointment(appointmentBookingSessionId: UUID!, slotId: UUID!)`

- Return type: `CreateOnSiteJobsAppointment`
- Description: Create an Appointment. The possible errors that can be raised are: - KT-CT-13030: Booking session not found. - KT-CT-13025: Booking session has expired. - KT-CT-13033: Slot not found. - KT-CT-13028: Agent not found. - KT-CT-13019: Vendor not found. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13035: Request is inactive. - KT-CT-13032: Request does not exist. - KT-CT-13036: Booking service currently unavailable. - KT-CT-13037: Appointment reference not provided by booking service. - KT-CT-13031: Timeslot is no longer available. - KT-CT-13027: Booking system error occurred. - KT-CT-13056: Appointment cannot be rescheduled. - KT-CT-13044: Failed to update appointment slot. - KT-CT-13001: Appointment does not exist. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13006: No properties found for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `appointmentBookingSessionId` | `UUID!` |  | The appointment booking session ID to create an appointment. |
| `slotId` | `UUID!` |  | The slot ID to book the appointment for. |

## `createOnSiteJobsAppointmentWithDate(appointmentBookingDetails: OnSiteJobsAppointmentBookingDetailsInput!, deadlineDate: Date, overrideAppointmentCheckWarnings: Boolean = false, preferredDate: Date!, requestId: UUID!)`

- Return type: `CreateOnSiteJobsAppointmentWithDate`
- Description: Create an Appointment using DATE booking mode. Used when the booking flow does not require selecting a specific timeslot. The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13020: Could not identify agent from property. - KT-CT-13021: Invalid job type. - KT-CT-13022: Work category not found for job type. - KT-CT-13057: Date booking mode is not applicable for this request. - KT-CT-13023: Appointment booking checks failed. - KT-CT-13024: Appointment booking checks returned warnings. - KT-CT-13028: Agent not found. - KT-CT-13019: Vendor not found. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13035: Request is inactive. - KT-CT-13036: Booking service currently unavailable. - KT-CT-13037: Appointment reference not provided by booking service. - KT-CT-13027: Booking system error occurred. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-13006: No properties found for the given supply points. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `appointmentBookingDetails` | `OnSiteJobsAppointmentBookingDetailsInput!` |  | The appointment booking details. |
| `deadlineDate` | `Date` |  | The deadline date for the appointment. |
| `overrideAppointmentCheckWarnings` | `Boolean` | `false` | Whether to override appointment booking check warnings. Defaults to False. |
| `preferredDate` | `Date!` |  | The preferred date for the appointment. |
| `requestId` | `UUID!` |  | The ID of the request to book an appointment for. |

## `createOnSiteJobsAppointmentWithoutBooking(input: OnSiteJobsCreateAppointmentInput!)`

- Return type: `CreateOnSiteJobsAppointmentWithoutBooking`
- Description: Create an Appointment on Kraken without making a booking via the booking vendor system. This is typically used by booking vendors to inform Kraken about appointments created on their system. The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13035: Request is inactive. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13034: Appointment already exists for this request. - KT-CT-13021: Invalid job type. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13039: Cancellation fields require CANCELLED status. - KT-CT-13027: Booking system error occurred. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13062: Datetime field must be timezone-aware. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `OnSiteJobsCreateAppointmentInput!` |  | The input objects required to create an Appointment on Kraken without making a booking. |

## `createOnSiteJobsRequest(input: CreateOnSiteJobsRequestInputType!)`

- Return type: `CreateOnSiteJobsRequest`
- Description: Create a Request. The possible errors that can be raised are: - KT-CT-13002: Supply point not found. - KT-CT-13003: Supply points must belong to the same account. - KT-CT-13004: No account found for the given supply points. - KT-CT-13006: No properties found for the given supply points. - KT-CT-13028: Agent not found. - KT-CT-13010: No booking adapter found for agent. - KT-CT-13007: At least one of the request checks failed. - KT-CT-13008: At least one of the request checks has warnings. - KT-CT-13009: On site jobs Request already exists. - KT-CT-13012: Viewer is not allowed to create a request. - KT-CT-13013: Reporter post init error. - KT-CT-13014: Request reason is not supported. - KT-CT-13015: Request sub_reason is not supported. - KT-CT-13041: User is not allowed to override request/appointment checks. - KT-CT-13042: Multiple supply points not supported by this booking adapter. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13047: Multiple supply points found. - KT-CT-13048: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_ids. - KT-CT-13049: Neither supply_point_identifier_to_market_name_mapping nor supply_point_internal_ids provided. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13058: Reason approval details are required when the reason requires approval. - KT-CT-13059: Emergency approval details are required when the emergency requires approval. - KT-CT-13060: Reason approval details should not be provided when the reason does not require approval. - KT-CT-13061: Emergency approval details should not be provided when the emergency does not require approval. - KT-CT-13063: Failed to derive property for the given supply points. - KT-CT-13064: Provided supply point(s) not supported by the On-Site Jobs market manager. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateOnSiteJobsRequestInputType!` |  | The input objects required to create a Request. |

## `createOpportunityAndLead(input: CreateOpportunityAndLeadInput!)`

- Return type: `CreateOpportunityAndLead`
- Description: Create an opportunity and lead with the provided details. The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8919: Funnel initial stage not set. - KT-CT-8930: Unable to parse address. - KT-CT-8907: Lead not found. - KT-CT-8901: Unable to create lead. - KT-CT-8902: Unable to create lead. - KT-CT-8935: National ID bad input. - KT-CT-4121: Invalid phone number. - KT-CT-8931: Extra detail value is invalid. - KT-CT-9017: Consent type not found. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-8936: Only one address is required to create an opportunity. - KT-CT-8937: One or more Supply Points cannot be validated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateOpportunityAndLeadInput!` |  | Input fields for creating an opportunity. |

## `createOpportunityFileAttachment(input: CreateOpportunityFileAttachmentInput!)`

- Return type: `CreateOpportunityFileAttachment`
- Description: Creates an Opportunity File Attachment.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateOpportunityFileAttachmentInput!` |  | Input to create an Opportunity File Attachment. |

## `createOpportunityForLead(input: CreateOpportunityForLeadInput!)`

- Return type: `CreateOpportunityForLead`
- Description: Create an opportunity for a lead with the provided details. The possible errors that can be raised are: - KT-CT-8912: Funnel not found. - KT-CT-8919: Funnel initial stage not set. - KT-CT-8907: Lead not found. - KT-CT-8913: Organisation is not valid to be assigned. - KT-CT-8924: Unable to create opportunity. - KT-CT-8925: Unable to create opportunity. - KT-CT-8926: Unable to create opportunity. - KT-CT-8928: The funnel is not active and cannot be used to create this entity. - KT-CT-8930: Unable to parse address. - KT-CT-8936: Only one address is required to create an opportunity. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8937: One or more Supply Points cannot be validated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateOpportunityForLeadInput!` |  | Input fields for creating an opportunity for a lead. |

## `createOrUpdateLoyaltyCard(input: CreateOrUpdateLoyaltyCardInput!)`

- Return type: `CreateOrUpdateLoyaltyCardMutation`
- Description: Create or update a loyalty card for the given account user. The possible errors that can be raised are: - KT-CT-5412: No account user exists with the given id. - KT-CT-8610: Invalid data. - KT-CT-8611: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateOrUpdateLoyaltyCardInput!` |  | Input fields for creating or updating a loyalty card. |

## `createOrUpdateTimeSeriesEntries(input: CreateOrUpdateTimeSeriesEntriesInput!)`

- Return type: `CreateOrUpdateTimeSeriesEntries!`
- Description: Create or update time series entries. The possible errors that can be raised are: - KT-CT-12014: Time series not found. - KT-CT-12015: Characteristics mismatch. - KT-CT-12016: Conflicting time series entries. - KT-CT-12017: Invalid time series entries period. - KT-CT-12038: Invalid time series entries granularity. - KT-CT-12040: Time series entries in use. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateOrUpdateTimeSeriesEntriesInput!` |  | The time series input for time series entry creation or update. |

## `createPaymentActionIntent(input: CreatePaymentActionIntentInput!)`

- Return type: `CreatePaymentActionIntent`
- Description: Create a new payment action intent. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3980: Invalid ledger identifier. - KT-CT-3981: Unauthorized. - KT-CT-3982: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreatePaymentActionIntentInput!` |  | Input fields for creating a payment action intent. |

## `createPortfolio(input: CreatePortfolioInput)`

- Return type: `CreatePortfolio`
- Description: Mutation to create a new Portfolio instance. The possible errors that can be raised are: - KT-CT-9402: Received an invalid brandCode. - KT-CT-9401: Received an invalid operationsTeamId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreatePortfolioInput` |  | Input fields for creating a portfolio. |

## `createPortfolioUserRole(input: CreatePortfolioUserRoleInput)`

- Return type: `CreatePortfolioUserRole`
- Description: Mutation to create a new portfolio user role. This will effectively link the user to the portfolio giving them all the permissions enabled for the specific role. The possible errors that can be raised are: - KT-CT-9403: Received an invalid portfolioId. - KT-CT-9404: Received an invalid accountUserId. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreatePortfolioUserRoleInput` |  | Input fields for connecting a user to a portfolio. |

## `createPostEvents(input: CreatePostEventsInput!)`

- Return type: `CreatePostEvents`
- Description: Create post delivery events from external vendors. The possible errors that can be raised are: - KT-CT-9907: Post events batch size exceeded. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreatePostEventsInput!` |  | Batch of post events to create. |

## `createProduct(input: CreateProductInput!)`

- Return type: `CreateProductOutput!`
- Description: Create a new product. The possible errors that can be raised are: - KT-CT-12003: Specified product brand does not exist. - KT-CT-12004: Invalid product tag type. - KT-CT-12005: A selection of a terms and conditions type does not exist. - KT-CT-12006: Provided product characteristic overrides are not in the correct format. - KT-CT-12007: Unable to create product. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateProductInput!` |  |  |

## `createQuote(input: CreateQuoteInput!)`

- Return type: `CreateQuote`
- Description: Create a quote for the provided CUPS Or Estimation. The possible errors that can be raised are: - KT-CT-4639: Unable to quote for the provided market identifier. - KT-CT-1501: Agreement not found. - KT-CT-4131: Invalid brand. - KT-CT-7719: Session not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateQuoteInput!` |  | Input for creating a quote. |

## `createQuoteForAccount(input: CreateQuoteForAccountInput!)`

- Return type: `CreateQuoteForAccount`
- Description: Create a quote for switching product. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided. - KT-CT-4616: Unable to create a quote. - KT-CT-4631: Unable to quote for the chosen market. - KT-CT-4645: No supply point found belonging to the account for the provided identifier. - KT-CT-4924: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateQuoteForAccountInput!` |  |  |

## `createQuoteForProducts(input: CreateQuoteForProductsInput!)`

- Return type: `QuoteRequest`
- Description: Create a quote. The possible errors that can be raised are: - KT-CT-4616: Unable to create a quote. - KT-ES-4601: Invalid product codes. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateQuoteForProductsInput!` |  |  |

## `createReferral(input: CreateReferralInput!)`

- Return type: `CreateReferral`
- Description: Create an account referral using an email address, personal link or code.This is for customers to refer other customers so it only works with friend referrals and not partner referrals. The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6710: Unable to create referral. - KT-CT-6711: Accounts may not self-refer. - KT-CT-6713: Referring and referred account brands do not match. - KT-CT-6712: Invalid reference. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateReferralInput!` |  | Input fields for creating a referral. |

## `createReminder(input: CreateReminderInput!)`

- Return type: `CreateReminder`
- Description: Create an account reminder. The possible errors that can be raised are: - KT-CT-1401: Invalid data. - KT-CT-1402: Unable to create account reminder. - KT-CT-1403: Missing user or team assignee. - KT-CT-1404: This reminder type is deprecated. - KT-CT-1405: Both user and team assignee provided. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateReminderInput!` |  | Input variables needed for creating an account reminder. |

## `createScheduledTransactions(input: [CreateScheduledTransactionsInput]!)`

- Return type: `CreateScheduledTransactions`
- Description: Create scheduled transactions. The possible errors that can be raised are: - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3830: Invalid action. - KT-CT-3831: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `[CreateScheduledTransactionsInput]!` |  | Input fields to create scheduled transactions. |

## `createShellAccount(input: CreateShellAccountInput!)`

- Return type: `CreateShellAccountPayload`
- Description: Create a shell/payment account.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateShellAccountInput!` |  |  |

## `createSolarWalletRelationship(input: CreateSolarWalletRelationshipType!)`

- Return type: `CreateSolarWalletRelationship`
- Deprecated: Yes (The 'createSolarWalletRelationship' field is deprecated. Use 'createCreditTransferPermission' mutation instead. - Marked as deprecated on 2025-02-10. - Scheduled for removal on or after 2025-08-10.)
- Description: Create solar wallet sharing credit between a solar wallet credit ledger and spain electricity ledger. The possible errors that can be raised are: - KT-ES-7805: The request to create a solar wallet sharing credit between ledgers was incomplete or malformed. - KT-CT-4123: Unauthorized. - KT-ES-4116: Account not found. - KT-ES-7809: There is no ledger of this type on this account.. - KT-ES-7806: Couldn't create sharing credit between ledgers because credit sharing ledger already exist. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateSolarWalletRelationshipType!` |  | Input fields for creating a solar wallet sharing credit between ledgers. |

## `createTimeSeriesPrices(input: CreateTimeSeriesPricesInput!)`

- Return type: `CreateTimeSeriesPrices!`
- Deprecated: Yes (The 'createTimeSeriesPrices' field is deprecated. Please use the 'createOrUpdateTimeSeriesEntries' mutation instead. - Marked as deprecated on 2025-02-03. - Scheduled for removal on or after 2025-03-01.)
- Description: Create time series prices. The possible errors that can be raised are: - KT-CT-12014: Time series not found. - KT-CT-12015: Characteristics mismatch. - KT-CT-12016: Conflicting time series entries. - KT-CT-12017: Invalid time series entries period. - KT-CT-12038: Invalid time series entries granularity. - KT-CT-12040: Time series entries in use. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateTimeSeriesPricesInput!` |  | The time series input for price creation. |

## `deauthenticateDevice(input: DeAuthenticationInput)`

- Return type: `DeauthenticateDevice`
- Deprecated: Yes (The 'deauthenticateDevice' field is deprecated. Please use 'deauthenticateFlexDevice' instead. - Marked as deprecated on 2025-05-12. - Scheduled for removal on or after 2026-01-16. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/606/)
- Description: De-authenticate a device. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4350: Unable to de-authenticate device. - KT-CT-4352: This device cannot currently be de-authenticated. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeAuthenticationInput` |  |  |

## `deauthenticateFlexDevice(input: DeauthenticateFlexDeviceInput)`

- Return type: `DeauthenticateFlexDevice`
- Description: De-authenticate a device by device id. The possible errors that can be raised are: - KT-CT-4350: Unable to de-authenticate device. - KT-CT-4352: This device cannot currently be de-authenticated. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeauthenticateFlexDeviceInput` |  |  |

## `deductLoyaltyPoints(input: DeductLoyaltyPointsInput!)`

- Return type: `DeductLoyaltyPoints`
- Description: Deduct the passed number of Loyalty Points from the account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-5420: Unauthorized. - KT-CT-9211: Invalid reason for loyalty points award. - KT-CT-9219: Loyalty points user not found. - KT-CT-9204: Negative or zero points set. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9221: Idempotency key already used on ledger entry. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeductLoyaltyPointsInput!` |  | Input fields for deducting Loyalty Points. |

## `deleteAccountReference(input: DeleteAccountReferenceInput!)`

- Return type: `DeleteAccountReference`
- Description: Delete an account reference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8312: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeleteAccountReferenceInput!` |  | Input fields for removing an account reference. |

## `deleteBoostCharge(input: DeleteBoostChargeInput)`

- Return type: `DeleteBoostCharge`
- Deprecated: Yes (The 'deleteBoostCharge' field is deprecated. Please use 'updateBoostCharge' instead. - Marked as deprecated on 2025-05-12. - Scheduled for removal on or after 2026-01-26. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/607/)
- Description: Stop any active boost charging. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4354: Unable to cancel boost charge. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeleteBoostChargeInput` |  |  |

## `deleteMfaDevice(input: DeleteMfaDeviceInputType!)`

- Return type: `DeleteMfaDevice`
- Description: Delete MFA Device for user. The possible errors that can be raised are: - KT-CT-1150: MFA device not found. - KT-CT-1154: Unable to delete MFA device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeleteMfaDeviceInputType!` |  | Input fields for deleting an existing multi-factor authentication device for the logged user. |

## `deletePropertyDescendants(input: DeletePropertyDescendantsInput!)`

- Return type: `DeletePropertyDescendants`
- Description: Delete all descendants of a property in a hierarchy. This permanently deletes all descendant nodes (children, grandchildren, etc.) but keeps the property node itself in the hierarchy. This operation is idempotent - if the property is not in the hierarchy or has no descendants, it will succeed without error. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeletePropertyDescendantsInput!` |  | Input fields for deleting descendants from a property. |

## `deletePushNotificationBinding(input: DeletePushNotificationBindingInput!)`

- Return type: `DeletePushNotificationBinding`
- Description: Delete a device token used for push notifications. This field requires the `Authorization` header to be set. The possible errors that can be raised are: - KT-CT-5411: Invalid token or no push notification binding found for the given account user. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeletePushNotificationBindingInput!` |  | Input fields for deleting a push notification binding. |

## `detachSupplyPointFromEstimationGroup(input: DetachSupplyPointFromEstimationGroupInput!)`

- Return type: `DetachSupplyPointFromEstimationGroup`
- Description: The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-13603: Supply Point does not exist. - KT-CT-13604: Supply point has no estimation group assigned. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DetachSupplyPointFromEstimationGroupInput!` |  | Input fields for detaching a supply point from an estimation group. |

## `deviceRegistration(input: DeviceRegistrationInput)`

- Return type: `DeviceRegistration`
- Deprecated: Yes (The 'deviceRegistration' field is deprecated. Please use 'startSmartFlexOnboarding' instead. - Marked as deprecated on 2025-09-08. - Scheduled for removal on or after 2026-03-01. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/678/)
- Description: Register a device (EV, battery or heat pump) for smart control. The possible errors that can be raised are: - KT-CT-4324: Device already registered error. - KT-CT-4321: Serializer validation error. - KT-CT-4312: Unable to register device. - KT-CT-4363: No capable devices found. - KT-CT-4364: Multiple devices found. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DeviceRegistrationInput` |  |  |

## `endContributionAgreement(input: EndContributionAgreementInput!)`

- Return type: `EndContributionAgreement`
- Description: End a contribution agreement for an account. The possible errors that can be raised are: - KT-CT-9603: Unable to find contribution agreement. - KT-CT-4123: Unauthorized. - KT-CT-9604: Unable to end contribution agreement. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `EndContributionAgreementInput!` |  | Input variables needed for ending a contribution agreement on an account. |

## `enqueueInboundCall(input: EnqueueInboundCallInput!)`

- Return type: `EnqueueInboundCall`
- Description: The possible errors that can be raised are: - KT-CT-11802: Call not found. - KT-CT-11803: Unable to enqueue the call. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `EnqueueInboundCallInput!` |  |  |

## `enrollAccountInLoyaltyProgram(input: EnrollAccountInLoyaltyProgramInput!)`

- Return type: `EnrollAccountInLoyaltyProgram`
- Description: Enroll users account in Loyalty program. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9213: ineligible loyalty points enrollment. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `EnrollAccountInLoyaltyProgramInput!` |  | The account number to enroll in the loyalty program. |

## `enrollment(input: EnrollmentInput!)`

- Return type: `EnrollmentInitiated!`
- Description: Initiate an enrollment for an account and a set of supply points. The possible errors that can be raised are: - KT-CT-1602: Serializer validation error. - KT-CT-4410: Invalid postcode. - KT-CT-4412: The supplied address is not valid. - KT-CT-4501: Unauthorized. - KT-CT-7719: Session not found. - KT-CT-10312: Mutation not enabled in this environment. - KT-CT-10313: Failed to enroll account. - KT-CT-10314: This supply point is already on supply. - KT-CT-10315: Unable to begin enrollment journey due to invalid data. - KT-CT-6622: Unauthorized. - KT-CT-10340: House move enrollment is not enabled. - KT-CT-10302: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `EnrollmentInput!` |  | The Enrollment Input data for the Join Supplier. |

## `fetchGeneratePaymentFingerprint(input: FetchGeneratePaymentFingerprintInput!)`

- Return type: `FetchGeneratePaymentFingerprint`
- Description: Fetch or generate payment fingerprint from vendor. The possible errors that can be raised are: - KT-CT-12101: Payment instruction not found. - KT-CT-12102: Payment vendor not supported. - KT-CT-12103: Missing payment metadata from vendor. - KT-CT-12104: Unable to fetch or generate payment fingerprint. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `FetchGeneratePaymentFingerprintInput!` |  |  |

## `fetchPreSignedLinkForOpportunityAttachment(input: FetchPreSignedLinkForOpportunityAttachmentInput!)`

- Return type: `FetchPreSignedLinkForOpportunityAttachment`
- Description: Fetch a pre-signed link for an opportunity file attachment. The possible errors that can be raised are: - KT-CT-8933: Opportunity file attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `FetchPreSignedLinkForOpportunityAttachmentInput!` |  | Input fields for fetching a pre-signed link for an opportunity file attachment. |

## `forceReauthentication(input: ForceReauthenticationInput!)`

- Return type: `ForceReauthentication`
- Description: Force users of Kraken Tokens and refresh tokens issued to the viewer to reauthenticate. Calling this mutation will cause all Kraken Tokens and refresh tokens issued to the authenticated viewer before the mutation was called to become invalid.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ForceReauthenticationInput!` |  | Input object argument to the force-reauthentication mutation. |

## `generateAffiliatesAudioRecordingPreSignedUrl(input: GenerateAffiliatesAudioRecordingPreSignedUrlInput!)`

- Return type: `GenerateAffiliatesAudioRecordingPreSignedUrl!`
- Description: Generate a pre signed url for uploading a file for use with affiliates.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GenerateAffiliatesAudioRecordingPreSignedUrlInput!` |  | Input fields for creating a pre-signed URL for uploading an audio file to S3. |

## `generateInkPresignedUrl(input: GenerateInkPresignedUrlInput)`

- Return type: `GenerateInkPresignedUrl`
- Description: The possible errors that can be raised are: - KT-CT-7620: Channel not supported. - KT-CT-7618: Unable to process message. - KT-CT-7624: Error when generating the presigned URL. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GenerateInkPresignedUrlInput` |  |  |

## `generateLeadsFileAttachmentDownloadPreSignedUrl(input: GenerateLeadsFileAttachmentDownloadPreSignedUrlInput!)`

- Return type: `GenerateLeadsFileAttachmentDownloadPreSignedUrl`
- Description: Generate a pre-signed URL for downloading a leads attachment file. The possible errors that can be raised are: - KT-CT-8933: Opportunity file attachment not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GenerateLeadsFileAttachmentDownloadPreSignedUrlInput!` |  | Input fields for creating a pre-signed URL for downloading a lead file attachment from S3. |

## `generateLeadsFileAttachmentPreSignedUrl(input: GenerateLeadsFileAttachmentPreSignedUrlInput!)`

- Return type: `GenerateLeadsFileAttachmentsPreSignedUrl`
- Description: Generate a pre signed url for uploading a leads attachment file.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GenerateLeadsFileAttachmentPreSignedUrlInput!` |  | Input fields for creating a pre-signed URL for uploading a lead file attachment file to S3. |

## `generatePreSignedToken(email: String!, numberOfDaysAllowed: Int!, scope: PreSignedTokenScope!)`

- Return type: `GeneratePreSignedToken`
- Description: Generate a pre-signed token with a set expiry time. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1120: The Kraken Token has expired. - KT-CT-1131: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `email` | `String!` |  |  |
| `numberOfDaysAllowed` | `Int!` |  | The number of days that the token will be available for authentication (From now on). |
| `scope` | `PreSignedTokenScope!` |  | Define (and limit) the scope of the token. |

## `getEmbeddedSecretForNewPaymentInstruction(input: GetEmbeddedSecretForNewPaymentInstructionInput!)`

- Return type: `GetEmbeddedSecretForNewPaymentInstruction`
- Description: Get the client secret needed to create a new payment instruction using an embedded form. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3820: Received both ledger ID and number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GetEmbeddedSecretForNewPaymentInstructionInput!` |  | Input fields for getting the client secret for an embedded new card payment method form. |

## `getEmbeddedSecretForNewPaymentInstructionWithoutAccount(input: GetEmbeddedSecretForNewPaymentInstructionWithoutAccountInput!)`

- Return type: `GetEmbeddedSecretForNewPaymentInstructionWithoutAccount`
- Description: Get the client secret needed to create a new payment instruction using an embedded form without tying it to a customer.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GetEmbeddedSecretForNewPaymentInstructionWithoutAccountInput!` |  | Input fields for getting the client secret for an embedded new card payment method form. |

## `getHostedUrlForNewPaymentInstruction(input: GetHostedUrlForNewPaymentInstructionInput!)`

- Return type: `GetHostedUrlForNewPaymentInstruction`
- Description: Get the external URL where the user can set up a payment instruction. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GetHostedUrlForNewPaymentInstructionInput!` |  | Input fields for getting the external URL for setting up a payment instruction. |

## `getOrCreateAgreement(input: CreateAgreementInput!)`

- Return type: `GetOrCreateAgreement`
- Description: Get an existing agreement or create a new one if it doesn't exist. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-4910: No product exists with the given input. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1509: Unable to create agreement. - KT-CT-1511: Cannot create overlapping agreement. - KT-CT-1512: Account type does not support agreements. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CreateAgreementInput!` |  | Input fields for getting or creating an agreement. |

## `grantUserAccessToBusiness(input: GrantUserAccessToBusinessInput!)`

- Return type: `GrantUserAccessToBusiness`
- Description: Grant user access to the business using the provided role. The possible errors that can be raised are: - KT-CT-5463: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-13501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GrantUserAccessToBusinessInput!` |  |  |

## `initializeAccount(input: BaseInitializeAccountInput!)`

- Return type: `InitializeAccountResult!`
- Description: Initialize account for sign up. Returns the existing account if matching datafound for the provided input, otherwise creates a new account. The possible errors that can be raised are: - KT-CT-10324: Mutation not enabled in this environment. - KT-CT-10325: Input data has invalid format. - KT-CT-10326: An error occurred when trying to initialize the account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `BaseInitializeAccountInput!` |  |  |

## `initializeUser(input: BaseInitializeUserInput!)`

- Return type: `InitializeUserResult!`
- Description: Initialize user for sign up. Returns an existing user if matching datafound for the provided input, otherwise creates a new one. The possible errors that can be raised are: - KT-CT-10327: Mutation not enabled in this environment. - KT-CT-10328: Input data has invalid format. - KT-CT-10329: An error occurred when trying to initialize the user. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `BaseInitializeUserInput!` |  |  |

## `initiateHostedStandalonePayment(input: InitiateHostedStandalonePaymentInput!)`

- Return type: `InitiateHostedStandalonePayment`
- Description: Initiate a standalone payment and return the url where the customer can complete it. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3943: Invalid ledger. - KT-CT-3957: No collection method provided. - KT-CT-3958: Provide either ledger ID or ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InitiateHostedStandalonePaymentInput!` |  | Input fields for initiating a standalone payment. |

## `initiateProductSwitch(input: InitiateProductSwitchInput!)`

- Return type: `InitiateProductSwitch`
- Description: Do a product switch for a user. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4619: Quote with given code not found. - KT-CT-4624: Unable to accept the given product code. - KT-CT-4924: Unauthorized. - KT-CT-4626: No product selected for the given quote code. - KT-CT-4719: No supply point found for identifier provided. - KT-CT-1509: Unable to create agreement. - KT-CT-1507: Agreement product switch date is not within the acceptable range. - KT-CT-4640: Unable to get market or client params from quoted product. - KT-CT-4627: No products are available for this quote. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InitiateProductSwitchInput!` |  | Instigate a product switch for a specific supply point given a valid product and account number. |

## `initiateStandalonePayment(input: InitiateStandalonePaymentInput!)`

- Return type: `InitiateStandalonePayment`
- Description: Initiate a standalone payment and return the client secret required to complete it. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3943: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InitiateStandalonePaymentInput!` |  | Input fields for initiating a standalone payment. |

## `instigateContractTermination(input: BaseInstigateContractTerminationInput!)`

- Return type: `ContractTerminationInstigated!`
- Description: Instigate a contract termination journey. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10004: Supply loss process instigation has failed. - KT-CT-10007: Unable to terminate contract. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10013: Requested termination date is invalid. - KT-CT-10014: The provided contract termination input data is invalid. - KT-CT-10015: Supply point termination context is not serializable. - KT-CT-10016: Error building contract termination engine. - KT-CT-10022: Contract already terminated. - KT-CT-10023: Contract is already revoked. - KT-CT-10024: Contract already expired. - KT-CT-10025: Contract has not started yet. - KT-CT-10037: Contract notes feature is disabled. - KT-CT-10038: Contract note reason not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `BaseInstigateContractTerminationInput!` |  |  |

## `instigateContractVariation(input: InstigateContractVariationInput!)`

- Return type: `InstigateContractVariationOutput!`
- Deprecated: Yes (The 'instigateContractVariation' field is deprecated. This is a legacy mutation. The varyContractTerms should be used instead. - Marked as deprecated on 2026-03-05. - Scheduled for removal on or after 2026-04-11.)
- Description: Instigate a contract variation journey. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10011: Unable to vary contract terms. - KT-CT-10033: Unable to save term. - KT-CT-10012: Contract variation implies breach. - KT-CT-10034: Unknown contract journey type. - KT-CT-10035: Cannot process a non-active contract journey. - KT-CT-10036: The contract journey manager is not found. - KT-CT-10037: Contract notes feature is disabled. - KT-CT-10038: Contract note reason not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InstigateContractVariationInput!` |  |  |

## `instigateLeaveSupplier(input: LeaveSupplierInput!)`

- Return type: `LeaveSupplierInstigated!`
- Description: Instigate a leave supplier process or update an existing process. The possible errors that can be raised are: - KT-CT-10304: Mutation not enabled in this environment. - KT-CT-4501: Unauthorized. - KT-CT-10301: Unable to instigate leave supplier process. - KT-CT-10330: Unsupported leave supplier type. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LeaveSupplierInput!` |  |  |

## `invalidatePaymentInstruction(input: InvalidatePaymentInstructionInput!)`

- Return type: `InvalidatePaymentInstruction`
- Description: Invalidate an existing instruction. The possible errors that can be raised are: - KT-CT-3926: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InvalidatePaymentInstructionInput!` |  | Input fields for invalidating a payment instruction from an embedded form. |

## `invalidatePreSignedToken(input: InvalidatePreSignedTokenInput!)`

- Return type: `InvalidatePreSignedToken`
- Description: Invalidate a previously-issued pre-signed token. The possible errors that can be raised are: - KT-CT-1129: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InvalidatePreSignedTokenInput!` |  |  |

## `invalidatePreSignedTokensForUser(input: InvalidatePreSignedTokensForUserInput!)`

- Return type: `InvalidatePreSignedTokensForUser`
- Description: Invalidate pre-signed tokens issued to a particular user. The possible errors that can be raised are: - KT-CT-1129: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InvalidatePreSignedTokensForUserInput!` |  |  |

## `invalidateRefreshToken(input: InvalidateRefreshTokenInput!)`

- Return type: `InvalidateRefreshToken`
- Description: Invalidate a previously-issued refresh token. The possible errors that can be raised are: - KT-CT-1130: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InvalidateRefreshTokenInput!` |  |  |

## `invalidateRefreshTokensForUser(input: InvalidateRefreshTokensForUserInput!)`

- Return type: `InvalidateRefreshTokensForUser`
- Description: Invalidate refresh tokens issued to a particular user. The possible errors that can be raised are: - KT-CT-1128: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `InvalidateRefreshTokensForUserInput!` |  |  |

## `joinSupplierAcceptTermsAndConditions(input: JoinSupplierAcceptTermsAndConditionsInput!)`

- Return type: `JoinSupplierAcceptTermsAndConditions`
- Description: Accept terms and conditions for a join supplier process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `JoinSupplierAcceptTermsAndConditionsInput!` |  |  |

## `legacyProcessOrder(input: LegacyProcessOrderInput!)`

- Return type: `LegacyProcessOrderOutput!`
- Description: Process an Order (legacy) The possible errors that can be raised are: - KT-CT-1605: Invalid input. - KT-CT-7701: The affiliate organisation was not found. - KT-CT-8906: Opportunity not found. - KT-CT-12701: Invalid sales channel code. - KT-CT-13102: Invalid order data. - KT-CT-13103: Unprocessable order. - KT-CT-13104: Conflicting order. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LegacyProcessOrderInput!` |  |  |

## `linkAccountToBusiness(input: LinkAccountToBusinessInput!)`

- Return type: `LinkAccountToBusiness`
- Description: Link an account to a business. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11104: Business role already allocated. - KT-CT-11105: Business role already allocated. - KT-CT-11106: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LinkAccountToBusinessInput!` |  | Input fields for linking an account to a business. |

## `linkUserToLine(input: LinkUserToLineInput!)`

- Return type: `LinkUserToLineResponse!`
- Description: Link an account user and line user together.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `LinkUserToLineInput!` |  | Input fields to link an account user with LINE. |

## `markPrintBatchAsProcessed(printBatchId: ID!)`

- Return type: `MarkPrintBatchAsProcessed!`
- Description: Mark the print batch as processed. The possible errors that can be raised are: - KT-CT-9011: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `printBatchId` | `ID!` |  |  |

## `masqueradeAuthentication(masqueradeToken: String!, userId: String!)`

- Return type: `MasqueradeAuthentication`
- Description: Provide a temporary token to get an auth token. This is intended to allow support users to view customer data through the brand interface.

| Arg | Type | Default | Description |
|---|---|---|---|
| `masqueradeToken` | `String!` |  | The masquerade token issued by the support site. |
| `userId` | `String!` |  | The ID of the AccountUser to masquerade as. |

## `moveToBucket(input: MoveToBucketInput)`

- Return type: `MoveToBucket`
- Description: The possible errors that can be raised are: - KT-CT-7612: The Ink conversation was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `MoveToBucketInput` |  | Input for moving a conversation to a bucket. |

## `nextOperationsTeamRoundRobin(teamGroupName: String!)`

- Return type: `NextOperationsTeamRoundRobin`

| Arg | Type | Default | Description |
|---|---|---|---|
| `teamGroupName` | `String!` |  | The name of the operations team group to select from. |

## `obtainKrakenToken(input: ObtainJSONWebTokenInput!)`

- Return type: `ObtainKrakenJSONWebToken`
- Description: Create a Kraken Token (JWT) for authentication. Provide the required input fields to obtain the token. The token should be used as the `Authorization` header for any authenticated requests. The possible errors that can be raised are: - KT-CT-1135: Invalid data. - KT-CT-1134: Invalid data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ObtainJSONWebTokenInput!` |  | Input fields that can be used to obtain a Json Web Token (JWT) for authentication to the API. |

## `obtainLongLivedRefreshToken(input: ObtainLongLivedRefreshTokenInput!)`

- Return type: `ObtainLongLivedRefreshToken`
- Description: For authorized third-party organizations only. The possible errors that can be raised are: - KT-CT-1120: The Kraken Token has expired. - KT-CT-1121: Please use Kraken Token to issue long-lived refresh tokens. - KT-CT-1132: Unauthorized. - KT-CT-1122: Long-lived refresh tokens can only be issued for account users. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ObtainLongLivedRefreshTokenInput!` |  | Input fields for obtaining a long-lived refresh token to extend the expiry claim of a Kraken token. |

## `ocppAuthentication(input: OCPPAuthenticationInput)`

- Return type: `OCPPAuthentication`
- Description: Trigger OCPP authentication. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4310: Unable to register OCPP authentication details. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `OCPPAuthenticationInput` |  |  |

## `pauseCollectionProcess(input: PauseCollectionProcessInput!)`

- Return type: `PauseCollectionProcess`
- Description: Pause a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11214: Invalid pause length for collection process. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PauseCollectionProcessInput!` |  | Details for pausing a collection process. |

## `pauseDunning(input: PauseDunningInputType!)`

- Return type: `PauseDunning`
- Description: Pause the dunning process for an account. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11301: Account not in a dunning process for the given path name. - KT-CT-11302: No active dunning process found. - KT-CT-11303: Multiple active dunning processes found. - KT-CT-11304: Dunning pause process failed verifying the dates. - KT-CT-11305: Pausing the dunning process failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PauseDunningInputType!` |  | Input variables needed for pausing a dunning process for an account. |

## `payoutReferralForAccount(input: PayoutReferralForAccountInput!)`

- Return type: `PayoutReferralForAccount`
- Description: Pay out a referral reward for an account. The possible errors that can be raised are: - KT-CT-6712: Invalid reference. - KT-CT-6723: Unauthorized. - KT-CT-6730: Referral cannot be paid out. - KT-CT-6731: The account is unrelated to the referral. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PayoutReferralForAccountInput!` |  | Input fields for paying out a referral for an account. |

## `postCredit(input: PostCreditInput!)`

- Return type: `PostCredit`
- Description: Post credit to a ledger. The possible errors that can be raised are: - KT-CT-5316: Invalid data. - KT-CT-5311: The credit reason with the requested code is deprecated. - KT-CT-5312: The credit reason with the requested code does not exist. - KT-CT-5313: An error occurred whilst posting the credit. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PostCreditInput!` |  | Input fields for posting a credit. |

## `prepareAccount(input: PrepareAccountInput!)`

- Return type: `PrepareAccountResult!`
- Description: Prepare account for sign up. Returns the existing account and/or user if matching datafound for the provided input, otherwise creates a new account and account user. The possible errors that can be raised are: - KT-CT-10303: Mutation not enabled in this environment. - KT-CT-10316: Input data has invalid format. - KT-CT-10317: An error occured when trying to prepare the account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PrepareAccountInput!` |  |  |

## `publishApprovalApprovedEvent(input: PublishApprovalApprovedEventInput!)`

- Return type: `PublishApprovalApprovedEvent`
- Description: Publish an approval approved external event. The possible errors that can be raised are: - KT-CT-14501: Invalid event parameters. - KT-CT-14502: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PublishApprovalApprovedEventInput!` |  | Input fields for publishing an approval approved event. |

## `publishTransactionalMessagingExternalTrigger(input: PublishTransactionalMessagingExternalTriggerInput!)`

- Return type: `PublishTransactionalMessagingExternalTrigger`
- Description: Publish an externally defined transactional messaging trigger. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-5421: Account user not found. - KT-CT-9901: Invalid trigger type code. - KT-CT-9905: Top-level context fields are missing. - KT-CT-9906: Template variables do not match the defined schema. - KT-CT-9908: Invalid recipient information. - KT-CT-9909: Invalid recipient information. - KT-CT-9910: Invalid input field combination. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PublishTransactionalMessagingExternalTriggerInput!` |  | Input fields to publish an external transactional messaging trigger. |

## `publishTransactionalMessagingTrigger(input: PublishTransactionalMessagingTriggerInput!)`

- Return type: `PublishTransactionalMessagingTrigger`
- Description: Publish a trigger within the transactional messaging service. The possible errors that can be raised are: - KT-CT-9901: Invalid trigger type code. - KT-CT-9902: Invalid trigger type params. - KT-CT-9903: Trigger type cannot be published externally. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PublishTransactionalMessagingTriggerInput!` |  | Input fields to publish a transactional messaging trigger. |

## `purchaseVoucher(input: PurchaseVoucherInput!)`

- Return type: `PurchaseVoucher`
- Description: Purchase a voucher.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `PurchaseVoucherInput!` |  |  |

## `reactivateCollectionProcessRecord(input: ReactivateCollectionProcessRecordInputType!)`

- Return type: `ReactivateCollectionProcessRecord`
- Description: Reactivate a Collection Process Record that was previously activated. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11217: Invalid collection process record status for reactivation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ReactivateCollectionProcessRecordInputType!` |  | Input variables needed for reactivating a collection process record. |

## `recordDepositAgreementAccepted(input: DepositAgreementInput!)`

- Return type: `RecordDepositAgreementAccepted`
- Description: Record the customer's acceptance of a deposit agreement. The possible errors that can be raised are: - KT-CT-4177: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DepositAgreementInput!` |  |  |

## `recordFailedPayment(input: RecordFailedPaymentInput!)`

- Return type: `RecordFailedPayment`
- Description: Record one or more failed payments. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RecordFailedPaymentInput!` |  | Details about the failed payments. |

## `recordPendingPayment(input: RecordPendingPaymentInput!)`

- Return type: `RecordPendingPayment`
- Description: Record one or more pending payments. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RecordPendingPaymentInput!` |  | Details about the pending payments. |

## `recordSuccessfulPayment(input: RecordSuccessfulPaymentInput!)`

- Return type: `RecordSuccessfulPayment`
- Description: Record one or more successful payments. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3985: Received both token and options for action intent. - KT-CT-3986: Received neither token nor options for action intent. - KT-CT-3987: Invalid payment method type code. - KT-CT-3988: Number of items in list exceeds maximum value. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RecordSuccessfulPaymentInput!` |  | Details about the successful payments. |

## `redeemLoyaltyPointsForAccountCredit(input: RedeemLoyaltyPointsInput!)`

- Return type: `RedeemLoyaltyPointsForAccountCredit`
- Description: Redeem the passed number of Loyalty Points as account credit. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9201: No Loyalty Point ledger found for the user. - KT-CT-9202: Loyalty Points adapter not configured. - KT-CT-9203: No ledger entries for the ledger. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9206: Indivisible points. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9209: Negative Loyalty Points balance. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RedeemLoyaltyPointsInput!` |  | Input fields for redeeming Loyalty Points. |

## `redeemReferralClaimCode(input: RedeemReferralClaimCodeInput!)`

- Return type: `RedeemReferralClaimCode`
- Description: Redeem the referral claim code from certain referral scheme. The possible errors that can be raised are: - KT-CT-6723: Unauthorized. - KT-CT-6724: Referral claim code not found. - KT-CT-6725: Referral claim code redeeming error. - KT-CT-6726: Referral claim code has already been redeemed. - KT-CT-6727: Referral claim code is not available. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RedeemReferralClaimCodeInput!` |  | Input fields for redeeming referral code. |

## `refundPayment(input: RefundPaymentInput!)`

- Return type: `RefundPayment`
- Description: Refund a cleared payment. The possible errors that can be raised are: - KT-CT-3924: Unauthorized. - KT-CT-3928: Idempotency key used for another repayment request. - KT-CT-3929: The payment is not in a refundable state. - KT-CT-3933: Refund amount greater than payment amount. - KT-CT-3937: Payment not eligible for refund. - KT-CT-3938: Partial refund not allowed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RefundPaymentInput!` |  | Input fields for refunding a payment. |

## `regenerateSecretKey`

- Return type: `RegenerateSecretKey`
- Description: Regenerate the live secret key for the authenticated user.

## `registerEvChargerLead(lead: EVChargerLeadZohoType)`

- Return type: `RegisterEVChargerLead`
- Description: Register an EV Charger lead to Zoho. The possible errors that can be raised are: - KT-ES-7803: The request to Chipiron was incomplete or malformed. - KT-ES-7804: The request to Chipiron caused a conflict - might you be trying to create a duplicate? - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `lead` | `EVChargerLeadZohoType` |  |  |

## `registerLeadFlowStatusEvent(input: RegisterLeadFlowStatusEventInput!)`

- Return type: `RegisterLeadFlowStatusEvent`
- Description: Register a flow status event for a lead. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RegisterLeadFlowStatusEventInput!` |  | Input fields for registering a flow status event for a Lead. |

## `registerOpportunityFlowStatusEvent(input: RegisterOpportunityFlowStatusEventInput!)`

- Return type: `RegisterOpportunityFlowStatusEvent`
- Description: Register a flow status event for an opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RegisterOpportunityFlowStatusEventInput!` |  | Input fields for registering a flow status event for a opportunity. |

## `registerPhoneLead(input: TelephoneLeadType)`

- Return type: `RegisterPhoneLead`
- Description: Register a phone lead The possible errors that can be raised are: - KT-ES-8910: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TelephoneLeadType` |  |  |

## `registerPushNotificationBinding(input: RegisterPushNotificationBindingInput!)`

- Return type: `RegisterPushNotificationBinding`
- Description: Register a device token to be used for push notifications for an app. This field requires the `Authorization` header to be set.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RegisterPushNotificationBindingInput!` |  | Input fields for creating an push notification binding. |

## `registerSolarSimulatorDirectSale(input: SolarSimulatorDirectSaleInput)`

- Return type: `SolarSimulatorDirectSaleOutput`
- Description: Create a solar direct sale. The possible errors that can be raised are: - KT-ES-7803: The request to Chipiron was incomplete or malformed. - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SolarSimulatorDirectSaleInput` |  |  |

## `registerSolarSimulatorLead(input: SolarSimulatorLeadInput)`

- Return type: `SolarSimulatorLeadOutput`
- Description: Create a solar lead. The possible errors that can be raised are: - KT-ES-7803: The request to Chipiron was incomplete or malformed. - KT-ES-7802: The request to Chipiron was not fulfilled correctly. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SolarSimulatorLeadInput` |  |  |

## `removeCampaignFromAccount(input: RemoveCampaignFromAccountInput!)`

- Return type: `RemoveCampaignFromAccount`
- Description: The possible errors that can be raised are: - KT-CT-7424: Failed to remove campaign from account. - KT-CT-7426: The account is not part of the given campaign. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RemoveCampaignFromAccountInput!` |  | Input variables needed for removing a campaign from an account. |

## `removeCampaignItems(input: RemoveCampaignItemsInput!)`

- Return type: `RemoveCampaignItems`
- Description: The possible errors that can be raised are: - KT-CT-11501: Voice campaign not found. - KT-CT-11502: Cannot remove items from multiple campaigns at once. - KT-CT-11505: Voice campaign item not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RemoveCampaignItemsInput!` |  |  |

## `removeItemsFromRiskList(input: [RiskListItemInputType]!)`

- Return type: `RemoveItemsFromRiskList`
- Description: Remove items from the risk list. The possible errors that can be raised are: - KT-CT-12106: Risk list item removal failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `[RiskListItemInputType]!` |  | A list of risk list items to remove. |

## `removePropertyFromHierarchy(input: RemovePropertyFromHierarchyInput!)`

- Return type: `RemovePropertyFromHierarchy`
- Description: Remove a property from a hierarchy. This operation is idempotent - if the property is not in the hierarchy, it will succeed without error. When a property is removed, its descendants are reparented to the removed property's parent. If removing a root node, its children become new root nodes. The possible errors that can be raised are: - KT-CT-6622: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RemovePropertyFromHierarchyInput!` |  | Input fields for removing a property from a hierarchy. |

## `requestDoubleOptIn(input: DoubleOptInInput)`

- Return type: `RequestDoubleOptIn`
- Description: Request a double opt in The possible errors that can be raised are: - KT-CT-9019: Invalid input. - KT-CT-9018: Account not found. - KT-CT-1111: Unauthorized. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-9023: Consent already accepted. - KT-CT-1199: Too many requests. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `DoubleOptInInput` |  |  |

## `requestPasswordReset(input: RequestPasswordResetInput!)`

- Return type: `RequestPasswordResetOutputType`
- Description: Provide the email address of an account user to send them an email with instructions on how to reset their password. The possible errors that can be raised are: - KT-CT-11331: Invalid input data. - KT-CT-11332: Invalid data. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RequestPasswordResetInput!` |  | Input fields for requesting a password reset email. |

## `requestPrintedBill(input: RequestPrintedBillInput!)`

- Return type: `RequestPrintedBill`
- Description: Request an issued bill to be printed and (re)posted to billing address of the account. The possible errors that can be raised are: - KT-CT-3824: Unauthorized. - KT-CT-9705: The billing document has not been issued. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RequestPrintedBillInput!` |  | Input fields to request a printed bill. |

## `resetPassword(input: ResetPasswordMutationInput!)`

- Return type: `ResetPasswordMutationPayload`
- Deprecated: Yes (The 'resetPassword' field is deprecated. Please use `resetUserPassword` instead. - Marked as deprecated on 2024-12-04. - Scheduled for removal on or after 2025-06-01. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/81/)
- Description: Reset the password of an account user indicated by the userId to the value supplied.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ResetPasswordMutationInput!` |  |  |

## `resetUserPassword(input: ResetUserPasswordInput!)`

- Return type: `ResetUserPasswordOutput`
- Description: Reset the password of an account user. Raises `KT-CT-5450` if password validation fails. Inspect the `validationErrors` extension to get the exact validation error: ```json { "data": {"resetUserPassword": null}, "errors": [ { "message": "Password is invalid.", "path": ["resetUserPassword"], "extensions": { "errorType": "VALIDATION", "errorCode": "KT-CT-5450", "errorDescription": "Given password fails password policy requirements.", "validationErrors": [ { "code": "password_too_short", "message": "This password is too short. It must contain at least 7 characters.", "inputPath": ["input", "password"] }, { "code": "password_too_common", "message": "This password is too common.", "inputPath": ["input", "password"] } ] } } ] } ``` The validation error's `code` can be any of - `password_too_short` - `password_too_common` - `password_reused` - `password_matches_current` - `password_has_too_few_numeric_characters` - `password_has_too_few_special_characters` - `password_has_too_few_lowercase_characters` - `password_has_too_few_uppercase_characters` - `password_contains_account_number` - `password_contains_part_of_email_address` The possible errors that can be raised are: - KT-CT-4125: Unauthorized. - KT-CT-1132: Unauthorized. - KT-CT-5450: Password is invalid. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ResetUserPasswordInput!` |  | Input fields for resetting an account user's password. |

## `resumeCollectionProcess(input: ResumeCollectionProcessInput!)`

- Return type: `ResumeCollectionProcess`
- Description: Resume a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11215: Unable to resume, collection process is not paused. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ResumeCollectionProcessInput!` |  | Details for resuming a collection process. |

## `resumeControl(input: AccountNumberInput)`

- Return type: `ResumeDeviceControl`
- Deprecated: Yes (The 'resumeControl' field is deprecated. Please use 'updateDeviceSmartControl' instead. - Marked as deprecated on 2024-09-17. - Scheduled for removal on or after 2025-12-11. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/468/)
- Description: Resume control of the device. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4359: Unable to resume device control. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AccountNumberInput` |  |  |

## `reverseEnrollment(input: ReverseEnrollmentInput!)`

- Return type: `EnrollmentReversed!`
- Description: Reverse an enrollment (Join Supplier process). The possible errors that can be raised are: - KT-CT-10312: Mutation not enabled in this environment. - KT-CT-10318: Enrollment process not found. - KT-CT-10349: Enrollment process is not reversible. - KT-CT-10350: Enrollment process can still be cancelled. - KT-CT-10351: Enrollment process being cancelled cannot be reversed. - KT-CT-10352: Market actions cannot be reversed for this enrollment process. - KT-CT-10353: Failed to reverse enrollment process. - KT-CT-10354: Enrollment reversal cut-off has passed. - KT-CT-10355: Enrollment reversal is not allowed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ReverseEnrollmentInput!` |  | The input required to reverse an enrollment. |

## `reverseLeaveSupplier(input: ReverseLeaveSupplierInput!)`

- Return type: `LeaveSupplierReversed!`
- Description: Reverse a leave supplier process. The possible errors that can be raised are: - KT-CT-10304: Mutation not enabled in this environment. - KT-CT-10302: Invalid data. - KT-CT-10341: Leave supplier process is not reversible. - KT-CT-10342: Leave supplier process can still be cancelled. - KT-CT-10343: Leave supplier process being cancelled cannot be reversed. - KT-CT-10344: Leave supplier reversal cut-off has passed. - KT-CT-10345: Occupier leave with real join cannot be reversed. - KT-CT-10346: Market action reversal is not supported for this leave supplier process. - KT-CT-10347: Failed to reverse leave supplier process. - KT-CT-10348: Leave supplier reversal is missing required dependencies. - KT-CT-1607: Value cannot be empty. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ReverseLeaveSupplierInput!` |  |  |

## `revokeAgreement(input: RevokeAgreementInput!)`

- Return type: `RevokeAgreement`
- Description: Revoke an agreement. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1501: Agreement not found. - KT-CT-1502: Billed agreements cannot be revoked. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RevokeAgreementInput!` |  | Input fields for revoking an agreement. |

## `revokeContract(input: RevokeContractInput!)`

- Return type: `RevokeContractOutput!`
- Description: Revoke an existing contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10022: Contract already terminated. - KT-CT-10023: Contract is already revoked. - KT-CT-10024: Contract already expired. - KT-CT-10032: Contract has already started. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RevokeContractInput!` |  |  |

## `revokeUserAccessFromBusiness(input: RevokeUserAccessFromBusinessInput!)`

- Return type: `RevokeUserAccessFromBusiness`
- Description: Revoke the selected role from the user for the business. The possible errors that can be raised are: - KT-CT-5463: Unauthorized. - KT-CT-11107: Unauthorized. - KT-CT-13501: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RevokeUserAccessFromBusinessInput!` |  |  |

## `runAgreementRollover(input: RunAgreementRolloverInput!)`

- Return type: `RunAgreementRollover`
- Description: Run an agreement rollover. The possible errors that can be raised are: - KT-CT-13705: Agreement rollover not found. - KT-CT-13706: Agreement rollover has an invalid status for this operation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RunAgreementRolloverInput!` |  | Input for running an agreement rollover. |

## `scheduleQuoteFollowUp(input: QuoteShareInput!)`

- Return type: `ScheduleQuoteFollowUp`
- Description: Schedule a quote follow-up to the provided recipient. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4632: Invalid recipient information. - KT-CT-4633: Mutation not enabled in this environment. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `QuoteShareInput!` |  |  |

## `selectChargePointMakeForSmartFlexOnboarding(input: SelectChargePointMakeInput!)`

- Return type: `SelectChargePointMakeForSmartFlexOnboarding`
- Deprecated: Yes (The 'selectChargePointMakeForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Select the charge point make to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectChargePointMakeInput!` |  |  |

## `selectChargePointVariantForSmartFlexOnboarding(input: SelectChargePointVariantInput!)`

- Return type: `SelectChargePointVariantForSmartFlexOnboarding`
- Deprecated: Yes (The 'selectChargePointVariantForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Select the charge point model variant to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectChargePointVariantInput!` |  |  |

## `selectDeviceTypeForSmartFlexOnboarding(input: SelectDeviceTypeInput!)`

- Return type: `SelectDeviceTypeForSmartFlexOnboarding`
- Deprecated: Yes (The 'selectDeviceTypeForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Select the device type to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectDeviceTypeInput!` |  |  |

## `selectFromListForSmartFlexOnboarding(input: SelectFromListInput!)`

- Return type: `SelectFromListForSmartFlexOnboarding`
- Description: Select from a list of options presented. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectFromListInput!` |  |  |

## `selectInverterMakeForSmartFlexOnboarding(input: SelectInverterMakeInput!)`

- Return type: `SelectInverterMakeForSmartFlexOnboarding`
- Deprecated: Yes (The 'selectInverterMakeForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Select the inverter make to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectInverterMakeInput!` |  |  |

## `selectProducts(input: SelectProductsInput!)`

- Return type: `SelectProducts`
- Description: Mark quoted products on a quote request as selected. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4634: Quoted product with given id not found. - KT-CT-4626: No product selected for the given quote code. - KT-CT-4635: Missing a quoted product for at least one quoted supply point on the quote request. - KT-CT-4636: Quoted product not linked to a product. - KT-CT-4646: Attempted to select multiple products for the same quoted supply point. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectProductsInput!` |  |  |

## `selectUserVehicleForSmartFlexOnboarding(input: SelectUserVehicleInput!)`

- Return type: `SelectUserVehicleForSmartFlexOnboarding`
- Deprecated: Yes (The 'selectUserVehicleForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Select the user's vehicle to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectUserVehicleInput!` |  |  |

## `selectVehicleMakeForSmartFlexOnboarding(input: SelectVehicleMakeInput!)`

- Return type: `SelectVehicleMakeForSmartFlexOnboarding`
- Deprecated: Yes (The 'selectVehicleMakeForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Select the vehicle make to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectVehicleMakeInput!` |  |  |

## `selectVehicleOrChargePointForSmartFlexOnboarding(input: SelectVehicleOrChargePointInput!)`

- Return type: `CompleteSelectVehicleOrChargePointForSmartFlexOnboarding`
- Description: Select the vehicle or charge point for the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectVehicleOrChargePointInput!` |  |  |

## `selectVehicleVariantForSmartFlexOnboarding(input: SelectVehicleVariantInput!)`

- Return type: `SelectVehicleVariantForSmartFlexOnboarding`
- Deprecated: Yes (The 'selectVehicleVariantForSmartFlexOnboarding' field is deprecated. Please use 'selectFromListForSmartFlexOnboarding' instead. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Select the vehicle model variant to proceed in the onboarding journey. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SelectVehicleVariantInput!` |  |  |

## `sendOfferQuoteSummary(input: OfferQuoteSummaryInput!)`

- Return type: `SendOfferQuoteSummary`
- Description: Send an offer quote summary to all active account users. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4178: No account found with given account number. - KT-CT-12407: The offer group does not contain an accepted offer. - KT-CT-5518: Account user not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `OfferQuoteSummaryInput!` |  |  |

## `sendQuoteSummary(input: QuoteShareInput!)`

- Return type: `SendQuoteSummary`
- Description: Send a quote summary to the provided recipient. The possible errors that can be raised are: - KT-CT-4619: Quote with given code not found. - KT-CT-4178: No account found with given account number. - KT-CT-4632: Invalid recipient information. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `QuoteShareInput!` |  |  |

## `sendVerificationEmail(input: SendVerificationEmailInput!)`

- Return type: `SendVerificationEmail`
- Description: Verify user's email address. The possible errors that can be raised are: - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SendVerificationEmailInput!` |  |  |

## `setDevicePreferences(input: SmartFlexDevicePreferencesInput!)`

- Return type: `SmartFlexDeviceInterface`
- Description: Set the user preferences for a device. The possible errors that can be raised are: - KT-CT-4314: Unable to get provider details. - KT-CT-4321: Serializer validation error. - KT-CT-4374: An error occurred while trying to set your device preferences. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SmartFlexDevicePreferencesInput!` |  | The device preference details to be updated. |

## `setLoyaltyPointsUser(input: SetLoyaltyPointsUserInput!)`

- Return type: `SetLoyaltyPointsUser`
- Description: Set the Loyalty Point user for the account. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-9214: Couldn't assign user loyalty points role. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SetLoyaltyPointsUserInput!` |  | Input fields for saving the Loyalty Points user. |

## `setOpportunityOutcome(input: SetOpportunityOutcomeInput!)`

- Return type: `SetOpportunityOutcome`
- Description: Update the opportunity outcome to mark the opportunity as won or lost. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SetOpportunityOutcomeInput!` |  | Input fields for setting the outcome of a opportunity. |

## `setPaymentPreference(input: SetPaymentPreferenceInput!)`

- Return type: `SetPaymentPreference`
- Description: Set a preference to collect payments from a specific payment method. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3967: Payment method is not valid. - KT-CT-3968: Preference cannot be set this soon. - KT-CT-3969: Preferences must change on a specific day of the week for weekly schedules. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SetPaymentPreferenceInput!` |  |  |

## `setUpDirectDebitInstruction(input: SetUpDirectDebitInstructionInput!)`

- Return type: `SetUpDirectDebitInstruction`
- Description: Set up a new direct debit instruction. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3940: Invalid data. - KT-CT-5415: Account user not found. - KT-CT-11103: Business not found. - KT-CT-3971: Instruction owners are not valid. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SetUpDirectDebitInstructionInput!` |  | Input fields for creating a new direct debit instruction. |

## `setUpDirectDebitInstructionForBusiness(input: SetUpDirectDebitInstructionForBusinessInput!)`

- Return type: `SetUpDirectDebitInstructionForBusiness`
- Description: Set up a new direct debit instruction for a business. The possible errors that can be raised are: - KT-CT-3940: Invalid data. - KT-CT-3956: Temporary error occurred. - KT-CT-11107: Unauthorized. - KT-CT-3948: Could not set up direct debit instruction. - KT-CT-3971: Instruction owners are not valid. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SetUpDirectDebitInstructionForBusinessInput!` |  | Input fields for creating a new direct debit instruction. |

## `setUpDirectDebitInstructionFromStoredDetails(input: SetUpDirectDebitInstructionFromStoredDetailsInput!)`

- Return type: `SetUpDirectDebitInstructionFromStoredDetails`
- Description: Set up a new direct debit instruction from stored details. The possible errors that can be raised are: - KT-CT-3956: Temporary error occurred. - KT-CT-3948: Could not set up direct debit instruction. - KT-CT-3971: Instruction owners are not valid. - KT-CT-5415: Account user not found. - KT-CT-11103: Business not found. - KT-CT-4123: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SetUpDirectDebitInstructionFromStoredDetailsInput!` |  | Input fields for creating a new direct debit instruction from stored details. |

## `setVehicleChargePreferences(input: VehicleChargingPreferencesInput)`

- Return type: `SetVehicleChargingPreferences`
- Deprecated: Yes (The 'setVehicleChargePreferences' field is deprecated. Please use `setDevicePreferences` instead of this endpoint. - Marked as deprecated on 2024-09-18. - Scheduled for removal on or after 2026-01-26. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/469/)
- Description: Set charging preferences for your electric vehicle. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4321: Serializer validation error. - KT-CT-4353: An error occurred while trying to update your charging preferences. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `VehicleChargingPreferencesInput` |  |  |

## `shareGoodsQuote(input: ShareGoodsQuoteInput!)`

- Return type: `ShareGoodsQuote`
- Description: Share a goods quote. The possible errors that can be raised are: - KT-CT-4122: Invalid email. - KT-CT-8203: Received an invalid quote code. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ShareGoodsQuoteInput!` |  | Input fields for sharing a quote. |

## `startCollectionProcess(input: StartCollectionProcessInput!)`

- Return type: `StartCollectionProcess`
- Description: Start a collection process. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11208: Invalid billing document identifier for collection process. - KT-CT-11209: Collection process configuration does not have published version. - KT-CT-11210: Active collection process for entity already exists. - KT-CT-11211: Too many active collection processes for config. - KT-CT-11212: Invalid collection process config code. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `StartCollectionProcessInput!` |  | Details to start collection process for. |

## `startCustomerVerification(input: StartCustomerVerificationInput!)`

- Return type: `StartCustomerVerification`
- Description: Start the customer verification using the provided verification method. The possible errors that can be raised are: - KT-CT-1701: Brand does not exist. - KT-CT-4194: Verification type not supported yet. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `StartCustomerVerificationInput!` |  |  |

## `startOnSiteJobsAppointmentBookingSession(appointmentBookingDetails: OnSiteJobsAppointmentBookingDetailsInput!, appointmentIdToReschedule: UUID, overrideAppointmentCheckWarnings: Boolean = false, requestId: UUID!)`

- Return type: `StartOnSiteJobsAppointmentBookingSession`
- Description: Start the appointment booking process for an on-site jobs request. The possible errors that can be raised are: - KT-CT-13010: No booking adapter found for agent. - KT-CT-13020: Could not identify agent from property. - KT-CT-13021: Invalid job type. - KT-CT-13022: Work category not found for job type. - KT-CT-13023: Appointment booking checks failed. - KT-CT-13024: Appointment booking checks returned warnings. - KT-CT-13032: Request does not exist. - KT-CT-13054: Appointment not found for rescheduling. - KT-CT-13055: Appointment does not belong to the specified request. - KT-CT-13056: Appointment cannot be rescheduled. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `appointmentBookingDetails` | `OnSiteJobsAppointmentBookingDetailsInput!` |  | The appointment booking details. |
| `appointmentIdToReschedule` | `UUID` |  | The ID of an existing appointment to reschedule. If provided, this booking session will be used to reschedule the appointment instead of creating a new one. |
| `overrideAppointmentCheckWarnings` | `Boolean` | `false` | Whether to override appointment booking check warnings. Defaults to False. |
| `requestId` | `UUID!` |  | The ID of the request to book an appointment for. |

## `startReAuthentication(input: StartReAuthenticationInput!)`

- Return type: `StartReAuthentication`
- Description: Create a wizard for re-authenticating a device with SmartFlex. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4385: Re-authentication is not supported for this device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `StartReAuthenticationInput!` |  |  |

## `startSmartFlexOnboarding(input: StartSmartFlexOnboardingInput!)`

- Return type: `StartSmartFlexOnboarding`
- Description: Create a wizard for onboarding a device with SmartFlex. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4385: Re-authentication is not supported for this device. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `StartSmartFlexOnboardingInput!` |  |  |

## `startTestChargeForSmartFlexOnboarding(input: CompleteSmartFlexOnboardingStepInput!)`

- Return type: `StartTestChargeForSmartFlexOnboarding`
- Deprecated: Yes (The 'startTestChargeForSmartFlexOnboarding' field is deprecated. This functionality will no longer be available. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Attempt to start a test charge. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4371: Onboarding wizard ID is invalid. - KT-CT-4372: Simultaneous attempts to update onboarding process. - KT-CT-4375: Incorrect or missing parameters for SmartFlex onboarding step. - KT-CT-4376: Unable to complete onboarding step. Please try again later. - KT-CT-4377: Invalid onboarding step ID. - KT-CT-4378: Invalid input or step id. Please make sure you are using the correct step id and providing the expected input params. - KT-CT-4379: Vehicle is not ready for a test charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CompleteSmartFlexOnboardingStepInput!` |  |  |

## `stopAutomatedPayments(input: StopAutomatedPaymentsInput!)`

- Return type: `StopAutomatedPayments`
- Description: Set a preference to not collect automated payments. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3968: Preference cannot be set this soon. - KT-CT-3969: Preferences must change on a specific day of the week for weekly schedules. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `StopAutomatedPaymentsInput!` |  |  |

## `storeDirectDebitPaymentMethodDetails(input: StoreDirectDebitPaymentMethodDetailsInput!)`

- Return type: `StoreDirectDebitPaymentMethodDetails`
- Description: Store bank details with the vendor. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3940: Invalid data. - KT-CT-3956: Temporary error occurred. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `StoreDirectDebitPaymentMethodDetailsInput!` |  | Store bank details with the vendor. |

## `storePaymentInstruction(input: StorePaymentInstructionInput!)`

- Return type: `StorePaymentInstruction`
- Description: Store a new payment instruction created through the embedded process. The possible errors that can be raised are: - KT-CT-3820: Received both ledger ID and number. - KT-CT-4177: Unauthorized. - KT-CT-3822: Unauthorized. - KT-CT-3979: Invalid ledger. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `StorePaymentInstructionInput!` |  | Input fields for storing a new payment instruction created through the embedded process. |

## `submitCustomerFeedback(input: CustomerFeedbackInputType!)`

- Return type: `SubmitCustomerFeedback`
- Description: Submit customer feedback. The possible errors that can be raised are: - KT-CT-5514: Unable to submit feedback. - KT-CT-5511: The feedback_id should be provided for feedback source. - KT-CT-5512: The feedback doesn't match the account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CustomerFeedbackInputType!` |  |  |

## `submitGasSelfReading(input: GasSelfReadingSubmissionInput!)`

- Return type: `SubmitGasSelfReading`
- Description: Submit a self-reading for a supply point. The possible errors that can be raised are: - KT-ES-4508: Self-reading input is invalid. - KT-ES-4509: Self-reading submission failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `GasSelfReadingSubmissionInput!` |  | Input fields for submitting a gas self-reading. |

## `submitRepaymentRequest(input: RequestRepaymentInputType!)`

- Return type: `SubmitRepaymentRequest`
- Description: Submit a repayment request. The possible errors that can be raised are: - KT-CT-1132: Unauthorized. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3823: Unauthorized. - KT-CT-3926: Unauthorized. - KT-CT-3927: Invalid Amount. - KT-CT-3928: Idempotency key used for another repayment request. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `RequestRepaymentInputType!` |  | Input fields for requesting a repayment. |

## `suspendControl(input: AccountNumberInput)`

- Return type: `SuspendDeviceControl`
- Deprecated: Yes (The 'suspendControl' field is deprecated. Please use 'updateDeviceSmartControl' instead. - Marked as deprecated on 2024-09-17. - Scheduled for removal on or after 2025-12-11. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/468/)
- Description: Suspend control of the device. The possible errors that can be raised are: - KT-CT-4301: Unable to find device for given account. - KT-CT-4358: Unable to suspend device control. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AccountNumberInput` |  |  |

## `switchAccountToVariablePaymentSchedule(input: SwitchAccountToVariablePaymentScheduleInput!)`

- Return type: `SwitchAccountToVariablePaymentSchedule`
- Description: Switch account to variable payment schedule. Current schedule type will be preserved. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-3921: Account not found. - KT-CT-3922: Ledger not found for the account. - KT-CT-3947: An unexpected error occurred. - KT-CT-3984: Could not delete conflicting future payment schedule. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SwitchAccountToVariablePaymentScheduleInput!` |  | Input fields for switching to a variable payment schedule. |

## `terminateAgreement(input: TerminateAgreementInput!)`

- Return type: `TerminateAgreement`
- Description: Terminate an agreement. The possible errors that can be raised are: - KT-CT-1501: Agreement not found. - KT-CT-1513: Unable to terminate agreement. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TerminateAgreementInput!` |  | Input for terminating an agreement. |

## `terminateContract(input: TerminateContractInput!)`

- Return type: `TerminateContractOutput!`
- Description: Terminate an existing contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10007: Unable to terminate contract. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10013: Requested termination date is invalid. - KT-CT-10022: Contract already terminated. - KT-CT-10023: Contract is already revoked. - KT-CT-10024: Contract already expired. - KT-CT-10025: Contract has not started yet. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TerminateContractInput!` |  |  |

## `terminateCreditTransferPermission(input: TerminateCreditTransferPermissionInput!)`

- Return type: `TerminateCreditTransferPermission`
- Description: Terminate credit transfer permission. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3825: Credit transfer permission not found. - KT-CT-3827: The ledger is not valid. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TerminateCreditTransferPermissionInput!` |  | Input fields for terminating a credit transfer permission. |

## `terminateSolarWalletRelationship(input: TerminateSolarWalletRelationshipType!)`

- Return type: `TerminateSolarWalletRelationship`
- Deprecated: Yes (The 'terminateSolarWalletRelationship' field is deprecated. Use 'terminateCreditTransferPermission' mutation instead. - Marked as deprecated on 2025-02-10. - Scheduled for removal on or after 2025-08-10.)
- Description: Terminate solar wallet sharing credit between a solar wallet credit ledger and spain electricity ledger. The possible errors that can be raised are: - KT-ES-4116: Account not found. - KT-ES-7807: The request to terminate a solar wallet sharing credit between ledgers was incomplete or malformed. - KT-ES-7808: Couldn't stop sharing credit between ledgers because credit sharing ledger doesn't exist. - KT-ES-7809: There is no ledger of this type on this account.. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TerminateSolarWalletRelationshipType!` |  | Input fields for terminaring solar wallet sharing credit between ledgers. |

## `thirdPartyCompleteDeviceRegistration(input: CompleteDeviceRegistrationInput)`

- Return type: `ThirdPartyCompleteDeviceRegistration`
- Deprecated: Yes (The 'thirdPartyCompleteDeviceRegistration' field is deprecated. This functionality will no longer be available. - Marked as deprecated on 2026-01-05. - Scheduled for removal on or after 2026-07-05.)
- Description: Completes the registration of a device if the contract is eligible and the device registration valid. The possible errors that can be raised are: - KT-CT-4321: Serializer validation error. - KT-CT-4322: Unable to complete registration error. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `CompleteDeviceRegistrationInput` |  |  |

## `transferLeadOpportunities(input: TransferLeadOpportunitiesInput!)`

- Return type: `TransferLeadOpportunities`
- Description: Transfer opportunities across leads. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TransferLeadOpportunitiesInput!` |  | Input for transfer opportunities across leads. |

## `transferLedgerBalance(input: TransferLedgerBalanceInputType!)`

- Return type: `TransferLedgerBalance`
- Description: Transfer value from a source ledger to a destination ledger. This decreases the balance of the source ledger by the given amount and increases the balance of the destination ledger by the same amount. If the amount is negative, the effect is reversed (the source ledger's balance increases and the destination ledger's balance decreases). This field requires the `Authorization` header to be set. The possible errors that can be raised are: - KT-CT-3822: Unauthorized. - KT-CT-3823: Unauthorized. - KT-CT-9701: Balance transfer to same account is not allowed. - KT-CT-9702: Balance transfer is not support for debit account with Zero balance. - KT-CT-9703: Balance transfer is not supported for debit account. - KT-CT-9704: Balance transfer amount should be non-zero. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TransferLedgerBalanceInputType!` |  | Input fields for processing an account balance transfer. |

## `transferLoyaltyPointsBetweenUsers(input: TransferLoyaltyPointsBetweenUsersInput!)`

- Return type: `TransferLoyaltyPointsBetweenUsers`
- Description: Transfer Loyalty Point from one account user to another. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9205: Insufficient Loyalty Points. - KT-CT-9204: Negative or zero points set. - KT-CT-9208: Invalid posted at datetime. - KT-CT-9209: Negative Loyalty Points balance. - KT-CT-9210: Unhandled Loyalty Points exception. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TransferLoyaltyPointsBetweenUsersInput!` |  | Input fields for transferring Loyalty Points. |

## `triggerBoostCharge(input: AccountNumberInput)`

- Return type: `PerformBoostCharge`
- Deprecated: Yes (The 'triggerBoostCharge' field is deprecated. Please use 'updateBoostCharge' instead. - Marked as deprecated on 2025-05-12. - Scheduled for removal on or after 2026-01-26. You can read more about this deprecation on: https://announcements.kraken.tech/announcements/public/607/)
- Description: Initiate a boost charge for an electric vehicle (EV). This will start charging the EV and will not stop until the battery reaches 100% charged. If it is not possible to initiate a boost charge, a KT-CT-4357 error will be returned. It may have a `boostChargeRefusalReasons` extension which lists the reasons why the boost charge was refused. Possible reasons include: - `BC_DEVICE_NOT_YET_LIVE` (device is not yet live) - `BC_DEVICE_RETIRED` (device is retired) - `BC_DEVICE_SUSPENDED` (device is suspended) - `BC_DEVICE_DISCONNECTED` (device is disconnected) - `BC_DEVICE_NOT_AT_HOME` (device is not at home) - `BC_BOOST_CHARGE_IN_PROGRESS` (boost charge already in progress) - `BC_DEVICE_FULLY_CHARGED` (device is already fully charged) The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4356: A boost charge cannot currently be performed. - KT-CT-4357: Unable to trigger boost charge. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AccountNumberInput` |  |  |

## `triggerCollectionProcessMessage(input: TriggerCollectionProcessMessageInput!)`

- Return type: `TriggerCollectionProcessMessage`
- Description: Trigger a collection process message with safety checks. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `TriggerCollectionProcessMessageInput!` |  | Input for sending a collection process communication. |

## `triggerPostUploadOperations(s3Key: String!)`

- Return type: `TriggerPostUploadOperations!`
- Description: The possible errors that can be raised are: - KT-CT-8710: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `s3Key` | `String!` |  |  |

## `triggerTestCharge(input: AccountNumberInput)`

- Return type: `PerformTestCharge`
- Description: Initiate a test charge of an electric vehicle (EV). This is to ensure that the EV or EVSE (charge point) can be controlled remotely and successfully charged for a short period. If it is not possible to initiate a test charge, a KT-CT-4355 error will be returned. It may have a `testChargeRefusalReasons` extension which lists the reasons why the test charge was refused. Possible reasons include: - `TC_DEVICE_LIVE` (device is already live) - `TC_DEVICE_ONBOARDING_IN_PROGRESS` (test dispatch already in progress) - `TC_DEVICE_RETIRED` (device is retired) - `TC_DEVICE_SUSPENDED` (device is suspended) - `TC_DEVICE_DISCONNECTED` (device is disconnected) - `TC_DEVICE_ALREADY_CHARGING` (device is already charging) - `TC_DEVICE_AWAY_FROM_HOME` (device is away from home) - `TC_DEVICE_NO_LOCATION_CONFIGURED` (device has no location configured) - `TC_DEVICE_LOCATION_UNABLE_TO_IDENTIFY` (unable to identify device location) - `TC_DEVICE_LOCATION_MISSING` (device location is missing) The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4362: Device not ready for test charge. - KT-CT-4355: Unable to trigger charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AccountNumberInput` |  |  |

## `unenrollAccountFromLoyaltyProgram(input: UnenrollAccountFromLoyaltyProgramInput!)`

- Return type: `UnenrollAccountFromLoyaltyProgram`
- Description: Unenroll users account from Loyalty program. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-9220: Ineligible loyalty points unenrollment. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UnenrollAccountFromLoyaltyProgramInput!` |  | The account number to unenroll from the loyalty program. |

## `unlinkUserFromLine`

- Return type: `UnlinkUserFromLineResponse!`
- Description: Unlink an account user and line together.

## `updateAccountBillingAddress(input: AccountBillingAddressInput!)`

- Return type: `UpdateAccountBillingAddress`
- Description: Update the account billing address. The possible errors that can be raised are: - KT-CT-4145: Invalid address. - KT-CT-7123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AccountBillingAddressInput!` |  | Input variables needed for updating an account billing address. |

## `updateAccountBillingEmail(input: UpdateAccountBillingEmailInput!)`

- Return type: `UpdateAccountBillingEmail`
- Description: Update account billing email. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4122: Invalid email. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAccountBillingEmailInput!` |  | Input fields for updating billing email for an account. |

## `updateAccountConsents(accountNumber: String!, consents: [ConsentInput]!)`

- Return type: `UpdateAccountConsents`
- Description: Update the consents of an account The possible errors that can be raised are: - KT-CT-9014: Duplicate consent. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-9018: Account not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `accountNumber` | `String!` |  | The account number to update consents for. |
| `consents` | `[ConsentInput]!` |  | Consents to update for account. |

## `updateAccountReference(input: AccountReferenceInput!)`

- Return type: `UpdateAccountReference`
- Description: Update an account reference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-8310: Invalid data. - KT-CT-8311: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `AccountReferenceInput!` |  | Input fields for updating an account reference. |

## `updateAccountReferralStatus(input: UpdateAccountReferralStatusInput!)`

- Return type: `UpdateAccountReferralStatus`
- Description: Update the status of an account referral. The possible errors that can be raised are: - KT-CT-6712: Invalid reference. - KT-CT-6732: Invalid referral status transition. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAccountReferralStatusInput!` |  | Input fields for updating the status of an account referral. |

## `updateAccountUser(input: UpdateAccountUserInput)`

- Return type: `UpdateAccountUser`
- Description: Update an account. The possible errors that can be raised are: - KT-ES-5410: Invalid data. - KT-CT-5414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAccountUserInput` |  | Input fields for updating user. |

## `updateAccountUserConsents(consents: [ConsentTypeInput], userNumber: String)`

- Return type: `UpdateAccountUserConsents`
- Description: Update the consents of an account user (the authenticated user) The possible errors that can be raised are: - KT-CT-9014: Duplicate consent. - KT-CT-9016: Consent management not enabled. - KT-CT-9017: Consent type not found. - KT-CT-1111: Unauthorized. - KT-CT-5421: Account user not found. - KT-CT-5422: Invalid data. - KT-CT-1605: Invalid input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `consents` | `[ConsentTypeInput]` |  | Consents to update for account user. |
| `userNumber` | `String` |  | User number of the account user to update consents for. Only needed if the viewer is an organization. |

## `updateActivePurchase(input: UpdatePurchaseInput!)`

- Return type: `UpdateActivePurchase`
- Description: Update an active purchase. The possible errors that can be raised are: - KT-CT-8225: Received an invalid purchaseId. - KT-CT-8226: The provided purchase is not active. - KT-CT-8206: Invalid data. - KT-CT-8227: Available grants could not be applied. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdatePurchaseInput!` |  | Input fields for updating an active purchase. |

## `updateAffiliateLink(input: UpdateAffiliateLinkInputType!)`

- Return type: `UpdateAffiliateLink!`
- Description: Update an existing affiliate link. The possible errors that can be raised are: - KT-CT-7711: Invalid data. - KT-CT-7713: Invalid data. - KT-CT-7714: Invalid data. - KT-CT-7715: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAffiliateLinkInputType!` |  | Input fields for Updating an existing affiliate link. |

## `updateAffiliateOrganisation(input: UpdateAffiliateOrganisationInputType!)`

- Return type: `UpdateAffiliateOrganisation!`
- Description: Update an existing affiliate organisation. The possible errors that can be raised are: - KT-CT-7717: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAffiliateOrganisationInputType!` |  | Input fields for Updating an existing affiliate organisation. |

## `updateAgentAuxiliaryStatus(input: UpdateAgentAuxiliaryStatusInput!)`

- Return type: `UpdateAgentAuxiliaryStatus`
- Description: The possible errors that can be raised are: - KT-CT-7813: Support user not found with that username. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAgentAuxiliaryStatusInput!` |  | The input data for this mutation. |

## `updateAgreementPeriod(input: UpdateAgreementPeriodInput!)`

- Return type: `UpdateAgreementPeriod`
- Description: Update the period of an agreement. The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-1501: Agreement not found. - KT-CT-1503: Agreement valid_to date must be later than valid_from date. - KT-CT-1504: Account does not match with the agreement. - KT-CT-1505: Unable to edit agreement. - KT-CT-1506: Agreement period is not within the supply and property period. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAgreementPeriodInput!` |  | Input for updating the agreement period. |

## `updateAgreementRescission(input: UpdateAgreementRescissionInput!)`

- Return type: `UpdateAgreementRescission`
- Description: Update an agreement rescission. The possible errors that can be raised are: - KT-CT-14101: Agreement rescission not found. - KT-CT-14102: Cannot update completed agreement rescission. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAgreementRescissionInput!` |  | Input fields for updating an agreement rescission. |

## `updateAgreementRollover(input: UpdateAgreementRolloverInput!)`

- Return type: `UpdateAgreementRollover`
- Description: Update an agreement rollover. The possible errors that can be raised are: - KT-CT-4910: No product exists with the given input. - KT-CT-13705: Agreement rollover not found. - KT-CT-13706: Agreement rollover has an invalid status for this operation. - KT-CT-13707: Agreement rollover has an invalid type for this operation. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAgreementRolloverInput!` |  | Input for updating an agreement rollover. |

## `updateApiException(input: UpdateAPIExceptionInput!)`

- Return type: `UpdateAPIException`
- Description: Mutation to update an existing APIException instance. The possible errors that can be raised are: - KT-CT-7804: No fields present in the input for updating the APIException. - KT-CT-7803: Received an invalid apiExceptionId. - KT-CT-7809: Update results in no changes to API Exception. - KT-CT-7805: Too many tags associated with this API Exception. - KT-CT-7806: Cannot create duplicate tags for the same API exception. - KT-CT-7801: Received an invalid operationsTeamId. - KT-CT-7811: Received an invalid assignedUserId. - KT-CT-7812: Support user is inactive. - KT-CT-7814: Received an invalid accountNumber. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAPIExceptionInput!` |  | Input fields for updating an API exception. |

## `updateApiExceptionNote(input: UpdateAPIExceptionNoteInput!)`

- Return type: `UpdateAPIExceptionNote`
- Description: Mutation to update an existing APIExceptionNote instance. The possible errors that can be raised are: - KT-CT-7807: Received an invalid apiExceptionNoteId. - KT-CT-7808: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAPIExceptionNoteInput!` |  | Input fields for creating an API exception note. |

## `updateAutoTopUpAmount(input: UpdateAutoTopUpAmountInput!)`

- Return type: `UpdateAutoTopUpAmount`
- Description: Change the auto top up amount for the payment schedule. The possible errors that can be raised are: - KT-CT-3815: No active payment schedule found for this account. - KT-CT-3941: Invalid data. - KT-CT-3942: An unexpected error occurred. - KT-CT-3947: An unexpected error occurred. - KT-CT-3953: The payment schedule is not a balance triggered schedule. - KT-CT-3820: Received both ledger ID and number. - KT-CT-3821: Received neither ledger ID nor ledger number. - KT-CT-3822: Unauthorized. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAutoTopUpAmountInput!` |  | Input fields for updating the auto-top-up amount for a schedule. |

## `updateBillingAddress(input: UpdateAccountBillingAddressInput)`

- Return type: `UpdateBillingAddress`
- Description: Updates billing address details. The possible errors that can be raised are: - KT-ES-4118: Invalid data. - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAccountBillingAddressInput` |  |  |

## `updateBillingDetails(input: UpdateAccountBillingDetailsInput)`

- Return type: `UpdateBillingDetails`
- Description: Updates billing details. The possible errors that can be raised are: - KT-ES-4119: Invalid data. - KT-ES-1130: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAccountBillingDetailsInput` |  |  |

## `updateBoostCharge(input: UpdateBoostChargeInput)`

- Return type: `SmartFlexDeviceInterface`
- Description: Update the boost charge for a specific device. If it is not possible to initiate a boost charge, a KT-CT-4357 error will be returned. It may have a `boostChargeRefusalReasons` extension which lists the reasons why the boost charge was refused. Possible reasons include: - `BC_DEVICE_NOT_YET_LIVE` (device is not yet live) - `BC_DEVICE_RETIRED` (device is retired) - `BC_DEVICE_SUSPENDED` (device is suspended) - `BC_DEVICE_DISCONNECTED` (device is disconnected) - `BC_DEVICE_NOT_AT_HOME` (device is not at home) - `BC_BOOST_CHARGE_IN_PROGRESS` (boost charge already in progress) - `BC_DEVICE_FULLY_CHARGED` (device is already fully charged) The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4354: Unable to cancel boost charge. - KT-CT-4356: A boost charge cannot currently be performed. - KT-CT-4357: Unable to trigger boost charge. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateBoostChargeInput` |  |  |

## `updateCollectionProcessRecordToActive(input: UpdateCollectionProcessRecordToActiveInputType!)`

- Return type: `UpdateCollectionProcessRecordToActive`
- Description: Update the Collection Process Record from raised status to active. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11202: No External reference provided. - KT-CT-11207: Unsupported external source for collection process. - KT-CT-11218: External reference cannot be updated once it has been set. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateCollectionProcessRecordToActiveInputType!` |  | Input variables needed for making a collection process record active. |

## `updateCollectionProcessRecordToComplete(input: UpdateCollectionProcessRecordToCompleteInputType!)`

- Return type: `UpdateCollectionProcessRecordToComplete`
- Description: Update the Collection Process Record from raised status to complete. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-11201: No Collection Process Records associated with id. - KT-CT-11203: No Completion reason provided. - KT-CT-11204: No Completion details provided. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateCollectionProcessRecordToCompleteInputType!` |  | Input variables needed for making a collection process record complete. |

## `updateCommsDeliveryPreference(input: UpdateCommsDeliveryPreferenceInput!)`

- Return type: `UpdateCommsDeliveryPreference`
- Description: Update account communication delivery preference. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-4136: Cannot set comms preference to email when account has no email. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateCommsDeliveryPreferenceInput!` |  | Input fields for updating comms delivery preferences for an account. |

## `updateCommsPreferences(input: UpdateAccountUserCommsPreferencesMutationInput!)`

- Return type: `UpdateAccountUserCommsPreferencesMutationPayload`
- Description: Update the comms preferences of the account user (the authenticated user).

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAccountUserCommsPreferencesMutationInput!` |  |  |

## `updateDcaProceeding(input: UpdateDCAProceedingInputType!)`

- Return type: `UpdateDCAProceeding`
- Description: Update the status of a DCA proceeding. The possible errors that can be raised are: - KT-CT-11610: unable to edit the debt collection proceeding. - KT-CT-11604: Active debt collection proceeding does not exist for account. - KT-CT-11605: Multiple active Proceeding's found for same agency and campaign on account. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateDCAProceedingInputType!` |  |  |

## `updateDeviceGridExport(input: UpdateDeviceGridExportInput)`

- Return type: `SmartFlexDeviceInterface`
- Description: Update the grid export preference for a device. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4386: An error occurred while trying to update your device's grid export status. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateDeviceGridExportInput` |  |  |

## `updateDeviceSmartControl(input: SmartControlInput!)`

- Return type: `SmartFlexDeviceInterface`
- Description: Suspends or resumes the smart control of a specific device. For some devices, this will also adjust smart control of related devices. e.g. suspending one zone in a multi-zone heat pump system will suspend all zones in that system. The possible errors that can be raised are: - KT-CT-4313: Could not find KrakenFlex device. - KT-CT-4314: Unable to get provider details. - KT-CT-4387: Could not find the KrakenFlex controller device. - KT-CT-4358: Unable to suspend device control. - KT-CT-4359: Unable to resume device control. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `SmartControlInput!` |  | The input to action the desired device control, i.e. suspend or unsuspend a device. |

## `updateDocumentAccessibilityPreference(input: UpdateDocumentAccessibilityPreferenceInput!)`

- Return type: `UpdateDocumentAccessibilityPreference!`
- Description: Update the document accessibility preference for an account. The possible errors that can be raised are: - KT-CT-4123: Unauthorized. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateDocumentAccessibilityPreferenceInput!` |  | Input fields for updating document accessibility preference for an account. |

## `updateIsChargingDurationCapped(input: UpdateIsChargingDurationCappedInput)`

- Return type: `SmartFlexDeviceInterface`
- Description: Update the charging duration cap preference for a device. The possible errors that can be raised are: - KT-CT-1111: Unauthorized. - KT-CT-4389: An error occurred while trying to update your device's isChargingDurationCapped setting. - KT-CT-4390: An error occurred while trying to update your device's preference. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateIsChargingDurationCappedInput` |  | Input fields for updating the charging duration cap preference. |

## `updateLeadAssignment(input: UpdateLeadAssignmentInput!)`

- Return type: `UpdateLeadAssignment`
- Description: Update assignment fields for a Lead. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateLeadAssignmentInput!` |  | Fields for updating a lead assignment. |

## `updateLeadDetails(input: UpdateLeadDetailsInput!)`

- Return type: `UpdateLeadDetails`
- Description: Update the details of a lead. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-8912: Funnel not found. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8935: National ID bad input. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateLeadDetailsInput!` |  | Fields for updating a lead's details. |

## `updateLeadStage(input: UpdateLeadStageInput!)`

- Return type: `UpdateLeadStage`
- Description: Update the stage of a lead. The possible errors that can be raised are: - KT-CT-8907: Lead not found. - KT-CT-8914: Stage not found. - KT-CT-8915: Stages are not in the same funnel. - KT-CT-8916: Current stage mismatch. - KT-CT-8917: Stage transition not allowed. - KT-CT-8918: Stage precondition not met. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateLeadStageInput!` |  | Fields for updating a lead's stage. |

## `updateLeaveSupplier(input: UpdateLeaveSupplierInput!)`

- Return type: `LeaveSupplierUpdated!`
- Description: Update an existing leave supplier process. The possible errors that can be raised are: - KT-CT-10304: Mutation not enabled in this environment. - KT-CT-10302: Invalid data. - KT-CT-10309: Failed to update leave supplier process - the service is not enabled. - KT-CT-10310: Failed to update leave supplier process. The process status is not in updatable status. - KT-CT-1607: Value cannot be empty. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateLeaveSupplierInput!` |  |  |

## `updateMessageTags(input: UpdateMessageTagsInput)`

- Return type: `UpdateMessageTags`
- Description: The possible errors that can be raised are: - KT-CT-7611: The message was not found. - KT-CT-7614: The Ink tag was not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateMessageTagsInput` |  |  |

## `updateMetadata(input: MetadataInput!)`

- Return type: `UpdateMetadata`
- Description: Update metadata on an object. The possible errors that can be raised are: - KT-CT-4323: Unauthorized. - KT-CT-8413: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `MetadataInput!` |  | Input fields for updating metadata. |

## `updateNotesOnOpportunity(input: UpdateNotesOnOpportunityInput!)`

- Return type: `UpdateNotesOnOpportunity`
- Description: Update the notes of an opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateNotesOnOpportunityInput!` |  | Input to update the note on an opportunity. |

## `updateOfferGroupOnOpportunity(input: UpdateOfferGroupOnOpportunityInput!)`

- Return type: `UpdateOfferGroupOnOpportunity`
- Description: Update the offer group of an opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateOfferGroupOnOpportunityInput!` |  | Input to update the offer group on an opportunity. |

## `updateOnSiteJobsAppointment(input: OnSiteJobsUpdateAppointmentInput!)`

- Return type: `UpdateOnSiteJobsAppointment`
- Description: Update an Appointment. The possible errors that can be raised are: - KT-CT-13001: Appointment does not exist. - KT-CT-13043: Cannot update appointment as it has terminal status. - KT-CT-13044: Failed to update appointment slot. - KT-CT-13018: Unable to record cancellation_category/cancellation_sub_category. - KT-CT-13039: Cancellation fields require CANCELLED status. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-13062: Datetime field must be timezone-aware. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `OnSiteJobsUpdateAppointmentInput!` |  | The appointment and its details to update. |

## `updateOnSiteJobsRequest(input: OnSiteJobsUpdateRequestInput!)`

- Return type: `UpdateOnSiteJobsRequest`
- Description: Update an On Site Jobs Request. The possible errors that can be raised are: - KT-CT-13032: Request does not exist. - KT-CT-13035: Request is inactive. - KT-CT-13038: Invalid request status. - KT-CT-13040: Agent not set on request. - KT-CT-13045: Failed to update appointment assets. - KT-CT-13050: Cannot provide both supply_point_identifier_to_market_name_mapping and supply_point_internal_id when creating assets. - KT-CT-13051: Supply point not found when creating assets. - KT-CT-13052: Multiple supply points found when creating assets. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `OnSiteJobsUpdateRequestInput!` |  | The input objects required to update a Request. |

## `updateOpportunityAssignment(input: UpdateOpportunityAssignmentInput!)`

- Return type: `UpdateOpportunityAssignment`
- Description: Update assignment fields for an Opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8903: Unable to update opportunity. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateOpportunityAssignmentInput!` |  | Input fields for creating an opportunity. |

## `updateOpportunityDetails(input: UpdateOpportunityDetailsInput!)`

- Return type: `UpdateOpportunityDetails`
- Description: Update the details of an opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8930: Unable to parse address. - KT-CT-8931: Extra detail value is invalid. - KT-CT-8912: Funnel not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateOpportunityDetailsInput!` |  | Input fields for updating the address of a opportunity. |

## `updateOpportunityExtraDetails(input: UpdateExtraDetailsInput!)`

- Return type: `UpdateOpportunityExtraDetails`
- Description: Update the extra details of a opportunity. The possible errors that can be raised are: - KT-CT-8906: Opportunity not found. - KT-CT-8926: Unable to create opportunity. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateExtraDetailsInput!` |  | Input fields for updating the extra details of a opportunity. |

## `updateOpportunityStage(input: UpdateOpportunityStageInput!)`

- Return type: `UpdateOpportunityStage`
- Description: Update the stage of a opportunity. The possible errors that can be raised are: - KT-CT-8903: Unable to update opportunity. - KT-CT-8910: Received opportunity current stage is not valid. - KT-CT-8914: Stage not found. - KT-CT-8915: Stages are not in the same funnel. - KT-CT-8916: Current stage mismatch. - KT-CT-8917: Stage transition not allowed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateOpportunityStageInput!` |  | Input fields for updating the state of a opportunity. |

## `updatePassword(input: UpdatePasswordInput)`

- Return type: `UpdatePassword`
- Description: Update password of the authenticated user This field requires the `Authorization` header to be set. The possible errors that can be raised are: - KT-CT-5460: Old password is invalid. - KT-CT-5450: Password is invalid. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdatePasswordInput` |  |  |

## `updatePaymentDetails(newPaymentDetails: UpdateAccountPaymentInput)`

- Return type: `UpdatePaymentDetails`
- Description: Updates payment details. The possible errors that can be raised are: - KT-ES-4120: Invalid data. - KT-ES-1130: Unauthorized. - KT-ES-3910: Payment instruction couldn't be created or was cancelled. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `newPaymentDetails` | `UpdateAccountPaymentInput` |  |  |

## `updateProductPrices(input: UpdateProductPricesInput!)`

- Return type: `UpdateProductPricesOutput!`
- Description: Update the prices of a product. The possible errors that can be raised are: - KT-CT-12008: Unable to find the product. - KT-CT-12009: Specified product does not have a specification. - KT-CT-12010: Unable to find the product's specification. - KT-CT-12011: The list of provided prices contains validation errors. - KT-CT-12012: Product prices start date is in the past. - KT-CT-12013: Product prices would overwrite existing prices. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateProductPricesInput!` |  |  |

## `updateSiteworksRequest(input: UpdateSiteworksRequestInputType!)`

- Return type: `UpdateSiteworksRequest`
- Deprecated: Yes (The 'updateSiteworksRequest' field is deprecated. Please use updateOnSiteJobsRequest instead. - Marked as deprecated on 2026-03-01. - Scheduled for removal on or after 2026-09-01.)
- Description: Update a Request. The possible errors that can be raised are: - KT-CT-4231: Unauthorized. - KT-CT-4232: Status passed is not valid. - KT-CT-4233: Request does not exist. - KT-CT-4234: Terminated Request cannot be updated. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateSiteworksRequestInputType!` |  | The input objects required to update a Request. |

## `updateUser(input: UpdateUserInput!)`

- Return type: `UpdateUserMutation`
- Description: Update the account user details of the authenticated user. Only one name field can be updated per day, other fields can be updated freely. This prevents users from switching accounts to someone else (usually when moving homes). All account changes should be handled by operations or the move out journey. New customers are exempt from this rule for the first 31 days. This field requires the `Authorization` header to be set. The possible errors that can be raised are: - KT-CT-5413: Invalid data. - KT-CT-5414: Invalid data. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateUserInput!` |  | Input fields for updating user. |

## `updateUserDetails(input: UpdateAccountUserMutationInput!)`

- Return type: `UpdateAccountUserMutationPayload`
- Deprecated: Yes (The 'updateUserDetails' field is deprecated. Please use the 'updateUser' mutation instead. - Marked as deprecated on 2020-10-02. - Scheduled for removal on or after 2023-04-06.)
- Description: **DEPRECATED: Please use updateUser instead** Update the account user details of the authenticated user. Only one field can be updated per day. This prevents users from switching accounts to someone else (usually when moving homes) All account changes should be handled by operations or the move out journey. New customers are exempt from this rule for the first 31 days.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `UpdateAccountUserMutationInput!` |  |  |

## `validateEmail(input: ValidateEmailInput!)`

- Return type: `ValidateEmail`
- Description: Validate user's email address.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ValidateEmailInput!` |  |  |

## `validateMfaDevice(input: ValidateMfaDeviceInputType!)`

- Return type: `ValidateMfaDevice`
- Description: Validate MFA Device for user. The possible errors that can be raised are: - KT-CT-1150: MFA device not found. - KT-CT-1151: MFA device not found. - KT-CT-1152: Invalid MFA token. - KT-CT-1155: Enabled backup device is needed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ValidateMfaDeviceInputType!` |  | Input fields for validating a new multi-factor authentication device for the logged user. |

## `validatePhone(input: ValidatePhoneNumberInput!)`

- Return type: `ValidatePhone`
- Description: Validate user's phone number.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `ValidatePhoneNumberInput!` |  |  |

## `varyContractTerms(input: VaryContractTermsInput!)`

- Return type: `VaryContractTermsOutput!`
- Description: Vary the terms of a contract. The possible errors that can be raised are: - KT-CT-10003: Contract not found. - KT-CT-10008: The contract is currently undergoing an active journey. - KT-CT-10011: Unable to vary contract terms. - KT-CT-10033: Unable to save term. - KT-CT-10012: Contract variation implies breach. - KT-CT-10034: Unknown contract journey type. - KT-CT-10035: Cannot process a non-active contract journey. - KT-CT-10036: The contract journey manager is not found. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `VaryContractTermsInput!` |  |  |

## `verifyCustomer(input: VerifyCustomerInput!)`

- Return type: `VerifyCustomer`
- Description: Verify a customer using the provided verification code and type. The possible errors that can be raised are: - KT-CT-4191: Error while verifying the customer. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `VerifyCustomerInput!` |  |  |

## `verifyEmail(input: VerifyEmailInput!)`

- Return type: `VerifyEmail`
- Description: Verify user's email address. The possible errors that can be raised are: - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `VerifyEmailInput!` |  |  |

## `verifyIdentity(input: VerifyIdentityInput!)`

- Return type: `VerifyIdentity`
- Description: Provide identifying information about an account and user to get a scoped token that will permit access to associate an email address with the account's user. The possible errors that can be raised are: - KT-CT-1145: Account/user details do not match. - KT-CT-1113: Disabled GraphQL field requested.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `VerifyIdentityInput!` |  | Details about the user to be verified. |

## `withdrawDunning(input: WithdrawDunningInputType!)`

- Return type: `WithdrawDunning`
- Description: Withdraw a dunning process for an account The possible errors that can be raised are: - KT-CT-4178: No account found with given account number. - KT-CT-11301: Account not in a dunning process for the given path name. - KT-CT-11302: No active dunning process found. - KT-CT-11303: Multiple active dunning processes found. - KT-CT-11306: Withdrawing the dunning process failed. - KT-CT-1113: Disabled GraphQL field requested. - KT-CT-1111: Unauthorized. - KT-CT-1112: 'Authorization' header not provided.

| Arg | Type | Default | Description |
|---|---|---|---|
| `input` | `WithdrawDunningInputType!` |  | Input variables needed for withdrawing a dunning process for an account. |

