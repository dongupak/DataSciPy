#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 10-11 상관관계 계산하기
#

import numpy as np

x = [ i for i in range(100) ]
y = [ i ** 2 for i in range(100) ]
z = [ 100 * np.sin(3.14*i/100) for i in range(100) ]

result = np.corrcoef( [x, y, z] )
print(result)
