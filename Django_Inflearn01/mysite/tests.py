from django.test import TestCase
from .models import GuessNumbers
# Create your tests here.

# test code 작성
class GuessNumbersTestCase(TestCase): #testcase를 상속 받아온다.
    def test_generate(self):
        g = GuessNumbers(name = 'mark', text = '당첨?')
        g.generate()
        print(g.update_data) # 현재시간으로 업뎃
        print(g.lottos) # Lotto의 내용
        self.assertTrue(len(g.lottos) > 20) # 글자수가 20글자수보다 크면 통과한다.
        # 성공인지 실패인지 확인할때 assertTrue로 확인