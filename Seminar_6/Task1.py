'''
================Задача 1=================
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
    Ввод:                   Вывод:
    7                       3 3 2 12
    3 1 3 4 2 4 12
    6
    4 15 43 1 15 1          (каждое число вводится с новой строки)
'''
#================Решение 1==========================
from random import randint

size1 = int(input("Ввведите длину 1 массива: "))
# mass1 = []

# for _ in range(size1):
#     mass1.append(randint(1,10))
# print(mass1)
mass1 = [randint(1,10) for _ in range(size1)]
print(mass1)

size2 = int(input("Ввведите длину 2 массива: "))
mass2 = [randint(1,10) for _ in range(size2)]
print(mass2)

# res_mass=[]
for num in mass1:
    if num not in mass2:
        print(num, end=" ")
print()
print(*[num for num in mass1 if num not in mass2])

# #================Решение 2==========================
# from random import randint

# n = int(input('Введите длину 1-го массива: '))
# m = int(input('Введите длину 2-го массива: '))

# # # Запись 1:
# # list1 = [] #Пустое место для 1-го массива
# # list2 = [] #Пустое место для 2-го массива

# # for _ in range(n):
# #     list1.append(randint(1, 10))
# # print(list1)

# # for _ in range(m):
# #     list2.append(randint(1, 10))
# # print(list2)

# # Запись 2, аналогична записи 1, только более компактнее:
# list1 = [randint(1, 10) for _ in range(n)]
# print(list1)

# list2 = [randint(1, 10) for _ in range(m)]
# print(list2)
# # list2 = set(list2) # Можно преобразовать список в множество и сравнить их между собой
# # print(list2)

# # Проверяем элементы 1-го массива и выводим только те, которых нет во-2м массиве:

# res_list = []
# for num in list1:
#     if num not in list2:
#         res_list.append(num)
#         print(num, end=' ')