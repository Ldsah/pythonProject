# После каждого из трех наибольших дробных элементов последовательности a(n) вставить
# значение их полусуммы.

t = [1.2, 9.0, 8.0, 5.2, 22.8, 8.2, 21.5, 4.0]
index_max_element = []


def insertHalfSumLargestElements(t):
   sorted_list = sorted(t)
   max_elements = sorted_list[-3:]
   half_sum = sum(max_elements)/2
   print(half_sum)
   for i in range(3):
      t.insert(t.index(max_elements[i]) + 1, half_sum)
   print(t)

insertHalfSumLargestElements(t)