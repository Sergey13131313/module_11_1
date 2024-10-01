import requests

"""Библиотека requests используется для составления HTTP запросов.
HTTP запросы используются для обмена информацией по протоколу HTTP.
Функция .get()возвращает объект requests.models.Response и код состояния код (200-400) код полученный от сервера"""
re = requests.get('https://ya.ru/')
print(f're, {type(re)}, {re}/n/n')

'''Метод status_code возвращает int код состояния'''
re_status = re.status_code
print(f're_status, {type(re_status)}, {re_status}')

'''метод content возвращает байтстроку только что это не понятно'''
re_content = re.content
print(f're_content, {type(re_content)}, {re_content}')

'''Метод text возвращает строку в которой в формате html храниться содержание сайта'''
re_text = re.text
print(f're_text, {type(re_text)}, {re_text}')

'''Метод json возвращает словарь нет выбрасывает исключение'''
try:
    re_json = re.json()
    print(f're_json, {type(re_json)}, {re_json}')
except requests.exceptions.JSONDecodeError as e:
    print('Не формат словаря')

'''Метод headers возвращает словарь каких-то заголовков, пока не знаю каких'''
re_headers = re.headers
print(f're_headers, {type(re_headers)}, {re_headers}')

aaa = 10
