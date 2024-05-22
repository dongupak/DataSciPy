#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 5.5 일정한 횟수 반복에 while 사용하기, 138쪽
#

count = 1
s = 0           # s는 누적하여 더한 값을 담을 변수로 0으로 초기화 함
while count <= 10:
    s = s + count       # 매번 count 값을 s에 더함
    count = count + 1   # 매번 count 값을 1씩 증가시킴
print("합계는", s)