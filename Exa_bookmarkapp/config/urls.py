"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from bookapp import views
# 6
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.Home),
    # r 정규표현식, ^ 시작, $ 끝

    # 9
    #http://localhost/detail로 요청하면 views 모듈의 detail 함수 실행
    url(r'^detail$', views.detail),
]

# 클라이언트에서 요청할 수 있는 url 정의
# url("url pattern", 실행 할 코드)