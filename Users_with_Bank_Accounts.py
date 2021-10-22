class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, deposit):
        self.balance += deposit
        return self
    def withdrawal(self, withdrawal):
        self.balance -= withdrawal
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        if self.balance > 0:
            print("Balance: $" + str(self.balance))
        elif self.balance < 0:
            print("Balance: $(" + str(self.balance) + ")")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance*self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    def make_deposit(self, deposit):
        self.account.deposit(deposit)
        return self
    def make_withdrawal(self, withdraw):
        self.account.withdrawal(withdraw)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self

acc1 = User("Player 1", "email@email.com")
acc1.make_deposit(200).make_withdrawal(100).display_user_balance()
