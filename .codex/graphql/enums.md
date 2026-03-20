# Enums

Total `ENUM` types: **212**

## `APIBrownoutStatus`

Possible API Brownout statuses.

| Value | Deprecated | Description |
|---|---|---|
| `SCHEDULED` | No |  |
| `IN_PROGRESS` | No |  |
| `CANCELLED` | No |  |
| `COMPLETED` | No |  |
| `ABORTED` | No |  |

## `APIExceptionCategories`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ACCOUNT` | No |  |
| `UNKNOWN` | No |  |

## `APIExceptionPriority`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `LOW` | No |  |
| `MEDIUM` | No |  |
| `HIGH` | No |  |

## `APIExceptionResolutionStatus`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ASSIGNED` | No |  |
| `CANCELLED` | No |  |
| `IN_PROGRESS` | No |  |
| `RESOLVED` | No |  |
| `UNASSIGNED` | No |  |
| `UNSUCCESSFUL` | No |  |
| `WAITING_ON_THIRD_PARTY` | No |  |

## `APIExceptionResolutionType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `AUTOMATIC` | No |  |
| `MANUAL` | No |  |
| `UNASSIGNED` | No |  |

## `APIExceptionTags`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `MOVE_IN` | No |  |
| `MOVE_OUT` | No |  |
| `PRODUCT_UPDATE` | No |  |

## `APIType`

Possible API types.

| Value | Deprecated | Description |
|---|---|---|
| `GRAPHQL` | No |  |
| `REST` | No |  |

## `ATRType`

The ATR contract type.

| Value | Deprecated | Description |
|---|---|---|
| `ANNUAL` | No | Anual. |
| `EVENTUAL` | No | Eventual Medido. |
| `SEASONAL` | No | Temporada. |
| `RECORE_SUPPLY` | No | Suministro a instalaciones RECORE. |
| `WORKS_SUPPLY` | No | Suministro de Obras. |
| `RELIEF_SUPPLY` | No | Suministro de Socorro. |
| `EVENTUAL_LUMP_SUM` | No | Eventual a tanto alzado. |
| `TESTING` | No | Pruebas. |
| `DUPLICATE` | No | Duplicado. |
| `STAND_BY` | No | De reserva. |

## `AccountApplicationStatus`

| Value | Deprecated | Description |
|---|---|---|
| `CURRENT` | No |  |
| `FAILED` | No |  |
| `HISTORIC` | No |  |
| `WITHDRAWN` | No |  |

## `AccountBillingOptionsPeriodLength`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `MONTHLY` | No | Monthly |
| `QUARTERLY` | No | Quarterly |

## `AccountCreditReasonType`

Please note: these labels are exposed in the API documentation.

| Value | Deprecated | Description |
|---|---|---|
| `EXTERNAL_REFERRAL_CREDIT` | No | External referral credit |

## `AccountEventType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `EMAIL_SENT` | No | The email messages that were sent by the account. |
| `EMAIL_RECEIVED` | No | The email messages that were received by the account. |
| `MARKETING_EMAIL_SENT` | No | The marketing email messages that were sent by the account. |
| `PRINT_SENT` | No | The print messages that were sent to the print partner by the account. |
| `PRINT_FAILED` | No | The print messages that failed to be delivered. |
| `PRINT_RETURNED` | No | The print messages that were returned to sender. |
| `PRINT_CANCELLED` | No | The print messages that were cancelled. |
| `PRINT_SUCCEEDED` | No | The print messages that were sent by the print partner. |
| `SMS_SENT` | No | The SMS messages that were sent by the account. |
| `SMS_RECEIVED` | No | The SMS messages that were received by the account. |

## `AccountPaymentStatusOptions`

The current status of the payment. Note: REQUESTED payments are excluded by default.

| Value | Deprecated | Description |
|---|---|---|
| `SCHEDULED` | No | The payment has been scheduled for collection and the customer has been notified. While a payment is scheduled, it can still be deleted. |
| `PENDING` | No | The payment has been submitted. From this point it cannot be altered. |
| `CLEARED` | No | The payment has been approved by the merchant and added to your Kraken account. |
| `FAILED` | No | The payment failed permanently. |
| `PROMISED` | No | A payment promise has been created, but it has not left the customers bank account. |
| `FULFILLED` | No | The payment has been made successfully and applied to the Kraken balance. |
| `PROMISE_BROKEN` | No | The payment promise has been broken. |
| `HISTORIC` | No | Payments made in a previous system and then imported into Kraken. |
| `THIRD_PARTY` | No | Third Party payments are those recorded for financial purposes in a different system but should be added to statements. |
| `REQUESTED` | No | The initial state of a payment in Kraken. It should be scheduled with a payment vendor in the future. |
| `DELETED` | No | This payment was deleted. From this point it cannot be altered. |

## `AccountPaymentTransactionTypeChoices`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `DD_FIRST_COLLECTION` | No |  |
| `DD_REGULAR_COLLECTION` | No |  |
| `DD_RE_PRESENTATION` | No |  |
| `DD_FINAL_COLLECTION` | No |  |
| `CREDIT_CARD` | No |  |
| `DEBIT_CARD` | No |  |
| `PREPAID_CARD` | No |  |
| `AGENCY` | No |  |
| `AUSTRALIA_POST` | No |  |
| `BACS_DEPOSIT` | No |  |
| `BPAY` | No |  |
| `BPOINT` | No |  |
| `BRISTOL_POUND` | No |  |
| `BTRE` | No |  |
| `CASH` | No |  |
| `CENTREPAY` | No |  |
| `CHEQUE` | No |  |
| `DESKTOP_DEPOSIT` | No |  |
| `EAPA_VOUCHER` | No |  |
| `EBOX` | No |  |
| `EFT` | No |  |
| `ERRONEOUS_PAYMENT` | No |  |
| `FUEL_DIRECT` | No |  |
| `HEEAS` | No |  |
| `IVR` | No |  |
| `MONEYGRAM` | No |  |
| `PAYPAL` | No |  |
| `SERVICE_TICKET` | No |  |
| `SOCIAL_WELFARE_PAYMENT` | No |  |
| `TELPAY` | No |  |
| `TRANSFER_FROM_SAP` | No |  |
| `URGS` | No |  |
| `WALMART_CASH` | No |  |
| `PAYPOINT_CASH` | No |  |
| `PAYPOINT_CARD` | No |  |
| `PAYPOINT_CHEQUE` | No |  |
| `ALLPAY_CASH` | No |  |
| `ALLPAY_CARD` | No |  |
| `ALLPAY_CHEQUE` | No |  |
| `PAYZONE` | No |  |
| `DWP` | No |  |
| `POST_OFFICE_CASH` | No |  |
| `POST_OFFICE_CHEQUE` | No |  |
| `POST_OFFICE_SAVINGS_STAMPS` | No |  |
| `POST_OFFICE_CARD` | No |  |
| `DCA_COLLECTION` | No |  |
| `PREPAY_KEY` | No |  |
| `PREPAY_CARD` | No |  |
| `PREPAY_TOKEN` | No |  |
| `PREPAY_SMART` | No |  |
| `PAYMENT_FEE` | No |  |
| `FAILED_REPAYMENT_REVERSAL` | No |  |
| `KONBINI` | No |  |
| `PAGOPA_NOTICE` | No |  |
| `IDEAL` | No |  |
| `UNKNOWN` | No |  |

## `AccountReminderTypes`

Contains reminder type choices for all territories.

