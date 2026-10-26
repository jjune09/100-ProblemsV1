def calculate_investment_growth(principal: float, annual_rate: float, years: int) -> list[float]:
    results = []
    for year in range(1, years + 1):
        amount = principal * (1 + annual_rate / 100) ** year
        results.append(round(amount, 2))
    return results
print(calculate_investment_growth(1000, 5, 5))
# Output: [1050.0, 1102.5, 1157.63, 1215.51, 1276.28]