#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.5 워드 클라우드
#

from wordcloud import WordCloud
import matplotlib.pyplot as plt
# 텍스트 파일 읽기
with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.read()
# 워드 클라우드 생성
wordcloud = WordCloud(font_path='malgun.ttf', 	# 폰트
                      background_color='white', 	# 배경색
                      width=800, 		       # 폭
                      height=800, 		       # 높이
                      max_words=100, 		# 최대 단어 개수
                      max_font_size=200, 	       # 최대 폰트 크기
                      contour_width=1, 		# 윤곽선 두께
                      contour_color='steelblue',	# 윤곽선 색상
                      collocations=False).generate(text)
# 워드 클라우드 그리기
plt.figure(figsize=(8,8))			# 이미지 크기
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()