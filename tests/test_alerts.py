import math

import pytest

from arcwell.alerts import months_until_watch


@pytest.mark.parametrize(
    ("cash", "expenses", "revenue", "expected"),
    [
        (1_199, 100, 0, 0),
        (599, 100, 0, 0),
        (1_200, 100, 0, 1),
        (1_299, 100, 0, 1),
        (1_300, 100, 0, 2),
    ],
)
def test_months_until_watch_counts_until_runway_drops_below_watch_boundary(
    cash, expenses, revenue, expected
):
    assert months_until_watch(cash, expenses, revenue) == expected


def test_months_until_watch_uses_a_custom_threshold():
    assert months_until_watch(600, 100, 0, threshold_months=3) == 1


@pytest.mark.parametrize("expenses, revenue", [(100, 100), (80, 100)])
def test_months_until_watch_is_infinite_without_net_burn(expenses, revenue):
    assert math.isinf(months_until_watch(1_000, expenses, revenue))


def test_months_until_watch_requires_a_positive_threshold():
    with pytest.raises(ValueError, match="threshold_months must be positive"):
        months_until_watch(1_000, 100, 0, threshold_months=0)
