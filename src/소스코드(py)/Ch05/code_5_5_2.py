#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 5.5 일정한 횟수 반복에 while 사용하기, 138쪽
#

import turtle

t = turtle.Turtle()
i = 0
while i < 4:
    t.forward(100)
    t.right(90)
    i = i + 1