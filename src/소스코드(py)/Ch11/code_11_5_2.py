#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 11-5 막대형 차트도 손쉽게 그려보자
#

import matplotlib.pyplot as plt

# 1인당 국민소득
years = [1965, 1975, 1985, 1995, 2005, 2015]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [890, 5120, 11500, 42130, 40560, 38780]
ch = [100, 200, 290, 540, 1760, 7940]

x_range = range(len(years))
plt.bar(x_range, ko, width = 0.25)
plt.bar(x_range, jp, width = 0.25)
plt.bar(x_range, ch, width = 0.25)
plt.show()