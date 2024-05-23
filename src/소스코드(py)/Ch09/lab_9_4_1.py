#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-4 단어 빈도 계산
#

# Counter 클래스를 이용하는 방법
from collections import Counter
 
s='the quick brown fox jumps over the lazy dog.'
print(f"입력={s}")
words = s.split()
 
frequency = Counter(words)
print(f"출력={frequency}")