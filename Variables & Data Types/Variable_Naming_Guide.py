# variable_naming_guide.py
"""
This script explains how to name variables in Python in a simple way,
understandable even for a 5-year-old (using the Feynman Technique).

Feynman Technique: Explaining complex concepts using simple language,
analogies, and concrete examples.
"""

print("=" * 60)
print("LEARNING TO NAME VARIABLES IN PYTHON")
print("(Like Explaining to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# PART 1: WHY DO VARIABLE NAMES MATTER?
# ============================================================================
print("1. WHY DO VARIABLE NAMES MATTER?")
print("-" * 40)

print("""Variable names are like PET NAMES.
They must be clear, easy to remember, and describe what they are!""")

print("\nThe Analogy:")
print("• Imagine two cats:")
print("  Cat 1 is named: 'x'")
print("  Cat 2 is named: 'WhiteCatBlueEyes'")
print("• Which one is easier to recognize?")

print("\nCode Example:")
print("BAD: x = 25            # What does this mean?")
print("GOOD: temperature = 25 # Oh, the temperature is 25 degrees!")

print("\nA good variable name is:")
print("1. Readable (like reading a storybook)")
print("2. Understandable (you know what it means instantly)")
print("3. Memorable (no guessing games)")

# ============================================================================
# PART 2: BASIC NAMING RULES
# ============================================================================
print("\n\n2. BASIC NAMING RULES")
print("-" * 40)

print("""Python has simple rules for names.
Like the rules of a playground!""")

# Rule 1: Letters and underscores allowed
print("\nRULE 1: You can use letters and underscores (_)")
name = "Buddy"           # ✅ Allowed
_name = "Buddy"          # ✅ Allowed (starting with underscore)
full_name = "Buddy Smith" # ✅ Allowed (using underscore)

print(f"Examples: name = '{name}'")
print(f"          _name = '{_name}'")
print(f"          full_name = '{full_name}'")

# Rule 2: Numbers allowed, but NOT at the start
print("\nRULE 2: Numbers are okay, but NEVER at the beginning")
name1 = "Buddy1"         # ✅ Allowed (number at the end)
name_1 = "Buddy_1"       # ✅ Allowed (number after underscore)
# 1name = "Buddy"        # ❌ ERROR! Cannot start with a number

print(f"Examples: name1 = '{name1}'")
print(f"          name_1 = '{name_1}'")
print("          # 1name = 'Buddy'  ← ERROR! No numbers at the start")

# Rule 3: No special symbols
print("\nRULE 3: NO special symbols (@, $, %, etc.)")
# email@addr = "b@email.com"  # ❌ ERROR!
# money$ = 100                # ❌ ERROR!
# discount% = 50              # ❌ ERROR!

print("Examples of ERRORS:")
print("• email@addr = '...' ← ERROR! No @ allowed")
print("• money$ = 100       ← ERROR! No $ allowed")
print("• discount% = 50     ← ERROR! No % allowed")

# Rule 4: Python is Case-Sensitive
print("\nRULE 4: Python treats BIG letters and small letters DIFFERENTLY")
Name = "Buddy"
name = "Andy"
NAME = "Charlie"

print(f"Name (Capitalized): '{Name}'")
print(f"name (lowercase):   '{name}'")
print(f"NAME (UPPERCASE):   '{NAME}'")
print("\nNotice: These are THREE DIFFERENT VARIABLES!")

# ============================================================================
# PART 3: NAMING STYLE - SNAKE CASE
# ============================================================================
print("\n\n3. NAMING STYLE - SNAKE CASE")
print("-" * 40)

print("""In Python, we use SNAKE CASE for variable names.
All lowercase letters, words separated by underscores (_).""")

print("\nWhy is it called 'snake case'?")
print("very_long_variable_name")
print("↑ ↑ ↑ ↑ ↑ ↑ ↑")
print("It looks like a long snake body crawling on the ground!")

print("\nExamples of CORRECT snake case:")
print("• full_name = 'Buddy Smith'")
print("• age_in_years = 8")
print("• height_in_cm = 120.5")
print("• is_login = True")
print("• number_of_apples = 5")

print("\nComparison:")
print("SNAKE CASE (Python):  student_full_name")
print("camelCase (Java):     studentFullName")
print("PascalCase (C#):      StudentFullName")

print("\nTips:")
print("""Snake case is easier to read because:
1. All lowercase (no need to remember which letter is capital)
2. Underscores clearly separate words
3. Great for long descriptive names""")

# ============================================================================
# PART 4: DESCRIPTIVE VS GENERIC NAMES
# ============================================================================
print("\n\n4. DESCRIPTIVE VS GENERIC NAMES")
print("-" * 40)

print("""Choose DESCRIPTIVE names (describes the content).
Don't use GENERIC names that are unclear.""")

print("\n❌ GENERIC NAMES (BAD):")
print("data = [...]       # What data?")
print("value = 10         # What value?")
print("temp = 'Buddy'     # Temporary what?")
print("x = 25             # What is x?")

print("\n✅ DESCRIPTIVE NAMES (GOOD):")
print("student_list = ['Buddy', 'Andy', 'Charlie']")
print("student_age = 10")
print("student_name = 'Buddy'")
print("room_temperature = 25")

print("\nThe Analogy:")
print("""• Generic name = "Stuff in the room"
• Descriptive name = "Harry Potter book on the top shelf"
Which one is easier to find?""")

# ============================================================================
# PART 5: SINGLE-LETTER NAMES
# ============================================================================
print("\n\n5. WHEN CAN WE USE SINGLE LETTERS?")
print("-" * 40)

print("""Generally, avoid single-letter names.
BUT there are exceptions for specific cases.""")

print("\n❌ DO NOT use for normal things:")
print("a = 10            # Unclear, what is a?")
print("n = 'Buddy'       # Unclear, what is n?")

print("\n✅ ALLOWED for Math/Coordinates:")
print("# For coordinates:")
print("x = 10            # x-coordinate")
print("y = 20            # y-coordinate")
print("z = 30            # z-coordinate")

print("\n# For loops (indexes):")
print("for i in range(5):      # i for index")
print("    print(i)")
print("")
print("matrix = [[1,2],[3,4]]")
print("for i in range(2):      # i for rows")
print("    for j in range(2):  # j for columns")
print("        print(matrix[i][j])")

print("\nSummary:")
print("• i, j, k → for index/iteration")
print("• x, y, z → for coordinates")
print("• f, g, h → for math functions")
print("• n → for counts (number)")
print("• Use only if the CONTEXT IS CLEAR!")

# ============================================================================
# PART 6: ABBREVIATIONS - YES OR NO?
# ============================================================================
print("\n\n6. ABBREVIATIONS - YES OR NO?")
print("-" * 40)

print("""Avoid unclear abbreviations.
Only use abbreviations that are COMMONLY UNDERSTOOD.""")

print("\n❌ UNCLEAR ABBREVIATIONS:")
print("cust = 'Buddy'       # Customer? Custom? Custody?")
print("emp = 10             # Employee? Empty? Empire?")
print("doc = 'file.txt'     # Document? Doctor?")

print("\n✅ COMMON ABBREVIATIONS:")
print("msg = 'Hello'        # Message (very common)")
print("cmd = 'run.py'       # Command (very common)")
print("info = 'data'        # Information (very common)")
print("temp = 25            # Temperature/temporary (context matters)")

print("\n✅ BETTER TO USE FULL NAMES:")
print("customer = 'Buddy'")
print("employee_count = 10")
print("document = 'file.txt'")

print("\nTest: Ask yourself:")
print("1. Will other people understand this immediately?")
print("2. Will I remember this tomorrow?")
print("3. Is this a universally known short form?")

# ============================================================================
# PART 7: NAMES FOR LISTS, DICTS, AND TUPLES
# ============================================================================
print("\n\n7. NAMES FOR LISTS, DICTS, AND TUPLES")
print("-" * 40)

print("""Give names that match the data type.
Usually: PLURAL for lists/dicts, SINGULAR for tuples representing one thing.""")

# List: Use Plural
print("\n✅ LIST: Use PLURAL names:")
fruits = ["apple", "orange", "mango"]
students = ["Buddy", "Andy", "Charlie"]
numbers = [1, 2, 3, 4, 5]

print(f"fruits = {fruits}")
print(f"students = {students}")
print(f"numbers = {numbers}")

print("\n❌ DO NOT use singular for lists:")
print("# fruit = ['apple', 'orange']  ← Confusing, sounds like just one")

# Dictionary: Also Plural
print("\n✅ DICTIONARY: Also Plural:")
colors = {"red": "#FF0000", "green": "#00FF00"}
student_scores = {"Buddy": 8, "Andy": 9}

print(f"colors = {colors}")
print(f"student_scores = {student_scores}")

# Tuple: Singular if it represents one entity
print("\n✅ TUPLE: Singular if representing one entity:")
rgb_color = (255, 0, 0)          # One single color value
student_data = ("Buddy", 8, "3A")# Data for ONE student
point = (10, 20)                 # One coordinate point

print(f"rgb_color = {rgb_color}")
print(f"student_data = {student_data}")
print(f"point = {point}")

# ============================================================================
# PART 8: BOOLEAN FLAGS - PREFIXES is_, has_, can_
# ============================================================================
print("\n\n8. BOOLEAN FLAGS - PREFIXES is_, has_, can_")
print("-" * 40)

print("""For boolean variables (True/False),
use a prefix that asks a question.""")

print("\n✅ USE CLEAR PREFIXES:")
is_login = True          # Is the user logged in?
has_permission = False   # Does the user have permission?
can_edit = True          # Can the user edit?
should_update = True     # Should the system update?
is_empty = False         # Is the list empty?
is_valid = True          # Is the data valid?

print(f"is_login = {is_login}")
print(f"has_permission = {has_permission}")
print(f"can_edit = {can_edit}")

print("\n❌ WITHOUT CLEAR PREFIXES:")
print("# login = True        ← This is a verb/action, not a state")
print("# permission = False  ← This is a noun, not a state")
print("# edit = True         ← Unclear meaning")

print("\nBenefits of is_, has_, can_:")
print("1. You know instantly it's a Boolean (True/False)")
print("2. You know exactly what it checks")
print("3. Consistent across your code")

# ============================================================================
# PART 9: PRIVATE/PROTECTED VARIABLES (PREFIX _)
# ============================================================================
print("\n\n9. PRIVATE/PROTECTED VARIABLES (PREFIX _)")
print("-" * 40)

print("""Use an underscore at the start (_name) for variables
that should NOT be touched from outside the module/class.""")

print("\n✅ PRIVATE VARIABLES (use _ at start):")
print("_api_key = 'secret123'   # Don't touch from outside!")
print("_config_data = {...}     # For internal use only")
print("_counter = 0             # Internal counter")

print("\n✅ PROTECTED/MANGLED (use __ at start):")
print("__secret_data = 'top secret'  # Very private")

print("\nThe Analogy:")
print("""• Normal Variable = Living Room (Guests are welcome)
• Private Variable (_) = Bedroom (Family only)
• Protected Variable (__) = Locked Safe (Owner only)""")

# ============================================================================
# PART 10: FORBIDDEN NAMES (PYTHON KEYWORDS)
# ============================================================================
print("\n\n10. FORBIDDEN NAMES (PYTHON KEYWORDS)")
print("-" * 40)

print("""Python has special reserved words that
CANNOT be used as variable names.""")

# List of some Python keywords
keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
]

