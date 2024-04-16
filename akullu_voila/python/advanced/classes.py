class Person:
    def __init__(self, name, height, feet):
        self.name = name
        self.height = height
        self.feet = feet

    def jump(self):
        return "I'm jumping " + str(self.feet) + " Feet"
    
if __name__ == '__main__':
    person2 = Person(name='Shafara', height=5.7, feet=3)
    print(type(person2))

