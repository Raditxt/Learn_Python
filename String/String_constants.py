"""
This script explains Python strings and common string operations in a simple way
that can be understood even by a 5-year-old (using Feynman Technique).

Feynman Technique: Explain complex concepts with simple language,
analogies, and concrete examples.
"""

print("=" * 60)
print("PYTHON STRINGS: THE MAGIC OF TEXT")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: WHAT IS A STRING?
# ============================================================================
print("1. WHAT IS A STRING?")
print("-" * 40)

print("""A string is just a fancy word for TEXT.
It's a sequence of letters, numbers, spaces, and symbols.
Think of it as a necklace where each bead is a character.""")

print("\nSimple examples:")
print("'hello' — 5 beads: h, e, l, l, o")
print('"Python" — 6 beads: P, y, t, h, o, n')
print("'123' — 3 beads: 1, 2, 3 (still text, not numbers!)")
print("'😊🐍' — 2 beads: smiley face and snake (emojis work too!)")

print("\nHow to create a string:")
print("1. With single quotes: 'Hello'")
print("2. With double quotes: \"World\"")
print("3. With triple quotes: '''Multi-line text'''")

print("\nLet's make some strings:")
greeting = "Hello, Python!"
print(f"greeting = '{greeting}'")
print(f"Type: {type(greeting).__name__}")
print(f"Length: {len(greeting)} characters")

# ============================================================================
# SECTION 2: STRING CONSTANTS – PYTHON'S READY‑MADE LETTER SETS
# ============================================================================
print("\n\n2. STRING CONSTANTS – PYTHON'S READY‑MADE LETTER SETS")
print("-" * 40)

print("""Python has a special toolbox called 'string'.
Inside it, there are ready‑made sets of letters, digits, and symbols.
No need to type them yourself!""")

# Import the string module
import string

print("\n📦 Open the string toolbox: import string")
print("\nNow let's peek inside:")

# ascii_lowercase
print("\n🔹 string.ascii_lowercase")
print("   All lowercase English letters, like a‑z.")
print(f"   '{string.ascii_lowercase}'")
print(f"   Length: {len(string.ascii_lowercase)}")

# ascii_uppercase
print("\n🔹 string.ascii_uppercase")
print("   All UPPERCASE English letters, like A‑Z.")
print(f"   '{string.ascii_uppercase}'")
print(f"   Length: {len(string.ascii_uppercase)}")

# ascii_letters
print("\n🔹 string.ascii_letters")
print("   Lowercase + Uppercase together.")
print(f"   '{string.ascii_letters}'")
print(f"   Length: {len(string.ascii_letters)}")

# digits
print("\n🔹 string.digits")
print("   The digits 0‑9.")
print(f"   '{string.digits}'")
print(f"   Length: {len(string.digits)}")

# hexdigits
print("\n🔹 string.hexdigits")
print("   Hexadecimal digits (0‑9, a‑f, A‑F).")
print(f"   '{string.hexdigits}'")
print(f"   Length: {len(string.hexdigits)}")

# octdigits
print("\n🔹 string.octdigits")
print("   Octal digits (0‑7).")
print(f"   '{string.octdigits}'")
print(f"   Length: {len(string.octdigits)}")

# punctuation
print("\n🔹 string.punctuation")
print("   Punctuation symbols like !, ?, ., etc.")
print(f"   '{string.punctuation}'")
print(f"   Length: {len(string.punctuation)}")

# whitespace
print("\n🔹 string.whitespace")
print("   Whitespace characters: space, tab, newline, etc.")
print(f"   {repr(string.whitespace)}")  # use repr to show special chars
print(f"   Length: {len(string.whitespace)}")

# printable
print("\n🔹 string.printable")
print("   All characters that can be printed: digits, letters, punctuation, whitespace.")
print(f"   Length: {len(string.printable)} (too long to show all!)")

