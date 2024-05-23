#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-6 열을 기준으로 데이터 선택하기
#

import pandas as pd
import matplotlib.pyplot as plt 

weather = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')
weather['평균풍속'].plot(kind='hist', bins=33)
plt.show()