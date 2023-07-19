import os
from NoSQLite3._funcs import _open_db, _save_db, _db_exists


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


def drop_collection(db_name: str, collection: str) -> None:
    """
    The function deletes the table from database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be dropped
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    del(DATABASE[collection])
    _save_db(db_name=db_name, DB=DATABASE)


def drop_object(db_name: str, collection: str, object: str) -> None:
    """
    The function deletes the collection from database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be modified
    :param object: the name of the object to be dropped
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    del(DATABASE[collection][object])
    _save_db(db_name=db_name, DB=DATABASE)
