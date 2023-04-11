class Account:
    """
    Class representing name and balance for Account
    """
    def __init__(self, name: str) -> None:
        """
        Sets the variables when Account is created
        :param name: Account's name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: int) -> bool:
        """
        Will increase Account's balance if amount is greater than 0
        :param amount: amount changed
        :return: if transaction worked
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: int) -> bool:
        """
        Will decrease Account's balance if amount is greater than 0
        :param amount: amount changed
        :return: if transaction worked
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> int:
        """
        :return: Account's balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        :return: Account's name
        """
        return self.__account_name