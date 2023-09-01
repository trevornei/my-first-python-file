print("Hello, world!!!")

# My first single line comment.
"""
Here is a multiline comment.
    - My first typo in python was when printing "Hello World!!!" I ran into a syntax error because I used single 'quotes'.
"""

# # Creating my first function.
# print("What's your name? ")
# # Input takes an argument itself. 
# input()

# I have commented the above code out because input takes an argument and creates a new line.
# Refactored code below
# input("What is your name? ")
# print("Hello, Trevor!")

"""
    Adding Return Values: 
    Let's make the code more contextual. 
        - If the input has a different name than Trevor, we need to be able to respond appropriately.
        How do we do so?
            - Variables
            -- Assignment operator assigns left to right. 
            --- name will store the value of the input().
"""
# Returns users name.
name = input("What's your name? ")
print(name)

