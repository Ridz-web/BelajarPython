
number = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']


while True:
    password = input('buat password anda: ')
    
    jumlah_angka = sum(1 for char in password if char in number)
    jumlah_huruf = sum(1 for char in password if char.isalpha())
    
    if len(password) < 8:
        print("password harus lebih dari 8 karakter")
    else:

        if jumlah_angka <= 1 or jumlah_huruf <= 4:
            keamanan = 'lemah'
            konfirmasi = input('password anda terlalu lemah, ingin mengganti? [y/n]: ')

            if konfirmasi.lower() == 'n': 
                 print(f"sandi anda telah ditetapkan dengan keamanan: {keamanan}")
                 break


        elif jumlah_angka == 2 and jumlah_huruf >= 5:
            keamanan = 'sedang'
            konfirmasi = input('password anda terlalu lemah, ingin mengganti? [y/n]: ')

            if konfirmasi.lower() == 'n': 
                 print(f"sandi anda telah ditetapkan dengan keamanan: {keamanan}")
                 break


        elif jumlah_angka >= 3 and jumlah_huruf >= 5:
            while True:
                keamanan = 'tinggi'
                konfirmasi_password = input('konfirmasi password anda: ')
                if konfirmasi_password == password:
                    print(f'password anda telah di tetapkan dengan keamanan: {keamanan}')
                    exit()
                else:
                    print('\npassword salah')