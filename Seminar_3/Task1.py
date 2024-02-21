'''
                Задача 1
Дан список чисел. Определите, сколько в нем
встречается различных чисел.

    Input: [1, 1, 2, 0, -1, 3, 4, 4]
    Output: 6

Примечание: Пользователь может вводить значения
списка или список задан изначально.
'''
# # Решение 1
# from random import randint

# size = int(input ('Введите размер массива: '))
# #Запись 1: создали список
# list_1 = []
# for _ in range(size):
#     n = randint(0, 9)
#     list_1.append(n)
# print(list_1) # [8, 3, 8, 8, 1, 7, 7, 3, 9, 9]
# print()

# #Запись 2, тоже самое, что и запись 1, только болеее компактно и работает быстрее:
# list_2 = [randint(0, 9) for _ in range(size)]
# print(list_2) # [4, 7, 6, 4, 0, 6, 9, 0, 1, 2] 
# print()

# # Способ решения №1
# set(list_1) #  set() множество, которое убирает дубли из списка list_1, останется посчитать только количество элементов, которые остались
# print(set(list_1)) # {1, 3, 7, 8, 9} - для больших массивов это очень хороший вариант, в разы уменьшает массив
# print(len(set(list_1))) # 5


# Решение 2
from random import randint

size = int(input ('Введите размер массива: '))
#Запись 1: создали список
list_1 = []
count = 0
for _ in range(size):
    n = randint(0, 9)
    if n not in list_1:
        count+=1
    list_1.append(n)
print(list_1) # [5, 7, 5, 4, 5]
print(count) # 3

# Решение 3
from random import randint

size = int(input ('Введите размер массива: '))

result = []
count = 0
for num in list_1: # проверяем наличие элементов
    if num not in result:
        count+=1
    result.append(num)

print(count) #3

# Решение 4
# count = 0
# i = 0
# for i in range(len(list_1)):
#     print (i, end=' ')
#     if list_1[i] != list_1[len(list_1)-1]:
#         count += 1
#         i += 1
#     else:
#         i += 1
# print ()
# print (count)
