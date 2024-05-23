#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 10-3 2차원 배열 연습하기
#

import numpy as np

x = np.array( [['a', 'b', 'c', 'd'],
               ['c', 'c', 'g', 'h']])
mat_a = np.array( [[10, 20, 30], [10, 20, 30]])
mat_b = np.array( [[2, 2, 2], [1, 2, 3]])

print(x [ x == 'c' ])  # 'c' 원소만 있는 부분을 추출함  
print(mat_a - mat_b)  # 배열 mat_a의 모든 원소에서 mat_b의 모든 원소를 뺀다