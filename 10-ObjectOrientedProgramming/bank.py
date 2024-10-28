class BankAccount:
    def __init__(self, acc_number):
        self.acc_number=acc_number
        self.balance=0.00
    def display_balance(self):
        print(f"The balance is : {self.balance}")
    def deposit(self, num):
        self.balance+=num
    def withdraw(self, num):
        if num<=self.balance:
            self.balance-=num
        else:
            print("Insufficient funds on the account")
    def show_status(self):
        print(f"Bank Account No: {self.acc_number}\nBalance: {self.balance}")
