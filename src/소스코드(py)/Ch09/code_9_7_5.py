#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 9.7 정규식을 이용하여 특정한 패턴 찾기
#

import re
def is_valid_jumin(st):
    pattern = '^\d{6}\-\d{7}'     # 출생년도-7자리 숫자로 주민등록번호를 검사하는 정규식
    match = re.match(pattern, st)
    return match

jumin = input('당신의 주민등록번호는: ') # 주민등록번호를 입력받는 코드
if is_valid_jumin(jumin):
    print('주민등록번호가 유효합니다.')
else:
    print('주민등록번호가 유효하지 않습니다.')