#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 6.4 여러 개의 값을 넘겨주고 여러 개의 값을 돌려받자, 162쪽
#

def calc(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2  # 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 반환

n1, n2 = 200, 100
t1, t2, t3, t4 = calc(n1, n2)  # 네 개의 값을 반환받기 위해 4개의 변수를 사용함
print(n1, '+', n2, '=', t1)
print(n1, '-', n2, '=', t2)
print(n1, '*', n2, '=', t3)
print(n1, '/', n2, '=', t4)