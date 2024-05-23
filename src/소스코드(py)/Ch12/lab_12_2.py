#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 12-2 울릉도는 몇 월에 바람이 가장 강할까? - groupby() 활용
#

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv('d:/data/weather.csv', encoding='CP949')

weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean(numeric_only = True)
means['평균풍속'].plot(kind = 'bar')

plt.show()