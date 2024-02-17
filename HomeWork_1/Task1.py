'''
===================Задача 1====================
Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

num = int (input('Введите трехзначное число: '))
num_1 = num //100 # Получаем первую цифру
print( num_1 )
print()

a = num_1*100
b = num - a

num_2 = b // 10
print( num_2 )
print()

num_3 = b - (num_2 * 10)
print( num_3 )
print()

summa = num_1 + num_2 + num_3

print( summa )