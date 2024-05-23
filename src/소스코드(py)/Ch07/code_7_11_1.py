#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 7.11 zip() 함수를 사용한 집적화, 208쪽
#

name = ['서울', '부산', '광주']                     # 도시의 이름
population = (9765, 3441, 1501)                 # 도시의 인구(단위: 천명)

city_info = list(zip(name, population))         # 집적화한 자료를 리스트 자료형으로 만들기 
print('city_info =', city_info)