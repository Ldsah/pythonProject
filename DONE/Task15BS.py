# За минимальное количество шагов проверить, есть ли в упорядоченной по убыванию
# последовательности a(n) некоторая величина b. Если есть, то указать ее порядковый номер.

t = 4, 2, 1

target = 3
left_border = 0
right_border = len(t) - 1

while left_border != right_border:
    middle = int((left_border + right_border) / 2)
    if (t[middle] > target):
        left_border = middle + 1
    else:
        right_border = middle

if t[left_border] == target:
    print(left_border)
