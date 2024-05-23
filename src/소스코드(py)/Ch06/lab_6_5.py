#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 6-5 리스트에서 최대/최소값을 찾아서 두 개를 반환하는 함수, 171쪽
#

def getMinAndMax(mylist):
    min_value = mylist[0]           # 리스트의 첫 번째 값을 min_value로 두자
    max_value = mylist[0]           # 리스트의 첫 번째 값을 max_value로 두자

    for value in mylist:
        if value > max_value: 
            max_value = value 
        if value < min_value: 
            min_value = value
    return max_value, min_value     # 두 개의 값을 반환함

list_data = [82, 27, 90, 30, 87, 56]    # 데이터를 여러 개 담는 리스트 자료구조
# getMinAndMax() 함수가 두 개의 값을 반환하므로 두 개의 변수에 이를 담는다
max_v, min_v = getMinAndMax(list_data)

print('리스트의 원소 :') 
print(list_data) 
print('최대값 :', max_v) 
print('최소값 :', min_v)