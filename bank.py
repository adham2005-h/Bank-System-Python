# Full Name: Adham Muayad Hashem
from customer import Customer
from math import isfinite


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, password, balance):
        account_number = account_number.strip()
        name = name.strip()

        if not account_number.isdigit():
            print("Account number must contain digits only.")
            return False
        if not name:
            print("Name cannot be empty.")
            return False
        if len(password) < 4 or not password.strip():
            print("Password must contain at least 4 characters and cannot be blank.")
            return False
        if not isfinite(balance):
            print("Initial balance must be a finite number.")
            return False

        if account_number in self.accounts:
            print("Account already exists.")
            return False

        elif balance < 0:
            print("Initial balance cannot be negative.")
            return False

        else:
            self.accounts[account_number] = Customer(
                account_number,
                name,
                password,
                balance
            )

            self.accounts[account_number].add_transaction(
                f"Account created with balance: {balance}"
            )

            print("Account created successfully.")
            return True

    def login_customer(self, account_number, password):
        account_number = account_number.strip()
        if account_number in self.accounts:
            account = self.accounts[account_number]

            if account.get_password() == password:
                print("Login successful.")
                return account
            else:
                print("Wrong password.")
                return None

        else:
            print("Account not found.")
            return None

    def find_account(self, account_number):
        return self.accounts.get(account_number.strip())

    def delete_account(self, account_number):
        account_number = account_number.strip()
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
            return True
        else:
            print("Account not found.")
            return False

    def show_all_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts available.")
        else:
            print("\n===== All Accounts =====")
            for account in self.accounts.values():
                account.show_info()

    def total_bank_money(self):
        total = 0

        for account in self.accounts.values():
            total += account.get_balance()

        return total