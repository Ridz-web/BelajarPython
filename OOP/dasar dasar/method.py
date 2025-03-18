class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    # void function, method tanpa return
    def kenalan(self):
        print(f"hai namaku {self.name}")
        
    # method dengan argumen
    def healthUp(self, up):
        self.health += up
    
    # method dengan return
    def getHealth(self):
        return self.health


if __name__ == "__main__":
     hero1 = Hero("knight", 100, 8)
     hero2 = Hero("Rook", 120, 4)
     
     hero1.kenalan()
     hero2.healthUp(5)
     print(hero2.health)
     print(hero1.getHealth())