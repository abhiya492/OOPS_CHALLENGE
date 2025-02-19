class BankAccount:
    def __init__(self, holder_name, initial_balance=0):
        self.holder_name = holder_name
        self.__balance = initial_balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False
    
    def __sub__(self, other):
        if isinstance(other, BankAccount):
            transfer_amount = self.__balance
            self.transfer(other, transfer_amount)
        return self
    
    def __str__(self):
        return f"{self.holder_name} - Balance: {self.__balance}"



acc1 = BankAccount("Alice", 10000)
acc2 = BankAccount("Bob", 5000)
acc1.withdraw(2000)
print(acc1)  # Alice - Balance: 8000
acc1 - acc2
print(acc1)  # Alice - Balance: 0
print(acc2)  # Bob - Balance: 13000