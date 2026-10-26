from typing import List

def calculate_total_payment(num_bills: int, bills: List[float]) -> float:
    if num_bills != len(bills):
        raise ValueError("num_bills must match length of bills list.")
    total = sum(bills)
    if total >= 10000:
        discount = 0.20
    elif total >= 5000:
        discount = 0.10
    elif total >= 1000:
        discount = 0.05
    else:
        discount = 0.0
    return total * (1 - discount)
print(calculate_total_payment(3, [3000, 4000, 3500]))
# Output: 8400.0