class Arithmetic:
    def add(self, number1, number2):
        return number1 + number2
    
    def subtract(self, number1, number2):
        return number1 - number2
    
    def multiply(self, number1, number2):
        return number1 * number2
    
    def divide(self, number1, number2):
        return round(number1 / number2, 3)
    
class MathFunctions(Arithmetic):
    def square(self, number):
        return number ** 2
    
    def cube(self, number):
        return number ** 3
    

# Test out
math_functions = MathFunctions()

x = 7
y = 3

# print(math_functions.square(number=x))
# print(math_functions.cube(number=x))

product = math_functions.multiply(number1=x, number2=y)
print(product)













# operator = Arithmetic(number1=7, number2=3)

# summation = operator.add()
# difference = operator.subtract()
# product = operator.multiply()
# quotient = operator.divide()

# print(f'Given two numbers 7 and 3: \n'
#       f'Summation: {summation} \n'
#       f'Difference: {difference} \n'
#       f'Product: {product} \n'
#       f'Quotient: {quotient}')
