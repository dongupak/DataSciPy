#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 8-1 편의점 재고 관리 프로그램을 만들자
#
stores = { "커피음료": 7, "펜": 3, "종이컵": 2, "우유": 8, "콜라": 4, "책": 5 } 
 
name = input("물건의 이름을 입력하시오: ") 
print('재고 :', stores[name])