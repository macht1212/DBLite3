import os

from LiteDB._funcs import _open_db, _save_db


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