| Value | Deprecated | Description |
|---|---|---|
| `AD_HOC` | No |  |
| `GBR_ADD_PHOTO_TO_METER_READING` | No |  |
| `GBR_GET_PHOTO_OF_METER_AND_CALL_SUPPLIER` | No |  |
| `GBR_RAISE_DISPUTE` | No |  |
| `GBR_VERIFY_MHHS_MESSAGE` | No |  |
| `JPN_MULTIPLE_VALID_REFERRALS` | No |  |
| `JPN_FAILED_TO_SEND_SMS_FOR_BILLING_INFO` | No |  |
| `JPN_FAILED_TO_SEND_SMS_FOR_CONVENIENCE_STORE_PAYMENT` | No |  |
| `JPN_SWITCH_IN_SCHEDULE_OVERLAP` | No |  |
| `ITA_ACCOUNT_WITHDRAWN_WITHOUT_NOTIFICATION` | No |  |
| `ITA_PROCESS_WELCOME_PACK_STEP` | No |  |
| `AUS_EMBEDDED_CHILD_NMIS` | No |  |
| `FOLLOW_UP_PAYMENT_PROMISE` | No |  |
| `DUNNING_REMINDER` | No |  |
| `WITHDRAWAL_RECEIVED` | No |  |
| `CHURN_PREVENTION` | No |  |
| `PLANNED_INTERRUPTION` | No |  |
| `PLANNED_INTERRUPTION_MEDICAL_DEPENDENCY` | No |  |
| `MOVE_IN_MOVE_OUT_MANUAL_PROCESS` | No |  |
| `MOVE_IN_CES_LIFE_SUPPORT_REQUIRED` | No |  |
| `MOVE_IN_DEFAULT_PAYMENT_SCHEDULE_FAILED` | No |  |
| `CANCEL_MOVE_OUT_UNABLE_TO_REINSTATE_FUTURE_AGREEMENTS` | No |  |
| `COS_GAIN` | No |  |
| `COS_LOSS` | No |  |
| `MOVE_IN` | No |  |
| `MOVE_OUT` | No |  |
| `AMPERAGE_CHANGE` | No |  |
| `CUSTOMER_DETAILS_CHANGE` | No |  |
| `BILLING` | No |  |
| `INDUSTRY_CUSTOMER_TRANSFER_DELAYED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_OF_SUPPLIER_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_OF_SUPPLIER_CANCELLED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_OF_SUPPLIER_OBJECTED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_OF_SUPPLIER_CONFLICTING_PERIOD` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_OBJECTED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_CANCELLED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_OBJECTION_MISSING_ACK` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_WITHDRAWAL_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_OBJECTION_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_OBJECTION_WITHDRAWAL_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_UNABLE_TO_PROCESS_ROLR` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_OF_SUPPLIER_GAIN_COMPLETION_OVERDUE` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_COMPLETED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_CANCELLATION_FAILED` | No |  |
| `INDUSTRY_EXCEPTION_CHANGE_REQUEST_UNABLE_TO_WITHDRAW` | No |  |
| `INDUSTRY_EXCEPTION_SITE_ACCESS_DETAILS_REQUEST_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_SITE_ACCESS_DETAILS_NOTIFICATION_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_SITE_ACCESS_DETAILS_NOTIFICATION_MISSING_BUSINESS_ACCEPTANCE` | No |  |
| `INDUSTRY_MANUAL_CUSTOMER_DETAILS_NOTIFICATION_REQUIRED` | No |  |
| `INDUSTRY_EXCEPTION_CUSTOMER_DETAILS_NOTIFICATION_MISSING_BUSINESS_ACCEPTANCE` | No |  |
| `INDUSTRY_EXCEPTION_CUSTOMER_DETAILS_NOTIFICATION_MISSING_MANDATORY_FIELDS` | No |  |
| `INDUSTRY_EXCEPTION_CUSTOMER_DETAILS_NOTIFICATION_INVALID_BILLING_ADDRESS` | No |  |
| `INDUSTRY_EXCEPTION_CUSTOMER_DETAILS_REQUEST_SPECIAL_REASON` | No |  |
| `INDUSTRY_EXCEPTION_CUSTOMER_DETAILS_REQUEST_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_CUSTOMER_DETAILS_REQUEST_MISSING_BUSINESS_ACCEPTANCE` | No |  |
| `INDUSTRY_EXCEPTION_CUSTOMER_DETAILS_NOTIFICATION_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_MULTIPLE_ACCOUNTS_MATCHES` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_MULTIPLE_LIFE_SUPPORT_CONTACT_MATCHES` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_FAILED_TO_SEND` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_UNKNOWN_CONTACT` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_INVALID_PHONE` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_INVALID_CONTACT_METHOD` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_RECEIVED_FROM_NON_REGISTRATION_OWNER` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_CONTAINS_UNEXPECTED_DATA` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_REQUEST_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_REJECTED` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_REQUEST_MISSING_BUSINESS_ACCEPTANCE` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_MISSING_BUSINESS_ACCEPTANCE` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_REQUEST_MISSING_LIFE_SUPPORT_NOTIFICATION` | No |  |
| `INDUSTRY_EXCEPTION_LIFE_SUPPORT_CONTACT_USER_REMOVED_FROM_ACCOUNT` | No |  |
| `INDUSTRY_MANUAL_ACTION_REQUIRED` | No |  |
| `INDUSTRY_MANUAL_LIFE_SUPPORT_NOTIFICATION_REQUIRED` | No |  |
| `INDUSTRY_VIC_DRO_MANUAL_LIFE_SUPPORT_EXTENSION_REQUEST` | No |  |
| `INDUSTRY_EXCEPTION_FAILED_TO_CANCEL_DEENERGISATION_SERVICE_ORDER` | No |  |
| `INDUSTRY_EXCEPTION_HOUSE_MOVE_ENROLMENT_SERVICE_ORDER_ALREADY_IN_PROGRESS` | No |  |
| `INDUSTRY_EXCEPTION_HOUSE_MOVE_ENROLMENT_UNABLE_TO_COPY_LAST_METER_READING` | No |  |
| `INDUSTRY_EXCEPTION_HOUSE_MOVE_ENROLMENT_CANNOT_CALCULATE_MOVE_IN_READING` | No |  |
| `INDUSTRY_EXCEPTION_HOUSE_MOVE_OUT_CANNOT_CALCULATE_MOVE_OUT_READING` | No |  |
| `INDUSTRY_EXCEPTION_METER_POINT_ENROLMENT_INCOMPLETE_COULD_NOT_SEND_SERVICE_ORDER` | No |  |
| `INDUSTRY_EXCEPTION_UNABLE_TO_ENROL_METER_POINT_INCOMPLETE_COULD_NOT_SEND_CHANGE_REQUEST` | No |  |
| `INDUSTRY_EXCEPTION_UNABLE_TO_ENROL_METER_POINT_NEXT_SCHEDULED_READ_DATE_PAST` | No |  |
| `INDUSTRY_EXCEPTION_RELINKING_OCCURRED_DURING_SDR_SYNC` | No |  |
| `INDUSTRY_SEND_LIFE_SUPPORT_DE_REGISTRATION_FORM` | No |  |
| `INDUSTRY_LIFE_SUPPORT_MANUAL_BEST_ENDEAVOUR_REQUIRED` | No |  |
| `INDUSTRY_LIFE_SUPPORT_REVIEW_DEREGISTRATION` | No |  |
| `INDUSTRY_LIFE_SUPPORT_REVIEW_POST_DEREGISTRATION_COMMS` | No |  |
| `INDUSTRY_LIFE_SUPPORT_REVIEW_POST_DEREGISTRATION` | No |  |
| `INDUSTRY_LIFE_SUPPORT_CANCEL_DEREGISTRATION_FAILED` | No |  |
| `INDUSTRY_LIFE_SUPPORT_REGISTRATION_FOLLOW_UP_REQUIRED` | No |  |
| `INDUSTRY_LIFE_SUPPORT_REVIEW_AFTER_CANCELLED_MOVE_OUT_FOR_NEXT_ACCOUNT` | No |  |
| `INDUSTRY_LIFE_SUPPORT_REVIEW_ATTEMPTED_CANCELLED_MOVE_OUT_FOR_NEXT_ACCOUNT` | No |  |
| `INDUSTRY_UNABLE_TO_CREATE_RECORD` | No |  |
| `INDUSTRY_CHANGE_OF_SUPPLIER_DOUBLE_GAIN` | No |  |
| `INDUSTRY_METER_POINT_MISSING_CUSTOMER_CLASSIFICATION` | No |  |
| `INDUSTRY_WARNING_MESSAGE_RECEIVED` | No |  |
| `SERVICE_ORDER_ACKNOWLEDGEMENT_OVERDUE` | No |  |
| `SERVICE_ORDER_INITIAL_RESPONSE_OVERDUE` | No |  |
| `SERVICE_ORDER_NOT_COMPLETED` | No |  |
| `SERVICE_ORDER_CANCELLATION_REQUEST_REJECTED` | No |  |
| `SERVICE_ORDER_PARTIALLY_COMPLETED` | No |  |
| `SERVICE_ORDER_UNABLE_TO_CHARGE` | No |  |
| `SERVICE_ORDER_REQUEST_REJECTED` | No |  |
| `SERVICE_ORDER_UNSOLICITED_RECEIVED` | No |  |
| `SERVICE_ORDER_UNSOLICITED_RECEIVED_DEENERGISED_METER_POINT` | No |  |
| `SERVICE_ORDER_FAILED` | No |  |
| `SERVICE_ORDER_CANCELLATION_FAILED` | No |  |
| `SERVICE_ORDER_OTHER_JOB_ENQUIRY_CODE` | No |  |
| `SMARTFLEX_DEVICE_INTEGRATION_POSTPONED` | No |  |
| `SPECIAL_READ_FAILED` | No |  |
| `SPECIAL_READ_CANCELLATION_FAILED` | No |  |
| `SPECIAL_READ_OUTSTANDING` | No |  |
| `SPECIAL_READ_WITH_ESTIMATE_READ_RECEIVED` | No |  |
| `NETWORK_TARIFF_ONE_WAY_NOTIFICATION` | No |  |
| `METER_EXCHANGE_ONE_WAY_NOTIFICATION` | No |  |
| `METER_FAULT_AND_ISSUE_ONE_WAY_NOTIFICATION_ACCEPTED` | No |  |
| `METER_FAULT_AND_ISSUE_ONE_WAY_NOTIFICATION_REJECTED` | No |  |
| `NOTICE_OF_METERING_WORKS_ONE_WAY_NOTIFICATION` | No |  |
| `COMMERCIAL_ENERGISATION_INTERVENTION_REQUIRED` | No |  |
| `PPA_EXPORT_INTERVENTION_REQUIRED` | No |  |
| `ACCOUNT_COOL_OFF` | No |  |
| `PLANNED_INTERRUPTION_ONE_WAY_NOTIFICATION` | No |  |
| `PLANNED_INTERRUPTION_ONE_WAY_NOTIFICATION_REJECTED` | No |  |
| `PLANNED_INTERRUPTION_NOTIFICATION_SENT_TO_LIFE_SUPPORT_CUSTOMER` | No |  |
| `FIELDWORKS_ALLOCATE_NMI_MARKET_PARTICIPANTS_NOT_SET` | No |  |
| `FIELDWORKS_BULK_DEPLOYMENT_JOURNEY_AUTO_CANCELLED` | No |  |
| `FIELDWORKS_METER_FAULT_JOURNEY_AUTO_CANCELLED` | No |  |
| `FIELDWORKS_MULTIPLE_OPEN_JOURNEYS_FOR_METER_POINT` | No |  |
| `FIELDWORKS_UPLOAD_ATTACHMENT_TO_JEMENA_PORTAL` | No |  |
| `FIELDWORKS_OBTAIN_SUPPLY_ABOLISHMENT_APPROVAL` | No |  |
| `FIELDWORKS_JOURNEY_CANCELLED_DUE_TO_LIFE_SUPPORT_REGISTRATION` | No |  |
| `FIELDWORKS_MIRN_DISCOVERY_FAILED` | No |  |
| `FIELDWORKS_SERVICE_ORDER_PARTIALLY_COMPLETED` | No |  |
| `FIELDWORKS_SERVICE_ORDER_FAILED` | No |  |
| `FIELDWORKS_PAYER_CONTACT_FAILED_VALIDATION` | No |  |
| `COS_GAIN_REL_RETRIEVAL_FAILURE` | No |  |
| `INDUSTRY_EXCEPTION_UNABLE_TO_ENROL_METER_POINT_INVALID_NMI_METER_STATUS` | No |  |
| `FIELDWORKS_JOURNEY_ATTACHMENTS` | No |  |
| `FIELDWORKS_SERVICE_ORDER_ATTACHMENTS` | No |  |
| `FIELDWORKS_SERVICE_ORDER_STATUS_UPDATED` | No |  |
| `FIELDWORKS_SERVICE_ORDER_COMPLETED` | No |  |
| `FIELDWORKS_SERVICE_ORDER_UNABLE_TO_ACCESS_WITH_CUSTOMER_CONSULTATION` | No |  |
| `FIELDWORKS_SERVICE_ORDER_UNABLE_TO_ACCESS_WITHOUT_CUSTOMER_CONSULTATION` | No |  |
| `FIELDWORKS_MOVE_OUT_CANCELLED_WHILE_SUPPLY_ABOLISHMENT_IN_PROGRESS` | No |  |
| `FIELDWORKS_SUPPLY_PERIOD_DOES_NOT_EXIST_FOR_METERPOINT` | No |  |
| `FIELDWORKS_METERPOINT_IS_NOT_ACTIVE` | No |  |
| `FIELDWORKS_EXPECTED_METER_POINT_NOT_CREATED` | No |  |
| `FIELDWORKS_NEW_CONNECTION_DATA_NOT_VALID` | No |  |
| `FIELDWORKS_NEW_CONNECTION_COMPLETION_REVIEW` | No |  |
| `FIELDWORKS_EXPECTED_METER_READ_NOT_RECEIVED` | No |  |
| `FIELDWORKS_EXPECTED_NTCS_NOT_RECEIVED` | No |  |
| `FIELDWORKS_CONTACT_SO_RECIPIENT_TO_UPDATE_THE_SO_DETAILS` | No |  |
| `FIELDWORKS_INVESTIGATE_WHETHER_JOURNEY_NEEDS_CONTINUATION` | No |  |
| `FIELDWORKS_CHANGE_REQUEST_STEP_FAILED` | No |  |
| `FIELDWORKS_CHANGE_REQUEST_STEP_ERRORED` | No |  |
| `FIELDWORKS_SERVICE_ORDER_STEP_FAILED` | No |  |
| `FIELDWORKS_SERVICE_ORDER_STEP_ERRORED` | No |  |
| `FIELDWORKS_OBTAIN_CUSTOMER_APPROVAL_BEFORE_PROGRESSING` | No |  |
| `FIELDWORKS_MANUALLY_COMPLETE_CUSTOMER_MOVE_IN` | No |  |
| `FIELDWORKS_ACCOUNT_CREATED_WITH_NO_EMAIL_ADDRESS` | No |  |
| `FIELDWORKS_MAINTAIN_REGISTER_BILLABLE_OVERRIDE_FOR_UNSOLICITED_METER_CHANGES` | No |  |
| `AUS_EMBEDDED_WATER_READING_FAILURE` | No |  |
| `AUS_EMBEDDED_WATER_ESTIMATION_REQUIRED_FOR_SKIPPED_READING` | No |  |
| `AUS_EMBEDDED_ACQUISITION_MATRIX_ERROR` | No |  |
| `AUS_VIC_SHAREDFUSE_NOTIFICATION` | No |  |
| `AUS_INDUSTRY_CUSTOMER_OWN_READING_NOT_SENT` | No |  |
| `JPN_READINGS_NOT_RECEIVED` | No |  |
| `JPN_FINAL_READING_OUTSIDE_AGREEMENT` | No |  |
| `JPN_CONFIRMATION_OF_RELOCATION` | No |  |
| `JPN_SHORT_TERM_MOVE_IN_REJECTION` | No |  |
| `JPN_SUPPLY_POINT_FAILS_CAN_SUPPLY_CHECK` | No |  |
| `JPN_BILLING_FIX_INVALID_CHARGE_DATA` | No |  |
| `DUNNING_OUTBOUND_REMINDER_CALL` | No |  |
| `DUNNING_BEST_ENDEAVOURS_CALL` | No |  |
| `DUNNING_DISCONNECTION_OUTBOUND_REMINDER_CALL` | No |  |
| `DUNNING_DISCONNECTION_DE_ENERGISATION_ASSESSMENT` | No |  |
| `DUNNING_MANDATORY_NOTICE_EMAIL_FAILURE` | No |  |
| `DUNNING_DISCONNECTION_MANDATORY_NOTICE_EMAIL_FAILURE` | No |  |
| `DUNNING_VACANT_CONSUMPTION_DE_ENERGISATION_ASSESSMENT` | No |  |
| `DUNNING_REMINDER_CALL` | No |  |
| `DUNNING_REMINDER_DISCONNECTION_APPLICATION` | No |  |
| `DUNNING_REMINDER_PAYMENT_MADE` | No |  |
| `DUNNING_REMINDER_FUTURE_PAYMENT` | No |  |
| `NON_ENERGY_PAYMENT_CALL_REMINDER` | No |  |
| `PAYMENTS_FAILED_REPAYMENT` | No |  |
| `PAYMENT_PLAN` | No |  |
| `PAYMENT_PLAN_MISSED_INSTALMENT` | No |  |
| `ACTIVATE_PAYMENT_CANCELLATION_STOPPED` | No |  |
| `POST_HARDSHIP_CANCELLATION` | No |  |
| `PAYMENT_PLAN_HARDSHIP_COMPLETION` | No |  |
| `PAYMENT_PLAN_HARDSHIP_COMPLETION_WORKFLOW_CANCELLED` | No |  |
| `HARDSHIP_GRADUATION_ASSESSMENT` | No |  |
| `HARDSHIP_REMOVAL_ASSESSMENT` | No |  |
| `AUS_CENTREPAY_EXCESSIVE_CREDIT` | No |  |
| `PAYMENT_INSTRUCTION_FAILED` | No |  |
| `PAYMENT_SCHEDULE_FAILED_TO_CREATE` | No |  |
| `HARDSHIP_NO_PAYMENT_PLAN` | No |  |
| `DISCONNECTION_MANDATORY_NOTICE_EMAIL_FAILURE` | No |  |
| `DISCONNECTION_MANDATORY_NOTICE_SMS_FAILURE` | No |  |
| `INDUSTRY_EXCEPTION_STANDING_DATA_PROPERTIES_ADDRESS_FAILED_TO_UPDATE` | No |  |
| `MARKET_SUPPLY_EXCEPTION_AGREEMENT_FAILED_TO_TERMINATE` | No |  |
| `MARKET_SUPPLY_EXCEPTION_AGREEMENT_FAILED_TO_CREATE` | No |  |
| `MARKET_SUPPLY_EXCEPTION_AGREEMENT_FAILED_TO_UPDATE` | No |  |
| `MARKET_SUPPLY_EXCEPTION_MISSING_ACCOUNT_QUOTED_PRODUCT` | No |  |
| `MARKET_SUPPLY_EXCEPTION_AGREEMENT_FAILED_TO_REVERSE_TERMINATION` | No |  |
| `GAS_EXCEPTION_SITE_ACCESS_DETAILS_RECEIVED_FOR_NON_EXISTENT_METER` | No |  |
| `GAS_EXCEPTION_CUSTOMER_DETAILS_NOTIFICATION_FAILED` | No |  |
| `GAS_EXCEPTION_LIFE_SUPPORT_NOTIFICATION_FAILED` | No |  |
| `GAS_EXCEPTION_SITE_ACCESS_DETAILS_NOTIFICATION_FAILED` | No |  |
| `GAS_EXCEPTION_SITE_ADDRESS_DETAILS_NOTIFICATION_FAILED` | No |  |
| `GAS_EXCEPTION_METER_DATA_VERIFY_REQUEST_FAILED` | No |  |
| `GAS_EXCEPTION_METER_DATA_VERIFY_RESPONSE_OVERDUE` | No |  |
| `GAS_EXCEPTION_METER_DATA_VERIFY_RESPONSE_NO_CHANGE_WITH_EXPLANATION` | No |  |
| `GAS_EXCEPTION_METER_DATA_VERIFY_RESPONSE_WITHOUT_REVISED_READ` | No |  |
| `GAS_NOTIFICATION_CHANGE_OF_SITE_ADDRESS` | No |  |
| `INDUSTRY_EXCEPTION_NEXT_SCHEDULED_READ_DATE_TOO_FAR_IN_FUTURE` | No |  |
| `GAS_EXCEPTION_CUSTOMER_TRANSFER_CANCELLED` | No |  |
| `GAS_EXCEPTION_CUSTOMER_TRANSFER_REJECTED` | No |  |
| `GAS_MANUAL_SERVICE_ORDER_REQUIRED_FOR_ENROLMENT` | No |  |
| `GAS_READING_REMOVED_INSTALLED_RECEIVED` | No |  |
| `GAS_UNKNOWN_CUSTOMER_CLASSIFICATION_CODE_RECEIVED` | No |  |
| `BILLING_AMENDED_METER_READ_BASIC` | No |  |
| `BILLING_AMENDED_METER_READ_GAS` | No |  |
| `BILLING_AMENDED_METER_READ_INTERVAL` | No |  |
| `BILLING_AMENDED_METER_READ_PRE_MIGRATION` | No |  |
| `BILLING_AMENDED_METER_READ_CES_ELEC_BASIC` | No |  |
| `BILLING_AMENDED_METER_READ_CES_ELEC_INTERVAL` | No |  |
| `BILLING_REGISTER_REPLACED_OR_REMOVED` | No |  |
| `BILLING_CUSTOMER_SELF_READ_RECEIVED` | No |  |
| `BILLING_MISSING_READ` | No |  |
| `SA_CONCESSION_STATEMENT_CLOSED` | No |  |
| `BILLING_QUOTED_NTC_DOES_NOT_ALIGN` | No |  |
| `FINAL_BILLING_UNABLE_TO_BILL` | No |  |
| `MANDATORY_COMMS_NOT_DELIVERED` | No |  |
| `CONTRACT_COMMS_NOT_DELIVERED` | No |  |
| `MOVE_IN_COMMS_NOT_DELIVERED` | No |  |
| `SMART_METER_MODE_CHANGE_UNSUPPORTED` | No |  |
| `HELD_STATEMENT` | No |  |
| `HELD_BILLING_DOCUMENT` | No |  |
| `AUTOMATED_BILLING_DISABLED` | No |  |
| `SOLAR_EXPORT_CREDITS_EXCESS` | No |  |
| `ASSIGNED_TO_CREDIT_TEAM` | No |  |
| `WORKFLOW_STEP_FAILED` | No |  |
| `WORKFLOW_STEP_ERRORED` | No |  |
| `WORKFLOW_CANCELLATION_FAILED` | No |  |
| `COS_GAIN_MIGRATION_ECOES_METER_MISMATCH` | No |  |
| `ACCOUNT_MIGRATION_SYNC_XOSERVE_METER_MISMATCH` | No |  |
| `SMART_CHANGE_OF_TENANCY_IN_PROGRESS` | No |  |
| `AGREEMENT_REVOKED` | No |  |
| `UNSUPPORTED_PAYMENT_DAY` | No |  |
| `UNSUPPORTED_FEATURE` | No |  |
| `EMBEDDED_NETWORK_EXCEPTION_PARENT_METER_POINT_LOST_OR_LOSING` | No |  |
| `EMBEDDED_NETWORK_EXCEPTION_PARENT_METER_POINT_RECEIVED_LIFE_SUPPORT_NOTIFICATION` | No |  |
| `EMBEDDED_NETWORK_EXCEPTION_PARENT_METER_POINT_RECEIVED_DANGEROUS_LIFE_SUPPORT_NOTIFICATION` | No |  |
| `EMBEDDED_NETWORK_EXCEPTION_DISTRIBUTOR_OWNED_PARENT_LIFE_SUPPORT_RECORD` | No |  |
| `EMBEDDED_NETWORK_ALL_CHILD_LIFE_SUPPORT_RECORDS_ARE_DEREGISTERED` | No |  |
| `SCHEDULED_BILLING_ADDRESS_UPDATE` | No |  |
| `SCHEDULED_OCCUPIER_PACK_SEND` | No |  |
| `PROPERTY_ADDRESS_NEEDS_UPDATE` | No |  |
| `FRA_ACTIVATION_PROCESS_INCEPTION_CHECKS` | No |  |
| `FRA_ACTIVATION_PROCESS_SCHEDULE_SITEWORKS` | No |  |
| `FRA_ACTIVATION_PROCESS_GAS_PROVIDER_CHANGE_REQUEST` | No |  |
| `FRA_ACTIVATION_PROCESS_PRM_ELIGIBILITY` | No |  |
| `FRA_ACTIVATION_PROCESS_AWAITING_SWITCH_READINGS` | No |  |
| `FRA_ELEC_ACTIVATION_PROCESS_WRONG_SWITCH_READINGS_FOR_PROVIDER_CALENDAR_TEMPORAL_CLASSES` | No |  |
| `FRA_ACTIVATION_PROCESS_COMMANDER_SOUSCRIPTION` | No |  |
| `FRA_ACTIVATION_PROCESS_AWAITING_SWITCH_IN_CONFIRMATION` | No |  |
| `FRA_TERMINATION_REQUEST_ERRORED` | No |  |
| `FRA_TERMINATION_PROCESS_NEEDS_INTERVENTION` | No |  |
| `FRA_ENERGY_CHEQUE_UNKNOWN` | No |  |
| `COMMS_TO_BE_PRINTED` | No |  |
| `FLOW_FILE_ERROR` | No |  |
| `NEW_PSR_ADDED_TO_PREPAY_ACCOUNT` | No |  |
| `PSR_IMPORT_COULD_NOT_IDENTIFY_ACCOUNT_USER` | No |  |
| `MAIL_RETURNED` | No |  |
| `MAIL_FAILED` | No |  |
| `DUPLICATE_CARD_FINGERPRINTS` | No |  |
| `WATER_METER_READING_ISSUE` | No |  |
| `WATER_ACCOUNT_REVERSION` | No |  |
| `DEU_SWICHTING_PROCESS_FAILED` | No |  |
| `DEU_METER_READINGS` | No |  |
| `DEU_MASTER_DATA_SYNCHRONISATION` | No |  |
| `DEU_MASTER_DATA_UPDATE` | No |  |
| `DEU_INBOUND_APERAK` | No |  |
| `FAMILY_ISSUES_ADDED` | No |  |
| `MIGRATION_TYPE` | No |  |
| `FIELDWORKS_APPOINTMENTS_UNAVAILABLE` | No |  |
| `COLLECTION_PROCESS_COMMS_FAILURE` | No |  |

## `AccountRepaymentStatusOptions`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `REQUESTED` | No | The request for a repayment has been received but not actioned yet. |
| `APPROVED` | No | The repayment has been approved but not made yet. |
| `SUBMITTED` | No | The payment has been submitted to the merchant. It is still possible for this repayment to fail. |
| `FAILED` | No | The repayment failed permanently. This could be because of technical issues, or if the merchant rejects the payment for some reason. The payment will need to be retried by ops. |
| `PAID` | No | The repayment has been made to the merchant to be sent to the customer. This is a terminal state, we don't get any further confirmation. |
| `THIRD_PARTY` | No | Third Party payments are those recorded for financial purposes in a different system but should be added to statements. |
| `HISTORIC` | No | Payments made in a previous system and then imported into Kraken. |

## `AccountStatementStatus`

Status of account statement (OPEN or CLOSED).

| Value | Deprecated | Description |
|---|---|---|
| `OPEN` | No |  |
| `CLOSED` | No |  |

## `AccountStatus`

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No | A pending account is one that has been created but no registrations have started. |
| `INCOMPLETE` | No | Account requires processes to be completed before supply can be set up |
| `WITHDRAWN` | No | Withdrawn before supply started |
| `ACTIVE` | No | Supply could have started, be ongoing or ended. |
| `ENROLMENT_ERROR` | No | An error occurred when we tried to enroll a meter point. This may be deprecated in future in favour of exposing this through enrollment property of a meter point. |
| `ENROLMENT_REJECTED` | No | Meter point enrollment was rejected. This may be deprecated in future in favour of exposing this through enrollment property of a meter point. |
| `DORMANT` | No | Dormant. Users should not be able to log into dormant accounts. |
| `VOID` | No | Void. Account created in error. |

## `AccountTypeChoices`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `BUSINESS` | No | An account designed to supply/bill business premises. |
| `BUSINESS_OCCUPIER` | No | An account created when we supply a business premises but do not have details for the occupants. |
| `BUSINESS_THIRD_PARTY_BILLED` | No | An account designed to supply/bill business premises where the bill is sent to a third party. |
| `BUSINESS_VACANT` | No | An account created when we supply a business premises and know there are definitely no occupants. |
| `DOMESTIC` | No | An account designed to supply/bill domestic premises. |
| `DOMESTIC_THIRD_PARTY_BILLED` | No | An account designed to supply/bill domestic premises where the bill is sent to a third party. |
| `MANAGED` | No | An account created when we supply domestic premises that are managed by a business, i.e., a B2B2C model. |
| `OCCUPIER` | No | An account created when we supply a domestic premises but do not have details for the occupants. |
| `PORTFOLIO_LEAD` | No | An account which is responsible for all other accounts in the portfolio, i.e. pays the bills for them. |
| `SUPPLY_POINT` | No | An account that represents the relationship between a supply point and a supplier. |
| `VACANT` | No | An account created when we supply a domestic premises and know there are definitely no occupants. |

## `AgreementRescissionStatus`

Status of an agreement rescission.

| Value | Deprecated | Description |
|---|---|---|
| `IN_PROGRESS` | No |  |
| `REJECTED` | No |  |
| `ERRORED` | No |  |
| `COMPLETED` | No |  |

## `AgreementRolloverRolloverType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `DEFAULT` | No | Default Rollover |
| `CUSTOM` | No | Custom Renewal |
| `EXTENSION` | No | Custom Extension |
| `CUSTOMER_REQUESTED` | No | Customer Requested |

