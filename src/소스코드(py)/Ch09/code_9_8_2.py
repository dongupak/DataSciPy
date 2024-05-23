#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.8 정규식을 이용하여 패턴 대체하기
#

import re
text = 'My email is john@example.com'
result = re.sub('\w+@\w+\.\w+', '****', text)
print(result)  # 'My email is ****'