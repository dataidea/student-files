name = 'Viola'
fruit = 'banana'
expression = 'so much'

# # positional formating
# statement = '{} loves my {}'.format(name, fruit)

# # indexing
# statement = '{0} loves my {1}'.format(name, fruit)

# # named indexes
# statement = '{name} loves my {fruit}'.format(name=name, fruit=fruit)

# Formatted string literal
# statement = f'{name} loves {expression} my {fruit}'

# more examples
# number1 = 6
# number2 = 9

# statement = f'The sum of {number1} and {number2} is {number1 + number2}'

# def addNumbers(number1, number2):
#     return number1 + number2

# statement = f'The sum is {addNumbers(6, 9)}'
age = 19
statement = f'You are {"allowed" if age > 18 else "not allowed"}'

print(statement)