class User:
    def __init__(self,name):
        self.name = name
        self.balance = 0

    def make_deposit(self,amount):
        self.balance += amount
        return self
    
    def make_withdrow(self,amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} , Balance ${self.balance}")

    def transfer_money(self,other_user,amount):
        self.make_withdrow(amount)
        other_user.make_deposit(amount)
        return self

osama = User('osama')
omar = User('omar')
nesma = User('nesma')

osama.make_deposit(50)
osama.make_deposit(100)
osama.make_deposit(150)
osama.make_withdrow(130)
osama.display_user_balance()

omar.make_deposit(100)
omar.make_deposit(200)
omar.make_deposit(50)
omar.make_deposit(70)
omar.display_user_balance()

nesma.make_deposit(500)
nesma.make_withdrow(30)
nesma.make_withdrow(100)
nesma.make_withdrow(140)
nesma.display_user_balance()
print("#######################")

osama.transfer_money(nesma,100)
osama.display_user_balance()
nesma.display_user_balance()

