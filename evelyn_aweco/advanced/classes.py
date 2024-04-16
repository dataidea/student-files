# class Person:
#     first_name = 'Juma'
#     last_name = 'Shafara'
#     age = 19

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def greet(self):
#         return 'Hello there'
    
#     def kick(self):
#         return 'Kick!!!!'


# person1 = Person('Juma', 'Shafara', 19)

# print(person1.kick())

# person1
# print('Person1:')
# print('First Name: ', person1.first_name)
# print('Last Name: ', person1.last_name)
# print('Age: ', person1.age)

# print(type(person1))


class Arithmetic():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        summation = self.number1 + self.number2
        return summation
    
    def subtract(self):
        difference = self.number1 - self.number2
        return difference
    
    def multiply(self):
        product = self.number1 * self.number2
        return product
    
    def divide(self):
        quotient = self.number1 / self.number2
        return quotient
    

ar_object = Arithmetic(number1=7, number2=3)

summ = ar_object.add()
diff = ar_object.subtract()
pdt = ar_object.multiply()
qnt = ar_object.divide()

print(summ)
print(diff)
print(pdt)
print(qnt)
    