class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name + ' walks ...'
    
class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return self.name + ' barks ...'


dog1 = Dog(name='brian', color='white')

dog1.speak()