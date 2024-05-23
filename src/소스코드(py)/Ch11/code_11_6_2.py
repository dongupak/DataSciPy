#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 11-6 데이터를 점으로 표현하는 산포도 그래프 그리기
#

import matplotlib.pyplot as plt 
times = [8, 14, 2]
timelabels = ["Sleep", "Study", "Play"]

# autopct로 백분율을 표시할 때 소수점 2번째 자리까지 표시하게 한다.
# labels 매개 변수에 timelabels 리스트를 전달한다.
plt.pie(times, labels = timelabels, autopct = "%.2f") 
plt.show()