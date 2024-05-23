#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.7 정규식을 이용하여 특정한 패턴 찾기
#

# 문자열에서 전화번호를 찾는 예제
import re
string = "My phone number is 010-1234-5678. Call me anytime."
result = re.search('\d{3}-\d{4}-\d{4}', string)
print(result.group())    # 010-1234-5678