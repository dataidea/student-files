# Conditional statements are used to execute a block of code 
# only if a certain condition is met. 

# The if statement

# y = 10
# x = 5

# if x > y:
#     print("x is less than y")

# age = 18

# if age >= 18:
#     print('Display pictures!')
# else:
#     print('No pictures!')

# x = 10

# if x > 10:
#     print('x is greater than 10')
# elif x < 10:
#     print('x is less than 10')
# else:
#     print('x is should be 10')

# score = 70

# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# elif score >= 50:
#     print('E')
# else:
#     print('F')
# print('Enter "y" for yes and "n" for no')
# is_adult = input('Are you 18+ ?')

# if is_adult == 'y':
#     print('Enter "m" for men and "w" for women')
#     preference = input('Are you interested in men or women?')
#     if preference == 'm':
#         print('Display male stuff')
#     elif preference == 'w':
#         print('Display female stuff')
#     else:
#         print('Display all stuff')
# else:
#     print('redirect to youtube for kids')


if age >= 18:
    print('Display some naked pictures')
else:
    print('redirect to youtube for kids')


print('Display some naked picture') if age >= 18 else print('redirect to youtube for kids')