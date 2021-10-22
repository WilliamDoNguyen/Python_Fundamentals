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

acc1 = BankAccount(0.08)
acc2 = BankAccount(0.05, 0)

acc1.deposit(500).deposit(200).deposit(20).withdrawal(300).yield_interest().display_account_info()

acc2.deposit(50).deposit(20).withdrawal(5).withdrawal(10).withdrawal(100).yield_interest().display_account_info()
