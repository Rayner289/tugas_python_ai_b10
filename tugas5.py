def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka), 2)

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self):
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"

if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Rayner"))
    print(tambah(5, 7))
    print(tambah(10))
    print(rata_rata([80, 90, 100]))
    print(rata_rata([]))

    print("\n=== CLASS STUDENT ===")

    s1 = Student("Rayner", "A123")
    s1.tambah_nilai(80)
    s1.tambah_nilai(85)
    s1.tambah_nilai(90)

    s2 = Student("Andi", "B456")
    s2.tambah_nilai(60)
    s2.tambah_nilai(65)
    s2.tambah_nilai(70)

    print(s1)
    print("Rata-rata:", s1.rata_nilai())
    print("Status:", s1.status())

    print()

    print(s2)
    print("Rata-rata:", s2.rata_nilai())
    print("Status:", s2.status())
