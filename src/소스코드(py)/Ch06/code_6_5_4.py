#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 6.5 변수의 범위는 어디까지인가
# 함수 안에서 전역변수 사용하기 : global 키워드, 165쪽
#

def calculate_area(radius): 
    global area                 # 전역변수 area를 사용함
    area = 3.14 * radius**2 
    return                      # 반환하는 값이 없음
 
area = 0 
r = float(input("원의 반지름을 입력하세요 : ")) 
calculate_area(r) 
print(area) 