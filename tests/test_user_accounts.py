from lib.user_accounts import *
"""
given a user account, verify that it contructs with an id, email_address and username
"""

def test_user_account_constructs():
    user_account = UserAccount(1, "Test email_address", "Test Username")
    assert user_account.id == 1
    assert user_account.email_address == "Test email_address"
    assert user_account.username == "Test Username"
  