print("\nSome Python Keywords (Do NOT use these as names):")
for i in range(0, len(keywords), 6):
    print("  " + ", ".join(keywords[i:i+6]))

print("\n❌ EXAMPLES OF ERRORS:")
print("# class = 'Math'      ← ERROR! 'class' is a keyword")
print("# if = 10             ← ERROR! 'if' is a keyword")
print("# for = 'loop'        ← ERROR! 'for' is a keyword")

print("\n✅ HOW TO FIX: Add an underscore at the end")
print("class_ = 'Math'       ← Add _ at the end")
print("if_ = 10              ← Add _ at the end")
print("for_ = 'loop'         ← Add _ at the end")

print("\n✅ EVEN BETTER: Choose a different name")
print("course = 'Math'       ← Rename to 'course'")
print("condition = 10        ← Rename to 'condition'")
print("loop_type = 'loop'    ← Rename to 'loop_type'")

# ============================================================================
# PART 11: DO NOT OVERWRITE BUILT-INS
# ============================================================================
print("\n\n11. DO NOT OVERWRITE BUILT-IN PYTHON NAMES")
print("-" * 40)

print("""Don't use the names of Python's built-in functions.
It's like naming your child "Spoon" - very confusing!""")

print("\n❌ DO NOT DO THIS:")
print("list = [1, 2, 3]      # list() is a built-in function")
print("dict = {'a': 1}       # dict() is a built-in function")
print("str = 'hello'         # str() is a built-in function")
print("sum = 10 + 20         # sum() is a built-in function")

