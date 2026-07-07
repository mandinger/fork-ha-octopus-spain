"""Tests for pure sensor helpers (prices, last-day aggregation, backfill windows)."""

from datetime import datetime, timedelta, timezone

from custom_components.octopus_spain_fork.sensor import (
    OctopusConsumptionStatisticsImporter,
    _last_day_consumption,
    _tariff_period_prices,
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
