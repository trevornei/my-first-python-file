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
# name = input("What's your name? ")
# print(name)
# name = input("What's your name? ")
# print("hello," + name + "!")
    # This code has a bug because it needs to format the value of the variable inside the string.
    # name = input("What's your name? ")
    # print("Hello, {name} it is nice to meet you :)")
    
    # Corrected bug: print(f"String plus{formattedvariable}")
name = input("What's your name? ")
print(f"Hello, {name} it is nice to meet you :)")

# Functions take arguments
# Paramaters have a lot of similiarities.

# Python docs: docs.python.org
"""
    Print(*objects, sep=' ', end='\n', file=None, flush=False)
    - Takes any number of objects.
    - Both sep and end must be strings.
    - They can also be none value.
    - If no objects are given, print will write none.
"""