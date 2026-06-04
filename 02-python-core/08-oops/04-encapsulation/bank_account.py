class BankAccount:

    def __init__(self, account_number, balance=0):

        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

        else:

            print("Insufficient balance")

    def get_balance(self):

        return self.__balance


account = BankAccount("ACC101", 5000)

account.deposit(1000)

print(account.get_balance())