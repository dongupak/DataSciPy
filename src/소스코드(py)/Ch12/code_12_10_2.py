#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-10 데이터를 특정한 값에 기반하여 묶는 기능 : 그룹핑
#

import pandas as pd

weather = pd.read_csv('d:/data/weather.csv', encoding='CP949')
weather['year'] = pd.DatetimeIndex(weather['일시']).year  # 새로운 'year' 열을 만든다
y_means = weather.groupby('year').mean(numeric_only=True)
print(y_means)

