saldo_awal = input('berapa saldo anda sebelum deposit?')
deposit = input('berapa jumlah saldo yang anda depositkan?')
saldo_akhir = int(saldo_awal) + int(deposit)

print('saldo awal : Rp' + str(saldo_awal))
print('saldo deposit : Rp' + str(deposit))
print('total saldo : Rp' + str(saldo_akhir))