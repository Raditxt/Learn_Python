# Working_With_Variables.py
"""
This script explains how to work with variables in Python in a simple way
that can be understood even by a 5-year-old child (using the Feynman Technique).

Feynman Technique: Explaining complex concepts with simple language, analogies,
and concrete examples.
"""

print("=" * 60)
print("WORKING WITH VARIABLES IN PYTHON")
print("(Like Explaining to a 5-Year-Old)")
print("=" * 60)
print()

# ============================================================================
# SECTION 1: VARIABLES IN EXPRESSIONS (FORMULAS)
# ============================================================================
print("1. VARIABLES IN EXPRESSIONS (CREATING FORMULAS)")
print("-" * 40)

print("""Expressions are mathematical calculations.
Variables make expressions more FLEXIBLE!""")

print("\nExample: Calculating circle circumference")
print("Formula: 2 × π × r")

# Using variables in formulas
pi = 3.1416
radius = 10

circumference = 2 * pi * radius
print(f"\nIf radius = {radius}")
print(f"Circumference = 2 × {pi} × {radius}")
print(f"Circumference = {circumference}")

# Change radius value
radius = 20
circumference = 2 * pi * radius
print(f"\nNow radius = {radius}")
print(f"Circumference = 2 × {pi} × {radius}")
print(f"Circumference = {circumference}")

print("\nAdvantages of using variables:")
print("1. No need to rewrite constant values (like π)")
print("2. Easy to change values (just modify the variable)")
print("3. Code is easier to read and understand")

# ============================================================================
# SECTION 2: COUNTER - COUNTING QUANTITIES
# ============================================================================
print("\n\n2. COUNTER - COUNTING QUANTITIES")
print("-" * 40)

print("""A counter is like an 'add one' calculator.
Every time we find something we're looking for, we add 1.""")

# Example: Counting how many fruits in a list
print("\nExample: Counting how many apples in the basket")

basket = ["apple", "orange", "apple", "grape", "apple", "orange", "apple"]
print(f"Basket contains: {basket}")

# Create counter for apples
apple_count = 0  # Start from 0

for fruit in basket:
    if fruit == "apple":
        apple_count += 1  # Add 1 every time we find an apple
        print(f"Found apple! Now there are {apple_count} apples")

print(f"\nTotal apples in basket: {apple_count}")

print("\nThe analogy:")
print("""• Counter is like a digital abacus/tally counter
• Every time an event occurs, we move one bead
• Finally we know the total occurrences""")

# Another example: Counting even numbers
print("\n\nAnother example: Counting even numbers in a list")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Number list: {numbers}")

even_count = 0
for n in numbers:
    if n % 2 == 0:  # n % 2 = remainder when divided by 2, if 0 means even
        even_count += 1
        print(f"{n} is even. Total even: {even_count}")

print(f"\nTotal even numbers: {even_count}")

# ============================================================================
# SECTION 3: ACCUMULATOR - SUMMING VALUES
# ============================================================================
print("\n\n3. ACCUMULATOR - SUMMING VALUES")
print("-" * 40)

print("""An accumulator is like a piggy bank.
We put in money little by little, eventually it becomes a lot!""")

# Example: Summing numbers
print("\nExample: Summing all numbers in a list")

allowance = [1000, 1500, 2000, 500, 3000]  # Weekly allowance
print(f"Weekly allowance: {allowance}")

total_money = 0  # Empty piggy bank

for money in allowance:
    total_money += money  # Add to piggy bank
    print(f"Add ${money} → Total now: ${total_money}")

print(f"\nTotal weekly allowance: ${total_money}")

# Calculate average
number_of_days = len(allowance)  # len() counts the number of items
average = total_money / number_of_days
print(f"Average per day: ${total_money} ÷ {number_of_days} = ${average}")

print("\nDifference between Counter vs Accumulator:")
print("• Counter: Counts QUANTITY (always add 1)")
print("• Accumulator: Sums VALUES (add the value itself)")

# ============================================================================
# SECTION 4: TEMPORARY VARIABLES
# ============================================================================
print("\n\n4. TEMPORARY VARIABLES")
print("-" * 40)

print("""Temporary variables are like extra plates in the kitchen.
We use them briefly to help with work, then stop using them.""")

# Classic example: Swapping two values
print("\nExample: Swapping contents of two glasses")
print("Glass A contains milk, Glass B contains juice")

milk = "milk"
juice = "juice"
print(f"Before: Glass A = {milk}, Glass B = {juice}")

# Use a third temporary glass
temp_glass = milk       # Move milk to temporary glass
milk = juice            # Fill glass A with juice
juice = temp_glass      # Fill glass B with milk from temporary glass

