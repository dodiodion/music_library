from lib.user_account import UserAccount
class UserAccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM user_accounts')
        user_accounts = []
        for row in rows:
            item = UserAccount(row["id"], row["email_address"], row["username"])
            user_accounts.append(item)
        return user_accounts
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM user_accounts WHERE id = %s', [id])
        row = rows[0]
        return UserAccount(row["id"], row["email_address"], row["username"])
    
    def create(self, new_user_account):
        self._connection.execute('INSERT INTO user_accounts (email_address, username) VALUES (%s, %s)', [new_user_account.email_address, new_user_account.username])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM user_accounts WHERE id = %s', [id])
        return None