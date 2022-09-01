from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    # 요청에 대한 모든 데이터는 request
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장
    # 데이터 저장 방법 3가지
    # 1. 
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    
    # 2.
    article = Article(title=title, content=content)
    article.save()
    
    # 3.
    # Article.objects.create(title=title, content=content)
    # 저장 전에 검증 시간이 필요하기에 3번보다는 2번이 좋음

    # return render(request, 'articles/index.html', context)
    return redirect('articles:detail', article.pk) # '/articles/' 도 가능

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)