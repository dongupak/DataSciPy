#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 8-4 파일에서 사용된 단어 구하기
#

def process(w):    # 단어에서 구두점을 제거하고 소문자로 만든다. 
    output ="" 
    for ch in w: 
        if ch.isalpha() : # ch 문자가 알파벳인 경우에 
            output += ch  # ch 문자를 output 다음에 연결함
    return output.lower() # output 문자열을 소문자로 바꿈 

words = set()      # 중복을 방지하기 위해 집합 자료형에 단어를 넣자
fname = input("입력 파일 이름: ") 
file = open(fname, "r")   # 파일을 연다
# 파일의 모든 줄에 대하여 반복한다. 
for line in file: 
    lineWords = line.split() 
    for word in lineWords: 
        words.add(process(word))   # 단어를 집합에 추가한다. 
 
print("사용된 단어의 개수 =", len(words)) 
print(words)