#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.6 한글 워드클라우드와 이미지 형태로 만들기
#

from wordcloud import WordCloud

wordcloud = WordCloud(font_path = 'malgun.ttf') # 한글 폰트를 지정

text = '''한글 클라우드를 만들기 위해서는
텍스트 데이터가 필요합니다. 텍스트 데이터는 txt, csv, 엑셀 파일
등 다양한 형식으로 제공될 수 있습니다.
이 예제에서는 txt 파일을 불러오겠습니다.'''
wordcloud.generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()