from abc import ABC, abstractmethod

# Generic Products 
class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class PaymentValidator(ABC):
    @abstractmethod
    def validate(self, card_number, amount):
        pass

# Concrete Product Classes (Specific Implementation)
class Paypal(PaymentProcessor, PaymentValidator):
    def process(self, amount):
        print(f"Processing Paypal Payment amount: {amount}")

    def validate(self, card_number, amount):
        print(f"Validating card: {card_number} with PayPal and amount: {amount}")
        return True  # Assume validation is successful

# Concrete Product Classes (Specific Implementation)
class Stripe(PaymentProcessor, PaymentValidator):
    def process(self, amount):
        print(f"Processing Stripe Payment amount: {amount}")

    def validate(self, card_number, amount):
        print(f"Validating card: {card_number} with Stripe and amount: {amount}")
        return True  # Assume validation is successful

_payment_processors = {
    "stripe": Stripe(),
    "paypal": Paypal(),
}

class PaymentFactory():
    def select_processor(self, processor_name):
        # if processor_name not in _payment_processors:
        #     raise f"No processor with name: {processor_name} found, available processors are {_payment_processors.keys()}"
        return _payment_processors[processor_name]


def process_payment(processor, amount: float, card_number: str):
    paymentFactory = PaymentFactory()
    paypalFactory = paymentFactory.select_processor(processor)
    paypalFactory.process(amount)
    paypalFactory.validate(card_number, amount)


process_payment('paypal', 100.0, "4111-1111-1111-1111")
process_payment('stripe', 200.0, "5500-0000-0000-0004")

