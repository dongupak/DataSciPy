#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# 8.3 딕셔너리의 다양한 메소드
#

phone_book ={'홍길동':'010-1234-5678','강감찬':'010-1234-5679','이순신':'010-1234-5680'} 
phone_num = phone_book.popitem()    # '홍길동'을 키로하는 값이 반환되며 이 항목이 삭제됨 
print('phone_book =', phone_book)
print('phone_num =', phone_num)