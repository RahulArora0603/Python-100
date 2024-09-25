
class Account:
    def __init__(self, accnumber,userId,name, initialamt):
        self.accnumber = accnumber
        self.userId = userId
        self.name = name
        self.accBalance = initialamt


    def deposit(self, amount):
        self.amount = amount
        self.accBalance = self.accBalance + amount

    def withdraw(self, amount1):
        self.amount1 = amount1
        if self.accBalance<amount1:
            print("Error! Not enough balance.")
        else:
            self.accBalance = self.accBalance - amount1    

    def balance(self):
        print(self.accBalance)

acc1 = Account(1, 1001, "Rahul", 100)
acc1.deposit(20)
acc1.deposit(1000)
acc1.withdraw(500)
acc1.balance()