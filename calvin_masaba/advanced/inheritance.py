class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name + ' is walking'

    def speak(self, sound):
        return self.name + ' is ' + sound + 'ing'

# animal1 = Animal(name='symore')

# print(animal1.name)
# print(animal1.walk())
    
class Dog(Animal):
    def __init__(self, name, lifespan, color):
        super().__init__(name)
        self.lifespan = lifespan
        self.color = color


dog1 = Dog(name='brian', lifespan=8, color='white')

print(dog1.name)
print(dog1.speak(sound='bark'))
print(dog1.lifespan)
print(dog1.walk())