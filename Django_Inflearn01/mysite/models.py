from django.db import models
from django.utils import timezone
import random
# Create your models here.

class GuessNumbers(models.Model): # Super_class (models) - Sub_class (Model) 상속
    name = models.CharField(max_length = 24)
    lottos = models.CharField(max_length = 255,default = '[1,2,3,4,5,6]')
    text = models.CharField(max_length = 255) # text는 한줄 메모장 처럼 간단하게
    num_lotto = models.IntegerField(default=5) # 게임 수
    update_data = models.DateTimeField()

    # Lotto 번호를 생성 및 데이터 베이스 저장
    def generate(self):
        self.lottos = ""
        origin = list(range(1,46))
        for _ in range(0,self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.update_data = timezone.now()
        self.save()

    def __str__(self):
        return "%s %s" %(self.name, self.text)


