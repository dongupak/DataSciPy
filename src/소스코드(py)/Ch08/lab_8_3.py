#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 8-3 파티에 동시에 참석한 사람 알아내기
#

partyA = set(["Park", "Kim", "Lee"]) 
partyB = set(["Park", "Choi"]) 
 
print("2개의 파티에 모두 참석한 사람은 다음과 같습니다. ") 
print( partyA.intersection(partyB))