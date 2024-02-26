'''
                    Задача 2
    Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
    Input:  She sells sea shells on the sea shore The shells
            that she sells are sea shells I'm sure So if she sells sea
            shells on the sea shore I'm sure that the shells are sea
            shore shells
    Output: 13
'''
line = "She sells sea shells on the sea shore The shells "\
        "that she sells are sea shells I'm sure So if she sells sea "\
        "shells on the sea shore I'm sure that the shells are sea "\
        "shore shells".lower() # Преобразуем весь текст в маленький регистр
print(line)
print()
# Преобразуем строку в список
print(line.split())
print()
# Преобразуем список в множество, 
# т.к. множество содержит ТОЛЬКО УНИКАЛЬНЫЕ значения, 
# то из нашего списка убирутся все дубликаты
print(set(line.split()))
print()
#Подсчитываем количество элементов сформировавшегося списка
print(len(set(line.split())))
