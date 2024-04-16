# to obtain body mass index

# def calculateBMI(weight_kg, height_m):

#     body_mass_index = weight_kg / height_m ** 2

#     rounded_bmi = round(body_mass_index, 3)

#     return rounded_bmi

# sample_bmi = calculateBMI(weight_kg=67, height_m=1.7)

# print(sample_bmi)

bmiCalculator = lambda weight, height: round(weight / height ** 2, 3)

print(bmiCalculator(67, 1.7))



