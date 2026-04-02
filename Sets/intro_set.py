"""
Materi: Sets (Himpunan) - Dokumentasi Resmi Python
Sumber: https://docs.python.org/3/tutorial/datastructures.html#sets

Set adalah koleksi yang tidak berurutan (unordered) dan tidak memiliki elemen duplikat.
Kegunaan utama: membership testing dan menghilangkan duplikat.
Mendukung operasi matematika: union, intersection, difference, symmetric difference.
"""

print("=" * 60)
print("1. MEMBUAT SET")
print("=" * 60)

# Menggunakan kurung kurawal
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f"basket = {basket}")
print("Duplikat otomatis dihilangkan, urutan tidak tetap.\n")

# Menggunakan set() constructor
a = set('abracadabra')
print(f"set('abracadabra') = {a}")

b = set('alacazam')
print(f"set('alacazam') = {b}")

# Set dari list
angka = set([1, 2, 2, 3, 4])
print(f"set([1,2,2,3,4]) = {angka}")

# Empty set (harus pakai set(), bukan {})
empty_set = set()
empty_dict = {}
print(f"empty_set = {empty_set}, type = {type(empty_set)}")
print(f"empty_dict = {empty_dict}, type = {type(empty_dict)} (ini dictionary)")

print("\n" + "=" * 60)
print("2. MEMBERSHIP TEST (pengecekan keanggotaan)")
print("=" * 60)

basket = {'apple', 'orange', 'pear', 'banana'}
print(f"basket = {basket}")
print(f"'orange' in basket -> {'orange' in basket}")
print(f"'crabgrass' in basket -> {'crabgrass' in basket}")
print(f"'apple' not in basket -> {'apple' not in basket}")

print("\n" + "=" * 60)
print("3. OPERASI HIMPUNAN (SET OPERATIONS)")
print("=" * 60)

a = set('abracadabra')
b = set('alacazam')
print(f"a = {a}")
print(f"b = {b}\n")

# Difference (a - b): elemen di a tapi tidak di b
print(f"a - b = {a - b}")

# Union (a | b): elemen di a atau b atau keduanya
print(f"a | b = {a | b}")

# Intersection (a & b): elemen di kedua himpunan
print(f"a & b = {a & b}")

# Symmetric difference (a ^ b): elemen di salah satu tapi tidak keduanya
print(f"a ^ b = {a ^ b}")

print("\n" + "=" * 60)
print("4. METHOD SET LAINNYA")
print("=" * 60)

s = {1, 2, 3}
print(f"s = {s}")

# Menambah elemen
s.add(4)
print(f"s.add(4) -> {s}")

# Menghapus elemen (raise error jika tidak ada)
s.remove(2)
print(f"s.remove(2) -> {s}")

# Menghapus elemen (tidak error jika tidak ada)
s.discard(10)
print(f"s.discard(10) -> {s}")

# Menghapus dan mengembalikan elemen arbitrary
popped = s.pop()
print(f"s.pop() -> {popped}, s menjadi {s}")

# Menghapus semua elemen
s.clear()
print(f"s.clear() -> {s}")

# Update (menambah multiple elemen)
s = {1, 2}
s.update([3, 4, 5])
print(f"s.update([3,4,5]) -> {s}")

print("\n" + "=" * 60)
print("5. SET COMPREHENSION")
print("=" * 60)

# Set comprehension mirip list comprehension tapi dengan kurung kurawal
a = {x for x in 'abracadabra' if x not in 'abc'}
print(f"{{x for x in 'abracadabra' if x not in 'abc'}} = {a}")

# Contoh lain: kuadrat bilangan genap
genap_kuadrat = {x**2 for x in range(10) if x % 2 == 0}
print(f"Kuadrat genap 0-9: {genap_kuadrat}")

print("\n" + "=" * 60)
print("6. FROZENSET (SET IMMUTABLE)")
print("=" * 60)

# Frozenset adalah versi immutable dari set
fs = frozenset([1, 2, 3])
print(f"frozenset([1,2,3]) = {fs}")
print(f"Tipe: {type(fs)}")

# Frozenset bisa menjadi key dictionary (karena hashable)
d = {fs: "value"}
print(f"Dictionary dengan key frozenset: {d}")

# Operasi himpunan juga bisa dilakukan pada frozenset
fs2 = frozenset([3, 4, 5])
print(f"fs | fs2 = {fs | fs2}")

print("\n" + "=" * 60)
print("7. PERBANDINGAN SET DENGAN LIST/TUPLE")
print("=" * 60)

# Set tidak mempertahankan urutan
list_data = [3, 1, 4, 1, 5, 9]
set_data = set(list_data)
print(f"List: {list_data}")
print(f"Set: {set_data} (urutan berubah, duplikat hilang)")

# Kecepatan membership test (set lebih cepat O(1) vs list O(n))
import time
besar = range(100000)
set_besar = set(besar)
list_besar = list(besar)

start = time.perf_counter()
_ = 99999 in set_besar
time_set = time.perf_counter() - start

start = time.perf_counter()
_ = 99999 in list_besar
time_list = time.perf_counter() - start

print(f"\nMembership test 99999 dalam 100k elemen:")
print(f"  Set: {time_set:.6f} detik (O(1))")
print(f"  List: {time_list:.6f} detik (O(n))")

print("\n" + "=" * 60)
print("RINGKASAN SET")
print("=" * 60)
print("- Set adalah koleksi tidak berurutan, tanpa duplikat")
print("- Buat set dengan {elemen1, elemen2} atau set(iterable)")
print("- Empty set: set() ({} untuk dictionary)")
print("- Operasi: | (union), & (intersection), - (difference), ^ (symmetric diff)")
print("- Method: add, remove, discard, pop, clear, update, dll.")
print("- Set comprehension: {expr for item in iterable if condition}")
print("- Frozenset: versi immutable, bisa jadi key dictionary")
print("- Kecepatan membership test sangat cepat (hash table)")