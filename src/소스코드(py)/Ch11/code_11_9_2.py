#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 11-9 한 화면에 여러 그래프 그리기 : subplots()
#

import matplotlib.pyplot as plt 

# 갯수가 2 x 2개, 크기가 (5, 5) 인치 
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.show()