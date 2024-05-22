#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 5.6 무한 루프와 break로 빠져나가기
# 루프를 제어하는 고급 기법 : continue와 break, 145쪽
#

st = 'I love Python Programming'  # 출력을 위한 문자열
for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        continue                  # 모음일 경우 아래 출력을 건너뛴다
    print(ch, end='')