#The continue statement is used to skip the rest of the code inside a loop 
#for the current iteration and proceed to the next iteration
    
#It is commonly used to skip certain iterations based on specific conditions


#Example1

for i in range(10):
    if i % 2 == 0: #This is the condition skipped
        continue
    print(i)  #It actually outputs odd nummbers from 1 to 9

#Example2
    
names = ['masaba', 'Lordrick', 'calvn', 'Tom', 'John', 'Richard']

for name in names:
    if name == 'Tom': #Tom is skipped
        continue
    print(name)


#Example3
    
for i in range(10):
    if i % 3 == 0:
        continue
    print(i)
