#operations on a list

characters = ['A','B','C','D','E']  #LIST OF CHARACTERS

vehicles = list(('V8','TX','RAUM','VITZ')) #creates a list using a constructor

characters.reverse() #creates a reversed list of characters
#print(characters)

vehicles.extend(characters)  #adds many items to the list vehicle from the list characters

vehicles.insert(4, 'masaba') 

del vehicles[2]  #Removes an item from the list vehicle
print(vehicles)


#Check if C exists in the list characters
if 'C' in characters:
    print("C exists in the list.")
else:
    print("C does not exist in the list.")