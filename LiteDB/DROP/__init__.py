import os
from LiteDB._funcs import _open_db, _save_db
from LiteDB.CREATE import _db_exists


# To drop the database, table or collection, use the DROP module.
#
# To drop database, you need to import the .drop_db method from the DROP module. (from LiteDB.DROP import drop_db)
# In this method, you must pass the name of the database.
#
# Example::
#
#     >>> from LiteDB.DROP import drop_db
#     >>> drop_db(db_name='new')
#
#
# To drop table from database, you need to import the .drop_db method from the DROP module.
# (from LiteDB.DROP import drop_table) In this method, you must pass the name of the database and the name of the
# table.
#
# Example::
#
#     >>> from LiteDB.DROP import drop_table
#     >>> drop_db(db_name='new', table_name='table')
#
# To drop collection from database, you need to import the .drop_collection method from the DROP module.
# (from LiteDB.DROP import drop_collection) In this method, you must pass the name of the database, the name of the
# table and the name of the collection.
#
# Example::
#
#     >>> from LiteDB.DROP import drop_collection
#     >>> drop_db(db_name='new', table_name='table', collection='coll')


def drop_db(db_name: str) -> None:
    """
    The function deletes the database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be dropped
    :return: None
    """
    if _db_exists(db_name=db_name):
        os.remove(f'{db_name}.json')
    else:
        print(Exception('Database does not exist.'))


def drop_table(db_name: str, table_name: str) -> None:
    """
    The function deletes the table from database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be modified
    :param table_name: the name of the table to be dropped
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    del(DATABASE[table_name])
    _save_db(db_name=db_name, DB=DATABASE)


def drop_collection(db_name: str, table_name: str, collection: str) -> None:
    """
    The function deletes the collection from database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be modified
    :param table_name: the name of the table to be modified
    :param collection: the name of the collection to be dropped
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    del(DATABASE[table_name][collection])
    _save_db(db_name=db_name, DB=DATABASE)
