#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-7 HTML 태그를 제거하자
#

import re

html = input("HTML 문장을 입력하세요: ")
# HTML 태그를 제거하는 sub()함수와 정규표현식
result = re.sub('<[^>]+>', '', html)
print(result)