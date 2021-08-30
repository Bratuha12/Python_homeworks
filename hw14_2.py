# Задание 2.
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"
import json


def read_json_file(file_name: str) -> list:
    with open(file_name, 'r') as json_file:
        return json.load(json_file)


def sort_by_surname(data_list: list) -> list:
    return sorted(data_list, key=lambda d: d['name'].split()[-1])


def filter_by_death_date(data_list: dict) -> list:
    date = data_list['years'].strip('.').split()
    return [int(date[-2]) * -1 if date[-1].upper() == 'BC' else int(date[-1])]


def sort_by_date(data_list: list) -> list:
    return sorted(data_list, key=filter_by_death_date)


def sort_by_words(data_list: list) -> list:
    return sorted(data_list, key=lambda d: len(d['text'].split()))


json_file = read_json_file('data.json')
print(json_file)
print(sort_by_surname(json_file))
print(sort_by_date(json_file))
print(sort_by_words(json_file))
