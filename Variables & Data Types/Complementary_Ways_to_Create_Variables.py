"""
This script explains complementary ways to create variables in Python
in a simple way that can be understood even by a 5-year-old (using Feynman Technique).

Feynman Technique: Explain complex concepts with simple language,
analogies, and concrete examples.
"""

print("=" * 60)
print("COMPLEMENTARY WAYS TO CREATE VARIABLES IN PYTHON")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: INTRODUCTION - BEYOND BASIC ASSIGNMENT
# ============================================================================
print("1. BEYOND THE BASICS: MORE WAYS TO CREATE VARIABLES")
print("-" * 40)

print("""So far we've learned: variable = value
But Python has MORE tricks for creating variables!
Today we learn 3 special ways:""")

print("\n1. Parallel Assignment (same value to many variables)")
print("2. Iterable Unpacking (unpacking values from lists/tuples)")
print("3. Assignment Expressions (walrus operator)")

print("\nThink of it like this:")
print("• Regular assignment: One name tag for one toy")
print("• Parallel assignment: Same name tag for many toys")
print("• Unpacking: Opening a gift box with many toys inside")
print("• Walrus operator: Naming something while using it")

# ============================================================================
# SECTION 2: PARALLEL ASSIGNMENT - ONE VALUE TO MANY
# ============================================================================
print("\n\n2. PARALLEL ASSIGNMENT: SAME VALUE TO MANY VARIABLES")
print("-" * 40)

print("""Parallel assignment is like giving the SAME name
to multiple toys at the same time!""")

print("\nBasic syntax:")
print("variable1 = variable2 = variable3 = value")

# Demonstration
print("\nDemonstration: Turning off all switches")

# Traditional way (repetitive)
print("\nTraditional way (repetitive):")
light1 = False
light2 = False
light3 = False
print(f"light1 = {light1}")
print(f"light2 = {light2}")
print(f"light3 = {light3}")

# Parallel assignment (cleaner)
print("\nParallel assignment (cleaner):")
lamp = fan = ac = False  # All set to False at once!
print(f"lamp = {lamp}")
print(f"fan = {fan}")
print(f"ac = {ac}")

# More examples
print("\nMore examples:")

# Initialize multiple counters
print("Initialize multiple counters to 0:")
count_a = count_b = count_c = 0
print(f"count_a = {count_a}, count_b = {count_b}, count_c = {count_c}")

# Set default values
print("\nSet default settings:")
volume = brightness = contrast = 50
print(f"volume = {volume}, brightness = {brightness}, contrast = {contrast}")

# String values
print("\nInitialize multiple strings:")
first = middle = last = "Unknown"
print(f"first = '{first}', middle = '{middle}', last = '{last}'")

print("\nImportant note:")
print("""ALL variables point to the SAME object!
If you change one, others DON'T change (for immutable types).
But for mutable types (like lists), be careful!""")

# Demonstrate with immutable vs mutable
print("\nDemonstration with immutable (int) vs mutable (list):")

# Immutable example
print("\n1. Immutable (integers):")
x = y = z = 10
print(f"Initially: x={x}, y={y}, z={z}")
x = 20  # Change only x
print(f"After x=20: x={x}, y={y}, z={z} (y and z unchanged)")

# Mutable example (careful!)
print("\n2. Mutable (lists) - Be careful!:")
list1 = list2 = list3 = []  # All point to SAME list!
print(f"Initially: list1={list1}, list2={list2}, list3={list3}")
list1.append(100)  # Modify through one variable
print(f"After list1.append(100):")
print(f"list1={list1}, list2={list2}, list3={list3} (ALL changed!)")

print("\nSolution for mutable objects:")
print("Use separate assignments: list1 = []; list2 = []; list3 = []")

# ============================================================================
# SECTION 3: ITERABLE UNPACKING - OPENING A GIFT BOX
# ============================================================================
print("\n\n3. ITERABLE UNPACKING: OPENING A GIFT BOX")
print("-" * 40)

print("""Iterable unpacking is like opening a gift box
and taking out each toy one by one!""")

print("\nBasic syntax:")
print("var1, var2, var3 = [value1, value2, value3]")
print("or")
print("var1, var2, var3 = (value1, value2, value3)")

