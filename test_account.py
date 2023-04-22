import pytest
from account import Account

def test_account_init():
    account = Account("John")
    assert account.get_name() == "John"
    assert account.get_balance() == 0

def test_deposit():
    account = Account("John")
    assert account.deposit(100) == True
    assert account.get_balance() == 100
    assert account.deposit(-50) == False
    assert account.get_balance() == 100
    assert account.deposit(0) == False
    assert account.get_balance() == 100

def test_withdraw():
    account = Account("John")
    account.deposit(100)
    assert account.withdraw(50) == True
    assert account.get_balance() == 50
    assert account.withdraw(-50) == False
    assert account.get_balance() == 50
    assert account.withdraw(0) == False
    assert account.get_balance() == 50
    assert account.withdraw(100) == False
    assert account.get_balance() == 50
