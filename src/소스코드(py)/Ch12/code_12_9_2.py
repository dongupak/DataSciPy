#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-9 연도와 월, 일을 다루는 DatetimeIndex와 그룹핑
#

import pandas as pd

weather = pd.read_csv('d:/data/weather.csv', encoding='CP949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month  # 새로운 'month' 열을 만든다
print(weather)