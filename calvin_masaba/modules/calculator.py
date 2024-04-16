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