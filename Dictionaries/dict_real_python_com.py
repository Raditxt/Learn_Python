"""
Materi tambahan: Dictionaries dari Real Python
Konsep yang TIDAK ADA di dokumentasi resmi python dalam hal ini sudah saya implementasikan pada file intro_dict.py, jadi di sini saya fokus pada fitur-fitur lanjutan yang tidak tercakup di dokumentasi resmi:
1. dict.fromkeys() - membuat dictionary dari iterable keys
2. Dictionary views (keys(), values(), items()) bersifat dinamis
3. Union operator (|) dan augmented union (|=) untuk dictionary (Python 3.9+)
4. Built-in functions: all(), any(), min(), max(), sorted(), sum() dengan dictionary
5. .setdefault() method untuk default values
6. Iterasi dengan unpacking di loop header
7. collections: OrderedDict, Counter, defaultdict
8. Membuat custom dictionary class (inherit dari dict)
9. .__dict__ attribute pada objek
10. Membuat dictionary dari dua list dengan zip()
"""

from collections import OrderedDict, Counter, defaultdict
import sys

print("=" * 60)
print("1. MEMBUAT DICTIONARY DENGAN dict.fromkeys()")
print("=" * 60)

# fromkeys(iterable, value) - semua key punya value yang sama
keys = ["apple", "orange", "banana", "mango"]
inventory = dict.fromkeys(keys, 0)
print(f"dict.fromkeys({keys}, 0) = {inventory}")

# Tanpa default value (None)
none_dict = dict.fromkeys(["a", "b", "c"])
print(f"dict.fromkeys(['a','b','c']) = {none_dict}")

# Hati-hati dengan mutable default value (semua key akan berbagi referensi yang sama)
bad_dict = dict.fromkeys([1, 2, 3], [])
bad_dict[1].append(99)
print(f"dict.fromkeys(..., []) - semua key berbagi list yang sama: {bad_dict}")

print("\n" + "=" * 60)
print("2. DICTIONARY VIEWS (DINAMIS)")
print("=" * 60)

d = {"a": 1, "b": 2, "c": 3}
print(f"d = {d}")

keys_view = d.keys()
values_view = d.values()
items_view = d.items()
print(f"keys_view = {keys_view}, type = {type(keys_view)}")
print(f"values_view = {values_view}")
print(f"items_view = {items_view}")

# Views bersifat dinamis - refleksi perubahan dictionary
d["d"] = 4
print(f"\nSetelah menambah d['d'] = 4:")
print(f"keys_view menjadi: {keys_view}")
print(f"values_view menjadi: {values_view}")
print(f"items_view menjadi: {items_view}")

# Konversi ke list (tidak dinamis)
print(f"list(keys_view) = {list(keys_view)}")

print("\n" + "=" * 60)
print("3. UNION OPERATOR | DAN AUGMENTED UNION |=")
print("=" * 60)

# Union (menggabungkan dua dictionary, nilai dari kanan menimpa kiri jika ada duplikat)
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 4, "e": 5}
result = d1 | d2
print(f"d1 = {d1}")
print(f"d2 = {d2}")
print(f"d1 | d2 = {result}")

# Augmented union (update in place)
d1 |= d2
print(f"Setelah d1 |= d2, d1 menjadi: {d1}")

print("\n" + "=" * 60)
print("4. BUILT-IN FUNCTIONS DENGAN DICTIONARY")
print("=" * 60)

grades = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    "Fiona": 95.6,
    "George": 73.4,
    "Hannah": 81.2,
}
print(f"grades = {grades}")

# all() dan any() untuk values
print(f"all(grades.values()) = {all(grades.values())} (semua nilai truthy?)")
print(f"any(g > 100 for g in grades.values()) = {any(g > 100 for g in grades.values())}")

# min() dan max() dengan key
min_by_value = min(grades.items(), key=lambda item: item[1])
max_by_value = max(grades.items(), key=lambda item: item[1])
print(f"Nilai terendah: {min_by_value}")
print(f"Nilai tertinggi: {max_by_value}")

# sorted() dengan key
sorted_by_name = dict(sorted(grades.items()))
print(f"Sorted by key (nama): {sorted_by_name}")

sorted_by_grade = dict(sorted(grades.items(), key=lambda item: item[1]))
print(f"Sorted by value (nilai): {sorted_by_grade}")

# sum() untuk values
total = sum(grades.values())
avg = total / len(grades)
print(f"Total nilai: {total}, Rata-rata: {avg:.2f}")

print("\n" + "=" * 60)
print("5. .setdefault() METHOD")
print("=" * 60)

d = {"a": 1, "b": 2}
print(f"d = {d}")

# Jika key ada, return value
print(f"d.setdefault('a', 100) = {d.setdefault('a', 100)}")
print(f"d setelah setdefault: {d}")

