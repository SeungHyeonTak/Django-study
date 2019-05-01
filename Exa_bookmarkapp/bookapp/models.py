from django.db import models

# Create your models here.

# 테이블을 하나의 클래스로 정의하고
# 테이블의 컬럼은 클래스의 변수로 매핑
# 테이블 클래스는 django.db.models.Model 클래스를 상속받아 정의 변수 자료형도 장고에서 미리 정의된 자료형을 사용한다.
# models.URLField('필드의 별칭', unique)
# __str__() : 객체를 문자열로 표현하는 Method

# 4
class Bookapp(models.Model): # django의 Model 클래스 상속
    # 필드 선언
    # blank 반값 허용 여부 ,null null 허용여부
    title = models.CharField(max_length=100, blank=True, null=True)
    # CharField - string(문자열) , blank - True (빈값이 들어가도 된다), null - True (null 값이 들어가도 된다)
    url = models.URLField('url', unique=True)
    # url - unique -true (url은 중복되면 안된다.)
    # unique: primary key

    def __str__(self): # 객체를 문자열로 바꿔줌
        return self.title
    # 다음은 admin.py 로 간다.