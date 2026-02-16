"""
Hey there! Let's talk about conditionals in Python.
Imagine you're making decisions in real life:
   "If it's raining, I'll take an umbrella; otherwise, I'll wear sunglasses."
In programming, conditionals let your code make decisions based on certain conditions.
Today, we'll break down the if statement and its friends step by step,
using simple language and plenty of examples.

This script follows the Feynman Technique – explaining complex ideas as if to a 5‑year‑old.
"""

print("=" * 60)
print("UNDERSTANDING CONDITIONALS IN PYTHON")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: THE SIMPLEST DECISION – THE if STATEMENT
# ============================================================================
print("1. THE SIMPLEST DECISION: THE if STATEMENT")
print("-" * 40)

print("""The most basic conditional in Python is the if statement.
It looks like this:

   if <condition>:
       <do something>

- <condition> is an expression that Python evaluates as either True or False.
  (e.g., x > 5, name == "Alice", or even just a variable)
- <do something> is the code that runs ONLY if the condition is True.
  That code MUST be indented (usually four spaces) so Python knows it belongs to the if.
- The colon : at the end of the condition line is REQUIRED – don't forget it!

How it works:
• If the condition is True, the indented block runs.
• If the condition is False, Python skips that block and moves on.
""")

print("\nLet's see some examples (imagine you're typing these in Python):\n")

print(">>> x = 0")
print(">>> y = 5")
print(">>> if x < y:      # True")
print("...     print('yes')")
print("...")
print("yes\n")

print(">>> if y < x:      # False")
print("...     print('yes')")
print("...")
print("# (nothing prints)\n")

print(">>> if x:          # 0 is considered False")
print("...     print('yes')")
print("...")
print("# (nothing)\n")

print(">>> if y:          # 5 is considered True")
print("...     print('yes')")
print("...")
print("yes\n")

print(">>> if x or y:     # True because y is True")
print("...     print('yes')")
print("...")
print("yes\n")

print(">>> if x and y:    # False because x is False")
print("...     print('yes')")
print("...")
print("# (nothing)\n")

print(">>> if 'aul' in 'grault':   # True")
print("...     print('yes')")
print("...")
print("yes\n")

print(">>> if 'quux' in ['foo', 'bar', 'baz']:   # False")
print("...     print('yes')")
print("...")
print("# (nothing)")

print("\n💡 Tip for beginners: If you're typing these in an interactive Python shell,")
print("   after typing print('yes') and pressing Enter, nothing happens immediately.")
print("   That's because Python is waiting for you to finish the block. Just press")
print("   Enter again on a blank line, and it will run.\n")

# ============================================================================
# SECTION 2: TRUTHY AND FALSY – WHAT DOES "TRUE" MEAN?
# ============================================================================
print("\n2. TRUTHY AND FALSY – WHAT DOES 'TRUE' MEAN?")
print("-" * 40)

print("""Python doesn't just work with the booleans True and False.
Many values are considered truthy (treated as True) or falsy (treated as False)
when used in a condition.

Falsy values (they act like False):
   • None
   • False
   • zero (0, 0.0)
   • empty collections: "" (empty string), [] (empty list), {} (empty dict), set(), range(0)

Truthy values (everything else):
   • non‑zero numbers
   • non‑empty strings, lists, tuples, dictionaries, etc.
   • True itself

That's why in the examples above, if x: with x = 0 was false, but if y: with y = 5 was true.
""")

print("\nQuick check:")
print("   bool(0)       →", bool(0))
print("   bool(5)       →", bool(5))
print("   bool('')      →", bool(''))
print("   bool('hello') →", bool('hello'))
print("   bool([])      →", bool([]))
print("   bool([1,2])   →", bool([1,2]))

# ============================================================================
# SECTION 3: ADDING AN ALTERNATIVE – THE else CLAUSE
# ============================================================================
print("\n\n3. ADDING AN ALTERNATIVE: THE else CLAUSE")
print("-" * 40)

print("""Sometimes you want to do one thing if a condition is true,
and a different thing if it's false. That's where else comes in.

   if <condition>:
       <do this when True>
   else:
       <do this when False>

The else block runs only when the condition is false. It doesn't need a condition
of its own – it's the "otherwise" part.
""")

