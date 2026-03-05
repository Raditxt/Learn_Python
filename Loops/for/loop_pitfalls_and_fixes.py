"""
Common pitfalls in for loops – and how to avoid them.
"""

# ===== 1. Modifying the loop collection while iterating =====
# Python lets you change mutable objects like lists and dicts.
# But doing it inside a loop can lead to surprises.

# Safe: updating existing items (no adding/removing)
names = ["Alice", "Bob", "John", "Jane"]
for i, name in enumerate(names):
    names[i] = name.upper()
print("Uppercased:", names)  # ['ALICE', 'BOB', 'JOHN', 'JANE']

# Unsafe: removing items while iterating
numbers = [2, 4, 6, 8]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)   # This messes up the iteration
print("Oops, still have:", numbers)   # [4, 8] – not what we wanted

# Why? When you remove an item, the list shifts, and the loop skips the next element.
# Fix: iterate over a copy
numbers = [2, 4, 6, 8]
for n in numbers[:]:        # using a slice copy
    if n % 2 == 0:
        numbers.remove(n)
print("All gone:", numbers)  # []

# More complex case: remove evens and square odds
numbers = [2, 1, 4, 6, 5, 8]
processed = []
for n in numbers:
    if n % 2 != 0:
        processed.append(n ** 2)
print("Squares of odds:", processed)   # [1, 25]

# Dictionaries raise an error if you change size during iteration
data = {"one": 1, "two": 2, "three": 3}
# This will crash:
# for k in data:
#     data["four"] = 4   # RuntimeError

# Workaround: iterate over a copy of keys
for k in list(data.keys()):   # or data.copy()
    data["four"] = 4
print("Dictionary after adding:", data)  # now has four

# ===== 2. Changing the loop variable doesn't affect the collection =====
# The loop variable is just a reference to the current item.
# Reassigning it doesn't change the original data.

items = [10, 20, 30]
for x in items:
    x = x * 2          # this only changes x, not the list
print("Items unchanged:", items)   # [10, 20, 30]

# To actually update, you need to access by index or build a new list.

# ===== 3. Ignoring exceptions inside the loop =====
# If an exception occurs and isn't caught, the loop stops.
# That can be a problem when processing multiple items.

files = ["file1.txt", "file2.txt", "file3.txt"]  # none exist

# Without error handling, loop dies on first file
for fname in files:
    # with open(fname) as f:   # would crash here
    #     print(f.read())
    pass

# Better: catch the exception and continue
for fname in files:
    try:
        with open(fname) as f:
            print(f"Contents of {fname}:")
            print(f.read())
    except FileNotFoundError:
        print(f"Warning: {fname} not found, skipping.")

# Now the loop processes all files, handling errors gracefully.

# ===== Summary =====
# - Be careful when adding/removing items from a list/dict you're iterating.
# - Changing the loop variable doesn't alter the original collection.
# - Always handle possible exceptions inside loops unless you want the loop to stop.