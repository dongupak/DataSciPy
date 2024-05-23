#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 7.7 바퀴의 재발명?, 200쪽
#

heights = [178, 173, 166, 164, 176]

largest = heights[0]        # 리스트의 첫번째 원소를 largest라고 두고
for item in heights:
    if item > largest:      # item이 largest보다 더 크면 이 값이 최대값이다
        largest = item      # 최대값을 갱신한다

print('리스트 원소들 :', heights)
print('이 중에서 가장 큰 값은 :', largest)