import mysql.connector
from mysql.connector import Error


class DatabaseManager:
    """
    A class to manage a MySQL database connection and perform various operations.

    Attributes
    ----------
    conn : mysql.connector.Connection
        The MySQL database connection.
    cursor : mysql.connector.Cursor
        The cursor object for executing SQL queries.

    Methods
    -------
    __init__(host='localhost', user='root', password='toor', database='bank_db')
        Initializes the database connection and creates the necessary tables.

    create_tables()
        Creates the customers, accounts, and transactions tables in the database.

    execute_query(query, params=None)
        Executes a SQL query with optional parameters and commits the changes.
        Returns True if the query is successful, False otherwise.

    fetch_one(query, params=None)
        Executes a SQL query with optional parameters and fetches the first result.
        Returns the fetched result or None if no result is found.

    fetch_all(query, params=None)
        Executes a SQL query with optional parameters and fetches all results.
        Returns a list of fetched results or None if no result is found.

    close()
        Closes the database connection and cursor.
    """

    def __init__(self, host='localhost', user='root', password='toor', database='bank_db'):
        try:
            self.conn = mysql.connector.connect(
                host=host, user=user, password=password, database=database
            )
            self.cursor = self.conn.cursor()
            self.create_tables()
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def create_tables(self):
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                national_code VARCHAR(20) PRIMARY KEY,
                name VARCHAR(100),
                address VARCHAR(255),
                phone VARCHAR(20)
            )''')

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number VARCHAR(20) PRIMARY KEY,
                national_code VARCHAR(20),
                card_number VARCHAR(20),
                balance DECIMAL(10, 2),
                FOREIGN KEY (national_code) REFERENCES customers (national_code)
            )''')

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                transaction_type VARCHAR(20),
                amount DECIMAL(10, 2),
                timestamp DATETIME,
                from_account VARCHAR(20),
                to_account VARCHAR(20),
                FOREIGN KEY (from_account) REFERENCES accounts (account_number),
                FOREIGN KEY (to_account) REFERENCES accounts (account_number)
            )''')

            self.conn.commit()
        except Error as e:
            print(f"Error creating tables: {e}")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except Error as e:
            print(f"Error executing query: {e}")
            return False

    def fetch_one(self, query, params=None):
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
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()