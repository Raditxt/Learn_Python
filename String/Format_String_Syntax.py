"""
This script explains Python's format string syntax and format specification mini‑language
in a simple way that can be understood even by a 5‑year‑old (using Feynman Technique).

Feynman Technique: Explain complex concepts with simple language,
analogies, and concrete examples.
"""

print("=" * 60)
print("FORMAT STRING SYNTAX – FILLING BLANKS LIKE MAGIC")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: WHAT IS A FORMAT STRING?
# ============================================================================
print("1. WHAT IS A FORMAT STRING?")
print("-" * 40)

print("""Imagine you have a postcard with blank spaces:
   'Dear ____, your score is ____.'
You want to fill those blanks with a name and a number.
A format string is that postcard – it has placeholders {} where you can insert values.""")

print("\nIn Python we use .format() to fill the blanks:")
name = "Alice"
score = 95
message = "Dear {}, your score is {}.".format(name, score)
print(f"   '{message}'")

print("\nThe curly braces {} are the blanks. Python replaces them with the values you give.")

# ============================================================================
# SECTION 2: BASIC SYNTAX – THE RULES OF THE BLANKS
# ============================================================================
print("\n\n2. BASIC SYNTAX – THE RULES OF THE BLANKS")
print("-" * 40)

print("""A replacement field looks like this: { [field_name] [!conversion] [:format_spec] }
Everything outside {} is normal text.""")

print("\nIf you need a real curly brace in your text, write it twice: {{ and }}")
print("Example: '{{Hello}}' → {Hello}")

print("\nLet's see the simplest form: empty {}")
print("   '{} + {} = {}'.format(2, 3, 5)")
print("   → '2 + 3 = 5'")

# ============================================================================
# SECTION 3: FIELD NAMES – WHICH BLANK GETS WHAT?
# ============================================================================
print("\n\n3. FIELD NAMES – LABELLING THE BLANKS")
print("-" * 40)

print("""You can give each blank a number (position) or a name.
This tells Python which value to put where.""")

print("\n🔹 Positional arguments (numbers):")
print("   '{0} is {1} years old. {0} loves Python.'.format('Alice', 8)")
print("   → 'Alice is 8 years old. Alice loves Python.'")
print("   (The same number can be used many times.)")

print("\n🔹 Keyword arguments (names):")
print("   '{name} is {age} years old.'.format(name='Bob', age=10)")
print("   → 'Bob is 10 years old.'")

print("\n🔹 You can even omit numbers if they appear in order (Python 3.1+):")
print("   '{} + {} = {}'.format(2, 3, 5)  → same as '{0} + {1} = {2}'")

print("\n🔹 Accessing attributes: use a dot like with objects.")
print("   point = (3, 5)  # tuple has no attributes, but we can use indexes:")
print("   'X: {0[0]}, Y: {0[1]}'.format(point)  → 'X: 3, Y: 5'")
print("   (For objects, you can write {0.real}, {0.imag} etc.)")

print("\n🔹 Accessing dictionary items: use square brackets without quotes.")
print("   data = {'name': 'Charlie', 'age': 7}")
print("   'Name: {0[name]}, Age: {0[age]}'.format(data)")
print("   → 'Name: Charlie, Age: 7'")

# ============================================================================
# SECTION 4: CONVERSION FLAGS – DRESSING UP THE VALUE
# ============================================================================
print("\n\n4. CONVERSION FLAGS – DRESSING UP THE VALUE")
print("-" * 40)

print("""Sometimes you want to force a value to be shown as a string (str()),
or as a programmer‑friendly representation (repr()), or as ASCII (ascii()).
You do that with !s, !r, !a.""")

print("\n🔹 !s – calls str() – the usual way we see things.")
print("🔹 !r – calls repr() – shows quotes and maybe more detail.")
print("🔹 !a – calls ascii() – like repr() but with only ASCII characters.")

example = "Hello\nWorld"
print(f"\n   Value = {repr(example)}")
print("   '{0!s}'.format(example) → '{0!s}'".format(example))
print("   '{0!r}'.format(example) → '{0!r}'".format(example))
print("   '{0!a}'.format(example) → '{0!a}'".format(example))

print("\nThink of it as choosing a costume: !s is casual clothes, !r is a detailed costume with tags, !a is a costume that only uses simple letters.")

# ============================================================================
# SECTION 5: FORMAT SPECIFICATION – MAKING IT PRETTY
# ============================================================================
print("\n\n5. FORMAT SPECIFICATION – DECORATING THE TEXT")
print("-" * 40)

print("""After a colon : you can give instructions on how to display the value.
This is like telling Python: 'make it 10 characters wide, align right, pad with stars, etc.'""")

print("\nThe general structure: [[fill]align][sign][#][0][width][grouping][.precision][type]")

print("\n🔹 Alignment and fill:")
print("   '<'  left align")
print("   '>'  right align")
print("   '^'  center")
print("   '='  pad after sign (for numbers)")

print("\n   Example: '{:*<10}'.format('left') → '{:*<10}'".format('left'))
print("   Example: '{:*>10}'.format('right') → '{:*>10}'".format('right'))
print("   Example: '{:*^10}'.format('center') → '{:*^10}'".format('center'))

print("\n🔹 Sign for numbers:")
print("   '+'  show sign for both + and -")
print("   '-'  show sign only for - (default)")
print("   ' '  show space for positive, minus for negative")

print("\n   Example: '{:+d} {:+d}'.format(42, -42) → '{:+d} {:+d}'".format(42, -42))
print("   Example: '{: d} {: d}'.format(42, -42) → '{: d} {: d}'".format(42, -42))

