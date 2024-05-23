#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 8.9 두 수의 약수와 최대공약수 그리고 프로그래밍적인 사고
#

def get_divisors(num):     # num의 약수를 집합형으로 반환함
    divisors = set()
    for i in range(2, num):
        if num % i == 0:
            divisors.add(i)
    return divisors

x = 48
print(x, '의 진약수 :', get_divisors(x))
y = 60
print(y, '의 진약수 :', get_divisors(y))