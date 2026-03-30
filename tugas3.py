# Variabel & tipe data
nama = "Reyx"
umur = 20
tinggi = 170.5
is_student = True
hobi = ["coding", "gaming", "scroll tiktok", "makan", "tidur"]

print("=== Variabel ===")
print(nama, umur, tinggi, is_student, hobi)

# Manipulasi string
print("\n=== String ===")
teks = "halo dunia"
print(teks + " anjing")
print(len(teks))
print(teks.upper())
print(teks.lower())

# Operasi matematika
print("\n=== Matematika ===")
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# List
print("\n=== List ===")
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
print(buah[0])
buah.append("melon")
buah.remove("jeruk")
print(buah)

# Input user
print("\n=== Input ===")
nama_user = input("Nama lu: ")
umur_user = input("Umur lu: ")
print("Halo, nama saya", nama_user, "dan umur saya", umur_user, "tahun.")
