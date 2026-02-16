"""
Hey there! Today we're going to learn about Python's conditional expression –
also known as the ternary operator. It's a super compact way to make a decision
and get a value in just one line. Think of it as a mini if‑else that gives you a result.

We'll explain it like you're five – simple words, lots of examples, and no confusing jargon.
"""

print("=" * 60)
print("CONDITIONAL EXPRESSIONS – PYTHON'S TERNARY OPERATOR")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: WHAT IS A CONDITIONAL EXPRESSION?
# ============================================================================
print("1. WHAT IS A CONDITIONAL EXPRESSION?")
print("-" * 40)

print("""Imagine you have two snacks: an apple and a cookie.
You want to choose one based on whether you're hungry or just want a treat.
In real life you might say: 'I'll take the apple if I'm hungry, otherwise the cookie.'

Python has a way to write exactly that kind of choice in one line:
   apple if hungry else cookie

In Python terms:
   <value_if_true> if <condition> else <value_if_false>
""")

print("\nLet's see a real example:")

raining = False
print(f"raining = {raining}")
print("print('Let's go to the', 'beach' if not raining else 'library')")
print("   →", end=" ")
print("Let's go to the", 'beach' if not raining else 'library')

raining = True
print(f"\nraining = {raining}")
print("print('Let's go to the', 'beach' if not raining else 'library')")
print("   →", end=" ")
print("Let's go to the", 'beach' if not raining else 'library')

print("\n👉 The condition is evaluated first. If it's True, we get the left value; if False, the right value.")

# ============================================================================
# SECTION 2: USING IT FOR VARIABLE ASSIGNMENT
# ============================================================================
print("\n\n2. USING IT FOR VARIABLE ASSIGNMENT")
print("-" * 40)

print("""A very common use is to assign one of two values to a variable based on a condition.
For example, finding the larger of two numbers:""")

a, b = 10, 20
print(f"a = {a}, b = {b}")
# Traditional way
if a > b:
    m = a
else:
    m = b
print(f"Traditional if/else: m = {m}")

# Ternary way
m = a if a > b else b
print(f"Ternary expression: m = a if a > b else b  →  m = {m}")

print("\nIt's shorter and often clearer for simple cases.")

# ============================================================================
# SECTION 3: CONDITIONAL EXPRESSIONS IN LARGER EXPRESSIONS
# ============================================================================
print("\n\n3. USING IT INSIDE LARGER EXPRESSIONS")
print("-" * 40)

print("""Because it's an expression (it produces a value), you can use it anywhere a value is expected,
like inside a print, a calculation, or even as part of another expression.""")

age = 12
s = 'minor' if age < 21 else 'adult'
print(f"age = {age} → s = 'minor' if age < 21 else 'adult' → s = '{s}'")

print("\nCheck if a word is in a list:")
word = 'qux'
result = 'yes' if word in ['foo', 'bar', 'baz'] else 'no'
print(f"result = 'yes' if '{word}' in ['foo','bar','baz'] else 'no' → '{result}'")

# ============================================================================
# SECTION 4: OPERATOR PRECEDENCE – WHEN TO USE PARENTHESES
# ============================================================================
print("\n\n4. OPERATOR PRECEDENCE – WHEN TO USE PARENTHESES")
print("-" * 40)

print("""The conditional expression has very low precedence – almost everything else happens first.
That means if you mix it with other operators, you might need parentheses to control the order.""")

x = y = 40
print(f"x = y = {x}")

z = 1 + x if x > y else y + 2
print("z = 1 + x if x > y else y + 2")
print(f"   → {z}  (because 1+x and y+2 are evaluated first, then the conditional)")

z = (1 + x) if x > y else (y + 2)
print("z = (1 + x) if x > y else (y + 2)")
print(f"   → {z}  (same)")

z = 1 + (x if x > y else y) + 2
print("z = 1 + (x if x > y else y) + 2")
print(f"   → {z}  (now the conditional is evaluated first)")

print("\n💡 If you're unsure, add parentheses – they make your intention clear.")

# ============================================================================
# SECTION 5: SHORT‑CIRCUIT EVALUATION – IT'S LAZY!
# ============================================================================
print("\n\n5. SHORT‑CIRCUIT EVALUATION – IT'S LAZY!")
print("-" * 40)

print("""Like and/or, the conditional expression only evaluates what it needs.
If the condition is True, it evaluates the left value and ignores the right.
If False, it evaluates the right and ignores the left.""")

print("\nExample: a division by zero that never happens")
print("'foo' if True else 1/0  →", 'foo' if True else 1/0)
print("1/0 if False else 'bar' →", 1/0 if False else 'bar')

print("\nNo errors – the dangerous part is skipped because it's not needed!")

# ============================================================================
# SECTION 6: CHAINING CONDITIONAL EXPRESSIONS (LIKE ELIF)
# ============================================================================
print("\n\n6. CHAINING CONDITIONAL EXPRESSIONS")
print("-" * 40)

print("""You can chain multiple conditional expressions to mimic an if/elif/else chain.
It looks like this:
   value1 if condition1 else value2 if condition2 else value3 ...

But be careful – it can become hard to read. Sometimes a regular if statement is clearer.
""")

x = 3
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux')
print(f"x = {x} → s = {s}")

print("\nIt works, but would you rather read this or a normal if/elif/else?")
print("For simple cases it might be okay; for complex ones, stick to the standard form.")

# ============================================================================
# SECTION 7: SUMMARY AND BEST PRACTICES
# ============================================================================
print("\n\n7. SUMMARY AND BEST PRACTICES")
print("-" * 40)

print("""
• A conditional expression (ternary) is a one‑line way to choose between two values.
• Syntax: <value_if_true> if <condition> else <value_if_false>
• It's an expression, so you can use it inside print, assignments, calculations, etc.
• It has low precedence – use parentheses to control evaluation order.
• It short‑circuits: only the chosen side is evaluated.
• You can chain them, but don't overdo it – readability counts!
• Use it for simple, clear choices. For complex logic, prefer a regular if statement.
""")

print("\n🎯 YOUR TURN! Try these exercises:")
print("""
1. Write a conditional expression that returns 'even' if a number is even, else 'odd'.
2. Use a conditional expression inside a print to say 'hot' if temperature > 30 else 'cold'.
3. Given two numbers, assign the smaller one to a variable using a ternary.
4. Experiment with chaining: rewrite a simple grade letter (A, B, C, D, F) using chained ternaries.
5. See what happens if you forget parentheses in a complex expression – then add them.
""")

print("\n" + "=" * 60)
print("SAVE AS: Conditional_Expressions.py")
print("RUN WITH: python Conditional_Expressions.py")
print("=" * 60)