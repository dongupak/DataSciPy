#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 11-8 데이터를 효율적으로 표현하는 상자 차트를 알아보자
#

import numpy as np
import matplotlib.pyplot as plt

random_data = np.random.randn(100)
plt.boxplot(random_data)
plt.show()