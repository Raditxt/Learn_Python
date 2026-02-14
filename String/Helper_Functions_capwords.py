"""
This script explains Python's string.capwords() helper function
in a simple way that can be understood even by a 5-year-old (using Feynman Technique).

Feynman Technique: Explain complex concepts with simple language,
analogies, and concrete examples.
"""

print("=" * 60)
print("STRING HELPER: capwords() – CAPITALIZING WORDS MADE EASY")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: WHAT IS capwords()?
# ============================================================================
print("1. WHAT IS capwords()?")
print("-" * 40)

print("""capwords() is a handy helper function that:
   • Takes a sentence (a string)
   • Splits it into words
   • Capitalizes each word (first letter uppercase, rest lowercase)
   • Joins them back together with a single space between words

Think of it as a "title case" maker, but smarter!""")

print("\nWhere is it? It lives in the 'string' module, so we need to import it first:")
print("   from string import capwords\n")

from string import capwords

print("Now we can use it!")

# ============================================================================
# SECTION 2: BASIC USAGE – WITHOUT CUSTOM SEPARATOR
# ============================================================================
print("\n\n2. BASIC USAGE – WITHOUT CUSTOM SEPARATOR")
print("-" * 40)

s = "hello world, how are you?"
print(f"Original: '{s}'")
result = capwords(s)
print(f"capwords(s) → '{result}'")

print("\nWhat happened?")
print("   • Words were split at spaces (any whitespace).")
print("   • Each word's first letter capitalized, rest lowercased.")
print("   • They were joined with a single space.")

print("\nNotice that punctuation stays attached to words, but the word itself is capitalized correctly.")

# ============================================================================
# SECTION 3: HOW capwords() WORKS – STEP BY STEP
# ============================================================================
print("\n\n3. STEP BY STEP – THE MAGIC REVEALED")
print("-" * 40)

print("""capwords() does three simple things:
   1. Split the string into words using .split()
   2. Capitalize each word using .capitalize()
   3. Join the words back using ' '.join()
""")

print("Let's simulate it manually:")

s = "  hello   world!  how are you?  "
print(f"\nOriginal string: '{s}'")

# Step 1: split
words = s.split()
print(f"Step 1: .split() → {words}")

# Step 2: capitalize each
capitalized = [w.capitalize() for w in words]
print(f"Step 2: capitalize each → {capitalized}")

# Step 3: join
joined = ' '.join(capitalized)
print(f"Step 3: join with space → '{joined}'")

print("\ncapwords(s) does exactly that:")
print(f"   capwords('{s}') → '{capwords(s)}'")

# ============================================================================
# SECTION 4: USING A CUSTOM SEPARATOR (sep PARAMETER)
# ============================================================================
print("\n\n4. CUSTOM SEPARATOR – WHEN WORDS ARE SEPARATED BY SOMETHING ELSE")
print("-" * 40)

print("""Sometimes words are not separated by spaces, but by commas, dashes, or other characters.
You can tell capwords() what separator to use with the 'sep' parameter.""")

print("\n🔹 Example with comma-separated values:")
csv = "apple,banana,orange,grape"
print(f"Original: '{csv}'")
print(f"capwords(csv, sep=',') → '{capwords(csv, sep=',')}'")

print("\nNotice: it splits at commas, capitalizes each, and joins with the SAME separator (a comma).")
print("But after joining, there's no extra space – it's exactly like you'd want for CSV.")

print("\n🔹 Example with hyphens:")
hyphenated = "hello-world-python"
print(f"Original: '{hyphenated}'")
print(f"capwords(hyphenated, sep='-') → '{capwords(hyphenated, sep='-')}'")

print("\n🔹 What about multiple spaces? The default behavior cleans them up.")
messy = "   too    many   spaces   "
print(f"Original: '{messy}'")
print(f"capwords(messy) → '{capwords(messy)}'  (spaces normalized)")

print("\nBut with a custom separator, it doesn't normalize spaces – it uses exactly that separator.")
messy_csv = "apple,  banana ,orange"
print(f"Original: '{messy_csv}'")
print(f"capwords(messy_csv, sep=',') → '{capwords(messy_csv, sep=',')}'")
print("(The extra spaces around banana are preserved because they're part of the words!)")

# ============================================================================
# SECTION 5: COMPARISON WITH .title() AND .capitalize()
# ============================================================================
print("\n\n5. capwords() vs .title() vs .capitalize()")
print("-" * 40)

print("Python has several ways to capitalize text. Let's compare:")

s = "hello world! how's it going?"

print(f"\nOriginal: '{s}'")
print(f"str.capitalize(): '{s.capitalize()}'  (only first word)")
print(f"str.title():      '{s.title()}'        (every word, but can mess up apostrophes)")
print(f"capwords():       '{capwords(s)}'      (smart: splits on whitespace, handles apostrophes better)")