print("\n🎯 Analogy:")
print("""These constants are like having sticker sheets:
• Lowercase stickers, uppercase stickers, number stickers, punctuation stickers.
You can use them right away to build things!""")

# ============================================================================
# SECTION 3: USING STRING CONSTANTS – PRACTICAL EXAMPLES
# ============================================================================
print("\n\n3. USING STRING CONSTANTS – PRACTICAL EXAMPLES")
print("-" * 40)

print("Let's solve simple problems with these ready‑made sets.")

# Example 1: Generate a random password
print("\n🔐 Generate a random 8‑character password:")
import random
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(8))
print(f"   characters pool = ascii_letters + digits + punctuation")
print(f"   password = '{password}'")

# Example 2: Check if a string contains only digits
print("\n🔎 Check if a string contains ONLY digits:")
test1 = "12345"
test2 = "12a45"
print(f"   {test1} → {test1.isdigit()} (using .isdigit() method)")
print(f"   {test2} → {test2.isdigit()}")

# Alternative using string.digits
print("   (string.digits is useful for building your own check)")

# Example 3: Remove punctuation from a sentence
print("\n✂️ Remove all punctuation from a sentence:")
sentence = "Hello, world! How's it going? (Python is awesome.)"
print(f"   Original: {sentence}")
# Build translation table that maps each punctuation to None
translator = str.maketrans('', '', string.punctuation)
clean = sentence.translate(translator)
print(f"   Clean:    {clean}")

# Example 4: Check if a character is a hex digit
print("\n🧪 Check if 'A' is a hex digit:")
print(f"   'A' in string.hexdigits → {'A' in string.hexdigits}")
print(f"   'G' in string.hexdigits → {'G' in string.hexdigits}")

# ============================================================================
# SECTION 4: COMMON STRING OPERATIONS (METHODS)
# ============================================================================
print("\n\n4. COMMON STRING OPERATIONS – STRING SUPERHERO POWERS")
print("-" * 40)

print("""Strings can do many things! They come with built‑in methods.
Think of them as superpowers every string has.""")

# Create a sample string
sample = "  Python Programming is FUN!  "
print(f"\nOur test string: '{sample}'")

# .lower() and .upper()
print("\n🔹 .lower()  – make everything lowercase")
print(f"   {sample.lower()}")
print("\n🔹 .upper()  – make everything UPPERCASE")
print(f"   {sample.upper()}")

# .capitalize() and .title()
print("\n🔹 .capitalize() – first letter uppercase, rest lowercase")
print(f"   {sample.capitalize()}")
print("\n🔹 .title() – first letter of each word uppercase")
print(f"   {sample.title()}")

# .strip() – remove whitespace from both ends
print("\n🔹 .strip() – remove spaces (and other whitespace) from front and back")
print(f"   '{sample.strip()}'")

# .lstrip() and .rstrip()
print("\n🔹 .lstrip() – remove from left side")
print(f"   '{sample.lstrip()}'")
print("\n🔹 .rstrip() – remove from right side")
print(f"   '{sample.rstrip()}'")

# .split() – cut into pieces
print("\n🔹 .split() – split string into a list (by space by default)")
words = sample.split()
print(f"   {words}")

print("\n🔹 .split(',') – split by comma")
csv_data = "apple,banana,orange"
print(f"   {csv_data.split(',')}")

# .join() – glue pieces together
print("\n🔹 .join() – opposite of split, glue list elements with a string")
fruits = ['apple', 'banana', 'orange']
print(f"   {'-'.join(fruits)}")
print(f"   {' and '.join(fruits)}")

# .replace() – swap parts
print("\n🔹 .replace(old, new) – replace occurrences")
message = "I like cats. Cats are cute."
print(f"   {message}")
print(f"   {message.replace('cats', 'dogs')} (careful: case‑sensitive)")
print(f"   {message.replace('Cats', 'Dogs')}")

