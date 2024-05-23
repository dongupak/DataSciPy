#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 11-7 히스토그램으로 자료의 분포를 한눈에 살펴보자
#

import numpy as np 
import matplotlib.pyplot as plt 
 
n_bins = 10 
x = np.random.randn(1000) 
y = np.random.randn(1000) 
 
plt.hist(x, n_bins, histtype='bar', color='red') 
plt.hist(y, n_bins, histtype='bar', color='blue', alpha=0.3) 
plt.show()