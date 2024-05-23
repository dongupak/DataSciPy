#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-2 불용어 제거하기
#

stop_words = ['is', 'and', 'the', 'a', 'an', 'in', 'of', 'to']

text = "This is an example of removing stop words from a string."
words = text.split()
filtered_sentence = [word for word in words if word.lower() not in stop_words]
print(f"입력={text}")
print(f'출력={" ".join(filtered_sentence)}')