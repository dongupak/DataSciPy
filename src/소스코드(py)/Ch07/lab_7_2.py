#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 7-2 2에서 100까지의 소수를 구해보자, 189쪽
#

primes = []                     # 소수를 담을 리스트 초기화

for n in range(2, 101):
    is_primes = True            # 일단 n을 소수라고 두자
    for num in range(2, n):
        if n % num == 0:        # n이 소수가 아닐 경우 is_prime을 False로 둔다
            is_primes = False   
    if is_primes:
        primes.append(n)        # 소수로 판정된 n을 리스트에 넣자

print('2에서 100사이의 소수들 :')
print(primes)