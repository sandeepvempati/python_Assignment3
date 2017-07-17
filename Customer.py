class Customer():
    def __init__(self,name, balance=0.0):
        self.name = name
        self.balance = balance

    def withdraw(self,amount):
        if amount>self.balance:
            raise RuntimeError("Amount greater than balance")
        self.balance -= amount
        return self.balance
    def deposit(self,deposit):
        self.balance += deposit
        return self.balance

c = Customer('san',200)

print c.withdraw(100)
print c.deposit(500)