user_name = input('masukkan user name anda!')
password = input('masukkan password')

while True :
    konfirmasi_password = input('konfirmasi password anda')
    if konfirmasi_password != password :
        print('password salah')
        continue
    else :
        print('terimakasih sudah mendaftar')
        break