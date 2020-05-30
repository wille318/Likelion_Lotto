from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def result(request):
    return render(request, 'result.html') 

    #home.html의 번호 6개 받기 {{number}
    number = request.GET["number1", "number2","number3","number4","number5","number6"]

    #로또 랜덤으로 6개 만들기 {{random}}