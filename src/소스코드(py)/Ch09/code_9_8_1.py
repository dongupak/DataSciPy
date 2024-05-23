#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.8 정규식을 이용하여 패턴 대체하기
#

import re
text = 'abc123def456'
result = re.sub('\d', '', text) # text 문자열에서 숫자를 모두 제거함
print(result)                   # 'abcdef'