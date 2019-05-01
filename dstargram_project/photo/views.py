from django.shortcuts import render

# Create your views here.
# CRUDL - 이미지를 띄우는 방법
# 제네릭 뷰
# 쿼리셋 변경하기, context_data 추가하기, 권한체크
# 함수형 <-> 클래스형 뷰

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Photo

class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

from django.shortcuts import redirect
class PhotoCreate(CreateView):
    model = Photo
    fields = ['author', 'image', 'text']
    template_name = 'photo/photo_create.html'
    #success_url = '/'

    def form_valid(self, form):
        # 입력된 자료가 올바른지 체크
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            # form : 모델 폼
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form':form})

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/photo_update.html'
    #success_url = '/'

class PhotoDelete(DeleteView):
    model = Photo
    #fields = ['image', 'text']
    template_name = 'photo/photo_delete.html'
    #success_url = '/'

class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'