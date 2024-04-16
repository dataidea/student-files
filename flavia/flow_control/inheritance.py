class Animal:
    def __init__(self, name, blood_color):
        self.name = name
        self.blood_color = blood_color

    def walk(self):
        print(self.name + ' walking...')

class Dog(Animal):
    def __init__(self, name, blood_color, age):
        super().__init__(name, blood_color)
        self.age = age

    def sound(self):
        print(self.name + ' barks...')

dog1 = Dog(name='brian', age=8, blood_color='red')

# Research
# format strings
# try ... except
# iterators
# user input
