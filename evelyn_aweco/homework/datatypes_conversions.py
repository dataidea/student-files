# A string is a datatype used to represent a sequence of characrters or numbers written within double/ single quotes.
# Strings are immutable meaning they can not be modified once constructed.
# converting a string into an interger
string_No = "123"
interger_No =   int(string_No)
print(interger_No)

# converting a float into an interger
float_No = 123.456
interger_No = int(float_No)
print(interger_No)

# converting a string into an a float
string_No = "123.456"
float_No = float(string_No)
print(float_No)

# converting an interger into a string
interger_No = 123
string_No = str(interger_No)
print(string_No)

# converting a list of strings to a list of intergers.
list_strings = ["10","11","12","13","14","15"]
list_integers = [int(x)for x in list_strings]
print(list_integers)

# converting a list of strings to a list of intergers using the map() function.
list_strings = ["10","11","12","13","14","15"]
list_integers = list(map(int,list_strings))
print(list_integers)

# converting dictionary keys or values to a list.
dictionary = {"a":1,"b": 2,"c": 3,"d": 4,"e": 5,"f":6}
list_keys = list(dictionary.keys())
list_values = list(dictionary.values())
print(list_keys)
print(list_values)