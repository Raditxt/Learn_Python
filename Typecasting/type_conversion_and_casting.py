# belajar type conversion
# dari programiz

print("=== implicit conversion ===")
# python otomatis ubah int ke float kalo perlu
bil_int = 123
bil_float = 1.23
hasil = bil_int + bil_float
print(hasil, type(hasil))

# kalo string + int error
# contoh: '12' + 23  # error

print("\n=== explicit conversion (typecasting) ===")
# pake int(), float(), str()
s = '12'
i = 23
print("sebelum:", s, type(s))
s = int(s)  # casting ke int
print("sesudah:", s, type(s))
jumlah = s + i
print(jumlah, type(jumlah))

print("\n=== contoh casting lain ===")
# float ke int -> ilang angka di belakang koma
x = 3.99
y = int(x)
print(x, "->", y)

# int ke str
z = 100
z_str = str(z)
print(z, type(z), "->", z_str, type(z_str))

# str ke float
a = "3.14"
a_float = float(a)
print(a, type(a), "->", a_float, type(a_float))

# boolean dari int
print(bool(0), bool(1), bool(999))

print("\n=== intinya ===")
print("- implicit: otomatis, aman (ga ilang data)")
print("- explicit: manual pake int(), dll, bisa ilang data")
print("- type() buat liat tipe")