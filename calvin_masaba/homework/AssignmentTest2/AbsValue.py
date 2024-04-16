#QUESTION 6

#returns the absolute value of a number without using the built-in abs() function

number = int(input('Enter the number: '))

def absoluteValue(number):
    if number >= 0:
        return number
    else:
        return -number

print("Number:", number)

print("Absolute Value:", absoluteValue(number))










#By Calvin Masaba