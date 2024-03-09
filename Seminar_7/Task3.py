'''
=====================Задача 3 ========================
1) Напишите функцию same_by(characteristic, objects), 
которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается, то False.
Для пустого набора объектовб функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику

        Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2 == 0, values): #- в данном случае, характеристака для каждого элемента:lambda x: x % 2 == 0
    print('same') # возвращаем, если все значения True либо False
else:
    print('different') # возвращаем, если хотябы одно значение не является True либо False

        Вывод: 
same
'''
#=================Решение 1=============================
def same_by(characteristic, objects):
    #print(len(set(map(characteristic,objects))) < 2)
    return len(set(map(characteristic,objects))) < 2


values = [1, 21, 11, 3]

if same_by(lambda x: x % 2 == 0, values): 
    print('same') # возвращаем, если все значения True либо False
else:
    print('different') # возвращаем, если хотябы одно значение не является True либо False



#=================Решение 2=============================
def same_by(characteristic, objects):
    print(f'{objects = }') # objects = [0, 20, 10, 4] | objects = [1, 21, 11, 41]
        #через итератор map():
    new_list = list(map(characteristic,objects))
    print(f'{new_list = }') # new_list = [True, True, True, True] | new_list = [False, False, False, False]
        #через итератор filter():
    new_list = list(filter(characteristic,objects))
    print(f'{new_list = }') # new_list = [0, 20, 10, 4] | new_list = []
    return objects == new_list or not new_list

values = [1, 21, 11, 41]

if same_by(lambda x: x % 2 == 0, values): 
    print('same') # возвращаем, если все значения True либо False
else:
    print('different') # возвращаем, если хотябы одно значение не является True либо False

#=================Решение 3=============================
def same_by(characteristic, objects):
    new_list = list(map(characteristic,objects))
    print(f'{new_list = }')
    return any(new_list) == all(new_list) or not new_list

values = []

if same_by(lambda x: x % 2 == 0, values): 
    print('same') # возвращаем, если все значения True либо False
else:
    print('different') # возвращаем, если хотябы одно значение не является True либо False
# Ввод: values = []                 | Вывод:    new_list = []
#                                               same
# Ввод: values = [1, 21, 11, 41]    | Вывод:    new_list = [False, False, False, False]
#                                               same
# Ввод: values = [0, 20, 10, 40]    | Вывод:    new_list = [True, True, True, True]
#                                               same
# Ввод: values = [1, 66, 11, 41]    | Вывод:    new_list = [False, True, False, False]
#                                               different