# Simple unpacking demonstration
print("\nSimple unpacking demonstration:")

# Create a tuple (like a gift box)
print("1. Create a tuple (gift box with 3 items):")
gift_box = ("teddy bear", "car", "ball")
print(f"gift_box = {gift_box}")

# Unpack the tuple
print("\n2. Unpack the tuple (open the box):")
toy1, toy2, toy3 = gift_box
print(f"toy1, toy2, toy3 = gift_box")
print(f"toy1 = '{toy1}'")
print(f"toy2 = '{toy2}'")
print(f"toy3 = '{toy3}'")

# Unpacking from list
print("\n3. Unpacking from list (same idea):")
colors = ["red", "green", "blue"]
color1, color2, color3 = colors
print(f"colors = {colors}")
print(f"color1, color2, color3 = colors")
print(f"color1='{color1}', color2='{color2}', color3='{color3}'")

# Compare with manual indexing
print("\nComparison: Unpacking vs Manual indexing")

# Manual way (clumsy)
print("\nManual way (clumsy):")
person = ("Alice", 25, "Engineer")
name = person[0]
age = person[1]
job = person[2]
print(f"name = '{name}', age = {age}, job = '{job}'")

# Unpacking way (clean)
print("\nUnpacking way (clean):")
name, age, job = person  # Same as above but cleaner!
print(f"name = '{name}', age = {age}, job = '{job}'")

# ============================================================================
# SECTION 4: UNPACKING TRICKS - STAR OPERATOR (*)
# ============================================================================
print("\n\n4. UNPACKING TRICKS: USING STAR (*) OPERATOR")
print("-" * 40)

print("""Sometimes we have more values than variables.
The star (*) operator helps us collect 'extra' values!""")

# Basic star operator
print("\n1. Collecting extra values:")

# Without star operator (this would error if we tried with too many values)
print("\nWithout star (must match exactly):")
numbers = [1, 2, 3]
a, b, c = numbers  # Must have exactly 3 variables for 3 values
print(f"numbers = {numbers}")
print(f"a={a}, b={b}, c={c}")

# With star operator
print("\nWith star operator (collect extras):")
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"numbers = {numbers}")
print(f"first, *middle, last = numbers")
print(f"first = {first}")
print(f"middle = {middle}  ← Collected the extras!")
print(f"last = {last}")

# More star examples
print("\n2. More star operator examples:")

# Get first and rest
print("\nGet first item and the rest:")
first_item, *remaining = ["apple", "banana", "orange", "grape"]
print(f"first_item = '{first_item}'")
print(f"remaining = {remaining}")

# Get first few and rest
print("\nGet first few and the rest:")
first, second, *others = [10, 20, 30, 40, 50, 60]
print(f"first = {first}, second = {second}")
print(f"others = {others}")

# Ignoring values
print("\nIgnoring some values:")
name, _, age, _ = ["Bob", "123 Street", 30, "Engineer"]
print(f"name = '{name}', age = {age}")
print("_ is used for values we don't care about")

# Swapping values (classic trick!)
print("\n3. The classic swap trick:")
print("\nTraditional swap (with temp variable):")
x = 5
y = 10
print(f"Before: x={x}, y={y}")
temp = x
x = y
y = temp
print(f"After: x={x}, y={y}")

print("\nPythonic swap (with unpacking):")
x = 5
y = 10
print(f"Before: x={x}, y={y}")
x, y = y, x  # Magic unpacking swap!
print(f"After: x={x}, y={y}")

print("\nHow it works:")
print("""Right side: (y, x) creates tuple (10, 5)
Left side: x, y = unpacks tuple to x=10, y=5
No temp variable needed!""")

# ============================================================================
# SECTION 5: WALRUS OPERATOR - NAMING WHILE USING
# ============================================================================
print("\n\n5. WALRUS OPERATOR (:=) - NAMING WHILE USING")
print("-" * 40)

print("""The walrus operator (:=) lets you:
1. Assign a value to a variable
2. AND use that value immediately

It's called 'walrus' because := looks like walrus eyes and tusks! 🦭""")

print("\nBasic syntax:")
print("(variable := expression)")

# Simple walrus example
print("\nSimple example:")

