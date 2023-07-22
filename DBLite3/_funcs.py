import json
import os
from typing import Any

# from DBLite3 import SelectError


def _open_db(db_name: str) -> dict:
    """
    The function parses the json file and returns a dictionary
    :param db_name: the name of the database that is planned to be opened
    :return: dict of parsed Database
    """
    with open(f'{db_name}.json', 'r') as db:
        info = db.read()
        return json.loads(info)


def _save_db(db_name: str, DB: dict) -> None:
    """
    The function translates the dictionary into a json file
    :param db_name: the name of the database that is planned to be saved
    :param DB: dict of the database that is planned to be saved
    :return: None
    """
    with open(f'{db_name}.json', 'w') as db:
        db.write(str(json.dumps(DB)))
    return


def _get_value_id(db_name: str, collection: str, object: str, value: Any) -> int:
    """
    The function returns the id of the value
    :param db_name: name of database to return id
    :param collection: name of collection to return id
    :param object: name of object to return id
    :param value: value to be returned id
    :return: int -> id of the value
    """
    DATABASE = _open_db(db_name=db_name)
    for v in DATABASE[collection][object]['values']:
        if v[1] == value:
            return v[0]


def _get_value_index(db_name: str, collection: str, object: str, id: int) -> int:
    """
    The function returns the index of the value
    :param: db_name: name of database to return index
    :param: collection: name of collection to return index
    :param: object: name of object to return index
    :param: id: id to be returned index
    :return: int -> index of the value by id
    """
    DATABASE = _open_db(db_name=db_name)
    for index, v in enumerate(DATABASE[collection][object]['values']):
        if v[0] == id:
            return index


def _db_exists(db_name: str) -> bool:
    """
    The function checks if the database exists in the base directory, returns False if it doesn't exist
    :param: db_name: the name of the database whose existence is to be checked
    :return: bool (True if DB exists)
    """
    if os.path.exists(f'{db_name}.json'):
        return True
    return False


def _collection_exists(collection: str, DB: dict) -> bool:
    """
    The function checks if the collection exists in the database, returns False if it doesn't exist
    :param collection: the name of the collection whose existence is to be checked
    :param DB: dict of parsed Database
    :return: bool (True if collection exists)
    """
    if collection in DB.keys():
        return True
    return False


def _object_exists(collection: str, object: str, DB: dict) -> bool:
    """
    The function checks if the object exists in the database, returns False if it doesn't exist
    :param collection: the name of the collection whose existence is to be checked
    :param object: the name of the object whose existence is to be checked
    :param DB: dict of parsed Database
    :return: bool (True if object exists)
    """
    if object in DB[collection].keys():
        return True
    return False


def _is_value_in(DB: dict, collection: str, object: str) -> bool:
    """
    The function checks if the first entry in the collection exists
    :param DB: dictionary containing the database
    :param object: The name of the table to add the value to
    :param collection: The name of the collection to add the value to
    :return: True if the first entry in the collection exists
    """
    if DB[collection][object]['values']:
        return False
    return True


# def _all_exists(db_name: str, collection: str, object: str, DB: dict) -> bool:
#     """
#
#     """
#     if not _db_exists(db_name=db_name):
#         raise SelectError(f'Database {db_name} does not exist.')
#     if not _collection_exists(collection=collection, DB=DB):
#         raise SelectError(f'Collection {collection} does not exist.')
#     if not _object_exists(collection=collection, object=object, DB=DB):
#         raise SelectError(f'Object {object} does not exist.')
#     return True


