
import requests
from pprint import pprint
import numpy as np
import pandas as pd


print('Задание № 1: requests - запросить данные с сайта и вывести их в консоль')

response = requests.get('https://api.coinlore.net/api/exchanges/')
pprint(response.status_code)
pprint(response.headers['content-type'])
pprint(response.encoding)
pprint(response.json())


print('Задание № 2: pandas - считать данные из файла,'
      ' выполнить простой анализ данных (на своё усмотрение)'
      ' и вывести результаты в консоль.')

dates = pd.date_range("20240101", periods=10)

pprint(dates)

print('Задание № 3: pnumpy - создать массив чисел, выполнить'
      ' математические операции с массивом и вывести результаты в консоль')

df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list("ABCD"))

pprint(df)

