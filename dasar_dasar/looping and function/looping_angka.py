def looping_angka(n):
    for i in range(1, n+1):
        print(str(i) * i)


def angka_terbalik(n):
    for i in range(n, 0, -1):
        print(str(i) * i)

if __name__ == "__main__":
    angka = int(input("masukkan angka: "))
    looping_angka(angka)
    angka_terbalik(angka)