# Without walrus
print("\nWithout walrus (two steps):")
name = input("What's your name? ")
print(f"Hello, {name}!")

# With walrus (one step)
print("\nWith walrus (one step):")
print(f"Hello, {(name := input('What is your name? '))}!")
print(f"name variable now contains: '{name}'")

print("\nWhy 'walrus'? Look at the operator:")
print("  :=  ← See the eyes (:) and tusks (=)?")

# Practical example: While loop
print("\nPractical example: Reading until 'quit'")

print("\nTraditional way (repetitive code):")
print("""# This would be repetitive:
# command = input("Enter command: ")
# while command != "quit":
#     print(f"You entered: {command}")
#     command = input("Enter command: ")""")

print("\nWith walrus operator (cleaner):")
print("""# while (command := input("Enter command: ")) != "quit":
#     print(f"You entered: {command}")""")

# Let's demonstrate a safe version
print("\nLet's demonstrate with a safe example:")
print("We'll read numbers until we get 0")

# Traditional way
print("\nTraditional way (without walrus):")
print("""number = float(input("Enter a number (0 to stop): "))
while number != 0:
    print(f"Number squared: {number * number}")
    number = float(input("Enter a number (0 to stop): "))""")

# Walrus way
print("\nWalrus way (more concise):")
print("""while (number := float(input("Enter a number (0 to stop): "))) != 0:
    print(f"Number squared: {number * number}")""")

# List comprehension example
print("\nAnother example: Filtering while computing")

print("\nWithout walrus (inefficient):")
numbers = [1, 2, 3, 4, 5]
print(f"numbers = {numbers}")

# Filter numbers where square is greater than 10
result = []
for n in numbers:
    square = n * n
    if square > 10:
        result.append(square)
print(f"Squares > 10: {result}")

print("\nWith walrus (more efficient):")
result = [square for n in numbers if (square := n * n) > 10]
print(f"Squares > 10 (using walrus): {result}")

print("\nWhat happened?")
print("""We computed n * n AND stored it in 'square'
AND checked if it's > 10
All in one line!""")

# ============================================================================
# SECTION 6: PUTTING IT ALL TOGETHER
# ============================================================================
print("\n\n6. REAL-WORLD EXAMPLE: STUDENT DATA PROCESSING")
print("-" * 40)

print("Let's process student data using all techniques:")

# Simulate student data (list of tuples)
print("\n1. Our student data (list of tuples):")
students = [
    ("Alice", 95, 87, 92),
    ("Bob", 78, 85, 80),
    ("Charlie", 88, 91, 85),
    ("Diana", 92, 94, 90)
]

print(f"students = {students}")

# Process each student
print("\n2. Process each student with unpacking:")

# Initialize accumulators with parallel assignment
total_math = total_science = total_english = 0

for student in students:
    # Unpack student data
    name, math, science, english = student
    
    # Use walrus to compute average and check condition
    if (average := (math + science + english) / 3) > 90:
        print(f"  {name}: Average = {average:.1f} (Excellent!)")
    else:
        print(f"  {name}: Average = {average:.1f}")
    
    # Add to totals
    total_math += math
    total_science += science
    total_english += english

print("\n3. Calculate subject averages:")
num_students = len(students)
avg_math = total_math / num_students
avg_science = total_science / num_students
avg_english = total_english / num_students

print(f"Math average: {avg_math:.1f}")
print(f"Science average: {avg_science:.1f}")
print(f"English average: {avg_english:.1f}")

# Find top student using walrus in max
print("\n4. Find top student:")
# Using walrus in a list comprehension
top_student = max(
    ((name, (math + science + english) / 3) 
     for name, math, science, english in students),
    key=lambda x: x[1]
)
print(f"Top student: {top_student[0]} with average {top_student[1]:.1f}")

# ============================================================================
# SECTION 7: WHEN TO USE EACH TECHNIQUE
# ============================================================================
print("\n\n7. WHEN TO USE EACH TECHNIQUE")
print("-" * 40)

