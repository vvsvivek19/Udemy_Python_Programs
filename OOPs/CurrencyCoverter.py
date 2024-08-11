class CurrencyConverter:
    def __init__(self,currency,rate):
        self.currency = currency
        self.rate = rate
    def set_currency(self,currency):
        self.currency = currency
    def get_currency(self):
        print('Current Currency is', self.currency)
    def set_rate(self,rate):
        self.rate = rate
    def get_rate(self):
        print('current rate of {} is {}'.format(self.currency,self.rate))
    def convert(self,amount):
        return str(amount) + ' ' + self.currency + ' to your currency is ' + str(amount * self.rate)
c1 = CurrencyConverter('USD',83.19)
print(c1.convert(1000))
c1.set_currency('AUD')
c1.set_rate(54.45)
print(c1.convert(1000))
