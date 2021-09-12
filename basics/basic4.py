class Account:
    num_of_accounts = 0
    def __init__(self):
        self.balance = 1000
        Account.num_of_accounts += 1

    @staticmethod
    def account_info():
        print("{} accounts have been created".format(Account.num_of_accounts))

Account.account_info()
ac2001 = Account()
Account.account_info()
