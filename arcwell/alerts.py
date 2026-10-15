"""Runway alert classification for Arcwell Cash Watch."""


def runway_alert(
    cash: float,
    expenses: float,
    revenue: float,
    threshold_months: float = 6,
) -> str:
    """Classify runway as ``ok``, ``watch``, or ``act``.

    ``act`` applies below ``threshold_months``. ``watch`` applies below twice
    that threshold. Companies with no net cash burn are ``ok``.
    """
    if threshold_months < 0:
        raise ValueError("threshold_months must not be negative")

    monthly_burn = expenses - revenue
    if monthly_burn <= 0:
        return "ok"

    runway = cash / monthly_burn
    if runway < threshold_months:
        return "act"
    if runway < 2 * threshold_months:
        return "watch"
    return "ok"
