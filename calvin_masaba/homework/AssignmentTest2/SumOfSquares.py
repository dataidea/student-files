#QUESTION 9

def sumOfSquares(n):
    if n <= 0:
        return "Input should be a positive integer."
    
    sum_squares = 0
    for number in range(1, n + 1):
        sum_squares += number **2
        #print(number)
    return sum_squares

n = int(input("Enter a positive integer: "))
print("Sum of squares up to", n, "is:", sumOfSquares(n))


#This function iterates from 1 to n, 
#calculating the square of each number and 
#adding it to the sum_squares variable. 
#Finally, it returns the total sum of squares





#By CALVIN MASABA