from django.test import TestCase

from app.calc import add

class CalcTest(TestCase):
    def test_numbers(self):
        """test that numbers are added together"""
        """you have to begin any fun you want to test with test word"""
        self.assertEqual(add(3,8),11)
    
    def test_substract_numbers(self):
        """test that values are substracted and returned"""
        
        self.assertEqual(substract(5,11),6)