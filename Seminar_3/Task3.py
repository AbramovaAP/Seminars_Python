# '''
#                 Задача 3
# Напишите программу для печати всех уникальных
# значений в словаре.

#     Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#     {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
#     {" VIII":" S007 "}]
#     Output: {'S005', 'S002', 'S007', 'S001', 'S009'} множество set - строковый тип

# Примечание: Список словарей задан изначально.
# Пользователь его не вводит
# '''
# # #Решение 1:
# # listd_1 =    [{"V": "S001", "X": "S0085"}, {"V": "S002"}, {"VI": "S001"}, 
# #             {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, 
# #             {"VIII":"S007"}]
# # res_set = set()
# # for dict_cur in listd_1:
# #     for v in dict_cur.values():
# #         res_set.add(v)
# # print(res_set)
# # #другая запись
# # print ({v.strip() for dict_cur in listd_1 for v in dict_cur.values()})

# # #Решение 2:
# # listd_1 =       [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# #                 {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
                
# # res_set = set()
# # for dict_cur in listd_1:
# #     res_set.add(*dict_cur.values()) # работают только для одного элемента в списке
# # print(res_set)

# #Решение 3:
# listd_1 =       [{"V": "S001", "X": "S0085"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#                 {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
                
# res_set = set()
# for dict_cur in listd_1:
#     res_set.update(dict_cur.values()) # добавляет все элементы списка
# print(res_set)




#ДОП:
my_set = {12, 234, 45, 5, 78, 456, 45}
text = 'python'
my_list = [11, 22, 33]
num = 999

# my_set.add(text)
# my_set.add(my_list)
# my_set.add(num)

print(my_set.update(text))
print(my_set.update(my_list))
# my_set.update(num)