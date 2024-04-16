class Animal:
    def __init__(self, name, sound):
        self.name = name 
        self.sound = sound

    def speak(self):
        print(self.name + ' is ' + self.sound + 'ing')
        # return

    def __str__(self):
        return 'Name:' + self.name + ', Sound: ' + self.sound 

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def walk(self):
        print( self.name + ' is ' + 'walking...')
        # return
    

class Snake(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def crawl(self):
        print(self.name + ' is ' + 'crawling..')

snake1 = Snake(name='Sensei', sound='Hiss')

print(snake1.speak())
    