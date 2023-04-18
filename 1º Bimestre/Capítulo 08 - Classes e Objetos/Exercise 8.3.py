class BankAccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount
    
    def showBalance(self):
        print(f'Account balance: $ {self.balance:.2f}')

account1 = BankAccount(float(input('Enter with your balance: $ ')))
account1.deposit(float(input('Amount you want to deposit: $ ')))
account1.withdraw(float(input('Amount you want to withdraw: $ ')))
account1.showBalance()