import random


class Branch:
    def __init__(self, branch_code, city, grade):
        self.branch_code = branch_code
        self.city = city
        self.grade = grade


class CreditCard:
    def __init__(self):
        self.card_number = "88446210" + ''.join([str(random.randint(0, 9)) for _ in range(8)])
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


class Account:
    def __init__(self):
        self.account_number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        self.credit_card = CreditCard()


class Customer:
    def __init__(self, name):
        self.name = name
        self.account = None


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def open_account(self, customer_name):
        customer = Customer(customer_name)
        customer.account = Account()
        self.customers[customer_name] = customer
        self.accounts[customer.account.account_number] = customer.account
        return customer.account.account_number

    def show_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].credit_card.balance
        return None

    def transfer(self, from_card, to_card, amount):
        from_account = next((acc for acc in self.accounts.values() if acc.credit_card.card_number == from_card), None)
        to_account = next((acc for acc in self.accounts.values() if acc.credit_card.card_number == to_card), None)

        if from_account and to_account and from_account.credit_card.withdraw(amount):
            to_account.credit_card.deposit(amount)
            return True
        return False

    def deposit(self, card_number, amount):
        account = next((acc for acc in self.accounts.values() if acc.credit_card.card_number == card_number), None)
        if account:
            return account.credit_card.deposit(amount)
        return False

    def withdraw(self, card_number, amount):
        account = next((acc for acc in self.accounts.values() if acc.credit_card.card_number == card_number), None)
        if account:
            return account.credit_card.withdraw(amount)
        return False

    def show_card_number(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].credit_card.card_number
        return None
