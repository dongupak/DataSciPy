#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 10-3 강력한 넘파이 배열의 연산을 알아보자
#

import numpy as np
import time

start = time.time()   # 시작 시간을 저장
# 벡터화 연산 대신 반복문을 사용하자.
total = 0
for i in np.arange(100000):
   total = i + total
end = time.time()  # 종료 시간을 저장

print('total =', total)
print("{:.5f} sec".format(end-start)) # 수행시간 출력