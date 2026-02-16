# The_Python_pass_Statement.py
"""
Hey there! Today we're going to talk about Python's `pass` statement.
It's a tiny keyword that does absolutely nothing – but sometimes doing nothing
is exactly what you need! Let's find out why.

We'll explain it like you're five – simple words, lots of examples, and no confusing jargon.
"""

print("=" * 60)
print("THE PYTHON pass STATEMENT – DOING NOTHING, PERFECTLY")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: THE PROBLEM – PYTHON NEEDS SOMETHING INSIDE BLOCKS
# ============================================================================
print("1. THE PROBLEM – PYTHON NEEDS SOMETHING INSIDE BLOCKS")
print("-" * 40)

print("""In many other languages (like C or Perl), you can write an empty block
using curly braces, like this:

   if (x) {
       // nothing here
   }

That's a valid block that does nothing. Python doesn't use braces – it uses indentation.
And you can't have an indented block with nothing in it. Python would complain.
""")

print("\nLet's see what happens if we try to write an empty block in Python:")
print("""
   if True:

   print('foo')
""")

print("\nIf you run that, Python says:")
print("   IndentationError: expected an indented block")
print("It's expecting something after the colon, but found nothing.")

# ============================================================================
# SECTION 2: THE SOLUTION – pass TO THE RESCUE
# ============================================================================
print("\n\n2. THE SOLUTION – pass TO THE RESCUE")
print("-" * 40)

print("""The `pass` statement is Python's way of saying: "I'm not doing anything here,
but that's okay – just move along." It's a placeholder that satisfies Python's
need for a statement, but does absolutely nothing when executed.""")

print("\nHere's the same code with `pass`:")

print("""
   if True:
       pass

   print('foo')
""")

print("\nNow it runs without error, and prints 'foo'.")
print("The `pass` is like a silent nod – it does nothing, but Python accepts it.")

# Demonstrate it live
print("\n👉 Let's try it right now:")
if True:
    pass
print("   (The pass did nothing, and now we print this line.)")

# ============================================================================
# SECTION 3: WHERE CAN YOU USE pass?
# ============================================================================
print("\n\n3. WHERE CAN YOU USE pass?")
print("-" * 40)

print("""You can use `pass` anywhere Python expects a statement but you don't want to do anything.
Common places include:

   • Inside an `if` block (as we saw)
   • Inside a function definition (you haven't written the code yet)
   • Inside a class definition (placeholder class)
   • Inside a loop (like a busy-wait that does nothing)
""")

print("\n🔹 Function placeholder:")
print("""
   def my_function():
       pass   # I'll write the code later
""")

def my_function():
    pass   # I'll write the code later
print("   my_function defined, does nothing when called.")

print("\n🔹 Class placeholder:")
print("""
   class MyClass:
       pass   # empty class for now
""")

class MyClass:
    pass   # empty class for now
print("   MyClass defined, can be instantiated but has no methods.")

print("\n🔹 Loop placeholder (e.g., waiting for something):")
print("""
   while condition_not_met:
       pass   # just wait, do nothing
   # but be careful – this will busy-loop!
""")

# ============================================================================
# SECTION 4: pass IS DIFFERENT FROM COMMENTS
# ============================================================================
print("\n\n4. pass IS DIFFERENT FROM COMMENTS")
print("-" * 40)

print("""You might think: "Why not just write a comment?" Comments are ignored by Python,
but they don't count as statements. If you write:

   if True:
       # TODO: do something later

Python still sees an empty block after the comment (the comment doesn't count),
so you'll get the same IndentationError. You need `pass` to actually fill the block.
""")

print("\n✅ Correct:")
print("""
   if True:
       pass   # placeholder
""")

print("\n❌ Incorrect (still empty):")
print("""
   if True:
       # just a comment
""")
print("   → This still causes an IndentationError.")

# ============================================================================
# SECTION 5: SUMMARY
# ============================================================================
print("\n\n5. SUMMARY")
print("-" * 40)

print("""
• `pass` is a statement that does absolutely nothing.
• It's used as a placeholder where Python requires a statement but you don't want any action.
• Common uses: stubbing out functions, classes, or conditional blocks.
• Without `pass`, an empty indented block would cause an IndentationError.
• `pass` is not a comment – comments don't fill the block requirement.

Now you know how to do nothing – the Python way!
""")

print("\n🎯 YOUR TURN! Try these exercises:")
print("""
1. Write a function called `todo` that does nothing (use `pass`).
2. Create an `if` statement that checks if a number is positive, and if so, do nothing (use `pass`).
3. Define an empty class called `Placeholder`.
4. Try removing the `pass` from one of your blocks and see the error.
""")

print("\n" + "=" * 60)
print("SAVE AS: The_Python_pass_Statement.py")
print("RUN WITH: python The_Python_pass_Statement.py")
print("=" * 60)