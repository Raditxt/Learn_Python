"""
Materi tambahan: Tuple dari Real Python (Deep Dive)
Konsep yang TIDAK ADA di dokumentasi resmi dan artikel The New Stack:
1. Membuat tuple dengan tuple() constructor (dari iterable, generator, dll)
2. Extended unpacking dengan * (mengumpulkan sisa elemen ke list)
3. Copy tuple (shallow vs deep copy) - termasuk alias dan deepcopy
4. Membalik tuple dengan reversed() dan slicing [::-1]
5. Mengurutkan tuple dengan sorted() dan parameter key
6. Traversing tuple dengan list comprehension dan generator expression
7. Membership test dengan in dan not in
8. Perbandingan tuple (lexicographical ordering)
9. Gotchas: tuple satu elemen butuh koma, hashability dengan mutable objects
10. Alternatif tuple: namedtuple, NamedTuple, dataclass (frozen)
"""

import sys
from copy import deepcopy
from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass

print("=" * 60)
print("1. MEMBUAT TUPLE DENGAN tuple() CONSTRUCTOR")
print("=" * 60)

# Dari list
from_list = tuple([1, 2, 3])
print(f"tuple([1,2,3]) = {from_list}")

# Dari string
from_string = tuple("Python")
print(f"tuple('Python') = {from_string}")

# Dari dictionary values
d = {"a": 1, "b": 2, "c": 3}
from_dict = tuple(d.values())
print(f"tuple(dict.values()) = {from_dict}")

# Dari generator expression
from_gen = tuple(x**2 for x in range(5))
print(f"tuple(x**2 for x in range(5)) = {from_gen}")

# Empty tuple
empty = tuple()
print(f"tuple() = {empty}")

print("\n" + "=" * 60)
print("2. EXTENDED UNPACKING DENGAN * OPERATOR")
print("=" * 60)

numbers = (1, 2, 3, 4, 5)

# Mengumpulkan sisa elemen ke list
first, *rest = numbers
print(f"first, *rest = {numbers} -> first={first}, rest={rest}")

first, *middle, last = numbers
print(f"first, *middle, last -> first={first}, middle={middle}, last={last}")

*head, last = numbers
print(f"*head, last -> head={head}, last={last}")

# Mengabaikan sisa dengan _
first, *_, last = numbers
print(f"first, *_, last -> first={first}, last={last}")

# Menggabungkan tuple dengan * saat membuat tuple baru
t1 = (1, 2)
t2 = (3, 4)
combined = (*t1, *t2)
print(f"(*t1, *t2) = {combined}")

print("\n" + "=" * 60)
print("3. COPY TUPLE (SHALLOW VS DEEP COPY)")
print("=" * 60)

# Tuple dengan list di dalamnya (mutable)
original = (1, 2, [3, 4])
print(f"Original: {original}")

# Shallow copy (sebenarnya alias karena tuple immutable)
shallow = original[:]
print(f"Shallow copy ([:]): {shallow}")
print(f"Apakah original dan shallow objek sama? {original is shallow}")  # True

# Deep copy
deep = deepcopy(original)
print(f"Deep copy: {deep}")
print(f"Apakah original dan deep objek sama? {original is deep}")  # False
print(f"Apakah list di dalamnya sama? {original[2] is deep[2]}")  # False

# Mengubah list di dalam deep copy
deep[2][0] = 99
print(f"Setelah deep[2][0]=99 -> deep={deep}")
print(f"Original tetap: {original}")

print("\n" + "=" * 60)
print("4. MEMBALIK TUPLE (REVERSED DAN SLICING)")
print("=" * 60)

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(f"Original: {days}")

# Menggunakan reversed() -> iterator
rev_iter = reversed(days)
reversed_tuple = tuple(rev_iter)
print(f"reversed() -> {reversed_tuple}")

# Menggunakan slicing step -1
sliced_rev = days[::-1]
print(f"days[::-1] -> {sliced_rev}")

print("\n" + "=" * 60)
print("5. MENGURUTKAN TUPLE DENGAN sorted()")
print("=" * 60)

# Sorting tuple angka
nums = (3, 1, 4, 1, 5, 9)
sorted_list = sorted(nums)  # menghasilkan list
print(f"sorted({nums}) = {sorted_list} (list)")

# Tuple dengan tuple di dalamnya (sort berdasarkan elemen tertentu)
fruits = (("apple", 0.40), ("banana", 0.25), ("orange", 0.35))
sorted_by_price = sorted(fruits, key=lambda x: x[1])
print(f"Sort by price: {sorted_by_price}")

# Descending
desc = sorted(nums, reverse=True)
print(f"Descending: {desc}")

# Catatan: sorted() pada tuple heterogen bisa error
try:
    mixed = ("a", 1, "b")
    sorted(mixed)
except TypeError as e:
    print(f"Error sorting heterogen tuple: {e}")

print("\n" + "=" * 60)
print("6. TRAVERSING TUPLE (COMPREHENSION & GENERATOR)")
print("=" * 60)

numbers = (1, 2, 3, 4, 5)

