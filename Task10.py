# Подсчитать количество несовпадающих пар символов заданного текста (не считая
# пробелы!) при условии, что пары формируются с начала и с конца текста (1-й и последний
# символы, 2-й и предпоследний и т.д.).

text = input()
text = text.replace(" ", "", len(text))
print(text)
dismatch_pair = 0
text_as_list = list(text)
print(text_as_list)
half_text = (int)(len(text_as_list) / 2) - 1

if (len(text) % 2 == 1):
    dismatch_pair += 1
    text_as_list.pop((int)(len(text) / 2))
print(text_as_list)

i, j = 0, (len(text_as_list) - 1)
while i != half_text + 1:
    if text_as_list[i] != text_as_list[j]:
        dismatch_pair += 1
    i = i + 1
    j = j - 1
print("Количество несовпадающих символов: ", end="")
print(dismatch_pair)