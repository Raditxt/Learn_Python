# Basic_Syntax.py
"""
This script explains basic Python syntax in a simple way
that can be understood even by a 5-year-old child (using the Feynman Technique).

Feynman Technique: Explaining complex concepts with simple language, analogies,
and concrete examples.
"""

print("=" * 60)
print("LEARNING PYTHON THE SIMPLE WAY")
print("(Like Explaining to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: FIRST PROGRAM - "Hello World!"
# ============================================================================
print("1. FIRST PROGRAM: 'HELLO WORLD!'")
print("-" * 40)

print("""Imagine Python is like a friend who can talk.
We give commands, it follows!""")

# Example 1: Simple print
print("Hello, World!")  # Python says: "Hello, World!"

print("\nSimple explanation:")
print("""• print() = command to speak/print text
• Parentheses () = like Python's mouth
• "Hello, World!" = the words we want to say
• # = sign for comments (Python doesn't read this)""")

# ============================================================================
# SECTION 2: HOW TO WRITE NAMES (IDENTIFIERS)
# ============================================================================
print("\n\n2. HOW TO WRITE NAMES IN PYTHON")
print("-" * 40)

print("""In Python, we give names to things like:
• Variables (storage boxes)
• Functions (special commands)
• Classes (blueprints for making objects)""")

# Examples of correct identifiers
animal_name = "Cat"  # Can use letters and underscore
age = 3  # Can use numbers, but not at the beginning
_weight = 4.5  # Can start with underscore
PetAnimal = "Fluffy"  # Class names usually start with capital letter

# Examples of incorrect identifiers (commented because they will error)
# 2name = "Wrong"  # Can't start with a number
# animal-name = "Wrong"  # Can't use minus sign
# animal@name = "Wrong"  # Can't use @

print("\nRules for writing names:")
print("1. Can use letters (a-z, A-Z)")
print("2. Can use underscore (_)")
print("3. Can use numbers (0-9), but not at the beginning")
print("4. Python is CASE SENSITIVE")
print("   'Name' and 'name' are DIFFERENT!")

# ============================================================================
# SECTION 3: FORBIDDEN WORDS (RESERVED WORDS)
# ============================================================================
print("\n\n3. FORBIDDEN WORDS IN PYTHON")
print("-" * 40)

print("""Python has special words that cannot be used
for variable names. It's like the words 'mom', 'dad' at home -
they have special meanings!""")

# List of reserved words
reserved_words = [
    'and', 'as', 'assert', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except', 'False',
    'finally', 'for', 'from', 'global', 'if', 'import',
    'in', 'is', 'lambda', 'None', 'nonlocal', 'not',
    'or', 'pass', 'raise', 'return', 'True', 'try',
    'while', 'with', 'yield'
]

print("\nReserved words (cannot be variable names):")
print(", ".join(reserved_words[:10]))  # Display first 10
print(", ".join(reserved_words[10:20]))
print(", ".join(reserved_words[20:]))

print("\nWrong examples (commented to avoid errors):")
print("# if = 5  # WRONG! 'if' is already used by Python")
print("# for = 'loop'  # WRONG! 'for' is already used by Python")

# ============================================================================
# SECTION 4: SPACES AND INDENTATION
# ============================================================================
print("\n\n4. SPACES AND INDENTATION")
print("-" * 40)

print("""In Python, spaces are IMPORTANT!
It's like stacking building blocks - must be neat and aligned.""")

# Example of correct indentation
print("\nExample of CORRECT indentation:")
print("if True:                      # If true,")
print("    print('This is true')     # ← 4 spaces")
print("    print('Still true')       # ← 4 spaces (must be same!)")
print("else:                         # If false,")
print("    print('This is false')    # ← 4 spaces")

# Example of incorrect indentation
print("\nExample of WRONG indentation (will error):")
print("if True:")
print("    print('This is true')")
print("   print('This is wrong')    # ← Only 3 spaces! ERROR!")
print("    print('This is correct') # ← 4 spaces, but already broken")

print("\nThe analogy:")
print("""• Python is like a neat child
• Every group of commands must be left-aligned
• Use spaces (usually 4) or TAB, but DON'T mix them!""")

# ============================================================================
# SECTION 5: WRITE MULTIPLE LINES IN ONE COMMAND
# ============================================================================
print("\n\n5. WRITE LONG BUT STILL ONE COMMAND")
print("-" * 40)

print("""Sometimes one command is too long.
We can help Python with the \\ (backslash) sign.""")

# Example of line continuation
total = 10 + \
        20 + \
        30

print(f"\n10 + 20 + 30 = {total}")
print("The \\ sign tells Python: 'Continue to the next line!'")

print("\nOr use parentheses (), [], {}:")
fruits = ['apple', 'orange', 'mango',
          'banana', 'grape']

print(f"List of fruits: {fruits}")
print("Python automatically knows to continue to the next line inside parentheses")

# ============================================================================
# SECTION 6: QUOTATION MARKS FOR TEXT
# ============================================================================
print("\n\n6. QUOTATION MARKS FOR WRITING WORDS")
print("-" * 40)

print("""Python accepts 3 types of quotation marks:
1. Single quotes: '...'
2. Double quotes: "..."
3. Triple quotes: '''...''' or \"\"\"...\"\"\"""")

# Examples of using quotation marks
word = 'word'  # Single quotes
sentence = "This is a sentence."  # Double quotes
paragraph = """This is a long paragraph
that can consist of
several lines."""  # Triple quotes

print(f"\n1. One word: {word}")
print(f"2. One sentence: {sentence}")
print(f"3. One paragraph:\n{paragraph}")

print("\nTips:")
print("• Triple quotes can be used for multi-line text")
print("• Choose what's comfortable, but be consistent!")

# ============================================================================
# SECTION 7: COMMENTS - NOTES FOR PROGRAMMERS
# ============================================================================
print("\n\n7. COMMENTS - NOTES FOR HUMANS")
print("-" * 40)

print("""Comments are notes for programmers.
Python ignores comments - they're only for us to read!""")

# This is a single-line comment
print("\nLook at the code above: # This is a comment")

# Comment next to code
name = "John"  # Student name

"""
This is a multi-line
comment.
You can also use triple quotes.
"""

print("""\nComments are useful for:
1. Explaining complex code
2. Taking notes
3. Temporarily disabling code""")

# ============================================================================
# SECTION 8: BLANK LINES AND SEMICOLONS
# ============================================================================
print("\n\n8. BLANK LINES AND SEMICOLONS")
print("-" * 40)

print("Blank lines in Python are like pauses in speech.")
print("Python ignores them, but they make code easier to read.")

print()

print("See, there's a blank line above this!")

# Multiple commands in one line
print("\nMultiple commands in one line (using semicolons):")
import sys; x = 'Python'; sys.stdout.write(x + ' is awesome!\n')

print("""\nBut it's better to:
• One line for one command
• Easier to read and understand""")

# ============================================================================
# SECTION 9: WAITING FOR USER INPUT
# ============================================================================
print("\n\n9. INTERACTING WITH USERS")
print("-" * 40)

print("Python can wait for us to type something.")

# Simple input example
print("\nSimple example (commented to avoid interruption):")
print("# name = input('What is your name? ')")
print("# print(f'Hello, {name}! Nice to meet you!')")

print("\nPress Enter to continue...")
# input("\n\nPress Enter to continue...")

print("\nDone! Python waits for us before continuing.")

# ============================================================================
# SECTION 10: COMMAND GROUPS (SUITES)
# ============================================================================
print("\n\n10. COMMAND GROUPS (SUITES)")
print("-" * 40)

print("""A suite is a group of commands that run together.
Like a cooking recipe - several steps for one goal.""")

# Example of suite with if-elif-else
print("\nExample of suite with if-elif-else:")
number = 7

if number > 10:
    print("Number is greater than 10")  # Part of if suite
elif number > 5:
    print("Number is greater than 5")   # Part of elif suite
else:
    print("Number is 5 or less")        # Part of else suite

print("\nNotice:")
print("• Each condition ends with a colon (:)")
print("• Commands inside are indented (spaces)")
print("• All commands in the group must be aligned")

# ============================================================================
# SECTION 11: COMMAND LINE ARGUMENTS
# ============================================================================
print("\n\n11. COMMAND LINE ARGUMENTS")
print("-" * 40)

print("""We can tell Python what to do
when starting a program from terminal/command prompt.""")

print("\nTry running in terminal:")
print("$ python Basic_Syntax.py")
print("\nOr for Python help:")
print("$ python -h")

print("\nThis shows the available options.")

# ============================================================================
# CONCLUSION
# ============================================================================
print("\n\n" + "=" * 60)
print("CONCLUSION FOR A 5-YEAR-OLD")
print("=" * 60)

print("""
1. Python is like a friend who understands commands
2. print() to speak/print
3. Give good names to variables (don't use reserved words)
4. Be neat! Spaces are important in Python
5. Quotation marks for writing words/sentences
6. Comments (#) for notes (Python doesn't read them)
7. Colon (:) to start a command group
8. input() to ask for user input
9. Python has many tricks - we're just getting started!

Remember: Learning Python is like learning a new language.
Start simple, practice, don't be afraid to make mistakes!
""")

print("=" * 60)
print("HAPPY LEARNING PYTHON!")
print("=" * 60)

# Note for users of this script
print("\n\nNOTE FOR USERS:")
print("1. Save this file as Basic_Syntax.py")
print("2. Run with: python Basic_Syntax.py")
print("3. Modify the code, experiment, and see what happens!")
print("4. Feynman Technique: Try explaining this code in your own words!")