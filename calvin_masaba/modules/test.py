from classes import Person as psn
from calculator import Arithmetic as ar
import bmi

class WeightedPerson(psn):
    def __init__(self, first_name, last_name, age, weight, height):
        super().__init__(first_name, last_name, age)
        self.weight = weight
        self.height = height

# create person objects
person1 = WeightedPerson(first_name='Juma', last_name='Shafara', 
                         age=35, weight=67, height=1.7)
person2 = WeightedPerson(first_name='Eva', last_name='Ssozi', 
                         age=30, weight=62, height=1.5)

# create the arithmetic object
arithmetic = ar()

# get the age_difference
age_difference = arithmetic.subtract(number1=person1.age, number2=person2.age)


person1_bmi_status = bmi.overWeightOrUnderWeight(weight_kg=person1.weight,
                                                 height_m=person1.height)
person2_bmi_status = bmi.overWeightOrUnderWeight(weight_kg=person2.weight,
                                                 height_m=person2.height)

print(f'Person1 BMI Status: {person1_bmi_status} \n'
      f'Person2 BMI Status: {person2_bmi_status}')

print('Age Difference: ', age_difference)
