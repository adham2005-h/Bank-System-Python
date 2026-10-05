# Full Name: Adham Muayad Hashem
from bank import Bank
from admin import Admin
from getpass import getpass
from math import isfinite


def read_positive_float(message):
    try:
        value = float(input(message))

        if not isfinite(value) or value <= 0:
            print("Amount must be a finite number greater than zero.")
            return None
        else:
            return value

    except ValueError:
        print("Invalid number.")
        return None


def read_valid_password(message):
    while True:
        password = getpass(message)

        if len(password) >= 4 and password.strip():
            return password
        else:
            print("Password must contain at least 4 characters and cannot be blank.")


def customer_menu(bank, customer):
    while True:
        print("\n===== Customer Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Show Balance")
        print("5. Show Transactions")
        print("6. Change Password")
        print("7. Logout")

        choice = input("Choose: ")

        if choice == "1":
            amount = read_positive_float("Enter deposit amount: ")

            if amount is not None:
                if customer.deposit(amount):
                    print("Deposit completed successfully.")

        elif choice == "2":
            amount = read_positive_float("Enter withdraw amount: ")

            if amount is not None:
                if customer.withdraw(amount):
                    print("Withdraw completed successfully.")

        elif choice == "3":
            receiver_number = input("Enter receiver account number: ").strip()
            receiver = bank.find_account(receiver_number)

            if receiver is None:
                print("Receiver account not found.")
            else:
                amount = read_positive_float("Enter transfer amount: ")

                if amount is not None:
                    if customer.transfer(receiver, amount):
                        print("Transfer completed successfully.")

        elif choice == "4":
            print("Your balance is:", customer.get_balance())

        elif choice == "5":
            customer.show_transactions()

        elif choice == "6":
            old_password = getpass("Enter old password: ")

            if old_password == customer.get_password():
                new_password = read_valid_password("Enter new password: ")

                if customer.set_password(new_password):
                    print("Password changed successfully.")
            else:
                print("Wrong old password.")

        elif choice == "7":
            print("Logged out.")
            break

        else:
            print("Invalid choice.")


def admin_menu(bank):
    admin = Admin()

    username = input("Admin username: ")
    password = getpass("Admin password: ")

    if admin.login(username, password):
        while True:
            print("\n===== Admin Menu =====")
            print("1. Show All Accounts")
            print("2. Search Account")
            print("3. Delete Account")
            print("4. Show Total Bank Money")
            print("5. Logout")

            choice = input("Choose: ")

            if choice == "1":
                bank.show_all_accounts()

            elif choice == "2":
                account_number = input("Enter account number: ").strip()
                account = bank.find_account(account_number)

                if account is None:
                    print("Account not found.")
                else:
                    account.show_info()
                    account.show_transactions()

            elif choice == "3":
                account_number = input("Enter account number: ").strip()
                bank.delete_account(account_number)

            elif choice == "4":
                print("Total money in bank:", bank.total_bank_money())

            elif choice == "5":
                print("Admin logged out.")
                break

            else:
                print("Invalid choice.")


def main():
    bank = Bank()

    while True:
        print("\n========== BANK SYSTEM ==========")
        print("1. Create Customer Account")
        print("2. Customer Login")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            account_number = input("Enter account number: ").strip()

            if not account_number.isdigit():
                print("Account number must contain digits only.")
                continue

            name = input("Enter customer name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            password = read_valid_password("Enter password: ")

            try:
                balance = float(input("Enter initial balance: "))
            except ValueError:
                print("Invalid balance.")
                continue

            bank.create_account(account_number, name, password, balance)

        elif choice == "2":
            account_number = input("Enter account number: ").strip()
            password = getpass("Enter password: ")

            customer = bank.login_customer(account_number, password)

            if customer is not None:
                customer_menu(bank, customer)

        elif choice == "3":
            admin_menu(bank)

        elif choice == "4":
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()