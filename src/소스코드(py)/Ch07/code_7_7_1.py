#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 7.7 바퀴의 재발명?, 200쪽
#

heights = [178, 173, 166, 164, 176]

smallest = heights[0]       # 리스트의 첫번째 원소를 smallest라고 두고
for item in heights:
    if item < smallest:     # item이 smallest보다 더 작으면 이 값이 최소값이다
        smallest = item     # 최소값을 갱신한다

print('리스트 원소들 :', heights)
print('이 중에서 가장 작은 값은 :', smallest)