print(f"After: Glass A = {milk}, Glass B = {juice}")
print("Temporary glass is no longer needed!")

# Python trick: Swap without temporary variable!
print("\n\nPython trick: Swap without temporary variable!")
a = "milk"
b = "juice"
print(f"Before: a = {a}, b = {b}")

a, b = b, a  # Python magic! Swap directly
print(f"After: a = {a}, b = {b}")

print("\nWhen to use temporary variables?")
print("""1. When calculating step by step
2. When need to store value before it changes
3. To make code easier to read""")

# ============================================================================
# SECTION 5: BOOLEAN FLAGS
# ============================================================================
print("\n\n5. BOOLEAN FLAGS")
print("-" * 40)

print("""Boolean flags are like traffic lights.
Only two states: GREEN (True) or RED (False).""")

# Example: Flag for light control
print("\nExample: Automatic light system")

light_on = False  # Initially light is off
print(f"Initial status: Light on = {light_on}")

# Simulate switch button
print("\nButton pressed...")
light_on = not light_on  # not flips True ↔ False
print(f"Current status: Light on = {light_on}")

print("\nButton pressed again...")
light_on = not light_on
print(f"Current status: Light on = {light_on}")

# Example: Room temperature alarm system
print("\n\nExample: Room temperature alarm system")
temperature = 28  # Degrees Celsius
heat_limit = 30

too_hot = temperature > heat_limit  # Will become True or False

if too_hot:
    print(f"⚠️ WARNING! Temperature {temperature}°C is too hot!")
    print("Turn on the AC!")
else:
    print(f"✅ Temperature {temperature}°C is normal.")
    print("AC stays off.")

print("\nGood naming for Boolean flags:")
print("• Use prefixes is_, has_, can_, should_")
print("• Example: is_logged_in, has_permission, can_edit, should_update")
print("• Name directly explains the meaning (True/False for what?)")

# ============================================================================
# SECTION 6: LOOP VARIABLES
# ============================================================================
print("\n\n6. LOOP VARIABLES")
print("-" * 40)

print("""Loop variables are like a pointing finger.
Each time it moves, it points to the next item in the list.""")

# Simple example: Loop through list of colors
print("\nExample: Looking at all rainbow colors")

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print(f"Rainbow colors: {rainbow_colors}")

print("\nUsing loop to see one by one:")
for color in rainbow_colors:  # 'color' is the loop variable
    print(f"  • {color}")

print("\nUsing enumerate() to get sequence numbers:")
for number, color in enumerate(rainbow_colors, start=1):  # Two loop variables!
    print(f"  {number}. {color}")

# Example: Loop with dictionary
print("\n\nExample: Student data (using dictionary)")
student = {
    "name": "John",
    "age": 8,
    "class": "3A",
    "hobbies": ["reading", "swimming"]
}

print("Student data:")
for key, value in student.items():  # Two loop variables: key and value
    print(f"  {key}: {value}")

print("\nSpecial loop variables:")
print("""• Use _ (underscore) for variables that aren't used
• Example: for _, value in data:  # We only need value, not key""")

# ============================================================================
# SECTION 7: DATA STORAGE VARIABLES
# ============================================================================
print("\n\n7. DATA STORAGE VARIABLES")
print("-" * 40)

print("""Storage variables are like a filing cabinet.
Can store lots of organized data in one place.""")

# Example: Simple phone book
print("\nExample: Family phone book")

phone_book = [
    ("Mom", "0811-1111-111", "mom@email.com"),
    ("Dad", "0812-2222-222", "dad@email.com"),
    ("Sister", "0813-3333-333", "sister@email.com"),
    ("Brother", "0814-4444-444", "brother@email.com")
]

print(f"Total contacts: {len(phone_book)}")

print("\nDisplaying all contacts:")
for name, phone, email in phone_book:  # Three variables at once!
    print(f"  {name}: {phone}")

print("\nSearching for Mom's number:")
for name, phone, email in phone_book:
    if name == "Mom":
        print(f"  Mom's number: {phone}")
        break  # Stop after finding

# Example: Shopping cart
print("\n\nExample: Online shopping cart")

shopping_cart = {
    "apple": {"price": 10000, "quantity": 3},
    "milk": {"price": 25000, "quantity": 1},
    "bread": {"price": 15000, "quantity": 2}
}

print("Shopping cart contents:")
total_purchase = 0

for item, info in shopping_cart.items():
    subtotal = info["price"] * info["quantity"]
    total_purchase += subtotal
    print(f"  {item}: {info['quantity']} × ${info['price']} = ${subtotal}")

