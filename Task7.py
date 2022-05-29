# В квадратной матрице a(n, n) в каждой строке элемент, расположенный на диагонали,
# увеличить на значение минимального элемента соответствующего столбца. Матрица —
# список списков.

matrix = [[1, 3, 2],
          [3, 1, 0],
          [0, 0, 8]]

for i in range(3):
    min_element = matrix[i][i]
    for j in range(3):
        cur =  matrix[j][i]
        if min_element > cur:
            min_element = cur
    matrix[i][i] = min_element

print(matrix)