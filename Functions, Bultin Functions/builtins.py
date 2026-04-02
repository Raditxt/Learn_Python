"""
Materi: Built-in Functions (Fungsi Bawaan Python)
Daftar lengkap: https://docs.python.org/3/library/functions.html
Fungsi-fungsi ini selalu tersedia tanpa perlu import.
"""

print("=" * 60)
print("1. FUNGSI NUMERIK / MATEMATIKA")
print("=" * 60)

# abs() - nilai mutlak
print(f"abs(-5) = {abs(-5)}")
print(f"abs(3+4j) = {abs(3+4j)}")  # magnitude untuk kompleks

# divmod() - quotient dan remainder
quot, rem = divmod(17, 5)
print(f"divmod(17, 5) = ({quot}, {rem})")

# pow() - pangkat dengan modulo opsional
print(f"pow(2, 10) = {pow(2, 10)}")
print(f"pow(2, 10, 100) = {pow(2, 10, 100)}")  # (2^10) % 100
# modular inverse: pow(38, -1, 97)  # Python 3.8+

# round() - pembulatan
print(f"round(3.14159, 2) = {round(3.14159, 2)}")
print(f"round(2.675, 2) = {round(2.675, 2)}")  # perhatikan perilaku float

# sum() - menjumlahkan iterable
angka = [1, 2, 3, 4]
print(f"sum([1,2,3,4]) = {sum(angka)}")
print(f"sum([1,2,3,4], start=10) = {sum(angka, 10)}")

# min() dan max()
print(f"min([5,2,8,1]) = {min([5,2,8,1])}")
print(f"max([5,2,8,1]) = {max([5,2,8,1])}")
print(f"min('abcde') = {min('abcde')}")  # berdasarkan nilai Unicode
print(f"max('abcde') = {max('abcde')}")

# min/max dengan key
data = ["apple", "banana", "cherry"]
print(f"min panjang string: {min(data, key=len)}")
print(f"max panjang string: {max(data, key=len)}")

print("\n" + "=" * 60)
print("2. KONVERSI TIPE DATA")
print("=" * 60)

# int(), float(), complex(), str(), bool()
print(f"int('123') = {int('123')}")
print(f"int(45.67) = {int(45.67)}")  # truncate menuju nol
print(f"float('3.14') = {float('3.14')}")
print(f"complex(2, 3) = {complex(2, 3)}")
print(f"str(123) = {str(123)}")
print(f"bool(0) = {bool(0)}")
print(f"bool('hello') = {bool('hello')}")

# bin(), oct(), hex() - representasi biner/oktal/hexadesimal
print(f"bin(42) = {bin(42)}")
print(f"oct(42) = {oct(42)}")
print(f"hex(42) = {hex(42)}")

# chr() dan ord() - Unicode
print(f"chr(65) = {chr(65)}")
print(f"ord('A') = {ord('A')}")
print(f"ord('€') = {ord('€')}")

# list(), tuple(), set(), frozenset(), dict()
print(f"list('abc') = {list('abc')}")
print(f"tuple([1,2,3]) = {tuple([1,2,3])}")
print(f"set([1,2,2,3]) = {set([1,2,2,3])}")
print(f"dict([('a',1), ('b',2)]) = {dict([('a',1), ('b',2)])}")

# bytearray dan bytes
ba = bytearray([65, 66, 67])
print(f"bytearray([65,66,67]) = {ba}")
b = bytes([65,66,67])
print(f"bytes([65,66,67]) = {b}")

print("\n" + "=" * 60)
print("3. FUNGSI UNTUK ITERABLE DAN SEQUENCE")
print("=" * 60)

# len() - panjang
print(f"len([1,2,3]) = {len([1,2,3])}")

# range() - menghasilkan urutan angka
r = range(5)
print(f"list(range(5)) = {list(r)}")
print(f"list(range(2,10,2)) = {list(range(2,10,2))}")

# enumerate() - index dan value
buah = ["apel", "pisang", "ceri"]
for i, item in enumerate(buah, start=1):
    print(f"  enumerate start=1: {i} -> {item}")