## `AgreementRolloverStatus`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No | Rollover Pending |
| `REJECTED` | No | Rollover Rejected |
| `ENQUEUED` | No | Rollover In Progress |
| `ERROR` | No | Error During Rollover |
| `DONE` | No | Rollover Completed |
| `REVOKED` | No | Rollover Revoked |

## `Alignment`

| Value | Deprecated | Description |
|---|---|---|
| `START` | No |  |
| `CENTER` | No |  |
| `END` | No |  |

## `AmountStrategy`

| Value | Deprecated | Description |
|---|---|---|
| `FIXED` | No |  |
| `PLAN` | No |  |
| `BALANCE` | No |  |
| `BILL` | No |  |

## `AppSessionOutcomeCategories`

Enumeration of app session types.

| Value | Deprecated | Description |
|---|---|---|
| `SUCCESS` | No |  |
| `INTERESTED` | No |  |
| `QUOTED_NO_SWITCH` | No |  |
| `QUOTED_NO_SALE` | No |  |
| `PITCH_NO_QUOTE` | No |  |
| `NO_PITCH` | No |  |
| `CALLBACK` | No |  |
| `UNSUCCESSFUL` | No |  |
| `DONT_CALL_AGAIN` | No |  |
| `PSR_REGISTERED` | No |  |
| `SMART_METER_REGISTERED` | No |  |
| `CONSUMER_APP_DOWNLOAD` | No |  |
| `VULNERABILITY_PROJECT` | No |  |
| `TRANSFERRED` | No |  |
| `UNKNOWN` | No |  |
| `OTHER` | No |  |
| `SWITCHED` | No |  |
| `SWITCHED_BUSINESS` | No |  |
| `SWITCHED_CREDIT_CHECK_WAIVER` | No |  |
| `SWITCHED_FIRST_CONTACT` | No |  |
| `SWITCHED_CALLBACK` | No |  |
| `SWITCHED_SMART_PRODUCT` | No |  |
| `QUOTED_NO_SALE_QUOTE_EMAILED` | No |  |
| `QUOTED_NO_SALE_PRICE` | No |  |
| `QUOTED_NO_SALE_EXIT_FEES` | No |  |
| `QUOTED_NO_SALE_NO_EMAIL` | No |  |
| `QUOTED_NO_SALE_ISSUE_BANK_DETAILS` | No |  |
| `QUOTED_NO_SALE_ADVANCED_PAYMENT` | No |  |
| `QUOTED_NO_SALE_STANDING_CHARGE` | No |  |
| `QUOTED_NO_SALE_PAPER_BILLS` | No |  |
| `QUOTED_NO_SALE_MONTHLY_DD` | No |  |
| `QUOTED_NO_SALE_CREDIT_CHECK_ISSUE` | No |  |
| `QUOTED_NO_SALE_WAIVER_WANTED` | No |  |
| `QUOTED_NO_SALE_DEPOSIT` | No |  |
| `QUOTED_NO_SALE_AUTOPAY` | No |  |
| `QUOTED_NO_SALE_PREPAY` | No |  |
| `QUOTED_NO_SALE_UNSURE_OF_CURRENT_CONTRACT` | No |  |
| `QUOTED_NO_SALE_OTHER` | No |  |
| `NO_PITCH_SWITCHED_RECENTLY` | No |  |
| `NO_PITCH_VULNERABLE` | No |  |
| `NO_PITCH_NO_D2D` | No |  |
| `NO_PITCH_NOT_INTERESTED` | No |  |
| `NO_PITCH_TPI_THIRD_PARTY` | No |  |
| `PITCH_NO_QUOTE_SWITCHED_RECENTLY` | No |  |
| `PITCH_NO_QUOTE_PRICE` | No |  |
| `PITCH_NO_QUOTE_IN_CONTRACT` | No |  |
| `PITCH_NO_QUOTE_NO_EMAIL` | No |  |
| `PITCH_NO_QUOTE_NOT_INTERESTED` | No |  |
| `PITCH_NO_QUOTE_ADVANCED_PAYMENT` | No |  |
| `QUOTED_CALLBACK` | No |  |
| `CALLBACK_PITCHED` | No |  |
| `NO_ANSWER` | No |  |
| `NOT_BILL_PAYER` | No |  |
| `NOT_DECISION_MAKER` | No |  |
| `BUSY` | No |  |
| `MULTIPLE_PROPERTIES` | No |  |
| `CALLBACK_COURTESY_CALL` | No |  |
| `NO_COLD_CALLING` | No |  |
| `SHELTERED_HOUSING` | No |  |
| `NO_FIXED_ADDRESS` | No |  |
| `OCCUPY_ACCOUNT` | No |  |
| `OCCUPIER_NOT_BILL_PAYER` | No |  |
| `OCCUPIER_NO_ANSWER` | No |  |
| `OCCUPIER_REFUSED_TO_DISCUSS` | No |  |
| `OCCUPIER_SUSPECTED_EMPTY_PROPERTY` | No |  |
| `METER_READING` | No |  |
| `METER_READING_UNABLE_TO_TAKE_READING` | No |  |
| `METER_READING_NO_ANSWER` | No |  |
| `ENERGY_HELP_VISIT_COMPLETED` | No |  |
| `ENERGY_HELP_VISIT_LEAFLET` | No |  |
| `EBSS_VOUCHER_CHECK_IN` | No |  |
| `WRONG_ADDRESS_SELECTED` | No |  |
| `PREPAYMENT_METER` | No |  |
| `EXISTING_CUSTOMER` | No |  |
| `LEAD_GENERATION` | No |  |
| `LEAD_GENERATION_EV` | No |  |
| `LEAD_GENERATION_EJ` | No |  |
| `LEAD_GENERATION_EJ_LITE` | No |  |
| `LEAD_GENERATION_BUSINESS` | No |  |
| `LEAD_GENERATION_SOLAR` | No |  |
| `LEAD_GENERATION_HEAT_PUMP` | No |  |
| `PROPERTY_INELIGIBLE` | No |  |
| `ELECTRIC_JUICE_SWITCH` | No |  |
| `ELECTRIC_JUICE_SWITCH_LITE` | No |  |
| `ELECTRIC_JUICE_NOT_INTERESTED` | No |  |
| `PPM_REQUESTED` | No |  |
| `COT_PROVEN` | No |  |
| `COT_NO_PROOF` | No |  |
| `COS` | No |  |
| `PAID_IN_FULL` | No |  |
| `PAYMENT_PLAN` | No |  |
| `PAID_PARTIAL` | No |  |
| `PAID_REDUCED_SETTLEMENT` | No |  |
| `INSOLVENCY` | No |  |
| `EXHAUSTED_NO_CONTACT` | No |  |
| `EXHAUSTED_CONTACT` | No |  |
| `UNABLE_TO_LOCATE` | No |  |
| `EMPTY` | No |  |
| `DEMOLISHED` | No |  |
| `UNABLE_TO_TRACE` | No |  |
| `PRISON` | No |  |
| `VULNERABLE` | No |  |
| `DECEASED` | No |  |
| `WITHDRAWN` | No |  |
| `QUERY` | No |  |

## `AppSessionOutcomeCategory`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `SUCCESS` | No | Success |
| `INTERESTED` | No | Interested |
| `QUOTED_NO_SWITCH` | No | Quoted No Switch |
| `QUOTED_NO_SALE` | No | Quoted No Sale |
| `PITCH_NO_QUOTE` | No | Pitch No Quote |
| `NO_PITCH` | No | No Pitch |
| `CALLBACK` | No | Callback |
| `UNSUCCESSFUL` | No | Unsuccessful |
| `DONT_CALL_AGAIN` | No | Dont Call Again |
| `PSR_REGISTERED` | No | Psr Registered |
| `SMART_METER_REGISTERED` | No | Smart Meter Registered |
| `CONSUMER_APP_DOWNLOAD` | No | Consumer App Download |
| `VULNERABILITY_PROJECT` | No | Vulnerability Project |
| `TRANSFERRED` | No | Transferred |
| `UNKNOWN` | No | Unknown |
| `OTHER` | No | Other |
| `SWITCHED` | No | Switched |
| `SWITCHED_BUSINESS` | No | Switched Business |
| `SWITCHED_CREDIT_CHECK_WAIVER` | No | Switched Credit Check Waiver |
| `SWITCHED_FIRST_CONTACT` | No | Switched First Contact |
| `SWITCHED_CALLBACK` | No | Switched Callback |
| `SWITCHED_SMART_PRODUCT` | No | Switched Smart Product |
| `QUOTED_NO_SALE_QUOTE_EMAILED` | No | Quoted No Sale Quote Emailed |
| `QUOTED_NO_SALE_PRICE` | No | Quoted No Sale Price |
| `QUOTED_NO_SALE_EXIT_FEES` | No | Quoted No Sale Exit Fees |
| `QUOTED_NO_SALE_NO_EMAIL` | No | Quoted No Sale No Email |
| `QUOTED_NO_SALE_ISSUE_BANK_DETAILS` | No | Quoted No Sale Issue Bank Details |
| `QUOTED_NO_SALE_ADVANCED_PAYMENT` | No | Quoted No Sale Advanced Payment |
| `QUOTED_NO_SALE_STANDING_CHARGE` | No | Quoted No Sale Standing Charge |
| `QUOTED_NO_SALE_PAPER_BILLS` | No | Quoted No Sale Paper Bills |
| `QUOTED_NO_SALE_MONTHLY_DD` | No | Quoted No Sale Monthly Dd |
| `QUOTED_NO_SALE_CREDIT_CHECK_ISSUE` | No | Quoted No Sale Credit Check Issue |
| `QUOTED_NO_SALE_WAIVER_WANTED` | No | Quoted No Sale Waiver Wanted |
| `QUOTED_NO_SALE_DEPOSIT` | No | Quoted No Sale Deposit |
| `QUOTED_NO_SALE_AUTOPAY` | No | Quoted No Sale Autopay |
| `QUOTED_NO_SALE_PREPAY` | No | Quoted No Sale Prepay |
| `QUOTED_NO_SALE_UNSURE_OF_CURRENT_CONTRACT` | No | Quoted No Sale Unsure Of Current Contract |
| `QUOTED_NO_SALE_OTHER` | No | Quoted No Sale Other |
| `NO_PITCH_SWITCHED_RECENTLY` | No | No Pitch Switched Recently |
| `NO_PITCH_VULNERABLE` | No | No Pitch Vulnerable |
| `NO_PITCH_NO_D2D` | No | No Pitch No D2D |
| `NO_PITCH_NOT_INTERESTED` | No | No Pitch Not Interested |
| `NO_PITCH_TPI_THIRD_PARTY` | No | No Pitch Tpi Third Party |
| `PITCH_NO_QUOTE_SWITCHED_RECENTLY` | No | Pitch No Quote Switched Recently |
| `PITCH_NO_QUOTE_PRICE` | No | Pitch No Quote Price |
| `PITCH_NO_QUOTE_IN_CONTRACT` | No | Pitch No Quote In Contract |
| `PITCH_NO_QUOTE_NO_EMAIL` | No | Pitch No Quote No Email |
| `PITCH_NO_QUOTE_NOT_INTERESTED` | No | Pitch No Quote Not Interested |
| `PITCH_NO_QUOTE_ADVANCED_PAYMENT` | No | Pitch No Quote Advanced Payment |
| `QUOTED_CALLBACK` | No | Quoted Callback |
| `CALLBACK_PITCHED` | No | Callback Pitched |
| `NO_ANSWER` | No | No Answer |
| `NOT_BILL_PAYER` | No | Not Bill Payer |
| `NOT_DECISION_MAKER` | No | Not Decision Maker |
| `BUSY` | No | Busy |
| `MULTIPLE_PROPERTIES` | No | Multiple Properties |
| `CALLBACK_COURTESY_CALL` | No | Callback Courtesy Call |
| `NO_COLD_CALLING` | No | No Cold Calling |
| `SHELTERED_HOUSING` | No | Sheltered Housing |
| `NO_FIXED_ADDRESS` | No | No Fixed Address |
| `OCCUPY_ACCOUNT` | No | Occupy Account |
| `OCCUPIER_NOT_BILL_PAYER` | No | Occupier Not Bill Payer |
| `OCCUPIER_NO_ANSWER` | No | Occupier No Answer |
| `OCCUPIER_REFUSED_TO_DISCUSS` | No | Occupier Refused To Discuss |
| `OCCUPIER_SUSPECTED_EMPTY_PROPERTY` | No | Occupier Suspected Empty Property |
| `METER_READING` | No | Meter Reading |
| `METER_READING_UNABLE_TO_TAKE_READING` | No | Meter Reading Unable To Take Reading |
| `METER_READING_NO_ANSWER` | No | Meter Reading No Answer |
| `ENERGY_HELP_VISIT_COMPLETED` | No | Energy Help Visit Completed |
| `ENERGY_HELP_VISIT_LEAFLET` | No | Energy Help Visit Leaflet |
| `EBSS_VOUCHER_CHECK_IN` | No | Ebss Voucher Check In |
| `WRONG_ADDRESS_SELECTED` | No | Wrong Address Selected |
| `PREPAYMENT_METER` | No | Prepayment Meter |
| `EXISTING_CUSTOMER` | No | Existing Customer |
| `LEAD_GENERATION` | No | Lead Generation |
| `LEAD_GENERATION_EV` | No | Lead Generation Ev |
| `LEAD_GENERATION_EJ` | No | Lead Generation Ej |
| `LEAD_GENERATION_EJ_LITE` | No | Lead Generation Ej Lite |
| `LEAD_GENERATION_BUSINESS` | No | Lead Generation Business |
| `LEAD_GENERATION_SOLAR` | No | Lead Generation Solar |
| `LEAD_GENERATION_HEAT_PUMP` | No | Lead Generation Heat Pump |
| `PROPERTY_INELIGIBLE` | No | Property Ineligible |
| `ELECTRIC_JUICE_SWITCH` | No | Electric Juice Switch |
| `ELECTRIC_JUICE_SWITCH_LITE` | No | Electric Juice Switch Lite |
| `ELECTRIC_JUICE_NOT_INTERESTED` | No | Electric Juice Not Interested |
| `PPM_REQUESTED` | No | Ppm Requested |
| `COT_PROVEN` | No | Cot Proven |
| `COT_NO_PROOF` | No | Cot No Proof |
| `COS` | No | Cos |
| `PAID_IN_FULL` | No | Paid In Full |
| `PAYMENT_PLAN` | No | Payment Plan |
| `PAID_PARTIAL` | No | Paid Partial |
| `PAID_REDUCED_SETTLEMENT` | No | Paid Reduced Settlement |
| `INSOLVENCY` | No | Insolvency |
| `EXHAUSTED_NO_CONTACT` | No | Exhausted No Contact |
| `EXHAUSTED_CONTACT` | No | Exhausted Contact |
| `UNABLE_TO_LOCATE` | No | Unable To Locate |
| `EMPTY` | No | Empty |
| `DEMOLISHED` | No | Demolished |
| `UNABLE_TO_TRACE` | No | Unable To Trace |
| `PRISON` | No | Prison |
| `VULNERABLE` | No | Vulnerable |
| `DECEASED` | No | Deceased |
| `WITHDRAWN` | No | Withdrawn |
| `QUERY` | No | Query |

