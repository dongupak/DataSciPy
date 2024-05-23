#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-5 판다스로 데이터 파일을 읽기
#

import pandas as pd 

df = pd.read_csv('d:/data/countries.csv', index_col = 0) # 첫 열을 인덱스 컬럼으로 사용
print(df)