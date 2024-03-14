'''
=====================Задача 1 ========================
1) У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое

2) Дан код:
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] #Или любой другой список
transformed_values = list(map(transformation, values))
if value == transformed_values:
    print("ok")
else:
    print("fail")

В переменную ~TRANSFORMATION~ нужно прописать такую функцию ,чтобы в переменной 
~TRANSFORMED_VALUES~ пролучилась КОПИЯ списка ~VALUES~
'''
# Иной способ создания КОПИИ списка
transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Или любой другой список
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print("ok")
else:
    print("fail")