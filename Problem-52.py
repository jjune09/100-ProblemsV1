from typing import List

def group_by_unit_digit(numbers: List[int]) -> List[List[int]]:
    groups = [[] for _ in range(10)]
    for x in numbers:
        unit = abs(x) % 10
        groups[unit].append(x)
    return groups
print(group_by_unit_digit([21, 34, 51, 23, 37, 44, 60, 11, 91, 99]))