import json
import os


def _open_db(db_name: str) -> dict:
    """
    The function parses the json file and returns a dictionary
    :param db_name: the name of the database that is planned to be opened
    :return: dict
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


def _get_value_id(db_name: str, collection: str, object: str, value) -> int:
    DATABASE = _open_db(db_name=db_name)
    for v in DATABASE[collection][object]['values']:
        if v[1] == value:
            return v[0]


def _db_exists(db_name: str) -> bool:
    """
    The function checks if the database exists in the base directory, returns False if it doesn't exist
    :param: db_name: db's name
    :return: bool (True if DB exists)
    """
    if os.path.exists(f'{db_name}.json'):
        return True
    return False


def _collection_exists(collection: str, DB: dict) -> bool:
    """
    The function checks if the table exists in the database, returns False if it doesn't exist
    :param collection:
    :param DB:
    :return:
    """
    if collection in DB.keys():
        return True
    return False


def _value_in(DATABASE: dict, collection: str, object: str) -> bool:
    """
    The function checks if the first entry in the collection exists
    :param DATABASE: dictionary containing the database
    :param object: The name of the table to add the value to
    :param collection: The name of the collection to add the value to
    :return: True if the first entry in the collection exists
    """
    if DATABASE[collection][object]['values']:
        return False
    return True
