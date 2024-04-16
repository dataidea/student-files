# A set is an unordered collection of unique items.

# creating a set
countries = {'uganda', 'rwanda', 'kenya'}
# print(type(countries))

# a set can contain different data types
countries = {'uganda', 45_000_000, True}

# accessing items in a set
# for country in countries:
#     print(country)

# adding items to a set
countries.add('tanzania')

# Items in a set cannot be changed once they are added.

# removing items from a set
countries.remove('uganda')
countries.discard(True)

# Combine 2 sets
countries = {'uganda', 'rwanda', 'kenya'}
other_countries = {'tanzania', 'zambia'}

countries.update(other_countries)

# another way create a set
countries = set(('uganda', 'rwanda', 'kenya'))

print(countries)

# a set cannot contain duplicate items
pets = {'dog', 'cat', 'dog', 'fish', 'horse'}
print(pets)




# Assignements
# 1. How to drop elements using pop()
# 2. How to find the number of elements in a set
# 3. How to check if an element exists in a set
# 4. Find the difference between 2 sets

