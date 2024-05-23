#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-12 빠진 데이터를 깨끗하게 메워 보자
#

import pandas as pd

weather = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')
weather.fillna(0, inplace = True)  # 결손값을 0으로 채움, inplace를 True로 설정해 원본 데이터를 수정

print(weather.loc['2012-02-11'])   # 2012년 2월 11일 데이터가 삭제되지 않음