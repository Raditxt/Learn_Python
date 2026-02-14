"""
This script explains Python's custom string formatting using the Formatter class,
in a simple way that can be understood even by a 5-year-old (using Feynman Technique).

Feynman Technique: Explain complex concepts with simple language,
analogies, and concrete examples.
"""

print("=" * 60)
print("CUSTOM STRING FORMATTING – THE BUILDER'S TOOLKIT")
print("(Explaining Like to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: RECAP – WHAT IS STRING FORMATTING?
# ============================================================================
print("1. WHAT IS STRING FORMATTING? (A Quick Refresher)")
print("-" * 40)

print("""Imagine you have a form letter with blanks to fill in:
   'Dear ____, your score is ____.'

String formatting is the magic that fills those blanks with actual values.""")

print("\nIn Python, we have several ways:")
print("1. Old style (%) – like filling blanks with a list")
print("2. .format() method – more flexible")
print("3. f-strings (modern) – easiest, but not always customizable")

print("\nExample with .format():")
name = "Alice"
score = 95
message = "Dear {}, your score is {}.".format(name, score)
print(f"   '{message}'")

print("\nBut what if we want to change HOW the blanks are filled?")
print("That's where the Formatter class comes in – it lets us build our own filling rules!")

# ============================================================================
# SECTION 2: INTRODUCING THE FORMATTER CLASS
# ============================================================================
print("\n\n2. MEET THE FORMATTER – YOUR CUSTOM BUILDER")
print("-" * 40)

print("""The Formatter is like a robot that normally fills blanks in a standard way.
But you can teach it new tricks by creating a subclass.""")

print("\nFirst, let's import it:")
print("   from string import Formatter")

from string import Formatter

print("\nNow we can create a basic formatter and use its .format() method:")
fmt = Formatter()
result = fmt.format("Hello {}, your balance is {:.2f}", "Bob", 123.456)
print(f"   {result}")

print("\nThis is the same as the built-in str.format(). But now we can customize!")

# ============================================================================
# SECTION 3: THE FORMATTER'S METHODS – THE ROBOT'S INSTRUCTIONS
# ============================================================================
print("\n\n3. THE FORMATTER'S METHODS – HOW THE ROBOT WORKS")
print("-" * 40)

print("""The Formatter robot has several internal steps when it formats a string.
We can override these steps to change its behavior.""")

print("\n🔧 Main methods (in order of execution):")
print("   1. parse()        – splits the string into text and placeholders")
print("   2. get_value()     – fetches the value for a placeholder")
print("   3. convert_field() – applies conversion (!s, !r, !a)")
print("   4. format_field()  – applies format spec (:10.2f etc.)")
print("   5. vformat()       – orchestrates everything")
print("   6. format()        – the public method that starts it all")

print("\nLet's explore each one...")

# ============================================================================
# SECTION 4: UNDERSTANDING EACH METHOD (WITH SIMPLE EXAMPLES)
# ============================================================================
print("\n\n4. PEEKING UNDER THE HOOD – SIMPLE EXAMPLES")
print("-" * 40)

# We'll create a simple formatter and demonstrate what parse() returns
print("🔹 parse(format_string) – breaks the string into pieces")

fmt = Formatter()
format_string = "Hello {name}, you have {count:d} messages."
print(f"Format string: '{format_string}'")

parsed = list(fmt.parse(format_string))
print("\nparse() returns an iterable of tuples (literal_text, field_name, format_spec, conversion):")
for i, (literal, field, spec, conv) in enumerate(parsed):
    print(f"  Tuple {i}:")
    print(f"    literal_text = '{literal}'")
    print(f"    field_name   = '{field}'")
    print(f"    format_spec  = '{spec}'")
    print(f"    conversion   = {conv}")

print("\n🔹 get_value(key, args, kwargs) – gets the value for a field")
print("   (called for each field_name after parse)")

# We'll simulate by calling get_value manually
args = ("Alice", 5)
kwargs = {}
key = 0  # first positional argument
value = fmt.get_value(key, args, kwargs)
print(f"   fmt.get_value(0, {args}, {{}}) → {value}")

print("\n🔹 convert_field(value, conversion) – applies !s, !r, !a")

class MyFormatter(Formatter):
    def convert_field(self, value, conversion):
        print(f"   convert_field called with value={value}, conversion='{conversion}'")
        # Let's add a custom conversion: !u for uppercase string
        if conversion == 'u':
            return str(value).upper()
        # Otherwise use default
        return super().convert_field(value, conversion)

myfmt = MyFormatter()
result = myfmt.format("Hello {name!u}", name="Alice")
print(f"   Result with custom !u: '{result}'")

print("\n🔹 format_field(value, format_spec) – applies formatting like :.2f")

class DebugFormatter(Formatter):
    def format_field(self, value, format_spec):
        print(f"   format_field called: value={value}, spec='{format_spec}'")
        return super().format_field(value, format_spec)

debug_fmt = DebugFormatter()
result = debug_fmt.format("Price: {price:.2f}", price=19.995)
print(f"   Result: '{result}'")

print("\n🔹 vformat() – the brain that calls everything")
print("   You normally don't override this, but it's the core.")

print("\n🔹 format() – the public face, calls vformat()")

# ============================================================================
# SECTION 5: CUSTOMIZING FORMATTER – BUILDING YOUR OWN RULES
# ============================================================================
print("\n\n5. BUILDING A CUSTOM FORMATTER – A SIMPLE TEMPLATE ENGINE")
print("-" * 40)

print("""Let's create a formatter that:
   - Automatically capitalizes names (if field ends with '_name')
   - Masks credit card numbers (if field is 'cc')
   - Adds a default value if a key is missing
""")

class SmartFormatter(Formatter):
    def get_value(self, key, args, kwargs):
        """Try to get value; if missing, return '<missing>' instead of error."""
        try:
            return super().get_value(key, args, kwargs)
        except (IndexError, KeyError):
            return "<missing>"

    def format_field(self, value, format_spec):
        """Apply special rules based on field name (passed via format_spec)."""
        # format_spec can be used to pass extra info, but we'll use a trick:
        # we can't easily know the field name here, so we'll need to store it.
        # For simplicity, we'll assume we know the field from context.
        # Better: we could override vformat and store field names.
        # Let's keep it simple: just show we can customize.
        if format_spec == "capitalize":
            return str(value).capitalize()
        elif format_spec == "mask_cc":
            s = str(value)
            return "****-****-****-" + s[-4:] if len(s) >= 4 else s
        return super().format_field(value, format_spec)

# We need to pass the rule via format_spec, e.g., {name:capitalize}
smart = SmartFormatter()
template = "Customer: {name:capitalize}, Card: {cc:mask_cc}, Missing: {missing}"
result = smart.format(template, name="alice", cc="1234567890123456")
print(f"Template: '{template}'")
print(f"Result:   '{result}'")

print("\nWe could go further and use custom conversion flags (!c for capitalize, !m for mask).")
print("Let's add custom conversions instead:")

class EvenSmarterFormatter(Formatter):
    def convert_field(self, value, conversion):
        if conversion == 'c':
            return str(value).capitalize()
        elif conversion == 'm':
            s = str(value)
            return "****-****-****-" + s[-4:] if len(s) >= 4 else s
        return super().convert_field(value, conversion)

smarter = EvenSmarterFormatter()
template = "Customer: {name!c}, Card: {cc!m}"
result = smarter.format(template, name="alice", cc="1234567890123456")
print(f"Template: '{template}'")
print(f"Result:   '{result}'")

# ============================================================================
# SECTION 6: A MORE PRACTICAL EXAMPLE – LOGGING FORMATTER
# ============================================================================
print("\n\n6. PRACTICAL EXAMPLE: CUSTOM LOGGING FORMATTER")
print("-" * 40)

print("""Imagine you're writing a logging system. You want to format log messages
with timestamps, levels, and maybe color-code them.""")

import datetime

class LogFormatter(Formatter):
    def format_field(self, value, format_spec):
        # If the field is 'time', format it as HH:MM:SS
        if format_spec == 'time':
            return datetime.datetime.now().strftime("%H:%M:%S")
        # If field is 'level' and spec is 'color', add ANSI colors
        if format_spec == 'color':
            colors = {
                'INFO': '\033[92m',    # green
                'WARNING': '\033[93m', # yellow
                'ERROR': '\033[91m',   # red
            }
            reset = '\033[0m'
            return f"{colors.get(value, '')}{value}{reset}"
        return super().format_field(value, format_spec)

log_fmt = LogFormatter()
log_template = "[{time:time}] {level:color}: {message}"
print(f"Log template: '{log_template}'")

# Simulate log entries
for level, msg in [("INFO", "System started"), ("WARNING", "Low disk space"), ("ERROR", "Connection lost")]:
    print(log_fmt.format(log_template, level=level, message=msg))

print("\n(Note: ANSI colors may not show in all terminals, but the idea is clear.)")

# ============================================================================
# SECTION 7: THE OTHER METHODS – check_unused_args
# ============================================================================
print("\n\n7. CHECKING UNUSED ARGUMENTS – BEING NEAT")
print("-" * 40)

print("""Sometimes you want to ensure that every argument you passed was actually used.
The check_unused_args() method can raise an error if there are extras.""")

class StrictFormatter(Formatter):
    def check_unused_args(self, used_args, args, kwargs):
        # used_args is a set of keys (integers for positional, strings for named)
        # args is the tuple of positional arguments
        # kwargs is the dict of keyword arguments
        unused_pos = set(range(len(args))) - used_args
        unused_kw = set(kwargs.keys()) - used_args
        if unused_pos or unused_kw:
            raise ValueError(f"Unused arguments: positions {unused_pos}, keys {unused_kw}")

strict = StrictFormatter()
try:
    strict.format("Hello {name}", name="Alice", extra="Bob")
except ValueError as e:
    print(f"   Error: {e}")

# ============================================================================
# SECTION 8: PUTTING IT ALL TOGETHER – A CUSTOM TEMPLATE ENGINE
# ============================================================================
print("\n\n8. PUTTING IT ALL TOGETHER – A MINI TEMPLATE ENGINE")
print("-" * 40)

print("""Let's create a small template engine that:
   - Uses {{ ... }} for placeholders (instead of {})
   - Supports if‑conditions (imaginary)
   - Auto‑escapes HTML
""")

import html

class TemplateEngine(Formatter):
    def __init__(self, delimiter='{{', end_delimiter='}}'):
        self.delimiter = delimiter
        self.end_delimiter = end_delimiter
        super().__init__()

    def parse(self, format_string):
        # We override parse to look for our custom delimiters
        # This is a simplified version – in reality you'd need a proper parser.
        # For demonstration, we'll just replace {{ with { and }} with } and then use normal parse.
        # But that would break if braces are nested. We'll keep it simple.
        modified = format_string.replace(self.delimiter, '{').replace(self.end_delimiter, '}')
        return super().parse(modified)

    def convert_field(self, value, conversion):
        if conversion == 'e':
            return html.escape(str(value))
        return super().convert_field(value, conversion)

engine = TemplateEngine()
template = "Hello {{name!e}}, your balance is {{balance:.2f}}"
print(f"Template: {template}")
result = engine.format(template, name="<b>Alice</b>", balance=123.456)
print(f"Result:   {result}")

print("\n(Notice the HTML tags are escaped: <b> becomes &lt;b&gt;.)")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================
print("\n\n" + "=" * 60)
print("PRACTICE EXERCISES")
print("=" * 60)

print("""
Exercise 1: Currency Formatter
-------------------------------
Create a custom formatter that adds a currency symbol based on a 'currency' field.
Use a custom conversion like !usd, !eur, etc.

Exercise 2: Pluralize
----------------------
Write a formatter that automatically pluralizes words based on a count.
E.g., "You have {count} {item:pluralize(count)}" where if count != 1, add 's'.

Exercise 3: Safe Dictionary Access
-----------------------------------
Create a formatter that, when a key is missing, returns 'N/A' instead of raising KeyError.

Exercise 4: Date Formatting Shortcuts
--------------------------------------
Allow format spec like :date to format a datetime object as YYYY-MM-DD,
and :time as HH:MM.

Exercise 5: Full Custom Parser
-------------------------------
Extend the TemplateEngine to actually parse custom delimiters properly (not just replace).
(Hint: you need to scan the string manually.)
""")

print("\n" + "=" * 40)
print("HINTS (Try yourself first!)")
print("=" * 40)

print("""
Hint 1: Use conversion flags (!usd) and in convert_field, check conversion and add symbol.
Hint 2: You need the count value; either pass it twice or use a custom field name.
Hint 3: Override get_value and catch KeyError/IndexError.
Hint 4: In format_field, if format_spec is 'date' or 'time', format accordingly.
Hint 5: Write a custom parse that yields tuples; you'll need to find {{ and }}.
""")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS – CUSTOM STRING FORMATTING")
print("=" * 60)

print("""
1. 🎨 Formatter class lets you customize how strings are built from templates.
2. 🧩 Override methods: parse, get_value, convert_field, format_field, check_unused_args.
3. 🚀 Custom conversions (!c, !m) and format specs (:mask_cc) give you endless flexibility.
4. 🔧 Use get_value to handle missing keys gracefully.
5. 🛡️ Override convert_field for type conversions (str, repr, ascii, or your own).
6. 🧪 Override format_field to apply special formatting rules.
7. 📦 Use check_unused_args to enforce that all arguments are used.

Remember: The Formatter is the engine behind str.format(). By learning it,
you become a true string‑bending wizard! 🧙‍♂️
""")

print("\n" + "=" * 60)
print("SAVE AS: Custom_String_Formatting.py")
print("RUN WITH: python Custom_String_Formatting.py")
print("=" * 60)