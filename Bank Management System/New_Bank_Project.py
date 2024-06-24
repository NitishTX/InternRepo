class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance=${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance=${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.getBalance()

    def variableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.variableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer..🚀') 
            self.variableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete!✅\n\n*********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit Complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.variableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')


def main():
    # Example usage in main function with user input
    initial_amount = float(input("Enter initial amount for savings account: "))
    acct_name = input("Enter account name: ")
    savings_acct = SavingsAcct(initial_amount, acct_name)

    while True:
        print("\nOperations Available:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            savings_acct.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            savings_acct.withdraw(amount)
        elif choice == '3':
            amount = float(input("Enter amount to transfer: "))
            target_acct_name = input("Enter target account name: ")
            # For simplicity, assuming target account is the same as savings account
            target_acct = savings_acct
            savings_acct.transfer(amount, target_acct)
        elif choice == '4':
            savings_acct.getBalance()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
