"""Cash runway estimates for a fictional company."""


def monthly_burn(expenses: list[float], revenue: list[float]) -> float:
    """Average net monthly burn over the months given."""
    if not expenses:
        raise ValueError("no months given")
    net = [e - r for e, r in zip(expenses, revenue)]
    return sum(net) / len(net)


def runway_months(cash: float, expenses: list[float], revenue: list[float]) -> float:
    """Months of runway left at the average burn. Infinite when the company is not burning cash."""
    burn = monthly_burn(expenses, revenue)
    if burn <= 0:
        return float("inf")
    return cash / burn
