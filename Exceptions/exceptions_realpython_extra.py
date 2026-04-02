"""
MATERI TAMBAHAN: KONSEP DARI REAL PYTHON
=========================================
File ini melengkapi 'errors_exceptions.py' dengan konsep yang ada di Real Python:
1. assert statement untuk debugging
2. Bahaya bare except (except: tanpa tipe)
3. Contoh fungsi linux_interaction() berbasis sys.platform
4. Perbedaan else vs kode di luar try
5. Docstring pada custom exception
6. Tips memilih exception type yang tepat
7. Peringatan assert tidak untuk produksi
"""

import sys

print("=" * 70)
print("1. ASSERT STATEMENT - Untuk Debugging Saja")
print("=" * 70)

# Contoh assert: memeriksa kondisi, jika False => AssertionError
print("Contoh assert dengan kondisi True (tidak melakukan apa-apa):")
angka = 3
assert angka < 5, "Angka harus kurang dari 5"
print("  assert (angka < 5) -> lolos, program lanjut")

print("\nContoh assert dengan kondisi False (memicu AssertionError):")
try:
    angka = 10
    assert angka < 5, f"Angka {angka} tidak boleh >= 5"
    print("  Baris ini tidak akan dicetak")
except AssertionError as e:
    print(f"  AssertionError tertangkap: {e}")

print("\n⚠️ PERINGATAN PENTING TENTANG ASSERT:")
print("  - Assert DINONAKTIFKAN saat Python dijalankan dengan flag -O atau -OO")
print("  - Jangan gunakan assert untuk validasi data di PRODUKSI")
print("  - Assert hanya untuk DEBUGGING dan testing internal")
print("  - Contoh: 'python -O script.py' akan menghilangkan semua assert")

print("\n" + "=" * 70)
print("2. BAHAYA 'BARE EXCEPT' (except: tanpa tipe)")
print("=" * 70)

print("❌ JANGAN PERNAH LAKUKAN INI:")
print("""
try:
    some_function()
except:  # BARE EXCEPT - menangkap SEMUA exception termasuk SystemExit, KeyboardInterrupt
    print("Terjadi error")  # Anda tidak tahu error apa yang terjadi
""")

print("✅ YANG BENAR:")
print("""
try:
    some_function()
except Exception as e:   # Menangkap exception turunan Exception, tapi tidak SystemExit dll
    print(f"Error: {e}")
""")

print("\nContoh bahaya bare except (menyembunyikan Ctrl+C):")
print("  # Coba tekan Ctrl+C saat kode berikut dijalankan (tanpa komentar)")
print("""
try:
    while True:
        pass
except:
    print("Bare except menangkap KeyboardInterrupt juga!")  # Ctrl+C tidak menghentikan program
""")
print("  (Contoh di atas sengaja dikomentari karena akan loop tak berujung)")

print("\n" + "=" * 70)
print("3. CONTOH FUNGSI BERBASIS PLATFORM: linux_interaction()")
print("=" * 70)

class PlatformException(Exception):
    """Exception khusus untuk platform yang tidak kompatibel."""
    pass

def linux_interaction():
    """
    Fungsi yang hanya bisa dijalankan di sistem operasi Linux.
    Jika tidak di Linux, melempar PlatformException.
    """
    import sys
    if "linux" not in sys.platform:
        raise PlatformException(
            f"Fungsi ini hanya bisa berjalan di Linux. "
            f"Platform saat ini: {sys.platform}"
        )
    print("✅ Menjalankan aksi khas Linux...")

# Demonstrasi linux_interaction dengan try/except
print(f"Platform sistem saat ini: {sys.platform}")
try:
    linux_interaction()
except PlatformException as e:
    print(f"⚠️ {e}")
else:
    print("Fungsi linux_interaction() berhasil dijalankan")

print("\n" + "=" * 70)
print("4. PERBEDAAN else vs KODE DI LUAR try")
print("=" * 70)

print("Kode dengan else (hanya jalan jika TIDAK ada exception):")
def demo_else(ada_error):
    try:
        if ada_error:
            raise ValueError("Error buatan")
        print("  Try block: sukses")
    except ValueError as e:
        print(f"  Except block: {e}")
    else:
        print("  Else block: hanya jalan jika try sukses (tidak ada error)")

print("  Memanggil demo_else(ada_error=False):")
demo_else(False)
print("  Memanggil demo_else(ada_error=True):")
demo_else(True)

print("\nKode dengan kode di luar try (jalan SETELAH except, apakah error atau tidak):")
def demo_luar_try(ada_error):
    try:
        if ada_error:
            raise ValueError("Error buatan")
        print("  Try block: sukses")
    except ValueError as e:
        print(f"  Except block: {e}")
    print("  >> Kode di luar try/except: tetap jalan meskipun ada error (setelah ditangani)")

print("  Memanggil demo_luar_try(ada_error=False):")
demo_luar_try(False)
print("  Memanggil demo_luar_try(ada_error=True):")
demo_luar_try(True)

