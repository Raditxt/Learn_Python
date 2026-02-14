"""
This script explains Python's Template strings ($-strings) in a simple way
that can be understood even by a 5-year-old (using Feynman Technique).

Feynman Technique: Explain complex concepts with simple language,
analogies, and concrete examples.
"""

print("=" * 60)
print("TEMPLATE STRINGS – SIMPLE $ FILL‑IN‑THE‑BLANKS")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: WHAT ARE TEMPLATE STRINGS?
# ============================================================================
print("1. WHAT ARE TEMPLATE STRINGS?")
print("-" * 40)

print("""Imagine you have a letter with blank spaces marked by $ signs:
   'Dear $name, your balance is $amount.'
Template strings are a super simple way to fill those blanks.
They use $ (like in shell scripts) instead of {}.""")

print("\nThey were introduced in Python 2.4 and are perfect when you want:")
print("   • A very simple syntax (easy for translators)")
print("   • To avoid the complexity of .format() or f‑strings")
print("   • Safe substitution (no errors if a placeholder is missing)")

print("\nThey are NOT the same as f‑strings (which are evaluated immediately).")
print("Template strings are evaluated later, when you call .substitute().")

# ============================================================================
# SECTION 2: BASIC USAGE – THE Template CLASS
# ============================================================================
print("\n\n2. BASIC USAGE – THE Template CLASS")
print("-" * 40)

print("""We need to import Template from the string module:""")
print("   from string import Template\n")

from string import Template

print("Now we can create a template:")

# Create a simple template
t = Template("Hello, $name!")
print("   t = Template('Hello, $name!')")

# Substitute
result = t.substitute(name="Alice")
print("   result = t.substitute(name='Alice')")
print(f"   → '{result}'")

print("\nYou can use multiple placeholders:")
t2 = Template("$who likes $what")
print("   t2 = Template('$who likes $what')")
result2 = t2.substitute(who="tim", what="kung pao")
print(f"   → '{result2}'")

print("\nYou can also pass a dictionary:")
d = {"who": "Bob", "what": "ice cream"}
result3 = t2.substitute(d)
print(f"   t2.substitute({d}) → '{result3}'")

print("\nAnd you can mix dictionary and keyword arguments (keywords win):")
result4 = t2.substitute(d, what="cake")
print(f"   t2.substitute(d, what='cake') → '{result4}'")

# ============================================================================
# SECTION 3: ESCAPING $ – WRITING A REAL DOLLAR SIGN
# ============================================================================
print("\n\n3. ESCAPING $ – WRITING A REAL DOLLAR SIGN")
print("-" * 40)

print("""What if you need a real $ in your text? Use $$ to escape it.""")

t_dollar = Template("Give me $$100")
print("   t_dollar = Template('Give me $$100')")
result = t_dollar.substitute()
print(f"   → '{result}'")  # 'Give me $100'

print("\nThis is like telling Python: 'This $ is just a dollar sign, not a placeholder.'")

# ============================================================================
# SECTION 4: BRACED PLACEHOLDERS – ${identifier}
# ============================================================================
print("\n\n4. BRACED PLACEHOLDERS – ${identifier}")
print("-" * 40)

print("""Sometimes a placeholder touches other letters, like in '${noun}ification'.
Without braces, Python would think the whole word is the placeholder.""")

t_brace = Template("The concept of ${noun}ification is important.")
print("   t_brace = Template('The concept of ${noun}ification is important.')")
result = t_brace.substitute(noun="class")
print(f"   → '{result}'")

print("\nWithout braces, $nounification would look for a key 'nounification', which doesn't exist.")

# ============================================================================
# SECTION 5: DEALING WITH MISSING PLACEHOLDERS – substitute vs safe_substitute
# ============================================================================
print("\n\n5. MISSING PLACEHOLDERS – substitute vs safe_substitute")
print("-" * 40)

print("""If you forget to provide a value for a placeholder, what happens?""")

