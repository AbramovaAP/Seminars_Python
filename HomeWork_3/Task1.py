'''
                Задача 1
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X
N = 9
A[i] = 1 3 2 3 4 5 3 1 3
X = 3
-> 4
'''
from random import randint

#1: Запрашиваем у пользователя размер массива:
size = int(input ('Введите размер массива: '))
print()

#2: Создаем рандомный массив из элементов и печатаем его
list_1 = []
for _ in range(size):
    n = randint(0, 9)
    list_1.append(n)
print(('Сгенерированный массив: '))
print(list_1) 
print()

#3: Запрашиваем у пользователя какой элемент нужно проверить на повторяемость
element = int(input ('Введите элемент массива для проверки: '))

#4: цикл для проверки выбранного элемента массива на повторяемость 
count = 0
for i in range(len(list_1)):
    if element == list_1[i]:
        count+=1
print(count) 