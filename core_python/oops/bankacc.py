class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

#example usage 
if __name__=="__main__":
    # create an account
    ay_account = BankAccount(account_number="123456789", account_holder="Fred Bloggs", balance=1000.0)
    print("Account Number:", ay_account.account_number)
    print("Account Holder:", ay_account.account_holder)
    print("Balance:", ay_account.balance)