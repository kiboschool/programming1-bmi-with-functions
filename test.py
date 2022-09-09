import unittest
from main import calculate_bmi

class TestBMI(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertEqual(calculate_bmi(60, 2), 15.0)
        self.assertEqual(calculate_bmi(80, 2), 20.0)
        self.assertEqual(calculate_bmi(56, 1.6), 21.9)
        self.assertEqual(calculate_bmi(61.2, 1.5), 27.2)
        self.assertEqual(calculate_bmi(50, 1.4), 25.5)
        self.assertEqual(calculate_bmi(120, 1.8), 37.0)

if __name__ == "__main__":
    unittest.main()
