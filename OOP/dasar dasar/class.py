class Hero:
    def __init__(self, name, health, attack, defend):
        self.name = name
        self.health = health
        self.attack = attack
        self.defend = defend

hero1 = Hero("Knight", 100, 8, 10)
hero2 = Hero("Rook", 150, 4, 10)

if __name__ == "__main__":
    print(hero1.__dict__)
    print(hero2.__dict__)