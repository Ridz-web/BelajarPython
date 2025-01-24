class car:
    def __init__(self, merk, warna, nomor_plat):
        self.merk = merk
        self.warna = warna
        self.nomor_plat = nomor_plat
    
    def deskripsi(self):
        return f"kendaraan {self.merk} dengan warna {self.warna} dan nomor plat {self.nomor_plat}"

class sport_car(car):
    def __init__(self, merk, warna, nomor_plat, kecepatan_max):
        super().__init__(merk, warna, nomor_plat)
        self.kecepatan_max = kecepatan_max
        
    def kecepatan(self):
            return f"kecepatan maksimal {self.kecepatan_max} m/s"

class bus(car):
    def __init__(self,merk, warna, nomor_plat, jumlah_kursi, rute):
         super().__init__(merk,warna, nomor_plat)
         self.jml_kursi = jumlah_kursi
         self.rute = rute
    
    def angkutan(self):
        return f"bus memiliki jumlah {self.jml_kursi} kursi kosong dengan rute {self.rute}"

sport = sport_car("toyota", "hitam", "P001", "50")
bis = bus("sinar jaya", "putih corak warna warni", "P002", "57", "semarang - jakarta dan sekitarnya")

print(sport.deskripsi())
print(sport.kecepatan())

print(bis.deskripsi())
print(bis.angkutan())