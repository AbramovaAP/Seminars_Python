'''
                    Задача 2
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
    Input: 5 -> 1 3 3 3 4
    Output: 1 3 3 3 1
'''
# #================Решение 1===================================
# # 1.
# def max_to_min(numbers):
#     max_num = max(numbers) #Встроенная функция для поиска max элемента в списке 
#     min_num = min(numbers) #Встроенная функция для поиска min элемента в списке
#     #Цикл для замены макс эл-та на мин эл-нт
#     while max_num in numbers:
#         max_i = numbers.index(max_num)# Определяем индекс max элемента в списке
#         numbers[max_i] = min_num #Замена макс эл-та на мин эл-нт
#     return numbers


# # 2.
# from random import randint
# n = int(input("Введите количество оценок: "))

# # marks = [] #Пустой список marks - оценки
# # for _ in range(n):
# #     n = randint(1,5)
# #     marks.append(n)
# # print(marks)

# # Создание рандомных чисел, через list comprehension:
# marks = [randint(1,5) for _ in range(n)]
# print(marks)

# # 3.
# # Вызов функции замены макс чисел на мин:
# print(max_to_min(marks))

#================Решение 2===================================

from random import randint
n = int(input("Введите количество оценок: "))

#1. Рандомно создали число за пределами списка
first_num = randint(1,5)
min_num = first_num
max_num = first_num

#2. Получаем список индексов максимальных чисел:
max_i = [0]
marks = [first_num] #Создали список пока с единственным числом, 
                    # нужно в него еще индексы добавить, 
                    # если макс чисел в списке будет больше, чем 1
for i in range(1, n):
    num = randint(1,5)
    marks.append(num)
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
        max_i = [i]
    elif num == max_num:
        max_i.append(i)
print(marks) # Список рандомных оценок
print(max_i) # Список индексов максимальных оценок

#3. Цикл для замены макс оценок на мин
for i in max_i: # т.е. проходимся по индексам максимальных оценок
    marks[i] = min_num
print(marks) # Список измененных оценок
