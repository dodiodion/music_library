from lib.user_account import *
"""
given a user account, verify that it contructs with an id, email_address and username
"""

def test_user_account_constructs():
    user_account = UserAccount(1, "Test email_address", "Test Username")
    assert user_account.id == 1
    assert user_account.email_address == "Test email_address"
    assert user_account.username == "Test Username"

"""
Given two identical UserAccount,
I want them to be equal
"""
def test_user_accounts_are_equal():
    user_account1 = UserAccount(1, "andre@hotmail.com", "andre234")
    user_account2 = UserAccount(1, "andre@hotmail.com", "andre234")
    assert user_account1 == user_account2

"""
Given a UserAccount
it should return a nicely formatted string
"""
def test_format_user_account():
    assert str(UserAccount(1, "andre@hotmail.com", "andre234")) == f"User Account -  id: 1 - andre@hotmail.com - andre234"