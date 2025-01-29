angka = int(input("masukkan angka: "))
hasil = 0

for tambah in range(angka + 1):
    hasil += tambah

print(hasil)

hasil1 = 0
tambah = 0
while tambah <= angka:
    hasil1 += tambah
    tambah += 1

print(hasil1)