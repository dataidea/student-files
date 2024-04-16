# defining a function
def areaOfTriangle(base, height):
    area = 0.5 * base * height
    return area

# Calling a function
tri_area1 = areaOfTriangle(7, 14)
tri_area2 = areaOfTriangle(3, 14)

# print(tri_area1)
# print(tri_area2)

def greet(respect):
    print('Hello ' + respect)

# greet('Doctor')
    
def add(number1, number2):
    return number1 + number2

def calculateBMI(weight_kg, height_m):
    bmi = weight_kg / height_m ** 2
    rounded_bmi = round(bmi, 3)
    return bmi, rounded_bmi
 
value1, value2 = calculateBMI(67, 1.7)


def subtract(num1, num2):
    subtract = num1 - num2
    return subtract

print(subtract(10, 7))


# lambda functions





