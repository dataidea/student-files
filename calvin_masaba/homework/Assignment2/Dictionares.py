#Dictionaries

My_dict = {
    "Surname": "MASABA", 
    "Given_Name": "CALVIN",
    "Gender" : "MALE", 
    "Age":"28", 
    "student" : {"Course": "BITC", 
                 "Student_ID": "234CXR"}
    
}

print(My_dict) # prints out the dictionary elements including sub-dictionaries

print(My_dict['Surname']) #prints the Surname item in the dictionary

print(len(My_dict))

print("student" in My_dict) #checks if an item exists in a dictionary

del My_dict['Gender'] #removes an item from a dictionary

print(My_dict)