## `AppSessionOutcomeType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `SALE` | No | Sale |
| `BUSINESS_SALE` | No | Business Sale |
| `OCCUPIER` | No | Occupier |
| `METER_READING` | No | Meter Reading |
| `ELECTROVERSE_LEAD` | No | Electroverse Lead |
| `ELECTROVERSE` | No | Electroverse |
| `EV_LEAD` | No | Ev Lead |
| `ENERGY_HELP` | No | Energy Help |
| `SOLAR_LEAD` | No | Solar Lead |
| `EV_CHARGER` | No | Ev Charger |
| `HEAT_PUMP_LEAD` | No | Heat Pump Lead |
| `INTELLIGENT_OCTOPUS_SIGNUP` | No | Intelligent Octopus Signup |
| `CREDIT` | No | Credit |
| `CREDIT_BUSINESS` | No | Credit Business |
| `BUSINESS_LEAD_HALF_HOURLY` | No | Business Lead Half Hourly |
| `UNKNOWN` | No | Unknown |
| `LEAD` | No | Lead |
| `BUSINESS_LEAD` | No | Business Lead |
| `ELECTRIC_UNIVERSE` | No | Electric Universe |
| `ENERGY_SUPPORT` | No | Energy Support |

## `AppSessionSalesMode`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `DOOR` | No | Door |
| `VENUE` | No | Venue |

## `AppSessionTypeChoices`

Enumeration of app session types.

| Value | Deprecated | Description |
|---|---|---|
| `SALE` | No |  |
| `BUSINESS_SALE` | No |  |
| `OCCUPIER` | No |  |
| `METER_READING` | No |  |
| `ELECTROVERSE_LEAD` | No |  |
| `ELECTROVERSE` | No |  |
| `EV_LEAD` | No |  |
| `ENERGY_HELP` | No |  |
| `SOLAR_LEAD` | No |  |
| `EV_CHARGER` | No |  |
| `HEAT_PUMP_LEAD` | No |  |
| `INTELLIGENT_OCTOPUS_SIGNUP` | No |  |
| `CREDIT` | No |  |
| `CREDIT_BUSINESS` | No |  |
| `BUSINESS_LEAD_HALF_HOURLY` | No |  |
| `UNKNOWN` | No |  |
| `LEAD` | No |  |
| `BUSINESS_LEAD` | No |  |
| `ELECTRIC_UNIVERSE` | No |  |
| `ENERGY_SUPPORT` | No |  |

## `BillTypeEnum`

| Value | Deprecated | Description |
|---|---|---|
| `STATEMENT` | No |  |
| `INVOICE` | No |  |
| `CREDIT_NOTE` | No |  |
| `PRE_KRAKEN` | No |  |
| `COLLECTIVE` | No |  |

## `BillsOrderBy`

| Value | Deprecated | Description |
|---|---|---|
| `FROM_DATE_DESC` | No |  |
| `ISSUED_DATE_DESC` | No |  |

## `BrandChoices`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `OCTOPUS_ENERGY_SPAIN` | No | Octopus Energy Spain. |

## `BusinessTypeOptions`

Available business account type options (e.g., sole trader, limited company, partnership, charity).

| Value | Deprecated | Description |
|---|---|---|
| `SOLE_TRADER` | No | A business account where the company type is sole trader. |
| `LIMITED` | No | A business account where the company type is limited. |
| `PROPRIETARY_LIMITED_COMPANY` | No | A business account where the company type is proprietary limited. |
| `PARTNERSHIP` | No | A business account where the company type is partnership. |
| `CHARITY` | No | A business account where the company type is charity. |
| `PUBLIC_LIMITED_COMPANY` | No | A business account where the company type is public limited. |
| `LIMITED_LIABILITY_PARTNERSHIP` | No | A business account where the company type is limited liability partnership. |
| `TRUST` | No | A business account where the company type is a trust. |
| `TRADING_AS` | No | A business account where the company has a trading name to carry out its business activities. |
| `GOVERNMENT` | No | A business account for a government institution. |
| `NON_PROFIT` | No | A business account for a non-profit organisation. |
| `CHURCH` | No | A business account for a church or other religious organisation. |
| `HOMEOWNER_ASSOCIATION` | No | A business account for a homeowner association or similar community group. |
| `TO_BE_DETERMINED` | No | A business account where the company type is to be determined. |

## `ButtonStyle`

| Value | Deprecated | Description |
|---|---|---|
| `PRIMARY` | No |  |
| `SECONDARY` | No |  |

## `ButtonVariance`

| Value | Deprecated | Description |
|---|---|---|
| `FILLED` | No |  |
| `OUTLINED` | No |  |
| `TEXT_ONLY` | No |  |

## `CampaignItemStatus`

The status of the campaign item.

| Value | Deprecated | Description |
|---|---|---|
| `UNASSIGNED` | No |  |
| `SELECTED_FOR_CALLING` | No |  |
| `ASSIGNED` | No |  |
| `IN_PROGRESS` | No |  |
| `COMPLETE` | No |  |
| `REMOVED` | No |  |

## `CampaignStatus`

The status of the campaign. Indicates whether calls can be made for items in the campaign or not.

| Value | Deprecated | Description |
|---|---|---|
| `ACTIVE` | No |  |
| `INACTIVE` | No |  |

## `CatalogComponentStatus`

Status of a catalog component (offering, product, etc.).

| Value | Deprecated | Description |
|---|---|---|
| `DRAFT` | No |  |
| `ACTIVE` | No |  |
| `EXPIRED` | No |  |

## `Category`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `FILE_ATTACHMENT_CUSTOMER_ID` | No |  |

## `ChangeOfTenancyType`

The change of tenancy type (subrogation or transfer) for the supply point.

| Value | Deprecated | Description |
|---|---|---|
| `SUBROGATION` | No |  |
| `TRANSFER` | No |  |

## `Channel`

The set of channels that messages can be sent through.

| Value | Deprecated | Description |
|---|---|---|
| `EMAIL` | No |  |
| `SMS` | No |  |
| `POST` | No |  |
| `ANDROID_PUSH_NOTIFICATION` | No |  |
| `IOS_PUSH_NOTIFICATION` | No |  |

## `ChargingSessionType`

All possible types of charging sessions.

| Value | Deprecated | Description |
|---|---|---|
| `PUBLIC` | No |  |
| `SMART` | No |  |
| `BOOST` | No |  |

## `CheckResultStatus`

| Value | Deprecated | Description |
|---|---|---|
| `PASSED` | No |  |
| `WARNING` | No |  |
| `FAILED` | No |  |

## `ClientType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `APP` | No |  |
| `WEB` | No |  |

## `CollectDepositStatusChoices`

| Value | Deprecated | Description |
|---|---|---|
| `APPROVED` | No |  |
| `CLEARED` | No |  |
| `CANCELLED` | No |  |
| `HELD_FOR_REVIEW` | No |  |
| `FAILED` | No |  |
| `PENDING` | No |  |
| `REQUESTED` | No |  |
| `SCHEDULED` | No |  |
| `NONE` | No |  |

## `CollectionCampaignType`

| Value | Deprecated | Description |
|---|---|---|
| `NONE` | No |  |

## `CollectionMethod`

| Value | Deprecated | Description |
|---|---|---|
| `CARD` | No |  |
| `DIRECT_DEBIT` | No |  |

## `CollectionProcessAssociatedItemType`

Associated item type choices.

| Value | Deprecated | Description |
|---|---|---|
| `TRANSACTIONAL_MESSAGING_TRIGGER` | No |  |
| `CONTRACT_TERMINATION` | No |  |
| `LEAVE_SUPPLIER_PROCESS` | No |  |
| `TRANSACTIONAL_MESSAGING_PUBLISHING_ERROR` | No |  |

## `CollectionProcessEventTypeEnum`

Type of events that can occur in a collection process.

| Value | Deprecated | Description |
|---|---|---|
| `REACTIVATION_PENDING` | No |  |
| `REACTIVATION_COMPLETED` | No |  |
| `TERMINATED_WITHOUT_REACTIVATION` | No |  |

## `CollectionProcessRecordCompletionTypeChoices`

Options for Collection Process Record Completion types. `ENDED`: ended`WITHDRAWN`: withdrawn`CANCELLED`: cancelled`NEVER_ACTIONED`: never_actioned

| Value | Deprecated | Description |
|---|---|---|
| `ENDED` | No |  |
| `WITHDRAWN` | No |  |
| `CANCELLED` | No |  |
| `NEVER_ACTIONED` | No |  |

## `CollectionProcessRecordStatusTypes`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No |  |
| `ACTIVE` | No |  |
| `COMPLETE` | No |  |

## `CollectionProcessTypes`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ACCOUNT` | No |  |
| `BILLING_DOCUMENT` | No |  |
| `LEDGER` | No |  |

## `CommsDeliveryPreference`

The method the account has specified they prefer we contact them

| Value | Deprecated | Description |
|---|---|---|
| `EMAIL` | No |  |
| `POSTAL_MAIL` | No |  |

## `CommunicationMethods`

Preferred communication method.

| Value | Deprecated | Description |
|---|---|---|
| `LANDLINE` | No |  |
| `MOBILE` | No |  |
| `EMAIL` | No |  |
| `POST` | No |  |

## `ComplaintSourceChoices`

Source of the complaint.

| Value | Deprecated | Description |
|---|---|---|
| `TELEPHONE` | No |  |
| `ONLINE` | No |  |
| `PERSON` | No |  |
| `POST` | No |  |
| `SOCIAL_MEDIA` | No |  |
| `CUSTOMER_SURVEY` | No |  |

## `ConnectionStatus`

Connection status of the device, provided as part of the telemetry data.

| Value | Deprecated | Description |
|---|---|---|
| `ONLINE` | No |  |
| `OFFLINE` | No |  |

## `ConsentEventSource`

The possible sources of a consent event.

| Value | Deprecated | Description |
|---|---|---|
| `CONSUMER_SITE` | No |  |
| `SUPPORT_SITE` | No |  |
| `API_SITE` | No |  |
| `THIRD_PARTY_VENDOR` | No |  |
| `ONBOARDING` | No |  |
| `MIGRATION` | No |  |
| `DATA_IMPORT` | No |  |
| `COMMAND_JOB` | No |  |

## `ConsentValue`

The possible values for a consent.

| Value | Deprecated | Description |
|---|---|---|
| `ACCEPTED` | No |  |
| `REJECTED` | No |  |
| `UNKNOWN` | No |  |
| `PENDING` | No |  |

## `ConsumptionUnit`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `kWh` | No |  |
| `MJ` | No |  |
| `L` | No |  |

## `ContractActivityTypeOptions`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ALL_ACTIVITY_TYPES` | No |  |
| `CONTRACT_TERMINATION_STARTED` | No |  |
| `CONTRACT_VARIATION_STARTED` | No |  |

## `ContractJourneyStatus`

The status of the contract journey.

| Value | Deprecated | Description |
|---|---|---|
| `IN_PROGRESS` | No |  |
| `STALLED` | No |  |
| `COMPLETED` | No |  |
| `CANCELLED` | No |  |
| `ERRORED` | No |  |

## `ContractJourneyType`

The type of the contract journey.

| Value | Deprecated | Description |
|---|---|---|
| `CONTRACT_CREATION` | No |  |
| `CONTRACT_TERMINATION` | No |  |
| `CONTRACT_VARIATION` | No |  |

## `ContractStatus`

The status of the contract.

| Value | Deprecated | Description |
|---|---|---|
| `REVOKED` | No |  |
| `ACTIVE` | No |  |
| `EXPIRED` | No |  |
| `TERMINATED` | No |  |
| `INACTIVE` | No |  |
| `JOURNEY_IN_PROGRESS` | No |  |

## `ConversationClosedReasonChoices`

The available reasons for closing a conversation.

| Value | Deprecated | Description |
|---|---|---|
| `AGENT_CLOSED` | No |  |
| `CUSTOMER_CLOSED` | No |  |
| `STALE` | No |  |
| `INACTIVE` | No |  |

## `CustomerFeedbackSourceChoices`

Source of the customer feedback.

| Value | Deprecated | Description |
|---|---|---|
| `FEEDBACK_SOURCE_PHONE_CALL_FOLLOW_UP` | No |  |
| `FEEDBACK_SOURCE_EMAIL_FOLLOW_UP` | No |  |
| `FEEDBACK_SOURCE_TRUSTPILOT` | No |  |
| `FEEDBACK_SOURCE_MANUAL` | No |  |
| `FEEDBACK_SOURCE_LOGIN_FOLLOW_UP` | No |  |
| `FEEDBACK_SOURCE_CONSUMER_SITE` | No |  |

## `CustomerVerificationType`

The verification types available.

| Value | Deprecated | Description |
|---|---|---|
| `EMAIL` | No | Email. |
| `SMS` | No | SMS. |
| `MANUAL` | No | Manual. |
| `OTHER` | No | Other. |

## `CutReason`

The declared reason for the request.

| Value | Deprecated | Description |
|---|---|---|
| `END_ACTIVITY` | No |  |
| `END_CONTRACT` | No |  |
| `CUT_OFF_SUPPLY` | No |  |
| `NON_PAYMENT` | No |  |
| `SAFETY_CONCERN` | No |  |
| `INDEFINITE_PRODUCT_TERMINATION` | No |  |

## `DataFrequency`

The frequency of the cost of charge data to be shown in the consumer app. We are generating this data daily, weekly, monthly or annually, with the following aggregations: daily -> half-hourly aggregation weekly & monthly -> daily aggregations annually -> monthly aggregations

| Value | Deprecated | Description |
|---|---|---|
| `DAILY` | No |  |
| `WEEKLY` | No |  |
| `MONTHLY` | No |  |
| `ANNUALLY` | No |  |

## `DayOfWeek`

Day of the week.

| Value | Deprecated | Description |
|---|---|---|
| `MONDAY` | No |  |
| `TUESDAY` | No |  |
| `WEDNESDAY` | No |  |
| `THURSDAY` | No |  |
| `FRIDAY` | No |  |
| `SATURDAY` | No |  |
| `SUNDAY` | No |  |

