# В последовательности a(n) найти сумму целых элементов, расположенных между
# минимальным и максимальным элементами.
from typing import Tuple

t = 9, 2, 1, 4, 5, 6, 7, 8, 9, 10
max_element = t[0]
min_element = t[0]
max_index = 0
min_index = 0


for number in t:
    if number > max_element:
        max_element = number
        max_index = t.index(number)
    if number < min_element:
        min_element = number
        min_index = t.index(number)

if min_index > max_index:
    srez =t[(max_index + 1): min_index]
    sum_element = sum(srez)
if max_index > min_index:
    srez =t[(min_index + 1): max_index]
    sum_element = sum(srez)
print(sum_element)
