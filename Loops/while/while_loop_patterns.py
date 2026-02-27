# =============================================================================
# WRITING EFFECTIVE while LOOPS IN PYTHON
# =============================================================================
# This script demonstrates practical, efficient, and readable ways to use
# while loops in real-world scenarios. It covers waiting for conditions,
# handling unknown iterations, processing collections, user input,
# manual iterator control, and emulating do-while loops.

# =============================================================================
# 1. RUNNING TASKS BASED ON A CONDITION (WAITING FOR A RESOURCE)
# =============================================================================
# A classic use case: wait for a file to appear before proceeding.

import time
from pathlib import Path

print("\n--- Waiting for a file to be created ---")
filename = Path("hello.txt")
print(f"Waiting for {filename.name} to be created... (Run this script, then create the file in another terminal)")

# while the file does NOT exist, keep waiting
while not filename.exists():
    print("File not found. Retrying in 1 second...")
    time.sleep(1)

print(f"{filename} found! Proceeding with processing.")
if filename.exists():
    with open(filename, mode="r") as file:
        print("File contents:")
        print(file.read())
else:
    print("File still missing? This shouldn't happen.")

# =============================================================================
# 2. UNKNOWN NUMBER OF ITERATIONS (INFINITE LOOP WITH break)
# =============================================================================
# When you don't know how many iterations are needed, use while True and break.

import random

print("\n--- Simulating temperature monitoring ---")

def read_temperature():
    # Simulate a sensor reading between 20.0 and 30.0 °C
    return random.uniform(20.0, 30.0)

while True:
    temperature = read_temperature()
    print(f"Temperature: {temperature:.2f}°C")
    if temperature >= 28:
        print("Required temperature reached! Stopping monitoring.")
        break
    time.sleep(1)   # wait before next reading

# =============================================================================
# 3. REMOVING ITEMS FROM AN ITERABLE DURING ITERATION
# =============================================================================
# Modifying a list while iterating with for can be tricky; while is safer.

print("\n--- Processing and removing items from a list ---")
colors = ["red", "blue", "yellow", "green"]
print("Original list:", colors)

while colors:                     # loop until list is empty
    color = colors.pop()          # remove last item
    print(f"Processing color: {color}")

print("All colors processed. Final list:", colors)

# =============================================================================
# 4. GETTING USER INPUT WITH A while LOOP
# =============================================================================
# A common pattern: ask repeatedly until the user types a sentinel value.

print("\n--- Simple user input loop (without walrus) ---")
line = input("Type some text (or 'stop' to quit): ")
while line != "stop":
    print("You typed:", line)
    line = input("Type some text (or 'stop' to quit): ")
print("Loop ended.")

# Using the walrus operator (Python 3.8+) to avoid duplicate input() call.
print("\n--- Same loop with walrus operator ---")
while (line := input("Type some text (or 'stop' to quit): ")) != "stop":
    print("You typed:", line)
print("Loop ended.")

# =============================================================================
# 5. TRAVERSING ITERATORS MANUALLY WITH next()
# =============================================================================
# While loops give fine control over iterators, including error handling.

print("\n--- Manual iteration over a list using next() ---")
requests = ["first request", "second request", "third request"]
it = iter(requests)

while True:
    try:
        request = next(it)
    except StopIteration:
        break               # no more items
    print(f"Handling {request}")

# This is equivalent to a for loop, but you can insert custom logic
# between fetching items if needed.

# =============================================================================
# 6. EMULATING A DO-WHILE LOOP
# =============================================================================
# Python has no built-in do-while, but you can emulate it with while True + break.

print("\n--- Emulating a do-while loop (body runs at least once) ---")
while True:
    number = int(input("Enter a positive number: "))
    print("You entered:", number)
    if number > 0:
        break   # exit if condition met (condition at the end)
print("Good! Positive number received.")

# =============================================================================
# 7. KEY POINTS FOR WRITING EFFECTIVE while LOOPS
# =============================================================================
# - Prefer for loops when iterating over known collections.
# - Use while loops when the number of iterations is unknown or condition‑based.
# - Always ensure the loop condition eventually becomes false, or include a break.
# - Avoid modifying the loop variable inside the body in unexpected ways.
# - Use else clauses sparingly; they can improve readability when you need
#   to distinguish between natural termination and break.
# - Keep loop bodies short and focused; factor complex logic into functions.

# =============================================================================
# End of tutorial. Experiment with the examples above.
# =============================================================================