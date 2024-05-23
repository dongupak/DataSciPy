#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 12-9 연도와 월, 일을 다루는 DatetimeIndex와 그룹핑
#

import pandas as pd

# DatetimeIndex를 이용하여 연도를 추출
print(pd.DatetimeIndex(['2010-08-01', '2011-09-21']).year)
# DatetimeIndex를 이용하여 월을 추출
print(pd.DatetimeIndex(['2010-08-01', '2011-09-21']).month)
# DatetimeIndex를 이용하여 일을 추출
print(pd.DatetimeIndex(['2010-08-01', '2011-09-21']).day)