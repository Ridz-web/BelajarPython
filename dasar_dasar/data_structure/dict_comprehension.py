siswa = [
    ('andi', 90),
    ('eko', 85),
    ('rendy', 74),
    ('roma', 93),
    ('lilia', 65),
    ('mukidi', 70),
    ('setiawan', 80)
]

nilai_siswa = {nama: nilai for nama, nilai in siswa} # mencetak seluruh key dan value ke dalam dictionaries
siswa_lulus = {nama: nilai for nama, nilai in siswa if nilai >= 80} # hanya mencetak element yang valuenya di >= 80

print(nilai_siswa)
print(siswa_lulus)

# memangkat kan angka jika angka tersebut adalah genap dan negaitve jika ganjil
angka = [i for i in range(1, 11)]
angka_custom = {value: value**2 if value % 2 == 0 else -value**1 for value in angka}
print(angka_custom)

# value dipangkatkan 3
angka = [1,2,3,4,5]
new_angka = {num: num**3 for num in angka}
print(new_angka)

# menggabungkan dua list
buah = ["Apple", "Mangga", "jeruk"]
harga = [15_000,20_000,12_000]

buah_merge = dict(zip(buah, harga))
print(buah_merge)

# filter data
data = {'a': 10, 'b': 23, 'c': 5, 'd': 40, 'a': 20}
new_data = {key: value for key,value in data.items() if value % 2 == 0}
print(new_data)