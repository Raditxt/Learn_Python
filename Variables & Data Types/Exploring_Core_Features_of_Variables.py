"""
Exploring_Core_Features_of_Variables.py

This script explains the core features of Python variables in a simple way
that can be understood even by a 5-year-old (using Feynman Technique).

Feynman Technique: Explain complex concepts with simple language,
analogies, and concrete examples.
"""

print("=" * 60)
print("EXPLORING CORE FEATURES OF PYTHON VARIABLES")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

print("=" * 60)
print("SECTION 1: VARIABLES ARE REFERENCES (LIKE NAME TAGS)")
print("=" * 60)
print()

print("1. VARIABLES ARE REFERENCES, NOT BOXES")
print("-" * 40)

print("""In Python, variables don't store objects directly.
They're like NAME TAGS that POINT to objects.""")

print("\nSimple analogy:")
print("• Object = A toy (like a red ball)")
print("• Variable = A name tag that says 'My Toy'")
print("• The name tag POINTS to the toy, doesn't CONTAIN it!")

# Demonstrate with id() - shows memory address
print("\nDemonstration with id() function:")
toy = "red ball"  # Create a string object
print(f"toy = '{toy}'")
print(f"id(toy) = {id(toy)} # Unique ID (like toy's address)")

print("\nNow let's create another reference to SAME object:")
my_toy = toy  # Both variables point to SAME object
print(f"my_toy = toy # Make my_toy point to same object")
print(f"id(my_toy) = {id(my_toy)}")
print(f"Same ID? {id(toy) == id(my_toy)}")

print("\nKey insight:")
print("""• Multiple variables can point to ONE object
• Changing object affects ALL variables pointing to it
• Variables are CONNECTIONS, not containers""")

print("\n" + "=" * 60)
print("SECTION 2: HOW PYTHON CREATES OBJECTS")
print("=" * 60)

print("\n2. HOW PYTHON CREATES AND MANAGES OBJECTS")
print("-" * 40)

print("""When you write: x = 100
Python does 3 things:

1. Creates integer object with value 100
2. Gives it a unique ID (address)
3. Makes variable x POINT to that object""")

# Step-by-step demonstration
print("\nStep-by-step demonstration:")

# Step 1: Create object
print("Step 1: Python creates integer object 300")
print(" Object created: 300 (type: int)")
print(" Memory address assigned (we can't see directly)")

# Step 2: Assign to variable
print("\nStep 2: Assign to variable 'count'")
count = 300
print(f" count = {count}")
print(f" count's ID: {id(count)}")

# Step 3: Show type
print("\nStep 3: Check object type")
print(f" type(count) = {type(count)}")

print("\nWhat really happens:")
print("""
count = 300
│
└───┐
▼
┌─────────────┐
│ OBJECT      │
│ Value: 300  │
│ Type: int   │
│ ID: {id}    │
└─────────────┘
The variable 'count' POINTS to the object""")

print("\n" + "=" * 60)
print("SECTION 3: GARBAGE COLLECTION - CLEANING UP")
print("=" * 60)

print("\n3. GARBAGE COLLECTION - PYTHON'S CLEANER")
print("-" * 40)

print("""When no variables point to an object,
Python's garbage collector removes it.
Think of it as a robot cleaner!""")

# Demonstration
print("\nDemonstration: Creating orphaned objects")

# Create initial object
print("1. Create variable 'book' pointing to 'Harry Potter'")
book = "Harry Potter"
print(f" book = '{book}'")
print(f" Object ID: {id(book)}")

# Create another reference
print("\n2. Create 'favorite_book' pointing to SAME object")
favorite_book = book
print(f" favorite_book = book")
print(f" Same ID? {id(book) == id(favorite_book)}")

# Change one variable
print("\n3. Change 'book' to point to NEW object")
book = "Lord of the Rings"
print(f" book = '{book}' (new object)")
print(f" favorite_book = '{favorite_book}' (still old object)")

