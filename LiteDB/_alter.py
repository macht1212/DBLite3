import os

from LiteDB._funcs import _open_db, _save_db


# To change an object in the database, you need to call the .alter_object method from the alter module (from alter
# import alter_object) and pass the method name of db, collection name and old and new object name.
#
# Example::
#
#     >>> from alter import alter_object
#     >>> alter_object(db_name='new_db', collection='table', object_old='coll1', object_new='col2')
#
# To change a collection in the database, you need to call the .alter_collection method from the alter module (from
# alter import alter_collection) and pass the method name of db and old and new collection name.
#
# Example::
#
#     >>> from alter import alter_collection
#     >>> alter_collection(db_name='new_db', collection_new='table2', collection_old='table1')
#
# To change a name of the database, you need to call the .alter_db method from the alter module (from alter
# import alter_db) and pass the method name of db.
#
# Example::
#
#     >>> from alter import alter_db
#     >>> alter_db(db_name='new_db')


def alter_object(db_name: str, collection: str, object_old: str, object_new: str) -> None:
    """
    The function makes changes to the name of the object
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be modified
    :param object_old: the old name of the object to be modified
    :param object_new: the new name of the object to be modified
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    DATABASE[collection][object_new] = DATABASE[collection][object_old]
    del (DATABASE[collection][object_old])
    _save_db(db_name=db_name, DB=DATABASE)


def alter_collection(db_name: str, collection_new: str, collection_old: str) -> None:
    """
    The function makes changes to the name of the collection
    :param db_name: the name of the database to be modified
    :param collection_new: the new name of the collection to be modified
    :param collection_old: the old name of the collection to be modified
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    DATABASE[collection_new] = DATABASE.pop(collection_old)
    _save_db(db_name=db_name, DB=DATABASE)


def alter_db(db_name_old: str, db_name_new: str) -> None:
    """
    The function makes changes to the name of the database
    :param db_name_old: the old name of the database to be modified
    :param db_name_new: the new name of the database to be modified
    :return: None
    """
    os.rename(src=f'{db_name_old}.json', dst=f'{db_name_new}.json')
