# prompt the user 
# for the number of guests and 
# number of slices per guest
input_number_of_guests = input('Number of guests: ')
input_number_of_slices = input('Number of slices: ')

# convert the input to integers
number_of_guests = int(input_number_of_guests)
number_of_slices = int(input_number_of_slices)

# calculate the total number of pizzas
total_slices = number_of_guests * number_of_slices
total_number_of_pizzas = total_slices / 8

# round the total number of pizzas
rounded_number_of_pizzas = round(total_number_of_pizzas)

# display the total number of pizzas
print('Total number of pizzas: ', rounded_number_of_pizzas)