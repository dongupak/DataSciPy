#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-11 조건에 맞게 골라내자 : 필터링
#

import pandas as pd

weather = pd.read_csv('d:/data/weather.csv', encoding='CP949')
missing_data = weather [ weather['평균풍속'].isna() ] 
print(missing_data)