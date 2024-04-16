#QUESTION 10

#Takes two numbers as input and returns the
#result of dividing the first number by the second. 
#Handle the ZeroDivisionError using a try-except block.

number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))

def divideNumbers():
    return number1/number2
try:
    print(divideNumbers())

except:
    print('Error occurred while dividing numbers')

else:
    print('Operation Successful')

finally:
    print('Execution completed!')

