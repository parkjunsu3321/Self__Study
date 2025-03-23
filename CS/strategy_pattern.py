from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount: float):
        print(f"{amount}원 결제 완료 (신용카드 - {self.card_number[-4:]})")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"{amount}원 결제 완료 (PayPal - {self.email})")

class VirtualAccountPayment(PaymentStrategy):
    def __init__(self, account_number: str):
        self.account_number = account_number

    def pay(self, amount: float):
        print(f"{amount}원 결제 완료 (가상계좌 - {self.account_number})")

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount: float):
        self._strategy.pay(amount)

if __name__ == "__main__":
    credit_card = CreditCardPayment("1234-5678-9876-5432", "123")
    payment_processor = PaymentProcessor(credit_card)
    payment_processor.process_payment(50000)

    paypal = PayPalPayment("user@example.com")
    payment_processor.set_strategy(paypal)
    payment_processor.process_payment(30000)

    virtual_account = VirtualAccountPayment("110-123-456789")
    payment_processor.set_strategy(virtual_account)
    payment_processor.process_payment(70000)