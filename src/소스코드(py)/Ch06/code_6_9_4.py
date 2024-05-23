#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 6.9 모듈과 별명 만들기, 177쪽
#

import turtle           # 터틀 그래픽 모듈을 가져온다

t = turtle.Turtle()     # 거북이 객체를 생성함, t라는 변수로 참조함
t.shape("turtle")       # 거북이 객체 t에 내리는 명령 shape()은 메소드라고 함
t.forward(100)          # 거북이 객체 t에 내리는 명령 forward() 역시 메소드라고 함 
s = turtle.Turtle()     # 새로운 거북이 객체를 생성함, s라는 변수로 참조함
s.shape("square") 
s.backward(100) 

turtle.done()           # 이 거북이 그래픽 프로그램이 사용자의 입력을 받아서 실행하는 루프로 진입







