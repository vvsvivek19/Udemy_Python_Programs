class MinimumBalanceError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class BankAccount:
    AccNumber = 1001

    def __init__(self, name, balance):
        self.name = name
        try:
            if balance < 1000:
                raise MinimumBalanceError('Account Cannot be Created')
            else:
                self.balance = balance
        except MinimumBalanceError as m:
            print(m)
        self.AccountNumber = BankAccount.AccNumber
        BankAccount.AccNumber += 1

    def deposit(self, amount):
        self.balance += amount
        print('Rs {} deposited successfully!'.format(amount))
        print('New balance:', self.balance)

    def withdrawal(self, amount):
        try:
            if self.balance - amount < 1000:
                raise MinimumBalanceError('Minimum Balance cannot be less than 1000!')
            else:
                self.balance -= amount
                print('Withdrawal Successful!! Please take your money!')
                print('Balance Remaining:', self.balance)
        except MinimumBalanceError as m:
            print(m)

    def show_details(self):
        print('Welcome to Our Bank')
        print('*' * 20)
        print("Account Holder's Name:", self.name)
        print('Account Number:', self.AccountNumber)
        print('Balance:', self.balance)
        print('*' * 20)


cus1 = BankAccount('Vivek Singh', 200000)
cus1.show_details()
cus2 = BankAccount('Bittu Singh', 100000)
cus2.show_details()
cus3 = BankAccount('Vidhwansh Kumar', 150000)
cus3.show_details()
