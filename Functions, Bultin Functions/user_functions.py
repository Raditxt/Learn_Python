"""
Materi: Mendefinisikan dan Menggunakan Fungsi Sendiri (User-Defined Functions)
Berdasarkan tutorial Real Python: Defining Your Own Python Function

Topik:
1. Dasar def, parameter, argumen posisi dan keyword
2. Return value, side effects, early exit
3. Default argument values
4. *args (variable positional arguments)
5. **kwargs (variable keyword arguments)
6. Positional-only arguments (/) dan keyword-only arguments (*)
7. Unpacking iterable (*) dan dictionary (**) saat pemanggilan
8. Docstring dan annotations (type hints)
9. Async functions (pendahuluan)
"""

print("=" * 60)
print("1. DASAR DEFINING FUNCTION")
print("=" * 60)

def greet(name):
    """Menyapa seseorang."""
    print(f"Hello, {name}!")

greet("Pythonista")  # positional argument

print("\n" + "=" * 60)
print("2. POSITIONAL VS KEYWORD ARGUMENTS")
print("=" * 60)

def calculate_cost(item, quantity, price):
    print(f"{quantity} {item} cost ${quantity * price:.2f}")

# Positional arguments (harus urut)
calculate_cost("bananas", 6, 0.74)

# Keyword arguments (bebas urut)
calculate_cost(price=0.74, quantity=6, item="bananas")

# Campuran: positional dulu, baru keyword
calculate_cost("bananas", quantity=6, price=0.74)

# Error: keyword setelah positional tidak masalah, tapi positional setelah keyword tidak boleh
# calculate_cost(item="bananas", 6, 0.74)  # SyntaxError

print("\n" + "=" * 60)
print("3. RETURN VALUE DAN SIDE EFFECTS")
print("=" * 60)

