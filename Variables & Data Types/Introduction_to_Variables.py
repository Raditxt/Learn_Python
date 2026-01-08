# Introduction_to_Variables.py
"""
This script explains Python variables in a simple way
that can be understood even by a 5-year-old child (using the Feynman Technique).

Feynman Technique: Explaining complex concepts with simple language, analogies,
and concrete examples.
"""

print("=" * 60)
print("LEARNING VARIABLES IN PYTHON")
print("(Like Explaining to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: WHAT IS A VARIABLE?
# ============================================================================
print("1. WHAT IS A VARIABLE?")
print("-" * 40)

print("""Imagine a variable as a LABEL or NICKNAME
for something we store in computer memory.""")

print("\nThe analogy:")
print("""• You have a red toy car
• You name it 'MyRedCar'
• Every time you say 'MyRedCar', you mean that red car
• Variable = nickname for a value/data""")

# ============================================================================
# SECTION 2: HOW TO CREATE A VARIABLE
# ============================================================================
print("\n\n2. HOW TO CREATE A VARIABLE")
print("-" * 40)

print("""Creating a variable is EASY! Just:
VARIABLE_NAME = VALUE

The equal sign (=) means 'store the value on the right
into the name on the left'.""")

# Simple examples
print("\nSimple examples:")
name = "John"      # Store text "John" in variable 'name'
age = 8            # Store number 8 in variable 'age'
height = 120.5     # Store decimal number 120.5 in variable 'height'

print(f"Variable 'name' contains: {name}")
print(f"Variable 'age' contains: {age}")
print(f"Variable 'height' contains: {height}")

print("\nSee how to use them:")
print(f"Hello, my name is {name}")
print(f"I am {age} years old")
print(f"My height is {height} cm")

# ============================================================================
# SECTION 3: VARIOUS TYPES OF DATA THAT CAN BE STORED
# ============================================================================
print("\n\n3. VARIOUS TYPES OF DATA THAT CAN BE STORED")
print("-" * 40)

print("""Variables can store various types of data,
like a cabinet with many drawers for different items.""")

# Examples of various data types
print("\nExamples of various data types:")

# 1. String (text)
animal_name = "Cat"  # Use quotes for text
print(f"1. String: '{animal_name}' (for text)")

# 2. Integer (whole number)
number_of_legs = 4
print(f"2. Integer: {number_of_legs} (for whole numbers)")

# 3. Float (decimal number)
weight = 3.5
print(f"3. Float: {weight} (for decimal numbers)")

# 4. Boolean (True/False)
cute = True
print(f"4. Boolean: {cute} (for true/false)")

# 5. List (list)
food = ["fish", "cat food", "milk"]
print(f"5. List: {food} (for lists/collections)")

# 6. Dictionary (dictionary)
animal_info = {"breed": "persian", "color": "white", "age": 2}
print(f"6. Dictionary: {animal_info} (for key-value pairs)")

print("\nThe analogies:")
print("""• String = Sentence/word
• Integer = Whole number (1, 2, 3)
• Float = Number with decimal (1.5, 2.75)
• Boolean = Yes/No, True/False
• List = Shopping list
• Dictionary = Language dictionary""")

# ============================================================================
# SECTION 4: WITHOUT QUOTES = DIFFERENT MEANING!
# ============================================================================
print("\n\n4. WITHOUT QUOTES = DIFFERENT MEANING!")
print("-" * 40)

print("""ATTENTION! Python distinguishes between:
• Variable name (without quotes)
• String value (with quotes)""")

# Demonstration of difference
print("\nExample of difference:")
number = 10     # Store number 10
text = "10"     # Store text "10" (not a number!)

print(f"number = {number}  → type: {type(number)}")
print(f"text = '{text}'  → type: {type(text)}")

print("\nCan they be added?")
print(f"number + 5 = {number + 5}")  # 10 + 5 = 15
# print(f"text + 5 = {text + 5}")  # This will ERROR! Can't add text and number

print(f"text + '5' = '{text + '5'}'")  # Can! Concatenate two texts: "10" + "5" = "105"

print("\nLesson:")
print("• 10 (without quotes) = number → can be calculated")
print("• '10' (with quotes) = text → cannot be calculated")
print("• Python DISTINGUISHES between numbers and text that look the same!")

# ============================================================================
# SECTION 5: VARIABLES CAN CHANGE!
# ============================================================================
print("\n\n5. VARIABLES CAN CHANGE VALUE AND TYPE")
print("-" * 40)

print("""Variables in Python are FLEXIBLE!
Can change value, even change data type.""")

# Example of value change
print("\nExample: Variable 'quantity' changes")
quantity = 5
print(f"Initial: quantity = {quantity} (type: {type(quantity)})")

quantity = 8  # Change value
print(f"After changed: quantity = {quantity} (type: {type(quantity)})")

quantity = "many"  # Change to text!
print(f"Now: quantity = '{quantity}' (type: {type(quantity)})")

print("\nThe analogy:")
print("""• Variable is like a label/sticker
• Can stick to anything
• Can move from car to doll to book
• The label stays the same, but what it points to can be different""")

# ============================================================================
# SECTION 6: VARIABLE NAMING RULES
# ============================================================================
print("\n\n6. RULES FOR GOOD VARIABLE NAMES")
print("-" * 40)

print("""Variable names should be clear and follow rules.
It's like naming a pet - must be appropriate!""")

print("\nEXAMPLES OF GOOD NAMES:")
full_name = "John Smith"   # Clear, uses underscore
age_years = 8              # Descriptive
total_cost = 15000         # Easy to understand

print("\nEXAMPLES OF BAD NAMES:")
x = "John"    # What does it mean? Not clear!
y = 8         # Not descriptive
h = 120.5     # Unclear abbreviation

print("\nNAMING RULES:")
print("1. Can use letters (a-z, A-Z)")
print("2. Can use numbers (0-9), but not at the beginning")
print("3. Can use underscore (_)")
print("4. CANNOT use spaces")
print("5. CANNOT use symbols (@, $, %, etc.)")
print("6. Python is CASE SENSITIVE")

print("\nExamples legal vs illegal:")
print("Legal: name, name1, full_name, FullName")
print("Illegal: 1name, full-name, full@name")

# ============================================================================
# SECTION 7: VARIABLES CAN "POINT" TO OTHER VARIABLES
# ============================================================================
print("\n\n7. VARIABLES CAN BE CONNECTED TO EACH OTHER")
print("-" * 40)

print("""Variables can 'point' to other variables.
It's like giving two names to the same toy.""")

# Example of connected variables
print("\nExample: Two names for the same toy")
favorite_toy = "Remote Car"
john_toy = favorite_toy  # john_toy is now also "Remote Car"

print(f"favorite_toy = '{favorite_toy}'")
print(f"john_toy = '{john_toy}'")

print("\nNow change favorite_toy...")
favorite_toy = "Transformer Robot"
print(f"favorite_toy = '{favorite_toy}'")
print(f"john_toy = '{john_toy}'")

print("\nNotice:")
print("• john_toy DOES NOT change!")
print("• When we do 'john_toy = favorite_toy'")
print("• It's like copying the value at that moment, not forever connected")

# ============================================================================
# SECTION 8: MATHEMATICAL OPERATIONS WITH VARIABLES
# ============================================================================
print("\n\n8. CALCULATING WITH VARIABLES")
print("-" * 40)

print("""We can calculate using variables,
like using pocket money to buy candy.""")

# Example of mathematical operations
print("\nExample: Buy candy with pocket money")
pocket_money = 10000   # John's pocket money
candy_price = 2000     # Price of one candy

# How many candies can be bought?
number_of_candies = pocket_money // candy_price  # // = integer division
remaining_money = pocket_money % candy_price     # % = modulo (remainder)

print(f"Pocket money: ${pocket_money}")
print(f"Candy price: ${candy_price}")
print(f"John can buy {number_of_candies} candies")
print(f"Remaining money: ${remaining_money}")

print("\nBasic mathematical operations:")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")   # Addition
print(f"a - b = {a - b}")   # Subtraction
print(f"a * b = {a * b}")   # Multiplication
print(f"a / b = {a / b}")   # Division (decimal result)
print(f"a // b = {a // b}") # Integer division
print(f"a % b = {a % b}")   # Modulo (remainder)
print(f"a ** b = {a ** b}") # Power (10 to the power of 3)

# ============================================================================
# SECTION 9: type() FUNCTION - CHECKING DATA TYPE
# ============================================================================
print("\n\n9. CHECKING DATA TYPE WITH type()")
print("-" * 40)

print("""We can ask Python: "What type is this variable?"
with the type() function.""")

# Demonstration of type()
print("\nLet's check data types:")

example_string = "Hello"
example_integer = 42
example_float = 3.14
example_boolean = True
example_list = [1, 2, 3]
example_dict = {"name": "John"}

print(f"'{example_string}' is: {type(example_string)}")
print(f"{example_integer} is: {type(example_integer)}")
print(f"{example_float} is: {type(example_float)}")
print(f"{example_boolean} is: {type(example_boolean)}")
print(f"{example_list} is: {type(example_list)}")
print(f"{example_dict} is: {type(example_dict)}")

print("\nWhy is it important to know data types?")
print("""• So we know what operations can be performed
• Example: numbers can be added, text cannot
• Avoid errors when running the program""")

# ============================================================================
# SECTION 10: REAL CASE - SIMPLE PROGRAM
# ============================================================================
print("\n\n10. SIMPLE PROGRAM EXAMPLE")
print("-" * 40)

print("""Let's create a simple program using variables.
Program: Calculate the area of a rectangle.""")

# Program to calculate rectangle area
print("\nPROGRAM: CALCULATE RECTANGLE AREA")

# Rectangle data
length = 10  # in cm
width = 5    # in cm

# Calculate area
area = length * width

# Display result
print(f"Length: {length} cm")
print(f"Width: {width} cm")
print(f"Area = Length × Width")
print(f"Area = {length} × {width}")
print(f"Area = {area} cm²")

print("\nAdvantages of using variables:")
print("1. Easy to read (clearer than numbers directly)")
print("2. Easy to change (just change variable value)")
print("3. Can be used repeatedly")

# ============================================================================
# CONCLUSION
# ============================================================================
print("\n\n" + "=" * 60)
print("CONCLUSION ABOUT VARIABLES")
print("=" * 60)

print("""
1. Variable = NICKNAME for value/data
2. How to create: variable_name = value
3. The = sign means 'store value into name'
4. Can store various data types:
   • String (text with quotes)
   • Integer (whole number)
   • Float (decimal number)
   • Boolean (True/False)
   • List (list)
   • Dictionary (dictionary)
5. Python DISTINGUISHES between numbers and text that look the same
6. Variables can change value and type
7. Give clear and descriptive variable names
8. Can calculate with variables
9. Use type() to check data type
10. Variables make programs more flexible and easier to read

Remember: Variables are like LABELS on storage boxes.
The contents can be changed, but the label stays!
""")

print("=" * 60)
print("CONGRATULATIONS! NOW YOU UNDERSTAND VARIABLES IN PYTHON!")
print("=" * 60)

# ============================================================================
# EXERCISES FOR THE READER
# ============================================================================
print("\n\nEXERCISES FOR YOU:")
print("-" * 40)

print("""1. Try creating variables for:
   • Your full name
   • Your age
   • Your height
   • Hobbies (in a list)
   
2. Calculate:
   • How old are you in months?
   • If height increases by 10%, what's the new height?
   
3. Change data types:
   • Create variable number = 10
   • Change to text '10'
   • Try adding 5 (what happens?)""")

print("\nHow to run exercises:")
print("1. Open Python interpreter (type 'python' in terminal)")
print("2. Try each example above one by one")
print("3. Don't be afraid to make mistakes - errors are part of learning!")

print("\n" + "=" * 60)
print("SAVE AS: Variables_in_Python.py")
print("RUN WITH: python Variables_in_Python.py")
print("=" * 60)