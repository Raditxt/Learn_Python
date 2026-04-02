"""
Materi: Python Tuple (dari artikel The New Stack)
Fokus: Konsep tuple yang belum tercakup di materi sebelumnya:
1. Berbagai jenis tuple (empty, integer, mixed, nested)
2. Indexing pada nested tuple
3. Slicing tuple
4. Concatenation (+) dan repetition (*) pada tuple
5. Method count() dan index() termasuk mencari indeks kedua
6. Perbedaan praktis tuple vs list (immutable vs mutable)
"""

print("=" * 60)
print("1. MEMBUAT BERBAGAI JENIS TUPLE")
print("=" * 60)

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")
print(f"Tipe: {type(empty_tuple)}")
print(f"Panjang: {len(empty_tuple)}")

# Integer tuple
int_tuple = (1, 2, 3)
print(f"\nInteger tuple: {int_tuple}")

# Mixed data types tuple
mixed_tuple = (0, "Hello", 1.2, "World!")
print(f"Mixed tuple: {mixed_tuple}")

# Nested tuple (tuple berisi tuple lain dan list)
nested_tuple = ("aardvark", [0, 1, 2], (2, 1, 0))
print(f"Nested tuple: {nested_tuple}")

# Tuple dengan satu elemen (perhatikan koma)
single_element = (42,)  # koma wajib
print(f"Tuple satu elemen: {single_element}")
print(f"Tanpa koma jadi int: {(42)}")

print("\n" + "=" * 60)
print("2. MENGAKSES ELEMEN TUPLE (INDEXING)")
print("=" * 60)

tns_tuple = ('N', 'e', 'w', 'S', 't', 'a', 'c', 'k')
print(f"Tuple: {tns_tuple}")
print(f"tns_tuple[0] = {tns_tuple[0]}")
print(f"tns_tuple[-1] = {tns_tuple[-1]}")
print(f"tns_tuple[3] = {tns_tuple[3]}")

# Indexing pada nested tuple
print("\n--- Indexing nested tuple ---")
n_tuple = ("kubernetes", "cloud native", [8, 6, 7, 5, 3, 0, 9])
print(f"Nested tuple: {n_tuple}")
print(f"n_tuple[0] = {n_tuple[0]}")
print(f"n_tuple[1] = {n_tuple[1]}")
print(f"n_tuple[2] = {n_tuple[2]}")
# Akses elemen dalam list di dalam tuple
print(f"n_tuple[2][3] = {n_tuple[2][3]}")  # elemen ke-4 dari list
# Akses karakter dalam string di dalam tuple
print(f"n_tuple[0][3] = {n_tuple[0][3]}")  # karakter ke-4 dari 'kubernetes' -> 'r'? (0:k,1:u,2:b,3:e) -> 'e'

# Tuple di dalam tuple
deep_nested = (1, (2, 3), (4, (5, 6)))
print(f"\nTuple bersarang dalam: {deep_nested}")
print(f"deep_nested[1][0] = {deep_nested[1][0]}")
print(f"deep_nested[2][1][0] = {deep_nested[2][1][0]}")

print("\n" + "=" * 60)
print("3. SLICING TUPLE")
print("=" * 60)

tns_tuple = ('N', 'e', 'w', 'S', 't', 'a', 'c', 'k')
print(f"Tuple: {tns_tuple}")
print(f"tns_tuple[0:3] = {tns_tuple[0:3]}")
print(f"tns_tuple[3:8] = {tns_tuple[3:8]}")
print(f"tns_tuple[:4] = {tns_tuple[:4]}")
print(f"tns_tuple[4:] = {tns_tuple[4:]}")
print(f"tns_tuple[::2] = {tns_tuple[::2]}")  # loncatan 2

print("\n" + "=" * 60)
print("4. KONKATENASI (+) DAN REPETISI (*) TUPLE")
print("=" * 60)

# Concatenation
tuple1 = ('T', 'h', 'e')
tuple2 = ('N', 'e', 'w')
tuple3 = ('S', 't', 'a', 'c', 'k')
concatenated = tuple1 + tuple2 + tuple3
print(f"('T','h','e') + ('N','e','w') + ('S','t','a','c','k') =")
print(f"  {concatenated}")

