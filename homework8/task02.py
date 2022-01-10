"""Write a wrapper class TableData for database table,
that when initialized with database name and table acts as collection object
(implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite',
                              table_name='presidents')
then len(presidents) will give current amount of rows in presidents table
in database
presidents['Yeltsin'] should return single data row
for president with name Yeltsin
'Yeltsin' in presidents should return if president with same name
exists in table

object implements iteration protocol. i.e. you could use it in for loops::
for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance,
your calls should return updated data.

Avoid reading entire table into memory.
When iterating through records, start reading the first record,
then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls
completely. Use supplied example.sqlite file as database fixture file.
"""
import sqlite3


class TableData:
    """wrapper class for database table,
    that when initialized with database name and table
    acts as collection object

    :param path: database path
    :type path: str
    :param table_name: database table name
    :type table_name: str
    """

    def __init__(self, path: str, table_name: str):
        self.path = path
        self.table_name = table_name
        self.__connection = sqlite3.connect(self.path)
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = self.__connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.cursor().close()
        self.__connection.close()

    def __iter__(self):
        yield from self.__cursor.execute(
            f'SELECT * FROM {self.table_name}'
        )

    def __len__(self):
        self.__cursor.execute(f'SELECT count(*) FROM {self.table_name}')
        return self.__cursor.fetchone()[0]

    def __getitem__(self, item: str):
        self.__cursor.execute(
            f'SELECT * FROM {self.table_name} WHERE name = ?', (item,)
        )
        return tuple(self.__cursor.fetchone())

    def __contains__(self, item: str):
        self.__cursor.execute(
            f'SELECT count(*) FROM {self.table_name} WHERE name = ?',
            (item,),
        )
        return self.__cursor.fetchone()[0] > 0

    def close(self):
        """closes the cursor and drops database connection
        """
        self.__connection.cursor().close()
        self.__connection.close()
