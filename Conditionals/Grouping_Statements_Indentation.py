"""
Hey there! Let's talk about how Python groups statements together.
Imagine you're making a decision: "If it's sunny, I will:
   • Mow the lawn
   • Weed the garden
   • Walk the dog"
You want to do ALL these things if the condition is true.
In programming, we need a way to group multiple statements into one block.

Today we'll learn how Python uses indentation to create blocks – it's simple and clean!
"""

print("=" * 60)
print("GROUPING STATEMENTS: INDENTATION AND BLOCKS")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: WHY DO WE NEED BLOCKS?
# ============================================================================
print("1. WHY DO WE NEED BLOCKS?")
print("-" * 40)

print("""When you write an if statement, you often want to do MORE THAN ONE THING
if the condition is true. For example:

   If the weather is nice:
       Mow the lawn
       Weed the garden
       Walk the dog

You wouldn't want to stop after just one task – you want ALL of them done!
In Python, we group those tasks into a BLOCK.""")

print("\nA block is like a to‑do list that Python runs all at once when the condition is true.")
print("If the condition is false, the whole block is skipped – nothing inside happens.")

# ============================================================================
# SECTION 2: PYTHON'S WAY – INDENTATION IS THE KEY
# ============================================================================
print("\n\n2. PYTHON'S WAY – INDENTATION IS THE KEY")
print("-" * 40)

print("""Python uses a special rule called the 'off‑side rule' (from football!).
It means: statements that are indented to the SAME level belong to the same block.""")

print("\nHere's what a block looks like in Python:")
print("""
   if <condition>:
       <statement 1>   # all these are
       <statement 2>   # indented the same
       <statement 3>   # amount (usually 4 spaces)
   <next statement>    # back to normal indentation
""")

print("The colon `:` at the end of the `if` line tells Python: 'A block is coming!'")
print("Then everything indented is part of that block.")

# ============================================================================
# SECTION 3: SIMPLE EXAMPLE – MULTIPLE ACTIONS
# ============================================================================
print("\n\n3. SIMPLE EXAMPLE – MULTIPLE ACTIONS")
print("-" * 40)

print("Let's write a short program that checks if it's sunny and then does three things.")

# Simulating a script (we'll just print the actions)
weather = "sunny"   # try changing to "rainy" to see the block skipped

print(f"Weather = '{weather}'")
print("\nCode:")
print("""
if weather == 'sunny':
    print("Mow the lawn")
    print("Weed the garden")
    print("Walk the dog")
print("Done for the day!")
""")

print("\nOutput:")
if weather == 'sunny':
    print("Mow the lawn")
    print("Weed the garden")
    print("Walk the dog")
print("Done for the day!")

print("\nNotice that all three indented prints happened because the condition was true.")
print("If weather were 'rainy', nothing inside would print, and we'd go straight to 'Done for the day!'.")

# ============================================================================
# SECTION 4: HOW INDENTATION WORKS – SPACES, NOT BRACES
# ============================================================================
print("\n\n4. HOW INDENTATION WORKS – SPACES, NOT BRACES")
print("-" * 40)

print("""In many other languages (like C, Java, Perl), blocks are marked with curly braces {}:

   if (condition) {
       statement1;
       statement2;
   }

Python doesn't use braces – it uses INDENTATION.
This means you MUST be consistent with your indentation.""")

print("\n✅ Good indentation:")
print("""
if x > 0:
    print("Positive")
    print("Great!")
""")

print("❌ Bad indentation (will cause an error):")
print("""
if x > 0:
    print("Positive")
      print("Great!")   # ← different indentation level
""")

print("\n💡 Tip: Always use 4 spaces for each indentation level.")
print("   Don't mix tabs and spaces – Python gets confused!")

# ============================================================================
# SECTION 5: NESTED BLOCKS – BLOCKS INSIDE BLOCKS
# ============================================================================
print("\n\n5. NESTED BLOCKS – BLOCKS INSIDE BLOCKS")
print("-" * 40)

