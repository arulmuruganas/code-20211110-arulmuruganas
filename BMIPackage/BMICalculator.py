import traceback
from functools import lru_cache


class BMICalculator:
    def __init__(self):
        # Move to yaml config if required
        self.metadata = {
            'CATEGORY_RANGE': [
                {'LOW': 0, 'HIGH': 18.4, 'CATEGORY': 'Underweight', 'HEALTHRISK': 'Malnutrition risk'},
                {'LOW': 18.5, 'HIGH': 24.9, 'CATEGORY': 'Normal weight', 'HEALTHRISK': 'Low risk'},
                {'LOW': 25, 'HIGH': 29.9, 'CATEGORY': 'Overweight', 'HEALTHRISK': 'Enhanced risk'},
                {'LOW': 30, 'HIGH': 34.9, 'CATEGORY': 'Moderately obese', 'HEALTHRISK': 'Medium risk'},
                {'LOW': 35, 'HIGH': 39.9, 'CATEGORY': 'Severly obese', 'HEALTHRISK': 'High risk'}
            ],
            'CATEGORY_MAX': {'LOW': 40, 'CATEGORY': 'Very severly obese', 'HEALTHRISK': 'Very high risk'}
        }

    def __str__(self):
        return 'Package to compute BMI and category'

    def convert_cm_to_m(self, value):
        return value / 100

    def check_zero(self, value):
        return True if value > 0 else False

    @lru_cache(maxsize=128)
    def calculate_bmi(self, weight, height):
        if self.check_zero(weight) and self.check_zero(height):
            try:
                height_in_meter = self.convert_cm_to_m(height)
                bmi = round(weight / (height_in_meter * height_in_meter), 1)
                return {'status': True, 'output': bmi}
            except:
                return {'status': False, 'error': traceback.format_exc()}
        else:
            return {'status': False, 'error': 'zero value is not acceptable'}

    @lru_cache(maxsize=128)
    def get_bmi_category(self, bmivalue):
        for category in self.metadata['CATEGORY_RANGE']:
            if category['LOW'] <= bmivalue <= category['HIGH']:
                return {'CATEGORY': category['CATEGORY'], 'HEALTHRISK': category['HEALTHRISK']}
        return {'CATEGORY': self.metadata['CATEGORY_MAX']['CATEGORY'],
                'HEALTHRISK': self.metadata['CATEGORY_MAX']['HEALTHRISK']}

    def calculate_bmi_bulk(self, data):
        response = []
        for record in data:
            this_response = []
            if 'Weightkg' in record and 'HeightCm' in record:
                bmi_response = self.calculate_bmi(record['Weightkg'], record['HeightCm'])
                if bmi_response['status']:
                    this_response = record
                    this_response['bmi'] = bmi_response['output']
                    this_response |= self.get_bmi_category(this_response['bmi'])
                else:
                    print(bmi_response['error'])
            else:
                print('Either Weightkg or HeightCm or both are missing in', record)
            if this_response:
                response.append(this_response)
        return response

    def get_summary(self, data):
        # use pandas for more detailed and complex summary
        response = {}
        for record in data:
            if record['CATEGORY'] not in response:
                response[record['CATEGORY']] = 0
            response[record['CATEGORY']] += 1
        return response
