#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 10-11 상관관계 계산하기
#

import numpy as np 

x = [ i for i in range(100) ]       # 0에서 99까지의 값을 요소로 하는 리스트
y = [ i ** 2 for i in range(100) ]  # 0에서 99까지의 값의 제곱을 요소로 하는 리스트

result = np.corrcoef(x, y)
print(result)