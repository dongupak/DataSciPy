#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 6.3 함수에 일을 시키고 그 값을 받아오도록 하자
# 함수에 여러 개의 값을 넘겨주는 고급 기능, 161쪽
#

def get_sum(start, end):            # start, end를 매개변수로하여 인자를 받는다
    s = 0
    for i in range(start, end+1):   # start부터 end까지 정수의 합을 구함
        s += i
    return s                        # start부터 end까지 수의 합을 반환한다

y = get_sum(1,20)                   # 1과 20이 인자가 된다. y는 1에서 20까지의 합을 반환받는다.
print('1에서 20까지의 합 :', y)        