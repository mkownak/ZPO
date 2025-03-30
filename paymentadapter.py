class PayPalPayment:
    def pay(self, amount:float)->str:
        return "PayPal Payment of {}".format(amount)

class StripePayment:
    def pay(self, amount:float)->str:
        return "Stripe Payment of {}".format(amount)

class PaymentAdapter:
    def __init__(self, method = PayPalPayment):
        self.method = method

    def pay(self, amount:float)->None:
        print(self.method.pay(amount))


Paypal = PayPalPayment()
Stripe = StripePayment()

PaymentAdapter = PaymentAdapter(Stripe)
PaymentAdapter.pay(100.5)
