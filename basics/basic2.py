class BankAccount:
    """
    Class to simulate Bank Account

    Attributes:
        balance: to hold balance amount in the account
    """

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        return self.balance

ac2001 = BankAccount()
ac2001.deposit(11000)
print("Now the balance in the account is :{}".format(ac2001.balance))
ac2001.withdraw(5000)
print("Now the balance in the account is :{}".format(ac2001.balance))
