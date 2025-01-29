angka = int(input("masukan angka: "))
genap = 0
ganjil = 0

for genap_ganjil in range(angka + 1):
    if genap_ganjil % 2 == 0:
        genap += 1
    elif genap_ganjil % 2 == 1:
        ganjil += 1
    else:
        print("masukkan sebuah angka")
        break

print(f"input user adalah: {angka}")
print(f"bilangan genap   : {genap}")
print(f"bilangan ganjil  : {ganjil}")