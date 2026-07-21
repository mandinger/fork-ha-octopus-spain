"""Tests for coordinator subscription (account) filtering."""

from custom_components.octopus_spain_fork.coordinator import OctopusCoordinator


def test_select_accounts_none_loads_all():
    """No configured selection (None) loads every discovered account."""
    assert OctopusCoordinator._select_accounts(["A", "B"], None) == ["A", "B"]


def test_select_accounts_filters_to_selected_preserving_order():
    """Only selected accounts are kept, in discovery order (not selection order)."""
    assert OctopusCoordinator._select_accounts(["A", "B", "C"], {"C", "A"}) == ["A", "C"]


def test_select_accounts_drops_vanished_selection():
    """A selection that no longer matches any account yields nothing."""
    assert OctopusCoordinator._select_accounts(["A", "B"], {"Z"}) == []
