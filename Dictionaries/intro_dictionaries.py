"""
Materi: Dictionaries (Kamus) - Dokumentasi Resmi Python
Sumber: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Dictionary adalah koleksi pasangan key: value.
Key harus immutable (string, number, tuple yang berisi immutable), unik.
Dictionary tidak berurutan sampai Python 3.7+ mempertahankan insertion order.
"""

print("=" * 60)
print("1. MEMBUAT DICTIONARY")
print("=" * 60)

# Dictionary kosong
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# Dictionary dengan pasangan key:value
tel = {'jack': 4098, 'sape': 4139}
print(f"tel = {tel}")

# Menambah pasangan baru
tel['guido'] = 4127
print(f"Setelah tel['guido'] = 4127 -> {tel}")

# Mengubah nilai key yang sudah ada
tel['jack'] = 4100
print(f"Setelah tel['jack'] = 4100 -> {tel}")

print("\n" + "=" * 60)
print("2. MENGAKSES NILAI")
print("=" * 60)

# Akses dengan key
print(f"tel['jack'] = {tel['jack']}")

# Akses key yang tidak ada (KeyError)
try:
    print(tel['irv'])
except KeyError as e:
    print(f"Error: {e}")

# Menggunakan get() untuk menghindari KeyError
print(f"tel.get('irv') = {tel.get('irv')}")
print(f"tel.get('irv', 'Tidak ditemukan') = {tel.get('irv', 'Tidak ditemukan')}")

print("\n" + "=" * 60)
print("3. MENGHAPUS PASANGAN")
print("=" * 60)

# Menghapus dengan del
del tel['sape']
print(f"Setelah del tel['sape'] -> {tel}")

# Menambah lagi untuk contoh
tel['irv'] = 4127
print(f"Setelah tel['irv'] = 4127 -> {tel}")

print("\n" + "=" * 60)
print("4. OPERASI DASAR")
print("=" * 60)

# list() mengembalikan daftar key (urutan insertion sejak Python 3.7)
print(f"list(tel) = {list(tel)}")

# sorted() mengembalikan key terurut
print(f"sorted(tel) = {sorted(tel)}")

# in dan not in untuk pengecekan key
print(f"'guido' in tel = {'guido' in tel}")
print(f"'jack' not in tel = {'jack' not in tel}")

print("\n" + "=" * 60)
print("5. MEMBUAT DICTIONARY DENGAN dict() CONSTRUCTOR")
print("=" * 60)

# Dari list of tuples
d1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(f"dict([('sape',4139), ('guido',4127), ('jack',4098)]) = {d1}")

# Dari keyword arguments (hanya untuk key string)
d2 = dict(sape=4139, guido=4127, jack=4098)
print(f"dict(sape=4139, guido=4127, jack=4098) = {d2}")

print("\n" + "=" * 60)
print("6. DICTIONARY COMPREHENSION")
print("=" * 60)

# Membuat dictionary dari ekspresi
squares = {x: x**2 for x in (2, 4, 6)}
print(f"{{x: x**2 for x in (2,4,6)}} = {squares}")

# Contoh lain: genap kuadrat
even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print(f"Genap kuadrat: {even_squares}")

print("\n" + "=" * 60)
print("7. KETENTUAN KEY (HARUS IMMUTABLE)")
print("=" * 60)

# String dan number bisa jadi key
valid = {1: 'one', 'two': 2, (1,2): 'tuple key'}
print(f"Valid keys: {valid}")

# List tidak bisa jadi key (mutable)
try:
    invalid = {[1,2]: 'list key'}
except TypeError as e:
    print(f"List sebagai key error: {e}")

# Tuple yang berisi mutable juga tidak bisa
try:
    invalid = {(1, [2,3]): 'tuple with list'}
except TypeError as e:
    print(f"Tuple dengan list error: {e}")

print("\n" + "=" * 60)
print("8. METHOD DICTIONARY LAINNYA")
print("=" * 60)

d = {'a': 1, 'b': 2, 'c': 3}
print(f"d = {d}")

# keys() - view of keys
print(f"d.keys() = {d.keys()}")

# values() - view of values
print(f"d.values() = {d.values()}")

# items() - view of (key, value) pairs
print(f"d.items() = {d.items()}")

# update() - menggabungkan dictionary lain
d.update({'d': 4, 'e': 5})
print(f"d.update({{'d':4,'e':5}}) -> {d}")

# pop() - hapus key dan return value
val = d.pop('b')
print(f"d.pop('b') -> {val}, d sekarang {d}")

# popitem() - hapus dan return pasangan terakhir (insertion order)
key_val = d.popitem()
print(f"d.popitem() -> {key_val}, d sekarang {d}")

# setdefault() - dapatkan nilai, jika key tidak ada maka set default
print(f"d.setdefault('x', 100) = {d.setdefault('x', 100)}")
print(f"d setelah setdefault = {d}")

print("\n" + "=" * 60)
print("RINGKASAN DICTIONARY")
print("=" * 60)
print("- Dictionary: koleksi key:value, key unik, key harus immutable")
print("- Buat: {key:value, ...} atau dict() constructor")
print("- Akses: d[key] atau d.get(key, default)")
print("- Hapus: del d[key] atau d.pop(key)")
print("- Cek key: key in d")
print("- Iterasi key: list(d), sorted(d)")
print("- Dictionary comprehension: {key_expr: value_expr for item in iterable}")
print("- Sejak Python 3.7, dictionary mempertahankan urutan insertion")
print("- Method: keys(), values(), items(), update(), pop(), popitem(), setdefault()")