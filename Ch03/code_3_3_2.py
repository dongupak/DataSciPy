#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 3.3 거듭제곱 연산자 : **, 78쪽
#

bottom = float(input('직각삼각형의 밑변의 길이를 입력하시오: '))
height = float(input('직각삼각형의 높이를 입력하시오: '))
hypotenuse = (bottom ** 2 + height ** 2 ) ** 0.5
print('빗변은', hypotenuse, '입니다')