from math import inf, nan

import pytest

from arcwell.alerts import runway_alert


@pytest.mark.parametrize(
    ("cash", "expenses", "revenue", "expected"),
    [
        (1_200, 100, 0, "ok"),
        (1_199, 100, 0, "watch"),
        (600, 100, 0, "watch"),
        (599, 100, 0, "act"),
        (1_000, 100, 100, "ok"),
        (1_000, 80, 100, "ok"),
    ],
)
def test_runway_alert_classifies_runway(cash, expenses, revenue, expected):
    assert runway_alert(cash, expenses, revenue) == expected


def test_runway_alert_uses_a_custom_threshold():
    assert runway_alert(5, 1, 0, threshold_months=3) == "watch"
    assert runway_alert(3, 1, 0, threshold_months=3) == "watch"
    assert runway_alert(2.99, 1, 0, threshold_months=3) == "act"


def test_runway_alert_rejects_negative_thresholds():
    with pytest.raises(ValueError, match="threshold_months must not be negative"):
        runway_alert(100, 10, 0, threshold_months=-1)


@pytest.mark.parametrize("invalid", [nan, inf, -inf])
@pytest.mark.parametrize("field", ["cash", "expenses", "revenue", "threshold_months"])
def test_runway_alert_rejects_non_finite_inputs(field, invalid):
    arguments = {"cash": 1_000, "expenses": 100, "revenue": 0, "threshold_months": 6}
    arguments[field] = invalid

    with pytest.raises(ValueError, match=rf"{field} must be a finite number"):
        runway_alert(**arguments)
