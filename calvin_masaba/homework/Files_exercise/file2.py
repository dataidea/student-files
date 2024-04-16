# Create a new file and write some content to it
file = open(file = "example23.txt", mode = "w")
file.write("This is the initial content.\n")
file.close()

# Read the content of the file
file = open(file = "example23.txt", mode = "r")
content = file.read()
print("Initial content:")
print(content)
file.close()

# Append more content to the file
file = open(file = "example23.txt", mode = "a")
file.write("This is the appended content.\n")
file.close()

# Read the content of the file again to see the changes
file = open(file = "example23.txt", mode = "r")
content = file.read()
print("Updated content:")
print(content)
file.close()

# Delete the file
import os
os.remove("example23.txt")
print("File deleted.")