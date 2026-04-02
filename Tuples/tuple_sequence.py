"""
Materi: Tuples and Sequences (dokumentasi resmi Python)
Sumber: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

Konsep yang dibahas:
1. Tuple packing (mengemas nilai ke tuple)
2. Tuple unpacking (membongkar tuple ke variabel)
3. Multiple assignment (sebenarnya kombinasi packing & unpacking)
4. Tuple dengan 0 elemen (empty tuple) dan 1 elemen (perlu koma)
5. Tuple bersarang (nested)
6. Immutability tuple vs mutable items di dalamnya
7. Perbedaan tuple dan list (heterogen vs homogen)
"""

print("=" * 60)
print("1. TUPLE PACKING (MENGEMAS NILAI KE TUPLE)")
print("=" * 60)

# Tuple packing: nilai dipisah koma, otomatis menjadi tuple
t = 12345, 54321, 'hello!'
print(f"Hasil tuple packing: t = {t}")
print(f"Tipe t: {type(t)}")
print(f"t[0] = {t[0]}")
print(f"t[1] = {t[1]}")
print(f"t[2] = {t[2]}")

print("\n" + "=" * 60)
print("2. TUPLE UNPACKING (MEMBONGKAR TUPLE KE VARIABEL)")
print("=" * 60)

# Sequence unpacking
x, y, z = t
print(f"Setelah unpacking: x = {x}, y = {y}, z = {z}")

# Unpacking untuk sequence lain (list, string, dll)
a, b, c = [10, 20, 30]
print(f"Unpacking list: a={a}, b={b}, c={c}")

p, q, r = "XYZ"
print(f"Unpacking string: p={p}, q={q}, r={r}")

# Jumlah variabel harus sama
try:
    w, v = t  # t punya 3 elemen, hanya 2 variabel
except ValueError as e:
    print(f"Error unpacking: {e}")

print("\n" + "=" * 60)
print("3. MULTIPLE ASSIGNMENT (PACKING + UNPACKING)")
print("=" * 60)

# Multiple assignment sebenarnya adalah packing di kanan, unpacking di kiri
m, n, o = 100, 200, 300
print(f"Multiple assignment: m={m}, n={n}, o={o}")

# Swap variabel menggunakan tuple packing/unpacking
a, b = 5, 10
print(f"Sebelum swap: a={a}, b={b}")
a, b = b, a
print(f"Setelah swap: a={a}, b={b}")

print("\n" + "=" * 60)
print("4. TUPLE DENGAN 0 ATAU 1 ELEMEN")
print("=" * 60)

# Empty tuple (0 elemen)
empty = ()
print(f"Empty tuple: {empty}")
print(f"Panjang: {len(empty)}")
print(f"Tipe: {type(empty)}")

# Tuple dengan 1 elemen - HARUS dengan koma di akhir
singleton1 = 'hello',
singleton2 = (42,)  # dengan kurung juga perlu koma
not_tuple = (42)    # ini integer, bukan tuple

print(f"Tuple satu elemen (tanpa kurung): {singleton1}")
print(f"Tuple satu elemen (dengan kurung): {singleton2}")
print(f"Tanpa koma: {not_tuple} (tipe: {type(not_tuple)})")

print("\n" + "=" * 60)
print("5. TUPLE BERSARANG (NESTED TUPLE)")
print("=" * 60)

# Tuple bisa berisi tuple lain
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)
print(f"Tuple bersarang u = {u}")
print(f"u[0] = {u[0]}")
print(f"u[0][1] = {u[0][1]}")  # akses elemen kedua dari tuple dalam
print(f"u[1][2] = {u[1][2]}")

print("\n" + "=" * 60)
print("6. IMMUTABILITY TUPLE (TIDAK BISA DIUBAH)")
print("=" * 60)

t = (1, 2, 3)
print(f"Tuple awal: {t}")
try:
    t[0] = 99
except TypeError as e:
    print(f"Error saat mencoba mengubah tuple: {e}")

# TAPI tuple bisa berisi objek mutable (seperti list)
print("\n--- Tuple berisi mutable objects ---")
v = ([1, 2, 3], [3, 2, 1])
print(f"Tuple v = {v}")
print(f"v[0] adalah list: {v[0]}")
v[0][0] = 999  # mengubah isi list di dalam tuple
print(f"Setelah mengubah list di dalam tuple: {v}")
print("Catatan: tuple tetap immutable, tapi elemen yang mutable bisa diubah isinya.")
print("Yang tidak bisa diubah adalah referensi objek di dalam tuple.")

print("\n" + "=" * 60)
print("7. PERBEDAAN TUPLE DAN LIST (MENURUT DOKUMENTASI)")
print("=" * 60)

print("Tuple:")
print("  - Immutable (tidak bisa diubah)")
print("  - Biasanya berisi elemen HETEROGEN (berbeda tipe)")
print("  - Diakses melalui unpacking atau indexing")
print("  - Dapat digunakan sebagai key dictionary (karena hashable)")
print("  - Lebih hemat memori")

print("\nList:")
print("  - Mutable (bisa diubah)")
print("  - Biasanya berisi elemen HOMOGEN (sama tipe)")
print("  - Diakses melalui iterasi atau indexing")
print("  - Tidak bisa jadi key dictionary")
print("  - Lebih fleksibel untuk operasi modifikasi")

# Contoh heterogen tuple (berbagai tipe)
person = ("John", 30, 175.5, True)
print(f"\nContoh tuple heterogen: {person}")
name, age, height, is_active = person
print(f"Unpacking: name={name}, age={age}, height={height}, active={is_active}")

print("\n" + "=" * 60)
print("RINGKASAN")
print("=" * 60)
print("- Tuple packing: nilai dipisah koma -> jadi tuple")
print("- Tuple unpacking: assign tuple ke variabel terpisah")
print("- Multiple assignment sebenarnya packing + unpacking")
print("- Empty tuple: ()")
print("- Tuple satu elemen: (value,) atau value, (koma wajib)")
print("- Tuple bersarang: diindeks seperti biasa")
print("- Tuple immutable, tapi bisa berisi list mutable")
print("- Gunakan tuple untuk data yang tidak berubah dan heterogen")