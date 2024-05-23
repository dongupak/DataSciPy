#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 6.8 모듈을 이용해서 함수를 재사용하자
# 나만의 모듈을 만들고 불러서 사용해 보자, 175쪽
#

# filename: my_func.py
def mf_print(msg, n = 1) :      # msg를 n번 반복하는 함수
   print(msg * n)