print("\nWhat happened?")
print("""• 'Harry Potter' object still has ONE reference (favorite_book)
• 'Lord of the Rings' is a NEW object
• Garbage collector NOT activated yet""")

# Remove last reference
print("\n4. Remove last reference to 'Harry Potter'")
favorite_book = "New Book"
print(f" favorite_book = '{favorite_book}' (new object)")
print(" 'Harry Potter' object now has ZERO references!")

print("\nGarbage collector sees:")
print("""• Object: 'Harry Potter'
• Reference count: 0
• Action: Clean up memory (we can't see this happen)""")

print("\nAnalogy:")
print("""• Objects = Toys in playroom
• Variables = Children playing with toys
• Garbage collector = Parent who puts away unused toys""")

print("\n" + "=" * 60)
print("SECTION 4: DYNAMIC TYPING - VARIABLES CAN CHANGE TYPE")
print("=" * 60)

print("\n4. DYNAMIC TYPING - SHAPESHIFTING VARIABLES")
print("-" * 40)

print("""Python variables can change their type!
This is called DYNAMIC TYPING.""")

# Demonstration of type changing
print("\nDemonstration: One variable, many types:")

# Start as integer
data = 100
print(f"1. data = {data} (type: {type(data).__name__})")

# Change to float
data = 99.5
print(f"2. data = {data} (type: {type(data).__name__})")

# Change to string
data = "Hello Python"
print(f"3. data = '{data}' (type: {type(data).__name__})")

# Change to list
data = [1, 2, 3]
print(f"4. data = {data} (type: {type(data).__name__})")

# Change to dictionary
data = {"name": "Budi", "age": 8}
print(f"5. data = {data} (type: {type(data).__name__})")

print("\nWhat's happening?")
print("""The variable 'data' changes what it POINTS to:

1. First points to integer object 100
2. Then points to float object 99.5
3. Then points to string object 'Hello Python'
4. Then points to list object [1, 2, 3]
5. Then points to dictionary object {...}

The VARIABLE doesn't change - it just points to DIFFERENT objects!""")

print("\n" + "=" * 60)
print("SECTION 5: THE DANGER OF DYNAMIC TYPING")
print("=" * 60)

print("\n5. THE DANGER - TYPE ERRORS AT RUNTIME")
print("-" * 40)

print("""Dynamic typing can cause errors
if we're not careful about types!""")

# Example of type error
print("\nExample: What works and what breaks")

# Working example
print("\n1. Working example (string methods):")
text = "hello world"
print(f" text = '{text}'")
print(f" text.upper() = '{text.upper()}' ✓ Works!")

# Problematic example
print("\n2. Problematic example (type changes):")
data = "hello"
print(f" Step 1: data = '{data}'")
print(f" data.upper() = '{data.upper()}' ✓ Works!")

print("\n Step 2: Change data to number")
data = 123
print(f" data = {data}")

print("\n Step 3: Try string method on number:")
print(" data.upper() ← This will ERROR!")
print(" Because numbers don't have .upper() method")

print("\nActual error would be:")
print("""AttributeError: 'int' object has no attribute 'upper'
Python says: 'Hey! Numbers can't do string tricks!'""")

print("\nSolution: Be careful or use type hints (next section)")

print("\n" + "=" * 60)
print("SECTION 6: TYPE HINTS - TELLING PYTHON ABOUT TYPES")
print("=" * 60)

print("\n6. TYPE HINTS - LEAVING NOTES ABOUT TYPES")
print("-" * 40)

print("""Type hints are like notes we leave for:

1. Ourselves (to remember)
2. Other programmers
3. Tools (to check for errors)

They DON'T change how Python works, just help prevent mistakes!""")

# Basic type hints
print("\nBasic type hints (optional but helpful):")

# String with type hint
name: str = "Budi"
print(f"name: str = '{name}'")
print(f" Type hint says: 'name should always be string'")

# Integer with type hint
age: int = 8
print(f"\nage: int = {age}")
print(f" Type hint says: 'age should always be integer'")

