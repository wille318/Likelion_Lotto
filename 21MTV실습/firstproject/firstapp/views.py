from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
    # 함수이름은 welcome. 다른 파일에서 welcome을 외치면, render함수를 타고 welcome.html을 실행시킴

def hello(request) : 
    userName = request.GET['name']
    return render(request, 'hello.html', {'userName' : userName})