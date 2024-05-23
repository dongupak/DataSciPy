#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-1 글자 수, 단어 수, 평균 단어 길이
#

s="This movie was terrible! The acting was poor and the story was boring."

print(f"s={s}")
print(f"\n글자수={len(s)}")
words = s.split()
print(f"단어들의 리스트={words}")
print(f"단어 수={len(words)}")
print(f"평균 단어 길이={sum(len(word) for word in words)/len(words)}")