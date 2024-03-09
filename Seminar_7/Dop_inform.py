# # #=============================Функция lambda()==================================
# #     '''1. Укорачивание кода и замена функции def с return на lambda функцию'''
# # # Запись 1
# # def noname(x, y):
# #     return x * y

# # noname(2,3)

# # # Запись 2 аналогична записи 1, только короче и с использованием функции lambda
# # f = lambda x, y : x * y  # Имеется функция lambda, принимающая в себя переменные x и y,
# #                         # на выходе получим результат выражения x * y. 
# #                         # Результат данной функции мы решили записать в некую переменную f.
# # f(2,3)

# #     '''2. Использование lambda функции для выборки из массива только ЧЕТНЫХ чисел:'''
# # my_list = [1, 2, 34, 5, 7, 8, 90, 0, 3, 67, 89, 35, 2]
# # '''
# #     Итератор filter применяется только к итерируемым объектам, н-р, my_list, т.е. к тем объектам,
# # которые можно пропустить через цикл for. 
# #     В данном случае, функция filter - перебирает и фильтрует список my_list, с помощью lambda функции. 
# #     lambda функция - помещает в свою переменную х, только те элементы списка my_list,
# # которые удовлетворяют условию x % 2 == 0
# # '''
# # # Запись 1, используя итератор filter
# # res_list = filter(lambda x: x % 2 == 0, my_list)
# # print(*res_list) # 2 34 8 90 0 2
# # print(list(res_list)) # []

# # # Запись 2, используя итератор filter
# # res_list = list(filter(lambda x: x % 2 == 0, my_list))
# # print(*res_list) # 2 34 8 90 0 2
# # # print(res_list) # [2, 34, 8, 90, 0, 2]
# # print(list(res_list)) # [2, 34, 8, 90, 0, 2]

# #     '''3. Раскрытие итератора filter'''
# # my_list = [1, 2, 34, 5, 7, 8, 90, 0, 3, 67, 89, 35, 2]
# # # Запись 1
# # res_list = list(filter(lambda x: x % 2 == 0, my_list))
# # print(res_list) [False, True, True, False, False, True, True, True, False, False, False, False, True]

# # # Запись 2 - аналогична Записи 1, наглядно показываем, раскрытие итератора filter
# # res_list = [] # Создаем пустой список, для сохранения результата
# # f = lambda x: x % 2 == 0 # Результат работы функции lambda записыввем в новую переменную f.
# # for element in my_list: # Перебираем весь список my_list по элементам и поочереди помещаем их в переменную element
# #     if f(element): # помещаем каждый элемент в функцию lambda и проверяем на True условию 
# #         res_list.append(element) # если элемент True условию, то помещаем его в конец ранее созданного списка res_list
# # #Запишем цикл for с использованием list comprehension:
# # # print([element for element in my_list if f(element)]) # [2, 34, 8, 90, 0, 2]
# # print(res_list) # [2, 34, 8, 90, 0, 2]

# #=============================Функция map()==================================
# '''2. Использование функции map() для выборки из массива только ЧЕТНЫХ чисел:'''
# my_list = [1, 2, 34, 5, 7, 8, 90, 0, 3, 67, 89, 35, 2]
# '''
#     В данном случае, функция map - перебирает и применяет к каждому элементу списока my_list 
# действие x ** 2, НЕ ИСПОЛЬЗУЯ условие if, как это делает итератор filter.
# '''
# # Запись 1, используя итератор filter
# res_list = map(lambda x: x ** 2, my_list)
# print(*res_list) # 1 4 1156 25 49 64 8100 0 9 4489 7921 1225 4
# print(list(res_list)) # []

# # Запись 2, используя итератор filter
# res_list = list(map(lambda x: x ** 2, my_list))
# print(*res_list) # 1 4 1156 25 49 64 8100 0 9 4489 7921 1225 4
# # print(res_list) # [1, 4, 1156, 25, 49, 64, 8100, 0, 9, 4489, 7921, 1225, 4]
# print(list(res_list)) # [1, 4, 1156, 25, 49, 64, 8100, 0, 9, 4489, 7921, 1225, 4]

# '''3. Раскрытие итератора map'''
# my_list = [1, 2, 34, 5, 7, 8, 90, 0, 3, 67, 89, 35, 2]
# # Запись 1
# res_list = list(map(lambda x: x % 2 == 0, my_list))
# print(res_list) # [False, True, True, False, False, True, True, True, False, False, False, False, True]

