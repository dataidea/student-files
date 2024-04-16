#QUESTION 5

#This function takes two positive integers as input and 
#returns their greatest common divisor

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ensure both numbers are positive
if num1 <= 0 or num2 <= 0:
    print("Both numbers should be positive integers.")
else:
    print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))






#By CALVIN MASABA