'''
===============Задача 2==============
В некоторой школе решили набрать три новых 
математических класса и оборудовать кабинеты для 
них новыми партами. За каждой партой может сидеть 
два учащихся. Известно количество учащихся в 
каждом из трех классов. Выведите наименьшее 
число парт, которое нужно приобрести для них.
Input: 
        20 21 22(ввод чисел НЕ в одну строку)
Output: 
        32
'''
Class1 = int (input('Введите кол-во учеников в 1-м классе: '))
Class2 = int (input('Введите кол-во учеников в 2-м классе: '))
Class3 = int (input('Введите кол-во учеников в 3-м классе: '))

Parts1 = (Class1 + 1) // 2 #Количество парт в первом классе
Parts2 = (Class2 + 1) // 2
Parts3 = (Class3 + 1) // 2

print(f"{Parts1 + Parts2 + Parts3 = }")
