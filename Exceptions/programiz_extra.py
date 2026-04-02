"""
Materi tambahan dari Programiz yang tidak ada atau kurang jelas di:
- Dokumentasi resmi Python
- Real Python

Fokus:
1. Contoh exception di dalam else clause yang TIDAK ditangani oleh except sebelumnya.
2. Penggunaan assert di dalam try bersama else.
3. Contoh bare except (except:) untuk pemula (meskipun tidak direkomendasikan).
"""

print("=" * 60)
print("1. EXCEPTION DI DALAM ELSE CLAUSE TIDAK DITANGANI")
print("=" * 60)
print("Jika exception terjadi di dalam block else, exception tersebut tidak akan")
print("ditangani oleh except clause yang mendahuluinya.\n")

# Contoh: exception ZeroDivisionError terjadi di else
try:
    num = int(input("Masukkan angka (0 untuk demo error di else): "))
    # Tidak ada exception di try block
except ValueError:
    print("Error: Input harus angka.")
else:
    # Exception di sini TIDAK akan ditangani oleh except di atas
    reciprocal = 1 / num
    print(f"Kebalikan dari {num} adalah {reciprocal}")

print("\nPenjelasan: Jika Anda memasukkan 0, program akan crash dengan")
print("ZeroDivisionError karena except hanya menangani ValueError.\n")

print("=" * 60)
print("2. MENANGANI EXCEPTION DI ELSE DENGAN TRY BERSARANG")
print("=" * 60)
print("Solusi: gunakan try-except di dalam else atau tangani exception spesifik.\n")

try:
    num = int(input("Masukkan angka: "))
except ValueError:
    print("Error: Input harus angka.")
else:
    try:
        reciprocal = 1 / num
        print(f"Kebalikan: {reciprocal}")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol (di dalam else).")

print("\n" + "=" * 60)
print("3. INTEGRASI assert DENGAN try-except-else")
print("=" * 60)
print("assert digunakan untuk memeriksa kondisi. Jika kondisi False,")
print("akan memicu AssertionError. Cocok untuk debugging.\n")

try:
    num = int(input("Masukkan bilangan genap: "))
    assert num % 2 == 0, "Bukan bilangan genap"
except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError:
    print("Error: Input harus angka.")
else:
    reciprocal = 1 / num
    print(f"{num} adalah genap, kebalikannya: {reciprocal}")

print("\nCatatan: assert tidak aktif di mode optimasi (python -O).")
print("Jangan gunakan assert untuk validasi data produksi.\n")

print("=" * 60)
print("4. CONTOH BARE EXCEPT (except:) UNTUK PEMULA")
print("=" * 60)
print("Bare except menangkap SEMUA exception termasuk KeyboardInterrupt.")
print("Ini tidak direkomendasikan, tetapi sering muncul di tutorial pemula.\n")

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except:
    print("Error: Terjadi kesalahan (bare except).")

print("\nKelebihan: sederhana. Kekurangan: tidak tahu error apa yang terjadi.")
print("Lebih baik gunakan 'except Exception as e' atau tipe spesifik.\n")

print("=" * 60)
print("RINGKASAN FITUR YANG DITAMBAHKAN")
print("=" * 60)
print("- Exception di dalam else TIDAK ditangani oleh except sebelumnya.")
print("- Solusi dengan try bersarang di dalam else.")
print("- Integrasi assert dengan try-except-else.")
print("- Contoh bare except untuk pemula (beserta peringatan).")