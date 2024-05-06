# function to return the absolute value of a number
def absoluteValue(number):
    if number < 0:
        return -number
    else:
        return number

# function to return the square of a number
def square(number):
    return number * number

# function to return the cube of a number
def cube(number):
    return number * number * number

# function to return the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)