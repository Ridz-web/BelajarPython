class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        # variabel instance private
        self.__tglLahir = "private"
        
        # variabel instance protected
        self._protected = "protected"

user1 = User("Ridz", 16)
user2 = User("Riviel", 18)

if __name__ == "__main__":
    print(user1.__dict__)
    print(user2.__dict__)
    # print(user1.__tglLahir) akan error karena tidak bisa mengakses variabel private