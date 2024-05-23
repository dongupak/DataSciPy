#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 7.11 zip() 함수를 사용한 집적화
# 집적화된 항목들을 풀어보자, 209쪽
#

city_info = [('서울', 9765),('부산', 3441),('인천', 2954),('광주', 1501),('대전', 1531)]
city_name, city_pop = zip(*city_info)  

min_pop = min(city_pop)
n = city_pop.index(min_pop)
print('최소 인구 도시: {0}, 인구: {1} 천명'.format(city_name[n], min_pop)) 
print('리스트 도시 평균 인구: {0} 천명'.format(sum(city_pop) / len(city_pop)))