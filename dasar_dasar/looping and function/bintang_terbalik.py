def bintang(n):
    star = "*"
    spasi = ""
    for i in range(n, 0, -1):
        print(spasi + star * i)
        spasi += " "

if __name__ == "__main__":
    angka = int(input("masukan angka: "))
    bintang(angka)