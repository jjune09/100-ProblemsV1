from typing import Set, Tuple

def calculate_set_differences(set1: Set, set2: Set) -> Tuple[Set, Set]:
    """
    หาค่าที่ต่างกันระหว่างเซตสองชุด
    Return: (set1_minus_set2, set2_minus_set1)
    """
    diff1 = set1 - set2  # ค่าใน set1 ที่ไม่มีใน set2
    diff2 = set2 - set1  # ค่าใน set2 ที่ไม่มีใน set1
    return (diff1, diff2)

set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
print(calculate_set_differences(set1, set2))