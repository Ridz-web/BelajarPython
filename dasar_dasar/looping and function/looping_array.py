import time

nama = ["Ridho", "Budi", "Muta`ali"]
usia = [15, 12, 18]

for data_nama, data_usia in zip(nama, usia):
    print('Nama :' + data_nama)
    print('Usia :' + str(data_usia))
    time.sleep(4)