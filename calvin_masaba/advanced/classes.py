class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Student:
    def __init__(self, id_number, name, age):
        self.id_number = id_number,
        self.name = name
        self.age = age

    def greet(self, person_name, greetings):
        print(f'{greetings} {person_name}')

    def __str__(self):
        info = f' Name: {self.name} \n ID Number: {self.id_number} \n Age: {self.age}'
        return info 




