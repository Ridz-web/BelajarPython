class Hero:
    
    def __init__(self,name,health,armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
    
    @property
    def info(self):
        return "name {} : \n\thealth : {}\n\tarmor : {}".format(self.__name, self.__health, self.__armor)

    # getter & setter
    @property
    def armor(self):
        pass
    
    @armor.getter
    def getarmor(self):
        return self.__armor
    
    @armor.setter
    def setarmor(self, inputArmor):
        self.__armor = inputArmor
    
    @armor.deleter
    def delarmor(self):
        print("armor di delete")
        self.__armor = None

zilong = Hero("zilong", 100, 10)
hylos = Hero("hylos", 400, 50)

if __name__ == "__main__":
    print(hylos.__dict__)
    hylos.setarmor = 40
    
    print(hylos.setarmor)
    print(hylos.__dict__)
    
    del hylos.delarmor
    print(hylos.__dict__)