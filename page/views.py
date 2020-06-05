from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def result(request):
    #사용자 입력값 받기
    ulist = []
    for a in range(6):
        num1 = request.GET['number' + str(a+1)]
        num1 = int(num1)
        ulist.append(num1)

    #랜덤으로 6개
    import random
    rlist = []
    for b in range(6):
        num2 = random.randrange(1,46)
        rlist.append(num2)

    #일치 개수
    count = 0
    for a in range(6):
        for b in range(6):
            if(ulist[a] == rlist[b]) :
                count += 1
    
    return render(request, 'result.html', {'number_list': ulist, 'random_list':rlist, 'count' : count}) 