class Bank:
    def __init__(self, account_number, bal):
        self.__account_number = account_number
        self.__bal = bal

    @property
    def account_number(self):
        return f"account number:{self.__account_number}"
    
    @property
    def balance(self):                         #methods to acceess private variables
        return f"account balance:{self.__bal}"

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.__bal += amount
            print(f"account successfully credited with {amount} and balance is:{self.__bal}")
        else:
            print("invalid amount")
    
    def withdraw(self, amount):
        if amount <= self.__bal:
            self.__bal -= amount
            print(f"account debited with {amount} and balance is:{self.__bal}")
        else:
            print("insufficient bal")

    def __str__(self):
        return f"account number:{self.__account_number}, account balance:{self.__bal}"
if __name__=="__main__":
    bank = Bank(20120, 0) 
    print(bank.__str__())
    # bank.__bal = 2000  # This won't work - creates new public attribute instead
    # To set balance, use deposit method
    bank.deposit(500000)
    bank.withdraw(100000)
    print(bank.balance)
    print(bank.account_number)
