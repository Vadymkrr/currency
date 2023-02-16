import sqlite3
from datetime import datetime

con = sqlite3.connect('Chinook_Sqlite.sqlite')
con.row_factory = sqlite3.Row
cur = con.cursor()

sql = '''
SELECT LastName, CustomerId, FirstName  FROM Customer;
'''

cur.execute(sql)
res = cur.fetchall()
con.close()


class User:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_full_name(self):
        return f'{self.FirstName} {self.LastName}'

    def save(self):
        con = sqlite3.connect('Chinook_Sqlite.sqlite')
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        sql = f"""
        UPDATE Customer
        SET LastName = '{self.LastName}',
            FirstName = '{self.FirstName}'
        WHERE CustomerId = {self.CustomerId}
        """
        cur.execute(sql)
        con.commit()
        con.close()


users = [User(**data) for data in res]
# for user in users:
#   print(f'{user.CustomerId} {user.FirstName} {user.LastName}')
breakpoint()

