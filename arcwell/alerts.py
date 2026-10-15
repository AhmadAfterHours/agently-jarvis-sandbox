"""Runway alert timing helpers for Arcwell Cash Watch."""

from math import floor


def months_until_watch(
    cash: float,
    expenses: float,
    revenue: float,
    threshold_months: float = 6,
) -> int | float:
    """Return whole months until the runway alert reaches ``watch``.

    The alert reaches ``watch`` when runway falls below twice
    ``threshold_months``. Return zero when it is already at ``watch`` or
    worse. Return infinity when there is no net monthly cash burn.
    """
    if threshold_months <= 0:
        raise ValueError("threshold_months must be positive")

    monthly_burn = expenses - revenue
    if monthly_burn <= 0:
        return float("inf")

    runway = cash / monthly_burn
    watch_boundary = 2 * threshold_months
    if runway < watch_boundary:
        return 0

    return floor(runway - watch_boundary) + 1
