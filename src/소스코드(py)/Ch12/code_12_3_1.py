#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-3 CSV에서 원하는 데이터를 뽑아보자
#

import csv 
    
f = open('d:/data/weather.csv')   # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)              # reader() 함수를 이용하여 읽는다. 
header = next(data)               # 헤더를 제거한다. 
for row in data:                  # 반복 루프를 사용하여 데이터를 읽는다. 
    print(row[3], end=',')        # 평균풍속만 출력하고, 쉼표로 연결한다.
f.close()