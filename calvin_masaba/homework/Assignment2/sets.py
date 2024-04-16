#sets

birds = {'Hen', 'Doves', 'Fouls', 'Turkey', 34, True} 

#print(type(birds))

names = {'calvin', 'masaba','charles', 'Kuloba'}
for name in names: #Accesses all items in the set one at a time
    print(name)

numbers = set((1, 2, 3, 4, 5))

#print(type(numbers))

#Adding many items to the list

names.update(numbers)  #adds items of set Even_numbers to set names at once
#print(names)


birds.remove('Fouls') #removes an item foul from the set birds
birds.pop() #removes an item randomly from the set
print(birds)

numbers_list = list(numbers) #converts set to list
del numbers_list[2]   #removes an item from the list
print(numbers_list)


print('Derick' in names)  #checks if Derick exists in set names

print(len(names))

reversed_set = list(numbers)[::-1]  #converts the set into a list
print(reversed_set) #retrieves items from the end backwards
#for i in reversed_set:
#    print(i)

