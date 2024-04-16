#QUESTION 1

#  This function takes an integer as input and 
# returns "Even" if the number is even, and "Odd" if the number is odd.

number = int(input('Enter the integer: '))

def evenOrOdd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
status = evenOrOdd(number)
print('This integer is : ', status)










#By Calvin Masaba