print("\n🔍 KESIMPULAN:")
print("  - else: hanya dijalankan jika try sukses (tanpa exception)")
print("  - Kode di luar try: dijalankan setelah except selesai, apakah error atau tidak")

print("\n" + "=" * 70)
print("5. CUSTOM EXCEPTION DENGAN DOCSTRING YANG BAIK")
print("=" * 70)

class ValidationError(Exception):
    """Exception yang dilempar ketika data gagal memenuhi kriteria validasi.
    
    Attributes:
        field -- nama field yang gagal validasi
        value -- nilai yang tidak valid
        message -- penjelasan error
    """
    def __init__(self, field, value, message=None):
        self.field = field
        self.value = value
        self.message = message or f"Validasi gagal pada field '{field}' dengan nilai {value}"
        super().__init__(self.message)

# Contoh penggunaan
try:
    age = -5
    if age < 0:
        raise ValidationError("age", age, "Umur tidak boleh negatif")
except ValidationError as e:
    print(f"Tertangkap: {e}")
    print(f"  Field: {e.field}, Value: {e.value}")

print("\n📝 Tips membuat custom exception:")
print("  1. Turunkan dari Exception (bukan BaseException langsung)")
print("  2. Beri docstring yang menjelaskan kapan exception ini digunakan")
print("  3. Tambahkan atribut tambahan jika perlu (seperti field, value)")
print("  4. Nama exception sebaiknya diakhiri dengan 'Error'")

print("\n" + "=" * 70)
print("6. TIPS MEMILIH EXCEPTION TYPE YANG TEPAT")
print("=" * 70)

print("🔹 Hirarki exception penting (dari yang paling umum ke spesifik):")
print("  BaseException")
print("   ├── SystemExit (keluar dengan sys.exit())")
print("   ├── KeyboardInterrupt (Ctrl+C)")
print("   └── Exception")
print("        ├── ArithmeticError")
print("        │    └── ZeroDivisionError")
print("        ├── LookupError")
print("        │    ├── IndexError")
print("        │    └── KeyError")
print("        ├── OSError (error sistem file, koneksi, dll)")
print("        │    └── FileNotFoundError")
print("        ├── ValueError (tipe data benar tapi nilai tidak sesuai)")
print("        ├── TypeError (operasi pada tipe yang salah)")
print("        └── RuntimeError (error umum lainnya)")

print("\n🎯 Panduan memilih:")
print("  - File tidak ditemukan → FileNotFoundError")
print("  - Input angka tapi diisi huruf → ValueError")
print("  - List index di luar range → IndexError")
print("  - Dictionary key tidak ada → KeyError")
print("  - Pembagian dengan nol → ZeroDivisionError")
print("  - Operasi tidak didukung tipe data → TypeError")
print("  - Tidak ada yang cocok → RuntimeError atau buat custom exception")

print("\n" + "=" * 70)
print("7. DEMONSTRASI LENGKAP: Program Sederhana dengan Best Practices")
print("=" * 70)

def baca_file_dan_proses(nama_file):
    """
    Membaca file, mengonversi isi ke integer, dan menjumlahkannya.
    Menggunakan exception handling yang tepat.
    """
    total = 0
    try:
        with open(nama_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    angka = int(line.strip())
                    total += angka
                except ValueError:
                    # Tangkap error konversi, tapi lanjutkan ke baris berikutnya
                    print(f"  Peringatan: Baris {line_num} bukan angka, dilewati")
    except FileNotFoundError:
        print(f"  Error: File '{nama_file}' tidak ditemukan")
        return None
    except PermissionError:
        print(f"  Error: Tidak punya izin membaca '{nama_file}'")
        return None
    except OSError as e:
        print(f"  Error sistem: {e}")
        return None
    else:
        print(f"  Berhasil membaca file, total = {total}")
        return total
    finally:
        print("  Blok finally: pembersihan (jika perlu)")

# Buat file contoh
with open("contoh_angka.txt", "w") as f:
    f.write("10\n20\ntiga\n40\n")

print("Memanggil baca_file_dan_proses('contoh_angka.txt'):")
hasil = baca_file_dan_proses("contoh_angka.txt")
print(f"Hasil akhir: {hasil}")

# Bersihkan file
import os
os.remove("contoh_angka.txt")

print("\n" + "=" * 70)
print("RINGKASAN FITUR YANG DITAMBAHKAN")
print("=" * 70)
print("✓ assert statement dengan peringatan -O/-OO")
print("✓ Bahaya bare except (except:) dan cara menghindarinya")
print("✓ Contoh linux_interaction() dengan PlatformException")
print("✓ Perbedaan else vs kode di luar try (dengan contoh konkret)")
print("✓ Custom exception dengan docstring dan atribut tambahan")
print("✓ Panduan memilih exception type yang tepat (hirarki)")
print("✓ Program contoh lengkap dengan best practices")
print("\n📚 File ini melengkapi 'errors_exceptions.py' yang sudah ada.")
print("   Jalankan keduanya untuk pemahaman exception yang komprehensif.")