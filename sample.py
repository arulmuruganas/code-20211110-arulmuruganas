import json
from BMIPackage import BMICalculator

if __name__ == '__main__':
    obj = BMICalculator.BMICalculator()
    # print(obj.calculate_bmi(81, 171))
    data = obj.calculate_bmi_bulk([{'Gender':'Male','HeightCm':123,'Weightkg':56}, {'HeightCm':123,'Weightkg':65},
                                   {'HeightCm':351,'Weightkg':0},
                                   {'Gender':'FeMale','HeightCm':123,'Weightkg':56}
                                   ])
    print(data)
    print(json.dumps(obj.get_summary(data), sort_keys=True, indent=4))