print("\nExample:")
print("   temperature = 25")
print("   if temperature > 30:")
print("       print(\"It's hot! Let's go swimming.\")")
print("   else:")
print("       print(\"It's not too hot. Let's go for a walk.\")")
print("\nOutput:")
temperature = 25
if temperature > 30:
    print("It's hot! Let's go swimming.")
else:
    print("It's not too hot. Let's go for a walk.")

print("\nIf temperature were 35, you'd see the first message. With 25, you see the second.")

# ============================================================================
# SECTION 4: MULTIPLE PATHS – THE elif CLAUSE
# ============================================================================
print("\n\n4. MULTIPLE PATHS: THE elif CLAUSE")
print("-" * 40)

print("""What if you have more than two possibilities? You can chain conditions using elif
(short for "else if").

   if <condition1>:
       <do thing 1>
   elif <condition2>:
       <do thing 2>
   elif <condition3>:
       <do thing 3>
   else:
       <do if none of the above are true>

Python checks each condition in order. As soon as one is true, it runs that block
and skips the rest. The else at the end is optional – it catches any leftover case.
""")

print("\nClassic example – grading system:")
print("""
   score = 85
   if score >= 90:
       grade = 'A'
   elif score >= 80:
       grade = 'B'
   elif score >= 70:
       grade = 'C'
   elif score >= 60:
       grade = 'D'
   else:
       grade = 'F'
   print(f"Your grade is {grade}")
""")

score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"   → Your grade is {grade}")

print("\nNotice that once score >= 80 is true, Python doesn't check the later elifs –")
print("   that's why 85 gives a B, not a C.")

# ============================================================================
# SECTION 5: NESTING CONDITIONALS
# ============================================================================
print("\n\n5. NESTING CONDITIONALS")
print("-" * 40)

print("""You can put an if statement inside another if statement. This is called nesting.

   age = 20
   has_license = True
   if age >= 18:
       print("You are old enough to drive.")
       if has_license:
           print("And you have a license – you can drive!")
       else:
           print("But you don't have a license yet.")
   else:
       print("You are too young to drive.")
""")

age = 20
has_license = True
if age >= 18:
    print("You are old enough to drive.")
    if has_license:
        print("And you have a license – you can drive!")
    else:
        print("But you don't have a license yet.")
else:
    print("You are too young to drive.")

print("\nBe careful with nesting – too many levels can make your code hard to read.")
print("Sometimes you can avoid deep nesting by using logical operators (and, or, not).")

# ============================================================================
# SECTION 6: COMMON PITFALLS AND BEST PRACTICES
# ============================================================================
print("\n\n6. COMMON PITFALLS AND BEST PRACTICES")
print("-" * 40)

print("""🔴 Don't forget the colon : after the condition. It's a common syntax error.
🔴 Indentation matters! All code inside a block must be indented the same amount.
   Mixing tabs and spaces can cause weird errors – stick to four spaces.
🔴 Parentheses are optional around the condition, unlike in some languages.
   But you can use them to make complex conditions clearer.
🔴 Use elif, not nested if, when you're checking mutually exclusive conditions – it's cleaner.
🔴 Avoid unnecessary if statements when a boolean expression is enough.
   Instead of:
       if x > 5:
           return True
       else:
           return False
   just write:
       return x > 5
""")

print("\nExample of a cleaner condition:")
print("   x = 10")
print("   is_big = x > 5   # directly assigns the boolean result")
x = 10
is_big = x > 5
print(f"   is_big = {is_big}")

# ============================================================================
# SECTION 7: SUMMARY
# ============================================================================
print("\n\n7. SUMMARY")
print("-" * 40)

print("""
• The if statement lets your code make decisions.
• else handles the "otherwise" case.
• elif chains multiple conditions.
• Indentation defines blocks.
• Values are considered truthy or falsy – everything counts as True except
  None, False, zero, and empty collections.

Now you know the basics of conditionals! Practice by writing small programs
that make decisions – like a simple number guesser, or a program that tells you
what to wear based on the weather. Happy coding!
""")

print("\n" + "=" * 60)
print("SAVE AS: Understanding_Conditionals.py")
print("RUN WITH: python Understanding_Conditionals.py")
print("=" * 60)

# Optional: interactive exercise reminder
print("\n\n💡 Want to practice? Try writing a program that asks the user for their age")
print("   and prints whether they are a child (<12), teen (13-19), adult (20-64), or senior (65+).")