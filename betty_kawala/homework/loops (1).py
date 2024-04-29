# Nested for loop
# A nested for loop is used to repeat a certain block of code multiple times.
# The outer loop controls the number of times the inner loop runs
for number1 in range(1,3):
    for number2 in range(1,3):
        print( str(number1) + "x" + str(number2) + "=" + str(number1 * number2))

# While loop
# A while loop repeats a block of code until a certain condition is met
number = 0
while number < 6 :
    print(number) 
    number += 1       

# Break and continue statement 
# Break statement.
# The break statement is used to terminate a loop once a specified condition is met.
# for example
fruits =["apple","banana","cherry","date","mangoe","orange"]
for fruit in fruits:
    if fruit=="date":
        break
    print(fruit)

# Continue statement
#The continue statement is used to skip the current iteration of the loop and move to the next one
# for example
numbers = [1,2,3,4,5,6,7,8,9] 
for number in numbers:
    if number % 2 == 0:
        continue  
    print(number)


# The pass statement
# This is a null statement. It does nothing when executed.
#It is useful when you need to create a placeholder for code that will be implemented later
# for example
def my_fuction():
    pass    