# .find() and .index()
print("\n🔹 .find(substring) – find position (-1 if not found)")
print(f"   In '{sample.strip()}':")
pos = sample.find("Programming")
print(f"   'Programming' starts at index {pos}")
print(f"   'Java' starts at index {sample.find('Java')} (not found → -1)")

# .count()
print("\n🔹 .count(substring) – how many times does it appear?")
text = "abracadabra"
print(f"   '{text}' → 'a' appears {text.count('a')} times")

# .startswith() and .endswith()
print("\n🔹 .startswith() – does it begin with ...?")
print(f"   '{sample.strip()}' starts with 'Python'? {sample.strip().startswith('Python')}")
print("\n🔹 .endswith() – does it end with ...?")
print(f"   '{sample.strip()}' ends with 'FUN!'? {sample.strip().endswith('FUN!')}")

# .isalpha(), .isdigit(), .isalnum(), .isspace()
print("\n🔹 Checking character types:")
a = "Python3"
print(f"   '{a}'.isalpha() → {a.isalpha()} (only letters? No, has digit)")
print(f"   'Python'.isalpha() → {'Python'.isalpha()}")
print(f"   '123'.isdigit() → {'123'.isdigit()}")
print(f"   '123abc'.isalnum() → {'123abc'.isalnum()} (letters+digits)")
print(f"   '   '.isspace() → {'   '.isspace()} (only whitespace)")

# ============================================================================
# SECTION 5: F-STRINGS – THE EASIEST WAY TO BUILD STRINGS
# ============================================================================
print("\n\n5. F-STRINGS – MAGIC EMBROIDERY")
print("-" * 40)

print("""f‑strings (formatted string literals) let you insert variables directly into a string.
Just put an 'f' before the quotes and use {curly braces}.""")

name = "Alice"
age = 7
score = 95.5

# Old ways (don't do this unless you have to)
print("\n❌ Old ways (avoid):")
print("   'My name is ' + name + ' and I am ' + str(age) + ' years old.'")
print("   'My name is %s and I am %d years old.' % (name, age)")

# f-string way
print("\n✅ f-string way (best):")
print(f"   f'My name is {name} and I am {age} years old.'")
print(f"   Result: My name is {name} and I am {age} years old.")

print("\nYou can even do calculations inside {}:")
print(f"   f'Next year I will be {age + 1} years old.'")
print(f"   Result: Next year I will be {age + 1} years old.")

print(f"   f'Your score is {score:.1f}%'  # one decimal")
print(f"   Result: Your score is {score:.1f}%")

# ============================================================================
# SECTION 6: PUTTING IT ALL TOGETHER – A REAL EXAMPLE
# ============================================================================
print("\n\n6. REAL-WORLD EXAMPLE: SIMPLE TEXT ANALYZER")
print("-" * 40)

print("""Let's build a mini program that analyzes a sentence.
We'll use string constants and methods.""")

def text_analyzer(text):
    """Analyze a given text and print statistics."""
    print(f"\n📊 Analyzing: '{text}'")
    
    # Basic info
    print(f"   Length: {len(text)} characters")
    print(f"   Words: {len(text.split())}")
    
    # Count letters, digits, punctuation, whitespace
    letter_count = sum(1 for c in text if c in string.ascii_letters)
    digit_count = sum(1 for c in text if c in string.digits)
    punct_count = sum(1 for c in text if c in string.punctuation)
    space_count = sum(1 for c in text if c in string.whitespace)
    
    print(f"   Letters: {letter_count}")
    print(f"   Digits: {digit_count}")
    print(f"   Punctuation: {punct_count}")
    print(f"   Whitespace: {space_count}")
    
    # Uppercase / lowercase
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    print(f"   Uppercase: {upper_count}")
    print(f"   Lowercase: {lower_count}")
    
    # Does it contain only alphanumeric + spaces?
    clean_text = text.replace(" ", "")  # remove spaces for check
    if clean_text.isalnum():
        print("   ✅ Contains only letters, digits, and spaces.")
    else:
        print("   ❌ Contains other characters (punctuation, symbols).")

