from services import db
from simple_app import main

def add():
    kode_barang = input('kode barang: ')
    nama_barang = input('nama barang: ')
    stok_barang = int(input('stok barang: '))
    harga_barang = int(input('harga barang: Rp'))
    
    db.insert_item(kode_barang, nama_barang, stok_barang, harga_barang)

def check():
   itemss = db.fetch_item()
   for item in itemss:
       kode_barang = item[1]
       nama_barang = item[2]
       stok_barang = item[3]
       harga_barang = item[4]
       print(f'''
kode item: {kode_barang}
{nama_barang} | Rp{harga_barang}
stok item: {stok_barang}

''')

def warung() :
    while True:
        try :
            menu = int(input('MENU :\n\n1. Tambah barang\n2. Check barang\n3. Kembali\n\npilihan anda : '))

            if menu == 1:
                add()
            elif menu == 2:
                check()
            elif menu == 3:
                main()
            else:
                print('tolong masukkan pilihan yang ada di menu!!')
                continue
        except ValueError:
            print('tolong masukkan pilihan yang ada di menu!!')
            continue


if __name__ == '__main__' :
    warung()