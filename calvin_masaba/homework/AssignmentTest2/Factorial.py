#QUESTION 4

# This function takes an integer as input and
#  returns its factorial

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))


#This function first checks if the input number is negative, 
# in which case it returns a message stating that 
# the factorial is not defined for negative numbers. 

#Then, it handles the cases where the input number is 0 or 1, 
#returning 1 since the factorial of 0 and 1 is defined as 1. 

#Finally, for other positive integers, it calculates the factorial by: 
#multiplying all the numbers from 1 to n inclusive.


#By CALVIN MASABA
