class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amt):
        self.balance += amt
        print(f"Deposited {amt}")
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print(f"Withdrawn {amt}")
        else: print("Insufficient funds")
    def display(self):
        print(f"Account: {self.owner} | Balance: {self.balance}")

acc = BankAccount("Rahul", 1000)
acc.deposit(500)
acc.display()