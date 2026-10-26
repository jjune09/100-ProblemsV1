def calculate_profit(sales,costs):
    if len(sales) != 5 or len(costs) != 5:
        raise ValueError("Both sales and costs must be tuples of length 5.")
    annual_profits = tuple(s - c for s, c in zip(sales, costs))
    total = sum(annual_profits)
    return (annual_profits, total)
print(calculate_profit((10000.0, 15000.0, 20000.0, 25000.0, 30000.0),
                        costs = (7000.0, 8000.0,
                        9000.0, 11000.0, 12000.0)))
# Output: ((3000.0, 7000.0, 11000.0, 14000.0, 18000.0), 53000.0)