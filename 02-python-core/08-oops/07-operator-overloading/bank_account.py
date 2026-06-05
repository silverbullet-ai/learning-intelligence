class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def __add__(self, other):

        return self.balance + other.balance

    def __repr__(self):

        return (
            f"BankAccount("
            f"owner='{self.owner}', "
            f"balance={self.balance})"
        )


acc1 = BankAccount(
    "Aahish",
    50000
)

acc2 = BankAccount(
    "Manav",
    25000
)

print(acc1 + acc2)