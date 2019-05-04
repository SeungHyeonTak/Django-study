from django.test import TestCase
from .models import GuessNumbers
# Create your tests here.

# test code 작성
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name = 'apple', text = 'pineappne')
        g.generate()
        print(g.update_data)
        print(g.lottos)
        self.assertTrue(len(g.lottos) > 20)