print("\nNotice: .title() capitalizes after apostrophe? Actually 'How'S' – not good.")
print("capwords() treats 'how's' as one word, capitalizes 'How's' – much better for normal sentences.")

# ============================================================================
# SECTION 6: EDGE CASES AND SPECIAL SITUATIONS
# ============================================================================
print("\n\n6. EDGE CASES – WHAT ABOUT EMPTY STRINGS?")
print("-" * 40)

print("Empty string:")
print(f"   capwords('') → '{capwords('')}'")

print("\nString with only spaces:")
print(f"   capwords('   ') → '{capwords('   ')}'")

print("\nString with no letters:")
print(f"   capwords('123 456') → '{capwords('123 456')}' (digits stay digits)")

print("\nString with mixed case:")
mixed = "tHiS iS a MiXeD CaSe SeNtEnCe"
print(f"   Original: '{mixed}'")
print(f"   capwords: '{capwords(mixed)}'")

print("\nCustom separator with no separator in string:")
print(f"   capwords('hello world', sep=',') → '{capwords('hello world', sep=',')}'")
print("   (If the separator isn't found, the whole string is treated as one word.)")

# ============================================================================
# SECTION 7: PRACTICAL USE CASES
# ============================================================================
print("\n\n7. PRACTICAL USE CASES – WHERE capwords() SHINES")
print("-" * 40)

print("🔹 Cleaning up user‑entered names:")
user_input = "  jOhN  dOE  "
clean_name = capwords(user_input)
print(f"   '{user_input}' → '{clean_name}'")

print("\n🔹 Formatting product titles:")
product = "   python programming   FOR beginners   "
print(f"   '{product}' → '{capwords(product)}'")

print("\n🔹 Processing CSV data where you want consistent capitalization:")
csv_data = "apple,BANANA,Orange,Grape"
print(f"   Original CSV: '{csv_data}'")
print(f"   capwords(..., sep=','): '{capwords(csv_data, sep=',')}'")

print("\n🔹 Making headings for a report:")
heading = "sales report for Q1 2025"
print(f"   '{heading}' → '{capwords(heading)}'")

# ============================================================================
# SECTION 8: IMPLEMENTATION DETAIL (JUST FOR CURIOSITY)
# ============================================================================
print("\n\n8. HOW WOULD YOU WRITE capwords YOURSELF?")
print("-" * 40)

print("""If Python didn't provide capwords, you could write it like this:

def my_capwords(s, sep=None):
    if sep is None:
        words = s.split()
    else:
        words = s.split(sep)
    capitalized = [word.capitalize() for word in words]
    if sep is None:
        return ' '.join(capitalized)
    else:
        return sep.join(capitalized)

But it's already built-in, so just use it!""")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

print("""
Exercise 1: Fixing Names
------------------------
Given a list of names with messy capitalization and extra spaces:
   names = ["  alice   ", "BOB", "  charlie  ", "  dAVID  "]
Use capwords to clean them up and print the cleaned list.

Exercise 2: CSV Cleanup
------------------------
You have a CSV string: "red, GREEN, blue, YELLOW"
Use capwords with the appropriate separator to produce a clean CSV with proper capitalization.

Exercise 3: Poem Formatter
--------------------------
Write a function that takes a multi‑line poem (with irregular spacing) and uses capwords to capitalize each line. Keep the line breaks intact.

Exercise 4: Custom Separator Challenge
--------------------------------------
Given a string like "hello-world-python-java", use capwords with a custom separator to make it "Hello-World-Python-Java".

Exercise 5: Compare with .title()
----------------------------------
Take a sentence with an apostrophe, e.g., "it's a beautiful day".
Compare the output of capwords and .title(). Which one looks more correct? Why?
""")

print("\n" + "=" * 40)
print("HINTS (Try yourself first!)")
print("=" * 40)

print("""
Hint 1: Use a list comprehension or loop with capwords.
Hint 2: sep=',' – remember to strip extra spaces if needed.
Hint 3: Split the poem into lines, apply capwords to each line, then join with newline.
Hint 4: sep='-'.
Hint 5: .title() capitalizes every word, including after apostrophe, so "It'S" – ugly. capwords treats "it's" as one word, gives "It's".
""")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS – capwords()")
print("=" * 60)

print("""
1. ✨ capwords(s) capitalizes every word in a string intelligently.
2. 🔪 It splits on whitespace (by default), capitalizes, and rejoins with a single space.
3. 🧵 You can provide a custom separator (sep) for non‑space delimiters.
4. 🧹 It cleans up extra spaces when using default behavior.
5. 👑 It's often better than .title() for normal sentences because it handles apostrophes and punctuation gracefully.
6. 📦 It's in the string module – import it to use.

Remember: capwords is your friend for making titles, names, and any text look neat and professional! 🎩
""")

print("\n" + "=" * 60)
print("SAVE AS: Helper_Functions_capwords.py")
print("RUN WITH: python Helper_Functions_capwords.py")
print("=" * 60)