# Test the analyzer
test_sentence = "Hello Python 3.12! How's it going?"
text_analyzer(test_sentence)

# ============================================================================
# SECTION 7: COMMON PITFALLS AND TIPS
# ============================================================================
print("\n\n7. COMMON PITFALLS AND TIPS")
print("-" * 40)

print("⚠️ Strings are IMMUTABLE – you cannot change them in place!")
print("""When you use methods like .upper(), .replace(), etc.,
they return a NEW string; the original stays the same.""")

s = "hello"
print(f"\ns = '{s}'")
s.upper()
print(f"s.upper() → but s is still '{s}' (unchanged!)")
s = s.upper()
print(f"s = s.upper() → now s is '{s}'")

print("\n💡 Use triple quotes for multi‑line strings:")
poem = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''
print(poem)

print("\n💡 Escape characters: use \\ for special symbols")
print("   She said, \"Hello!\" → She said, \"Hello!\"")
print("   New line:\\nSecond line → New line:\n   Second line")

print("\n💡 Raw strings (r'...') ignore escapes (useful for paths):")
print(r"   Windows path: C:\Users\Name\Documents")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

print("""
Exercise 1: Password Strength Checker
------------------------------------
Write a function that checks if a password is strong:
- At least 8 characters
- Contains at least one lowercase letter
- Contains at least one uppercase letter
- Contains at least one digit
- Contains at least one punctuation symbol (string.punctuation)

Use string constants and string methods.

Exercise 2: Clean Phone Number
------------------------------
Given a phone number like "+62 812-3456-7890", remove all non‑digit characters.
Output should be "6281234567890".
Hint: use string.digits and a loop or join.

Exercise 3: Pig Latin Translator
--------------------------------
Pig Latin rule: for a word starting with a vowel (a,e,i,o,u), add "yay".
For a word starting with consonant, move first letter to end and add "ay".
Example: "hello" → "ellohay", "apple" → "appleyay".
Write a function that translates a sentence.

Exercise 4: Secret Code
-----------------------
Create a simple Caesar cipher: shift each letter by 3 positions.
Use string.ascii_lowercase to wrap around.
Example: "abc" → "def", "xyz" → "abc".
Only shift letters, keep case.

Exercise 5: Count Vowels
------------------------
Count how many vowels (a,e,i,o,u) are in a given string, case‑insensitive.
""")

print("\n" + "=" * 40)
print("HINTS (Try yourself first!)")
print("=" * 40)

print("""
Hint 1: use any() with generator expressions
Hint 2: use str.join() and filter
Hint 3: check if first letter is vowel using 'aeiou'
Hint 4: find index in ascii_lowercase, shift, use modulo
Hint 5: use .lower() and .count() in a loop
""")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS – STRINGS IN A NUTSHELL")
print("=" * 60)

print("""
1. 📦 string module gives you ready‑made letter/digit/punctuation sets.
2. 🛠️ Strings have many useful methods: lower, upper, strip, split, join, replace, find, count, etc.
3. ✨ f-strings are the modern, clean way to embed variables.
4. 🔒 Strings are immutable – every operation creates a new string.
5. 🧠 Use f-strings and string methods to write clean, readable code.

Remember: Strings are everywhere in programming.
Master them and you can handle any text! 🚀
""")

print("\n" + "=" * 60)
print("SAVE AS: String_Operations.py")
print("RUN WITH: python String_Operations.py")
print("=" * 60)

# ============================================================================
# BONUS: INTERACTIVE DEMO (if user wants to run)
# ============================================================================
print("\n\n🎮 BONUS: Quick interactive demo (uncomment to try)")
print("""
# Uncomment these lines if you want to play:

# user_text = input("Enter some text: ")
# print(f"You entered: {user_text}")
# print(f"Uppercase: {user_text.upper()}")
# print(f"Title case: {user_text.title()}")
# print(f"Reversed: {user_text[::-1]}")
""")