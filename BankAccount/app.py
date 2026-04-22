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
    
first_account = BankAccount(0.02, 0)
second_account = BankAccount(0.05, 1000)

first_account.deposit(50).deposit(40).deposit(100).withdraw(70).yield_interest().display_account_info()
second_account.deposit(100).deposit(150).withdraw(50).withdraw(20).withdraw(15).withdraw(30).yield_interest().display_account_info()
