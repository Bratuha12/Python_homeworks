# Для задания 1-7 за основу можете взять код из ДЗ № 8.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
def modify_list(my_list):
    new_list = [value[::-1] if index % 2 else value for index, value in enumerate(my_list)]
    return new_list


list_1 = ['qwe', 'rty', 'uio', 'asd']
print(modify_list(list_1))
##############################################################################
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
def select_elements(my_list):
    new_list = [value for value in my_list if value[0] == 'a']
    return new_list


list_1 = ['aqwe', 'rty', 'uio', 'asd']
print(select_elements(list_1))
##############################################################################
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
def select_elements(my_list):
    new_list = [value for value in my_list if 'a' in value]
    return new_list


list_1 = ['qwe', 'rty', 'uaio', 'asd']
print(select_elements(list_1))
##############################################################################
# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
def select_str(my_list):
    new_list = [value for value in my_list if type(value) is str]
    return new_list


list_1 = [1, 2, 3, "11", "22", 33]
print(select_str(list_1))
##############################################################################
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
def select_unique_symbols(my_str):
    my_set = set(my_str)
    new_list = [symbol for symbol in my_set if my_str.count(symbol) == 1]
    return new_list


my_str = 'we will rock you'
print(select_unique_symbols(my_str))
##############################################################################
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
def create_intersection_list(str_1, str_2):
    my_set = set(str_1) & set(str_2)
    new_list = list(my_set)
    return new_list


my_str_1 = 'we will rock you'
my_str_2 = 'make a big noise'
print(create_intersection_list(my_str_1, my_str_2))
##############################################################################
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
def create_symbol_list(str_1, str_2):
    my_set = set(str_1) & set(str_2)
    new_list = [symbol for symbol in my_set if str_1.count(symbol) == 1 and str_2.count(symbol) == 1]
    return new_list


my_str_1 = 'we will rock you1'
my_str_2 = 'make a big noise1'
print(create_symbol_list(my_str_1, my_str_2))
##############################################################################
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
# 1й вариант
from random import randint, choice

def generate_email(names_list, domains_list):
    random_str = ''.join([chr(randint(ord('a'), ord('z'))) for _ in range(0, randint(5, 7))])
    e_mail = choice(names_list) + '.' + str(randint(100, 999)) + '@' + random_str + '.' + choice(domains_list)
    return e_mail


names = ["king", "miller", "kean", "man"]
domains = ["net", "com", "ua"]
print(generate_email(names, domains))

# 2й вариант
from random import randint, choice
from string import ascii_lowercase

def generate_email(names_list, domains_list):
    random_str = ''.join([choice(ascii_lowercase) for _ in range(0, randint(5, 7))])
    e_mail = choice(names_list) + '.' + str(randint(100, 999)) + '@' + random_str + '.' + choice(domains_list)
    return e_mail


names = ["king", "miller", "kean", "man"]
domains = ["net", "com", "ua"]
print(generate_email(names, domains))
