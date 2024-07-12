import random
from transaction import Transaction


class Bank:
    def __init__(self, db_manager):
        """
        Initialize a Bank instance with a database manager.

        :param db_manager: An instance of a database manager class.
        """
        self.db = db_manager

    def open_account(self, name, national_code, address, phone):
        """
        Open a new bank account for a customer.

        :param name: The customer's name.
        :param national_code: The customer's national code.
        :param address: The customer's address.
        :param phone: The customer's phone number.

        :return: A tuple containing the account number and card number of the new account.
                 If the account could not be opened, return (None, None).
        """
        # Generate a random account number and card number
        account_number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        card_number = "88446210" + ''.join([str(random.randint(0, 9)) for _ in range(8)])

        # Prepare SQL queries for inserting customer and account data
        customer_query = "INSERT INTO customers (national_code, name, address, phone) VALUES (%s, %s, %s, %s)"
        account_query = "INSERT INTO accounts (account_number, national_code, card_number, balance) VALUES (%s, %s, %s, %s)"

        # Execute the SQL queries and check if both were successful
        if self.db.execute_query(customer_query, (national_code, name, address, phone)) and \
                self.db.execute_query(account_query, (account_number, national_code, card_number, 0.0)):
            return account_number, card_number
        return None, None

    def show_balance(self, account_number):
        """
        Get the current balance of a bank account.

        :param account_number: The account number.

        :return: The current balance of the account. If the account does not exist, return None.
        """
        # Prepare SQL query for fetching account balance
        query = "SELECT balance FROM accounts WHERE account_number = %s"

        # Execute the SQL query and return the balance
        result = self.db.fetch_one(query, (account_number,))
        return result[0] if result else None

    def transfer(self, from_card, to_card, amount):
        """
        Transfer funds from one account to another.

        :param from_card: The card number of the account to transfer from.
        :param to_card: The card number of the account to transfer to.
        :param amount: The amount to transfer.

        :return: True if the transfer is successful, False otherwise.
        """
        # Prepare SQL queries for fetching account data
        from_query = "SELECT account_number, balance FROM accounts WHERE card_number = %s"
        to_query = "SELECT account_number FROM accounts WHERE card_number = %s"

        # Execute the SQL queries and fetch the account data
        from_account = self.db.fetch_one(from_query, (from_card,))
        to_account = self.db.fetch_one(to_query, (to_card,))

        # Check if both accounts exist and if the from_account has sufficient balance
        if from_account and to_account and from_account[1] >= amount:
            # Prepare SQL queries for updating account balances
            update_from = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
            update_to = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"

            # Execute the SQL queries and check if both were successful
            if self.db.execute_query(update_from, (amount, from_account[0])) and \
                    self.db.execute_query(update_to, (amount, to_account[0])):
                # Create a new transaction record
                Transaction.create(self.db, "Transfer", amount, from_account[0], to_account[0])
                return True
        return False

    def deposit(self, card_number, amount):
        """
        Deposit funds into a bank account.

        :param card_number: The card number of the account to deposit into.
        :param amount: The amount to deposit.

        :return: True if the deposit is successful, False otherwise.
        """
        # Check if the deposit amount is positive
        if amount > 0:
            # Prepare SQL query for fetching account data
            query = "SELECT account_number FROM accounts WHERE card_number = %s"

            # Execute the SQL query and fetch the account data
            account = self.db.fetch_one(query, (card_number,))

            # Check if the account exists
            if account:
                # Prepare SQL query for updating account balance
                update_query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"

                # Execute the SQL query and check if it was successful
                if self.db.execute_query(update_query, (amount, account[0])):
                    # Create a new transaction record
                    Transaction.create(self.db, "Deposit", amount, None, account[0])
                    return True
        return False

    def withdraw(self, card_number, amount):
        """
        Withdraw funds from a bank account.

        :param card_number: The card number of the account to withdraw from.
        :param amount: The amount to withdraw.

        :return: True if the withdrawal is successful, False otherwise.
        """
        # Prepare SQL query for fetching account data
        query = "SELECT account_number, balance FROM accounts WHERE card_number = %s"

        # Execute the SQL query and fetch the account data
        account = self.db.fetch_one(query, (card_number,))

        # Check if the account exists and if it has sufficient balance
        if account and 0 < amount <= account[1]:
            # Prepare SQL query for updating account balance
            update_query = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"

            # Execute the SQL query and check if it was successful
            if self.db.execute_query(update_query, (amount, account[0])):
                # Create a new transaction record
                Transaction.create(self.db, "Withdrawal", amount, account[0], None)
                return True
        return False

    def get_transaction_history(self, account_number):
        """
        Get the transaction history of a bank account.

        :param account_number: The account number.

        :return: A list of transactions for the account.
        """
        # Call the get_history method of the Transaction class to fetch the transaction history
        return Transaction.get_history(self.db, account_number)