## `DebtCollectionProceedingStopReason`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `BANKRUPT` | No | Bankrupt |
| `DECEASED` | No | Deceased |
| `GONE_AWAY` | No | Gone away |
| `IN_PRISON` | No | In prison |
| `NEGATIVE_TRACE` | No | Negative trace |
| `PAID_IN_FULL` | No | Paid in full |
| `PROCESS_EXHAUSTED` | No | Process exhausted |
| `PROCESS_EXHAUSTED_NO_CONTACT` | No | Process exhausted - no contact |
| `PROCESS_EXHAUSTED_CONTACT` | No | Process exhausted - contact |
| `REDUCED_SETTLEMENT` | No | Reduced settlement |
| `VULNERABLE` | No | Vulnerable |
| `WITHDRAWN` | No | Withdrawn |
| `WRITE_OFF` | No | Write off |
| `PAYMENT_ARRANGEMENT` | No | Payment arrangement |
| `PAYMENT_PLAN_AGREED` | No | Payment plan agreed |
| `PART_PAYMENT` | No | Part payment |
| `PPM_ARRANGEMENT` | No | PPM arrangement |
| `PPM_REQUESTED` | No | PPM requested |
| `ARREARS_TO_CLIENT` | No | Arrears to client |
| `HIGH_LEVEL_COMPLAINT` | No | High level complaint |
| `INSOLVENCIES_DEALING` | No | Insolvencies dealing |
| `PARTIAL_SETTLEMENT` | No | Partial settlement |
| `PPM_FITTED` | No | PPM fitted |
| `REFUSED_TO_DEAL` | No | Refused to deal |
| `LIVE_TO_FINAL` | No | Live to final |
| `COT_COS` | No | COT / COS |
| `COS` | No | COS |
| `COT_PROOF_SEEN` | No | COT proof seen |
| `COT_NO_PROOF` | No | COT no proof |
| `ENROLLED_IN_ERROR` | No | Enrolled in Error |
| `LOW_BALANCE` | No | Low balance |
| `EXP` | No | Expired |
| `UNABLE_TO_LOCATE_PROPERTY` | No | Unable to locate property |
| `CONFIRMED_EMPTY` | No | Confirmed empty |
| `DEMOLISHED` | No | Demolished |
| `UNABLE_TO_TRACE` | No | Unable to trace |
| `QUERY` | No | Query |

## `DelayerDaysStrategy`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `FIXED` | No |  |
| `WORKING_DAYS` | No |  |

## `DeletePushNotificationBindingOutput`

| Value | Deprecated | Description |
|---|---|---|
| `SUCCESSFUL` | No |  |
| `FAILED` | No |  |

## `DirectDebitInstructionStatus`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ACTIVE` | No | The instruction is active and can be used to take payments. |
| `PROVISIONAL` | No | The instruction has not yet been set up. |
| `FAILED` | No | The instruction could not be set up with the vendor. |

## `DocumentAccessibilityChoices`

Enum representing document accessibility preferences for an account.

| Value | Deprecated | Description |
|---|---|---|
| `LARGE_PRINT` | No |  |
| `BRAILLE` | No |  |
| `AUDIO` | No |  |

## `ElectricityATRChoices`

The electricity ATR choices type.

| Value | Deprecated | Description |
|---|---|---|
| `TD20` | No | 2.0TD. |
| `TD30` | No | 3.0TD. |
| `TD61` | No | 6.1TD. |
| `TD62` | No | 6.2TD. |
| `TD63` | No | 6.3TD. |
| `TD64` | No | 6.4TD. |
| `TDVE30` | No | 3.0TDVE. |
| `TDVE61` | No | 6.1TDVE. |
| `TDVE62` | No | 6.2TDVE. |
| `TDVE30EMB` | No | 3.0TDVE-Embarcaciones. |
| `TDVE61EMB` | No | 6.1TDVE-Embarcaciones. |
| `TDVE62EMB` | No | 6.2TDVE-Embarcaciones. |

## `EmailFormats`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `TEXT` | No |  |
| `HTML` | No |  |

## `EnergyUnit`

The energy unit.

| Value | Deprecated | Description |
|---|---|---|
| `KILOWATT_HOUR` | No |  |

## `EnodeVendors`

Available vendors supported by Enode.

| Value | Deprecated | Description |
|---|---|---|
| `AUDI` | No |  |
| `BMW` | No |  |
| `CHEVROLET` | No |  |
| `CITROEN` | No |  |
| `CUPRA` | No |  |
| `DS` | No |  |
| `FIAT` | No |  |
| `FORD` | No |  |
| `HYUNDAI` | No |  |
| `JAGUAR` | No |  |
| `KIA` | No |  |
| `MERCEDES` | No |  |
| `MINI` | No |  |
| `NISSAN` | No |  |
| `OPEL` | No |  |
| `PEUGEOT` | No |  |
| `PORSCHE` | No |  |
| `RENAULT` | No |  |
| `SEAT` | No |  |
| `SKODA` | No |  |
| `TOYOTA` | No |  |
| `VAUXHALL` | No |  |
| `VOLKSWAGEN` | No |  |
| `VOLVO` | No |  |

## `EssentialIndicator`

Indicates if the supply is not essential, essential for electrodependency or essential without electrodependency.

| Value | Deprecated | Description |
|---|---|---|
| `NO_ESSENTIAL` | No |  |
| `ESSENTIAL_FOR_ELECTRODEPENDENCY` | No |  |
| `ESSENTIAL_NO_ELECTRODEPENDANT` | No |  |

## `ExpiringTokenScope`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `SUBMIT_METER_READINGS` | No | Scope that enables account user to submit meter readings. |
| `SUBMIT_CUSTOMER_FEEDBACK` | No | Scope that enables account user to submit customer feedback. |
| `BOOK_SMART_METER_APPOINTMENTS` | No | Scope that enables account user to book smart meter appointments. |
| `UPDATE_SMART_METER_INTEREST` | No | Scope that enables account user to update their smart meter interest. |
| `UPDATE_DIRECT_DEBIT` | No | Scope that enables account user to update their direct debit details. |
| `EDIT_CUSTOMER_MARKETING_PREFERENCE` | No | Edit Customer Marketing Preference |
| `JOIN_CAMPAIGNS` | No | Scope that enables account user to join campaigns. |
| `JOIN_CAMPAIGN_EVENTS` | No | Scope that enables account user to join campaign events. |
| `VIEW_CAMPAIGN_DASHBOARDS` | No | Scope that enables account user to visit campaign dashboard. |
| `VIEW_DETAILED_USAGE` | No | Scope that enables account user to visit detailed property usage pages. |
| `REDEEM_LOYALTY_POINTS` | No | Scope that enables account user to redeem loyalty points |
| `MANAGE_ACCOUNT_RENEWALS` | No | Scope that enables account user to generate a renewal quote and renew agreements. |
| `CHECKOUT_QUOTE` | No | Scope that enables account user to checkout a quote (validate terms & conds and provide a payment detail). |
| `UPDATE_BLACKHOLE_EMAIL` | No | Scope that enables account user to update their blackhole email address. |
| `UPDATE_BLACKHOLE_EMAIL_NO_ACCOUNT_NUMBER` | No | Scope that enables account user to update their blackhole email address without enabling access to account number. |
| `UPDATE_SENSITIVE_CUSTOMER_INFORMATION` | No | Update Sensitive Customer Information |
| `MANAGE_GOODS_PURCHASES` | No | Scope that enables account user to accept goods quotes and process goods purchases. |
| `SET_GOODS_PURCHASE_SALE_ITEM_PRICES` | No | Set Goods Purchase Sale Item Prices |
| `REPORT_MOVE_OUT` | No | Scope that enables account user to report a property move-out. |
| `ACCEPT_TERMS_AND_CONDITIONS` | No | Scope that enables account user to accept the terms and conditions for a product. |
| `MANAGE_PRODUCT_SWITCH` | No | Scope that enables account user to do a self-serve product switch through the Dashboard. |
| `MANAGE_PRODUCT_SWITCH_WITH_QUOTES` | No | Scope that enables account user to do a self-serve product switch with quotes. |
| `MANAGE_BUSINESS_SECURITY_DEPOSIT` | No | Scope that enables account user to manage security deposit payments for business accounts. |
| `SEND_LOSS_OBJECTION_FOR_CHANGE_OF_SUPPLIER` | No | Scope that enables user to send a loss objection for a change of supplier process. |
| `UPDATE_ACCOUNT_DETAILS` | No | Scope that enables the user to update information about themselves and their account. |
| `CANCEL_ENROLLMENT` | No | Scope that enables the user to cancel enrollment to a supplier. |
| `VIEW_ACCOUNT_NUMBER` | No | Scope that grants access to view the account number. |
| `ACCEPT_FIT_SCHEDULE` | No | Scope that grants ability to accept fit schedule. |
| `AMEND_PAYMENTS` | No | Scope that grants access to amend payments. |
| `ACCEPT_FIT_TERMS` | No | Scope that grants ability to accept fit terms. |
| `VERIFY_CUSTOMER_DETAILS` | No | Scope that grants ability to verify the customer details. |
| `ACCEPT_QUOTE` | No | Scope that enables user to review and accept a quote sent via an email link. |
| `SUBMIT_FIT_METER_READINGS` | No | Scope that grants ability to submit fit readings for a meter. |
| `ACCESS_CHANGE_MY_TARIFF_EXPIRING_LINK` | No | Scope grants ability to access Change My Tariff journey without login |
| `SUBMIT_MISSING_METER_DETAILS` | No | Scope that enables account user to submit missing meter details. |
| `FINALIZE_ACCOUNT_SETUP` | No | Scope that enables the user to finalize their account setup. |

## `ExternalAccountEventCategory`

Enum of allowable event type categories for external account events.

| Value | Deprecated | Description |
|---|---|---|
| `COMMUNICATIONS` | No |  |
| `WEB` | No |  |
| `MOBILE` | No |  |
| `MESSAGING` | No |  |
| `DEBT` | No |  |
| `SALES` | No |  |
| `SECURITY` | No |  |
| `WORKFLOW` | No |  |

## `ExternalAccountEventContentType`

Enum of allowable content types for external account events. The content type field is used to determine how to display the content in the account event description.

| Value | Deprecated | Description |
|---|---|---|
| `PLAINTEXT` | No |  |
| `LINK` | No |  |
| `HTML` | No |  |
| `S3` | No |  |

## `ExternalAccountEventSubCategory`

Enum of allowable event type subcategories for external account events.

| Value | Deprecated | Description |
|---|---|---|
| `TELEPHONE` | No |  |
| `EMAIL` | No |  |
| `SMS` | No |  |
| `PRINT` | No |  |
| `PUSH_NOTIFICATION` | No |  |
| `SOCIAL_MEDIA` | No |  |
| `FEEDBACK` | No |  |
| `WHATSAPP` | No |  |
| `CLICK_TO_CALL` | No |  |
| `DUNNING` | No |  |
| `THIRD_PARTY` | No |  |
| `INTERNAL` | No |  |
| `LIVE_CHAT` | No |  |
| `PASSWORD_RESET_EMAIL` | No |  |
| `FORCE_LOGOUT` | No |  |
| `DENY_ACCESS` | No |  |
| `UPDATED` | No |  |
| `CREATED` | No |  |

## `FailureReason`

Stable GraphQL API enum for payment failure reasons. These values are decoupled from the domain FailureReason enum to maintain API stability. Note: KRAKEN_ERROR is intentionally excluded as it's internal-only.

| Value | Deprecated | Description |
|---|---|---|
| `PAYMENT_INSTRUCTION_NOT_USABLE` | No |  |
| `PAYER_DECEASED` | No |  |
| `INSUFFICIENT_FUNDS` | No |  |
| `ACTION_REQUIRED` | No |  |
| `CUSTOMER_OBJECTION` | No |  |
| `INSTITUTIONAL_OBJECTION` | No |  |
| `INVALID_AMOUNT` | No |  |
| `SUSPICIOUS` | No |  |
| `INSUFFICIENT_NOTICE` | No |  |
| `PAST_DATE` | No |  |
| `BAD_TIMING` | No |  |
| `VENDOR_SYSTEM_MALFUNCTION` | No |  |
| `UNKNOWN` | No |  |

## `FieldTypeChoices`

The type of the field.

| Value | Deprecated | Description |
|---|---|---|
| `STR` | No |  |
| `INT` | No |  |
| `FLOAT` | No |  |
| `DATE` | No |  |
| `DATETIME` | No |  |
| `BOOL` | No |  |
| `CHOICE` | No |  |
| `MULTIPLE_CHOICE` | No |  |

## `FlexGridExportStatus`

The status of the device's grid export capability.

| Value | Deprecated | Description |
|---|---|---|
| `ENABLED` | No |  |
| `DISABLED` | No |  |
| `NOT_APPLICABLE` | No |  |

## `FlexIsChargingDurationCapped`

The status of the device's charging duration cap.

| Value | Deprecated | Description |
|---|---|---|
| `ENABLED` | No |  |
| `DISABLED` | No |  |
| `NOT_APPLICABLE` | No |  |

## `FormType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `COVID_19_FINANCIAL_ENERGY_ASSESSMENT` | No | Covid-19 Financial Energy Assessment |
| `COVID_19_GAS_PRICES_FINANCIAL_ENERGY_ASSESSMENT` | No | Covid-19 Gas Prices Financial Energy Assessment |

## `FulfilmentSourceType`

The type of the fulfilment source.

| Value | Deprecated | Description |
|---|---|---|
| `UNKNOWN` | No |  |
| `CREDIT` | No |  |
| `PAYMENT` | No |  |
| `CHARGE` | No |  |

## `FunnelStatusChoices`

The status of the funnel.

| Value | Deprecated | Description |
|---|---|---|
| `DRAFT` | No |  |
| `ACTIVE` | No |  |
| `DEPRECATED` | No |  |

## `FunnelTypeChoices`

The type of the funnels to get the schema for.

| Value | Deprecated | Description |
|---|---|---|
| `LEAD` | No |  |
| `OPPORTUNITY` | No |  |

## `GuaranteeOfOriginPercentage`

The percentage of the guarantee of origin.

| Value | Deprecated | Description |
|---|---|---|
| `ZERO` | No |  |
| `TWENTY_FIVE` | No |  |
| `FIFTY` | No |  |
| `SEVENTY_FIVE` | No |  |
| `ONE_HUNDRED` | No |  |

## `HardshipAgreementExitReason`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `INITIAL_PAYMENT_PLAN_NOT_ESTABLISHED` | No | Initial payment plan not established |
| `CUSTOMER_REQUEST` | No | Customer request |
| `PAYMENT_PLAN_BROKEN_FOR_NON_PAYMENT` | No | Payment plan broken for non-payment |
| `PAYMENT_PLAN_COMPLETED_SUCCESSFULLY` | No | Payment plan completed successfully |
| `FURTHER_PAYMENT_PLAN_NOT_ESTABLISHED` | No | Further payment plan not established |
| `ACCOUNT_FINALISED` | No | Account finalised |
| `RAISED_IN_ERROR` | No | Raised in Error |
| `NO_ENGAGEMENT` | No | No Engagement |
| `CREDIT_OR_NIL_BALANCE` | No | Credit or nil balance |
| `OTHER` | No | Other |

## `HardshipAgreementHardshipEntryReason`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `SELF_IDENTIFIED` | No | Customer self-identified as being in hardship |
| `EXTERNAL_REFERENCE` | No | Financial counsellor or external agent referral |
| `RETAILER_REFERRAL` | No | Retailer referral |

## `HardshipAgreementHardshipType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `DEATH_IN_FAMILY` | No | Death in the family |
| `HOUSEHOLD_ILLNESS` | No | Household illness |
| `FAMILY_VIOLENCE` | No | Family violence |
| `UNEMPLOYMENT` | No | Unemployment |
| `REDUCED_INCOME` | No | Reduced income |
| `OTHER` | No | Other |

## `InkCommunicationChannel`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `EMAIL` | No |  |
| `SMS` | No |  |
| `POST` | No |  |
| `GENERIC_API` | No |  |
| `WHATSAPP` | No |  |

## `InkConversationStatus`

| Value | Deprecated | Description |
|---|---|---|
| `OPEN` | No |  |
| `OPEN_NEW` | No |  |
| `OPEN_CUSTOMER_REPLIED` | No |  |
| `OPEN_REMINDED` | No |  |
| `SNOOZED` | No |  |
| `CLOSED` | No |  |

## `InkMessageDeliveryStatus`

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No |  |
| `SENT` | No |  |
| `DELIVERED` | No |  |
| `FAILED` | No |  |
| `OUTSIDE_REPLY_WINDOW` | No |  |

## `InkMessageDirection`

| Value | Deprecated | Description |
|---|---|---|
| `INBOUND` | No |  |
| `OUTBOUND` | No |  |

## `IntegrationStatus`

| Value | Deprecated | Description |
|---|---|---|
| `INTERNAL_TESTING` | No |  |
| `TESTING` | No | Testing - The device is in testing status. |
| `NOT_AVAILABLE` | No | Not Available - The device is not available. |
| `GENERALLY_AVAILABLE` | No | Generally Available - The device is available. |

## `Interval`

The frequency at which contributations are made

| Value | Deprecated | Description |
|---|---|---|
| `MONTHLY` | No |  |
| `QUARTERLY` | No |  |

## `KrakenFlexDeviceTypes`

The device types that can be controlled by KrakenFlex.

| Value | Deprecated | Description |
|---|---|---|
| `BATTERIES` | No |  |
| `ELECTRIC_VEHICLES` | No |  |
| `INVERTERS` | No |  |
| `HEAT_PUMPS` | No |  |
| `STORAGE_HEATERS` | No |  |
| `ELECTRICITY_METERS` | No |  |
| `THERMOSTATS` | No |  |

