# Game sederhana yang  setiap karakter bisa saling serang
import random

class Hero:
    def __init__(self, name, health, damage, defend):
        self.name = name
        self.health = health
        self.damage = damage
        self.defend = defend
    
    def attack(self, enemy):
        if enemy.defend == 2 :
            print(f"{self.name} memberikan {self.damage} kepada {enemy.name}")
            enemy.health -= self.damage
        else:
            print(f"{enemy.name} berhasil menghidari serangan {self.name}")
        
        print(
            f'{self.name} Health remaining : {self.health}\n'
            f'{enemy.name} Health remaining : {enemy.health}\n'
            )

if __name__ == "__main__":
    knight = Hero("Knight", 100, 8, random.randint(2,3))
    rook = Hero("Rook", 100, 8, random.randint(2,3))
    
    while knight.health > 0 and rook.health > 0:
        knight.attack(rook)
        if rook.health <= 0 or knight.health <= 0:
            break
        rook.attack(knight)