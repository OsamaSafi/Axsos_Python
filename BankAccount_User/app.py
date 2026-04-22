class BankAccount:
    def __init__(self,int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self
    

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            'first_account' : BankAccount(int_rate=0.02, balance=0),
            'secound_account' : BankAccount(int_rate=0.05, balance=100),
        }
    
    def make_deposit(self,amount,type_account):
        self.account[type_account].deposit(amount)
        return self
    
    def make_withdraw(self,amount,type_account):
        self.account[type_account].withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"--------{self.name}-----------")
        for account_type , account_info in self.account.items():
            print(f"Account: {account_type.capitalize()}")
            account_info.display_account_info()
            print('')
        return self


user = User('osama')
user.make_deposit(20,'first_account')
user.make_deposit(30,"first_account")
user.make_withdraw(10,"first_account")
user.make_deposit(20,'secound_account')
user.make_deposit(30,"secound_account")
user.make_withdraw(10,"secound_account")
user.display_user_balance()