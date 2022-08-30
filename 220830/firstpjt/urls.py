"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # include가 url 나누기의 기능


urlpatterns = [
    path('admin/', admin.site.urls),
    # 화면 추가 path('경로', 해당 경로를 처리해 줄 view.py의 함수 이름)
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
