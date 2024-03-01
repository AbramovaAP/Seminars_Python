'''
                    Задача 4
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
    Input:  5 -> 1 2 3 4 5
    Output: 5 4 3 2 1
'''
# # ===================Решение 1==============================
# def reversed(num):
#     elements = input("Введите число: ")
#     if num == 1:
#        print(elements, end=" ") 
#        return
#     reversed(num - 1)
#     print(elements, end=" ") # 5 4 3 2 1

# n = int(input("Введите количество чисел последовательности: "))
# reversed(n)

# #===================Решение 2==============================

# from random import randint
# n = int(input("Введите количество чисел последовательности: "))
# list = []
# for _ in range(n):
#     n = randint(1,5)
#     list.append(n)
# print("Первоначальный список", list) # Первоначальный список [2, 4, 2, 2, 5]
# list.reverse()
# print("Перевернутый список", list) # Перевернутый список [5, 2, 2, 4, 2]


#===================Решение 3==============================
# рандомный ввод и функция
from random import randint

# 3
def reversed(elements, num):
    # num = len(elements)
    # print(num)
    mass = []
    while num <= len(elements) and num !=0:
        mass.append(elements[num-1])
        print(mass, end=" ") 
        # num -= 1
        reversed(elements, num-1)

        if num == 1:
            print(elements[num-1], end=" ") 
            return

# 1
n = int(input("Введите количество чисел последовательности: "))
list = []
for _ in range(n):
    n = randint(1,5)
    list.append(n)
print("Первоначальный список", list) #
# num = len(list)
# print(num)
# print(type(num))

# 2
reversed(list, n)