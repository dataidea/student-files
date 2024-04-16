# Problem: Pizza Party
# 5. You're organizing a pizza party and want to ensure there's enough pizza for everyone
# attending. Each pizza has 8 slices. Write a Python script that calculates the number
# of pizzas needed based on the number of guests and slices per person.
# Consider the following inputs:
# - Number of guests attending the party.
# - Slices each guest should have (assume each guest will have the same number of slices).
# Your script should:
# - Prompt the user for the number of guests attending.
# - Prompt for the number of slices each guest should have.
# - Calculate the total number of slices needed.
# - Calculate the total number of pizzas required (round up to the nearest whole pizza). For
# instance, if 10 guests are attending and each should have 3 slices, your program
# should output the number of pizzas needed to fulfill the requirement.

import math

number_of_guests = int(input('Enter number of guests: '))
number_of_slices = int(input('Enter number of slices for each guest: '))

total_number_of_slices = number_of_guests * number_of_slices
total_number_of_pizzas = math.ceil(total_number_of_slices / 8)

print(f'Number of guests: {number_of_guests}\n'
      f'Number of slices per guest: {number_of_slices}\n'
      f'Total number of pizzas: {total_number_of_pizzas}')

