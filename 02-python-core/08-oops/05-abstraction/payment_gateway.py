from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid via UPI")


class Card(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid via Card")


class Wallet(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid via Wallet")


payments = [
    UPI(),
    Card(),
    Wallet()
]

for payment in payments:

    payment.pay(500)