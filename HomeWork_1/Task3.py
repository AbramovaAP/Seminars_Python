'''
=====================Задача 3=====================
Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no
'''

num = int (input('Введите 6-ти значное число: '))

#=======================================================
NUM1 = num // 1000 # Получаем первую тройку цифр
#=======================================================
NUM2 = num - NUM1 * 1000 # Получаем вторую тройку цифр
#=======================================================
num_1_1 = NUM1 //100 # Получаем первую цифру

a = num_1_1*100
b = NUM1 - a
num_2_1 = b // 10

num_3_1 = b - (num_2_1 * 10)

summa_1 = num_1_1 + num_2_1 + num_3_1
#=======================================================
num_1_2 = NUM2 //100 # Получаем первую цифру

a = num_1_2*100
b = NUM2 - a
num_2_2 = b // 10

num_3_2 = b - (num_2_2 * 10)

summa_2 = num_1_2 + num_2_2 + num_3_2
#=======================================================
if summa_1 == summa_2:
    print("YES")
else:
    print("NO")