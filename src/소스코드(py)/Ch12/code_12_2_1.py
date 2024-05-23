#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-2 CSV라고 들어봤니
#

import csv     # 판다스가 아닌 파이썬 csv 모듈을 사용함

# 아래의 d:/data/weather.csv 대신 c:/data/weather.csv 과 같이 실습자의
# 환경에 맞는 경로 설정을 하여 사용할 것
f = open('d:/data/weather.csv')  # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)             # reader() 함수를 이용하여 읽는다. 
for row in data: 
    print(row) 
f.close()