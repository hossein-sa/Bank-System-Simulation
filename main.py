import bank_system as bank


def print_menu():
    print("\nBank System Menu")
    print("1. Open an account")
    print("2. Show balance")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Transfer money")
    print("6. Show card number")
    print("7. Exit")


def main():
    bank_instance = bank.Bank()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter customer name: ")
            account_num = bank_instance.open_account(name)
            print(f"Account opened. Account number: {account_num}")

        elif choice == '2':
            account_num = input("Enter account number: ")
            balance = bank_instance.show_balance(account_num)
            if balance is not None:
                print(f"Account balance: {balance}")
            else:
                print("Account not found.")

        elif choice == '3':
            card_num = input("Enter card number: ")
            amount = float(input("Enter amount to deposit: "))
            if bank_instance.deposit(card_num, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed.")

        elif choice == '4':
            card_num = input("Enter card number: ")
            amount = float(input("Enter amount to withdraw: "))
            if bank_instance.withdraw(card_num, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed.")

        elif choice == '5':
            from_card = input("Enter from card number: ")
            to_card = input("Enter to card number: ")
            amount = float(input("Enter amount to transfer: "))
            if bank_instance.transfer(from_card, to_card, amount):
                print("Transfer successful.")
            else:
                print("Transfer failed.")

        elif choice == '6':
            account_num = input("Enter account number: ")
            card_num = bank_instance.show_card_number(account_num)
            if card_num:
                print(f"Card number: {card_num}")
            else:
                print("Account not found.")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
