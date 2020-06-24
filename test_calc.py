import unittest
import calc
class TestCalc(unittest.TestCase):
    def test_add(self): #changing the vcariable to add test wont run any test
        result = calc.add(10,5)
        self.assertEqual(result,15)#cahnge value from 15 to 14
