# Bank System

A simple bank system implemented in Python that allows users to open accounts, deposit and withdraw money, transfer funds, and check balances. This project includes an interactive menu for easy user interaction.

## Features

- Open an account
- Show balance
- Deposit money
- Withdraw money
- Transfer money
- Show card number

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/bank_system.git
    cd bank_system
    ```

2. No additional libraries are required.

### Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to interact with the bank system.

### Code Overview

#### bank_system.py

- **Branch**: Represents a bank branch with a code, city, and grade.
- **CreditCard**: Represents a credit card with a card number and balance. Supports deposit and withdraw methods.
- **Account**: Represents a bank account with an account number and an associated credit card.
- **Customer**: Represents a customer with a name and an associated account.
- **Bank**: Manages customers and accounts. Supports opening accounts, showing balances, transferring funds, depositing money, withdrawing money, and showing card numbers.

#### main.py

- Provides an interactive menu to interact with the `Bank` class.

### Example Interaction

```text
Bank System Menu
1. Open an account
2. Show balance
3. Deposit money
4. Withdraw money
5. Transfer money
6. Show card number
7. Exit

Enter your choice: 1
Enter customer name: Alice
Account opened. Account number: 1234567

Enter your choice: 2
Enter account number: 1234567
Account balance: 0.0

Enter your choice: 3
Enter card number: 8844621001234567
Enter amount to deposit: 1000
Deposit successful.

Enter your choice: 2
Enter account number: 1234567
Account balance: 1000.0
```


### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request



### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact

- **Author**: Hossein Sadeghi
- **Email**: sadeghi.ho@hotmail.com
- **GitHub**: [hossein-sa](https://github.com/hossein-sa)
