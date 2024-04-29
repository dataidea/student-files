## Python Classes and Objects

# Everything in Python is an object.

# A list of countries is an object.
countries = ["India", "USA", "UK"]

# Because ...
len(countries) # number of elements (attribute)

other_countries = ["Canada", "Australia"]
countries.extend(other_countries) # add elements (behavior)

# A class helps us to create objects.

## Creating a class
# We use the class keyword to create a class.

class Person:
    first_name = "Betty"
    last_name = "Kawala"
    age = 30

## Instantiating a class
# Now we can ceate an object from the class by instantiating it.
# To instantiate a class, add round brackets to the class name.

person_obj1 = Person()

type(person_obj1)

# After instiating a class, we can access its attributes.
# print(person_obj1.first_name)
# print(person_obj1.last_name)
# print(person_obj1.age)

# We can also create multiple objects from a class.
person_obj2 = Person()

# After instiating a class, we can access its attributes.
# print(person_obj2.first_name)
# print(person_obj2.last_name)
# print(person_obj2.age)


## Class Attributes
# a class can have multiple attributes.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# create an object from the class
person_obj3 = Person(first_name="Betty", last_name="Kawala", age=30)

# print out the person_obj3 attributes
# print(person_obj3.first_name)
# print(person_obj3.last_name)
# print(person_obj3.age)

# # But now if we create a new object
# person_obj4 = Person(first_name='Juma', last_name='Shafara', age=36)

# # print out the person_obj4 attributes
# print(person_obj4.first_name)   
# print(person_obj4.last_name)
# print(person_obj4.age)


## Methods
# Methods are functions that belong to a class.
# These methods should be defined inside a class.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet(self, name):
        print(self.first_name + " Says hello to " + name)


person_obj5 = Person(first_name="Betty", last_name="Kawala", age=30)

person_obj5.greet(name='Shafara')

# As you may notice we used the self parameter to access the attributes of the class.

