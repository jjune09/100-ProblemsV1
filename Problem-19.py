def sum_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0]) if rows else 0
    result = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result
print(sum_matrices([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [[4,3,2,1],[4,3,2,1],[4,3,2,1]]))
# Output: [[5, 5, 5, 5], [9, 9, 9, 9], [13, 13, 13, 13]]