## `LeadContactRoles`

The roles a contact has in relation to their lead.

| Value | Deprecated | Description |
|---|---|---|
| `LEGAL_CONTACT` | No |  |
| `COMMUNICATIONS_CONTACT` | No |  |
| `OTHER_CONTACT` | No |  |

## `LeadTypeChoices`

The type of the lead.

| Value | Deprecated | Description |
|---|---|---|
| `BUSINESS` | No |  |
| `DOMESTIC` | No |  |

## `LeaveSupplierSubType`

Indicates the type of a leave supplier process.

| Value | Deprecated | Description |
|---|---|---|
| `MOVE_OUT` | No |  |
| `DEMIGRATION` | No |  |

## `LifecycleProcessesSortOrder`

| Value | Deprecated | Description |
|---|---|---|
| `ASC` | No |  |
| `DESC` | No |  |

## `LifecycleSupplyPointProcessStatus`

The status of the lifecycle process.

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No |  |
| `IN_PROGRESS` | No |  |
| `COMPLETED` | No |  |
| `PARTIALLY_COMPLETED` | No |  |
| `NEEDS_ATTENTION` | No |  |
| `STALLED` | No |  |
| `FAILED` | No |  |
| `ERRORED` | No |  |
| `CANCELLATION_IN_PROGRESS` | No |  |
| `CANCELLED` | No |  |
| `PARTIALLY_CANCELLED` | No |  |
| `CANCELLATION_STALLED` | No |  |
| `CANCELLATION_ERRORED` | No |  |
| `CANCELLATION_FAILED` | No |  |
| `REVERSAL_IN_PROGRESS` | No |  |
| `REVERSE_IN_PROGRESS` | No |  |
| `REVERSED` | No |  |
| `PARTIALLY_REVERSED` | No |  |
| `REVERSAL_STALLED` | No |  |
| `REVERSAL_ERRORED` | No |  |
| `REVERSAL_FAILED` | No |  |

## `LineLinkErrorType`

| Value | Deprecated | Description |
|---|---|---|
| `NO_MATCHING_LINE_LINK` | No |  |
| `ALREADY_LINKED` | No |  |

## `LinkTrainingStatus`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `NOT_APPLICABLE` | No | Not applicable |
| `IN_TRAINING` | No | In training |
| `QUALIFIED` | No | Qualified |

## `LinkedObjectType`

| Value | Deprecated | Description |
|---|---|---|
| `ACCOUNT` | No |  |
| `ACCOUNT_USER` | No |  |

## `LoyaltyPointAwardEntryReasonCode`

The reason code associated with the loyalty points entry.

| Value | Deprecated | Description |
|---|---|---|
| `POINTS_AWARDED_FOR_ACCOUNT_ACTION` | No |  |

## `LoyaltyPointDeductionEntryReasonCode`

The reason code associated with the loyalty points entry.

| Value | Deprecated | Description |
|---|---|---|
| `POINTS_DEDUCTED_FOR_ACCOUNT_ACTION` | No |  |

## `MFAMethodChoices`

MFA enrolment method choices.

| Value | Deprecated | Description |
|---|---|---|
| `EMAIL` | No | Email. |
| `TOTP` | No | Totp. |
| `SMS` | No | Sms. |

## `MarketName`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ESP_ELECTRICITY` | No |  |
| `ESP_GAS` | No |  |
| `SIMPLE_SERVICES` | No |  |

## `MaximumRefundReasonChoices`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `MAX_AVAILABLE_AMOUNT` | No | Maximum refund is equal to the current balance minus the account recommended balance. |
| `TOTAL_AMOUNT_PAID_VIA_ACTIVE_DDI` | No | Maximum refund is equal to the total amount the customer has paid using the current account Direct Debit instruction. |
| `MAX_ALLOWED_TO_REQUEST_VIA_DASHBOARD` | No | Maximum refund is equal to the maximum refund amount allowed to be requested via the dashboard. |

## `NoYes`

Yes or no.

| Value | Deprecated | Description |
|---|---|---|
| `NO` | No | No. |
| `YES` | No | Sí. |

## `NoticePriority`

| Value | Deprecated | Description |
|---|---|---|
| `HIGH` | No |  |
| `NORMAL` | No |  |

## `NotifiableApplicationExternalProvider`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `PINPOINT` | No | AWS Pinpoint |

## `NotifiableApplicationService`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `GCM` | No | Android (GCM) |
| `APNS` | No | iOS (APNs) |
| `APNS_SANDBOX` | No | iOS Sandbox (APNs Sandbox) |

## `OnSiteJobsAgent`

| Value | Deprecated | Description |
|---|---|---|
| `GENERIC_AGENT` | No |  |
| `TTE_FACILITA` | No |  |
| `SMS` | No |  |
| `AES` | No |  |
| `OES` | No |  |
| `PROVIDOR` | No |  |
| `MDS` | No |  |
| `EON_METERING` | No |  |
| `LOWRI_BECK` | No |  |
| `METERPLUS` | No |  |
| `ENTERPRISE_MANAGED` | No |  |
| `MIDS_ELEC` | No |  |
| `N_POWERGRID` | No |  |
| `ELEC_NW` | No |  |
| `NATIONAL_GRID` | No |  |
| `SGN` | No |  |
| `ENERGY_ASSETS` | No |  |
| `SIEMENS` | No |  |
| `LONDON` | No |  |
| `ECM` | No |  |
| `OESL` | No |  |
| `EDF_FIELD` | No |  |
| `ESSENTIAL_FIELD` | No |  |

## `OnSiteJobsAppointmentActionTriggerStage`

| Value | Deprecated | Description |
|---|---|---|
| `POST_APPOINTMENT_BOOKING` | No |  |
| `POST_APPOINTMENT_COMPLETION` | No |  |
| `POST_APPOINTMENT_CANCELLATION` | No |  |
| `POST_APPOINTMENT_ABORTED` | No |  |
| `OTHER` | No |  |

## `OnSiteJobsAppointmentCancellationCategory`

Appointment cancellation category with any subcategories in the format of 'CATEGORY___SUB_CATEGORY'. For categories without subcategories, just 'CATEGORY'.

| Value | Deprecated | Description |
|---|---|---|
| `CANCELLED_BY_SUPPLIER___CUSTOMER_CHANGING_SUPPLIER` | No |  |

## `OnSiteJobsAppointmentStatus`

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No |  |
| `BOOKED` | No |  |
| `DISPATCHED` | No |  |
| `EN_ROUTE` | No |  |
| `ON_SITE` | No |  |
| `CANCELLED` | No |  |
| `ABORTED` | No |  |
| `PARTIALLY_COMPLETE` | No |  |
| `COMPLETED` | No |  |

## `OnSiteJobsAssetFuelType`

| Value | Deprecated | Description |
|---|---|---|
| `ELECTRICITY` | No |  |
| `GAS` | No |  |

## `OnSiteJobsAssetKind`

| Value | Deprecated | Description |
|---|---|---|
| `METER` | No |  |
| `HEAT_PUMP` | No |  |
| `WATER_HEATER` | No |  |

## `OnSiteJobsAssetStatus`

| Value | Deprecated | Description |
|---|---|---|
| `EXISTING` | No |  |
| `REQUESTED` | No |  |
| `INSTALLED` | No |  |

## `OnSiteJobsCancellationCategory`

| Value | Deprecated | Description |
|---|---|---|
| `CANCELLED_BY_CUSTOMER` | No |  |
| `CANCELLED_BY_BUSINESS` | No |  |
| `CANCELLED_BY_SUPPLIER` | No |  |
| `CANCELLED_BY_PROVIDER` | No |  |

## `OnSiteJobsCommsStrategy`

| Value | Deprecated | Description |
|---|---|---|
| `SEND_ALL` | No |  |
| `SEND_ONLY_JOB_COMPLETED` | No |  |
| `SUPPRESS_ALL` | No |  |

## `OnSiteJobsReporterCategory`

| Value | Deprecated | Description |
|---|---|---|
| `CUSTOMER` | No |  |
| `UNKNOWN` | No |  |

## `OnSiteJobsRequestActionTriggerStage`

| Value | Deprecated | Description |
|---|---|---|
| `POST_REQUEST_COMPLETION` | No |  |

## `OnSiteJobsRequestStatus`

Request status.

| Value | Deprecated | Description |
|---|---|---|
| `APPROVAL_ON_HOLD` | No |  |
| `APPOINTMENT_FAILED` | No |  |
| `APPROVAL_REJECTED` | No |  |
| `CANCELLED` | No |  |
| `BOOKED` | No |  |
| `COMPLETED` | No |  |
| `IN_PROGRESS` | No |  |
| `APPROVAL_PENDING` | No |  |
| `PENDING` | No |  |
| `HELD` | No |  |

## `OnSiteJobsWorkCategory`

| Value | Deprecated | Description |
|---|---|---|
| `EXCHANGE` | No |  |
| `MOVE` | No |  |
| `NEW_CONNECTION` | No |  |
| `REMOVE` | No |  |
| `REINSTALL` | No |  |
| `INVESTIGATE_FAULT` | No |  |
| `IHD_INSTALL` | No |  |
| `COMMISSION` | No |  |
| `COMMS_HUB_POWER_CYCLE` | No |  |
| `COMMS_HUB_REPLACEMENT` | No |  |
| `METER_TAILS_UPGRADE` | No |  |
| `ISOLATOR_SWITCH_INSTALL` | No |  |
| `ACCURACY_TEST` | No |  |
| `BRACKET_INSTALLATION` | No |  |
| `CONFIRM_METER_DETAILS` | No |  |
| `REPLACE_SEALS` | No |  |
| `ENERGISE` | No |  |
| `DE_ENERGISE` | No |  |
| `EV` | No |  |
| `OTHER` | No |  |
| `AD_HOC_READING` | No |  |
| `INTERNAL` | No |  |
| `SUPPLY_SERVICE_WORKS` | No |  |
| `METERING_SERVICE_WORKS` | No |  |
| `SEWER` | No |  |
| `WATER` | No |  |

## `OnSiteJobsWorkflowStatus`

The status of the workflow.

| Value | Deprecated | Description |
|---|---|---|
| `SKIPPED` | No |  |
| `COMPLETED` | No |  |
| `PENDING` | No |  |
| `IN_PROGRESS` | No |  |
| `STALLED` | No |  |
| `CANCELLED` | No |  |
| `FAILED` | No |  |
| `ERRORED` | No |  |

## `OpportunityAttachmentCategory`

The category of the opportunity attachment.

| Value | Deprecated | Description |
|---|---|---|
| `LEAD_FILE` | No |  |

## `OpportunityOutcome`

The possible outcome of the opportunity.

| Value | Deprecated | Description |
|---|---|---|
| `WON` | No |  |
| `LOST` | No |  |

## `OrderStatus`

The status of the order.

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No |  |
| `COMPLETED` | No |  |
| `CANCELLED` | No |  |
| `ERRORED` | No |  |

## `PaymentActionIntentTargetType`

The type of target the intent's payment should be associated with.

| Value | Deprecated | Description |
|---|---|---|
| `ledger` | No |  |

## `PaymentDayDirectionType`

| Value | Deprecated | Description |
|---|---|---|
| `OF_MONTH` | No | The payment day is calculated forward. |
| `BEFORE_END_OF_MONTH` | No | The payment day is calculated backwards from the last day of the month. |

## `PaymentFrequencyOptions`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `Weekly` | No | Weekly |
| `Monthly` | No | Monthly |
| `Planned` | No | Planned |

## `PaymentInstructionOwnerTypeChoices`

Available options for the type of entity a payment instruction owner may be.

| Value | Deprecated | Description |
|---|---|---|
| `ACCOUNT_USER` | No |  |
| `BUSINESS` | No |  |

## `PaymentInstructionStatus`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ACTIVE` | No | The instruction is active and can be used to take payments. |
| `PROVISIONAL` | No | The instruction has not yet been set up. |
| `FAILED` | No | The instruction could not be set up with the vendor. |

## `PaymentIntentCompletionStatus`

| Value | Deprecated | Description |
|---|---|---|
| `CLEARED` | No |  |
| `PENDING` | No |  |

## `PaymentReasonOptions`

| Value | Deprecated | Description |
|---|---|---|
| `BALANCE_THRESHOLD_CROSSED` | No |  |
| `BILL_ISSUED` | No |  |
| `PAYMENT_PLAN` | No |  |
| `REGULAR_SCHEDULE` | No |  |

## `PaymentScheduleReasonOptions`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `GENERAL_ACCOUNT_PAYMENT` | No | The default value for usual account payments. |
| `SSD_PAYMENT` | No | A payment schedule created to take a payment around the supply start date of a meterpoint to help prevent accounts accruing debt. |
| `FINAL_PAYMENT` | No | A payment schedule created to take the final payment when an account is closed. |
| `DEBT_REPAYMENT_PLAN` | No | A payment schedule created to take payments to pay back a debt. These schedules typically expire once the debt has been re-payed. |

## `PaymentType`

Possible payment instruction types.

| Value | Deprecated | Description |
|---|---|---|
| `BPAY` | No |  |
| `CARD` | No |  |
| `DIRECT_DEBIT` | No |  |
| `GMO_REFUND` | No |  |
| `PAYMENT_SLIP` | No |  |

## `PersonType`

The declared person type for the request.

| Value | Deprecated | Description |
|---|---|---|
| `F` | No | Physical person. |
| `J` | No | Legal person. |

## `PreSignedTokenScope`

Choices class for the pre-signed expiring tokens. These choices must have a certain format: {ACTION-VERB}_{DEFINING-NOUN} They should start with an action verb. It should be a single word. The action verb enables the account user to do the thing (defining noun) that comes after the action verb. Together they represent a task. The defining noun could be longer than a single word. Preferably, it should be kept short and simple as much as possible.

| Value | Deprecated | Description |
|---|---|---|
| `SUBMIT_METER_READINGS` | No | Scope that enables account user to submit meter readings. |
| `SUBMIT_CUSTOMER_FEEDBACK` | No | Scope that enables account user to submit customer feedback. |
| `BOOK_SMART_METER_APPOINTMENTS` | No | Scope that enables account user to book smart meter appointments. |
| `UPDATE_SMART_METER_INTEREST` | No | Scope that enables account user to update their smart meter interest. |
| `UPDATE_DIRECT_DEBIT` | No | Scope that enables account user to update their direct debit details. |
| `EDIT_CUSTOMER_MARKETING_PREFERENCE` | No | Edit Customer Marketing Preference |
| `JOIN_CAMPAIGNS` | No | Scope that enables account user to join campaigns. |
| `JOIN_CAMPAIGN_EVENTS` | No | Scope that enables account user to join campaign events. |
| `VIEW_CAMPAIGN_DASHBOARDS` | No | Scope that enables account user to visit campaign dashboard. |
| `VIEW_DETAILED_USAGE` | No | Scope that enables account user to visit detailed property usage pages. |
| `REDEEM_LOYALTY_POINTS` | No | Scope that enables account user to redeem loyalty points |
| `MANAGE_ACCOUNT_RENEWALS` | No | Scope that enables account user to generate a renewal quote and renew agreements. |
| `CHECKOUT_QUOTE` | No | Scope that enables account user to checkout a quote (validate terms & conds and provide a payment detail). |
| `UPDATE_BLACKHOLE_EMAIL` | No | Scope that enables account user to update their blackhole email address. |
| `UPDATE_BLACKHOLE_EMAIL_NO_ACCOUNT_NUMBER` | No | Scope that enables account user to update their blackhole email address without enabling access to account number. |
| `UPDATE_SENSITIVE_CUSTOMER_INFORMATION` | No | Update Sensitive Customer Information |
| `MANAGE_GOODS_PURCHASES` | No | Scope that enables account user to accept goods quotes and process goods purchases. |
| `SET_GOODS_PURCHASE_SALE_ITEM_PRICES` | No | Set Goods Purchase Sale Item Prices |
| `REPORT_MOVE_OUT` | No | Scope that enables account user to report a property move-out. |
| `ACCEPT_TERMS_AND_CONDITIONS` | No | Scope that enables account user to accept the terms and conditions for a product. |
| `MANAGE_PRODUCT_SWITCH` | No | Scope that enables account user to do a self-serve product switch through the Dashboard. |
| `MANAGE_PRODUCT_SWITCH_WITH_QUOTES` | No | Scope that enables account user to do a self-serve product switch with quotes. |
| `MANAGE_BUSINESS_SECURITY_DEPOSIT` | No | Scope that enables account user to manage security deposit payments for business accounts. |
| `SEND_LOSS_OBJECTION_FOR_CHANGE_OF_SUPPLIER` | No | Scope that enables user to send a loss objection for a change of supplier process. |
| `UPDATE_ACCOUNT_DETAILS` | No | Scope that enables the user to update information about themselves and their account. |
| `CANCEL_ENROLLMENT` | No | Scope that enables the user to cancel enrollment to a supplier. |
| `VIEW_ACCOUNT_NUMBER` | No | Scope that grants access to view the account number. |
| `ACCEPT_FIT_SCHEDULE` | No | Scope that grants ability to accept fit schedule. |
| `AMEND_PAYMENTS` | No | Scope that grants access to amend payments. |
| `ACCEPT_FIT_TERMS` | No | Scope that grants ability to accept fit terms. |
| `VERIFY_CUSTOMER_DETAILS` | No | Scope that grants ability to verify the customer details. |
| `ACCEPT_QUOTE` | No | Scope that enables user to review and accept a quote sent via an email link. |
| `SUBMIT_FIT_METER_READINGS` | No | Scope that grants ability to submit fit readings for a meter. |
| `ACCESS_CHANGE_MY_TARIFF_EXPIRING_LINK` | No | Scope grants ability to access Change My Tariff journey without login |
| `SUBMIT_MISSING_METER_DETAILS` | No | Scope that enables account user to submit missing meter details. |
| `FINALIZE_ACCOUNT_SETUP` | No | Scope that enables the user to finalize their account setup. |

