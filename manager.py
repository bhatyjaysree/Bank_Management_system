from account import Account
from database import load_data, save_data

class AccountManager:
    def __init__(self):
        self.accounts = [Account(**a) for a in load_data()]

    def add_account(self, account_no, name, balance=0):
        self.accounts.append(Account(account_no, name, balance))
        self._save()
        print("✅ Account created successfully!")

    def view_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return
        # Print in table format
        print(f"+-----------+----------------+---------+")
        print(f"| AccountNo | Name           | Balance |")
        print(f"+-----------+----------------+---------+")
        for a in self.accounts:
            print(f"| {a.account_no:<9} | {a.name:<14} | {a.balance:<7} |")
        print(f"+-----------+----------------+---------+")

    def search_account(self, account_no):
        for a in self.accounts:
            if a.account_no == account_no:
                return a
        return None

    def deposit(self, account_no, amount):
        acc = self.search_account(account_no)
        if acc and acc.deposit(amount):
            self._save()
            print(f"✅ Deposited {amount} successfully.")
        else:
            print("⚠️ Deposit failed.")

    def withdraw(self, account_no, amount):
        acc = self.search_account(account_no)
        if acc and acc.withdraw(amount):
            self._save()
            print(f"✅ Withdrawn {amount} successfully.")
        else:
            print("⚠️ Withdrawal failed.")

    def _save(self):
        save_data([a.__dict__ for a in self.accounts])
