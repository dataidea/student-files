# A dictionary is an unordered and mutable collection of items

country_data = {
    'name': ['brazil', 'uganda', 'croatia'],
    'gdp': [3456, 6743, 4586],
    'population': [120, 45, 8]
}

# Accessing dictionary element
name = country_data['name']
gdp = country_data['gdp']
ppn = country_data['population']

per_capita_incomes = []

for i in range(len(ppn)):
    per_capita_incomes.append(round(gdp[i] / ppn[i], 3))

# print(per_capita_incomes)


# Add elements to the dictionary
country_data['per_capita_incom'] = per_capita_incomes

# Changing values in a dictionary
country_data['name'] = ['croatia', 'tunisia', 'china']

# Nested dictionaries
employees = {
    'manager': {
        'name': 'Juma Shafara',
        'email': 'jumashafara@dataidea.org'
    },
    'programmer': {
        'name': 'Evelyn Aweco',
        'email': 'evelynaweco@dataidea.org'
    }
}

# Accessing elements from a nested dictionary
print(employees['programmer']['email'])

