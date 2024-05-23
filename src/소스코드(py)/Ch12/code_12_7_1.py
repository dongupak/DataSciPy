#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-7 슬라이싱으로 행 선택하기
#

import pandas as pd
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)
countries_df['density'] = countries_df['population'] / countries_df['area']
print(countries_df)