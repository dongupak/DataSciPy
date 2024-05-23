#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 10-6 배열의 형태를 바꾸어 보자.
#

import numpy as np 
 
a = np.arange(1, 37)
print('a :\n', a)

b = a.reshape(3, 12)
print('b :\n', b)

c = a.reshape(4, 9)
print('c :\n', c)

d = a.reshape(3, 2, 6)
print('d :\n', d)