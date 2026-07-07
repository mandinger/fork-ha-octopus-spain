"""Tests for the API client (lib/octopus_spain_fork.py)."""

from datetime import datetime, timezone

import pytest

import custom_components.octopus_spain_fork.lib.octopus_spain_fork as mod
from custom_components.octopus_spain_fork.lib.octopus_spain_fork import (
    OctopusApiError,
    OctopusSpain,
)

_START = datetime(2026, 6, 28, tzinfo=timezone.utc)
_END = datetime(2026, 6, 29, tzinfo=timezone.utc)


class _FakeClient:  # pylint: disable=too-few-public-methods
    """Fake GraphQL client returning a fixed response."""

    def __init__(self, response):
        self._response = response

    async def execute_async(self, query, variables=None):  # pylint: disable=unused-argument
        """Return the canned response, ignoring the query."""
        return self._response


class _SeqClient:  # pylint: disable=too-few-public-methods
    """Fake client returning a sequence of responses (one per call)."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.calls: list[dict] = []

    async def execute_async(self, query, variables=None):  # pylint: disable=unused-argument
        """Return the next response, recording the variables used."""
        self.calls.append(dict(variables or {}))
        return self._responses.pop(0)


def _patch(monkeypatch, client):
    """Patch GraphqlClient with a factory returning the given fake."""
    monkeypatch.setattr(mod, "GraphqlClient", lambda *a, **k: client)


def _api() -> OctopusSpain:
    api = OctopusSpain("e", "p", None)
    api._token = "t"  # pylint: disable=protected-access
    return api


def _node(hour: int, value: str) -> dict:
    """Build a single hourly measurement node."""
    return {
        "value": value,
        "unit": "kWh",
        "startAt": f"2026-06-28T{hour:02d}:00:00+00:00",
        "endAt": f"2026-06-28T{hour + 1:02d}:00:00+00:00",
    }


def _meas_page(nodes, has_next: bool, cursor: str | None = None, errors=None) -> dict:
    """Build one page of a measurements connection response."""
    response = {
        "data": {
            "account": {
                "properties": [
                    {
                        "id": "prop-1",
                        "measurements": {
                            "pageInfo": {"hasNextPage": has_next, "endCursor": cursor},
                            "edges": [{"node": n} for n in nodes],
                        },
                    }
                ]
            }
        }
    }
    if errors is not None:
        response["errors"] = errors
    return response


async def test_consumption_paginates_and_concatenates(monkeypatch):
    """_consumption() follows pageInfo.endCursor and concatenates every page."""
    client = _SeqClient(
        [
            _meas_page([_node(0, "1.0")], True, "c1"),
            _meas_page([_node(1, "2.0")], False),
        ]
    )
    _patch(monkeypatch, client)
    rows = await _api().hourly_consumption("A-1", start=_START, end=_END)
    assert [r["value"] for r in rows] == ["1.0", "2.0"]
    assert client.calls[0]["after"] is None
    assert client.calls[1]["after"] == "c1"


async def test_consumption_single_page(monkeypatch):
    """A single page without hasNextPage triggers exactly one request."""
    client = _SeqClient([_meas_page([_node(0, "1.5")], False)])
    _patch(monkeypatch, client)
    rows = await _api().hourly_consumption("A-1", start=_START, end=_END)
    assert len(rows) == 1
    assert len(client.calls) == 1


async def test_consumption_raises_on_errors_without_data(monkeypatch):
    """Errors with no usable account payload raise OctopusApiError."""
    _patch(
        monkeypatch,
        _FakeClient({"errors": [{"message": "Query exceeds maximum allowed node count."}]}),
    )
    with pytest.raises(OctopusApiError) as exc:
        await _api().hourly_consumption("A-1", start=_START, end=_END)
    assert "node count" in str(exc.value)


async def test_consumption_raises_on_null_data(monkeypatch):
    """{"data": null} without an errors key raises OctopusApiError (issue #29)."""
    _patch(monkeypatch, _FakeClient({"data": None}))
    with pytest.raises(OctopusApiError):
        await _api().hourly_consumption("A-1", start=_START, end=_END)


async def test_consumption_keeps_partial_data_with_field_errors(monkeypatch):
    """Field-level errors alongside usable data must not discard the rows."""
    page = _meas_page([_node(0, "3.0")], False, errors=[{"message": "partial"}])
    _patch(monkeypatch, _FakeClient(page))
    rows = await _api().hourly_consumption("A-1", start=_START, end=_END)
    assert [r["value"] for r in rows] == ["3.0"]


async def test_account_null_data_returns_empty_payload(monkeypatch):
    """account() must return the fallback payload on {"data": null} (issue #29)."""
    _patch(monkeypatch, _FakeClient({"data": None}))
    payload = await _api().account("A-1")
    assert payload["last_invoice"]["id"] is None
    assert payload["solar_wallet"] is None


async def test_payment_forecast_kt_ct_3949_returns_none(monkeypatch):
    """KT-CT-3949 (no forecastable payments) is expected and maps to None."""
    _patch(
        monkeypatch,
        _FakeClient(
            {
                "data": {"account": None},
                "errors": [
                    {
                        "message": "Received an error from the payment forecast service.",
                        "extensions": {"errorCode": "KT-CT-3949"},
                    }
                ],
            }
        ),
    )
    assert await _api().payment_forecast("A-1") is None
