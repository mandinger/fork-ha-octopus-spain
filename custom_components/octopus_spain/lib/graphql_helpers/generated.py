"""Generated GraphQL helper DTOs and request builders.

Do not edit manually. Regenerate with:
  python3 scripts/generate_graphql_helpers.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


def _serialize_input(value: Any) -> Any:
    if hasattr(value, 'to_dict') and callable(value.to_dict):
        return value.to_dict()
    if isinstance(value, list):
        return [_serialize_input(item) for item in value]
    return value

# Enum aliases
ReadingDirectionType = Literal["CONSUMPTION", "GENERATION"]
ReadingFrequencyType = Literal["RAW_INTERVAL", "FIVE_MIN_INTERVAL", "FIFTEEN_MIN_INTERVAL", "THIRTY_MIN_INTERVAL", "HOUR_INTERVAL", "DAY_INTERVAL", "WEEK_INTERVAL", "MONTH_INTERVAL", "QUARTER_INTERVAL", "DAILY", "POINT_IN_TIME", "INTERVALIZED"]
ReadingQualityType = Literal["ACTUAL", "ESTIMATE", "COMBINED"]

# Input DTOs
@dataclass(slots=True)
class ElectricityFiltersInput:
    readingFrequencyType: ReadingFrequencyType | None = None
    marketSupplyPointId: str | None = None
    deviceId: str | None = None
    readingDirection: ReadingDirectionType | None = None
    registerId: str | None = None
    readingQuality: ReadingQualityType | None = None

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        if self.readingFrequencyType is not None:
            out['readingFrequencyType'] = _serialize_input(self.readingFrequencyType)
        if self.marketSupplyPointId is not None:
            out['marketSupplyPointId'] = _serialize_input(self.marketSupplyPointId)
        if self.deviceId is not None:
            out['deviceId'] = _serialize_input(self.deviceId)
        if self.readingDirection is not None:
            out['readingDirection'] = _serialize_input(self.readingDirection)
        if self.registerId is not None:
            out['registerId'] = _serialize_input(self.registerId)
        if self.readingQuality is not None:
            out['readingQuality'] = _serialize_input(self.readingQuality)
        return out

@dataclass(slots=True)
class GasFiltersInput:
    readingFrequencyType: ReadingFrequencyType | None = None
    marketSupplyPointId: str | None = None
    deviceId: str | None = None
    registerId: str | None = None

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        if self.readingFrequencyType is not None:
            out['readingFrequencyType'] = _serialize_input(self.readingFrequencyType)
        if self.marketSupplyPointId is not None:
            out['marketSupplyPointId'] = _serialize_input(self.marketSupplyPointId)
        if self.deviceId is not None:
            out['deviceId'] = _serialize_input(self.deviceId)
        if self.registerId is not None:
            out['registerId'] = _serialize_input(self.registerId)
        return out

@dataclass(slots=True)
class ObtainJSONWebTokenInput:
    APIKey: str | None = None
    organizationSecretKey: str | None = None
    preSignedKey: str | None = None
    refreshToken: str | None = None
    captchaResponse: str | None = None

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        if self.APIKey is not None:
            out['APIKey'] = _serialize_input(self.APIKey)
        if self.organizationSecretKey is not None:
            out['organizationSecretKey'] = _serialize_input(self.organizationSecretKey)
        if self.preSignedKey is not None:
            out['preSignedKey'] = _serialize_input(self.preSignedKey)
        if self.refreshToken is not None:
            out['refreshToken'] = _serialize_input(self.refreshToken)
        if self.captchaResponse is not None:
            out['captchaResponse'] = _serialize_input(self.captchaResponse)
        return out

@dataclass(slots=True)
class UtilityFiltersInput:
    electricityFilters: ElectricityFiltersInput | None = None
    gasFilters: GasFiltersInput | None = None

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        if self.electricityFilters is not None:
            out['electricityFilters'] = _serialize_input(self.electricityFilters)
        if self.gasFilters is not None:
            out['gasFilters'] = _serialize_input(self.gasFilters)
        return out

# Operation helpers
getAccountBilling_QUERY = '''query getAccountBilling($account: String!) {
  account(accountNumber: $account) {
    ledgers {
      ledgerType
      balance
      invoices(last: 1) {
        edges {
          node {
            id
            invoicedAmount
            earliestChargeAt
            firstIssued
            pdfUrl
            totalCharges {
              grossTotal
              netTotal
              taxTotal
            }
          }
        }
      }
    }
  }
}'''

@dataclass(slots=True)
class GetAccountBillingVariables:
    account: str

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        out['account'] = _serialize_input(self.account)
        return out

def build_get_account_billing_request(variables: GetAccountBillingVariables | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        'operationName': 'getAccountBilling',
        'query': getAccountBilling_QUERY,
    }
    if variables is not None:
        payload['variables'] = variables.to_dict()
    return payload

getAccountNames_QUERY = '''query getAccountNames {
  viewer {
    accounts {
      ... on Account {
        number
      }
    }
  }
}'''

@dataclass(slots=True)
class GetAccountNamesVariables:
    pass

    def to_dict(self) -> dict[str, Any]:
        return {}

def build_get_account_names_request(variables: GetAccountNamesVariables | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        'operationName': 'getAccountNames',
        'query': getAccountNames_QUERY,
    }
    if variables is not None:
        payload['variables'] = variables.to_dict()
    return payload

getMeasurements_QUERY = '''query getMeasurements(
  $account: String!
  $startAt: DateTime!
  $endAt: DateTime!
  $utilityFilters: [UtilityFiltersInput!]
) {
  account(accountNumber: $account) {
    properties {
      id
      measurements(
        first: 1500
        utilityFilters: $utilityFilters
        startAt: $startAt
        endAt: $endAt
        timezone: "Etc/GMT"
      ) {
        edges {
          node {
            value
            unit
            ... on IntervalMeasurementType {
              startAt
              endAt
            }
          }
        }
      }
    }
  }
}'''

@dataclass(slots=True)
class GetMeasurementsVariables:
    account: str
    startAt: str
    endAt: str
    utilityFilters: list[UtilityFiltersInput] | None = None

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        out['account'] = _serialize_input(self.account)
        out['startAt'] = _serialize_input(self.startAt)
        out['endAt'] = _serialize_input(self.endAt)
        if self.utilityFilters is not None:
            out['utilityFilters'] = _serialize_input(self.utilityFilters)
        return out

def build_get_measurements_request(variables: GetMeasurementsVariables | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        'operationName': 'getMeasurements',
        'query': getMeasurements_QUERY,
    }
    if variables is not None:
        payload['variables'] = variables.to_dict()
    return payload

obtainKrakenToken_QUERY = '''mutation obtainKrakenToken($input: ObtainJSONWebTokenInput!) {
  obtainKrakenToken(input: $input) {
    token
  }
}'''

@dataclass(slots=True)
class ObtainKrakenTokenVariables:
    input: ObtainJSONWebTokenInput

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        out['input'] = _serialize_input(self.input)
        return out

def build_obtain_kraken_token_request(variables: ObtainKrakenTokenVariables | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        'operationName': 'obtainKrakenToken',
        'query': obtainKrakenToken_QUERY,
    }
    if variables is not None:
        payload['variables'] = variables.to_dict()
    return payload

__all__ = [
    'ReadingDirectionType',
    'ReadingFrequencyType',
    'ReadingQualityType',
    'ElectricityFiltersInput',
    'GasFiltersInput',
    'ObtainJSONWebTokenInput',
    'UtilityFiltersInput',
    'getAccountBilling_QUERY',
    'GetAccountBillingVariables',
    'build_get_account_billing_request',
    'getAccountNames_QUERY',
    'GetAccountNamesVariables',
    'build_get_account_names_request',
    'getMeasurements_QUERY',
    'GetMeasurementsVariables',
    'build_get_measurements_request',
    'obtainKrakenToken_QUERY',
    'ObtainKrakenTokenVariables',
    'build_obtain_kraken_token_request',
]
