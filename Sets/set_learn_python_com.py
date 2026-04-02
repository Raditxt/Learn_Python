"""
Materi tambahan: Sets dari learnpython.com
Konsep yang sebelumnya tidak tercakup di dokumentasi resmi Python:
1. Karakteristik set: mutable, unordered, unique immutable elements
2. Superset dan subset (issuperset, issubset)
3. Metode add, remove, update, copy, clear (beberapa sudah ada, tapi dengan contoh lebih detail)
4. Iterasi over set (dengan peringatan order tidak terjamin)
5. Use case: menghilangkan duplikat dari list
6. Use case: filtering data dengan set operations (contoh client IDs)
"""

print("=" * 60)
print("1. KARAKTERISTIK PYTHON SETS")
print("=" * 60)

# Mutable: bisa diubah
s = {1, 2, 3}
print(f"Set awal: {s}")
s.add(4)
print(f"Setelah add(4): {s} (mutable)")

# Unordered: tidak ada urutan tetap
unordered = {3, 1, 4, 1, 5, 9}
print(f"Set dengan elemen {3,1,4,1,5,9} -> {unordered} (urutan tidak tetap)")

# Unique elements: tidak ada duplikat
duplicate = {1, 1, 2, 2, 3}
print(f"Set dengan duplikat {1,1,2,2,3} -> {duplicate} (duplikat hilang)")

# Elemen harus immutable (tidak bisa pakai list)
try:
    invalid = {[1, 2], 3}
except TypeError as e:
    print(f"Error: set tidak boleh berisi list: {e}")

# Tapi bisa berisi tuple (immutable)
valid = {(1, 2), 3}
print(f"Set dengan tuple: {valid}")

print("\n" + "=" * 60)
print("2. SUPERSET DAN SUBSET")
print("=" * 60)

A = {1, 2, 3, 4, 5}
B = {1, 2, 4}

print(f"A = {A}")
print(f"B = {B}")

# issuperset() - apakah A mengandung semua elemen B?
print(f"A.issuperset(B) = {A.issuperset(B)}")

# issubset() - apakah B adalah bagian dari A?
print(f"B.issubset(A) = {B.issubset(A)}")

# Set adalah superset/subset dari dirinya sendiri
print(f"A.issuperset(A) = {A.issuperset(A)}")

# Empty set adalah subset dari semua set
empty = set()
print(f"empty.issubset(A) = {empty.issubset(A)}")

print("\n" + "=" * 60)
print("3. METODE SET UNTUK MANIPULASI")
print("=" * 60)

S = set()
print(f"S = {S}")

# add() - menambah elemen
S.add(2)
print(f"S.add(2) -> {S}")
S.add(2)  # tidak berpengaruh
print(f"S.add(2) lagi -> {S} (tidak berubah)")

# remove() - menghapus (KeyError jika tidak ada)
S.remove(2)
print(f"S.remove(2) -> {S}")
try:
    S.remove(10)
except KeyError as e:
    print(f"remove(10) error: {e}")

# update() - menambah semua elemen dari iterable lain
A = {1, 2, 3}
B = {3, 4, 5}
S.update(A)
print(f"S.update(A) -> {S}")
S.update(B)
print(f"S.update(B) -> {S}")

# copy() - membuat salinan independen
S1 = {1, 2, 3}
S2 = S1.copy()
S1.clear()
print(f"S1 = {S1}, S2 = {S2} (copy independen)")

print("\n" + "=" * 60)
print("4. ITERASI OVER SET (ORDER TIDAK TERJAMIN)")
print("=" * 60)

S = {1, 2, 3, 4, 5}
print(f"Iterasi set {S}:")
for number in S:
    print(f"  {number}")
print("Catatan: Urutan iterasi tidak tetap, bisa berbeda setiap kali dijalankan.")

print("\n" + "=" * 60)
print("5. USE CASE: MENGHILANGKAN DUPLIKAT DARI LIST")
print("=" * 60)

values = [1, 2, 2, 1, 3, 4, 1, 2, 3, 4, 1]
print(f"Original list: {values}")
unique_values = list(set(values))
print(f"Setelah set -> list: {unique_values} (urutan tidak dijamin)")

# Mempertahankan urutan dengan dict.fromkeys() (Python 3.7+)
ordered_unique = list(dict.fromkeys(values))
print(f"Mempertahankan urutan dengan dict: {ordered_unique}")

print("\n" + "=" * 60)
print("6. USE CASE: FILTERING DATA DENGAN SET OPERATIONS")
print("=" * 60)

all_clients = {104, 203, 255, 289, 448}
clients_bought_X = {104, 448}
clients_bought_Y = {104, 255, 289}

print(f"Semua klien: {all_clients}")
print(f"Klien beli X: {clients_bought_X}")
print(f"Klien beli Y: {clients_bought_Y}")

# Soal 1: Klien beli X tapi tidak Y
only_X = clients_bought_X - clients_bought_Y
print(f"1. Klien beli X tapi tidak Y: {only_X}")

# Soal 2: Klien beli kedua produk
both = clients_bought_X & clients_bought_Y
print(f"2. Klien beli kedua produk: {both}")

# Soal 3: Klien tidak beli apapun
buyers = clients_bought_X | clients_bought_Y
no_purchase = all_clients - buyers
print(f"3. Klien tidak beli apapun: {no_purchase}")

print("\n" + "=" * 60)
print("7. PERBANDINGAN KECEPATAN: SET vs LIST untuk MEMBERSHIP")
print("=" * 60)

import time

# Membuat data besar
data_range = range(10000)
list_data = list(data_range)
set_data = set(data_range)

search_item = 9999

# Test list
start = time.perf_counter()
found = search_item in list_data
list_time = time.perf_counter() - start

# Test set
start = time.perf_counter()
found = search_item in set_data
set_time = time.perf_counter() - start

print(f"List membership (10k elemen): {list_time:.6f} detik")
print(f"Set membership (10k elemen): {set_time:.6f} detik")
print(f"Set lebih cepat {list_time/set_time:.0f}x untuk pengecekan keanggotaan.")

print("\n" + "=" * 60)
print("RINGKASAN FITUR DARI LEARNPYTHON.COM")
print("=" * 60)
print("- Set: mutable, unordered, unique, elemen harus immutable")
print("- Superset/subset: issuperset(), issubset()")
print("- Metode: add, remove, update, copy, clear")
print("- Iterasi dengan for (order tidak terjamin)")
print("- Use case: menghilangkan duplikat list -> set -> list")
print("- Use case: filtering data dengan operasi himpunan")
print("- Kecepatan membership test sangat unggul dibanding list")