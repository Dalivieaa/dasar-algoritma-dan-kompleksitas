# SOAL NO 7 MENENTUKAN BILANGAN TERBESAR DARI 3 ANGKA
a = int(input("masukkan angka 1:"))
b = int(input("masukkan angka 2:"))
c = int(input("masukkan angka 3:"))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b 
else:
    terbesar = c
print("terbesar",terbesar)