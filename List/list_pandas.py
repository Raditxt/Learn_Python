"""
Materi tambahan: List dalam Python (dari artikel The New Stack)
Fokus: Penggunaan list untuk data tabular dengan pandas DataFrame

Konsep yang ditambahkan:
1. Membuat tabel dari dua list menggunakan pandas
2. Menampilkan list sebagai kolom terstruktur
3. Alternatif tanpa pandas (loop dan format string) - hanya sebagai perbandingan

PERSYARATAN: pandas harus terinstal. Jika tidak, program akan berhenti.
"""

import sys

print("=" * 60)
print("1. DASAR LIST DAN INDEXING (ULANGAN RINGKAS)")
print("=" * 60)

# List sederhana
color = ['blue', 'green', 'red', 'yellow']
fruit = ['blueberry', 'apple', 'cherry', 'banana']

print(f"List warna: {color}")
print(f"List buah: {fruit}")
print(f"Warna index 1: {color[1]}")
print(f"Buah index 1: {fruit[1]}")
print(f"Pasangan (index 1): {color[1]} {fruit[1]}")

print("\n" + "=" * 60)
print("2. MENAMPILKAN PASANGAN LIST TANPA PANDAS (LOOP)")
print("=" * 60)

print("Menggunakan loop for dengan range:")
print("Index | Warna   | Buah")
print("------|---------|----------")
for i in range(len(color)):
    print(f"  {i}    | {color[i]:<7} | {fruit[i]}")

print("\nMenggunakan zip() untuk iterasi paralel:")
print("Index | Warna   | Buah")
print("------|---------|----------")
for i, (c, f) in enumerate(zip(color, fruit)):
    print(f"  {i}    | {c:<7} | {f}")

print("\n" + "=" * 60)
print("3. MENGGUNAKAN PANDAS DATAFRAME (MEMBUAT TABEL)")
print("=" * 60)

print("Pandas adalah library eksternal untuk manipulasi data.")
print("Instalasi: pip install pandas  atau  apt-get install python3-pandas\n")

# Cek ketersediaan pandas - jika tidak ada, program BERHENTI
try:
    import pandas as pd
except ImportError:
    print("=" * 60)
    print("ERROR: PANDAS TIDAK TERINSTAL")
    print("=" * 60)
    print("Program ini membutuhkan pandas untuk melanjutkan.")
    print("Silakan instal pandas dengan salah satu perintah berikut:")
    print("  pip install pandas")
    print("  atau")
    print("  python -m pip install pandas")
    print("\nSetelah instalasi berhasil, jalankan ulang program ini.")
    sys.exit(1)

# Jika pandas berhasil diimport, lanjutkan
print("✓ Pandas berhasil diimport. Melanjutkan program...\n")

# Membuat DataFrame dari dua list
df = pd.DataFrame({
    'color': color,
    'fruit': fruit
})

print("DataFrame dari list color dan fruit:")
print(df)

print("\nMenampilkan dengan format yang lebih rapi (tanpa index numeric):")
print(df.to_string(index=False))

print("\n" + "=" * 60)
print("4. MEMBUAT TABEL DENGAN FORMAT MANUAL (SEBAGAI PERBANDINGAN)")
print("=" * 60)

def print_table(columns, data_dict):
    """
    Mencetak tabel sederhana dari dictionary list.
    columns: list nama kolom
    data_dict: dictionary dengan key = nama kolom, value = list data
    """
    # Menentukan lebar kolom
    widths = {}
    for col in columns:
        max_len = len(col)
        for item in data_dict[col]:
            max_len = max(max_len, len(str(item)))
        widths[col] = max_len + 2

    # Cetak header
    header = "".join(f"{col:>{widths[col]}}" for col in columns)
    print(header)
    print("-" * len(header))

    # Cetak baris
    for i in range(len(data_dict[columns[0]])):
        row = ""
        for col in columns:
            val = str(data_dict[col][i])
            row += f"{val:>{widths[col]}}"
        print(row)

# Contoh penggunaan
data = {
    'color': color,
    'fruit': fruit
}
print("Hasil print_table() manual:")
print_table(['color', 'fruit'], data)

print("\n" + "=" * 60)
print("5. MENGGABUNGKAN LIST MENJADI LIST OF DICTIONARIES")
print("=" * 60)

# Menggabungkan dua list menjadi list of dict
combined = []
for i in range(len(color)):
    combined.append({'color': color[i], 'fruit': fruit[i]})

print("List of dictionaries:")
for item in combined:
    print(f"  {item}")

# Akses elemen tertentu
print(f"\nElemen pertama: {combined[0]}")
print(f"Warna dari elemen kedua: {combined[1]['color']}")

print("\n" + "=" * 60)
print("6. MEMBUAT LIST DENGAN LIST COMPREHENSION")
print("=" * 60)

# List comprehension untuk membuat pasangan string
pairs = [f"{c} {f}" for c, f in zip(color, fruit)]
print("Pasangan warna-buah:")
for p in pairs:
    print(f"  {p}")

print("\n" + "=" * 60)
print("7. KESIMPULAN TAMBAHAN DARI ARTIKEL")
print("=" * 60)
print("- List dapat digunakan untuk menyimpan data terkait (misal warna dan buah)")
print("- Indexing list dimulai dari 0")
print("- Untuk menampilkan data tabular, gunakan pandas DataFrame")
print("- Alternatif tanpa pandas: loop dengan zip() atau format string")
print("- List dapat dikonversi menjadi DataFrame, list of dict, atau tabel manual")