def kecepatan(kecepatan, waktu):
    try:
        kecepatan = int(input("masukkan nilai kecepatan: "))
        waktu = int(input("masukkan waktu: "))
        hasil = kecepatan / waktu
        
        print(f"\nkecepatan: {hasil}")
        
    except ValueError:
        print("masukkan angka")


def luas_segitiga(alas, tinggi):
    try:
        alas = int(input("masukkan alas: "))
        tinggi = int(input("masukkan tinggi: "))
        hasil = 0.5 * alas * tinggi

        print(f"luas segitiga: {hasil}")
        
    except ValueError:
        print("masukkan angka")


def luas_persegi(sisi):
    try:
        sisi = int(input("masukkan panjang/lebar sisi: "))
        hasil = sisi * sisi
        
        print(f"luas persegi: {hasil}")
        
    except ValueError:
        print("masukkan angka")

def luas_balok(panjang, lebar, tinggi):
    try:
        panjang = int(input("masukkan panjang: "))
        lebar = int(input("masukkan lebar: "))
        tinggi = int(input("masukkan tinggi: "))
        hasil = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        
        print(f"luas balok: {hasil}")
        
    except ValueError:
        print("masukkan angka")
 

while True:
    try:
        pilihan = int(input("MENU MATEMATIKA\n\n1.kecepatan\n2.luas segitiga\n3.luas persegi\n4.luas balok\n\nmasukkan pilihan anda [1 / 2 / 3 / 4]: "))
        if pilihan == 1:
            kecepatan(0,0)
            
            lanjut = input("apakah ingin kembali ke menu[y/n]: ")
            
            if lanjut != "y":
                print("terimakashi telah menghitung")
                exit()
                
        elif pilihan == 2:
            luas_segitiga(0,0)
            
            lanjut = input("apakah ingin kembali ke menu[y/n]: ")
            
            if lanjut != "y":
                print("terimakashi telah menghitung")
                exit()
                
        elif pilihan == 3:
            luas_persegi(0)
            
            lanjut = input("apakah ingin kembali ke menu[y/n]: ")
            
            if lanjut != "y":
                print("terimakashi telah menghitung")
                exit()
                
        elif pilihan == 4:
            luas_balok(0,0,0)
            
            lanjut = input("apakah ingin kembali ke menu[y/n]: ")
            
            if lanjut != "y":
                print("terimakashi telah menghitung")
                exit()


    except ValueError:
       print("silahkan memilih menu yang ada!!")