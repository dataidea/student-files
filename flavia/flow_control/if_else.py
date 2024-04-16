def bmiCategory(weight_kg, height_m):

    body_mass_index = weight_kg / height_m ** 2

    rounded_bmi = round(body_mass_index, 3)

    return 'Normal' if 20 < rounded_bmi < 24 else 'Not Normal' 

print(bmiCategory(weight_kg=67, height_m=1.7))


# loops: for, while
# break, continue
# pass statement




