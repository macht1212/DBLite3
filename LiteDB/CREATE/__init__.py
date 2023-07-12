from LiteDB.CREATE.CREATE import _db_exists, _table_exists
from LiteDB._funcs import _open_db, _save_db


# To create new DataBase you need call .create_db method from CREATE module (from CREATE import create_db)
# and pass to method db name. If database with this name has already existed, the Error will raise to console but
# program will continue working.
#
# Example (DB does not exist)::
#
#     >>> from CREATE import create_db
#     >>> create_db(db_name='new_db')
#     'DataBase db_name was created.'
#
# Example (DB exists)::
#
#     >>> from CREATE import create_db
#     >>> create_db(db_name='new_db')
#     'DATABASE with this name has already existed'
#
# To create table  you need call .create_table method from CREATE module (from CREATE import create_table)
# and pass to method db name, table name and list of collections. If table with this name has already existed,
# the Error will raise to console but program will continue working.
#
# Example (Table does not exist):
#     >>> from CREATE import create_table
#     >>> create_table(db_name='new_db', table_name='table', collections='coll')
#     'Table table_name with collections: col, col was created.'
#
# Example (Table exists)::
#
#     >>> from CREATE import create_table
#     >>> create_table(db_name='new_db', table_name='table', collections='coll')
#     'Table with this name has already existed'


def create_db(db_name: str) -> None:
    """
    The function creates a database in the base directory of the project
    :param  db_name: the name of the database to be created. The name of the database must be unique in the project,
            otherwise the file will be overwritten. Data is passed to the function as a string
    :return: None
    """
    if _db_exists(db_name=db_name):
        print(ValueError(f'DATABASE with name {db_name} has already existed'))
    else:
        with open(f'./{db_name}.json', 'w') as f:
            f.write('{}')
        print(f'DataBase {db_name} was created.')


def create_table(db_name: str, table_name: str, collections: list) -> None:
    """
    The function creates a table with collections
    :param  db_name: the selected database to create the table. Data is passed to the function as a string
    :param  table_name: table name. IMPORTANT! The table name must be unique. Data is passed to the function as a string
    :param  collections: collection name. A collection is similar to a column in a classic relational database, but at
            the same time it does not require a clear fixation of data relative to other such collections. Data is
            passed to the function as a list
    :return: None
    """

    DATABASE = _open_db(db_name=db_name)
    if _table_exists(table_name=table_name, DB=DATABASE):
        print(Exception(f'Table with name {table_name} has already existed.'))
    else:
        DATABASE[table_name] = {}
        for collection in collections:
            DATABASE[table_name][collection] = {'values': None}
    _save_db(db_name=db_name, DB=DATABASE)
