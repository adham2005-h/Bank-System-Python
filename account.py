# Full Name: Adham Muayad Hashem
from datetime import datetime
from math import isfinite


class Account:
    def __init__(self, account_number, name, password, balance=0):
        self.__account_number = account_number
        self.__name = name
        self.__password = password
        self.__balance = balance
        self.__transactions = []

    def get_account_number(self):
        return self.__account_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        name = name.strip()
        if name != "":
            self.__name = name
        else:
            print("Name cannot be empty.")

    def get_password(self):
        return self.__password

    def set_password(self, password):
        if len(password) >= 4 and password.strip():
            self.__password = password
            self.add_transaction("Password changed")
            return True
        else:
            print("Password must contain at least 4 characters and cannot be blank.")
            return False

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if isfinite(amount) and amount > 0:
            self.__balance += amount
            self.add_transaction(f"Deposit: {amount}")
            return True
        else:
            print("Invalid amount. Amount must be greater than zero.")
            return False

    def withdraw(self, amount):
        if isfinite(amount) and 0 < amount <= self.__balance:
            self.__balance -= amount
            self.add_transaction(f"Withdraw: {amount}")
            return True
        else:
            if not isfinite(amount) or amount <= 0:
                print("Invalid amount. Amount must be greater than zero.")
            else:
                print("Insufficient balance.")
            return False

    def send_transfer(self, amount, receiver_account_number):
        if isfinite(amount) and 0 < amount <= self.__balance:
            self.__balance -= amount
            self.add_transaction(
                f"Transfer to {receiver_account_number}: {amount}"
            )
            return True
        else:
            if not isfinite(amount) or amount <= 0:
                print("Invalid amount. Amount must be greater than zero.")
            else:
                print("Insufficient balance.")
            return False

    def receive_transfer(self, amount, sender_account_number):
        if isfinite(amount) and amount > 0:
            self.__balance += amount
            self.add_transaction(
                f"Received from {sender_account_number}: {amount}"
            )
            return True
        else:
            print("Invalid amount. Amount must be greater than zero.")
            return False

    def add_transaction(self, text):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transactions.append(f"{date} - {text}")

    def show_info(self):
        print("\nAccount Number:", self.__account_number)
        print("Name:", self.__name)
        print("Balance:", self.__balance)

    def show_transactions(self):
        if len(self.__transactions) == 0:
            print("No transactions yet.")
        else:
            print("\n----- Transactions -----")
            for transaction in self.__transactions:
                print(transaction)