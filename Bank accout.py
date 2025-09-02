class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount, "New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount, "Remaining Balance:", self.balance)
        else:
            print("Insufficient funds!")

account = BankAccount("Niranjan", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