# Float with type hint
height: float = 120.5
print(f"\nheight: float = {height}")
print(f" Type hint says: 'height should always be float'")

print("\nWhy use type hints?")
print("1. Makes code easier to understand")
print("2. Tools can catch type errors before running")
print("3. Helps team collaboration")

print("\n" + "=" * 60)
print("SECTION 7: TYPE HINTS FOR COLLECTIONS (LISTS, DICTS)")
print("=" * 60)

print("\n7. TYPE HINTS FOR COLLECTIONS (MORE IMPORTANT!)")
print("-" * 40)

print("""Type hints are ESPECIALLY useful for collections
like lists, dictionaries, tuples.""")

# List with type hint
print("\n1. List with type hint:")
fruits: list[str] = ["apple", "banana", "orange"]
print(f"fruits: list[str] = {fruits}")
print(" Meaning: List that should contain ONLY strings")

# Empty list with type hint
print("\n2. Empty list with type hint:")
shopping_list: list[str] = []
print(f"shopping_list: list[str] = {shopping_list}")
print(" Even when empty, we know what should go inside!")

# Dictionary with type hints
print("\n3. Dictionary with type hints:")
student: dict[str, str | int] = {
    "name": "Budi",
    "age": 8,
    "grade": "3A"
}
print(f"""student: dict[str, str | int] = {student}""")
print(" Meaning: Keys are strings, values are strings OR integers")

# Complex example
print("\n4. Complex example - list of tuples:")
students: list[tuple[str, int, str]] = [
    ("Budi", 8, "3A"),
    ("Andi", 9, "4B"),
    ("Caca", 8, "3A")
]
print(f"""students: list[tuple[str, int, str]] = {students}""")
print(""" Meaning: List of tuples where each tuple has:

1. String (name)
2. Integer (age)
3. String (grade)""")

print("\n" + "=" * 60)
print("SECTION 8: PRACTICAL EXAMPLE WITH TYPE HINTS")
print("=" * 60)

print("\n8. PRACTICAL EXAMPLE: CONTACT BOOK")
print("-" * 40)

print("Let's build a simple contact book with type hints:")

# Define types first
print("\n1. Define our data structure with type hints:")

# Type alias for readability
from typing import TypedDict

class ContactInfo(TypedDict):
    phone: str
    email: str
    age: int

# Dictionary with type hints
contacts: dict[str, ContactInfo] = {
    "Alice": {"phone": "123-456", "email": "alice@email.com", "age": 25},
    "Bob": {"phone": "789-012", "email": "bob@email.com", "age": 30},
    "Charlie": {"phone": "345-678", "email": "charlie@email.com", "age": 22}
}

print(f"""contacts: dict[str, ContactInfo] = ...""")
print(f"Total contacts: {len(contacts)}")

print("\n2. Add new contact (type-safe):")
contacts["David"] = {
    "phone": "901-234",
    "email": "david@email.com",
    "age": 28
}

print("\n3. Access contact information:")
for name, info in contacts.items():
    print(f"  {name}: Phone: {info['phone']}, Age: {info['age']}")

print("\nBenefits of type hints here:")
print("1. Clear what data structure should be")
print("2. Tools can warn if we add wrong data type")
print("3. Easier for others to understand our code")

print("\n" + "=" * 60)
print("SECTION 9: CHECKING TYPES AT RUNTIME")
print("=" * 60)

print("\n9. CHECKING TYPES AT RUNTIME")
print("-" * 40)

print("""We can check types while program runs
using isinstance() function.""")

# Demonstrate isinstance
print("\nUsing isinstance() to check types:")

data = 100
print(f"data = {data}")
print(f"isinstance(data, int) = {isinstance(data, int)}")
print(f"isinstance(data, str) = {isinstance(data, str)}")

print("\nPractical example - safe function:")

def safe_uppercase(value):
    """Only call .upper() if value is string"""
    if isinstance(value, str):
        return value.upper()
    else:
        return f"Cannot uppercase {type(value).__name__}"

