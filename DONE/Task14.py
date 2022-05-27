# Дан текст. Найти множество встречающихся в тексте латинских букв. (только латинские)

text = input()
text_as_list = list(text)
many_letters = set()
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

for l in letters:
    if l in text_as_list:
        many_letters.add(l)

if (len(many_letters) != 0):
    print(many_letters)
