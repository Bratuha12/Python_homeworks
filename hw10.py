# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
#
# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
#
# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
#
import os
import time


def make_list_domains(file_name):
    with open(file_name, 'r') as txt_file:
        data = [line.lstrip('.').rstrip() for line in txt_file.readlines()]
    return data


def make_list_names(file_name):
    with open(file_name, 'r') as txt_file:
        data = [line.split('\t')[1] for line in txt_file.readlines()]
    return data

# 1й вариант с использованием словарей для преобразования дат
def modify_date(date):
    day_dict = {
        "1st": "01",
        "2nd": "02",
        "3rd": "03",
        "4th": "04",
        "5th": "05",
        "6th": "06",
        "7th": "07",
        "8th": "08",
        "9th": "09",
        "10th": "10",
        "11th": "11",
        "12th": "12",
        "13th": "13",
        "14th": "14",
        "15th": "15",
        "16th": "16",
        "17th": "17",
        "18th": "18",
        "19th": "19",
        "20th": "20",
        "21st": "21",
        "22nd": "22",
        "23rd": "23",
        "24th": "24",
        "25th": "25",
        "26th": "26",
        "27th": "27",
        "28th": "28",
        "29th": "29",
        "30th": "30",
        "31st": "31",
    }
    month_dict = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    temp_date = date.split()
    output_date = f"{day_dict[temp_date[0]]}/{month_dict[temp_date[1]]}/{temp_date[2]}"
    return output_date


def make_list_dates(file_name):
    with open(file_name, 'r') as txt_file:
        dates = [line.split(' - ')[0] for line in txt_file.readlines() if line.find(' - ') != -1]
        dates_list = [{"date_original": date_original, "date_modified": modify_date(date_original)} for date_original in
                      dates]
    return dates_list


# 2й вариант с использованием модуля time
def change_date(date_in):
    date_2 = time.strptime(date_in.replace(date_in[date_in.find(' ')-2:date_in.find(' ')], ''), '%d %B %Y')
    date_out = time.strftime("%d/%m/%Y", date_2)
    return date_out


def make_list_dates_2(file_name):
    with open(file_name, 'r') as txt_file:
        dates = [line.split(' - ')[0] for line in txt_file.readlines() if line.find(' - ') != -1]
        dates_list = []
    for date_original in dates:
        dates_list.append({"date_original": date_original,
                           "date_modified": change_date(date_original)
                           })
    return dates_list


file_domains = 'domains.txt'
file_names = 'names.txt'
file_authors = 'authors.txt'
print(make_list_domains(file_domains))
print(make_list_names(file_names))
print(make_list_dates(file_authors))
print(make_list_dates_2(file_authors))
