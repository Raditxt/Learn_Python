"""
MATERI: ERRORS AND EXCEPTIONS (Kesalahan dan Pengecualian)
===========================================================
Di Python ada dua jenis kesalahan:
1. Syntax Errors (kesalahan sintaks) - terjadi saat parsing kode.
2. Exceptions (pengecualian) - terjadi saat eksekusi meskipun sintaks benar.
"""

print("=" * 60)
print("1. SYNTAX ERRORS (Kesalahan Sintaks)")
print("=" * 60)
print("Syntax error terjadi ketika parser Python tidak bisa memahami kode.")
print("Contoh: menghilangkan titik dua (:) setelah while True")
print("Kode berikut akan menyebabkan SyntaxError (jika tidak dikomentari):")
print("# while True print('Hello world')  # SyntaxError: missing ':'")
print("Parser menunjuk lokasi error dengan tanda panah.\n")

print("=" * 60)
print("2. EXCEPTIONS (Pengecualian)")
print("=" * 60)
print("Exception terjadi saat kode secara sintaks benar, tetapi eksekusi gagal.")
print("Contoh-contoh exception:\n")

# ZeroDivisionError
try:
    result = 10 * (1 / 0)
except ZeroDivisionError as e:
    print(f"Contoh ZeroDivisionError: {e}")

# NameError
try:
    result = 4 + spam * 3
except NameError as e:
    print(f"Contoh NameError: {e}")

# TypeError
try:
    result = '2' + 2
except TypeError as e:
    print(f"Contoh TypeError: {e}")

print("\nSetiap exception memiliki tipe yang berbeda, dan pesan error memberikan detail.\n")

print("=" * 60)
print("3. HANDLING EXCEPTIONS (Menangani Pengecualian)")
print("=" * 60)

# Contoh dasar try-except untuk input angka
print("--- Contoh 1: try-except untuk validasi integer ---")
def contoh_input():
    try:
        x = int(input("Masukkan angka (coba masukkan huruf): "))
        print(f"Anda memasukkan {x}")
    except ValueError:
        print("Oops! Bukan angka yang valid.")
contoh_input()

print("\n--- Contoh 2: Multiple except clauses ---")
try:
    num = int(input("Masukkan angka: "))
    result = 10 / num
    print(f"Hasil: {result}")
except ValueError:
    print("Error: Input bukan angka!")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")

print("\n--- Contoh 3: except dengan beberapa exception type ---")
try:
    my_list = [1, 2, 3]
    index = int(input("Masukkan index (0-2): "))
    print(f"Nilai: {my_list[index]}")
except (ValueError, IndexError) as e:
    print(f"Terjadi error: {type(e).__name__} - {e}")

print("\n--- Contoh 4: except dengan inheritance exception class ---")
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
print("Perhatikan urutan except: dari paling spesifik ke paling umum.")

print("\n--- Contoh 5: Mengakses argumen exception ---")
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(f"Tipe exception: {type(inst)}")
    print(f"Args: {inst.args}")
    print(f"inst: {inst}")
    x, y = inst.args
    print(f"x = {x}, y = {y}")

print("\n--- Contoh 6: try-except-else-finally ---")
def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Error: Pembagian dengan nol!")
    else:
        print(f"Hasil pembagian: {hasil}")
    finally:
        print("Blok finally selalu dijalankan.")
bagi(10, 2)
bagi(10, 0)

print("\n--- Contoh 7: Exception di dalam fungsi ---")
def this_fails():
    return 1 / 0

try:
    this_fails()
except ZeroDivisionError as err:
    print(f"Menangani runtime error: {err}")

print("\n" + "=" * 60)
print("4. RAISING EXCEPTIONS (Melempar Pengecualian)")
print("=" * 60)

# raise sederhana
try:
    raise NameError('HiThere')
except NameError as e:
    print(f"Menangkap NameError: {e}")

# raise ulang
print("\n--- Melempar ulang exception ---")
try:
    raise NameError('HiThere')
except NameError:
    print("Exception terbang lewat!")
    # raise  # jika di-uncomment, akan melempar lagi

print("\n" + "=" * 60)
print("5. EXCEPTION CHAINING (Rantai Pengecualian)")
print("=" * 60)

# Chaining otomatis
print("--- Rantai otomatis ---")
try:
    open("database.sqlite")
except OSError:
    # raise RuntimeError("Tidak bisa handle error")  # akan menampilkan rantai
    print("(Contoh rantai otomatis: lihat dokumentasi)")

