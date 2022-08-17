class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return (f"Account owner: {self.owner}\nAccount balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"You have added ${amount} to your account")

    def withdraw(self, amount):

        if amount > self.balance :
            print("Sorry, Funds unavailable")
        else:
            self.balance -= amount
            print(f"You have withdraw ${amount} from your account")

acct1 = Account('Miłosz',0)
print(acct1)
x = acct1.owner
y = acct1.balance
print(x)
print(y)
acct1.deposit(100)
y = acct1.balance
print(y)
acct1.withdraw(50)
y = acct1.balance
print(y)