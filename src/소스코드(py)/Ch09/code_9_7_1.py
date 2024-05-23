#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.7 정규식을 알아보자
#

import re           # 이 코드 이후의 모든 정규식 코드 예제에서는 import re 문을 사용합니다
text = "이번 학기 개설 과목은 CS101입니다."
match = re.search('[A-Za-z]{2}\d{3}', text)
if match:
    print("과목 코드가 발견됨:", match)
else:
    print("과목 코드가 발견되지 않음:", match)