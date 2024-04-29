calculateBMI = lambda weight, height: weight / height ** 2

bmi = calculateBMI(65, 1.8)

print('You are normal') if 18 > bmi > 24 else print('You are not normal')

