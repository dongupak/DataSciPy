#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 6.5 변수의 범위는 어디까지인가, 164쪽
#

def print_counter():
    print('counter =', counter)  # 함수 내부의 counter 값

counter = 100
print_counter()
print('counter =', counter)      # 함수 외부의 counter 값