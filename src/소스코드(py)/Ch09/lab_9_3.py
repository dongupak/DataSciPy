#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-3 트위터 메시지 처리
#

s = "It's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAMS IN COVID!!!"

print(f"입력={s}")
count = 0
for word in s.split():
	if( word == word.upper() ): 	# 대문자로 변환한 것과 동일하면 대문자 단어
		count += 1	
print(f"\n대문자 단어의 수={count}")
t = s.lower()
t = t.replace('!',""); 
t = t.replace('.',""); 
t = t.replace("'",""); 
print(f"결과={t}")