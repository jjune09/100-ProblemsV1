from typing import List

def calculate_median(lst: List[int]) -> float:
    
    if not lst:
        raise ValueError("List cannot be empty")

    lst_sorted = sorted(lst)
    n = len(lst_sorted)
    mid = n // 2

    if n % 2 == 1:
        # จำนวนเป็นคี่ → คืนค่ากลาง
        return float(lst_sorted[mid])
    else:
        # จำนวนเป็นคู่ → เอาค่าเฉลี่ยของสองค่ากลาง
        return (lst_sorted[mid - 1] + lst_sorted[mid]) / 2.0

nums = [8, 4, 7, 4, 6, 2, 10, 9, 3, 7, 1]
print(calculate_median(nums)) 