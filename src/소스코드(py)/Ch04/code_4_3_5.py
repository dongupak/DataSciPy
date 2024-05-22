#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 4.3 배타적 조건에 따라 실행하는 if-else 문
# if-else 문으로 다양한 코드를 작성해보자, 103쪽
#

num = int(input("정수를 입력하시오: "))

if num < 0 :
    print("음수입니다.")
else:
    print("양수입니다.")
    if num % 2 == 0 :
        print("짝수입니다.")
    else:
        print("홀수입니다.")