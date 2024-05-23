#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-2 CSV 데이터의 내용을 읽어보자
#

import csv        # 판다스가 아닌 파이썬 csv 모듈을 사용함
 
f = open('d:/data/weather.csv')  # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)             # csv의 reader() 함수를 이용하여 읽는다. 
header = next(data)              # 헤더를 제거한다. 
for row in data:                 # 반복 루프를 사용하여 데이터를 읽는다. 
    print(row) 
f.close()                        # 파일을 닫는다.