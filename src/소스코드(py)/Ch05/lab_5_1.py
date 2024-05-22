#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 5-1 터틀 그래픽으로 여러 개의 원을 그려보자, 132쪽
#

import turtle
t = turtle.Turtle()

for i in range(6):  # 6회 반복하는 코드
    t.circle(100)
    t.left(360/6)