'''
================Задача 2=================
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
    Ввод:                   Ввод:
    5                       5
    1 2 3 4 5               1 5 1 5 1
    Вывод:                  Вывод:
    0                       2
(каждое число вводится с новой строки)
'''
#================Решение 1==========================
from random import randint

n = randint(10, 20)
arr = [randint(1, 10) for _ in range(n)]
print(arr)
count = 0

for i in range(1, n - 1):
    if arr[i - 1] < arr[i] > arr[i + 1]:
        count += 1
print(count)

print(sum(1 for i in range(1, n - 1) if arr[i - 1] < arr[i] > arr[i + 1]))

# #================Решение 2==========================
# from random import randint

# n = int(input('Введите длину массива: '))

# # # Запись 1:
# # Mass = [] #Пустое место для 1-го массива

# # for _ in range(n):
# #     n = randint(1, 10)
# #     Mass.append(n)
# # print(Mass)

# # Запись 2, аналогична записи 1, только более компактнее:
# Mass = [randint(1, 10) for _ in range(n)]
# print(Mass)

# count = 0
# for i in range(0, len(Mass)-1):
#     if Mass[i-1] < Mass[i] > Mass[i+1]:
#         count += 1
#         #print(Mass[i])
# print(count)

# #Вывод через list comprehension
# print(sum([1 for i in range(0, len(Mass)-1) if Mass[i-1] < Mass[i] > Mass[i+1]]))