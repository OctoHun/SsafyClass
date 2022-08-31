from django.shortcuts import render
import random
# Create your views here.
def index(request):
    # request : 사용자의 요청 정보가 담겨있다.
    # 사용자에게 보여줄 화면 html 파일이름
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['사과', '바나나', '코코넛',]
    info = {
        'name' : '오성훈'
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥',]
    pick = random.choice(foods)
    number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    context = {
        'pick':pick,
        'foods':foods,
        'number':number
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('ball'))

    ball = request.GET.get('ball')
    context = {'ball' : ball}

    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name':name,
    }
    return render(request, 'articles/hello.html', context)