# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
# 1й вариант
my_list = ['qwe', 'rty', 'uio', 'asd']
new_list = []
for index, value in enumerate(my_list):
    if index % 2 != 0:
        new_list.append(value[::-1])
    else:
        new_list.append(value)
print(new_list)
# 2й вариант
my_list = ['qwe', 'rty', 'uio', 'asd']
new_list = []
for index in range(len(my_list)):
    if index % 2 != 0:
        new_list.append((my_list[index])[::-1])
    else:
        new_list.append(my_list[index])
print(new_list)
##############################################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list = ['aqwe', 'rty', 'uio', 'asd']
new_list = []
for value in my_list:
    if value[0] == 'a':
        new_list.append(value)
print(new_list)
##############################################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list = ['qwe', 'rty', 'uaio', 'asd']
new_list = []
for value in my_list:
    if value.find('a') != -1:
        new_list.append(value)
print(new_list)
##############################################################################
# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
my_list = [1, 2, 3, "11", "22", 33]
new_list = []
for value in my_list:
    if type(value) == str:
        new_list.append(value)
print(new_list)
##############################################################################
# В заданиях 5,6,7 надо использовать множества:
#
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
my_str = 'we will rock you'
new_list = []
my_set = set(my_str)
for symbol in my_set:
    if my_str.count(symbol) == 1:
        new_list.append(symbol)
print(new_list)
##############################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
my_str_1 = 'we will rock you'
my_str_2 = 'make a big noise'
my_set = set(my_str_1) & set(my_str_2)
new_list = list(my_set)
print(new_list)
##############################################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
my_str_1 = 'we will rock you'
my_str_2 = 'make a big noise'
new_list = []
my_set = set(my_str_1) & set(my_str_2)
for symbol in my_set:
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        new_list.append(symbol)
print(new_list)
##############################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
my_dict = {
    'Фамилия': 'Иванов',
    'Имя': 'Иван',
    'Возраст': 30,
    'Проживание': {
        'Страна': 'Украина',
        'Город': 'Запорожье',
        'Улица': 'Почтовая'
    },
    'Работа': {
        'Наличие': True,
        'Должность': 'Начальник отдела'
    }
}
##############################################################################
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
recipe_dict = {
    'Составляющие': {
        'Коржи': {
            'Мука': 1000,
            'Молоко': 200,
            'Масло': 50,
            'Яйцо': 2
        },
        'Крем': {
            'Сахар': 20,
            'Масло': 50,
            'Ваниль': 5,
            'Сметана': 200
        },
        'Глазурь': {
            'Какао': 30,
            'Сахар': 10,
            'Масло': 20
        }
    }
}
##############################################################################
# 10) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
persons = [{"name": "John", "age": 15}, {"name": "Andrew", "age": 50}, {"name": "Jack", "age": 45}]
ages = []
names_length = []
for person in persons:
    ages.append(person["age"])
    names_length.append(len(person["name"]))
min_age = min(ages)
max_length_name = max(names_length)
for person in persons:
    if person["age"] == min_age:
        print(f'Самый молодой человек - {person["name"]}, ему {person["age"]} лет.')
    if len(person["name"]) == max_length_name:
        print(f'Самое длинное имя - {person["name"]}')
average_age = round(sum(ages) / len(ages), 1)
print(f"Средний возраст людей в списке - {average_age} лет.")
##############################################################################
# 11) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# my_dict_1 = {1: 1, 2: 2}
# my_dict_2 = {11: 11, 2: 22}

my_dict_1 = {
    'name': 'Dmitriy',
    'surname': 'Ivanov',
    'age': 35
}
my_dict_2 = {
    'name': 'Ivan',
    'country': 'Ukraine',
    'city': 'Dnepr'
}
# а)
my_set = set(my_dict_1) & set(my_dict_2)
key_list = list(my_set)
print(key_list)
# б)
my_set = set(my_dict_1) - set(my_dict_2)
key_list_2 = list(my_set)
print(key_list_2)
# в)
my_dict_3 = {(key, my_dict_1[key]) for key in key_list_2}
print(my_dict_3)
# г)
# 1й вариант
my_dict_4 = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        my_dict_4[key] = value
    else:
        my_dict_4[key] = [value, my_dict_2[key]]
for key, value in my_dict_2.items():
    if key not in my_dict_1:
        my_dict_4[key] = value
print(my_dict_4)

# 2й вариант
my_dict_4 = {}
my_set_all = set(my_dict_1) | set(my_dict_2)
my_set_intersection = set(my_dict_1) & set(my_dict_2)
for key in my_set_all:
    if key in my_set_intersection:
        my_dict_4[key] = [my_dict_1[key], my_dict_2[key]]
    else:
        my_dict_4[key] = my_dict_1.get(key) or my_dict_2.get(key)
print(my_dict_4)