print("\nWhat happens if you do?")
print("""
list = [1, 2, 3]          # Now 'list' is your variable
# Later in the code...
# new_list = list(range(5))  ← ERROR! 'list' is not a function anymore!
""")

print("\n✅ DO THIS INSTEAD:")
print("my_list = [1, 2, 3]   # Rename to 'my_list'")
print("my_dict = {'a': 1}    # Rename to 'my_dict'")
print("text = 'hello'        # Rename to 'text'")
print("total = 10 + 20       # Rename to 'total'")

# ============================================================================
# PART 12: COMPLETE EXAMPLE - BEFORE & AFTER
# ============================================================================
print("\n\n12. COMPLETE EXAMPLE - BEFORE & AFTER")
print("-" * 40)

print("Let's look at a simple program:")

print("\n" + "=" * 40)
print("BEFORE (Bad Naming):")
print("=" * 40)
print("""
a = 25
b = 150
c = ['a', 'b', 'c']
d = 0
for i in c:
    if i == 'a':
        d += 1
print(d)
""")
print("# Confusing right? You have to guess what 'a', 'b', and 'd' are.")

print("\n" + "=" * 40)
print("AFTER (Good Naming):")
print("=" * 40)
print("""
room_temp = 25
height_cm = 150
letter_list = ['a', 'b', 'c']
count_of_a = 0

for letter in letter_list:
    if letter == 'a':
        count_of_a += 1
        
print(f"Count of letter 'a': {count_of_a}")
""")

