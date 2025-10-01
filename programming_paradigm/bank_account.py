class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
            return True
        else:
            return False
            
    def display_balance(self):
        print(f'Account Balance: {self.account_balance}')
            
acc = BankAccount(200)
acc.deposit(50)
acc.withdraw(100)
acc.display_balance()  # Current balance: 150
