from typing import List

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix)
    # วิธีสั้น: return [list(row) for row in zip(*matrix)]
    return [list(row) for row in zip(*matrix)]
print(transpose_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))