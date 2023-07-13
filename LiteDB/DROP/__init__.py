import os
from LiteDB._funcs import _open_db, _save_db


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

    :param db_name:
    :return:
    """
    os.remove(f'{db_name}.json')


def drop_table(db_name: str, table_name: str) -> None:
    """

    :param db_name:
    :param table_name:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    del (DATABASE[table_name])
    _save_db(db_name=db_name, DB=DATABASE)


def drop_collection(db_name: str, table_name: str, collection: str) -> None:
    """

    :param db_name:
    :param table_name:
    :param collection:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    del (DATABASE[table_name][collection])
    _save_db(db_name=db_name, DB=DATABASE)
