# Задание 1.
# Ресурс с данными - http://forismatic.com/ru/api/
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.
# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# Имя файла сделать параметром по умолчанию.
# Заголовки csv файла:
# Author, Quote, URL.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
import random
import requests
import csv


def get_quotes(number: int) -> list:
    index = random.randint(1, 1000)
    data = []
    while len(data) < number:
        index += 1
        params = {"method": "getQuote", "format": "json", "key": index}
        r = requests.get('http://api.forismatic.com/api/1.0/', params=params)
        quote = r.json()
        if quote['quoteAuthor']:
            # data.append(quote['quoteText']) # применяем для вывода только цитат
            data.append(quote)
    return data


def sort_by_quote_author(quote_dict):
    quote_author = quote_dict["Author"]
    return quote_author


def write_csv(quotes: list, file_name="quotes.csv"):
    for i in range(len(quotes)):
        quotes[i]['Author'] = quotes[i].pop('quoteAuthor')
        quotes[i]['Quote'] = quotes[i].pop('quoteText')
        quotes[i]['URL'] = quotes[i].pop('quoteLink')
    # quotes.sort(key=sort_by_quote_author) # сортировка с помощью функции sort_by_quote_author
    quotes.sort(
        key=lambda d: d['Author'])  # сортировка с помощью lambda функции
    field_names = ['Author', 'Quote', 'URL']
    with open(file_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names,
                                extrasaction='ignore')
        writer.writeheader()
        writer.writerows(quotes)


print(get_quotes(3))
write_csv(get_quotes(7))
