# A dictionary is an unordered collection of mutable items
# Dictionaries are written with curly brackets
# Each item in a dictionary has a key and value

person = {
    "name": "Juma",
    "age": 30,
    "city": "Kampala"
}

# Accessing items
person['city']

# Adding items
person['job'] = 'Instructor'

# Removing items
person.pop('city')

# Assignment
# 1. How to find the number of items in a dictionary
# 2. Hoe check if an element exists in a dictionary


# Nested Dictionaries
employees = {
    "Juma": {
        "age": 30,
        "job": "Instructor"
    },
    "Betty": {
        "age": 25,
        "job": "Student"
    }
}

# Accessing items from a nested dictionary
betty_info = employees['Betty']
betty_job = betty_info['job']
# print(betty_job)