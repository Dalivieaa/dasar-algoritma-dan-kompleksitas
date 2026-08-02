# SOAL NO 8 GANJIL GENAP
n = int(input("masukkan angka:"))

if n % 2==0:
    print("genap")
else:
    print("ganjil")

# SOAL NO 9 MENENTUKAN BIL PRIMA
n = int(input("masukkan angka:"))

if n <=1:
    print("bukan bilangan prima")
else:
    is_prima = True
    for i in range(2,n):
        if n % i == 0:
            is_prima = False
            break

    if is_prima:
        print("bilangan prima")
    else:
        print("bukan bilangan prima")