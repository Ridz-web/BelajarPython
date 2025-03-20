class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, inputBalance):
        self.inputBalance = inputBalance
        self.balance += self.inputBalance
        return "Deposit : Rp{}\nSaldo setelah deposit : Rp{}".format(self.inputBalance, self.balance)
    
    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount
        if self.balance < 0:
            self.balance += amount
            return "saldo anda kurang!"
        else:
            return "Penarikan : {}\nSaldo setelah penarikan : {}".format(self.amount, self.balance)
        
    
    def showBalance(self):
        return "Akun : {}\nSaldo: Rp{}".format(self.owner, self.balance)


class saveAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.interest_rate = 0.05
    
    def add_interest(self):
        interest = self.interest_rate * self.balance
        self.balance += interest
        return "[Tabungan]\nBunga : 5%\nSaldo : Rp{}".format(self.balance)


ridho = saveAccount("Ridho", 10_000)

print(ridho.showBalance())
print(ridho.deposit(50_000))
print(ridho.withdraw(5_000))
print(ridho.add_interest())
