#반지름 r 값 받기
r = input("반지름을 입력하세요 : ")
r = int(r)
#if문에서 비교하기 위해 int()처리

#r값이 0 또는 음수인지 판단
if r > 0 : 
    R = pow(r,2)*3.14

    #원넓이>200일 경우
    if R >200 :
        print("너무 큰 원의 넓이는 구하기가 힘들어요.")
    else: 
        print(R)
        
else:
    print("잘못된 입력값입니다.")

