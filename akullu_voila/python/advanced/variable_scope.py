# local scope
# a variable that is created/defined 
# inside a function has a local scope

# create a fucntion that greats people

# - All variable declared outside a function global

name = 'Voila'

def my_func():
    global my_fruit
    my_fruit = 'banana'
    # print(name + ' loves my ' + my_fruit)

my_func()

print(my_fruit)