# Fungsi dengan side effect (mengubah mutable object)
def double_in_place(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2

data = [1, 2, 3, 4, 5]
double_in_place(data)
print(f"Setelah double_in_place: {data}")  # data asli berubah

# Fungsi tanpa side effect (return value baru)
def double_new(numbers):
    return [n * 2 for n in numbers]

data2 = [1, 2, 3, 4, 5]
result = double_new(data2)
print(f"Original: {data2}")
print(f"Hasil double_new: {result}")

# Return multiple values (sebagai tuple)
def create_point(x, y):
    return x, y

point = create_point(3, 4)
print(f"create_point(3,4) = {point}")

# Early exit dengan return
def find_user(username, user_list):
    for user in user_list:
        if user["username"] == username:
            return user
    return None

users = [
    {"username": "alice", "email": "alice@example.com"},
    {"username": "bob", "email": "bob@example.com"},
]
alice = find_user("alice", users)
print(f"find_user('alice') = {alice}")
print(f"find_user('charlie') = {find_user('charlie', users)}")

# Boolean-valued function (predicate)
def is_even(number):
    return number % 2 == 0

print(f"is_even(4) = {is_even(4)}")
print(f"is_even(5) = {is_even(5)}")

print("\n" + "=" * 60)
print("4. DEFAULT ARGUMENT VALUES")
print("=" * 60)

def greet_with_default(name="World"):
    print(f"Hello, {name}!")

greet_with_default()          # menggunakan default
greet_with_default("Python")  # override default

def greet_verbose(name, verbose=False):
    if verbose:
        print(f"Hello, {name}! Welcome to Real Python!")
    else:
        print(f"Hello, {name}!")

greet_verbose("Alice")
greet_verbose("Bob", verbose=True)

# PERINGATAN: default argument mutable (jangan gunakan list/dict sebagai default)
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

print(f"append_to(1) = {append_to(1)}")
print(f"append_to(2) = {append_to(2)}")
print(f"append_to(3) = {append_to(3)}")

print("\n" + "=" * 60)
print("5. VARIABLE NUMBER OF ARGUMENTS: *args")
print("=" * 60)

# *args mengumpulkan positional arguments menjadi tuple
def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(f"average(1,2,3,4,5) = {average(1,2,3,4,5)}")
print(f"average(10,20) = {average(10,20)}")
print(f"average() = {average()}")

def print_all(*args):
    print("args:", args)

print_all(1, 2, 3, "a", "b")

print("\n" + "=" * 60)
print("6. VARIABLE NUMBER OF KEYWORD ARGUMENTS: **kwargs")
print("=" * 60)

# **kwargs mengumpulkan keyword arguments menjadi dict
def report(**kwargs):
    print("Report:")
    for key, value in kwargs.items():
        print(f"  {key.capitalize()}: {value}")

report(name="Keyboard", price=19.99, quantity=5)

def display_info(**kwargs):
    print("kwargs:", kwargs)

display_info(a=1, b=2, c=3)

print("\n" + "=" * 60)
print("7. KOMBINASI *args DAN **kwargs")
print("=" * 60)

def flexible_function(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=30)

def mixed(a, b, *args, **kwargs):
    print(f"a={a}, b={b}, args={args}, kwargs={kwargs}")

mixed(10, 20, 30, 40, x=100, y=200)

print("\n" + "=" * 60)
print("8. POSITIONAL-ONLY ARGUMENTS (/)")
print("=" * 60)

# Parameter di kiri / harus diberikan secara positional
def format_name(first_name, last_name, /, title=None):
    full = f"{first_name} {last_name}"
    if title:
        full = f"{title} {full}"
    return full

# Benar
print(format_name("Jane", "Doe"))
print(format_name("John", "Doe", title="Dr."))

# Salah: last_name sebagai keyword argument akan error
# print(format_name("John", last_name="Doe"))  # TypeError

print("\n" + "=" * 60)
print("9. KEYWORD-ONLY ARGUMENTS (*)")
print("=" * 60)

# Parameter setelah * harus diberikan sebagai keyword
def calculate(x, y, *, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
    else:
        raise ValueError("Invalid operator")

print(f"calculate(3, 4, operator='+') = {calculate(3, 4, operator='+')}")
print(f"calculate(3, 4, operator='*') = {calculate(3, 4, operator='*')}")

# Salah: operator sebagai positional
# calculate(3, 4, "+")  # TypeError

def sum_numbers(*numbers, precision=2):
    return round(sum(numbers), precision)

print(f"sum_numbers(1.3467, 2.5243, precision=3) = {sum_numbers(1.3467, 2.5243, precision=3)}")
print(f"sum_numbers(1.3467, 2.5243, 3) = {sum_numbers(1.3467, 2.5243, 3)}")

print("\n" + "=" * 60)
print("10. UNPACKING ARGUMENTS SAAT PEMANGGILAN")
print("=" * 60)

def three_args(x, y, z):
    print(f"x={x}, y={y}, z={z}")

# Unpacking iterable ke positional arguments
numbers = [1, 2, 3]
three_args(*numbers)  # sama dengan three_args(1,2,3)

# Unpacking dictionary ke keyword arguments
data_dict = {"x": 10, "y": 20, "z": 30}
three_args(**data_dict)  # sama dengan three_args(x=10,y=20,z=30)

# Kombinasi
three_args(1, *[2, 3])  # x=1, lalu unpack [2,3] ke y,z
three_args(1, z=3, **{"y": 2})

print("\n" + "=" * 60)
print("11. DOCSTRINGS (Dokumentasi Fungsi)")
print("=" * 60)

def multiply(a, b):
    """
    Mengalikan dua bilangan.

    Args:
        a (int/float): Bilangan pertama
        b (int/float): Bilangan kedua

    Returns:
        int/float: Hasil perkalian a * b

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b

print(f"multiply(3,4) = {multiply(3,4)}")
print(f"Dokumentasi: {multiply.__doc__[:60]}...")
# help(multiply)  # untuk melihat docstring lengkap

print("\n" + "=" * 60)
print("12. ANNOTATIONS (TYPE HINTS)")
print("=" * 60)

def add_numbers(a: int | float, b: int | float) -> int | float:
    """Menjumlahkan dua angka dengan type hints."""
    return a + b

print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")
print(f"Annotations: {add_numbers.__annotations__}")

# Catatan: Python tidak memeriksa tipe saat runtime
print(f"add_numbers('5', '3') = {add_numbers('5', '3')}")  # tetap bisa

print("\n" + "=" * 60)
print("13. CLOSURE (Fungsi di dalam fungsi)")
print("=" * 60)

def generate_power(exponent):
    """Mengembalikan fungsi pangkat dengan eksponen tetap."""
    def power(base):
        return base ** exponent
    return power

square = generate_power(2)
cube = generate_power(3)

print(f"square(5) = {square(5)}")
print(f"cube(5) = {cube(5)}")

print("\n" + "=" * 60)
print("14. ASYNCHRONOUS FUNCTIONS (Pengenalan)")
print("=" * 60)

import asyncio

async def fetch_data():
    """Simulasi pengambilan data dari jaringan."""
    print("Fetching data...")
    await asyncio.sleep(1)  # simulasi delay
    print("Data received!")
    return {"user": "john", "status": "active"}

async def main():
    data = await fetch_data()
    print(f"Result: {data}")

# Menjalankan async function
# asyncio.run(main())  # dijalankan jika ingin melihat

print("Fungsi async didefinisikan dengan 'async def'")
print("Memanggil async function mengembalikan coroutine object")
print(f"fetch_data() = {fetch_data()}")  # coroutine object

print("\n" + "=" * 60)
print("RINGKASAN FITUR")
print("=" * 60)
print("- def: mendefinisikan fungsi")
print("- Positional arguments: sesuai urutan")
print("- Keyword arguments: arg=value, bebas urut")
print("- return: mengembalikan nilai (default None)")
print("- Default argument: nilai default untuk parameter")
print("- *args: menampung banyak positional arguments (tuple)")
print("- **kwargs: menampung banyak keyword arguments (dict)")
print("- / : positional-only arguments")
print("- * : keyword-only arguments")
print("- Unpacking (*iterable, **dict) saat pemanggilan")
print("- Docstring: dokumentasi dengan triple quotes")
print("- Annotations: type hints (opsional)")
print("- async def: fungsi asynchronous")