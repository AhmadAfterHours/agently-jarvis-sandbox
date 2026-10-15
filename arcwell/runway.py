"""Cash runway estimates for a fictional company."""


def monthly_burn(expenses: list[float], revenue: list[float]) -> float:
    """Average net monthly burn over the months given."""
    if len(expenses) != len(revenue):
        raise ValueError("expenses and revenue must have the same number of months")
    if not expenses:
        raise ValueError("no months given")
    net = [expense - income for expense, income in zip(expenses, revenue)]
    return sum(net) / len(net)


def runway_months(cash: float, expenses: list[float], revenue: list[float]) -> float:
    """Months of runway left at the average burn. Infinite when the company is not burning cash."""
    burn = monthly_burn(expenses, revenue)
    if burn <= 0:
        return float("inf")
    return cash / burn
