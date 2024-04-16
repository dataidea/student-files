
#The break statement exits the current loop prematurely 
#regardless of the loop's condition
#It is commonly used when a condition is met and you want to stop the loop execution.

#Example1

for i in range(10):
    if i == 5:
        break
    print(i)


#Example2
    
names = ['masaba', 'Lordrick', 'calvn', 'Tom', 'John', 'Richard']

for name in names:
    if name == 'Tom':
        break
    print(name)


#Example3

i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

