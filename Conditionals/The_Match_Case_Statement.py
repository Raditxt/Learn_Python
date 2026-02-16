# The_Match_Case_Statement.py
"""
Hey there! Today we're going to explore one of Python's newer features:
the `match` and `case` statements (introduced in Python 3.10). It's like
a supercharged version of an if‑elif‑else chain, but much cleaner and more powerful.
Think of it as a "pattern matching" swiss army knife!

We'll explain it like you're five – simple words, lots of examples, and no confusing jargon.
"""

print("=" * 60)
print("THE match case STATEMENT – PYTHON'S PATTERN MATCHING SUPERHERO")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: WHAT IS match case?
# ============================================================================
print("1. WHAT IS match case?")
print("-" * 40)

print("""Imagine you have a remote control with different buttons.
Pressing a button does something different: 'play' starts the movie,
'pause' freezes it, 'stop' turns it off. In programming, we often need
to check a value and do different things based on what it is.

The `match` statement is like that remote control. You give it a value,
and then you list several `case` options. Python looks at the value,
finds the first matching case, and runs the code under that case.

It's similar to an if‑elif‑else chain, but often shorter and more readable.
""")

print("\nHere's the simplest possible example:")

command = 'Hello, World!'
print(f"command = '{command}'")
match command:
    case 'Hello, World!':
        print("   → 'Hello to you too!'")
    case 'Goodbye, World!':
        print("   → 'See you later'")
    case other:
        print("   → 'No match found'")

print("\n👉 The value matched the first case, so that block ran.")

# ============================================================================
# SECTION 2: SYNTAX BASICS – match, case, and the wildcard _
# ============================================================================
print("\n\n2. SYNTAX BASICS – match, case, and the wildcard _")
print("-" * 40)

print("""The structure looks like this:

   match <expression>:
       case <pattern1>:
           <do something>
       case <pattern2>:
           <do something>
       case _:
           <default action>

- The `match` keyword starts the matching.
- Each `case` is a possible pattern.
- The last case with `_` (underscore) is the default – it matches anything.
  It's like `else` in an if‑statement.
- `match` and `case` are "soft keywords" – you can still use them as variable names
  elsewhere in your code, but inside a `match` they have special meaning.
""")

print("\nLet's see a default case in action:")

value = 42
print(f"value = {value}")
match value:
    case 1:
        print("   It's one!")
    case 2:
        print("   It's two!")
    case _:
        print("   It's something else (the default case)")

# ============================================================================
# SECTION 3: MATCHING MULTIPLE THINGS WITH OR PATTERNS (|)
# ============================================================================
print("\n\n3. MATCHING MULTIPLE THINGS WITH OR PATTERNS (|)")
print("-" * 40)

print("""Sometimes you want the same action for several different values.
You can use the `|` operator (like "or") inside a case pattern.""")

status = 404
print(f"status = {status}")
match status:
    case 200 | 201:
        print("   Success! (2xx)")
    case 404 | 410:
        print("   Not found (4xx)")
    case _:
        print("   Other status code")

print("\nHere both 404 and 410 would run the same block.")

# ============================================================================
# SECTION 4: PATTERN MATCHING ON SEQUENCES (LISTS, TUPLES)
# ============================================================================
print("\n\n4. PATTERN MATCHING ON SEQUENCES (LISTS, TUPLES)")
print("-" * 40)

print("""`match` really shines when you work with lists or tuples.
You can match on the structure of the sequence – for example,
a list with exactly one element, or a list starting with a certain word.
""")

def handle_command_v1(command):
    match command.split():
        case ['show']:
            print("   List all files and directories:")
            # (imagine actual code here)
        case ['remove', *files]:
            print(f"   Removing files: {files}")
        case _:
            print("   Command not recognized")

print("\nTesting with different commands:")
handle_command_v1('show')
handle_command_v1('remove file1.txt file2.jpg')
handle_command_v1('list')

print("\nNotice the `*files` in the second pattern – it's like *args in functions.")
print("It captures any number of remaining items into a list called `files`.")

# ============================================================================
# SECTION 5: ADDING GUARDS – EXTRA if CONDITIONS INSIDE A CASE
# ============================================================================
print("\n\n5. ADDING GUARDS – EXTRA if CONDITIONS INSIDE A CASE")
print("-" * 40)

print("""Sometimes a pattern alone isn't enough – you need an extra condition.
You can add an `if` after the pattern, called a "guard". The case matches
only if the pattern matches AND the guard condition is true.""")

