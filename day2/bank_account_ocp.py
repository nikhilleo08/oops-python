from abc import ABC, abstractclassmethod
from typing import List
from enum import Enum

class AccountType(Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"

# TransactionLogger class for logging transactions (SRP)
class TransactionLogger:
    def log_transaction(self, message: str) -> None:
        print(message)

class BankAccount(ABC):
    def __init__(self, account_number: str, account_holder_name: str, account_type: AccountType, initial_balance: float = 0.0, logger: TransactionLogger = None):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_type = account_type
        self._balance = initial_balance
        self._transaction_history: List[str] = []  # Protected variable
        self._logger = logger or TransactionLogger()  # Injected dependency for logging

    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def account_holder_name(self):
        return self._account_holder_name
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def account_type(self):
        return self._account_type

    # Deposit implementation
    def deposit(self, amount: float, ignore_logger: bool = False):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        if not ignore_logger:
            self._transaction_history.append(f"Deposited {amount} USD.")
            self._logger.log_transaction(f"Deposited {amount} USD. New balance: {self._balance} USD.")

    def withdraw(self, amount: float, ignore_logger: bool = False):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self._balance -= amount
        if not ignore_logger:
            self._transaction_history.append(f"Withdrew {amount} USD.")
            self._logger.log_transaction(f"Withdrew {amount} USD. New balance: {self._balance} USD.")

    def transfer(self, amount: float, to_account: 'BankAccount'):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient balance for transfer.")
        self.withdraw(amount, True)
        to_account.deposit(amount, True)
        self._transaction_history.append(f"Transferred {amount} USD to account {to_account.account_number}.")
        to_account._transaction_history.append(f"Received {amount} USD from account {self.account_number}.")
        self._logger.log_transaction(f"Transferred {amount} USD to account {to_account.account_number}. New balance: {self._balance} USD.")

    def get_transaction_history(self) -> List[str]:
        return self._transaction_history


# Specific bank account types (OCP)
class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, account_holder_name: str, initial_balance: float = 0.0, logger: TransactionLogger = None):
        super().__init__(account_number, account_holder_name, AccountType.CHECKING, initial_balance, logger)

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, account_holder_name: str, initial_balance: float = 0.0, logger: TransactionLogger = None):
        super().__init__(account_number, account_holder_name, AccountType.SAVINGS, initial_balance, logger)
    
    def apply_interest(self, interest_rate: float) -> None:
        interest = self.balance * interest_rate
        self.deposit(interest)
        self.get_transaction_history().append(f"Applied interest of {interest} USD.")
        self._TransactionLogger.log_transaction(f"Applied interest of {interest} USD.")


# Creating a logger
logger = TransactionLogger()

# Creating different bank accounts
account1 = CheckingAccount("123456", "John Doe", 500.0, logger)
account2 = SavingsAccount("654321", "Jane Smith", 300.0, logger)

# Performing operations
account1.deposit(200)
account1.withdraw(50)
account1.transfer(100, account2)

# Checking transaction history
print("\nTransaction History for Account 1:")
for transaction in account1.get_transaction_history():
    print(transaction)

print("\nTransaction History for Account 2:")
for transaction in account2.get_transaction_history():
    print(transaction)
