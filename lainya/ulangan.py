import time

saldo_awal = 10_000
deposit = int(input('berapa saldo yang ingin anda depositkan?'))
saldo_sementara = saldo_awal + deposit
hutang = 50_000
saldo_akhir = saldo_sementara - hutang

print('saldo anda sebelumnya adalah : ' + str(saldo_awal) )
time.sleep(1)
print('saldo anda sekarang : ' + str(saldo_sementara))
time.sleep(0.5)
print('hutang anda sebesar : ' + str(hutang))
time.sleep(0.5)

if saldo_sementara >= hutang :
    print('saldo anda akan otomatis di kurangi karena adanya hutang')
    time.sleep(0.5)
    print('saldo anda menjadi : ' + str(saldo_akhir))
else :
    print('saldo anda masih belum cukup untuk membayar hutang')
    time.sleep(0.5)
    print('perabotan di rumah anda akan disita dan seluruh saldo anda telah habis')