## `PreferencesModeChoices`

The mode for a user's preferences.

| Value | Deprecated | Description |
|---|---|---|
| `CHARGE` | No |  |
| `COOL` | No |  |
| `HEAT` | No |  |

## `PreferencesTargetType`

The target type for a user's preferences.

| Value | Deprecated | Description |
|---|---|---|
| `ABSOLUTE_STATE_OF_CHARGE` | No |  |
| `RELATIVE_STATE_OF_CHARGE` | No |  |
| `ABSOLUTE_TEMPERATURE` | No |  |

## `PreferencesUnitChoices`

The unit for a user's preferences (e.g. `min` and `max`). The `PERCENTAGE_ABSOLUTE` and `PERCENTAGE_RELATIVE` values are deprecated and should not be used - `PERCENTAGE` should be used instead.

| Value | Deprecated | Description |
|---|---|---|
| `CELSIUS` | No |  |
| `PERCENTAGE` | No |  |
| `PERCENTAGE_ABSOLUTE` | No |  |
| `PERCENTAGE_RELATIVE` | No |  |

## `PrintBatchStatus`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `OPEN` | No |  |
| `CLOSED` | No |  |
| `PROCESSED` | No |  |

## `ProductAvailability`

The product availability type.

| Value | Deprecated | Description |
|---|---|---|
| `EVERYONE` | No |  |
| `RESTRICTED` | No |  |

## `ProductAvailabilityStatus`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `PUBLIC` | No | No restrictions |
| `RESTRICTED` | No | Restricted |

## `ProductType`

Type of product (e.g., supply, goods).

| Value | Deprecated | Description |
|---|---|---|
| `SUPPLY` | No |  |
| `GOODS` | No |  |

## `ProviderChoices`

This refers to the provider that is used to authenticate when registering a device.

| Value | Deprecated | Description |
|---|---|---|
| `BYD` | No |  |
| `DAIKIN` | No |  |
| `DAIKIN_LCM` | No |  |
| `ECOBEE` | No |  |
| `ECOBEE_V2` | No |  |
| `ENERGIZER` | No |  |
| `ENODE` | No |  |
| `ENPHASE` | No |  |
| `FORD` | No |  |
| `GIVENERGY` | No |  |
| `HUAWEI` | No |  |
| `HUAWEI_V2` | No |  |
| `HYPERVOLT` | No |  |
| `INDRA` | No |  |
| `JEDLIX` | No |  |
| `JEDLIX_V2` | No |  |
| `MERCEDES` | No |  |
| `MYENERGI` | No |  |
| `MYENERGI_V2` | No |  |
| `NATURE` | No |  |
| `OCPP_WALLBOX` | No |  |
| `OCPP` | No |  |
| `OCTOPUS_ENERGY` | No |  |
| `OHME` | No |  |
| `OHME_V2` | No |  |
| `SENSI` | No |  |
| `SENSI_V2` | No |  |
| `SMARTCAR` | No |  |
| `SMARTFLEX_CONNECT` | No |  |
| `SMART_PEAR` | No |  |
| `SOLAREDGE` | No |  |
| `TESLA` | No |  |
| `TESLA_V2` | No |  |
| `VOLKSWAGEN` | No |  |
| `VP_AMAZON` | No |  |
| `VP_HONEYWELL_CC` | No |  |
| `VP_HONEYWELL_RES` | No |  |
| `VP_NEST` | No |  |

## `Provinces`

The provinces type.

| Value | Deprecated | Description |
|---|---|---|
| `ALAVA` | No | Álava/Araba. |
| `ALBACETE` | No | Albacete. |
| `ALICANTE` | No | Alicante/Alacant. |
| `ALMERIA` | No | Almería. |
| `ASTURIAS` | No | Asturias. |
| `AVILA` | No | Ávila. |
| `BADAJOZ` | No | Badajoz. |
| `BALEARES` | No | Balears, Illes. |
| `BARCELONA` | No | Barcelona. |
| `BURGOS` | No | Burgos. |
| `CACERES` | No | Cáceres. |
| `CADIZ` | No | Cádiz. |
| `CANTABRIA` | No | Cantabria. |
| `CASTELLON` | No | Castellón/Castelló. |
| `CIUDAD` | No | Ciudad Real. |
| `CORDOBA` | No | Córdoba. |
| `CORUNA` | No | Coruña, A. |
| `CUENCA` | No | Cuenca. |
| `GIRONA` | No | Gerona/Girona. |
| `GRANADA` | No | Granada. |
| `GUADALAJARA` | No | Guadalajara. |
| `GUIPUZCOA` | No | Guipúzcoa/Gipuzkoa. |
| `HUELVA` | No | Huelva. |
| `HUESCA` | No | Huesca. |
| `JAEN` | No | Jaén. |
| `LEON` | No | León. |
| `LLEIDA` | No | Lérida/Lleida. |
| `RIOJA` | No | Rioja, La. |
| `LUGO` | No | Lugo. |
| `MADRID` | No | Madrid. |
| `MALAGA` | No | Málaga. |
| `MURCIA` | No | Murcia. |
| `NAVARRA` | No | Navarra. |
| `ORENSE` | No | Orense/Ourense. |
| `PALENCIA` | No | Palencia. |
| `PALMAS` | No | Palmas, Las. |
| `PONTEVEDRA` | No | Pontevedra. |
| `SALAMANCA` | No | Salamanca. |
| `TENERIFE` | No | Santa Cruz de Tenerife. |
| `SEGOVIA` | No | Segovia. |
| `SEVILLA` | No | Sevilla. |
| `SORIA` | No | Soria. |
| `TARRAGONA` | No | Tarragona. |
| `TERUEL` | No | Teruel. |
| `TOLEDO` | No | Toledo. |
| `VALENCIA` | No | Valencia/València. |
| `VALLADOLID` | No | Valladolid. |
| `VIZCAYA` | No | Vizcaya/Bizkaia. |
| `ZAMORA` | No | Zamora. |
| `ZARAGOZA` | No | Zaragoza. |
| `CEUTA` | No | Ceuta. |
| `MELILLA` | No | Melilla. |

## `ReadingDirectionType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `CONSUMPTION` | No | Reading is based on the customer's usage of the utility. |
| `GENERATION` | No | Reading is based on the utility generated by the customer. For example: This will return solar readings if a customer has solar panels installed at their location. |

## `ReadingFrequencyType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `RAW_INTERVAL` | No | Interval Readings as provided, may be variable in length. |
| `FIVE_MIN_INTERVAL` | No | Readings taken in every 5 minute intervals. |
| `FIFTEEN_MIN_INTERVAL` | No | Readings taken in every 15 minute intervals. |
| `THIRTY_MIN_INTERVAL` | No | Readings taken in every 30 minute intervals. |
| `HOUR_INTERVAL` | No | Readings taken in every 1 hour intervals. |
| `DAY_INTERVAL` | No |  |
| `WEEK_INTERVAL` | No | Readings taken in every 1 week intervals. |
| `MONTH_INTERVAL` | No | Readings taken in every 1 month intervals. |
| `QUARTER_INTERVAL` | No | Readings taken in every 3 months intervals. |
| `DAILY` | No | Readings taken on a day to day basis. |
| `POINT_IN_TIME` | No | Readings taken at a point in time. |
| `INTERVALIZED` | No | Readings taken at a point in time and intervalized. |

## `ReadingQualityType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ACTUAL` | No |  |
| `ESTIMATE` | No |  |
| `COMBINED` | No |  |

## `ReadingStatisticTypeEnum`

The type of statistic for the reading interval.

| Value | Deprecated | Description |
|---|---|---|
| `STANDING_CHARGE_COST` | No | The calculated cost of standing charges for the interval. |
| `CONSUMPTION_COST` | No | The calculated cost of consumption for the interval. |
| `CAPACITY_CHARGE_COST` | No | The calculated cost of capacity charges for the interval. |
| `CONSUMPTION_BREAKDOWN` | No | The breakdown of consumption into time of use buckets. |
| `GENERATION_VALUE` | No | The calculated monetary value of generation for the interval |
| `TOU_BUCKET_COST` | No | The apportion cost of a time of use bucket for the interval. |
| `CARBON_COST` | No | The estimated carbon cost of the interval. |
| `GAS_READING_INFORMATION` | No | Information related to a gas reading eg. conversion_factor, volume etc. |
| `POWER_FACTOR_STATISTIC` | No | The calculated power factor for the interval. |
| `CO2_EMISSION_STATISTIC` | No | The calculated co2 emission for the interval. |

## `ReadingTypes`

Available reading types.

| Value | Deprecated | Description |
|---|---|---|
| `INTERVAL` | No | Readings indicating total consumption or generation of a utility between two points in time. |
| `ACCUMULATION` | No | Readings indicating total utility consumption since the meter was installed or reset. |
| `PEAK` | No | Readings indicating the maximum rate of utility transfer. |

## `ReferralSchemeAccountTypeOptions`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `DOMESTIC` | No |  |
| `BUSINESS` | No |  |

## `ReferralSchemeTypeChoices`

Referral scheme type choices.

| Value | Deprecated | Description |
|---|---|---|
| `REFERRAL_REWARD` | No | Referral Reward. |
| `SIGNUP_REWARD` | No | Signup Reward. |
| `PARTNER_REWARD` | No | Partner Reward. |
| `PROMO_REWARD` | No | Promo Reward. |
| `LEGACY_REFERRAL` | No | Legacy Referral. |

## `ReferralStatus`

Status of a referral.

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No |  |
| `PAID` | No |  |
| `CANCELLED` | No |  |

## `ReferralStatusChoices`

Referral status choices.

| Value | Deprecated | Description |
|---|---|---|
| `Pending` | No | Pending. |
| `Paid` | No | Paid. |
| `Cancelled` | No | Cancelled. |

## `RepaymentMethod`

Methods by which repayments can be sent to the customer.

| Value | Deprecated | Description |
|---|---|---|
| `BANK_TRANSFER` | No |  |
| `CHEQUE` | No |  |
| `CARD` | No |  |

## `RepaymentRequestStatus`

Possible status' for a repayment (or refund) request

| Value | Deprecated | Description |
|---|---|---|
| `REQUESTED` | No |  |
| `ACCEPTED` | No |  |
| `CANCELLED` | No |  |
| `REJECTED` | No |  |

## `RequestStatus`

Request status.

| Value | Deprecated | Description |
|---|---|---|
| `APPROVAL_PENDING` | No |  |
| `APPROVAL_ON_HOLD` | No |  |
| `APPROVAL_REJECTED` | No |  |
| `HELD` | No |  |
| `PENDING` | No |  |
| `BOOKED` | No |  |
| `IN_PROGRESS` | No |  |
| `APPOINTMENT_FAILED` | No |  |
| `CANCELLED` | No |  |
| `COMPLETED` | No |  |

## `RequestableRepaymentMethod`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `BANK_TRANSFER` | No |  |
| `CHEQUE` | No |  |

## `RequestedDateType`

The requested date type for the supply point.

| Value | Deprecated | Description |
|---|---|---|
| `AS_SOON_AS_POSSIBLE` | No |  |
| `NEXT_READING_CYCLE` | No |  |
| `FIXED_DATE` | No |  |

## `RolloverStatus`

Status of an agreement rollover.

| Value | Deprecated | Description |
|---|---|---|
| `PENDING` | No |  |
| `REJECTED` | No |  |
| `ENQUEUED` | No |  |
| `ERROR` | No |  |
| `DONE` | No |  |
| `REVOKED` | No |  |

## `SalesChannelChoices`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `SOLAR_SALES` | No |  |
| `AFFILIATE` | No |  |
| `DIRECT` | No |  |
| `PRICE_COMPARISON` | No |  |
| `TELESALES` | No |  |
| `DIGI_TELESALES` | No |  |
| `EVENTS` | No |  |
| `FIELD_SALES` | No |  |
| `AGGREGATOR` | No |  |
| `PARTNERSHIPS` | No |  |
| `NEW_TENANT` | No |  |
| `MOVE_IN` | No |  |
| `WORKPLACE_POP_UP` | No |  |
| `BROKER` | No |  |
| `PARENT_POWER` | No |  |
| `PEOPLE_POWER` | No |  |
| `GIFT_OF_KIT` | No |  |
| `HIGH_REFERRER` | No |  |
| `SUPPLIER_OF_LAST_RESORT` | No |  |
| `ACQUISITION` | No |  |
| `WORKS_WITH_OCTOPUS` | No |  |
| `LANDLORD` | No |  |
| `DEBT_COLLECTION_AGENCY` | No |  |

## `ScheduleFrequencyEnum`

The based unit of frequency at which payments are to be taken.

| Value | Deprecated | Description |
|---|---|---|
| `WEEKLY` | No |  |
| `MONTHLY` | No |  |

## `ScheduleTrigger`

| Value | Deprecated | Description |
|---|---|---|
| `PLAN` | No |  |
| `REGULAR` | No |  |
| `REGULAR_PLAN` | No |  |
| `BALANCE` | No |  |
| `BILL` | No |  |

## `ScheduleType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `BACS_TRANSFER` | No |  |
| `CARD_PAYMENT` | No |  |
| `DIRECT_DEBIT` | No |  |
| `PAYMENT_SLIP` | No |  |

## `SelectIntegrationChoices`

For when both the EV and charge point have an integration available.

| Value | Deprecated | Description |
|---|---|---|
| `ELECTRIC_VEHICLE` | No |  |
| `CHARGE_POINT` | No |  |

## `SelfConsumptionType`

The self consumptions type.

| Value | Deprecated | Description |
|---|---|---|
| `SC00` | No | Sin autoconsumo. |
| `SC11` | No | Sin excedentes. |
| `SC12` | No | Con excedentes. |
| `SC0C` | No | Baja como miembro de autoconsumo colectivo. |

## `SmartControlAction`

The smart control action choices, i.e. suspend or unsuspend.

| Value | Deprecated | Description |
|---|---|---|
| `SUSPEND` | No |  |
| `UNSUSPEND` | No |  |

## `SmartFlexChargingErrorCause`

| Value | Deprecated | Description |
|---|---|---|
| `SOC_LIMIT_REACHED` | No | State of charge limit reached - Charging prevented due to a device specific charging limit setting (current state of charge is equal to or above the set limit). |
| `COMMUNICATION_ERROR` | No | Unable to communicate with device - Dispatches were created but no telemetry readings available during the charge session. |
| `THIRD_PARTY_CHARGING_INTERFERENCE` | No | Third-party charging interference - Telemetry for an at-home charging event was found outside of `Dispatch Schedules`. |
| `POWER_DISCREPANCY` | No | Observed power discrepancy - Power during the session was observed to be significantly different from the value of the max. import in static data. |
| `POWER_TAPERING` | No | Observed power tapering - Power decreased at state of charge levels or towards the end of the session. |
| `NO_SCHEDULED_CHARGE` | No | No scheduled charge within session - There were no schedules for the given charge session period. |
| `FAILURE_CAUSE_ERROR` | No | Unable to determine cause of failure - If the charge session was not achieved, butwe are unable to determine the cause of failure. |
| `CUSTOMER_ACTION_REQUIRED` | No | Action required - Customer needs to take action to re-enable our control (i.e attemptto re-onboard). |
| `NO_CHARGING` | No | No charging - No charging (import of energy) was observed during the session. |
| `FULL_CHARGE` | No | Device fully charged - Device conducting a relative charge session indicated it hadreached 100% SoC or an internal SoC limit. Applied regardless of whether or not wewere able to add the energy requested. |
| `POST_CHARGE_BATTERY_DRAIN` | No | Post-charge battery drain - Target was hit but session ended below target due tobattery drain (caused e.g. by cell balancing). |
| `UNKNOWN_CHARGING_ERROR_CAUSE` | No | Unknown failure cause |

## `SmartFlexChargingTruncationCause`

The possible causes for a charging session ending prematurely.

