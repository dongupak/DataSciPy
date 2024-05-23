#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 11-2 삼각함수의 기본인 사인 그래프 그리기
#

import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0, 360)
y = np.sin(np.radians(x))

plt.plot(x, y) 
plt.title("SINE WAVE") 
plt.show()