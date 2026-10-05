# Full Name: Adham Muayad Hashem
from account import Account


class Customer(Account):
    def __init__(self, account_number, name, password, balance=0):
        super().__init__(account_number, name, password, balance)

    def transfer(self, other_account, amount):
        if self.get_account_number() == other_account.get_account_number():
            print("Cannot transfer to the same account.")
            return False
        if self.send_transfer(amount, other_account.get_account_number()):
            other_account.receive_transfer(amount, self.get_account_number())
            return True
        else:
            return False

    def show_info(self):
        print("\n----- Customer Information -----")
        super().show_info()