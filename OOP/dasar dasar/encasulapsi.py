class User:

    def __init__(self, name, umur):
        self.__name = name
        self.__umur = umur
    # getter ( mengambil variabel private )
    def getName(self):
        return self.__name
    # setter ( mengedit/setting value dari variabel private )
    def ulangTahun(self, umurBertambah):
        self.__umur += umurBertambah
        return

Riviel = User("Riviel", 16)

print(Riviel.__dict__)
print(Riviel.getName())
print(Riviel.ulangTahun(2))
