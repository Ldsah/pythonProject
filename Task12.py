#Из заданного текста удалить все знаки препинания.
import re


text = input()
changed_text = re.sub(r'[?,.!;:-]', ' ', text)
print(changed_text)