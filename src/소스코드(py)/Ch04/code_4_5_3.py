#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 4.5 터틀 객체와 스크린 객체, 106쪽
#

import turtle           # turtle 모듈을 가져온다

tur1 = turtle.Turtle()  # 터틀 객체를 생성함
tur1.shapesize(5, 3)    # 가로 크기가 원래 크기의 4배, 세로 크기가 원래 크기의 6배로 커짐
tur1.forward(100)

tur2 = turtle.Turtle()  # tur2 객체를 생성함
tur2.shapesize(4, 6)    # 원래 크기에서 가로 크기가 4배, 세로 크기가 6배만큼 늘어난 형태 
tur2.shape('square')    # 터틀의 형상을 사각형으로 바꾼다
tur2.left(90)           # 터틀을 왼쪽으로 회전시킨다
tur2.forward(200)       # 현재 방향에서 200 픽셀 전진시킨다