print("\nComparison:")
print("• BEFORE: You have no idea what the code does.")
print("• AFTER: You understand it immediately without comments!")
print("• AFTER: Easier to debug and fix.")

# ============================================================================
# CONCLUSION
# ============================================================================
print("\n\n" + "=" * 60)
print("CONCLUSION: HOW TO NAME VARIABLES")
print("=" * 60)

print("""
MANDATORY RULES:
1. ✅ Allowed: letters, numbers, underscores (_)
2. ❌ Not Allowed: numbers at the start
3. ❌ Not Allowed: symbols (@, $, %, etc.)
4. ❌ Not Allowed: spaces (use underscores)
5. ❌ Not Allowed: Python keywords (if, for, class, etc.)

BEST STYLE (Pythonic):
1. 🐍 Use SNAKE CASE: long_variable_name    
2. 📝 Use DESCRIPTIVE names (not generic)
3. 🔤 Avoid abbreviations (unless very common)
4. 📊 For list/dict: use PLURAL (fruits, users)
5. 🔢 For boolean: use is_, has_, can_ at the start
6. 🔒 For private: use _ at the start
7. 🚫 Don't overwrite built-in names (list, str)

THE GOLDEN RULE:
"Give names that make the code
readable WITHOUT COMMENTS!"

Questions to ask for every variable:
1. Is the meaning clear?
2. Will others understand it?
3. Will I remember it tomorrow?
4. Is it consistent with other code?

Remember: Writing code is like writing a letter.
Make it easy for humans to read, not just machines!
""")

print("=" * 60)
print("CONGRATULATIONS! NOW YOU CAN NAME VARIABLES LIKE A PRO!")
print("=" * 60)

# ============================================================================
# EXERCISE AND QUIZ
# ============================================================================
print("\n\nEXERCISE & QUIZ:")
print("-" * 40)

print("""FIX THE VARIABLE NAMES BELOW:
(Every line has a problem, try to identify and fix it!)""")

print("\nCode with BAD names:")
print("""
1. a = 25
2. 1st_name = 'Buddy'
3. last name = 'Smith'
4. class = '3A'
5. list = [1, 2, 3]
6. islogin = True
7. studentlist = ['Buddy', 'Andy']
8. x = 'Hello World'
9. data = {'a': 1, 'b': 2}
10. for = 'looping'
""")

print("\nCORRECT Answers:")
print("""
1. room_temp = 25          (descriptive name)
2. first_name = 'Buddy'    (cannot start with a number)
3. last_name = 'Smith'     (no spaces allowed)
4. class_name = '3A'       ('class' is a keyword)
5. number_list = [1, 2, 3] (don't overwrite 'list')
6. is_logged_in = True     (use snake_case)
7. students = ['Buddy',..] (snake_case and plural)
8. greeting = 'Hello...'   (descriptive name)
9. data_map = {'a': 1...}  (specific name)
10. loop_type = 'looping'  ('for' is a keyword)
""")

print("\nChallenge for you:")
print("1. Write a simple program with well-named variables.")
print("2. Ask a friend to read the code without explaining it.")
print("3. Ask: 'What does this program do?'")
print("4. If they understand, your variable names are great!")

print("\n" + "=" * 60)
print("SAVE AS: variable_naming_guide.py")
print("RUN WITH: python variable_naming_guide.py")
print("=" * 60)