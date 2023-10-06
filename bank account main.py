
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount} into {self.__account_holder_name}'s account.")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount} from {self.__account_holder_name}'s account.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    account = BankAccount("12345", "John Doe", 1000)
    account.display_balance()

    account.deposit(500)
    account.display_balance()

    account.withdraw(200)
    account.display_balance()

    account.withdraw(1500)