t = Template("Hello $name, you have $messages new messages.")
print("   t = Template('Hello $name, you have $messages new messages.')")

print("\n🔹 substitute() raises a KeyError:")
try:
    t.substitute(name="Alice")  # missing 'messages'
except KeyError as e:
    print(f"   → KeyError: {e}")

print("\n🔹 safe_substitute() leaves the placeholder untouched:")
result = t.safe_substitute(name="Alice")
print(f"   t.safe_substitute(name='Alice') → '{result}'")
print("   (It's 'safe' because it never crashes – but you get $messages back.)")

print("\nIt also handles invalid $ patterns gracefully:")
t_invalid = Template("This has a $ sign without a valid name.")
print("   t_invalid = Template('This has a $ sign without a valid name.')")
try:
    t_invalid.substitute()
except ValueError as e:
    print(f"   substitute() → {e}")
result = t_invalid.safe_substitute()
print(f"   safe_substitute() → '{result}'  (just leaves the $)")

# ============================================================================
# SECTION 6: CHECKING VALIDITY AND GETTING IDENTIFIERS
# ============================================================================
print("\n\n6. VALIDATION AND IDENTIFIERS (Python 3.11+)")
print("-" * 40)

print("""You can check if a template is valid without trying to substitute.""")

t1 = Template("$valid $also_valid")
t2 = Template("$invalid_$")  # ends with $, not valid

print("   t1.is_valid() →", t1.is_valid())  # True
print("   t2.is_valid() →", t2.is_valid())  # False

print("\nYou can also get the list of placeholder identifiers:")
print("   t1.get_identifiers() →", t1.get_identifiers())  # ['valid', 'also_valid']
# t2.get_identifiers() might return [] or only valid ones, ignoring invalid.

# Note: get_identifiers returns only valid identifiers, ignoring invalid ones.
# For t2, it would return an empty list, but depends on Python version.
# Let's demonstrate with a valid template:
t3 = Template("$a $b ${c} $$ $d")
print("   t3 = Template('$a $b ${c} $$ $d')")
print("   t3.get_identifiers() →", t3.get_identifiers())  # ['a', 'b', 'c', 'd']

# ============================================================================
# SECTION 7: CUSTOMIZING TEMPLATES – CHANGING THE DELIMITER
# ============================================================================
print("\n\n7. CUSTOMIZING TEMPLATES – YOUR OWN SYMBOL")
print("-" * 40)

print("""You can create your own template language by subclassing Template.
For example, use % as the delimiter instead of $.""")

class MyTemplate(Template):
    delimiter = '%'  # change delimiter to percent sign

# Now use % for placeholders
t = MyTemplate("Hello %name, you have %messages messages.")
print("   t = MyTemplate('Hello %name, you have %messages messages.')")
result = t.substitute(name="Alice", messages=5)
print(f"   → '{result}'")

print("\nYou can also change the pattern of allowed identifier names.")
print("For instance, allow digits anywhere:")

class DigitTemplate(Template):
    idpattern = r'[a-z][_a-z0-9]*'  # default-like, but you can adjust
    # Actually default already allows digits after first character.
    # Let's make a stricter one: only letters (no digits)
    # But to illustrate, we'll allow digits even at start? That's not typical.
    # We'll just show changing delimiter is more common.

# We'll skip too complex regex examples, but note you can override braceidpattern and flags.

print("\nAdvanced: you can override the whole regular expression pattern.")
print("This is for experts – you need four named groups: escaped, named, braced, invalid.")

# ============================================================================
# SECTION 8: COMPARISON WITH .format() AND f-STRINGS
# ============================================================================
print("\n\n8. COMPARISON – WHEN TO USE WHAT")
print("-" * 40)

