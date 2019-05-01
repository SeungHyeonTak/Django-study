from django.shortcuts import render,render_to_response
from bookapp.models import Bookapp
# Create your views here.

#7
# http:localhost 로 요청할 때 실행할 함수(기본 페이지)
def Home(request):
    # select * from bookapp_bookapp order by title ; //쿼리가 실행됨 SQL에서 확인해보기
    urlList = Bookapp.objects.order_by("title")

    # select count(*) from bookapp_bookapp ; // 쿼리가 실행됨 마찬가지로 확인해보기
    urlCount = Bookapp.objects.all().count()
    # list.html 페이지로 넘어가서 출력됨

    return render_to_response("list.html", {"urlList":urlList, "urlCount":urlCount})
    # render_to_reponse("url", {"변수명" : 값})

# templates 디렉토리 만들고 html만들기

#10
def detail(request):
    # get방식 변수 받아오기 request.GET["변수명"]
    # POST방식 변수 받아오기 request.POST["변수명"]
    addr = request.GET["url"]
    # select * from bookapp_bookapp where url=... 실행됨
    dto = Bookapp.objects.get(url=addr)
    #detail.html로 포워딩
    return render_to_response("detail.html", {"dto":dto})