# Jika key tidak ada, tambahkan dengan default
print(f"d.setdefault('c', 3) = {d.setdefault('c', 3)}")
print(f"d setelah setdefault('c'): {d}")

print(f"d.setdefault('d') = {d.setdefault('d')}")  # default None
print(f"d setelah setdefault('d'): {d}")

print("\n" + "=" * 60)
print("6. ITERASI DENGAN UNPACKING DI LOOP HEADER")
print("=" * 60)

# Unpacking items() langsung di loop header
for key, value in grades.items():
    print(f"  {key}: {value}")
# Output: Alice: 89.5, dst.

# Dengan enumerate
for i, (key, value) in enumerate(grades.items()):
    print(f"  {i+1}. {key}: {value}")

print("\n" + "=" * 60)
print("7. DICTIONARY-LIKE CLASSES DARI collections")
print("=" * 60)

# OrderedDict (meskipun dict sekarang sudah ordered, masih ada perbedaan)
print("--- OrderedDict ---")
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od.move_to_end("b")  # method khusus OrderedDict
print(f"OrderedDict: {od}")
print(f"move_to_end('b') -> {od}")

# Counter - untuk menghitung frekuensi
print("\n--- Counter ---")
text = "mississippi"
counter = Counter(text)
print(f"Counter('mississippi') = {counter}")
print(f"3 huruf paling umum: {counter.most_common(3)}")

# defaultdict - default value untuk key yang tidak ada
print("\n--- defaultdict ---")
employees = [
    ("Sales", "John"),
    ("Sales", "Martin"),
    ("Accounting", "Kate"),
    ("Marketing", "Elizabeth"),
    ("Marketing", "Linda"),
]
dept_dict = defaultdict(list)
for dept, name in employees:
    dept_dict[dept].append(name)
print(f"defaultdict(list): {dict(dept_dict)}")

# Dengan int untuk counting
word_count = defaultdict(int)
for word in ["apple", "banana", "apple", "orange", "banana", "apple"]:
    word_count[word] += 1
print(f"defaultdict(int): {dict(word_count)}")

print("\n" + "=" * 60)
print("8. MEMBUAT CUSTOM DICTIONARY CLASS")
print("=" * 60)

class SortableDict(dict):
    """Dictionary dengan kemampuan sorting in-place."""
    
    def sort_by_keys(self, reverse=False):
        sorted_items = sorted(self.items(), key=lambda item: item[0], reverse=reverse)
        self.clear()
        self.update(sorted_items)
    
    def sort_by_values(self, reverse=False):
        sorted_items = sorted(self.items(), key=lambda item: item[1], reverse=reverse)
        self.clear()
        self.update(sorted_items)

sd = SortableDict({"z": 1, "a": 2, "m": 3, "b": 4})
print(f"SortableDict awal: {sd}")
sd.sort_by_keys()
print(f"setelah sort_by_keys(): {sd}")
sd.sort_by_values(reverse=True)
print(f"setelah sort_by_values(reverse=True): {sd}")

print("\n" + "=" * 60)
print("9. .__dict__ ATTRIBUTE PADA OBJEK")
print("=" * 60)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(f"Person instance: {p}")
print(f"p.__dict__ = {p.__dict__}")  # mapping attribute name -> value

# globals() juga mengembalikan dictionary
print(f"globals() memiliki kunci: {list(globals().keys())[:5]}...")

print("\n" + "=" * 60)
print("10. MEMBUAT DICTIONARY DARI DUA LIST DENGAN zip()")
print("=" * 60)

cities = ["Jakarta", "Surabaya", "Bandung", "Medan"]
populations = [10_562_088, 2_874_314, 2_444_160, 2_435_252]

city_pop = dict(zip(cities, populations))
print(f"cities = {cities}")
print(f"populations = {populations}")
print(f"dict(zip(cities, populations)) = {city_pop}")

# Untuk dua list yang panjangnya tidak sama, zip berhenti di yang terpendek
more_cities = ["Jakarta", "Surabaya"]
city_pop2 = dict(zip(more_cities, populations))
print(f"zip dengan panjang tidak sama: {city_pop2}")

print("\n" + "=" * 60)
print("RINGKASAN FITUR REAL PYTHON YANG DITAMBAHKAN")
print("=" * 60)
print("- dict.fromkeys(iterable, value)")
print("- Dictionary views (dinamis, refleksi perubahan)")
print("- Union | dan augmented union |=")
print("- all(), any(), min(), max(), sorted(), sum() dengan dictionary")
print("- .setdefault(key, default)")
print("- Iterasi dengan unpacking items()")
print("- collections: OrderedDict, Counter, defaultdict")
print("- Custom dictionary class (inherit dict)")
print("- .__dict__ attribute")
print("- Membuat dictionary dengan zip() dari dua list")