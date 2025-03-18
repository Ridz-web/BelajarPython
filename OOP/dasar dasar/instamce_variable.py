class Hero:
    jumlah = 0
    
    def __init__(self, name, health, attack, defend):
        self.name = name
        self.health = health
        self.attack = attack
        self.defend = defend
        Hero.jumlah += 1
        print(f"Membuat hero dengan nama {name}")


if __name__ == "__main__":
    hero1 = Hero("Knight", 100, 8, 10)
    print(Hero.jumlah)
    hero2 = Hero("Rook", 150, 4, 10)
    print(Hero.jumlah)