# Repetition
repeated = ("The New Stack",) * 3
print(f"('The New Stack',) * 3 = {repeated}")

# Contoh lain
numbers = (1, 2, 3)
print(f"(1,2,3) * 2 = {numbers * 2}")

print("\n" + "=" * 60)
print("5. METHOD TUPLE: count() DAN index()")
print("=" * 60)

tns_tuple = ('N', 'e', 'w', 'S', 't', 'a', 'c', 'k', 'R', 'o', 'k', 's')
print(f"Tuple: {tns_tuple}")

# count() - menghitung kemunculan nilai
count_k = tns_tuple.count('k')
print(f"Jumlah 'k' dalam tuple: {count_k}")  # 2

# index() - mencari indeks pertama kemunculan
first_k = tns_tuple.index('k')
print(f"Indeks pertama 'k': {first_k}")

# Mencari indeks kedua
second_k = tns_tuple.index('k', first_k + 1)
print(f"Indeks kedua 'k': {second_k}")

# Mencari indeks ketiga (jika ada)
if tns_tuple.count('k') >= 3:
    third_k = tns_tuple.index('k', second_k + 1)
    print(f"Indeks ketiga 'k': {third_k}")

# index() dengan batas
print(f"index('c', 0, 5): {tns_tuple.index('c', 0, 5)}")  # cari antara indeks 0-5

print("\n" + "=" * 60)
print("6. PERBEDAAN PRAKTIS TUPLE vs LIST")
print("=" * 60)

# List mutable
list_example = [1, 2, 3]
print(f"List awal: {list_example}")
list_example[0] = 99
print(f"List setelah diubah: {list_example}")

# Tuple immutable
tuple_example = (1, 2, 3)
print(f"Tuple awal: {tuple_example}")
try:
    tuple_example[0] = 99
except TypeError as e:
    print(f"Tuple tidak bisa diubah: {e}")

# Tuple sebagai key dictionary (list tidak bisa)
print("\n--- Tuple sebagai dictionary key ---")
location = { (40.7128, -74.0060): "New York" }
print(f"Dictionary dengan key tuple: {location}")
try:
    bad_dict = { [1,2,3]: "value" }
except TypeError as e:
    print(f"List tidak bisa jadi key dict: {e}")

# Kecepatan pembuatan tuple vs list
import timeit
print("\n--- Perbandingan kecepatan pembuatan ---")
list_time = timeit.timeit('[1,2,3,4,5]', number=1000000)
tuple_time = timeit.timeit('(1,2,3,4,5)', number=1000000)
print(f"List 1 juta kali: {list_time:.4f} detik")
print(f"Tuple 1 juta kali: {tuple_time:.4f} detik")
print("Tuple lebih cepat untuk dibuat dan diakses.")

print("\n" + "=" * 60)
print("7. KONVERSI ANTARA LIST DAN TUPLE")
print("=" * 60)

my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7, 8)

# List ke tuple
converted_tuple = tuple(my_list)
print(f"List {my_list} -> tuple {converted_tuple}")

# Tuple ke list
converted_list = list(my_tuple)
print(f"Tuple {my_tuple} -> list {converted_list}")

# Gunakan konversi untuk mengubah tuple
# (karena tuple immutable, kita konversi ke list, ubah, lalu kembali ke tuple)
temp_list = list(my_tuple)
temp_list.append(9)
modified_tuple = tuple(temp_list)
print(f"Tuple setelah modifikasi (via list): {modified_tuple}")

print("\n" + "=" * 60)
print("RINGKASAN TUPLE")
print("=" * 60)
print("- Tuple ditulis dengan kurung biasa ()")
print("- Tuple bersifat IMMUTABLE (tidak bisa diubah setelah dibuat)")
print("- Indexing dan slicing sama seperti list")
print("- Bisa berisi berbagai tipe data, termasuk tuple lain (nested)")
print("- Method: count() dan index()")
print("- Operasi + (concatenation) dan * (repetition)")
print("- Lebih hemat memori dan lebih cepat daripada list")
print("- Bisa digunakan sebagai key dictionary (karena hashable)")  