"""
Materi tambahan: Tuple dari artikel The New Stack
1. Slicing tuple (range)
2. Concatenation (+) dan repetition (*) pada tuple
3. Method count() dan index() termasuk mencari indeks kedua
4. Penggunaan tuple sebagai key dictionary (karena immutable)
5. Akses karakter string di dalam nested tuple (indexing bertingkat)
"""

print("=" * 60)
print("1. JENIS-JENIS TUPLE (EMPTY, INTEGER, MIXED, NESTED)")
print("=" * 60)

empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

integer_tuple = (1, 2, 3)
print(f"Integer tuple: {integer_tuple}")

mixed_tuple = (0, "Hello", 1.2, "World!")
print(f"Mixed tuple: {mixed_tuple}")

nested_tuple = ("aardvark", [0, 1, 2], (2, 1, 0))
print(f"Nested tuple: {nested_tuple}")

print("\n" + "=" * 60)
print("2. MENGAKSES ELEMEN NESTED TUPLE (INDEXING BERTINGKAT)")
print("=" * 60)

n_tuple = ("kubernetes", "cloud native", [8, 6, 7, 5, 3, 0, 9])
print(f"n_tuple = {n_tuple}")
print(f"n_tuple[0] = {n_tuple[0]}")
print(f"n_tuple[0][3] = {n_tuple[0][3]}")  # karakter ke-4 dari 'kubernetes' -> 'e'
print(f"n_tuple[2][4] = {n_tuple[2][4]}")  # elemen ke-5 dari list -> 3

# Akses tuple di dalam tuple
deep = ((1, 2), (3, 4))
print(f"deep = {deep}")
print(f"deep[1][0] = {deep[1][0]}")

print("\n" + "=" * 60)
print("3. SLICING TUPLE (MEMOTONG TUPLE)")
print("=" * 60)

tns_tuple = ('N', 'e', 'w', 'S', 't', 'a', 'c', 'k')
print(f"tns_tuple = {tns_tuple}")
print(f"tns_tuple[0:3] = {tns_tuple[0:3]}")
print(f"tns_tuple[3:8] = {tns_tuple[3:8]}")
print(f"tns_tuple[:4] = {tns_tuple[:4]}")
print(f"tns_tuple[4:] = {tns_tuple[4:]}")
print(f"tns_tuple[::2] = {tns_tuple[::2]}")

print("\n" + "=" * 60)
print("4. KONKATENASI (+) DAN REPETISI (*) PADA TUPLE")
print("=" * 60)

# Concatenation
result = ('T', 'h', 'e') + ('N', 'e', 'w') + ('S', 't', 'a', 'c', 'k')
print("('T','h','e') + ('N','e','w') + ('S','t','a','c','k') =")
print(f"  {result}")

# Repetition
repeated = ("The New Stack",) * 3
print(f"('The New Stack',) * 3 = {repeated}")

# Contoh lain
angka = (1, 2, 3)
print(f"(1,2,3) * 2 = {angka * 2}")

print("\n" + "=" * 60)
print("5. METHOD count() DAN index() PADA TUPLE")
print("=" * 60)

tns_tuple = ('N', 'e', 'w', 'S', 't', 'a', 'c', 'k', 'R', 'o', 'k', 's')
print(f"Tuple: {tns_tuple}")

# count()
jumlah_k = tns_tuple.count('k')
print(f"Jumlah huruf 'k': {jumlah_k}")

# index() - mencari kemunculan pertama
posisi_pertama = tns_tuple.index('k')
print(f"Posisi pertama 'k': {posisi_pertama}")

# Mencari kemunculan kedua (dengan parameter start)
posisi_kedua = tns_tuple.index('k', posisi_pertama + 1)
print(f"Posisi kedua 'k': {posisi_kedua}")

# Mencari dalam rentang
posisi_c = tns_tuple.index('c', 0, 8)  # cari 'c' antara index 0-7
print(f"Posisi 'c' dalam indeks 0-7: {posisi_c}")

print("\n" + "=" * 60)
print("6. TUPLE SEBAGAI KEY DICTIONARY (KARENA IMMUTABLE)")
print("=" * 60)

# Tuple bisa menjadi key dictionary
location = { (40.7128, -74.0060): "New York" }
print(f"Dictionary dengan key tuple: {location}")
print(f"Akses: location[(40.7128, -74.0060)] = {location[(40.7128, -74.0060)]}")

# List TIDAK bisa menjadi key
try:
    bad_dict = { [1, 2, 3]: "value" }
except TypeError as e:
    print(f"List tidak bisa jadi key: {e}")

# Tuple dengan satu elemen juga bisa jadi key (perlu koma)
single_key = (42,)
valid_dict = {single_key: "the answer"}
print(f"Tuple satu elemen sebagai key: {valid_dict}")

print("\n" + "=" * 60)
print("7. PERBANDINGAN KECEPATAN TUPLE vs LIST (MEMBUAT DAN MENGAKSES)")
print("=" * 60)

import timeit

# Kecepatan pembuatan
list_time = timeit.timeit('[1,2,3,4,5]', number=1000000)
tuple_time = timeit.timeit('(1,2,3,4,5)', number=1000000)
print(f"Pembuatan list 1 juta kali: {list_time:.4f} detik")
print(f"Pembuatan tuple 1 juta kali: {tuple_time:.4f} detik")
print("Tuple lebih cepat dibuat.")

# Kecepatan akses (indexing)
list_access = timeit.timeit('x = [1,2,3,4,5][2]', number=1000000)
tuple_access = timeit.timeit('x = (1,2,3,4,5)[2]', number=1000000)
print(f"\nAkses list 1 juta kali: {list_access:.4f} detik")
print(f"Akses tuple 1 juta kali: {tuple_access:.4f} detik")
print("Tuple sedikit lebih cepat diakses.")

print("\n" + "=" * 60)
print("RINGKASAN (FITUR TAMBAHAN DARI ARTIKEL)")
print("=" * 60)
print("- Tuple mendukung slicing: tuple[start:end:step]")
print("- Concatenation: tuple1 + tuple2")
print("- Repetition: tuple * n")
print("- count() dan index() untuk pencarian")
print("- index() bisa diberi parameter start untuk mencari kemunculan berikutnya")
print("- Tuple immutable -> bisa menjadi key dictionary")
print("- Tuple lebih cepat daripada list untuk pembuatan dan akses")
print("- Nested tuple bisa diakses dengan indexing bertingkat")