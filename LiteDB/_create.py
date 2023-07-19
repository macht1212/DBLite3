from LiteDB._funcs import _open_db, _save_db, _db_exists, _collection_exists


# To create new DataBase you need call .create_db method from create module (from create import create_db)
# and pass to method db name. If database with this name has already existed, the Error will raise to console but
# program will continue working.
#
# Example (DB does not exist)::
#
#     >>> from create import create_db
#     >>> create_db(db_name='new_db')
#     'DataBase db_name was created.'
#
# Example (DB exists)::
#
#     >>> from create import create_db
#     >>> create_db(db_name='new_db')
#     'DATABASE with this name has already existed'
#
# To create table  you need call .create_table method from create module (from create import create_table)
# and pass to method db name, table name and list of collections. If table with this name has already existed,
# the Error will raise to console but program will continue working.
#
# Example (Table does not exist):
#     >>> from create import create_table
#     >>> create_table(db_name='new_db', table_name='table', collections='coll')
#     'Table table_name with collections: col, col was created.'
#
# Example (Table exists)::
#
#     >>> from create import create_collection
#     >>> create_table(db_name='new_db', collection='table', object='coll')
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


def create_collection(db_name: str, collection: str, object: list) -> None:
    """
    The function creates a table with collections
    :param  db_name: the selected database to create the table. Data is passed to the function as a string
    :param  collection: table name. IMPORTANT! The table name must be unique. Data is passed to the function as a string
    :param  object: object name. A collection is similar to a column in a classic relational database, but at
            the same time it does not require a clear fixation of data relative to other such collections. Data is
            passed to the function as a list
    :return: None
    """

    DATABASE = _open_db(db_name=db_name)
    if _collection_exists(collection=collection, DB=DATABASE):
        print(Exception(f'Table with name {collection} has already existed.'))
    else:
        DATABASE[collection] = {}
        for o in object:
            DATABASE[collection][o] = {'values': None}
    _save_db(db_name=db_name, DB=DATABASE)
