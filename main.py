from database_manager import DatabaseManager
from bank import Bank


def print_menu():
    """
    Print the banking portal menu options.
    """
    print("\n===== Banking Portal =====")
    print("1. Open a new account")
    print("2. Check balance")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Transfer money")
    print("6. View transaction history")
    print("7. Exit")
    print("==========================")


def get_valid_input(prompt, valid_options):
    """
    Get a valid input from the user within a specified set of options.

    :param prompt: The prompt message to display to the user.
    :param valid_options: A list of valid options for the user input.
    :return: The user's valid input.
    """
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        print("Invalid input. Please try again.")


def main():
    """
    The main function for the banking portal.
    """
    db_manager = DatabaseManager()
    bank = Bank(db_manager)

    while True:
        print_menu()
        choice = get_valid_input("Enter your choice (1-7): ", [str(i) for i in range(1, 8)])

        if choice == '1':
            name = input("Enter your name: ")
            national_code = input("Enter your national code: ")
            address = input("Enter your address: ")
            phone = input("Enter your phone number: ")
            account_num, card_num = bank.open_account(name, national_code, address, phone)
            if account_num and card_num:
                print(
                    f"Account opened successfully. Your account number is {account_num} and card number is {card_num}")
            else:
                print("Failed to open account. National code may already exist.")

        elif choice == '2':
            account_num = input("Enter your account number: ")
            balance = bank.show_balance(account_num)
            if balance is not None:
                print(f"Your current balance is: ${balance:.2f}")
            else:
                print("Account not found.")

        elif choice == '3':
            card_num = input("Enter your card number: ")
            amount = float(input("Enter the amount to deposit: $"))
            if bank.deposit(card_num, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed. Please check your card number and amount.")

        elif choice == '4':
            card_num = input("Enter your card number: ")
            amount = float(input("Enter the amount to withdraw: $"))
            if bank.withdraw(card_num, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed. Please check your card number and ensure you have sufficient balance.")

        elif choice == '5':
            from_card = input("Enter your card number: ")
            to_card = input("Enter the recipient's card number: ")
            amount = float(input("Enter the amount to transfer: $"))
            if bank.transfer(from_card, to_card, amount):
                print("Transfer successful.")
            else:
                print("Transfer failed. Please check the card numbers and ensure you have sufficient balance.")

        elif choice == '6':
            account_num = input("Enter your account number: ")
            transactions = bank.get_transaction_history(account_num)
            if transactions:
                print("\nTransaction History:")
                for transaction in transactions:
                    print(f"ID: {transaction[0]}, Type: {transaction[1]}, Amount: ${transaction[2]:.2f}, "
                          f"Time: {transaction[3]}, From: {transaction[4] or 'N/A'}, To: {transaction[5] or 'N/A'}")
            else:
                print("No transactions found or invalid account number.")

        elif choice == '7':
            print("Thank you for using our banking portal. Goodbye!")
            db_manager.close()
            break


if __name__ == "__main__":
    main()
