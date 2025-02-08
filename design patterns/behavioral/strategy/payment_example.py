from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass

# These are the implementations of the PaymentStrategy interface.
class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'Paying {amount} using Credit Card')

class PayPalStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'Paying {amount} using Paypal')

class BitcoinStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'Paying {amount} using Bitcoin')

# Context
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy  = payment_strategy
    
    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self._payment_strategy  = payment_strategy

    def checkout(self, amount):
        self._payment_strategy.pay(amount)
    
# Client Code
if __name__ == "__main__":
    cart = ShoppingCart(CreditCardStrategy())
    cart.checkout(100)  # Output: Paying 100 using Credit Card

    cart.set_payment_strategy(PayPalStrategy())
    cart.checkout(200)  # Output: Paying 200 using PayPal

    cart.set_payment_strategy(BitcoinStrategy())
    cart.checkout(300)  # Output: Paying 300 using Bitcoin
