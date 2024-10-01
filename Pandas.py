'''Мощный а главное быстый инструмент для работы с многомерными массивами'''
import pandas

df = pandas.DataFrame()
data = pandas.read_csv('tabl.csv')
if not data.empty:
    list_data = data.values
    size = list_data.shape
    head = data.head()
    sum = 0
    x = list_data.shape[0]
    y = list_data.shape[1]
    a = list_data[0, 2]
    for x in range(list_data.shape[0]):
        if list_data[x, 1] % 2 == 0:
            sum += list_data[x, 2]
    print(f'Сумма четных значений {data.columns[1]} = {sum}')









a = 10
