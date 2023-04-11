class Account:
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: int) -> bool:
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: int) -> bool:
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> int:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name