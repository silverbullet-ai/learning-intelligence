class BankAccount:

    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount > self.balance:

            print("Insufficient balance")

        else:

            self.balance -= amount

    def get_balance(self):

        return self.balance


account = BankAccount("Aahish", 5000)

account.deposit(1000)

print(account.get_balance())