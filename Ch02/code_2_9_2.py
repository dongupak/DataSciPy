#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 2.9 객체와 메소드 그리고 함수, 66쪽
#

import turtle
t = turtle.Turtle()  # 거북이 객체를 생성함, t라는 변수로 참조함
t.shape("turtle")    # 거북이 객체 t에 내리는 명령 shape()은 메소드라고 함
t.forward(100)       # 거북이 객체 t에 내리는 명령 forward() 역시 메소드라고 함
s = turtle.Turtle()  # 새로운 거북이 객체를 생성함, s라는 변수로 참조함
s.shape("square")
s.backward(100)
turtle.done()