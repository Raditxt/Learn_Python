"""
GETTING STARTED WITH THE PYTHON FOR LOOP
=========================================
This script introduces the for loop in Python, its syntax, and common use cases.
Run the examples and read the comments to understand how for loops work.
"""

# =============================================================================
# 1. FOR LOOPS VS WHILE LOOPS
# =============================================================================
# - for loops: used when you know how many times to iterate (e.g., over a collection).
# - while loops: used when the number of iterations is unknown and depends on a condition.

# =============================================================================
# 2. BASIC SYNTAX
# =============================================================================
# for variable in iterable:
#     <body>
#
# - 'for' keyword starts the loop.
# - 'variable' takes the value of each item in the iterable, one per iteration.
# - 'in' keyword connects the variable with the iterable.
# - 'iterable' is any object that can be iterated over (list, tuple, string, etc.).
# - '<body>' is the indented block to execute each iteration.

# Example: iterate over a list of colors
print("\n--- Basic for loop over a list ---")
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)

# =============================================================================
# 3. WHAT IS AN ITERABLE?
# =============================================================================
# An iterable is an object capable of returning its elements one at a time.
# Common built-in iterables: list, tuple, string, dictionary, set, range.

print("\n--- Iterating over different iterables ---")

# List (already seen)
print("List:")
for item in [1, 2, 3]:
    print(item)

# Tuple
print("\nTuple:")
for item in (10, 20, 30):
    print(item)

# String (iterates over characters)
print("\nString:")
for char in "Python":
    print(char)

# Dictionary (iterates over keys by default)
print("\nDictionary (keys):")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(key)

# To iterate over values, use .values()
print("\nDictionary (values):")
for value in person.values():
    print(value)

# To iterate over key-value pairs, use .items()
print("\nDictionary (key-value pairs):")
for key, value in person.items():
    print(f"{key} -> {value}")

# Set (order is not guaranteed)
print("\nSet:")
for element in {100, 200, 300}:
    print(element)

# Range (generates numbers)
print("\nRange (0 to 4):")
for i in range(5):
    print(i)

# =============================================================================
# 4. MULTIPLE LOOP VARIABLES (UNPACKING)
# =============================================================================
# If your iterable contains tuples (or other unpackable structures), you can
# use multiple variables directly in the loop header.

print("\n--- Multiple loop variables ---")
points = [(1, 4), (3, 6), (7, 3)]
for x, y in points:
    print(f"x = {x}, y = {y}")

# Works with any iterable that yields unpackable items, like dictionary items:
for key, value in person.items():
    print(f"{key}: {value}")

# =============================================================================
# 5. EMPTY ITERABLE
# =============================================================================
# If the iterable is empty, the loop body never executes.

print("\n--- Empty iterable ---")
empty_list = []
for item in empty_list:
    print("This will never be printed.")
print("Loop finished (no iterations).")

# =============================================================================
# 6. KEY POINTS TO REMEMBER
# =============================================================================
# - for loops are ideal when you need to process each item in a collection.
# - The loop variable takes a new value each iteration automatically.
# - You can iterate directly over most built‑in data types.
# - Use unpacking to get multiple values per iteration when appropriate.
# - If the iterable is empty, the loop does nothing.
# =============================================================================

# End of tutorial. Experiment by modifying the examples above.