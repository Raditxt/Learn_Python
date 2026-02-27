# =============================================================================
# ADVANCED WHILE LOOP SYNTAX: break, continue, and else
# =============================================================================
# This script dives deeper into Python's while loops. You'll learn how to
# control the flow with 'break' and 'continue', and how to use the 'else'
# clause for actions after natural loop termination.

# =============================================================================
# 1. THE break STATEMENT: EXIT THE LOOP EARLY
# =============================================================================
# 'break' immediately stops the loop, and execution jumps to the first line
# after the loop body. It's like hitting an emergency stop button.

print("\n--- break example ---")
number = 6
while number > 0:
    number -= 1
    if number == 2:
        break          # Loop stops completely when number becomes 2
    print(number)

print("Loop ended (after break)")

# Output:
# 5
# 4
# 3
# Loop ended (after break)
# Explanation:
# - The loop prints values until number == 2.
# - At that point, break is triggered, so 2 and 1 are never printed.
# - The program continues after the loop.

# =============================================================================
# 2. THE continue STATEMENT: SKIP THE REST OF THE CURRENT ITERATION
# =============================================================================
# 'continue' stops the current iteration and jumps back to the loop header
# to check the condition again. It's like saying "skip the rest of this round."

print("\n--- continue example ---")
number = 6
while number > 0:
    number -= 1
    if number == 2:
        continue       # Skip printing when number is 2
    print(number)

print("Loop ended (after continue)")

# Output:
# 5
# 4
# 3
# 1
# 0
# Loop ended (after continue)
# Explanation:
# - When number == 2, the print is skipped, but the loop continues.
# - All other values (including 1 and 0) are printed.

# =============================================================================
# 3. THE else CLAUSE: RUN CODE WHEN LOOP ENDS NATURALLY
# =============================================================================
# An optional 'else' block after a while loop runs ONLY if the loop
# terminates because its condition became false (i.e., no break was hit).

print("\n--- else clause example (without break) ---")
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
else:
    print("Loop finished naturally (count reached zero)")

# Output:
# Countdown: 3
# Countdown: 2
# Countdown: 1
# Loop finished naturally (count reached zero)
# Explanation: The loop ends because count became 0, so else runs.

print("\n--- else clause with break ---")
count = 3
while count > 0:
    print(f"Countdown: {count}")
    if count == 2:
        print("Break encountered!")
        break
    count -= 1
else:
    print("This will NOT be printed because of break.")

print("After loop (with break)")

# Output:
# Countdown: 3
# Countdown: 2
# Break encountered!
# After loop (with break)
# Explanation: break stops the loop, so else is skipped.

# =============================================================================
# 4. PRACTICAL EXAMPLE: CONNECTION RETRY WITH break AND else
# =============================================================================
# The 'else' clause shines when you need to handle cases where a loop
# exhausts all attempts without success.

import random
import time

MAX_RETRIES = 5
attempt = 0

print("\n--- Simulating server connection with retries ---")
while attempt < MAX_RETRIES:
    attempt += 1
    print(f"Attempt {attempt}: Connecting...", end=" ")
    time.sleep(0.3)                     # Simulate network delay
    # Randomly decide success (about 25% chance)
    if random.choice([False, False, False, True]):
        print("SUCCESS!")
        break
    print("Failed.")
else:
    # This runs only if the loop never hit 'break' after MAX_RETRIES
    print("All attempts failed. Unable to connect.")

print("Connection attempt finished.")

# Run this multiple times to see both outcomes.
# - If break happens, else is skipped.
# - If all attempts fail, else runs and prints the failure message.

# =============================================================================
# 5. KEY POINTS & COMMON PITFALLS
# =============================================================================
# - 'break' and 'continue' are almost always used inside conditionals (if).
# - Using 'break' outside an 'if' would terminate the loop immediately.
# - 'continue' in a while loop jumps back to the condition check.
# - The 'else' block is **not** executed if the loop ends due to a 'break'.
# - It's usually cleaner to put code after the loop (without else) unless
#   you specifically need to distinguish between break and natural exit.
# - Avoid deep nesting; keep loop bodies readable.

# =============================================================================
# 6.  SUMMARY
# =============================================================================
# - break:   "Stop the loop right now, no matter what."
# - continue: "Skip the rest of this round, but keep looping."
# - else:     "If the loop ends because its condition became false (not because
#             of break), then do this extra thing."
#
# Think of a game show where contestants have multiple tries to guess a number.
# - 'break' = someone guesses correctly, game ends immediately.
# - 'continue' = the guess was invalid (e.g., out of range), skip to next try.
# - 'else' = if no one guessed correctly after all tries, reveal the answer.

# =============================================================================
# 7. CHALLENGES (Test yourself)
# =============================================================================
# 1. Modify the connection example to allow the user to cancel with a 'q' input.
# 2. Write a while loop that prints numbers from 1 to 10, but skips multiples of 3.
# 3. Use a while-else to search for a prime number in a range. If found, break;
#    else print "No prime found".
# 4. What happens if you put a 'continue' after changing the loop variable?
#    Experiment with the countdown example.

# =============================================================================
# End of tutorial. Happy coding!
# =============================================================================