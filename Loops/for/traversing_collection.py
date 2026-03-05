"""
TRAVERSING BUILT-IN COLLECTIONS IN PYTHON
==========================================
This script demonstrates how to iterate over common built-in data types
using for loops: lists, tuples, strings, ranges, dictionaries, and sets.
"""

# =============================================================================
# 1. SEQUENCES: LISTS, TUPLES, STRINGS, RANGES
# =============================================================================
# Iteration over sequences happens in the order the items appear.

print("\n--- Lists ---")
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)               # 1, 2, 3, 4

print("\n--- Tuples ---")
person = ("Jane", 25, "Python Dev", "Canada")
for field in person:
    print(field)                # Jane, 25, Python Dev, Canada

print("\n--- Strings (character by character) ---")
text = "abcde"
for character in text:
    print(character)            # a, b, c, d, e

print("\n--- Ranges ---")
for index in range(5):
    print(index)                # 0, 1, 2, 3, 4

# =============================================================================
# 2. DICTIONARIES
# =============================================================================
# Dictionaries can be iterated over keys, values, or key-value pairs.

students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
}

print("\n--- Dictionary: iterating over keys (default) ---")
for student in students:
    print(student)              # Alice, Bob, Charlie, Diana, Ethan

print("\n--- Dictionary: iterating over keys explicitly with .keys() ---")
for student in students.keys():
    print(student)              # same as above

print("\n--- Dictionary: accessing values via key ---")
for student in students:
    print(student, "->", students[student])

print("\n--- Dictionary: iterating over values with .values() ---")
teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}
for team in teams.values():
    print(team)                 # Rockies, White Sox, Red Sox, Twins, Brewers, Mariners

print("\n--- Dictionary: iterating over key-value pairs with .items() ---")
for place, team in teams.items():
    print(place, "->", team)

# =============================================================================
# 3. SETS
# =============================================================================
# Sets are unordered, so iteration order is not guaranteed.

print("\n--- Sets (unordered iteration) ---")
tools = {"Django", "Flask", "pandas", "NumPy"}
for tool in tools:
    print(tool)                 # order may vary each run

# =============================================================================
# 4. KEY TAKEAWAYS
# =============================================================================
# - Use for loops to traverse any iterable collection.
# - For sequences, order is preserved.
# - Dictionaries offer .keys(), .values(), and .items() for different iteration needs.
# - Sets are unordered; do not rely on element order.
# - Naming: plural for collection, singular for loop variable (e.g., students, student).
# =============================================================================