print(f"\nTotal purchase: ${total_purchase}")

# ============================================================================
# SECTION 8: REAL CASE - SIMPLE STORE PROGRAM
# ============================================================================
print("\n\n8. REAL CASE: SIMPLE STORE PROGRAM")
print("-" * 40)

print("""Let's combine all concepts in one program!
Program: Simple store cashier system.""")

# Product data
products = {
    "P001": {"name": "Pencil", "price": 2000},
    "P002": {"name": "Book", "price": 5000},
    "P003": {"name": "Eraser", "price": 1000},
    "P004": {"name": "Ruler", "price": 3000}
}

print("\nProduct list:")
for code, info in products.items():
    print(f"  {code}: {info['name']} - ${info['price']}")

# Purchase simulation
print("\n" + "=" * 40)
print("PURCHASE SIMULATION")
print("=" * 40)

cart = []
total_price = 0  # Accumulator
item_count = 0  # Counter

# Buy several items
purchases = [
    ("P001", 2),  # 2 pencils
    ("P002", 1),  # 1 book
    ("P003", 3),  # 3 erasers
]

print("\nPurchase details:")
for product_code, qty in purchases:
    if product_code in products:
        name = products[product_code]["name"]
        unit_price = products[product_code]["price"]
        subtotal = unit_price * qty
        
        cart.append((name, qty, unit_price, subtotal))
        total_price += subtotal
        item_count += qty
        
        print(f"  {name} ({qty} × ${unit_price}) = ${subtotal}")

# Calculate discount
print("\n" + "=" * 40)
print("TOTAL AND DISCOUNT")
print("=" * 40)

print(f"Total items: {item_count}")
print(f"Total price: ${total_price}")

# Boolean flag for discount
eligible_for_discount = total_price > 15000
discount = 0

if eligible_for_discount:
    discount = total_price * 0.1  # 10% discount
    print(f"Congratulations! You get 10% discount: ${discount}")
else:
    print(f"No discount yet (minimum purchase $15,000)")

amount_to_pay = total_price - discount
print(f"Total amount to pay: ${amount_to_pay}")

# ============================================================================
# CONCLUSION
# ============================================================================
print("\n\n" + "=" * 60)
print("CONCLUSION ON WORKING WITH VARIABLES")
print("=" * 60)

print("""
1. VARIABLES IN EXPRESSIONS:
   • Make formulas more flexible
   • Easy to change values without changing formula

2. COUNTER:
   • For counting QUANTITY of occurrences
   • Always start from 0, add 1 per occurrence
   • Example: counting how many apples

3. ACCUMULATOR:
   • For summing VALUES
   • Always start from 0, add the value itself
   • Example: calculating total shopping price

4. TEMPORARY VARIABLES:
   • Help with work temporarily
   • Example: swapping two variable values
   • Python trick: a, b = b, a

5. BOOLEAN FLAGS:
   • Only have two values: True or False
   • For yes/no, on/off control
   • Good names: is_..., has_..., can_...

6. LOOP VARIABLES:
   • Point to current item in loop
   • Can get value and sequence number
   • Example: for number, item in enumerate(data)

7. DATA STORAGE VARIABLES:
   • Store organized data (list, dict)
   • Example: phone book, shopping cart

REMEMBER: Variables are our FRIENDS in programming!
The better we understand how to use them, the easier it is to create programs!
""")

print("=" * 60)
print("CONGRATULATIONS! NOW YOU CAN WORK WITH VARIABLES!")
print("=" * 60)

# ============================================================================
# EXERCISES FOR THE READER
# ============================================================================
print("\n\nEXERCISES FOR YOU:")
print("-" * 40)

print("""1. CREATE A COUNTER:
   • Count how many vowels (a,i,u,e,o) are in your name
   
2. CREATE AN ACCUMULATOR:
   • Calculate total price of your 5 favorite items
   • Calculate their average price
   
3. CREATE A BOOLEAN FLAG:
   • Check if your age is old enough to watch PG-13 movies (13+)
   
4. CREATE A LOOP WITH VARIABLES:
   • Make a list of 5 friends with their sequence numbers
   
5. COMBINE EVERYTHING:
   • Create a simple program to calculate average exam scores
   • With counter, accumulator, and pass/fail condition""")

print("\nBest way to learn:")
print("1. Read the code above")
print("2. Close it, try to rewrite in your own words")
print("3. Modify, experiment, make errors, learn from errors")
print("4. Teach someone else (Feynman Technique)")

print("\n" + "=" * 60)
print("SAVE AS: Working_With_Variables.py")
print("RUN WITH: python Working_With_Variables.py")
print("=" * 60)