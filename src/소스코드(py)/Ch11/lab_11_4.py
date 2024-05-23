#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 11-4 차종별 판매량을 파이 차트로 표현하자
#

import matplotlib.pyplot as plt 


volume = [15.7, 19.8, 11.2, 24.0]
name_labels = ['Sedan', 'RV', 'Premium Car', 'Etc']

plt.pie(volume, labels = name_labels, autopct = "%.1f")
plt.show()