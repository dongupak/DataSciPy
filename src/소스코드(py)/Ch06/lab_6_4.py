#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 6-4 리스트에서 최대/최소값을 찾는 함수, 170쪽
#

def getMinMax(mylist, method):
   min_Value = mylist[0]     # 리스트의 첫 번째 값을 min_value로 두자
   max_Value = mylist[0]     # 리스트의 첫 번째 값을 max_value로 두자

   if method == 'max' :
       for value in mylist:
           if value > max_Value:
               max_Value = value
       return max_Value
   elif method == 'min' :
       for value in mylist:
           if value < min_Value:
               min_Value = value
       return min_Value
   else :
       return 'Error : 잘못된 명령입니다.'

list_data = [82, 27, 90, 30, 87, 56] # 데이터를 여러 개 담는 리스트 자료구조
print(list_data)
s = input('최대값을 원하면 max, 최소값을 원하면 min을 입력하시오: ')
print(getMinMax(mylist = list_data, method = s))