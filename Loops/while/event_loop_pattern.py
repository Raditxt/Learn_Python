# =============================================================================
# USING while LOOPS FOR EVENT LOOPS
# =============================================================================
# Event loops are infinite loops that wait for events (user input, sensor data,
# network messages, etc.) and react accordingly. They are common in GUI
# applications, games, servers, and real‑time systems.

# The core structure is:
#   while True:
#       event = wait_for_event()
#       handle_event(event)

# =============================================================================
# EXAMPLE: NUMBER GUESSING GAME (SIMPLE EVENT LOOP)
# =============================================================================
# Here the "event" is the user's guess. The loop runs forever until the
# correct guess breaks it.

from random import randint

LOW, HIGH = 1, 10
secret_number = randint(LOW, HIGH)
clue = ""

print("\n--- Number Guessing Game ---")
while True:
    # Get user input (the event)
    guess = input(f"Guess a number between {LOW} and {HIGH} {clue}: ").strip()
    try:
        number = int(guess)
    except ValueError:
        print("Please enter a valid integer.")
        continue

    # Event handling logic
    if number > secret_number:
        clue = f"(less than {number})"
    elif number < secret_number:
        clue = f"(greater than {number})"
    else:
        break      # correct guess → exit loop

print(f"You guessed it! The secret number was {secret_number}.")

# =============================================================================
# KEY CHARACTERISTICS OF EVENT LOOPS
# =============================================================================
# - They run indefinitely (while True) until a termination event occurs.
# - They block waiting for an event (input(), network receive, etc.).
# - They dispatch the event to appropriate handlers (conditional branches).
# - They often need to handle multiple event types and maintain state.

# =============================================================================
# ADDITIONAL EXAMPLE: SIMPLE COMMAND PROCESSOR
# =============================================================================
# Another classic event loop: a command-line interface that responds to commands.

print("\n--- Simple Command Processor (type 'help' for commands) ---")
commands = {
    "hello": "Hello, world!",
    "time":  f"Current simulation time: {time.time()}",
    "help":  "Available commands: hello, time, exit"
}

while True:
    cmd = input("> ").strip().lower()
    if cmd == "exit":
        print("Goodbye.")
        break
    elif cmd in commands:
        print(commands[cmd])
    else:
        print(f"Unknown command '{cmd}'. Type 'help' for options.")

# =============================================================================
# NOTE
# =============================================================================
# In real‑world applications, event loops are often provided by frameworks
# (e.g., tkinter, pygame, asyncio). However, understanding how to build a
# simple event loop with while True gives you insight into how those frameworks
# work under the hood.
# =============================================================================