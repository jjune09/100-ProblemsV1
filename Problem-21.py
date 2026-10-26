from typing import Tuple

def calculate_statistics(t: Tuple[int, ...]) -> Tuple[Tuple[int, ...], int, int, int, float]:
    if not t:
        raise ValueError("Input tuple must have at least one element.")
    squares = tuple(x*x for x in t)
    mx = max(squares)
    mn = min(squares)
    s = sum(squares)
    avg = s / len(squares)
    return (squares, mx, mn, s, avg)
print(calculate_statistics((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
# Output: ((1, 4, 9, 16, 25, 36, 49, 64, 81, 100), 100, 1, 385, 38.5)