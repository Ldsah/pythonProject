# В матрице a(n, m) поменять местами столбцы с минимальным и максимальным
# количествами четных элементов. Матрица — список списков.

matrix = [[11, 2, 5],
          [3, 14, 2]]

count = 0
even = 0
max_column = 0
min_column = 0
max_even = 0
min_even = 0
changed_matrix = matrix
#скорее всего обнуляется каждый проход значение min_column и max_column, дебажить
# поиск минимального и максимального колчества четных элементов по столбцам

for i in range(3):
    for j in range(2):
        if matrix[j][i] % 2 == 0:
            even += 1
        if even > max_even:
            max_even = even
            max_column = i
        if even < min_even:
            min_even = even
            min_column = i
    even = 0

# смена столбцов местами
for i in range(3):
    for j in range(2):
        if i == min_column:
            changed_matrix[i][j] = matrix[min_column][j]
        if i == max_column:
            changed_matrix[i][j] = matrix[max_column][j]

print(matrix)
print(changed_matrix)
