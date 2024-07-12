import mysql.connector
from mysql.connector import Error


class DatabaseManager:
    def __init__(self, host='localhost', user='root', password='toor', database='bank'):
        """
                Initialize the DatabaseManager with connection parameters and create tables if they do not exist.
        """
        try:
            # Establish a connection to the MySQL server
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
            self.create_tables()
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def create_tables(self):
        """
        create necessary tables for the banking database
        """
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                national_code VARCHAR(10) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                address VARCHAR(255),
                phone VARCHAR(20)
            );''')

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number VARCHAR(20) PRIMARY KEY,
                national_code VARCHAR(10) NOT NULL,
                card_number VARCHAR(20) UNIQUE,
                balance DECIMAL(10, 2) DEFAULT 0,
                FOREIGN KEY (national_code) REFERENCES customers(national_code)
                );''')

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                account_number VARCHAR(20) NOT NULL,
                transaction_type VARCHAR(20) NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                details VARCHAR(255),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_number) REFERENCES accounts(account_number)
                );''')

            self.connection.commit()
        except Error as e:
            print(f"Error creating tables: {e}")

    def execute_query(self, query, params=None):
        """
                Execute a single query with optional parameters.
                :param query: SQL query to be executed
                :param params: Optional parameters to be included in the query
                :return: True if successful, None otherwise
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_one(self, query, params=None):
        """
                Execute a single query and fetch the first row.
                :param query: SQL query to be executed
                :param params: Optional parameters to be included in the query
                :return: The first row of the result set, or None if no rows are returned
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchone()
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    def fetch_all(self, query, params=None):
        """
                Fetch all results from a query with optional parameters.
                :param query: SQL query to be executed
                :param params: Optional parameters to be included in the query
                :return: List of fetched results or None in case of an error
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    def close(self):
        """
                Close the database connection.
        """
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")

    def insert_customer(self, national_code, name, address=None, phone=None):
        """
                Insert a new customer into the customers table.
                :param national_code: Unique national code of the customer
                :param name: Name of the customer
                :param address: Address of the customer
                :param phone: Phone number of the customer
                :return: True if successful, None otherwise
        """
        query = "INSERT INTO customers (national_code, name, address, phone) VALUES (%s, %s, %s, %s)"
        params = (national_code, name, address, phone)
        return self.execute_query(query, params)

    def insert_account(self, account_number, national_code, card_number, balance=0.0):
        """
                Insert a new account into the accounts table.
                :param account_number: Unique account number
                :param national_code: National code of the customer associated with the account
                :param card_number: Unique card number for the account
                :param balance: Initial balance of the account
                :return: True if successful, None otherwise
        """
        query = "INSERT INTO accounts (account_number, national_code, card_number, balance) VALUES (%s, %s, %s, %s)"
        params = (account_number, national_code, card_number, balance)
        return self.execute_query(query, params)

    def insert_transaction(self, account_number, transaction_type, amount, details):
        """
                Insert a new transaction into the transactions table.
                :param account_number: Account number of the transaction
                :param transaction_type: Type of the transaction (e.g., deposit, withdrawal)
                :param amount: Amount involved in the transaction
                :param details: Additional details about the transaction
                :return: True if successful, None otherwise
        """
        query = "INSERT INTO transactions (account_number, transaction_type, amount, details) VALUES (%s, %s, %s, %s)"
        params = (account_number, transaction_type, amount, details)
        return self.execute_query(query, params)
