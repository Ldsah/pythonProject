# Написать программу, умеющую делать так:
# «По рзелульаттам илссеовадний одонго анлигйсокго унвиертисета, не иеемт занчнеия, в
# кокам пряокде рсапожолены бкувы в солве. Галвоне, чотбы преавя и пслоендяя бквуы
# блыи на мсете. Осатьлыне бкувы мгоут селдовтаь в плоонм бсепордяке, все-рвано ткест
# чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы не чиатем кдаужю бкуву по
# отдльенотси, а все солво цликеом.»
import random
import re

text = "Panapple eaten by girl."
list_of_words = re.findall(r'[0-9]+|[A-z]+|,| |"|!|.|', text)
print(list_of_words)
for word in list_of_words:
    len_of_word = len(word)
    if (len_of_word > 3):
        index = list_of_words.index(word)
        list_of_symbol = list(word)
        # выбираю первую и последнюю буквы
        first_letter = word[0]
        last_letter = word[len_of_word - 1]
        # удаляю первую и последнюю буквы из слова
        list_of_symbol.remove(first_letter)
        list_of_symbol.remove(last_letter)
        # перемешиваю оставшиеся буквы и формирую конечный результат слова
        random.shuffle(list_of_symbol)
        list_of_symbol = ''.join(list_of_symbol)
        word = first_letter + list_of_symbol + last_letter
        list_of_words[index] = word
print(''.join(list_of_words))
