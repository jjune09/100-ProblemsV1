def calculate_total_cost(fried_eggs: int, omelets: int, boiled_eggs: int) -> int:
    if fried_eggs < 0 or omelets < 0 or boiled_eggs < 0:
        raise ValueError("Quantities must be non-negative")
    return fried_eggs * 7 + omelets * 10 + boiled_eggs * 5
print(calculate_total_cost(2, 3, 1))