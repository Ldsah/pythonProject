# Даны два текстовых файла. Записать в третий только те строки, которые есть в первом файле и нет во втором.


text1 = list(open("Utka1.txt").readlines())
text2 = list(open("Utka2.txt").readlines())
text3 = open("Utka3.txt", 'w+')
for word1 in text1:
    word1_repeats = False
    for word2 in text2:
        if word1 == word2:
            text1.remove(word1)
            word1_repeats = True
    if word1_repeats == False:
        text3.write(word1)
    else:
        word1_repeats = False