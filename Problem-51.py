from typing import List, Tuple

def separate_even_odd(numbers: List[int]) -> Tuple[List[int], List[int]]:
    even, odd = [], []
    for x in numbers:
        (even if x % 2 == 0 else odd).append(x)
    return even, odd
print(separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))