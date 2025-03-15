from random import randint, choice

class BankAccount:
    def __init__(self, account_holder, balance, available_account_number, account_number):
        self.account_holder = account_holder
        self.balance = 0
        self.available_account_numbers = [x for x in range(1000, 9999)]
        self.account_number = choice(available_account_number)
    def deposit_money(self):
        new_balance = int(input("Enter the amount you want to deposit € "))
        self.balance = new_balance

    def withdraw(self):
        amount = int(input(f"Enter amount to withdraw (you have {self.balance}): "))
        if amount <= self.balance:
            self.balance -= amount
        elif amount > self.balance:
            print(f"Your balance is not enough ")
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f" Account Number :{self.account_number} | Account Holder : {self.account_holder} | Balance : {self.balance}"
    

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_holder):
        account = BankAccount(account_holder)
        self.accounts.append(account)
        print(f"Account created, Account Holder : {account_holder} Account Number : {account.account_number}")
        return account
    
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number  == account_number:
                return account
        print("Account not found !")
        return None
    
def main():
    bank = Bank()

    while True:
        print("1.Create Account")
        print("2.Deposit Money")
        print("3.Withdraw money")
        print("4.Check Balance")
        print("5.View Account Details")
        print("6.SAve & Exit")
        choice = int(input("Enter choice (1-6) :"))
        match choice:
            case 1:
                name = input("Enter account name : ")
                bank.create_account(name)
            case 2:
                account_number = int(input("Enter account number : "))
                account = bank.find_account(account_number)
                if account:
                    amount = float(input("Enter deposit amount : "))
                    account.deposit(amount)

            case 3:      
                account_number = int(input("Enter your account number: "))
                account = bank.find_account(account_number)
                if account:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)

            case 4:
                account_number = int(input("Enter your account number: "))
                account = bank.find_account(account_number)
                if account:
                    print(f"Your balance: {account.get_balance()}")

            case 5:
                account_number = int(input("Enter your account number: "))
                account = bank.find_account(account_number)
                if account:
                    account.display_details()

            case 6:
                print("Thank you for using the bank system. Goodbye!")
                break

            case _:
                print('Invalid choice !')
main()