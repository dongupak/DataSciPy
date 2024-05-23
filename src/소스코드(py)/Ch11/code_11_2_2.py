#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 11-2 matplotlib 무작정 사용해 보기
#

import matplotlib.pyplot as plt 
 
# 우리나라의 연간 1인당 국민소득을 각각 years, gdp에 저장
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] 
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3] 
 
 
# 제목을 설정한다. 
plt.title("GDP per capita") # 1인당 국민소득
 
# y축에 레이블을 붙인다. 
plt.xlabel("dollars")
plt.ylabel("gdp")

plt.plot(gdp, years, color='red', marker='o', linestyle='solid') 
plt.savefig("gdp_per_capita.png", dpi=600)  # png 이미지로 저장 가능
plt.show()