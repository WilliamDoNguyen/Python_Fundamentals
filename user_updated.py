class User:
    def __init__(self, name, email, amount):
        self.name = name
        self.email = email
        self.amount = amount
    def make_deposit(self, deposit):
        self.amount += deposit
        return self
    def make_withdrawal(self, withdrawal):
        self.amount -= withdrawal
        return self
    def display_user_balance(self):
        print("User: " + self.name + "Balance: $" + str(self.amount))
        return self

player_one = User("Player 1, ", "name1@email.com", 0)
player_two = User("Player 2, ", "name1@email.com", 100)
player_three = User("Player 3, ", "name1@email.com", 1000)
player_one.display_user_balance()
player_two.display_user_balance()
player_three.display_user_balance()

player_one.make_deposit(200).make_deposit(20).make_deposit(5).make_withdrawal(100).display_user_balance()

player_two.make_deposit(75).make_deposit(300).make_withdrawal(100).make_withdrawal(50).display_user_balance()

player_three.make_deposit(25).make_withdrawal(300).make_withdrawal(50).make_withdrawal(300).display_user_balance()
