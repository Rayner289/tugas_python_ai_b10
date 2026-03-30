import numpy as np
import pandas as pd

np.random.seed(42)

nilai_np = np.random.randint(50, 100, 10)

rata = np.mean(nilai_np)
median = np.median(nilai_np)
std = np.std(nilai_np)
min_n = np.min(nilai_np)
max_n = np.max(nilai_np)

data = {
    "nama": ["Rayner", "Andi", "Siti", "Rina", "Doni"],
    "nim": ["A1", "A2", "A3", "A4", "A5"],
    "nilai": nilai_np[:5]
}

df = pd.DataFrame(data)
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

def tulis_ringkasan(path):
    with open(path, "w") as f:
        f.write("=== STATISTIK NUMPY ===\n")
        f.write(f"Rata-rata: {rata}\n")
        f.write(f"Median: {median}\n")
        f.write(f"Standar Deviasi: {std}\n")
        f.write(f"Minimum: {min_n}\n")
        f.write(f"Maksimum: {max_n}\n\n")

        f.write("=== DATAFRAME ===\n")
        f.write(f"Jumlah data: {len(df)}\n")
        lulus = (df["status"] == "LULUS").sum()
        tidak = (df["status"] == "TIDAK LULUS").sum()
        f.write(f"Lulus: {lulus}\n")
        f.write(f"Tidak lulus: {tidak}\n")

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("\n=== GRADEBOOK ===\n")
            f.write(f"Average: {self.average()}\n")
            f.write(f"Pass rate: {self.pass_rate()}%\n")

    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average()})"

if __name__ == "__main__":
    print("=== NUMPY ===")
    print("Data:", nilai_np)
    print("Rata-rata:", rata)
    print("Median:", median)
    print("Standar deviasi:", std)
    print("Minimum:", min_n)
    print("Maksimum:", max_n)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print("Average:", gb.average())
    print("Pass rate:", gb.pass_rate())

    file_path = "ringkasan_tugas6.txt"
    tulis_ringkasan(file_path)
    gb.save_summary(file_path)

    print("\nRingkasan disimpan ke", file_path)
