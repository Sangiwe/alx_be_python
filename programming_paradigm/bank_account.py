class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        print(f"Deposited: ${amount}")
        
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
            
    def display_balance(self):
        print(f'Current Balance: {self.account_balance}')
            
acc = BankAccount(200)
acc.deposit(50)
acc.withdraw(100)
acc.display_balance()  # Current balance: 150
