#Из заданного текста удалить два самых коротких слова.
import re

print("Введите текст: ", end='')
text = input()

def removeTwoShortestWords(text):
    all_words = re.findall(r'\w+', text)
    for i in range(2):
        min_len = len(all_words[0])
        index = 0
        for word in all_words:
            if(len(word)<min_len):
                min_len = len(word)
                index = all_words.index(word)
        all_words.pop(index)
    return ' '.join(all_words)

print(removeTwoShortestWords(text))