class BankAccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount
    
    def showBalance(self):
        print(f'Account balance: $ {self.balance:.2f}')

class Savings(BankAccount):
    def __init__(self, balance: float, fees: float) -> None:
        super().__init__(balance)
        self.fees = fees
    
    def incomes(self):
        income = (self.balance * self.fees) / 12
        print(f'Interest rate: {self.fees * 100}%')
        print(f'Income: $ {income:.2f}')

account1 = Savings(float(input('Enter with your balance: $ ')),  float(input('Enter the interest rate: ')))
account1.showBalance()
account1.deposit(float(input('Amount you want to deposit: $ ')))
account1.withdraw(float(input('Amount you want to withdraw: $ ')))
account1.incomes()