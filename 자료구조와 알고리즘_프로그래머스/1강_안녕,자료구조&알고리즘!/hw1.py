"""
1. 프로그래머스 테스트에 익숙해지기
입력으로 주어지는 리스트 x의 첫 원소와 마지막 원소의 합을 리턴하는 함수 solution()을 완성하세요. 
"""

for i in range(5): 
    x = []
    a = int(input('입력하세요 : '))
    x.appends(a)
    i +=1
    
def solution(x) : 
    print(x[0] + x[-1])