# zip() - menggabungkan beberapa iterable
nama = ["Ali", "Budi", "Cici"]
umur = [25, 30, 35]
for n, u in zip(nama, umur):
    print(f"  zip: {n} berumur {u}")
# zip dengan strict=True (Python 3.10+)
try:
    list(zip([1,2], ['a','b','c'], strict=True))
except ValueError as e:
    print(f"  zip strict=True error: {e}")

# reversed() - iterator mundur
print(f"list(reversed([1,2,3])) = {list(reversed([1,2,3]))}")

# sorted() - mengembalikan list baru terurut
print(f"sorted([3,1,4,2]) = {sorted([3,1,4,2])}")
print(f"sorted([3,1,4,2], reverse=True) = {sorted([3,1,4,2], reverse=True)}")
print(f"sorted(['banana','apple','cherry'], key=len) = {sorted(['banana','apple','cherry'], key=len)}")

# filter() - menyaring berdasarkan fungsi
def is_genap(x):
    return x % 2 == 0
print(f"list(filter(is_genap, [1,2,3,4,5])) = {list(filter(is_genap, [1,2,3,4,5]))}")

# map() - menerapkan fungsi ke setiap elemen
def kuadrat(x):
    return x ** 2
print(f"list(map(kuadrat, [1,2,3,4])) = {list(map(kuadrat, [1,2,3,4]))}")

# all() dan any()
print(f"all([True, True, False]) = {all([True, True, False])}")
print(f"any([True, True, False]) = {any([True, True, False])}")
print(f"all([1,2,3]) = {all([1,2,3])}")  # non-zero True
print(f"any([0,0,1]) = {any([0,0,1])}")

print("\n" + "=" * 60)
print("4. FUNGSI INPUT/OUTPUT DAN EKSEKUSI")
print("=" * 60)

# print() - output
print("print('Hello', 'world', sep='-', end='!\\n') -> ", end="")
print("Hello", "world", sep="-", end="!\n")

# input() - input dari user (contoh dikomentari)
# nama = input("Masukkan nama: ")
# print(f"Halo {nama}")

# open() - membuka file (contoh singkat)
with open("temp.txt", "w") as f:
    f.write("Contoh teks")
with open("temp.txt", "r") as f:
    print(f"  Isi file: {f.read()}")
import os
os.remove("temp.txt")

# eval() - mengevaluasi string expression (HATI-HATI, jangan untuk input user)
x = 5
print(f"eval('x + 2') = {eval('x + 2')}")

# exec() - mengeksekusi kode dinamis (HATI-HATI)
exec("a = 10\nprint(f'  exec: a = {a}')")

# compile() - mengompilasi kode ke object code
kode = compile("print('  compile: hello')", '<string>', 'exec')
exec(kode)

# breakpoint() - masuk ke debugger (Python 3.7+)
# breakpoint()  # akan memanggil pdb jika dijalankan

print("\n" + "=" * 60)
print("5. FUNGSI INTROSPEKSI DAN ATRIBUT OBJEK")
print("=" * 60)

# type() - tipe data objek
print(f"type(123) = {type(123)}")
print(f"type('abc') = {type('abc')}")

# isinstance() dan issubclass()
print(f"isinstance(5, int) = {isinstance(5, int)}")
print(f"issubclass(bool, int) = {issubclass(bool, int)}")

# id() - identitas unik objek
a = 100
print(f"id(a) = {id(a)}")

# dir() - daftar atribut
print(f"dir(str)[:5] = {dir(str)[:5]} ... (singkat)")

# vars() - __dict__ objek (tanpa argumen seperti locals)
class Demo:
    def __init__(self):
        self.x = 1
        self.y = 2
d = Demo()
print(f"vars(d) = {vars(d)}")

# locals() dan globals()
print(f"globals() memiliki kunci: {list(globals().keys())[:5]} ...")
print(f"locals() dalam fungsi: ", end="")
def func():
    lokal = 42
    print(locals().get('lokal'))
func()

# hasattr(), getattr(), setattr(), delattr()
class Person:
    name = "Unknown"
