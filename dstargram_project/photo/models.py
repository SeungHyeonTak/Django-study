from django.db import models

# Create your models here.
# 기본 모델
"""

작성자 : author
본문 : text
사진 : image
작성일 : created
수정일 : updated
+ tag, like
-- comment
"""
from django.contrib.auth.models import User
from django.urls import reverse
# url pattern 이름을 가지고 주소를 만들어주는 함수

# User모델은 확장 가능
# settings.AUTH_USER_MODEL
# from django.contrib.auth import get_user_model
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')# (연결되는 모델, 삭제시 동작, 연관이름)
    # related_name 으로 연관 데이터를 얻을 수 없다면 쿼리를 별도로 실행해야 한다.
    # 내 프로필 페이지 - 내가 올린 사진만 뜬다.

    # models.Foreignkey(get_user_model(),)
    # CASCADE 연속해서 지운다. 탈퇴하면 사진도 싹 지운다.
    # PROTECT 사진 다 안지우면 너 탈퇴 안됨!! - 탈퇴 프로세스에 사진을 우선 삭제하고 탈퇴 시킨다.
    # 특정값으로 셋팅 -

    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d') # Ymd 경로 자동 생성
    # upload_to는 함수를 사용해서 폴더를 동적으로 설정할 수 있다.
    created = models.DateTimeField(auto_now_add=True) # 시간 생성
    updated = models.DateTimeField(auto_now=True) # 수정일로 할때
    # def __str__(self):
    #     return self.author

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        # detail/<int:pk>/
        return reverse('photo:detail', args=[self.id])

