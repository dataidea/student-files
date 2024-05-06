guests = int(input('Enter number of guests: '))
slices = int(input('Enter number of slices: '))

import arithmetics as ar

total_slices = arithmetics.multiply(guests, slices)

pizzas_number = arithmetics.divide(total_slices, 8)

print(pizzas_number)

