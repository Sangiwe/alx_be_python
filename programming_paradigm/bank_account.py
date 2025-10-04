class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = float(initial_balance)

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"

    def deposit(self, amount):
        self.account_balance += amount
        return True  

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True   
        else:
            return False  
