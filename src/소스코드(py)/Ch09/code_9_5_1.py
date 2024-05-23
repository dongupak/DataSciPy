#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.5 워드 클라우드
#

from wordcloud import WordCloud
wordcloud = WordCloud()
text = "Hello Hello Hello This is a word cloud example."
wordcloud.generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()