
#lambda function are functions that have no name
#They are called aninymous functions

#Exampe 1

Subtract = lambda num1, num2 : num2 - num1

print('The difference is =', Subtract(12, 8))

#EXAMPLE 2

areaOfTriangle = lambda base, height : 0.5 * base * height

AREA = areaOfTriangle(5, 8)

print('The area of the triangle is: ', AREA)


#EXAMPLE 3
Body_Mass_Index = lambda weight_kg, height_m : weight_kg / (height_m**2)

BMI = Body_Mass_Index(58, 2.1)
Rounded_BMI = round(BMI, 3)
print('The Body mass index is: ', BMI)
print('The Body mass index rounded to 3dps is: ', Rounded_BMI)

if BMI > 12:
    print('STATUS: Overweight')
elif BMI < 8:
    print('STATUS: Underweight')
else:
    print('STATUS: Normal weight')    