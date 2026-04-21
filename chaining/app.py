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
        return self

    def transfer_money(self,other_user,amount):
        self.make_withdrow(amount)
        other_user.make_deposit(amount)
        return self

osama = User('osama')
omar = User('omar')
nesma = User('nesma')

osama.make_deposit(50).make_deposit(100).make_deposit(150).make_withdrow(130).display_user_balance()
omar.make_deposit(100).make_deposit(200).make_withdrow(50).make_withdrow(70).display_user_balance()
nesma.make_deposit(500).make_withdrow(30).make_withdrow(100).make_withdrow(140).display_user_balance()
print("#######################")
osama.transfer_money(nesma,100).display_user_balance()
nesma.display_user_balance()

