from django.shortcuts import render, redirect
from django.http import HttpResponse
# HttpRequest : 요청에 대한 메타정보를 가지고 있는 객체
# HttpResponse : 응답에 대한 메타정보를 가지고 있는 객체
from .models import GuessNumbers
from .forms import PostForm
def index(request):
    lottos = GuessNumbers.objects.all()

    #return HttpResponse("<h1> Hello, World!<h1>")
    return render(request, "mysite/default.html", {"lottos":lottos})

def post(request):
    if request.method == "POST":
        # save data
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'mysite/form.html',{"form":form})

def detail(request, mysitekey):
    lotto = GuessNumbers.objects.get(pk = mysitekey)
    return render(request, "mysite/detail.html", {'lotto':lotto})
