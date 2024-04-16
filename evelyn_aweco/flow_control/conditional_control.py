def calculateBMI(weight_kg, height_m):
    bmi = weight_kg / height_m ** 2

    if bmi >= 24:
        print('Overweight')
    elif bmi >= 18:
        print('Normal')
    else:
        print('Underweight')

    return bmi

print(calculateBMI(67, 1.5))