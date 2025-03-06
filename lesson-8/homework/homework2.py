import json
import os

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount}. New balance: {self.balance}"
        return "Invalid or insufficient funds for withdrawal."

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(1000 + len(self.accounts) + 1)  # Unique account number
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created successfully! Your Account Number: {account_number}"  # Clearly display account number

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance}"
        return "Account not found. Please check the account number and try again."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.deposit(amount)
            self.save_to_file()
            return result
        return "Account not found. Please check the account number and try again."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found. Please check the account number and try again."

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump({acc_num: vars(acc) for acc_num, acc in self.accounts.items()}, f)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                    self.accounts = {acc_num: Account(**acc_data) for acc_num, acc_data in data.items()}
                except json.JSONDecodeError:
                    self.accounts = {}

# Command-line interface
def main():
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. View Account\n3. Deposit\n4. Withdraw\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            print(bank.create_account(name, initial_deposit))
        elif choice == "2":
            acc_num = input("Enter your account number: ")
            print(bank.view_account(acc_num))
        elif choice == "3":
            acc_num = input("Enter your account number: ")
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit(acc_num, amount))
        elif choice == "4":
            acc_num = input("Enter your account number: ")
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw(acc_num, amount))
        elif choice == "5":
            print("Exiting... Thank you for using our bank application!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
