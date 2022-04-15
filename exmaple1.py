#!/usr/bin/env python3.9

# comment BMI = (weight in KG / height in meters squared)
# comment Imperial system ( BMI * 703)

def gather_info():
    height = float(input("what is your height? "))
    weight = float (input("what is your weight? "))
    system = input("what units is: ").lower().strip()
    return(height, weight, system)


def calculate_bmi(weight,height, system='metric'):
    """
    Return the body mass index
    """

    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 / (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f'your bmi is starts with i {bmi}')
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(f'yout is start with m {bmi}')
        break
    else:
        print('errorcito')
        
