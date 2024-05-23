#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 7.10 한번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
# 함수는 튜플을 돌려줄 수 있다, 207쪽
#

def calc_circle(r):         # 반지름이 r인 원의 넓이와 둘레를 동시에 반환하는 함수
    area = 3.14 * r * r
    circum = 2 * 3.14 * r
    return area, circum     # 튜플을 반환함

radius = float(input('원의 반지름을 입력하시오: '))
(a, c) = calc_circle(radius)
print('원의 넓이는{0:7.2f}이고 원의 둘레는{1:6.2f}이다.'.format(a, c))