# Chaining dengan from
print("\n--- Rantai eksplisit dengan 'from' ---")
class ConnectionError(Exception):
    pass

def func():
    raise ConnectionError("Koneksi gagal")

try:
    func()
except ConnectionError as exc:
    # raise RuntimeError('Gagal membuka database') from exc
    print("(Contoh rantai eksplisit: raise RuntimeError from exc)")

print("\n" + "=" * 60)
print("6. USER-DEFINED EXCEPTIONS (Pengecualian Buatan Pengguna)")
print("=" * 60)

class MyError(Exception):
    """Pengecualian kustom sederhana."""
    def __init__(self, message, code):
        self.message = message
        self.code = code

try:
    raise MyError("Terjadi kesalahan", 500)
except MyError as e:
    print(f"Menangkap MyError: {e.message} (kode {e.code})")

print("\n" + "=" * 60)
print("7. CLEAN-UP ACTIONS (Tindakan Pembersihan dengan finally)")
print("=" * 60)

def contoh_finally():
    try:
        print("Mencoba melakukan sesuatu...")
        raise KeyboardInterrupt
    finally:
        print("Goodbye, world!")
# contoh_finally()  # akan raise KeyboardInterrupt setelah finally

print("Contoh finally selalu dijalankan, bahkan jika exception terjadi.")
print("Contoh dengan return di finally (tidak disarankan):")
def bool_return():
    try:
        return True
    finally:
        return False
print(f"bool_return() = {bool_return()}  # finally override return")

print("\n" + "=" * 60)
print("8. PREDEFINED CLEAN-UP ACTIONS (with statement)")
print("=" * 60)

# Membuat file dummy untuk contoh
with open("contoh.txt", "w") as f:
    f.write("Baris 1\nBaris 2\n")

print("Membaca file dengan with statement (otomatis ditutup):")
with open("contoh.txt") as f:
    for line in f:
        print(line, end="")
print("\nFile sudah otomatis ditutup setelah blok with.")

import os
os.remove("contoh.txt")

print("\n" + "=" * 60)
print("9. EXCEPTIONGROUP DAN except* (Python 3.11+)")
print("=" * 60)

# Contoh ExceptionGroup
def demo_exception_group():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('Ada masalah', excs)

try:
    demo_exception_group()
except ExceptionGroup as eg:
    print(f"Tertangkap ExceptionGroup: {eg}")
    # Untuk menangani sub-exception secara selektif, gunakan except*
    # (Python 3.11+). Contoh:
    # except* OSError as e: ...

print("\nMenggunakan except* (Python 3.11+):")
try:
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup("group2", [OSError(3), RecursionError(4)])
        ]
    )
except* OSError as e:
    print(f"Menangani OSError: {e}")
except* SystemError as e:
    print(f"Menangani SystemError: {e}")
# RecursionError akan tetap tidak tertangani dan di-raise ulang

print("\n" + "=" * 60)
print("10. ENRICHING EXCEPTIONS WITH NOTES (Menambahkan Catatan)")
print("=" * 60)

try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Tambahkan informasi')
    e.add_note('Tambahkan informasi lagi')
    # raise  # jika diuncomment akan menampilkan notes
    print(f"Exception memiliki notes: {e.__notes__}")

print("\nContoh dengan ExceptionGroup dan notes:")
excs = []
for i in range(3):
    try:
        raise OSError('operation failed')
    except OSError as e:
        e.add_note(f'Terjadi di iterasi {i+1}')
        excs.append(e)

try:
    raise ExceptionGroup('Kami punya masalah', excs)
except ExceptionGroup as eg:
    print(f"ExceptionGroup dengan {len(eg.exceptions)} sub-exception:")
    for sub in eg.exceptions:
        print(f" - {sub}, notes: {sub.__notes__}")

print("\n" + "=" * 60)
print("RINGKASAN / KEY POINTS")
print("=" * 60)
print("1. Syntax error: kesalahan parsing, program tidak bisa dijalankan.")
print("2. Exception: kesalahan saat runtime, bisa ditangani dengan try/except.")
print("3. Gunakan multiple except untuk tipe exception berbeda.")
print("4. else: dijalankan jika try sukses, finally: selalu dijalankan.")
print("5. raise: melempar exception secara manual.")
print("6. Buat exception sendiri dengan menurunkan dari Exception.")
print("7. with statement: otomatis membersihkan resource (file, koneksi).")
print("8. ExceptionGroup untuk mengumpulkan beberapa exception (Python 3.11+).")
print("9. add_note() untuk menambah informasi ke exception.")