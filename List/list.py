"""
Materi: List (tipe data komposit)
Dokumentasi: https://docs.python.org/3/tutorial/introduction.html#lists

List adalah tipe data yang dapat berisi berbagai jenis item (biasanya homogen).
List bersifat mutable (dapat diubah), berbeda dengan string yang immutable.
"""

print("=" * 60)
print("1. MEMBUAT LIST DAN INDEXING")
print("=" * 60)

squares = [1, 4, 9, 16, 25]
print(f"squares = {squares}")

# Indexing (mengakses elemen)
print(f"squares[0] = {squares[0]}")   # elemen pertama
print(f"squares[-1] = {squares[-1]}") # elemen terakhir
print(f"squares[-3:] = {squares[-3:]}") # slicing (list baru)

print("\n" + "=" * 60)
print("2. KONKATENASI LIST")
print("=" * 60)

new_list = squares + [36, 49, 64, 81, 100]
print(f"squares + [36,49,64,81,100] = {new_list}")

print("\n" + "=" * 60)
print("3. MUTABILITY (MENGUBAH ISI LIST)")
print("=" * 60)

cubes = [1, 8, 27, 65, 125]  # 65 seharusnya 64
print(f"cubes sebelum perbaikan: {cubes}")
print(f"4**3 = {4**3}")  # 64
cubes[3] = 64  # mengganti elemen ke-4 (index 3)
print(f"cubes setelah perbaikan: {cubes}")

# Menambah elemen dengan append()
cubes.append(216)   # 6^3
cubes.append(7**3)  # 343
print(f"cubes setelah append: {cubes}")

print("\n" + "=" * 60)
print("4. ASSIGNMENT TIDAK MENYALIN DATA (REFERENSI)")
print("=" * 60)

rgb = ["Red", "Green", "Blue"]
rgba = rgb          # rgba merujuk ke list yang sama dengan rgb
print(f"rgb = {rgb}")
print(f"rgba = {rgba}")
print(f"id(rgb) == id(rgba) = {id(rgb) == id(rgba)}")  # True

rgba.append("Alph")
print(f"Setelah rgba.append('Alph'):")
print(f"rgb = {rgb}")   # rgb ikut berubah
print(f"rgba = {rgba}")

print("\n" + "=" * 60)
print("5. MEMBUAT SHALLOW COPY DENGAN SLICE")
print("=" * 60)

correct_rgba = rgba[:]  # slice tanpa batas membuat salinan baru
print(f"correct_rgba = rgba[:] -> {correct_rgba}")
correct_rgba[-1] = "Alpha"
print(f"Setelah correct_rgba[-1] = 'Alpha':")
print(f"correct_rgba = {correct_rgba}")
print(f"rgba (asli) = {rgba}")  # rgba tidak berubah

print("\n" + "=" * 60)
print("6. ASSIGNMENT KE SLICE (MENGUBAH BAGIAN LIST)")
print("=" * 60)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"letters awal: {letters}")

# Mengganti sebagian elemen
letters[2:5] = ['C', 'D', 'E']
print(f"letters[2:5] = ['C','D','E'] -> {letters}")

# Menghapus sebagian elemen (assignment dengan list kosong)
letters[2:5] = []
print(f"letters[2:5] = [] -> {letters}")

# Mengosongkan seluruh list
letters[:] = []
print(f"letters[:] = [] -> {letters}")

print("\n" + "=" * 60)
print("7. FUNGSI len() PADA LIST")
print("=" * 60)

letters = ['a', 'b', 'c', 'd']
print(f"letters = {letters}")
print(f"len(letters) = {len(letters)}")

print("\n" + "=" * 60)
print("8. NESTED LIST (LIST BERSARANG)")
print("=" * 60)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(f"a = {a}")
print(f"n = {n}")
print(f"x = [a, n] = {x}")
print(f"x[0] = {x[0]}")       # list a
print(f"x[0][1] = {x[0][1]}") # elemen 'b'

# Mengubah elemen dalam nested list
x[0][0] = 'Z'
print(f"Setelah x[0][0] = 'Z':")
print(f"x = {x}")
print(f"a = {a}")  # a juga berubah karena referensi

print("\n" + "=" * 60)
print("RINGKASAN LIST")
print("=" * 60)
print("- List ditulis dengan kurung siku []")
print("- Indexing: list[index] (0-based, negatif dari belakang)")
print("- Slicing: list[start:end:step] menghasilkan list baru")
print("- List bersifat mutable (isi dapat diubah)")
print("- append() menambah elemen di akhir")
print("- Assignment list ke variabel lain tidak menyalin data (referensi)")
print("- Gunakan slice [:] untuk membuat shallow copy")
print("- Assignment ke slice dapat mengubah ukuran list")
print("- len() mengembalikan panjang list")
print("- List dapat berisi list lain (nested)")