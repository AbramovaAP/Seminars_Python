'''
==================Задача 1=========================
За день машина проезжает N километров. Сколько дней нужно, чтобы проехать маршрут длиной M 
километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
Input:
        N = 700                      1 день = N км
        M = 750                      Х дней = М км      => Х = M/N
Output:
        2
'''
import math

N = int (input ('Enter the distance for one day: '))  # Дистанция за 1 день
M = int (input ('Enter total distance: ')) # Общая дистанция

#ВАРИАНТ 1
t1 = math.ceil(M/N)
print ('Distance: ', t1)
print ()

#ВАРИАНТ 2
t2 = (M-1) // N + 1
print ('Distance: ', t2)
print ()

#ВАРИАНТ 3
t3 = (M + N -1) // N 
print ('Distance: ', t3)