print("""Python has multiple ways to format strings:
   • f-strings:  f"Hello {name}" – evaluated immediately, most powerful.
   • .format():  "Hello {}".format(name) – flexible, older.
   • Template:   Template("Hello $name").substitute(...) – simplest, safest.

When to use Template strings?
   • When you need a VERY simple syntax (e.g., for translators).
   • When you want to avoid accidental code execution (no expressions).
   • When you need safe substitution (missing placeholders become text).
   • When you work with user‑provided templates (security).

When NOT to use Template strings?
   • When you need complex formatting (width, alignment, types).
   • When you need expressions inside placeholders.
""")

print("\nExample comparison:")
name = "Alice"
items = 3

# f-string
print("   f-string:       ", f"Hello {name}, you have {items} items.")

# .format()
print("   .format():      ", "Hello {}, you have {} items.".format(name, items))

# Template
t = Template("Hello $name, you have $items items.")
print("   Template:       ", t.substitute(name=name, items=items))

# ============================================================================
# SECTION 9: REAL‑WORLD USE CASE – INTERNATIONALIZATION (i18n)
# ============================================================================
print("\n\n9. REAL‑WORLD USE CASE – TRANSLATION (i18n)")
print("-" * 40)

print("""Imagine you have a message that needs to be translated into many languages.
You want the translators to see a simple template, not complex Python code.""")

# English template
en_template = Template("Hello $name, your score is $score.")

# French translation (same placeholders!)
fr_template = Template("Bonjour $name, votre score est $score.")

# Substitute with actual data
data = {"name": "Alice", "score": 95}
print("   English:", en_template.substitute(data))
print("   French: ", fr_template.substitute(data))

print("\nBecause the placeholders are just $name and $score, translators can move them around.")
print("This is much safer than giving them Python code with {} placeholders.")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

print("""
Exercise 1: Simple Greeting
----------------------------
Create a template that says "Good $time, $name!".
Substitute time = "morning", name = "Alice".
What happens if you forget to provide 'name'? Try both substitute and safe_substitute.

Exercise 2: Escaping Dollars
-----------------------------
Write a template that produces: "Price: $25.99".
Make sure the $ is not interpreted as a placeholder.

Exercise 3: Braces Needed
--------------------------
You want to write "The ${animal}ization of society".
Create a template and substitute animal = "dog". What if you forget the braces?

Exercise 4: Custom Delimiter
-----------------------------
Create a subclass of Template that uses '#' as delimiter.
Use it to format a string like "#title by #author".

Exercise 5: Safe Translation
-----------------------------
Given a list of user comments, some might contain $ signs.
Use safe_substitute to avoid crashes while still replacing known placeholders.
""")

print("\n" + "=" * 40)
print("HINTS (Try yourself first!)")
print("=" * 40)

print("""
Hint 1: Template("Good $time, $name!").substitute(time="morning") → KeyError. safe_substitute leaves $name.
Hint 2: Use '$$' to escape: Template("Price: $$25.99")
Hint 3: Without braces: $animalization would look for key 'animalization'. Braces fix it.
Hint 4: class HashTemplate(Template): delimiter = '#'
Hint 5: safe_substitute won't crash, but will leave $ signs that are not placeholders.
""")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS – TEMPLATE STRINGS")
print("=" * 60)

print("""
1. 💲 Template strings use $ for placeholders – simple and intuitive.
2. 🔒 They are safe: safe_substitute never raises errors for missing keys.
3. 🧩 Use $$ to include a literal dollar sign.
4. 🛡️ Braces ${identifier} separate placeholders from following text.
5. 🔧 You can customize the delimiter and identifier pattern by subclassing.
6. 🌍 Perfect for internationalization (i18n) because translators see only simple $placeholders.
7. ⚡ For complex formatting, use .format() or f-strings instead.

Remember: Template strings are the "easy‑to‑translate" members of the formatting family! 🚀
""")

print("\n" + "=" * 60)
print("SAVE AS: Template_Strings.py")
print("RUN WITH: python Template_Strings.py")
print("=" * 60)