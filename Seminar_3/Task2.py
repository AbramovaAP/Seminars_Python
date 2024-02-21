'''
                Задача 2
    Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
            0   1  2  3  4
    Input:  [1, 2, 3, 4, 5] k = 3
            -5 -4 -3 -2 -1
    Output: [3, 4, 5, 1, 2]

Примечание: Пользователь может вводить значения
списка или список задан изначально.
'''
# i = 0
# [1, 2, 3, 4, 5] k = 2 -> [4, 5, 1, 2, 3]: Элемент с индексом (i = 2) встает на первое место в массиве
# [1, 2, 3, 4, 5] k = 3 -> [3, 4, 5, 1, 2]: Элемент с индексом (i = 3) встает на первое место в массиве
# [1, 2, 3, 4, 5] k = 4 -> [2  3  4  5  1]: Элемент с индексом (i = 4) встает на первое место в массиве

#Решение 1
# list_1 = [1, 2, 3, 4, 5]
# print(list_1)
# k = 4
# left = list_1[:-k] # первые 2 элемента, крайний индекс до числа с индексом -k в срезах не учитывается
# # print(left)
# right = list_1[len(list_1)- k:] # крайние 3 элемента
# # print(right)
# # print(right + left)

#Решение 2
list_1 = [1, 2, 3, 4, 5]
#print(list_1)
k = 34 % len(list_1) # чтобы не делать лишних итераций вычисляем %. Вместо 34 итераций будет всего 4

for i in range(k):

    #print(list_1.pop()) # данная запись удаляет с конца значения, количество значений = k 
    last_num = list_1.pop() # удалили 3 последних элемента и сохранили их в новую переменную
    list_1.insert(0, last_num)  # крайний удаленный элемент вставляем на 1-ое место
#print(list_1) # [3, 4, 5, 1, 2] при k = 3
print(list_1) # [3, 4, 5, 1, 2] при k = 8 % len(list_1) - если сдвиг больше, чем длина списка. Сдвиг пройдется по кругу и встанет на сдвиг k = 3.
