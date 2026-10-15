import math

import pytest

from arcwell.runway import monthly_burn, runway_months


def test_monthly_burn_averages_net_spend():
    assert monthly_burn([100, 120], [40, 60]) == 60


def test_monthly_burn_rejects_mismatched_month_lists():
    with pytest.raises(
        ValueError, match="expenses and revenue must have the same number of months"
    ):
        monthly_burn([100, 120], [40])


def test_runway_months_divides_cash_by_burn():
    assert runway_months(600, [100, 120], [40, 60]) == 10


def test_profitable_company_has_infinite_runway():
    assert math.isinf(runway_months(600, [50], [80]))


def test_no_months_is_an_error():
    with pytest.raises(ValueError):
        monthly_burn([], [])
