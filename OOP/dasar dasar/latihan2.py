class pet:
    
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def showInfo(self):
        print("Nama : {}\nJenis : {}\nUsia : {} Tahun".format(self.name, self.species, self.age))

class dog(pet):
    
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Anjing"
    
    def makeSound(self):
        print("Suara : Woof!")
    
    


class cat(pet):
    
    def __init__(self, name, age):
        super().__init__(name, age)
        self.species = "Kucing"
            
    def makeSound(self):
        print("Suara : Meow!")
    
   


anjing = dog("Buddy", 3)
kucing = cat("Kitty", 2)

anjing.showInfo()
anjing.makeSound()
print("\n")
kucing.showInfo()
kucing.makeSound()