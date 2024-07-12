from datetime import datetime

class Transaction:
    @staticmethod
    def create(db, transaction_type, amount, from_account, to_account):
        """
        Creates a new transaction in the database.

        Parameters:
        db (Database): The database connection object.
        transaction_type (str): The type of transaction (e.g., 'deposit', 'withdrawal', 'transfer').
        amount (float): The amount of the transaction.
        from_account (int): The account number from which the transaction is made.
        to_account (int): The account number to which the transaction is made.

        Returns:
        None
        """
        query = """
        INSERT INTO transactions 
        (transaction_type, amount, timestamp, from_account, to_account) 
        VALUES (%s, %s, %s, %s, %s)
        """
        db.execute_query(query, (transaction_type, amount, datetime.now(), from_account, to_account))

    @staticmethod
    def get_history(db, account_number):
        """
        Retrieves the transaction history for a specific account.

        Parameters:
        db (Database): The database connection object.
        account_number (int): The account number for which to retrieve the transaction history.

        Returns:
        list: A list of dictionaries, where each dictionary represents a transaction.
        """
        query = """
        SELECT * FROM transactions 
        WHERE from_account = %s OR to_account = %s 
        ORDER BY timestamp DESC
        """
        return db.fetch_all(query, (account_number, account_number))