print("\n🔹 Width and zero padding:")
print("   A number sets minimum width. Use '0' to pad with zeros (for numbers).")
print("   Example: '{:5d}'.format(42) → '{:5d}'".format(42))
print("   Example: '{:05d}'.format(42) → '{:05d}'".format(42))

print("\n🔹 Grouping options: comma ',' or underscore '_'")
print("   Example: '{:,}'.format(1234567) → '{:,}'".format(1234567))
print("   Example: '{:_}'.format(1234567) → '{:_}'".format(1234567))

print("\n🔹 Precision for floats: .N")
print("   Example: '{:.2f}'.format(3.14159) → '{:.2f}'".format(3.14159))

print("\n🔹 Type codes – what kind of value:")
print("   For integers: b (binary), c (character), d (decimal), o (octal), x (hex), X (HEX)")
print("   For floats: e (scientific), f (fixed), g (general), % (percentage)")
print("   For strings: s (string – default)")

print("\n   Example: 'hex: {:x}, bin: {:b}'.format(42, 42) → 'hex: {:x}, bin: {:b}'".format(42, 42))
print("   Example: 'percentage: {:.2%}'.format(0.1234) → 'percentage: {:.2%}'".format(0.1234))

# ============================================================================
# SECTION 6: PUTTING IT ALL TOGETHER – FUN EXAMPLES
# ============================================================================
print("\n\n6. FUN EXAMPLES – MIXING EVERYTHING")
print("-" * 40)

print("""Let's make a little table using format specifications:""")

data = [
    ("apple", 1.5, 10),
    ("banana", 0.75, 25),
    ("cherry", 2.0, 5)
]

print("\n{:<10} {:>8} {:>6}".format("Item", "Price", "Qty"))
print("-" * 26)
for item, price, qty in data:
    print("{:<10} {:>8.2f} {:>6d}".format(item, price, qty))

print("\nNow with centering and fill:")
for item, price, qty in data:
    print("{:*^10} {:*^8} {:*^6}".format(item, f"{price:.2f}", qty))

# ============================================================================
# SECTION 7: NESTED REPLACEMENT FIELDS – DYNAMIC FORMATTING
# ============================================================================
print("\n\n7. NESTED REPLACEMENT FIELDS – FORMATTING THAT CHANGES")
print("-" * 40)

print("""You can put a replacement field inside the format_spec itself!
That means the width, precision, or even the type can be decided by another variable.""")

width = 10
align = '^'
fill = '-'
value = "hello"

print("   width = 10, align = '^', fill = '-'")
result = "{:{fill}{align}{width}}".format(value, fill=fill, align=align, width=width)
print(f"   Result: '{result}'")

print("\nYou can even nest deeper, but keep it simple or it gets confusing.")

# ============================================================================
# SECTION 8: TYPE‑SPECIFIC FORMATTING – DATES AND MORE
# ============================================================================
print("\n\n8. TYPE‑SPECIFIC FORMATTING – DATES, PERCENTAGES, ETC.")
print("-" * 40)

import datetime

now = datetime.datetime.now()
print("Today is {:%Y-%m-%d %H:%M:%S}".format(now))
print("   (This uses datetime's own formatting codes inside the format spec.)")

print("\nPercentage:")
score = 19 / 22
print("   Correct answers: {:.2%}".format(score))

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

print("""
Exercise 1: Table of Squares
-----------------------------
Use .format() to print a table of numbers from 1 to 5 with their squares.
Align the numbers right, width 5, and the squares right, width 5.

Exercise 2: Phone Number Formatter
----------------------------------
Given a phone number like 1234567890, format it as (123) 456-7890.
Hint: you can access digits by index using [0] etc.

Exercise 3: Currency with Commas
---------------------------------
Format a large number like 1234567.89 as $1,234,567.89.
Use grouping and two decimal places.

Exercise 4: Dynamic Width
--------------------------
Write a program that asks the user for a word and a width, then prints the word
centered in that width with '=' as fill.

Exercise 5: Binary and Hex Table
---------------------------------
Print numbers 0 to 15 in decimal, binary, hex, and octal, nicely aligned.
""")

print("\n" + "=" * 40)
print("HINTS (Try yourself first!)")
print("=" * 40)

print("""
Hint 1: Use '{:>5} {:>5}'.format(n, n*n)
Hint 2: '{}({}) {}-{}'.format(...) – you'll need to extract digits using string slicing or [0] on the string.
Hint 3: Use '{:,.2f}'.format(number) and add '$' before.
Hint 4: Use nested replacement: '{:{fill}^{width}}'.format(word, fill='=', width=width)
Hint 5: Use '{:>5} {:>5b} {:>5x} {:>5o}'.format(n, n, n, n)
""")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS – FORMAT STRING SYNTAX")
print("=" * 60)

print("""
1. 📝 Replacement fields {} are blanks you fill with .format().
2. 🔢 Use numbers or names to specify which argument goes where.
3. 🎭 Conversion flags !s, !r, !a change how the value is converted to string.
4. 🎨 Format spec after : lets you control width, alignment, padding, sign, grouping, precision, and type.
5. 🧩 You can nest replacement fields inside the format spec for dynamic formatting.
6. 📅 Different types (numbers, strings, dates) have their own formatting rules.

Remember: .format() is like a magic stamp – it turns a template into a beautiful final string! 🌟
""")

print("\n" + "=" * 60)
print("SAVE AS: Format_String_Syntax.py")
print("RUN WITH: python Format_String_Syntax.py")
print("=" * 60)