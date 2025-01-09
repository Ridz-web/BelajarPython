import random 

cuypy_position = random.randint(1,4)

print('******************************')
print('**  WELCOME TO CUYPY GAMES  **')
print('******************************')
print()

nama_user = input('siapa nama anda? ')
bentuk_lubang = '|_|'
lubang = [bentuk_lubang] * 4
lubang_kosong = lubang.copy()
print(" ".join(lubang_kosong)) # menampilkan array dalam bentuk satu string
lubang[cuypy_position - 1 ] = '|0_0|'

while True :
    try :
        jawaban = int(input('lubang nomer berapa yang ingin anda pilih [1 / 2 / 3 / 4]: '))
        if jawaban > 4 : 
            # jika jawaban tidak sesuai dengan pilihan
            print('jawaban tidak valid, silahkan pilih jawaban lain')
            print()
            continue
        else : 
            # mengkonfirmasi jawaban dari user
            konfirmasi = input(f'apakah anda yakin memilih nomer {jawaban}? [y/n]: ')
            print()
            if konfirmasi != "y" :
                print('silahkan pilih jawaban lain')
                continue # jika user memilih selain y maka kode akan tereksekusi ulang dari while True
            else :
                if jawaban == cuypy_position :
                    print(f'Selamat {nama_user} anda menang cuypy ada di lubang ke {cuypy_position}')
                    print(" ".join(lubang))
                else :
                    print(f'maaf jawaban kamu salah cuypy berada di lubang ke {cuypy_position} ')
                    print(" ".join(lubang))
                break # menghentikan program/kode
    except ValueError : # jika pada seksi "try" ada yang error maka akan di alihkan ke sini
        print('pilih jawaban dari salah satu pilihan yang di sediakan [1 / 2 / 3 / 4]') 
        continue