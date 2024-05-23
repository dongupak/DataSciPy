#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 11-8 데이터를 효율적으로 표현하는 상자 차트를 알아보자
#

import numpy as np
import matplotlib.pyplot as plt
data1 = [1, 2, 3, 4, 5]
data2 = [2, 3, 4, 5, 6]

plt.boxplot([ data1, data2 ] )

plt.show()