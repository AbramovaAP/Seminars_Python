'''
=====================Задача 2 ========================
1) 

2) Дан список размеров (длина, ширина) эллипсов
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]- список кортежей
- Напишите функцию find_farthest_orbit(list_of_orbits), которая находит
площадь самого большого элипса и возвращает КОРТЕЖ с его размерами.
- Площадь элипса вычисляется по формуле S = pi * a * b, 
где a и b - длина и ширина осей эллипса соответственно.
- Площадь кругов учитывать не нужно, т.е. если у эллипса a==b, то это круг.
- При решении задачи нужно использовать списочные выражения.
- Гарантируется, что самый большой эллип всего один.
'''
#==========Решение 1====================
from math import pi

def find_farthest_orbit(list_of_orbits):
    s_max = 0
    for a, b in list_of_orbits:
        if a != b:
            s = pi * a * b
            if s > s_max:
                s_max = s 
                a_b = a, b # сохраняем найденный кортеж в новую переменную
    return a_b

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits)) #(2.5, 10)

#==========Решение 2====================
from math import pi

def find_farthest_orbit(list_of_orbits):
    list_of_ellips = [a_b for a_b in list_of_orbits if a_b[0] != a_b[1]]  # где a_b[0] -> a
                                                                          #     a_b[1] -> b
    list_of_areas = [pi * a * b for a, b in list_of_ellips]
    max_area = max(list_of_areas)
    i_max_area = list_of_areas.index(max_area)
    return list_of_ellips[i_max_area]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))#(2.5, 10)

#==========Решение 3====================
from math import pi

def find_farthest_orbit(list_of_orbits):
    list_of_ellips = list(filter(lambda a_b: a_b[0] != a_b[1], list_of_orbits))  # где a_b[0] -> a
                                                                                 #     a_b[1] -> b
    list_of_areas = list(map(lambda a_b: pi * a_b[0] * a_b[1], list_of_ellips))   # где a_b[0] -> a
                                                                                  #     a_b[1] -> b
    max_area = max(list_of_areas)
    i_max_area = list_of_areas.index(max_area)
    return list_of_ellips[i_max_area]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))#(2.5, 10)
