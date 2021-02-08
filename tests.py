import unittest
from task1_calculator import Calculator
from task2_peter import meditate


class CalculatorTest(unittest.TestCase):
    def test_calculate(self):
        expressions = {
            '(5 + 8) * 3/8 +3': 7.875,
            '3+2*2': 7,
            ' 3/2 ': 1.5,
            '': 0
        }
        for expression, answer in expressions.items():
            calculator = Calculator(expression)
            self.assertEqual(calculator.calculate(), answer)


class PeterMeditationTest(unittest.TestCase):
    def test_meditation(self):
        numbers = {
            23245: 22999,
            11235888: 11235888,
            111110: 99999,
            33245: 29999
        }
        for number, answer in numbers.items():
            self.assertEqual(meditate(number), answer)


if __name__ == '__main__':
    unittest.main()
