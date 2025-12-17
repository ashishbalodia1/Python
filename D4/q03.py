# Q3. (Easy–Medium) — Encapsulation
# Create a class Account:
# private attribute: _balance
# methods: deposit(), withdraw(), get_balance()
# Ensure balance cannot be accessed directly.

class Account:
    def __init__(self,balance):
        self.balance=balance             # attribute
    
    def deposite(self, amount):
        if self.balance>0:
            self.balance+=amount
        print(f"{self.balance} Rs has been deposited to your account.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance-=amount    
        print(f"{self.balance} Rs have been withdrawn from your account.")

    def get_balance(self):
        return self.balance
    
b1=Account(1000)

b1.deposite(400)
b1.withdraw(500)
print(f"Your current balance: {b1.get_balance()}")
