"""Tests for pure sensor helpers (prices, last-day aggregation, backfill windows)."""

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from zoneinfo import ZoneInfo

from homeassistant.util import dt as dt_util
import pytest

from custom_components.octopus_spain_fork.sensor import (
    OctopusConsumptionStatisticsImporter,
    _account_for_unique_id,
    _last_day_consumption,
    _tariff_period_prices,
)

MADRID = ZoneInfo("Europe/Madrid")


@pytest.fixture
def madrid_tz():
    """Run with Home Assistant's local timezone set to Europe/Madrid.

    Restores the timezone directly rather than via ``monkeypatch``: the plugin's
    ``verify_cleanup`` fixture asserts it is back to UTC, and it runs before
    monkeypatch's undo.
    """
    original = dt_util.DEFAULT_TIME_ZONE
    dt_util.DEFAULT_TIME_ZONE = MADRID
    try:
        yield MADRID
    finally:
        dt_util.DEFAULT_TIME_ZONE = original


def _importer(*, fill_missing_hours_as_zero: bool = False):
    """Build an importer wired to stubs; enough for the pure window helpers."""
    coordinator = SimpleNamespace(
        async_fetch_hourly_consumption=None,
        async_fetch_daily_consumption=None,
    )
    return OctopusConsumptionStatisticsImporter(
        hass=None,
        coordinator=coordinator,
        account="A-1234",
        single=True,
        statistic_id="octopus_spain_fork:energy_consumption_a_1234",
        state_callback=lambda *_: None,
        fill_missing_hours_as_zero=fill_missing_hours_as_zero,
    )


def _contract(with_taxes=None, without_taxes=None) -> dict:
    return {"prices": {"variable_term_with_taxes": with_taxes, "variable_term": without_taxes}}


def test_tariff_period_prices_prefers_with_taxes():
    prices = _tariff_period_prices(_contract([0.2, 0.15, 0.1], [0.18, 0.13, 0.08]))
    assert prices["effective"] == [0.2, 0.15, 0.1]
    assert prices["without_taxes"] == [0.18, 0.13, 0.08]


def test_tariff_period_prices_falls_back_to_plain():
    prices = _tariff_period_prices(_contract(None, [0.18, 0.13, 0.08]))
    assert prices["effective"] == [0.18, 0.13, 0.08]
    assert prices["with_taxes"] is None


def test_tariff_period_prices_rejects_non_three_period():
    assert _tariff_period_prices(_contract([0.2], [0.18])) is None
    assert _tariff_period_prices(_contract(None, None)) is None
    assert _tariff_period_prices(None) is None
    assert _tariff_period_prices({}) is None


def test_account_for_unique_id_prefers_longest_slug():
    """When one account's slug is a suffix of another's, the longest wins."""
    slug_by_account = {"1234": "1234", "A_1234": "a_1234"}
    # "solar_wallet_a_1234" ends with both "_1234" and "_a_1234"; the longer wins.
    assert _account_for_unique_id("solar_wallet_a_1234", slug_by_account) == "A_1234"
    # An id that only ends with the shorter slug resolves to that account.
    assert _account_for_unique_id("octopus_credit_1234", slug_by_account) == "1234"
    assert _account_for_unique_id("no_match_here", slug_by_account) is None


def _row(day: int, hour: int, value) -> dict:
    return {
        "value": value,
        "unit": "kWh",
        "startAt": f"2026-06-{day:02d}T{hour:02d}:00:00+00:00",
        "endAt": f"2026-06-{day:02d}T{hour + 1:02d}:00:00+00:00",
    }


def test_last_day_consumption_sums_only_latest_day():
    rows = [_row(27, 0, "1.0"), _row(28, 0, "2.0"), _row(28, 1, "0.5")]
    total, day = _last_day_consumption(rows)
    assert total == 2.5
    assert day.isoformat() == "2026-06-28"


def test_last_day_consumption_skips_unparseable_and_negative():
    rows = [
        _row(28, 0, "2.0"),
        {"value": "bad", "startAt": "2026-06-28T01:00:00+00:00"},
        {"value": "-1.0", "startAt": "2026-06-28T02:00:00+00:00"},
        {"value": "1.0", "startAt": None},
    ]
    total, day = _last_day_consumption(rows)
    assert total == 2.0
    assert day.isoformat() == "2026-06-28"


