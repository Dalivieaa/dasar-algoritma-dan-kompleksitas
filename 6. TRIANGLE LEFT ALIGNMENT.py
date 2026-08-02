# SOAL NO 6 TRIANGLE LEFT ALIGNMENT, jika tidak dimulai dari satu index 0 tidak di cetak
n = int(input("Masukkan jumlah baris:"))
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()  