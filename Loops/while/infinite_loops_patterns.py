# =============================================================================
# EXPLORING INFINITE while LOOPS
# =============================================================================
# Infinite loops run forever unless interrupted. They can be unintentional
# (bugs) or intentional (useful for servers, games, event loops).

# =============================================================================
# 1. UNINTENTIONAL INFINITE LOOPS (BUGS)
# =============================================================================
# These happen when the loop condition never becomes false.
# Example: decrementing by 2, expecting to hit 0.

print("\n--- Unintentional infinite loop (commented out) ---")
# Uncomment the block below to see it in action (press Ctrl+C to stop).
"""
number = 5
while number != 0:
    print(number)
    number -= 2          # 5, 3, 1, -1, -3, ... never 0
"""
print("(The infinite loop is commented out for safety.)")

# Fix 1: Change the condition to something that will become false.
print("\n--- Fix 1: Adjust condition ---")
number = 5
while number > 0:        # stops when number <= 0
    print(number)
    number -= 2          # prints 5, 3, 1

# Fix 2: Add a failsafe break inside the loop.
print("\n--- Fix 2: Add a safeguard break ---")
number = 5
while number != 0:
    if number <= 0:      # extra safety net
        break
    print(number)
    number -= 2

# =============================================================================
# 2. INTENTIONAL INFINITE LOOPS (while True)
# =============================================================================
# Useful when the loop must run until some condition(s) inside are met.
# Always include at least one break to avoid truly infinite execution.

print("\n--- Intentional infinite loop: password checker ---")
MAX_ATTEMPTS = 3
correct_password = "secret123"
attempts = 0

while True:
    password = input("Password: ").strip()
    attempts += 1

    if password == correct_password:
        print("Login successful! Welcome!")
        break

    if attempts >= MAX_ATTEMPTS:
        print("Too many failed attempts.")
        break
    else:
        print(f"Incorrect password. {MAX_ATTEMPTS - attempts} attempts left.")

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - Unintentional infinite loops: check your condition and loop variable updates.
# - Intentional infinite loops: use while True and break when needed.
# - Always ensure there is a path to break, or the loop can be terminated externally.
# =============================================================================