from services import db
from tabulate import tabulate

def tambah():
    id_list = input  ('kode list          : ')
    todolist = input ('tambah list        : ')
    tanggal = input  ('tanggal penambahan : ')
    
    db.add_list(id_list, todolist, tanggal)
    

def hapus():
    id_list = input('kode list          : ')
    db.remove_list(id_list)

def check():
    headers = ['id_list', 'todolist', 'upload date']
    items = db.fetch_item()
    print(tabulate(items, headers=headers, tablefmt='grid'))

def main():
    while True:
        try:
            choice = int(input('MENU\n1.tambah list\n2.hapus list\n3.check list\n4.keluar\npilihan anda: '))
            if choice == 1:
                tambah()
            elif choice == 2:
                hapus()
            elif choice == 3:
                check()
            elif choice == 4:
                exit()
            else:
                print('masukkan pilihan yang ada di menu')
        except ValueError:
            print('masukkan angka 1 - 4 untuk memilih')

if __name__ == "__main__":
    main()