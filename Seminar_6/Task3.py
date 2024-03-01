'''
================Задача 3=================
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
    Ввод:               Вывод:
    1 2 3 2 3           2
'''

# #Решение 1
# from random import randint

# n = int(input('Введите длину массива: '))

# # # Запись 1:
# # list = [] 
# # for _ in range(n):
# #     n = randint(1, 10)
# #     list.append(n)
# # print(list)

# # Запись 2, аналогична записи 1, только более компактнее:
# list = [randint(1, 5) for _ in range(n)]
# print(list)

# count = 0
# for i in range(0, len(list)):
#     for j in range(i+1, len(list)):
#         if list[i] == list[j]:
#             #print(list[i], list[j])
#             count += 1
# print(count)

#Решение 2
from random import randint

n = int(input('Введите длину массива: '))
list = [randint(1, 5) for _ in range(n)]
print(list)

count = 0
for i in range(0, len(list)):
    count += list[i+1:].count(list[i])
print(count)