p = Person()
print(f"hasattr(p, 'name') = {hasattr(p, 'name')}")
print(f"getattr(p, 'name') = {getattr(p, 'name')}")
setattr(p, 'name', 'Budi')
print(f"setattr -> p.name = {p.name}")
delattr(p, 'name')
print(f"setelah delattr, hasattr(p,'name') = {hasattr(p, 'name')}")

# callable() - apakah objek bisa dipanggil?
def my_func(): pass
print(f"callable(my_func) = {callable(my_func)}")
print(f"callable(123) = {callable(123)}")

# help() - membuka dokumentasi (interaktif, tidak dijalankan di sini)
# help(print)

print("\n" + "=" * 60)
print("6. FUNGSI LAINNYA")
print("=" * 60)

# hash() - nilai hash untuk objek immutable
print(f"hash('python') = {hash('python')}")

# repr() vs str()
class Test:
    def __str__(self):
        return "str representation"
    def __repr__(self):
        return "repr representation"
t = Test()
print(f"str(t) = {str(t)}")
print(f"repr(t) = {repr(t)}")

# ascii() - repr dengan escape non-ASCII
print(f"ascii('café') = {ascii('café')}")

# format() - formatting nilai
print(f"format(123, '08x') = {format(123, '08x')}")

# slice() - membuat objek slice
s = slice(1, 10, 2)
print(f"slice(1,10,2) -> [1,10,2) step 2: {list(range(100))[s][:5]}...")

# property() - membuat property (biasa digunakan sebagai decorator)
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius tidak boleh negatif")
        self._radius = value
c = Circle(5)
print(f"property radius: {c.radius}")
c.radius = 10
print(f"setter mengubah radius menjadi {c.radius}")

# classmethod dan staticmethod
class MyClass:
    @classmethod
    def class_method(cls):
        return f"classmethod dipanggil dari {cls.__name__}"
    @staticmethod
    def static_method():
        return "static method"
print(f"{MyClass.class_method()}")
print(f"{MyClass.static_method()}")

# super() - memanggil method parent class
class Parent:
    def greet(self):
        return "Hello from Parent"
class Child(Parent):
    def greet(self):
        return super().greet() + " and Child"
ch = Child()
print(f"super() dalam Child: {ch.greet()}")

# object() - instance kosong
obj = object()
print(f"object() dibuat: {obj}")

# memoryview() - akses buffer tanpa copy
data = bytearray(b'hello')
mv = memoryview(data)
print(f"memoryview[0] = {mv[0]}")
mv[0] = 72  # 'H'
print(f"set memoryview -> data menjadi {data}")

# iter() - membuat iterator
lst = [1,2,3]
it = iter(lst)
print(f"next(iter([1,2,3])) = {next(it)}")

# next() dengan default
it2 = iter([])
print(f"next(iterator kosong, default='habis') = {next(it2, 'habis')}")

# aiter(), anext() - async version (Python 3.10+)
# tidak dicontohkan di sini karena memerlukan async function

print("\n" + "=" * 60)
print("7. FUNGSI KHUSUS (ADVANCED)")
print("=" * 60)

# __import__() - import dinamis (tidak direkomendasikan, gunakan importlib)
math = __import__('math')
print(f"__import__('math').sqrt(16) = {math.sqrt(16)}")

# type() dengan tiga argumen - membuat class dinamis
MyDynamic = type('MyDynamic', (), {'x': 100, 'y': lambda self: self.x})
dyn = MyDynamic()
print(f"type('MyDynamic', ...) -> dyn.x = {dyn.x}, dyn.y() = {dyn.y()}")

print("\n" + "=" * 60)
print("CATATAN PENTING")
print("=" * 60)
print("- eval() dan exec() dapat membahayakan jika diberi input user.")
print("- assert dinonaktifkan dengan flag -O (tidak termasuk built-in function).")
print("- breakpoint() memanggil debugger (Python 3.7+).")
print("- zip(strict=True) memastikan panjang iterable sama (Python 3.10+).")
print("- Lihat dokumentasi resmi untuk detail lengkap setiap fungsi.")