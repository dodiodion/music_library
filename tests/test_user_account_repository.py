from lib.user_account_repository import UserAccountRepository
from lib.user_account import UserAccount
"""
When we call UserAccountRepository#all
We get a list of UserAccount objects reflecting the seed data.
"""
def test_get_all_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)
    user_accounts = repository.all()
    assert user_accounts == [
        UserAccount(1, 'bob@gmail.com', 'bob1'),
        UserAccount(2, 'coxinha@hotmail.com', 'coxinha1995'),
        UserAccount(3, 'poutine@mail.com', 'poutine44'),
        UserAccount(4, 'feijoada@intel.it', 'feijoada983')
    ]

def test_find_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)
    user_account = repository.find(2)
    assert user_account == UserAccount(2, 'coxinha@hotmail.com', 'coxinha1995')

def test_create_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)
    repository.create(UserAccount(None, "fred@hotmail.com", "freddo"))
    result = repository.all()
    assert result == [
        UserAccount(1, 'bob@gmail.com', 'bob1'),
        UserAccount(2, 'coxinha@hotmail.com', 'coxinha1995'),
        UserAccount(3, 'poutine@mail.com', 'poutine44'),
        UserAccount(4, 'feijoada@intel.it', 'feijoada983'),
        UserAccount(5, 'fred@hotmail.com', 'freddo')
    ]

"""
When we call UserAccountRepository#delete
The userAccount is deleted from the database
"""
def test_delete_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        UserAccount(1, 'bob@gmail.com', 'bob1'),
        UserAccount(2, 'coxinha@hotmail.com', 'coxinha1995'),
        UserAccount(4, 'feijoada@intel.it', 'feijoada983')
    ]