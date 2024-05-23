#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.6 한글 워드클라우드와 이미지 형태로 만들기
#

from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt # matplotlib은 추후에 설명합니다.
# 워드 클라우드를 그릴 텍스트 데이터
text = '''Love is a river that flows so free,
A beautiful sight for all to see.
It glides around every bend,
A source of life that never ends.'''
mask = np.array(Image.open("comment.png")) # 사용할 이미지 파일
# 워드 클라우드 생성을 위한 다양한 키워드 인자들 설정
wc = WordCloud(background_color="white", mask=mask,
               contour_width=3, contour_color='steelblue')
wc.generate(text)         # 텍스트를 이용해 워드 클라우드 생성
wc.to_file("result.png")  # 워드 클라우드 이미지 저장
# 워드 클라우드 이미지 출력
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")     # matplotlib에서 축 설명을 생략함-추후 설명 예정
plt.show()