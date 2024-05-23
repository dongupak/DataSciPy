#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-12 빠진 데이터를 깨끗하게 메워 보자
#

import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)
sorted_df = countries_df.sort_values('population')  # 인구 수(population)의 오름차순 정렬
print(sorted_df)