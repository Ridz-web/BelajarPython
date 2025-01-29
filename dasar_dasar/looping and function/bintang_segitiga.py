def segitiga(n):
    for i in range(1, n + 1):
        spasi = ""
        bintang = ""
    
        for j in range(n - i):
         spasi += " "
        
        for k in range(2 * i - 1):
            bintang += "*"
        print(spasi + bintang)

def segitiga_terbalik(n):
    for i in range(n, 0, -1):
        spasi = ""
        bintang = ""
    
        for j in range(n - i):
         spasi += " "
        
        for k in range(2 * i - 1):
            bintang += "*"
        print(spasi + bintang)


tinggi = int(input("masukan angka: "))
segitiga(tinggi)
segitiga_terbalik(tinggi)