#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-4 단어 빈도 계산
#

# 딕셔너리를 이용하는 방법
s='the quick brown fox jumps over the lazy dog.'
print(f"입력={s}")

counter = {}
words = s.split()
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
print(f"출력={counter}")