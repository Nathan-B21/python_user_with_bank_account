

class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if(self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):

            self.balance += (self.balance*self.int_rate)
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
        
        
    def example_method(self):
        self.account.deposit(100)
        print(self.account.balance)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
        
    def make_withdrawal(self,amount):
        self.account.withdrawal(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} {self.account.display_account_info}")
        return self
        
    def transfer_money(self, other_user, amount):
        self.account.withdrawal(amount)
        other_user.account.deposit(amount)
        return self
    
account1 = BankAccount()
account2 = BankAccount()
account1.deposit(500).deposit(500).deposit(500).yield_interest().display_account_info()

account2.deposit(500).deposit(500).withdrawal(100).withdrawal(100).withdrawal(100).withdrawal(100).yield_interest().display_account_info()