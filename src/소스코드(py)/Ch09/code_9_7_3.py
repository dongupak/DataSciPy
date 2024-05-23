#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.7 정규식을 이용하여 특정한 패턴 찾기
#

import re
text = 'There are 12 apples and 3 oranges'
numbers = re.findall('\d+', text)
print(numbers)