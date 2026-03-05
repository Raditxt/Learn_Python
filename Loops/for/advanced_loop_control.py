"""
Advanced for loop syntax: break, continue, else, and nesting.
"""

# ========== break ==========
# Sometimes you want to stop the loop early. That's what 'break' does.
# Imagine searching for a number in a list – once you find it, no need to keep going.

numbers = [1, 3, 5, 7, 9]
target = 5

print("--- break example ---")
for n in numbers:
    print(f"Checking {n}...")
    if n == target:
        print(f"Found {target}, stopping.")
        break
# After break, we jump here. The remaining numbers (7,9) are skipped.

# ========== continue ==========
# 'continue' skips the rest of the current iteration and moves to the next item.
# Let's say we only want to do something for even numbers.

print("\n--- continue example ---")
values = [1, 2, 3, 4, 5, 6]
for v in values:
    if v % 2 != 0:          # odd numbers
        continue            # skip the even-processing part
    print(f"{v} is even!")  # only reached for evens

# ========== else clause ==========
# A for loop can have an 'else' that runs only if the loop finished normally
# (i.e., no 'break' was hit). Great for "not found" situations.

print("\n--- else example ---")
nums = [1, 3, 5, 7, 9]
search_for = 42

for x in nums:
    print(f"Looking at {x}...")
    if x == search_for:
        print(f"Found it!")
        break
else:
    # This runs because we never broke out
    print(f"{search_for} not in the list.")

# ========== nested for loops ==========
# You can put loops inside loops. Common for working with 2D data.
# Here's a multiplication table from 1 to 10.

print("\n--- nested loops: multiplication table ---")
for row in range(1, 11):                 # outer loop: rows
    for col in range(row, row*11, row):  # inner loop: columns
        # print each product, right-aligned, no newline
        print(f"{col:>4d}", end="")
    print()  # newline after each row

# That's the gist of it. Use these tools wisely, and your loops will be clean and efficient.