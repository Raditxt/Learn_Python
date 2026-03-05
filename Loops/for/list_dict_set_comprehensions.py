"""
For loops vs comprehensions: when to use each.
"""

# ===== Building a list with a loop =====
cubes = []
for number in range(10):
    cubes.append(number ** 3)
print("Loop result:", cubes)

# Same thing with a list comprehension
cubes = [number ** 3 for number in range(10)]
print("Comprehension result:", cubes)

# ===== With condition =====
# Loop: even numbers squared
even_squares = []
for n in range(10):
    if n % 2 == 0:
        even_squares.append(n ** 2)
print("Even squares (loop):", even_squares)

# Comprehension
even_squares = [n ** 2 for n in range(10) if n % 2 == 0]
print("Even squares (comprehension):", even_squares)

# ===== Dictionary comprehension =====
# Loop: create a dict mapping number to its square
squares_dict = {}
for n in range(5):
    squares_dict[n] = n ** 2
print("Dict loop:", squares_dict)

# Comprehension
squares_dict = {n: n ** 2 for n in range(5)}
print("Dict comp:", squares_dict)

# ===== Set comprehension =====
# Loop: collect unique lengths of words
words = ["hello", "world", "python", "loop", "hello"]
lengths = set()
for w in words:
    lengths.add(len(w))
print("Set loop:", lengths)

# Comprehension
lengths = {len(w) for w in words}
print("Set comp:", lengths)

# ===== When to use loops over comprehensions =====
# Comprehensions are great for simple transformations/filtering.
# Use a loop when:
# - The logic is too complex to fit in a single expression.
# - You need to perform side effects (e.g., printing, writing to file).
# - You need to break or continue based on complex conditions.
# - You're building more than one collection at a time.

# Example: building two lists at once
evens = []
odds = []
for n in range(10):
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)
print("Evens:", evens)
print("Odds:", odds)

# Trying that with a comprehension would be awkward (you'd need two separate ones).

# ===== Nested comprehensions =====
# Sometimes comprehensions can handle nested loops
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened:", flattened)

# Equivalent loop:
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print("Flattened (loop):", flat)

# ===== Performance note =====
# Comprehensions are generally faster than manual loops because they are optimized in C.
# But readability matters more than micro-optimizations. Choose what's clearer.

# ===== Summary =====
# - Comprehensions are Pythonic and concise for creating lists, dicts, sets.
# - Use loops when you need more control or side effects.