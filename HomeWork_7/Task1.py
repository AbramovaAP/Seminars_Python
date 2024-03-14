'''
=====================Задача 1 ========================
1) 
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: 
Количество фраз должно быть больше одной!.

Пример
На входе:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

На выходе:
Парам пам-пам

2) 
Пользователь вводит строк, которая разделена по пробелам на фразы,
если все фразы имеют одинаковое количество гласных,
то вывести "Парам пам-пам", иначе "Пам парам"

Н-р, дана строка: 'пара-ра-рам рам-пам-папам па-ра-па-дам'
Она сождержит 3 фразы:  пара-ра-рам             - 4 гласные
                        рам-пам-папам           - 4 гласные
                        па-ра-па-дам            - 4 гласные
                        Вывод: "Парам пам-пам" -> True

Если дана строка: 'пара-ра-рам рам-пам-папам-пам-пам па-ра-па-дам'
Она сождержит 3 фразы:  пара-ра-рам                     - 4 гласные
                        рам-пам-папам-пам-пам           - 6 гласные
                        па-ра-па-дам                    - 4 гласные
                        Вывод: "Пам парам" -> False
'''

def Count_vowels(str):
    count = 0
    for let in str:
        if let in Vowels:
            count += 1
    return count

Vowels = "а, е, ё, и, о, у, ы, э, ю, я".split(', ')
stroka = 'пара-ра-рамрам-пам-папампа-ра-па-дампа-ра-па-дам'
stroka =stroka.split()

if len(stroka) > 1:
    list = []
    for phraza in stroka:
        list.append(Count_vowels(phraza))
        if len(set(list)) != 1:
            print('Пам парам')
            break
    else:
        print('Парам пам-пам')
else:
    print('Количество фраз должно быть больше одной!')


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