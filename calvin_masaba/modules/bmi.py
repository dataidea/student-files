def overWeightOrUnderWeight(weight_kg, height_m):
    bmi = weight_kg / pow(height_m, 2)

    if bmi >= 24:
        return 'Overweight'
    elif bmi >= 18:
        return 'Normal'
    else:
        return 'Underweight'


# status = overWeightOrUnderWeight(67, 1.7)


# calculateBMI = lambda weight_kg, height_m: 'Normal' if 18 >= (weight_kg / height_m ** 2) <= 24 else 'Not Normal'

# bmi = calculateBMI(67, 1.7)

# print(bmi)

# age = input('Enter your age: ')

# state = 'Adult' if int(age) >= 18 else 'Child'

# print(state)