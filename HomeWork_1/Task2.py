'''
========================Задача 2===============================
Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе.
Вывести через пробел кол-во журавликов, сделанных Петей, Катей и Колей.
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
'''

quantity = int (input('Введите общее число журавликов: '))

F = quantity // 3 # Кол-во журавликов, кот сделали Коля и Петя вместе

res = F * 2 # Кол-во журавликов, которые сделала Катя 

print( F//2, res, F//2 )