print("""You can put an if statement inside another if. That's called nesting.
Each inner block is indented further.""")

print("\nExample:")
print("""
if 'foo' in ['foo', 'bar', 'baz']:
    print("Outer condition is true")
    if 10 > 20:
        print("Inner condition 1")   # won't run
    print("Between inner conditions")
    if 10 < 20:
        print("Inner condition 2")   # will run
    print("End of outer condition")
print("After outer condition")
""")

print("\nOutput:")
if 'foo' in ['foo', 'bar', 'baz']:
    print("Outer condition is true")
    if 10 > 20:
        print("Inner condition 1")
    print("Between inner conditions")
    if 10 < 20:
        print("Inner condition 2")
    print("End of outer condition")
print("After outer condition")

print("\nSee how each indentation level creates a new block.")
print("When you 'outdent' (go back to previous indentation), you end the block.")

# ============================================================================
# SECTION 6: WHAT ABOUT OTHER LANGUAGES? (CURIOSITY SECTION)
# ============================================================================
print("\n\n6. WHAT ABOUT OTHER LANGUAGES? (CURIOSITY SECTION)")
print("-" * 40)

print("""Python isn't the only way to do blocks. Let's peek at how other languages do it:""")

print("\n🔹 Curly braces (C, C++, Java, JavaScript, Perl):")
print("""
if (condition) {
    statement1;
    statement2;
}
""")

print("🔹 Keywords (Pascal, Ada):")
print("""
if condition then
begin
    statement1;
    statement2;
end;
""")

print("🔹 Indentation (Python, Haskell, CoffeeScript):")
print("""
if condition:
    statement1
    statement2
""")

print("\nWhich is better? It's a matter of taste. Python's way is clean and forces you")
print("to write readable code. No mismatched braces – what you see is what you get!")

# ============================================================================
# SECTION 7: PROS AND CONS OF INDENTATION‑BASED BLOCKS
# ============================================================================
print("\n\n7. PROS AND CONS OF INDENTATION‑BASED BLOCKS")
print("-" * 40)

print("👍 PROS:")
print("   • Clean, concise, and consistent.")
print("   • No mismatched braces – indentation is part of the syntax.")
print("   • Forces you to write readable, well‑formatted code.")
print("   • Virtually impossible to have misleading indentation (code always matches structure).")

print("\n👎 CONS:")
print("   • Some people don't like being forced into a specific style.")
print("   • Mixing tabs and spaces can cause hard‑to‑spot errors.")
print("   • Copy‑pasting code can mess up indentation if you're not careful.")

print("\n💡 The Python community has settled on using 4 spaces per level.")
print("   Most editors can be configured to insert spaces when you press Tab – do it!")

# ============================================================================
# SECTION 8: SUMMARY AND PRACTICE
# ============================================================================
print("\n\n8. SUMMARY AND PRACTICE")
print("-" * 40)

print("""
• Blocks group multiple statements together.
• In Python, blocks are defined by indentation (off‑side rule).
• All statements indented the same amount belong to the same block.
• The colon `:` introduces a new block.
• Nested blocks are created by further indentation.
• End a block by outdenting (going back to previous indentation).
• This makes Python code clean and readable – no curly braces needed!
""")

print("\n🎯 YOUR TURN! Try these exercises:")
print("""
1. Write a program that asks the user for a number.
   If it's positive, print "Positive", then print its square.
   (Both prints should be in the same block.)

2. Modify the program: if the number is positive, also check if it's even.
   If it's even, print "Even". (This requires nesting!)

3. Experiment with indentation – what happens if you indent one line differently?
   (Try it in a Python file, not in this script, to see the error.)
""")

print("\n" + "=" * 60)
print("SAVE AS: Grouping_Statements_Indentation_and_Blocks.py")
print("RUN WITH: python Grouping_Statements_Indentation_and_Blocks.py")
print("=" * 60)

