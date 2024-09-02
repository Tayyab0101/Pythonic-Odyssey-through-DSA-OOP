class BankAccountDetails:
    def __init__(self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit of {amount} is sucessful. New Balance is {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Cannot make transaction. Max withdrawl amount is {self.balance}")
        else:
            print(f"Withdrawing {amount} Rs. Remaining Balance is {self.balance - amount}")
    
    def __str__(self):
        return f"Acount Holder Name: {self.account_holder_name}\nAvailable Balance: {self.balance} Rupees"
    
    def __call__(self):
        return f"Hi from call method"
              
account1 = BankAccountDetails("Shanza", 54598)
print(account1)
account1.deposit(2500)
account1.withdraw(1600)
print(account1())