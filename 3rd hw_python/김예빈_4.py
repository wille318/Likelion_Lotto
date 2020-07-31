# 숫자 3개 입력
num1 = input("첫 번째 수를 입력하세요 : ")
num2 = input("두 번째 수를 입력하세요 : ")
num3 = input("세 번째 수를 입력하세요 : ")

a = [num1, num2, num3]

#가장 작은 수 출력
#a리스트의 첫 요소 a[0]를 smallist에 저장. for문으로 반복하며 가장 작은 수를 i에 저장해나가는 방식
smallist = a[0]
for i in a :
    if i <smallist :
        smallist = i
print("가장 작은 수는", smallist, "입니다.")

