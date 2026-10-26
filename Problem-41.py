def calculate_discounted_prices(prices, discount_percentage):
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")
    factor = 1 - discount_percentage / 100.0
    return [round(p * factor, 2) for p in prices]
print(calculate_discounted_prices([100.0, 250.0, 75.0], discount_percentage = 20.0))
# Output: [80.0, 200.0, 60.0]