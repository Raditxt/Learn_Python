# =============================================================================
# 1. WHAT IS A WHILE LOOP?
# =============================================================================
# Imagine you're waiting for a bus. You keep checking: "Is the bus here yet?"
# If not, you wait a bit and check again. You repeat this until the bus arrives.
#
# In programming, a while loop is exactly that: it repeats a block of code
# over and over as long as a certain condition remains true.
#
# Python has two main loop types:
#   - for loops: when you know how many times to repeat (like counting 5 passengers)
#   - while loops: when you don't know in advance (like waiting for an unknown arrival)
#
# A while loop is a "compound statement": it has a header with a condition,
# and an indented body that runs repeatedly.

# =============================================================================
# 2. BASIC SYNTAX
# =============================================================================
# while condition:
#     <body>
#
# - 'while' is the keyword.
# - 'condition' is an expression that Python evaluates for truthiness.
# - '<body>' is one or more indented statements.
#
# Important: The condition is checked BEFORE each iteration.
#            If it's True, the body runs; if False, the loop stops.

# =============================================================================
# 3. SIMPLE EXAMPLE: COUNTDOWN
# =============================================================================
print("\n--- Example 1: Countdown ---")
number = 5
while number > 0:
    print(number)
    number -= 1          # Decrease number by 1 each time
print("Blast off!")

# Explanation:
# - Initially number = 5, condition 5 > 0 is True → prints 5, then number becomes 4.
# - Next iteration: 4 > 0 True → prints 4, number becomes 3.
# - ... until number = 1: prints 1, number becomes 0.
# - Now condition 0 > 0 is False → loop ends. "Blast off!" is printed after the loop.

# =============================================================================
# 4. WHAT HAPPENS INSIDE THE LOOP
# =============================================================================
# The body must contain something that eventually makes the condition False.
# Otherwise, you get an infinite loop. The countdown works because we decrease 'number'
# each time. Eventually it becomes 0 and the loop stops.

# =============================================================================
# 5. INFINITE LOOPS (AND HOW TO STOP THEM)
# =============================================================================
print("\n--- Example 2: Infinite loop (watch out!) ---")
# Uncomment the code below to try it. Be ready to press Ctrl+C to stop.
"""
number = 5
while number != 0:
    print(number)
    number -= 2
# This loop will print: 5, 3, 1, -1, -3, ... and never reach 0.
# It's an infinite loop because number skips over 0.
# To stop it, press Ctrl+C (KeyboardInterrupt).
"""
print("(Infinite loop example is commented out to keep you safe.)")

# =============================================================================
# 6. LOOP THAT NEVER RUNS
# =============================================================================
print("\n--- Example 3: Loop with false condition initially ---")
number = 0
while number > 0:
    print("This will never be printed.")
    number -= 1
print("Condition was false from the start, so the loop was skipped.")

# Explanation: The condition is checked first. Since 0 > 0 is False,
# the body is never executed. Execution continues after the loop.

# =============================================================================
# 7. PRACTICAL EXAMPLE: USER INPUT VALIDATION
# =============================================================================
print("\n--- Example 4: Asking for positive number ---")
# While loops are great when you don't know how many tries the user will need.
value = -1   # Start with an invalid value to enter the loop
while value <= 0:
    try:
        value = int(input("Enter a positive integer: "))
        if value <= 0:
            print("That's not positive. Try again.")
    except ValueError:
        print("That's not an integer. Try again.")
print(f"Thanks! You entered {value}.")

# =============================================================================
# 8. USING 'break' AND 'continue'
# =============================================================================
print("\n--- Example 5: break and continue ---")
# - 'break' immediately exits the loop.
# - 'continue' skips the rest of the current iteration and jumps to the next condition check.

# Let's simulate a game: guess a secret number (7)
secret = 7
guess = None
print("Guess the secret number (between 1 and 10). Type 0 to give up.")
while True:                     # This creates an infinite loop, but we'll break out
    try:
        guess = int(input("Your guess: "))
        if guess == 0:
            print("You gave up. The secret was", secret)
            break
        if guess < 1 or guess > 10:
            print("Out of range. Try again.")
            continue             # Go back to the start of the loop
        if guess == secret:
            print("Correct! Well done.")
            break
        else:
            print("Wrong, try again.")
    except ValueError:
        print("Please enter a number.")

# =============================================================================
# 9. COMMON PITFALLS
# =============================================================================
# - Forgetting to update the variable used in the condition → infinite loop.
# - Using assignment (=) instead of comparison (==) in the condition.
# - Off-by-one errors: e.g., using > instead of >=.
# - Infinite loops due to floating-point inaccuracies (avoid comparing floats for equality).

# =============================================================================
# 10. SUMMARY: FEYNMAN-STYLE EXPLANATION
# =============================================================================
# Imagine a while loop as a guard at a door:
#   - The guard checks a condition (like "is it raining outside?").
#   - If true, he lets you go through the door, do something, and then come back.
#   - He checks again. As long as it's raining, you keep going in and out.
#   - When it stops raining (condition false), he closes the door and you move on.
#
# In code:
#   while it_is_raining:
#       take_umbrella()
#       go_outside()
#       come_back()
#   print("The rain has stopped.")
#
# The key is that something inside the loop must eventually change the condition
# (like the weather), otherwise you'll be stuck forever.

# =============================================================================
# 11. CHALLENGE EXERCISES (Test your understanding)
# =============================================================================
# Try to solve these mentally or by modifying the script:
#
# 1. Write a while loop that prints all even numbers from 10 down to 2.
# 2. Write a loop that repeatedly asks the user for a password until they enter "secret".
# 3. Write a loop that sums numbers entered by the user until they enter 0, then prints the total.
# 4. What would happen if you forget to indent the body statements? Try it (and fix it afterward).
# 5. Can you rewrite the countdown example using a for loop? When would you choose while instead?

print("\n--- End of tutorial. Happy coding! ---")