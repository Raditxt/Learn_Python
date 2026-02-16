"""
Hey there! So far we've always written if statements with the condition on one line
and the action indented on the next line. But did you know you can also write a whole
if statement on a single line? Let's explore this compact style and when it might
(and might not) be a good idea.

We'll keep it super simple – like explaining to a 5‑year‑old!
"""

print("=" * 60)
print("ONE‑LINE if STATEMENTS – WHEN EVERYTHING FITS ON ONE LINE")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: THE BASIC ONE‑LINE if
# ============================================================================
print("1. THE BASIC ONE‑LINE if")
print("-" * 40)

print("""Normally we write:

   if <condition>:
       <statement>

But Python also allows this on one line:

   if <condition>: <statement>

It does exactly the same thing – runs <statement> only if <condition> is true.
""")

print("\nExample:")
print(">>> if 'f' in 'foo': print('Found!')")
if 'f' in 'foo': print('Found!')
print("   (prints 'Found!')")

print("\n>>> if 'z' in 'foo': print('Found!')")
if 'z' in 'foo': print('Found!')
print("   (nothing prints)")

# ============================================================================
# SECTION 2: MULTIPLE STATEMENTS ON ONE LINE (USING SEMICOLONS)
# ============================================================================
print("\n\n2. MULTIPLE STATEMENTS ON ONE LINE")
print("-" * 40)

print("""You can even put several statements after the colon, separated by semicolons.
Python treats them all as one block – they all run if the condition is true,
or none run if it's false.

   if <condition>: <stmt1>; <stmt2>; ...; <stmtN>
""")

print("\nExample:")
print(">>> if 'f' in 'foo': print('1'); print('2'); print('3')")
if 'f' in 'foo': print('1'); print('2'); print('3')
print("   → prints 1, 2, 3")

print("\n>>> if 'z' in 'foo': print('1'); print('2'); print('3')")
if 'z' in 'foo': print('1'); print('2'); print('3')
print("   → nothing prints")

print("\nNotice that the semicolons bind more tightly than the colon.")
print("All statements are part of the same suite – they stand or fall together.")

# ============================================================================
# SECTION 3: ONE‑LINE elif AND else
# ============================================================================
print("\n\n3. ONE‑LINE elif AND else")
print("-" * 40)

print("""You can also write elif and else clauses on one line, with multiple statements:""")

print("\nExample with x = 2:")
x = 2
print(">>> x = 2")
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
print("   → prints qux, quux")

print("\nExample with x = 3:")
x = 3
print(">>> x = 3")
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
print("   → prints corge, grault")

# ============================================================================
# SECTION 4: READABILITY – THE DOWNSIDE
# ============================================================================
print("\n\n4. READABILITY – THE DOWNSIDE")
print("-" * 40)

print("""While Python lets you do this, it's usually NOT recommended.
PEP 8 (Python's style guide) specifically advises against writing multiple
statements on one line. It can make your code harder to read and understand.

Compare these two versions of the same logic:""")

print("\n🔹 One‑line style (harder to read):")
print("""
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
""")

print("\n🔹 Traditional style (easier to read):")
print("""
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')
""")

print("Most people find the second version much clearer at a glance.")

# ============================================================================
# SECTION 5: WHEN ONE‑LINE if MIGHT BE OKAY
# ============================================================================
print("\n\n5. WHEN ONE‑LINE if MIGHT BE OKAY")
print("-" * 40)

print("""For very simple, one‑statement conditions, a one‑liner can be acceptable.
For example, a quick debugging flag:""")

debugging = True
print("debugging = True")
if debugging: print("About to call function foo()")
print("foo()  # (imaginary function call)")

print("\nThis is short and clear – it probably won't confuse anyone.")
print("But once you have multiple statements or complex conditions, spread them out!")

# ============================================================================
# SECTION 6: SUMMARY
# ============================================================================
print("\n\n6. SUMMARY")
print("-" * 40)

print("""
• You can write an if (and elif/else) on one line.
• Use semicolons to separate multiple statements in the same block.
• All statements after the colon are executed together if the condition is true.
• This works, but it's often less readable.
• PEP 8 discourages multiple statements on one line.
• Reserve one‑liners for very simple cases (like a single print for debugging).

Now you know the trick – use it wisely!
""")

print("\n🎯 YOUR TURN! Try these exercises:")
print("""
1. Write a one‑line if that checks if a number is even and prints 'even'.
2. Write a one‑line if‑else that prints 'even' or 'odd' (hint: you can use a conditional expression, but that's another topic).
3. Experiment: try putting an assignment inside a one‑line if, like `if x > 0: y = 10`. Does it work? (Yes, it does.)
4. Convert a multi‑line if/elif/else into one‑line style and see how readable it is (or isn't).
""")

print("\n" + "=" * 60)
print("SAVE AS: One_Line_if_Statements.py")
print("RUN WITH: python One_Line_if_Statements.py")
print("=" * 60)