# # Запись 2 - аналогична Записи 1, наглядно показываем, раскрытие итератора map()
# res_list = [] # Создаем пустой список, для сохранения результата
# f = lambda x: x % 2 == 0 # Результат работы функции lambda записыввем в новую переменную f.
# for element in my_list:
#     res_list.append(f(element)) # если элемент True условию, то помещаем его в конец ранее созданного списка res_list
# print(res_list) # [False, True, True, False, False, True, True, True, False, False, False, False, True]
# #Запишем цикл for с использованием list comprehension:
# print([f(element) for element in my_list]) # [False, True, True, False, False, True, True, True, False, False, False, False, True]

# #========================= ДОПОЛНЕНИЕ: ===============================
# # all - если все True, тогда True
# # all - если хотябы кто-нибудь False, тогда False
# # all - если все False, тогда False
# # all - работает, как AND
# # 0 -> False
# # '' -> False
# # [''] -> массив заполненный пустой строкой
# # [] -> пустой массив
# print(all([True, True, True, True])) # True
# print(all([True, False, True, True])) # False
# print(all([False, False, False, False])) # False
# print()
# print(all([1, 2, 3, 4])) # True
# print(all([1, 0, 3, 4])) # False
# print(all([0, 0, 0, 0])) # False
# print()
# print(all(['qwe', 'rty', 'uio', 'asd'])) # True
# print(all(['qwe', '', 'uio', 'asd'])) # False
# print(all(['', '', '', ''])) # False
# print()
# print(all([[''], ('',), {''}, ['']])) # True
# print(all([[''], [], {''}, ['']])) # False
# print(all([{}, [], {}, {}])) # False
# print()

# # any - если все True, тогда True
# # any - если хотябы кто-нибудь True, тогда True
# # any - если все False, тогда False
# # any - работает, как OR
# # 0 -> False
# print(any([True, True, True, True])) # True
# print(any([True, False, True, True])) # True
# print(any([False, False, False, False])) # False
# print()
# print(any([1, 2, 3, 4])) # True
# print(any([1, 0, 3, 4])) # True
# print(any([0, 0, 0, 0])) # False
# print()
# print(any(['qwe', 'rty', 'uio', 'asd'])) # True
# print(any(['qwe', '', 'uio', 'asd'])) # True
# print(any(['', '', '', ''])) # False
# print()
# print(any([[''], ('',), {''}, ['']])) # True
# print(any([[''], [], {''}, ['']])) # True
# print(any([{}, [], {}, {}])) # False
# print()

#========================= ДОПОЛНЕНИЕ про винни пуха: ===============================

#1.
def rifma(poem):
    phrases_list = poem.lower().split()
    sum_vowels = lambda phrase: sum(1 for symbol in phrase if symbol in 'еёаиоуыэюя')
    tmp = sum_vowels(phrases_list[0]) #4 перебрали нулевую фразу
    if all([sum_vowels(phrase) == tmp for phrase in phrases_list[1:]]): #перебираем все оставшиеся фразу
        return 'Парам пам-пам'
    return 'Пам парам'

print(rifma('пара-ра-рам рам-пам-папам па-ра-па-дам'))

#2.
def rifma(poem):
    phrases_list = poem.lower().split()
    sum_vowels = lambda phrase: len(list(filter(lambda symbol: symbol in 'аеёиоуыэюя', phrase)))
    vowels_0 = sum_vowels(phrases_list[0]) #4
    if all(map(lambda phrase: sum_vowels(phrase) == vowels_0, phrases_list[1:])):
        return 'Парам пам-пам'
    return 'Пам парам'

print(rifma('пара-ра-рам рам-пам-папам па-ра-па-дам'))

#3.
def cntVowLet(str):
    cnt = 0
    for let in str:
        if let in vowLet:
            cnt += 1
    return cnt

vowLet = "а, е, ё, и, о, у, ы, э, ю, я".split(', ')

inStr = input("Введите стихотворение Винни-Пуха: ")
res = set(map(cntVowLet, inStr.split()))

if len(res) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')

#4.
def sum_vowels(phrase):
    vowLet = 'еёаиоуыэюя'
    cnt = 0
    for let in phrase:
        if let in vowLet:
            cnt += 1
    return cnt

def chek_rifm(poem):
    vowel_0 = sum_vowels(poem[0])
    for phrase in poem[1:]:
        if sum_vowels(phrase) != vowel_0:
            return 'Пам парам'
    return 'Парам пам-пам'


text= input("Введите стихотворение Винни-Пуха: ").split()
print(chek_rifm(text))
