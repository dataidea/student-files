# Identity operators are used to check if two values (or variables) 
# are located on the same part of the memory or point to the same 
# object.

# Here's a list of the identity operators:

# Operator              Name
# is                    Returns True if both variables are the same object
# is not                Returns True if both variables are not the same object

numbers1 = [1, 2, 3]
numbers2 = [1, 2, 3]
numbers3 = numbers1

print(numbers1 is not numbers3)
