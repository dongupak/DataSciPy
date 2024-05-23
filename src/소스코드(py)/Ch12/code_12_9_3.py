#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-9 연도와 월, 일을 다루는 DatetimeIndex와 그룹핑
#

import pandas as pd

weather = pd.read_csv('d:/data/weather.csv', encoding='CP949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month  # 새로운 'month' 열을 만든다

# numeric_only = True라는 키워드 인자를 통해서 일시 열을 계산에서 제외시키도록 한다
means = weather.groupby('month').mean(numeric_only = True) # 'month'를 기준으로 묶고 평균을 구함

print(means)    # 그룹으로 묶인 'month' 데이터를 기준으로 평균값을 출력한다