print("""Summary guide:

1. PARALLEL ASSIGNMENT
   Use when:
   • Initializing multiple variables to SAME value
   • Setting default values for related variables
   Example: x = y = z = 0

2. ITERABLE UNPACKING
   Use when:
   • Extracting values from lists/tuples
   • Swapping variable values
   • Function returning multiple values
   Example: name, age = ("Alice", 25)

3. STAR OPERATOR (*) in UNPACKING
   Use when:
   • You don't know how many values you'll get
   • You want to collect "extra" values
   • Ignoring some values
   Example: first, *rest = [1, 2, 3, 4, 5]

4. WALRUS OPERATOR (:=)
   Use when:
   • You need to use a value AND assign it
   • Avoiding repetition in loops/conditions
   • Making list comprehensions more efficient
   Example: while (line := input()) != "quit":

WARNINGS:
• Parallel assignment with mutable objects: Be careful!
• Unpacking needs correct number of variables (or use *)
• Walrus operator: Don't overuse, can make code hard to read""")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

print("""Exercise 1: Parallel Assignment
---------------------------------
Convert this repetitive code to parallel assignment:

red = "#FF0000"
green = "#FF0000"
blue = "#FF0000"  # Oops, all are red! Should be different colors

Exercise 2: Tuple Unpacking
---------------------------
Given this tuple:
person = ("John", "Doe", 30, "john@email.com", "Engineer")

Extract first_name, last_name, and age using unpacking.
Ignore the email and job for now.

Exercise 3: Star Operator
-------------------------
Given this list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Use unpacking with * to get:
- The first number
- The last number
- All numbers in between as a list

Exercise 4: Walrus Operator
---------------------------
Convert this while loop to use walrus operator:

data = input("Enter data (or 'stop' to finish): ")
while data != "stop":
    print(f"Processing: {data}")
    data = input("Enter data (or 'stop' to finish): ")

Exercise 5: Combined Challenge
------------------------------
You have this list of student records:
records = [
    ("Math", 85),
    ("Science", 92),
    ("English", 78),
    ("History", 88)
]

Using unpacking and walrus operator in a list comprehension,
create a new list that contains only subjects where score > 80,
but also include the letter grade:
- A for score >= 90
- B for score >= 80
""")

print("\n" + "=" * 40)
print("ANSWERS (Try first before looking!)")
print("=" * 40)

print("""
Exercise 1 Answer:
red, green, blue = "#FF0000", "#00FF00", "#0000FF"

Exercise 2 Answer:
first_name, last_name, age, _, _ = person

Exercise 3 Answer:
first, *middle, last = numbers

Exercise 4 Answer:
while (data := input("Enter data (or 'stop' to finish): ")) != "stop":
    print(f"Processing: {data}")

Exercise 5 Answer:
result = [
    (subject, grade, "A" if grade >= 90 else "B")
    for subject, grade in records
    if grade > 80
]
# Or with walrus if we want to compute grade letter only once:
result = [
    (subject, grade, letter)
    for subject, grade in records
    if grade > 80 and (letter := "A" if grade >= 90 else "B")
]
""")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
1. 🔄 Parallel assignment: One value to many variables (x = y = z = 0)
2. 🎁 Iterable unpacking: Extract values from collections (a, b = (1, 2))
3. ⭐ Star operator: Collect extra values (first, *rest = items)
4. 🦭 Walrus operator: Assign and use in one step (:=)

Remember:
• Use these techniques to write cleaner, more Pythonic code
• But don't overcomplicate - readability is most important!
• Practice makes perfect - try converting your old code""")

print("\n" + "=" * 60)
print("SAVE AS: Complementary_Ways_to_Create_Variables.py")
print("RUN WITH: python Complementary_Ways_to_Create_Variables.py")
print("=" * 60)

# Bonus interactive example
print("\n\nBonus: Interactive demonstration")
print("-" * 40)

# Ask user to try unpacking
print("Let's try unpacking with your name!")

# Get user input and unpack
full_name = input("Enter your full name (first middle last): ").split()
if len(full_name) >= 3:
    first, *middle, last = full_name
    print(f"\nFirst name: {first}")
    print(f"Middle name(s): {' '.join(middle)}")
    print(f"Last name: {last}")
else:
    print("\nPlease enter at least 3 names for proper unpacking!")

print("\n🎉 Congratulations! You've learned complementary ways to create variables!")