class Hero:
    
    __jumlah = 0
    def __init__(self,name):
        self.name = name
        Hero.__jumlah += 1
    
    # method ini hanya berlaku untuk objek(self)
    # def getJumlah(self):
    #     return Hero.__jumlah
    
    # method ini tidak berlaku untuk objek(tidak memiliki argumen self) tapi -
    # berlaku untuk class
    # def getJumlah():
    #     return Hero.__jumlah
    
    # static method (decorator)
    @staticmethod # decoratornya
    def getJumlah():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah2(cls):
        return cls.__jumlah



badang = Hero("Badang")
yuZhong = Hero("Yu Zhong")
zilong = Hero("Zilong")

if __name__ == "__main__":
    print(Hero.getJumlah())
    print(Hero.getJumlah2())