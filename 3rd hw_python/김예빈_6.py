# input을 int로 감싸서 한 줄에 짧게 쓸 수 있음. 
a = int(input("정수를 입력하세요 :"))
sum = 0

# 0에서 a까지 3의 배수를 찾음
for i in range(0, a+1) :    #(0,a)로 잡으면 a는 포함안됨
    if i%3 == 0 :   # 3으로 나눴을때 0이면(3의 배수)
        sum += i    # +=은 sum에 i를 더하고 저장
    else :
        pass
#print(sum)

#0512수정
print("0부터"+ str(a) +"까지의 3의 배수의 합은" + str(sum) + "입니다")
