#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.4 불용어를 쉽게 처리하자
#

import nltk   # pip install nltk 명령으로  nltk 모듈 설치 후 사용가능

from nltk.corpus import stopwords  # 불용어 패키지를 사용하기 위해 가져온다
nltk.download('stopwords')         # nltk 패키지로부터 불용어를 다운받는다
nltk.download('punkt')             # nltk 패키지로부터 토큰화 작업을 위하여 punkt를 다운받는다
text = "This is an example of removing stop words from a string."
stop_words = set(stopwords.words("english"))
words = nltk.word_tokenize(text)

filtered_sentence = [w for w in words if not w in stop_words]
print(f"입력={text}")
print(f'출력={" ".join(filtered_sentence)}')