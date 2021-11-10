import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from BMIPackage import BMICalculator


class MyTestCase(unittest.TestCase):
    def test_bmi_calculation(self):
        self.bmiobj = BMICalculator.BMICalculator()
        output = self.bmiobj.calculate_bmi(70, 170)
        self.assertEqual(output['output'], 24.2)

    def test_bmi_category(self):
        self.bmiobj = BMICalculator.BMICalculator()
        output = self.bmiobj.get_bmi_category(26)
        self.assertEqual(output['CATEGORY'], 'Overweight')

    def test_check_zero(self):
        self.bmiobj = BMICalculator.BMICalculator()
        output = self.bmiobj.check_zero(0)
        self.assertEqual(output, False)


if __name__ == '__main__':
    unittest.main()
