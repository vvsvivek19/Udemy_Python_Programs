class AccountBalanceException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

balance = 20000

def withdraw(amt):
    global balance
    global flag
    if balance - amt < 5000:
        flag = 0
        raise AccountBalanceException('Cannot withdraw, Balance will go less than 5000')
    else:
        balance = balance - amt
        print('Withdrawal was successful')
        print('Remaining Balance:',balance)
try:
    flag = 1
    while flag == 1:
        consent = input('Do you want to withdraw money: Please enter Y or N: ')
        if consent == 'y' or consent == 'Y':
            try:
                amount = int(input('Enter Amount: '))
                withdraw(amount)
            except ValueError:
                print("Please Enter a valid amount")
        else:
            print('Thankyou for choosing our services!')
            flag = 0
except AccountBalanceException as e:
    print(e)

