"""
Hey there! Now that you know how to make simple decisions with if,
let's add more options. Sometimes you want to do one thing if a condition is true,
and a different thing if it's false – that's where else comes in.
And if you have many possibilities, elif (else‑if) lets you check them in order.

We'll keep it super simple – like explaining to a 5‑year‑old!
"""

print("=" * 60)
print("THE else AND elif CLAUSES – MORE THAN ONE PATH")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: THE else CLAUSE – THE "OTHERWISE" PATH
# ============================================================================
print("1. THE else CLAUSE – THE 'OTHERWISE' PATH")
print("-" * 40)

print("""Sometimes you want to do one thing if a condition is true,
and a completely different thing if it's false.
That's exactly what else does.

Syntax:
   if <condition>:
       <do this when True>
   else:
       <do this when False>

The else block runs only when the condition is false.
No condition needed – it's the "otherwise" part.
""")

print("\nLet's see it in action:")

x = 20
print(f"x = {x}")
if x < 50:
    print("   (first suite) x is small")
else:
    print("   (second suite) x is large")
print("   (after the if-else)")

print("\nNow change x to 120:")
x = 120
if x < 50:
    print("   (first suite) x is small")
else:
    print("   (second suite) x is large")
print("   (after the if-else)")

print("\n👉 Only ONE of the two blocks runs, then execution continues afterward.")

# ============================================================================
# SECTION 2: THE elif CLAUSE – CHECKING MULTIPLE CONDITIONS
# ============================================================================
print("\n\n2. THE elif CLAUSE – CHECKING MULTIPLE CONDITIONS")
print("-" * 40)

print("""What if you have more than two possibilities?
For example, greeting different people by name.
You can chain conditions using elif (short for "else if").

Syntax:
   if <condition1>:
       <do thing 1>
   elif <condition2>:
       <do thing 2>
   elif <condition3>:
       <do thing 3>
   ...
   else:
       <do if none of the above are true>

Python checks each condition in order.
As soon as one is true, it runs that block and skips the rest.
The final else is optional – it catches any leftover case.
""")

print("\nExample – greeting by name:")
name = 'Joe'
print(f"name = '{name}'")
if name == 'Fred':
    print("   Hello Fred")
elif name == 'Xander':
    print("   Hello Xander")
elif name == 'Joe':
    print("   Hello Joe")
elif name == 'Arnold':
    print("   Hello Arnold")
else:
    print("   I don't know who you are!")
print("   Done.")

print("\nIf name were 'Arnold', it would print 'Hello Arnold'.")
print("If name were 'Rick', it would print the else message.")

# ============================================================================
# SECTION 3: SHORT‑CIRCUIT EVALUATION – STOPPING EARLY
# ============================================================================
print("\n\n3. SHORT‑CIRCUIT EVALUATION – STOPPING EARLY")
print("-" * 40)

print("""Just like with and/or, Python stops checking conditions
as soon as it finds one that's true. This is called short‑circuit evaluation.
It means that later conditions might never be evaluated – which can be important
if they would cause an error!""")

print("\nWatch this:")

print("""
if 'a' in 'bar':
    print('foo')
elif 1/0:                 # division by zero – would crash if evaluated!
    print("This won't happen")
elif var:                 # var is not defined – would also crash!
    print("This won't either")
""")

print("\nOutput:")
if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")

print("\nBecause the first condition was true, Python never looked at the others.")
print("So even though 1/0 would normally crash, it's safely skipped.")

# ============================================================================
# SECTION 4: A MORE PYTHONIC WAY – USING DICTIONARIES
# ============================================================================
print("\n\n4. A MORE PYTHONIC WAY – USING DICTIONARIES")
print("-" * 40)

print("""Long if/elif/else chains can get messy, especially when each branch
just returns a simple value. Python offers cleaner alternatives.
One of them is using a dictionary with .get().

For example, our name greeting could be rewritten like this:
""")

names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}

print("names =", names)
print("\nprint(names.get('Joe', \"I don't know who you are!\"))")
print("   →", names.get('Joe', "I don't know who you are!"))

print("\nprint(names.get('Rick', \"I don't know who you are!\"))")
print("   →", names.get('Rick', "I don't know who you are!"))

print("\nThis is often shorter and easier to read.")

# ============================================================================
# SECTION 5: COMMON PITFALLS AND TIPS
# ============================================================================
print("\n\n5. COMMON PITFALLS AND TIPS")
print("-" * 40)

print("""
🔴 Don't forget the colon `:` after if, elif, and else.
🔴 Indentation matters! All statements in a block must be indented the same.
🔴 You can have only one else clause, and it must come last.
🔴 elif is short for "else if" – it's one word, no space.
🔴 If you have many conditions, consider using a dictionary or a match statement (Python 3.10+).
""")

# ============================================================================
# SECTION 6: SUMMARY
# ============================================================================
print("\n\n6. SUMMARY")
print("-" * 40)

print("""
• else gives you an alternative path when the if condition is false.
• elif lets you check multiple conditions in order.
• Python stops checking after the first true condition (short‑circuit).
• You can use dictionaries to replace simple if/elif/else chains.
• Indentation and colons are your friends – use them correctly!
""")

print("\n🎯 YOUR TURN! Try these exercises:")
print("""
1. Write a program that asks the user for a number and prints:
   - "positive" if > 0
   - "negative" if < 0
   - "zero" if == 0
   (Use if/elif/else.)

2. Write a program that asks for a day of the week (as a string) and prints:
   - "Weekend" if it's "Saturday" or "Sunday"
   - "Weekday" otherwise
   (Use elif or a dictionary.)

3. Experiment with short‑circuit: write an if/elif chain where the second
   condition contains an error, but the first condition is true. See that no error occurs.
""")

print("\n" + "=" * 60)
print("SAVE AS: Else_and_Elif_Clauses.py")
print("RUN WITH: python Else_and_Elif_Clauses.py")
print("=" * 60)

