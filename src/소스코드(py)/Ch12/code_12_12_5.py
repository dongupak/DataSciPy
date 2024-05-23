#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-12 빠진 데이터를 깨끗하게 메워 보자
#

import pandas as pd
import matplotlib.pyplot as plt

countries = pd.read_csv('d:/data/countries.csv', index_col = 0, encoding='CP949')
countries.sort_values(['population', 'area'], ascending = False, inplace = True)
print(countries)