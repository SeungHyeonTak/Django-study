from django.shortcuts import render
from django.http import HttpResponse
# HttpRequest : 요청에 대한 메타정보를 가지고 있는 객체
# HttpResponse : 응답에 대한 메타정보를 가지고 있는 객체

def index(request):
    return HttpResponse("<h1> Hello, World!<h1>")

def post_list(request):
    return HttpResponse("Hi, mark")