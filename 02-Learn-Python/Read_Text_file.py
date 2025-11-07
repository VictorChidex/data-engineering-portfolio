# You're given a string. Your task: First write the input string to a file 
# 'example.txt'. Read the same file and return string. 

# Function to write and read an input text file
def read_file(text):

  with open('example.txt', mode = 'w') as file:
    write_file = file.write(text)

  with open('example.txt', mode = 'r') as file:
    read_file = file.read()
    return read_file


# script to test you code

text = "I am blessed, so blessed"
read_file(text)

