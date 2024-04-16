def calculateAge(year_of_birth):
    try:
        current_year = 2024
        age = current_year - year_of_birth
        if age < 0:
            raise ValueError ('Invalid year of birth')
        return age
    except ValueError as e:
        print('Error:', e)


year_of_birth = int(input('Enter year of birth: '))

age = calculateAge(year_of_birth)
if age is not None:
    print('You are', age, 'years old')
