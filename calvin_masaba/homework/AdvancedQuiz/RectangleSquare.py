#QUESTION 6 & QUESTION 7

#Python class named `Rectangle` with attributes `length` and `width`, 
#and a method `area()` that returns the area of the rectangle

x = int(input('Enter length: '))
y = int(input('Enter width: '))
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Square(Rectangle):
    def perimeter(self):
        if self.length == self.width:
            return self.length + self.width
        else:
            print('Not square because sides are not equal')


Rectangle1 = Rectangle(length = x, width = y)
print('Area of Rectangle is: ', Rectangle1.area())

Square1 = Square(length = x, width = y)
print('Perimeter of square is: ', Square1.perimeter())