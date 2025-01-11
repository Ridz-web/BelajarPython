# __ private attribute (hanya bisa digunakan di class sendiri)
# _ protected attribute (hanya bisa di gunakan di class dan class turunan dari class awal tersebut)


class Player:
    # attribute 
    name = 'Ridz'
    __age = 15 # private
    
    # cara agar private object bisa diakses keluar
    def user_age(self):
        return self.__age   
    

Player = Player()
print(Player.user_age())