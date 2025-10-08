from manager import AccountManager

def menu():
    print("\n🏦 Banking Management System")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

def main():
    manager = AccountManager()
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            acc_no = input("Account No: ")
            name = input("Name: ")
            balance = float(input("Initial Balance: "))
            manager.add_account(acc_no, name, balance)

        elif choice == "2":
            manager.view_accounts()

        elif choice == "3":
            acc_no = input("Account No: ")
            amount = float(input("Amount to Deposit: "))
            manager.deposit(acc_no, amount)

        elif choice == "4":
            acc_no = input("Account No: ")
            amount = float(input("Amount to Withdraw: "))
            manager.withdraw(acc_no, amount)

        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice!")

if __name__ == "__main__":
    main()
