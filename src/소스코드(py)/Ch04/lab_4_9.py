#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 4-9 입력을 받아서 도형 그리기를 해보자, 120쪽
#

import turtle
t = turtle.Turtle() 
t.shape("turtle") 
 
s = turtle.textinput("", "도형을 입력하시오: ") 
if s == "사각형":   # 사용자가 사각형을 입력한 경우 가로, 세로를 물어본다
    s = turtle.textinput("", "가로: ")
    w = int(s) 
    s = turtle.textinput("", "세로: ")
    h = int(s) 
    t.forward(w) 
    t.left(90) 
    t.forward(h) 
    t.left(90) 
    t.forward(w) 
    t.left(90) 
    t.forward(h)
# 나머지 부분은 여러분이 완성해 보세요.
turtle.done()