#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-5 영화평 분석
#

from textblob import TextBlob
review = "This movie was terrible! The acting was poor and the story was boring."
sentiment = TextBlob(review).sentiment.polarity
print(f"입력={review}\n")
    
if sentiment > 0:
	print("결과=긍정적")
elif sentiment == 0:
	print("결과=중립")
else:
	print("결과=부정적")