# Из матрицы a(n, m) удалить все неположительные столбцы (столбцы, в которых все
# элементы неположительные). Матрица — список списков.

matrix = [[-1, -5, 2],
          [-3, -4, 0],
          [-9, -5, 2]]

negative_row = -1


def removeNegativeColumns(matrix):
    remove_columns = []
    for i in range(len(matrix[0])):
        count_negative_number = 0
        for j in range(len(matrix)):
            if matrix[j][i] < 0:
                count_negative_number += 1
        if count_negative_number == len(matrix):
            remove_columns.append(i)
    removed_column = 0
    for column in remove_columns:
        for j in range(len(matrix)):
            matrix[j].pop(column - removed_column)
        removed_column +=1

    return (matrix)

print(removeNegativeColumns(matrix))