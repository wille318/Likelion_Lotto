#숫자 받기
a = input("아무 숫자나 넣어주세요")
#숫자 한번 더 확인
print("num은 ", a)

#숫자를 문자열로 변환 (자리 수 세야하니까)
b = str(a)

print("num은 ",len(b),"자리 수 입니다.")

##[  해설  ]##################
num = 3489
count = 0

while num>1:
    num /= 10 # num= num/10 이라는 뜻(반복을 피하기 위함)
    count += 1

print(count)