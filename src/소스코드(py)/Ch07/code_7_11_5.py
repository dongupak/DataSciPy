#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 7.11 zip() 함수를 사용한 집적화
# 집적화된 항목들을 풀어보자, 209쪽
#

city_info = [('서울', 9765),('부산', 3441),('인천', 2954),('광주', 1501),('대전', 1531)]
city_name, city_pop = zip(*city_info)    

max_pop = max(city_pop) 
print('max_pop =', max_pop)