def test_last_day_consumption_empty_returns_none():
    assert _last_day_consumption([]) is None
    assert _last_day_consumption(None) is None
    assert _last_day_consumption([{"value": "1.0"}]) is None


def test_backfill_windows_chunks_and_covers_range():
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    end = start + timedelta(days=65)
    windows = OctopusConsumptionStatisticsImporter._backfill_windows(start, end, chunk_days=30)
    assert windows[0] == (start, start + timedelta(days=30))
    assert windows[-1][1] == end
    assert len(windows) == 3
    # Consecutive, no gaps or overlaps.
    for (_, prev_end), (next_start, _) in zip(windows, windows[1:]):
        assert prev_end == next_start


def test_backfill_windows_empty_when_start_not_before_end():
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    assert OctopusConsumptionStatisticsImporter._backfill_windows(start, start) == []


def test_import_window_reaches_into_previous_month_after_rollover(madrid_tz):
    """On the 1st the window still covers the previous month's late readings."""
    now = datetime(2026, 8, 1, 10, 0, tzinfo=MADRID).astimezone(timezone.utc)
    start, end = OctopusConsumptionStatisticsImporter._import_window(now)
    # 7 days back, local midnight: 2026-07-25 00:00 +02:00.
    assert start == datetime(2026, 7, 25, tzinfo=MADRID).astimezone(timezone.utc)
    # Through the end of today: 2026-08-02 00:00 +02:00.
    assert end == datetime(2026, 8, 2, tzinfo=MADRID).astimezone(timezone.utc)
    assert start < OctopusConsumptionStatisticsImporter._current_month_start(now)


def test_import_window_is_current_month_once_catchup_elapsed(madrid_tz):
    now = datetime(2026, 8, 20, 10, 0, tzinfo=MADRID).astimezone(timezone.utc)
    start, end = OctopusConsumptionStatisticsImporter._import_window(now)
    assert start == datetime(2026, 8, 1, tzinfo=MADRID).astimezone(timezone.utc)
    assert start == OctopusConsumptionStatisticsImporter._current_month_start(now)
    assert end == datetime(2026, 8, 21, tzinfo=MADRID).astimezone(timezone.utc)


def _hours(day: datetime, hours: range) -> dict:
    return {day + timedelta(hours=hour): 1.0 for hour in hours}


def test_truncate_keeps_current_month_when_catchup_day_incomplete(madrid_tz, monkeypatch):
    """A previous month that never completed must not block the current one."""
    monkeypatch.setattr(
        dt_util,
        "utcnow",
        lambda: datetime(2026, 8, 3, 10, 0, tzinfo=MADRID).astimezone(timezone.utc),
    )
    jul_31 = datetime(2026, 7, 31, tzinfo=MADRID).astimezone(timezone.utc)
    aug_1 = datetime(2026, 8, 1, tzinfo=MADRID).astimezone(timezone.utc)
    aug_2 = datetime(2026, 8, 2, tzinfo=MADRID).astimezone(timezone.utc)
    measurements = {
        **_hours(jul_31, range(18)),  # incomplete: only 18 of 24 hours published
        **_hours(aug_1, range(24)),
        **_hours(aug_2, range(24)),
    }

    kept, truncated_from = _importer()._truncate_incomplete_days(
        prefix="test",
        measurements_by_start=measurements,
        blocking_from_day=aug_1.astimezone(MADRID).date(),
    )

    assert truncated_from is None
    assert len(kept) == 18 + 24 + 24


def test_truncate_still_blocks_on_incomplete_current_month_day(madrid_tz, monkeypatch):
    """Inside the current month an incomplete day still truncates what follows."""
    monkeypatch.setattr(
        dt_util,
        "utcnow",
        lambda: datetime(2026, 8, 3, 10, 0, tzinfo=MADRID).astimezone(timezone.utc),
    )
    aug_1 = datetime(2026, 8, 1, tzinfo=MADRID).astimezone(timezone.utc)
    aug_2 = datetime(2026, 8, 2, tzinfo=MADRID).astimezone(timezone.utc)
    measurements = {
        **_hours(aug_1, range(18)),  # incomplete and no longer today
        **_hours(aug_2, range(24)),
    }

    kept, truncated_from = _importer()._truncate_incomplete_days(
        prefix="test",
        measurements_by_start=measurements,
        blocking_from_day=aug_1.astimezone(MADRID).date(),
    )

    assert truncated_from == aug_1.astimezone(MADRID).date()
    assert kept == {}
