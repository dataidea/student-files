my_dict = {'a': 1, 
           'b': 2, 
           'c': 3
           }

# Get the number of items in the dictionary
num_items = len(my_dict)

print("Number of items in the dictionary:", num_items)


# Check if 'b' exists in the dictionary
if 'b' in my_dict:
    print("'b' exists in the dictionary.")
else:
    print("'b' does not exist in the dictionary.")


del my_dict['b'] #deletes an item from a dictionary
print(my_dict)
