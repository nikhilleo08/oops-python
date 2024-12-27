from typing import List

class BankAccount:
    def __init__(self, account_number: str, account_holder_name: str, account_type: str, initial_balance: float = 0.0):
        self.__account_number = account_number  # Private variable
        self.__account_holder_name = account_holder_name  # Private variable
        self.__account_type = account_type  # Private variable
        self.__balance = initial_balance  # Private variable
        self.__transaction_history: List[str] = []  # Private variable

    # Getter for account number
    @property
    def account_number(self) -> str:
        return self.__account_number

    # Getter for account holder name
    @property
    def account_holder_name(self) -> str:
        return self.__account_holder_name

    # Getter for balance (to view, but should not modify directly)
    @property
    def balance(self) -> float:
        return self.__balance

    # Getter for account type
    @property
    def account_type(self) -> str:
        return self.__account_type

    # Method to deposit an amount (ensures proper validation)
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.__balance += amount
        self.__transaction_history.append(f"Deposited {amount} USD.")
        print(f"Deposited {amount} USD in account number {self.account_number}, New balance: {self.__balance} USD.")
    
    # Method to withdraw an amount (ensures proper validation)
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self.__balance:
            raise ValueError("Insufficient balance for withdrawal.")
        
        self.__balance -= amount
        self.__transaction_history.append(f"Withdrew {amount} USD.")
        print(f"Withdrew {amount} USD from account number {self.account_number}, New balance: {self.__balance} USD.")

    # Method to transfer an amount to another account (ensures proper validation)
    def transfer(self, amount: float, to_account: 'BankAccount') -> None:
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        
        if amount > self.__balance:
            raise ValueError("Insufficient balance for transfer.")
        
        self.__balance -= amount
        to_account.__balance += amount  # Directly modifying the private variable of the other account (accessed within class)
        self.__transaction_history.append(f"Transferred {amount} USD to account {to_account.account_number}.")
        to_account.__transaction_history.append(f"Received {amount} USD from account {self.account_number}.")
        print(f"Transferred {amount} USD to account to account number {to_account.account_number} from account {self.account_number}. New balance: {self.__balance} USD.")

    # Getter for transaction history (only accessible via this method)
    def get_transaction_history(self) -> List[str]:
        return self.__transaction_history

    def get_account_details(self) -> None:
        print(f"""
Account Number: {self.account_number}
Account Holder Name: {self.account_holder_name}
Account Type: {self.account_type}
Balance: {self.balance}
""")
# Example usage:

# Creating bank accounts
account1 = BankAccount("123456", "John Doe", "Checking", 500.0)
account2 = BankAccount("654321", "Jane Smith", "Savings", 300.0)
account1.get_account_details()
account2.get_account_details()
# Performing operations
account1.deposit(2000)
account1.withdraw(500)
account1.transfer(1000, account2)
account1.get_account_details()
account2.get_account_details()

# Checking transaction history
print("\nTransaction History for Account 1:")
for transaction in account1.get_transaction_history():
    print(transaction)

print("\nTransaction History for Account 2:")
for transaction in account2.get_transaction_history():
    print(transaction)
