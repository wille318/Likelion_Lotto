num = [ ]

# 정수 받는 반복문(단, 0일 때 종료)
while True :
    a = int(input("숫자를 입력해주세요 : "))
    if a == 0 :
        break
#짝수일 경우 num안에 넣고, 아니면 넘어감
    if a%2==0 : 
        num.append(a)
    # else :
    #     pass

print("짝수의 개수는 : ", len(num) ,"개")