# Test the function
test_values = ["hello", 123, 45.6, ["a", "b"]]
print("\nTesting safe_uppercase function:")
for val in test_values:
    result = safe_uppercase(val)
    print(f"  safe_uppercase({repr(val)}) = {repr(result)}")

print("\nWhy check types?")
print("1. Prevent crashes from type errors")
print("2. Handle different input types gracefully")
print("3. Make code more robust")

print("\n" + "=" * 60)
print("SECTION 10: PUTTING IT ALL TOGETHER")
print("=" * 60)

print("\n10. SUMMARY - HOW PYTHON VARIABLES WORK")
print("-" * 40)

print("""Key concepts about Python variables:

1. REFERENCES, NOT CONTAINERS
   • Variables point to objects (don't contain them)
   • Multiple variables can point to same object
   • id() shows object's unique identifier

2. OBJECT LIFECYCLE
   • Objects created when needed
   • Garbage collected when no references
   • Memory managed automatically

3. DYNAMIC TYPING
   • Variables can point to objects of any type
   • Flexible but can cause runtime errors
   • Type can change during program execution

4. TYPE HINTS
   • Optional notes about expected types
   • Especially useful for collections
   • Helps tools find errors early

5. TYPE CHECKING
   • isinstance() checks types at runtime
   • Can prevent crashes
   • Makes code more reliable""")

print("\nVisual analogy:")
print("""Variables are like ARROWS
Objects are like TARGETS
Multiple arrows can point to same target
Arrows can change which target they point to""")

print("\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

print("""Exercise 1: Trace the References

Follow this code. How many objects are created?
When is each object garbage collected?

a = "Hello"
b = a
c = b
a = "World"
b = 123
c = [1, 2, 3]

Exercise 2: Fix Type Errors

This function has type-related issues.
How would you fix it?

def process_data(data):
    return data.upper() + str(len(data))

Test cases that should work:
process_data("hello") # Should return "HELLO5"
process_data(123)     # Should return error or handle gracefully

Exercise 3: Add Type Hints

Add type hints to this code:

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

What type hint would you add for 'scores' parameter?
What about return value?

Exercise 4: Object Identity Check

What does this code output? Why?

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y) # What's the output?
print(x is z) # What's the output?
print(x == y) # What's the output?
""")

print("\nAnswers (think first!):")
print("""Exercise 1:
4 objects created: "Hello", "World", 123, [1, 2, 3]
"Hello" garbage collected after line: b = 123

Exercise 2:
def process_data(data):
    if isinstance(data, str):
        return data.upper() + str(len(data))
    else:
        return f"Cannot process {type(data).__name__}"

Exercise 3:
def calculate_average(scores: list[float]) -> float:
    total = 0.0
    for score in scores:
        total += score
    return total / len(scores)

Exercise 4:
x is y → False (different objects, same values)
x is z → True (same object)
x == y → True (same values)""")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
🎯 Variables are REFERENCES, not containers
🔄 Python manages memory automatically (garbage collection)
🎭 Variables can change types (dynamic typing)
📝 Type hints help prevent errors (optional but useful)
🔍 Use isinstance() for runtime type checking
🧠 Understanding this makes you a better Python programmer!

Remember: In Python, everything is an object,
and variables are just names for those objects!""")

print("\n" + "=" * 60)
print("BONUS: Demonstration of object identity")
print("=" * 60)

print("\nBonus: Demonstration of object identity")
print("-" * 40)

# Show difference between 'is' and '=='
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2} (same values, different object)")
print(f"list3 = list1 (same object)")

print(f"\nlist1 is list2: {list1 is list2} # Different objects")
print(f"list1 is list3: {list1 is list3} # Same object")
print(f"list1 == list2: {list1 == list2} # Same values")

print("\n'is' checks: Are these the SAME object?")
print("'==' checks: Do these objects have SAME VALUE?")

print("\n" + "=" * 60)
print("END OF SCRIPT")
print("=" * 60)