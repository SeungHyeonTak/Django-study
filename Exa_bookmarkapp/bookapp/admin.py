from django.contrib import admin
from bookapp.models import Bookapp
# Register your models here.

# 5
# 관리자 페이지 로그인하고 나서의 페이지를 관리한다.
# 관리자 사이트에서 Bookapp 클래스가 어떤 모습으로 출력될지 정의하는 코드
class BookappAdmin(admin.ModelAdmin):
    # 관리자화면에 출력할 필드 목록( 튜플 형식 )
    list_display = ("title", 'url')

admin.site.register(Bookapp, BookappAdmin)

# python manage.py makemigrations
# python manage.py migrate
# 실행 ㄱㄱ
# DB에서 data 확인 후 url.py로