def handle_command_v2(command):
    match command.split():
        case ['show']:
            print("   List all files and directories")
        case ['remove' | 'delete', *files] if '--ask' in files:
            # Remove the '--ask' flag from the list before showing
            files_without_flag = [f for f in files if f != '--ask']
            print(f"   Please confirm: Removing files {files_without_flag}")
        case ['remove' | 'delete', *files]:
            print(f"   Removing files {files}")
        case _:
            print("   Command not recognized")

print("\nTest with 'remove --ask file1.txt file2.jpg':")
handle_command_v2('remove --ask file1.txt file2.jpg')

print("\nTest with 'delete file1.txt':")
handle_command_v2('delete file1.txt')

print("\nTest with 'remove file1.txt' (no --ask):")
handle_command_v2('remove file1.txt')

print("\nThe guard (`if '--ask' in files`) makes the second case only match")
print("when the flag is present. The third case handles the same command without the flag.")

# ============================================================================
# SECTION 6: MATCHING OBJECTS AND ATTRIBUTES
# ============================================================================
print("\n\n6. MATCHING OBJECTS AND ATTRIBUTES")
print("-" * 40)

print("""`match` can also match on objects and their attributes.
This is really powerful for object-oriented programming.""")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("   Origin")
        case Point(x=0, y=y):
            print(f"   On the Y axis at y={y}")
        case Point(x=x, y=0):
            print(f"   On the X axis at x={x}")
        case Point(x=x, y=y):
            print(f"   Somewhere at ({x},{y})")
        case _:
            print("   Not a point")

print("\nTesting with different points:")
where_is(Point(0,0))
where_is(Point(0,5))
where_is(Point(3,0))
where_is(Point(2,4))
where_is("not a point")

# ============================================================================
# SECTION 7: WHY USE match case? ADVANTAGES OVER if‑elif‑else
# ============================================================================
print("\n\n7. WHY USE match case? ADVANTAGES OVER if‑elif‑else")
print("-" * 40)

print("""
• ✅ Cleaner syntax – less repetitive code.
• ✅ More readable – the structure is obvious at a glance.
• ✅ Powerful pattern matching – you can match on sequences, objects, and even add guards.
• ✅ You can capture parts of the matched value (like `*files` or `x` in the point example).
• ✅ It's often faster to write and easier to maintain.

For example, compare a long if‑elif‑else chain with a match statement.
The match version is usually much shorter and clearer.
""")

# ============================================================================
# SECTION 8: IMPORTANT WARNINGS
# ============================================================================
print("\n\n8. IMPORTANT WARNINGS")
print("-" * 40)

print("""
⚠️ **Order matters!** Python checks cases from top to bottom, and runs the first match.
   If you put a more general case before a specific one, the specific one will never run.

⚠️ `match` is available only in Python 3.10 and later. If you're using an older version,
   you'll get a syntax error.

⚠️ The patterns are not expressions – you can't put arbitrary expressions inside a pattern.
   For example, `case x+1:` is invalid. Use guards for that.

⚠️ `match` doesn't add new functionality – you could always do the same with if‑elif‑else.
   But it makes your code much nicer!
""")

# ============================================================================
# SECTION 9: SUMMARY
# ============================================================================
print("\n\n9. SUMMARY")
print("-" * 40)

print("""
• `match` lets you compare a value against several patterns.
• Each `case` defines a pattern and a block of code.
• Use `_` as a wildcard to match anything (like `else`).
• Patterns can include literals, sequences, and object attributes.
• Use `|` for multiple alternatives in one case.
• Add a guard (`if condition`) for extra checks.
• Patterns can capture parts of the matched value (e.g., `*files`, `x`, `y`).
• It's a fantastic tool for writing clean, readable conditional code.
""")

print("\n🎯 YOUR TURN! Try these exercises:")
print("""
1. Write a function that takes a string and uses `match` to respond:
   - "hello" → prints "Hi there!"
   - "bye" → prints "See you!"
   - anything else → prints "I don't understand"

2. Create a function that accepts a list of numbers and matches:
   - an empty list → "Empty"
   - a list with one number → "Single: <number>"
   - a list with two numbers → "Pair: <first> and <second>"
   - any longer list → "Long list"

3. Write a class `Shape` with subclasses `Circle(radius)` and `Rectangle(width, height)`.
   Use `match` in a function to compute area differently for each shape.

4. Experiment with guards: write a match that checks a number and prints
   "small positive" if it's between 1 and 10, "big positive" if >10, etc.
""")

print("\n" + "=" * 60)
print("SAVE AS: The_Match_Case_Statement.py")
print("RUN WITH: python The_Match_Case_Statement.py")
print("=" * 60)