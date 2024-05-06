# function to add 2 numbers
def add(number1, number2):
    return number1 + number2

# function to subtract 2 numbers
def subtract(number1, number2):
    return number1 - number2

# function to multiply 2 numbers
def multiply(number1, number2):
    return number1 * number2

# function to divide 2 numbers
def divide(number1, number2):
    return number1 / number2


class Arithmetic:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def add(self):
        return self.number1 + self.number2
    
    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2