| Value | Deprecated | Description |
|---|---|---|
| `DISCONNECTED` | No |  |
| `SUSPENDED` | No |  |
| `BOOST_CHARGING` | No |  |
| `UNKNOWN_TRUNCATION_CAUSE` | No |  |
| `CHARGING_OPTIMISATION_CREATED` | No |  |
| `DEVICE_DEAUTH_SUCCESS` | No |  |

## `SmartFlexChargingType`

The available charging types.

| Value | Deprecated | Description |
|---|---|---|
| `SMART` | No |  |
| `BOOST` | No |  |
| `TEST` | No |  |

## `SmartFlexDeviceLifecycleStatus`

The current lifecycle status of a KrakenFlex device on the smarter tariff API.

| Value | Deprecated | Description |
|---|---|---|
| `ONBOARDING` | No |  |
| `PENDING_LIVE` | No |  |
| `LIVE` | No |  |
| `ONBOARDING_TEST_IN_PROGRESS` | No |  |
| `FAILED_ONBOARDING_TEST` | No |  |
| `RETIRED` | No |  |

## `SmartFlexDeviceState`

| Value | Deprecated | Description |
|---|---|---|
| `AUTHENTICATION_PENDING` | No | Authentication Pending - ready to start authentication and authorization, or auth is in progress. |
| `AUTHENTICATION_FAILED` | No | Authentication Failed - failed to connect and ready to restart authentication and authorization. |
| `AUTHENTICATION_COMPLETE` | No | Authentication Complete - ready to start test (if needed) or pending live where auth or telemetry is delayed. |
| `TEST_CHARGE_IN_PROGRESS` | No | Test Charge in Progress - connection and smart control test has successfully started and is occurring. |
| `TEST_CHARGE_FAILED` | No | Test Charge Failed - connection or smart control test has failed or could not start, ready to retry test. |
| `TEST_CHARGE_NOT_AVAILABLE` | No | Test Charge Not Available - not currently capable of smart control test (e.g. away from home or unplugged). |
| `SETUP_COMPLETE` | No | Setup Complete - test is complete (if needed) and device is live, but not ready for smart control. |
| `SMART_CONTROL_CAPABLE` | No | Smart Control Capable - live and ready for smart control (e.g. at home and plugged in) but none is scheduled. |
| `SMART_CONTROL_IN_PROGRESS` | No | Smart Control in Progress - smart control (e.g. smart charging) is scheduled or is currently occurring. |
| `BOOSTING` | No | Manual Boosting (e.g. bump charging) - user has overridden the schedule to immediately boost (e.g. bump charge now). |
| `SMART_CONTROL_OFF` | No | Smart Control Off (suspended) - smart control has been (temporarily) disabled (e.g. by the user with holiday mode). |
| `SMART_CONTROL_NOT_AVAILABLE` | No | Smart Control Not Available - not currently capable of smart control (e.g. away from home or unplugged). |
| `LOST_CONNECTION` | No | Lost Connection - lost connection to the device, ready to re-auth (if not temporary / automatic fix). |
| `RETIRED` | No | Retired - deleted / de-authed (re-auth not possible, re-register device to onboard again). |

## `Songs`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `NO_SONG_PREFERRED` | No | . |

## `StatementReversalsAfterClose`

Tracking of charge reversals after statement closure (ALL, SOME, NONE, or NOT_CLOSED).

| Value | Deprecated | Description |
|---|---|---|
| `ALL` | No | All charges have been reversed after the statement was closed. |
| `SOME` | No | Some charges have been reversed after the statement was closed. |
| `NONE` | No | No reversals after the statement was closed. |
| `NOT_CLOSED` | No | The statement has not been closed yet. |

## `Status`

The status of a workflow.

| Value | Deprecated | Description |
|---|---|---|
| `SKIPPED` | No |  |
| `COMPLETED` | No |  |
| `PENDING` | No |  |
| `IN_PROGRESS` | No |  |
| `STALLED` | No |  |
| `CANCELLED` | No |  |
| `FAILED` | No |  |
| `ERRORED` | No |  |

## `StorylineEntryTypes`

The available types of storyline entries.

| Value | Deprecated | Description |
|---|---|---|
| `INBOUND_MESSAGE` | No |  |
| `OUTBOUND_MESSAGE` | No |  |
| `INBOUND_CTI_CALL` | No |  |
| `OUTBOUND_CTI_CALL` | No |  |
| `INBOUND_VOICE_CALL` | No |  |
| `OUTBOUND_VOICE_CALL` | No |  |
| `CONVERSATION_NOTE_SUMMARY` | No |  |
| `COMPLAINT_SUMMARY` | No |  |
| `TRANSACTIONAL_MESSAGE` | No |  |
| `APPOINTMENT` | No |  |
| `METER_READING` | No |  |
| `STATEMENT` | No |  |
| `REFUND` | No |  |
| `PAYMENT` | No |  |
| `REPAYMENT` | No |  |
| `OTHER` | No |  |
| `MESSAGE_SUMMARY` | No |  |
| `CTI_CALL_SUMMARY` | No |  |
| `VOICE_CALL_SUMMARY` | No |  |

## `SubsectionType`

The subsection type.

| Value | Deprecated | Description |
|---|---|---|
| `WITHOUT_EXCESS_NO_COMPENSATION` | No | Sin excedentes No acogido a compensación. |
| `WITHOUT_EXCESS_WITH_COMPENSATION` | No | Sin excedentes acogido a compensación. |
| `WITH_EXCESS_NO_COMPENSATION` | No | Con excedentes no acogidos a compensación. |
| `WITH_EXCESS_WITH_COMPENSATION` | No | Con excedentes acogidos a compensación. |
| `NO_SELFCONSUMPTION` | No | Sin autoconsumo. |
| `DROPOUT_FROM_COLLECTIVE_SELFCONSUMPTION` | No | Baja como miembro de autoconsumo colectivo. |

## `SupplyPointMarketNameEnum`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `ESP_ELECTRICITY` | No |  |
| `ESP_GAS` | No |  |
| `SIMPLE_SERVICES` | No |  |

## `TaskStatusEnum`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `STARTED` | No |  |
| `FAILED` | No |  |
| `FINISHED` | No |  |

## `TaxTypesCode`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `IVA_STANDARD` | No | IVA |
| `IVA_REDUCED` | No | IVA reduced |
| `IVA_EXEMPT` | No | IVA exempt |
| `IGIC_STANDARD` | No | IGIC standard |
| `IGIC_REDUCED` | No | IGIC reduced |
| `IGIC_EXEMPT` | No | IGIC exempt |
| `IGIC_SUPERREDUCED` | No | IGIC superreduced |
| `IEE_STANDARD` | No | IEE standard |
| `IEE_REDUCED` | No | IEE reduced |
| `IEE_EXEMPT` | No | IEE exento |
| `IEH_STANDARD` | No | IEH |
| `IEH_REDUCED` | No | IEH (Reducido) |
| `IEH_EXEMPT` | No | IEH exento |

## `TaxTypesUnitType`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `PROPORTION` | No | Proportion |
| `CURRENCY_PER_KWH` | No | Currency Per Kwh |

## `TestChargeErrorType`

The type of test charge error.

| Value | Deprecated | Description |
|---|---|---|
| `UNABLE_TO_INITIATE_TEST_CHARGE` | No | An error occurred when attempting to initiate a test charge. |
| `UNABLE_TO_COMPLETE_TEST_CHARGE` | No | An error occurred during a test charge attempt. |

## `TestChargeRefusalReason`

All possible reasons for refusing a test charge.

| Value | Deprecated | Description |
|---|---|---|
| `DEVICE_LIVE` | No |  |
| `DEVICE_ONBOARDING_IN_PROGRESS` | No |  |
| `DEVICE_RETIRED` | No |  |
| `DEVICE_SUSPENDED` | No |  |
| `DEVICE_DISCONNECTED` | No |  |
| `DEVICE_ALREADY_CHARGING` | No |  |
| `DEVICE_AWAY_FROM_HOME` | No |  |
| `DEVICE_NO_LOCATION_CONFIGURED` | No |  |
| `DEVICE_LOCATION_UNABLE_TO_IDENTIFY` | No |  |
| `DEVICE_LOCATION_MISSING` | No |  |

## `TestDispatchAssessmentFailureReason`

The reason (if any) that we believe a test dispatch (test charge) did not succeed.

| Value | Deprecated | Description |
|---|---|---|
| `NONE` | No |  |
| `UNKNOWN` | No |  |
| `ASSESSMENTS_FAILED` | No |  |
| `NOT_AT_HOME` | No |  |
| `UNABLE_TO_COMMUNICATE` | No |  |
| `DEVICE_DISCONNECTED` | No |  |
| `SOC_LIMIT_REACHED` | No |  |
| `ERROR` | No |  |

## `TestDispatchStatus`

All possible test dispatch statuses.

| Value | Deprecated | Description |
|---|---|---|
| `TRIGGERED` | No |  |
| `COMPLETE` | No |  |
| `FAILED` | No |  |

## `TextStyleV1`

The style is the typographical hierarchy. These are Typescale Categories from the Mobile Design System (Figma).

| Value | Deprecated | Description |
|---|---|---|
| `TITLE1` | No |  |
| `TITLE2` | No |  |
| `TITLE3` | No |  |
| `TITLE4` | No |  |
| `TITLE5` | No |  |
| `TITLE6` | No |  |
| `BODY1` | No |  |
| `BODY2` | No |  |
| `BUTTON_TEXT` | No |  |
| `CALLOUT1` | No |  |
| `CALLOUT2` | No |  |
| `CALLOUT3` | No |  |
| `SMALL1` | No |  |
| `SMALL2` | No |  |
| `SMALL3` | No |  |
| `INPUT_TITLE` | No |  |
| `TABULAR` | No |  |

## `TimeGranularities`

Time buckets into which readings are grouped.

| Value | Deprecated | Description |
|---|---|---|
| `FIVE_MIN` | No |  |
| `FIFTEEN_MIN` | No |  |
| `THIRTY_MIN` | No |  |
| `HOUR` | No |  |
| `DAY` | No |  |
| `WEEK` | No |  |
| `MONTH` | No |  |
| `QUARTER` | No |  |
| `YEAR` | No |  |

## `TransactionTypeFilter`

Filter options for transaction types (e.g., energy charges, water charges, imported payments).

| Value | Deprecated | Description |
|---|---|---|
| `UNISSUED_TRANSACTIONS` | No | For filtering/excluding unissued transactions. |
| `ENERGY_CHARGES` | No | For filtering/excluding energy charge transactions: Gas or Electricity. |
| `WATER_CHARGES` | No | For filtering/excluding water charge transactions. |
| `IMPORTED_CHARGES` | No | For filtering/excluding imported charge transactions. |
| `IMPORTED_CREDITS` | No | For filtering/excluding imported credit transactions. |
| `IMPORTED_REPAYMENTS` | No | For filtering/excluding imported repayment transactions. |
| `IMPORTED_PAYMENTS` | No | For filtering/excluding imported payment transactions. |

## `TransactionTypes`

The type of transaction.

| Value | Deprecated | Description |
|---|---|---|
| `CREDIT` | No |  |
| `PAYMENT` | No |  |
| `REPAYMENT` | No |  |

## `TransactionsOrderBy`

| Value | Deprecated | Description |
|---|---|---|
| `POSTED_DATE_ASC` | No |  |
| `POSTED_DATE_DESC` | No |  |

## `TriggerProcessingStatus`

Set of possible outcomes resulting from the processing of a `Trigger`.

| Value | Deprecated | Description |
|---|---|---|
| `UNPROCESSED` | No |  |
| `PROCESSED` | No |  |
| `PROCESSING_SKIPPED` | No |  |
| `PROCESSING_FAILED` | No |  |

## `TypeOfVoiceCampaign`

The type of campaign, e.g. preview or predictive.

| Value | Deprecated | Description |
|---|---|---|
| `PREVIEW` | No |  |
| `PREDICTIVE` | No |  |

## `Unit`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `KILOWATT_HOURS` | No |  |
| `METERS_CUBED` | No |  |

## `Units`

Available units relevant to electricity, gas, and water.

| Value | Deprecated | Description |
|---|---|---|
| `WATT` | No |  |
| `WATT_HOURS` | No |  |
| `KILOWATT` | No |  |
| `KILOWATT_HOURS` | No |  |
| `AMPERE` | No |  |
| `KILOAMPERE` | No |  |
| `VOLT` | No |  |
| `KILOVOLT` | No |  |
| `VOLT_AMPERE` | No |  |
| `VOLT_AMPERE_HOURS` | No |  |
| `VOLT_AMPERE_REACTIVE` | No |  |
| `VOLT_AMPERE_REACTIVE_HOURS` | No |  |
| `KILOVOLT_AMPERE` | No |  |
| `KILOVOLT_AMPERE_HOURS` | No |  |
| `KILOVOLT_AMPERE_REACTIVE` | No |  |
| `KILOVOLT_AMPERE_REACTIVE_HOURS` | No |  |
| `POWER_FACTOR` | No |  |
| `METERS_CUBED` | No |  |
| `FEET_CUBED` | No |  |
| `DECALITERS` | No |  |
| `LITER` | No |  |
| `KILOLITERS` | No |  |
| `US_GALLONS` | No |  |

## `UpdateBoostChargeAction`

The boost action, i.e. boost or cancel.

| Value | Deprecated | Description |
|---|---|---|
| `BOOST` | No |  |
| `CANCEL` | No |  |

## `Vendor`

Possible payment vendors.

| Value | Deprecated | Description |
|---|---|---|
| `GOCARDLESS` | No |  |
| `GOCARDLESS_BULB` | No |  |
| `GOCARDLESS_AFFECT` | No |  |
| `GOCARDLESS_GEN4U` | No |  |
| `GOCARDLESS_IRESA` | No |  |
| `SMARTDEBIT` | No |  |
| `WORLDPAY` | No |  |
| `ACCESS_PAYSUITE` | No |  |
| `ACCESS_PAYSUITE_EXPORT` | No |  |
| `ACCESS_PAYSUITE_FIT` | No |  |
| `ACCESS_PAYSUITE_SHELL` | No |  |
| `BOTTOMLINE_PTX` | No |  |
| `BOTTOMLINE_PTX_BATCHED` | No |  |
| `BOTTOMLINE_GLOBAL_PAYMENTS_HUB` | No |  |
| `STRIPE` | No |  |
| `STRIPE_CONNECT` | No |  |
| `STRIPE_CONNECT_VOICE` | No |  |
| `STRIPE_VOICE` | No |  |
| `WESTPAC` | No |  |
| `WESTPAC_ILINK` | No |  |
| `WESTPAC_ILINK_MERIDIAN` | No |  |
| `WESTPAC_ILINK_POWERSHOP` | No |  |
| `WESTPAC_QUICKSTREAM` | No |  |
| `WESTPAC_QUICKSTREAM_MERIDIAN` | No |  |
| `WESTPAC_QUICKSTREAM_POWERSHOP` | No |  |
| `GMO` | No |  |
| `GMO_CARD` | No |  |
| `STRIPE_KONBINI` | No |  |
| `TESORO` | No |  |
| `DUMMY` | No |  |
| `COMMBANK` | No |  |
| `BPOINT` | No |  |
| `TG_PAYMENTS` | No |  |
| `TG_PAYMENTS_MYPAY` | No |  |
| `PAGOPA` | No |  |
| `BUCKAROO` | No |  |
| `BUCKAROO_SEPA` | No |  |
| `TOTALENERGIES` | No |  |
| `PAYMENTUS_DIGITAL_WALLET` | No |  |
| `CUSTOM` | No |  |

## `VerificationRequestStatus`

The status of verification for associated email.

| Value | Deprecated | Description |
|---|---|---|
| `NOT_SENT` | No |  |
| `PENDING` | No |  |
| `COMPLETED` | No |  |

## `VoiceVendor`

The Voice vendor managing the call.

| Value | Deprecated | Description |
|---|---|---|
| `TWILIO` | No | Twilio. |

## `WorkScheduleOpenOrClosedReason`

Why a Work Schedule is open or closed.

| Value | Deprecated | Description |
|---|---|---|
| `CLOSED_DUE_TO_PUBLIC_HOLIDAY` | No |  |
| `CLOSED_DUE_TO_DAY_OF_WEEK` | No |  |
| `CLOSED_BEFORE_OPEN_TIME` | No |  |
| `CLOSED_AFTER_CLOSE_TIME` | No |  |
| `OPEN_INSIDE_WORK_SCHEDULE` | No |  |
| `WORK_SCHEDULE_TIME_ZONE_MISCONFIGURED` | No |  |

## `_BillingDocumentsOrderBy`

| Value | Deprecated | Description |
|---|---|---|
| `FINALIZED_AT_ASC` | No |  |
| `FINALIZED_AT_DESC` | No |  |

## `query_type`

An enumeration.

| Value | Deprecated | Description |
|---|---|---|
| `query` | No |  |
| `mutation` | No |  |

