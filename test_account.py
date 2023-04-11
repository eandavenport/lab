import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account("John")
        self.a2 = Account("Jake")

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == "John"
        assert self.a2.get_name() == "Jake"
        assert self.a1.get_balance() == 0
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(50) is True
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 50
        assert self.a2.deposit(25) is True
        assert self.a2.deposit(-5) is False
        assert self.a2.get_balance() == 25

    def test_withdraw(self):
        self.a1.deposit(100)
        self.a2.deposit(100)
        assert self.a1.withdraw(20) is True
        assert self.a1.withdraw(-5) is False
        assert self.a1.get_balance() == 80
        assert self.a2.withdraw(50) is True
        assert self.a2.withdraw(0) is False
        assert self.a2.get_balance() == 50

if __name__ == "__main__":
    pytest.main()