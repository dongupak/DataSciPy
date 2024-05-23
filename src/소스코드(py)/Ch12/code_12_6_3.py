#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-6 열을 기준으로 데이터 선택하기
#

import pandas as pd 
import matplotlib.pyplot as plt

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)

countries_df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm') )
plt.show()
