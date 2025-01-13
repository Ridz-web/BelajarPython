# class dalam oop
class Hero:
    pass

hero1 = Hero()
hero2 = Hero()

hero1.name = 'rajaKegelapan'
hero1.health = 1000

hero2.name = 'rajaIblis'
hero2.health = 800

print(hero1.__dict__)
print(hero2.__dict__)