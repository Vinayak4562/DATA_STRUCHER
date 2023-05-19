'''Encapsulation is the procces of hiding the implementation details of an object from the outside world. 
It is achieved in Python by making the attributes and methods of a class private using underscores'''

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account balance: {self._balance}")

account = BankAccount("12345678912", 9000)
account.deposit(5000)
account.withdraw(20000)
account.display_balance()