# List comprehension dari tuple
squares_list = [x**2 for x in numbers]
print(f"List comprehension: {squares_list}")

# Generator expression (hemat memori)
squares_gen = (x**2 for x in numbers)
print(f"Generator expression: {squares_gen}")
print(f"Hasil generator: {tuple(squares_gen)}")

# Menggunakan map
squares_map = tuple(map(lambda x: x**2, numbers))
print(f"map() -> {squares_map}")

print("\n" + "=" * 60)
print("7. MEMBERSHIP TEST (in DAN not in)")
print("=" * 60)

skills = ("Python", "Django", "Flask", "CSS")
print(f"skills = {skills}")

print(f"'Flask' in skills -> {'Flask' in skills}")
print(f"'Java' in skills -> {'Java' in skills}")
print(f"'Java' not in skills -> {'Java' not in skills}")

# Perhatikan: O(n) untuk tuple, O(1) untuk set (jika banyak pengecekan)
print("\nCatatan: Membership test pada tuple O(n), untuk banyak pengecekan gunakan set.")

print("\n" + "=" * 60)
print("8. PERBANDINGAN TUPLE (LEXICOGRAPHICAL)")
print("=" * 60)

print(f"(1,2) == (1,2) -> {(1,2) == (1,2)}")
print(f"(1,2) < (2,1) -> {(1,2) < (2,1)}")  # bandingkan 1 dan 2
print(f"(1,2,3) < (1,2,4) -> {(1,2,3) < (1,2,4)}")
print(f"(1,2) < (1,2,3) -> {(1,2) < (1,2,3)}")  # tuple lebih pendek dianggap lebih kecil

# Hati-hati dengan tipe berbeda
try:
    (1, "a") < (2, "b")  # OK karena 1 < 2
    print("(1,'a') < (2,'b') -> True")
except TypeError:
    print("Error")

try:
    (1, "a") < (1, 2)  # bandingkan string "a" dengan int 2 -> TypeError
except TypeError as e:
    print(f"Error perbandingan tipe berbeda: {e}")

print("\n" + "=" * 60)
print("9. GOTCHAS (JEBATAN UMUM TUPLE)")
print("=" * 60)

# Gotcha 1: Tuple satu elemen butuh koma
not_a_tuple = (42)
is_tuple = (42,)
print(f"(42) -> {type(not_a_tuple)}")
print(f"(42,) -> {type(is_tuple)}")

# Gotcha 2: Tuple dengan mutable objects tidak hashable -> tidak bisa jadi key dict
good_key = (1, 2, 3)  # semua immutable
bad_key = (1, [2, 3])  # mengandung list
d = {good_key: "value"}
print(f"Tuple immutable jadi key dict: {d}")
try:
    d2 = {bad_key: "value"}
except TypeError as e:
    print(f"Tuple dengan list tidak bisa jadi key: {e}")

# Gotcha 3: Mengubah mutable object di dalam tuple bisa dilakukan
t = (1, [2, 3])
t[1].append(4)
print(f"Tuple dengan list setelah append: {t}")  # tuple tetap, isi list berubah

print("\n" + "=" * 60)
print("10. ALTERNATIF TUPLE: namedtuple, NamedTuple, dataclass")
print("=" * 60)

# collections.namedtuple
print("--- namedtuple ---")
Person = namedtuple("Person", ["name", "age", "job"])
p1 = Person("John", 35, "Developer")
print(f"Person: {p1}")
print(f"p1.name = {p1.name}, p1[0] = {p1[0]}")  # akses atribut dan index
# p1.name = "Jane"  # Error: immutable

# typing.NamedTuple (dengan type hints)
print("\n--- typing.NamedTuple ---")
class Employee(NamedTuple):
    name: str
    age: int
    position: str = "Staff"
emp = Employee("Alice", 30)
print(f"Employee: {emp}")
print(f"emp.name = {emp.name}, emp.position = {emp.position}")

# dataclass (frozen=True untuk immutability)
print("\n--- dataclass (frozen=True) ---")
@dataclass(frozen=True)
class Point:
    x: int
    y: int
pt = Point(10, 20)
print(f"Point: {pt}")
print(f"pt.x = {pt.x}")
# pt.x = 30  # Error: FrozenInstanceError

print("\n" + "=" * 60)
print("RINGKASAN FITUR REAL PYTHON YANG DITAMBAHKAN")
print("=" * 60)
print("- tuple() constructor (dari iterable, generator, dict.values)")
print("- Extended unpacking dengan * (first, *rest, last)")
print("- Copy: shallow copy (alias) vs deepcopy (copy.deepcopy)")
print("- reversed() dan slicing [::-1] untuk membalik")
print("- sorted() dengan key dan reverse")
print("- Traversing dengan list comprehension, generator expression, map")
print("- Membership test: in, not in")
print("- Perbandingan tuple (lexicographical) dan potensi TypeError")
print("- Gotchas: koma untuk satu elemen, hashability dengan mutable objects")
print("- Alternatif: namedtuple, NamedTuple, dataclass(frozen=True)")