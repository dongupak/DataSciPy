#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 6.4 여러 개의 값을 넘겨주고 여러 개의 값을 돌려받자, 162쪽
#

def sort_num(n1, n2):       # 2개의 값을 받아오는 함수
    if n1 < n2:
        return n1, n2       # n1이 더 작으면 n1, n2 순서로 반환
    else:
        return n2, n1       # n2가 더 작으면 n2, n1 순서로 반환

print(sort_num(110, 210))   # 110과 210을 함수의 인자로 전달하고 반환되는 값을 출력
print(sort_num(2100, 80))