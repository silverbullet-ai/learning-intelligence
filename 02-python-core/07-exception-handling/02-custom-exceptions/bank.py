class InsufficientBalanceException(Exception):
    """Raised when withdrawal amount exceeds balance"""
    pass


class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited.")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientBalanceException(
                "Withdrawal amount exceeds available balance."
            )

        self.balance -= amount
        print(f"₹{amount} withdrawn.")
        print(f"Current Balance: ₹{self.balance}")

    def get_balance(self):
        return self.balance


try:
    account = BankAccount("Aahish", 5000)

    print(f"Initial Balance: ₹{account.get_balance()}")

    account.withdraw(7000)

except InsufficientBalanceException as e:
    print(f"InsufficientBalanceException: {e}")