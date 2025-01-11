import random
import time

# Kelas Player
class Player:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, damage, monster):
        monster.health -= damage
        self.energy -= damage

        if damage == 5:
            print(f'Player critical damage to monster: {damage}')
            self.health += 2
            print(f'Player mendapatkan regen health: +2')

        else:
            print(f'Player damage to monster: {damage}')

        if monster.is_attack():
            self.health -= monster.damage
            print(
                f'Kamu terkena serangan balik sebesar {monster.damage} damage.\n'
                f'Your health: {self.health}\n'
                f'Monster health: {monster.health}\n'
                f'Your energy: {self.energy}\n'
            )
            time.sleep(0.5)

            serang_lagi = input('Apakah ingin menyerang lagi? [y/n]: ').lower()
            if serang_lagi != 'y':
                print('Anda kabur dari pertarungan!')
                exit()
        else:
            print('Monster tidak menyerang... zZZ')

# Kelas Monster
class Monster:
    def __init__(self, health):
        self.health = health
        self.health_default = health
        self.damage = random.randint(2, 7)

    def is_attack(self):
        return self.health < self.health_default


player = Player(health=100, energy=100)
monster = Monster(100)

while True:
    damage = random.randint(1, 5)
    player.attack(damage, monster)

    if player.energy <= 0:
        print('Anda kalah karena kehabisan energi!')
        break
    elif player.health <= 0:
        print('Anda kalah karena kehabisan health!')
        break
    elif monster.health <= 0:
        print('Selamat! Anda berhasil mengalahkan monster!')
        break
