# open(file=, mode=)

# Mode              Meaning
# "r"             Open a file for reading
# "w"            Open a file for writing, creates a file if it doesnt exist
# "a"            Open a file for writing, appends to the end of the file
# "x"            Open a file to create, fails if the file already exist

# Examples
# Writing
# file = open(file='demo.txt', mode='w')
# file.write('I love to code in JavaScript')
# file.close()

# Appending
# file = open(file='./file_handling/demo.txt', mode='a')
# file.write('\n I also love to code in Rust')
# file.close()

# Exclusive Creation
# file = open(file='./file_handling/notes.txt', mode='x')

# Reading
# To read everything in the file
# file = open('./file_handling/demo.txt', 'r')
# content = file.read()

# To read specific lines
# file = open('./file_handling/demo.txt', 'r')
# line1 = file.readline()
# line2 = file.readline()

# import os

# os.remove(path='./file_handling/notes.txt')

# Check if a file exists
# if os.path.exists(path='./file_handling/demo.txt'):
#     print('File exists')
# else:
#     print('File doesnot exist')
