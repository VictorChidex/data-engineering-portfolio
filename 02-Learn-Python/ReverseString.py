# Python code that can reverse any string of text

# Func definition
def reverse_string(text):

    new_string = ""
    index = len(text) - 1
    while index >= 0:

        new_string += text[index]
        index -= 1

    return new_string

# Testing the function
test = "The Lord is good!"
print("original text: ", test)
print("Reverse text: ", reverse_string(test))
