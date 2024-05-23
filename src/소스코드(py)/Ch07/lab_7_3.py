#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 7-3 도시의 인구 자료에 대한 슬라이싱을 해보자, 193쪽
#

# 다음과 같은 리스트가 생성되어 있다. 
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

print('서울 인구:', population[1])       # 문제 1)
print('인천 인구:', population[-1])      # 문제 2)

cities = population[0::2]              # 문제 3) 도시 이름 데이터를 추출
print('도시 리스트:', cities)
pops = population[1::2]                # 문제 4) 인구 데이터를 추출
print('인구의 합:', sum(pops))