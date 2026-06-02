class Account:

    def __init__(self, balance):

        self.balance = balance


class SavingsAccount(Account):

    def interest(self):

        return self.balance * 0.05


account = SavingsAccount(10000)

print(account.interest())