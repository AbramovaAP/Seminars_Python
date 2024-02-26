'''
                    Задача 1
    Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
    Input: a a a b c a a d c d d
    Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''

                    # # Решение 1 (минус данного решения в том, 
# # что в конце вывода ставится пробел и не все автотесты этот пробел пропускают)
# text_lst = "a a a b c a a d c d d". split()
# dict_letters = {} #Пустой словарь, для хранения количества 
#                 #каждой повторяющейся переменной, 
#                 #т.е. разные count для разных букв
# for letter in text_lst:
#     if letter not in dict_letters:
#         dict_letters[letter] = 0
#         print(letter, end=' ')
#     else:
#         dict_letters[letter] += 1
#         print(f"{letter}_{dict_letters[letter]}", end=' ')

                    # Решение 2 (вариант с собиранием строки)
text_lst = "a a a b c a a d c d d". split() # Преобразуем строку в список
dict_letters = {}
output_string = ""
for letter in text_lst:
    if letter not in dict_letters:
        output_string += letter + " "
    else:
        output_string += f"{letter}_{dict_letters[letter]} "
    dict_letters[letter] = dict_letters.get(letter, 0) + 1  # Переприсваиваем в библиотеке dict_letters значению, 
    # которое находится под ключом letter, другое значение. Если така\ буква есть, то все это выражение возвращает
    # значение этой буквы, если буквы нет, то выражение возвращает значение None
    # (Такой исход нас не устраивает, поэтому мы добавили "0", теперь вместо None
    # будет возвращаться число 0).
    # Метод .get - ищет значение в библиотеке  dict_letters по ключу letter.
print(output_string.rstrip())  # метод .rstrip() убирает все пробелы, 
# табуляцию и прочие разделители, убирает пробел с правой стороны/
# Данный способ вывода лучше использовать для АВТОТЕСТОВ, чтобы избежать лишних пробелов

                    # Решение 3 
text_lst = "a a a b c a a d c d d". split()
dict_letters = {}
output_string = ""
for letter in text_lst:
    dict_letters[letter] = dict_letters.get(letter, -1) + 1
    if not dict_letters[letter]:
        output_string += letter + " "
    else:
        output_string += f"{letter}_{dict_letters[letter]} "
print(output_string.rstrip())