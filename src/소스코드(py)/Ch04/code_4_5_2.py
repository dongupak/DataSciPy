#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 4.5 터틀 객체와 스크린 객체, 106쪽
#

import turtle           # turtle 모듈을 가져온다

tur1 = turtle.Turtle()  # 터틀 객체를 생성함
tur1.shapesize(5, 3)    # 가로 크기가 원래 크기의 4배, 세로 크기가 원래 크기의 6배로 커짐
tur1.forward(100)