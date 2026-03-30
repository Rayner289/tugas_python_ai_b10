print("=== LIST ===")
data = ["data1", 1, 2.5, "data2", 10, "data3"]
print(data[0], data[-1])
print(data[1:5:2])

print("Sebelum:", data)
data.append("data_baru")
data.insert(1, "tambahan")
data.extend([100, 200])
data.pop()
data.remove("data1")
print("Sesudah:", data)

print("\n=== TUPLE ===")
t = (1, 2, 3, 4, 5)
print(len(t))
print(t[2])
a, b, *rest = t
print(a, b, rest)

print("\n=== SET ===")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

duplikat = {1, 1, 2, 2, 3}
print(duplikat)

print("\n=== DICT ===")
mhs = {
    "nama": "Rayner",
    "nim": "123",
    "angkatan": 2023,
    "kota": "Batam"
}
mhs["prodi"] = "Sistem Informasi"
mhs["kota"] = "Jakarta"
del mhs["angkatan"]

print(mhs.keys())
print(mhs.values())
print(mhs.items())

for k, v in mhs.items():
    print(k, ":", v)

print("\n=== NESTED ===")
buku = [
    {"judul": "Pemrograman Python", "penulis": "A", "tahun": 2020},
    {"judul": "Struktur Data", "penulis": "B", "tahun": 2022},
    {"judul": "Basis Data", "penulis": "C", "tahun": 2019},
    {"judul": "Machine Learning", "penulis": "D", "tahun": 2023}
]

for b in buku:
    print(b["judul"])

baru = [b for b in buku if b["tahun"] >= 2021]
print(baru)

print("\n=== COMPREHENSION ===")
angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]
print(genap)
print(kuadrat)

dict_comp = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print(dict_comp)

kalimat = "Halo Dunia Rayner"
set_comp = {c.lower() for c in kalimat if c != " "}
print(set_comp)

print("\n=== CEK ===")
print(10 in angka)
print(5 in angka)
print(angka.index(5))
