'''
                    Задача 1
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120    
'''
# Решение 1:
num = int (input('Введите число, для получения факториала: '))
factorial = 1
count = 1
while (count <= num):
    factorial *= count
    count += 1

print (factorial)

#Решение 2:
num = int (input('Введите число, для получения факториала: '))
factorial = 1
while (num > 1):
    factorial *= num
    num -= 1
print (factorial)