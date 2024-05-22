#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 3-1 화씨온도를 섭씨온도로 변환하기, 79쪽
#

# int
fahrenheit = int(input("화씨온도: "))
celsius = (fahrenheit - 32) * 5 / 9
print("섭씨온도:", celsius)

#float
fahrenheit = float(input("화씨온도: "))
celsius = (fahrenheit - 32.0) * 5.0 / 9.0
print("섭씨온도:", celsius)