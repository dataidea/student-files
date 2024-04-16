import math
# Rounding up
def round_up(number):
    return math.ceil(number)

# Example 
number = 3.14
rounded_up = round_up(number)
print(rounded_up)  # Output: 4

#Rounding down
def round_down(number):
    return math.floor(number)

#Example
number = 3.14
rounded_down = round_down(number)
print(rounded_down)  # Output: 3

# More examples
x = 7.34
print(round_up(x)) # Output:8

y = 34.78
print(round_down(y)) # Output:34