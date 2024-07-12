# Bank System

A comprehensive bank system implemented in Python with MySQL database support. This system allows users to open accounts, manage transactions, and perform various banking operations through an interactive command-line interface.

## Features

- Open a new account
- Check account balance
- Deposit money
- Withdraw money
- Transfer money between accounts
- View transaction history
- Secure database storage of customer and account information


## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` package


### Database Setup

1. Install MySQL Server if you haven't already.
2. Create a new database named `bank`.
3. Update the database connection details in `database_manager.py`:

    ```python
    host='localhost'
    user='your_username'
    password='your_password'
    database='bank'
    ```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hossein-sa/Bank-System-Simulation.git
    cd Bank-System-Simulatio
    ```

### Usage

1. Run the main script to start the banking portal:
    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to interact with the bank system.

### Code Overview

#### main.py

- Provides an interactive menu to interact with the `Bank` class.

### Example Interaction

```text
===== Banking Portal =====
1. Open a new account
2. Check balance
3. Deposit money
4. Withdraw money
5. Transfer money
6. View transaction history
7. Exit
==========================

Enter your choice (1-7): 1
Enter your name: Alice Johnson
Enter your national code: 1234567890
Enter your address: 123 Main St, Anytown, USA
Enter your phone number: 555-1234

Account opened successfully. Your account number is 9876543 and card number is 8844621087654321

Enter your choice (1-7): 3
Enter your card number: 8844621087654321
Enter the amount to deposit: $1000

Deposit successful.

Enter your choice (1-7): 2
Enter your account number: 9876543

Your current balance is: $1000.00

Enter your choice (1-7): 7

Thank you for using our banking portal. Goodbye!
```


## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request



## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- **Author**: Hossein Sadeghi
- **Email**: sadeghi.ho@hotmail.com
- **GitHub**: [hossein-sa](https://github.com/hossein-sa)
