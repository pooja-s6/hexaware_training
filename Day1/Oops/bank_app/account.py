# account.py
 
class Account:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
 
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
 
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")
 
    def display_balance(self):
        print(f"Account Holder: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
 
# current_account.py
 
from account import Account
 
class CurrentAccount(Account):
    def __init__(self, account_number, customer_name, balance=0, overdraft_limit=5000):
        super().__init__(account_number, customer_name, balance)
        self.overdraft_limit = overdraft_limit
 
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Overdraft limit exceeded!")
 