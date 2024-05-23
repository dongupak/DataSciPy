#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 10-2 넘파이의 별칭 만들기. 그리고 간단한 배열 연산하기
#

import numpy as np

mid_scores = np.array([10, 20, 30])     # 넘파이 ndarray 객체를 생성
final_scores = np.array([60, 70, 80])   # 넘파이 ndarray 객체를 생성

total = mid_scores + final_scores 
print('시험성적의 합계 :', total)     # 각 요소별 합계가 나타난다
print('시험성적의 평균 :', total/2)   # 평균을 얻기위해 모든 요소를 2로 나눈다.