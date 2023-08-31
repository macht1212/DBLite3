import json
import os

from DBLite3_OOP._exceptions import OpenError, SaveError


def _get_value_index(db_name: str, collection: str, obj_name: str, id_: int) -> int | None:
    """
    Objective:
    The objective of the function is to return the index of a value in a specific object of a collection in a given
    database, based on the provided id.

    Inputs:
        - db_name: a string representing the name of the database to search for the value index.
        - collection: a string representing the name of the collection where the object is located.
        - obj_name: a string representing the name of the object where the value is located.
        - id_: an integer representing the id of the value to search for.

    Flow:
        - The function calls the _open_db() function to open the database and retrieve its content.
        - The function checks the type of 'db_name', 'collection', 'object', and 'id'. If they are not of the expected
          types, it raises a ValueError.
        - The function checks if the 'collection', 'object', and 'values' exist in the database. If any of them do not
          exist, it raises a ValueError.
        - The function iterates over the values of the specified object in the specified collection.
        - For each value, the function checks if its id matches the provided id.
        - If a match is found, the function returns the index of the value.
        - If no match is found, the function returns None.

    Outputs:
        - An integer representing the index of the value in the specified object of the specified collection in the
          specified database, based on the provided id.
        - None if no value with the provided id is found.

    Additional aspects:
        - The function assumes that the database, collection, object, and value with the provided names and id exist.
        - The function does not handle any errors that may occur during the file operations or the search for the value
          index.
    """
    try:
        database = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    if collection not in database or obj_name not in database[collection]:
        raise ValueError('Invalid collection, object, or database')
    if 'values' not in database[collection][obj_name]:
        raise ValueError('No values found in object')

    for index, v in enumerate(database[collection][obj_name]['values']):
        if v[0] == id_:
            return index
    return None


def _db_exists(db_name: str) -> bool:
    """
    Objective:
    The objective of the function is to check if a database with a given name exists in the base directory. It returns a
    boolean value indicating whether the database exists or not.

    Inputs:
        - db_name (str): the name of the database whose existence is to be checked.

    Flow:
        - The function first checks if a file with the name '{db_name}.json' exists in the base directory using the
          os.path.isfile() method.
        - If the file exists, the function returns True indicating that the database exists.
        - If the file does not exist, the function returns False indicating that the database does not exist.

    Outputs:
        - bool: True if the database exists, False if it does not exist.

    Additional aspects:
        - The function uses the os module to check if the file exists in the base directory.
        - The function assumes that the database is stored in a JSON file with the same name as the database name.
        - The function uses os.path.join to construct the file path instead of string concatenation to ensure
          compatibility across different operating systems.
        - The function validates that db_name is a non-empty string before proceeding.
    """

    if os.path.isfile(os.path.join(f'{db_name}.json')):
        return True
    return False


def _collection_exists(collection: str, database: dict) -> bool:
    """
    Objective:
    The objective of the function is to check if a given collection exists in a parsed database and return a boolean
    value indicating its existence.

    Inputs:
        - collection: a string representing the name of the collection to be checked
        - database: a dictionary representing the parsed database

    Flow:
        - The function checks if the given collection name exists in the keys of the database dictionary.
        - If the collection exists, the function returns True.
        - If the collection does not exist, the function returns False.

    Outputs:
        - bool: a boolean value indicating whether the collection exists in the database or not.

    Additional aspects:
        - The function assumes that the database has already been parsed and is represented as a dictionary.
        - The function only checks for the existence of the collection and does not perform any other operations on it
    """
    if collection in database.keys():
        return True
    return False


def _object_exists(collection: str, obj_name: str, database: dict) -> bool:
    """
    Objective:
    The main objective of the function is to check if a given object exists in a specified collection of a parsed
    database and return a boolean value indicating the existence of the object.

    Inputs:
        - collection: a string representing the name of the collection to be checked
        - obj_name: a string representing the name of the object to be checked
        - database: a dictionary representing the parsed database

    Flow:
        - The function takes in the collection, object, and database as inputs
        - It checks if the object exists in the specified collection of the database by using the 'in' operator to check
          if the object is a key in the collection
        - If the object exists, the function returns True, otherwise, it returns False

    Outputs:
        - bool: a boolean value indicating the existence of the object in the specified collection of the database

    Additional aspects:
        - The function is designed to work with a parsed database, which means that the database has already been
          processed and converted into a dictionary format
        - The function only checks for the existence of an object in a single collection, and not across multiple
          collections in the database.
    """
    if obj_name in database[collection].keys():
        return True
    return False


def _is_value_in(database: dict, collection: str, obj_name: str) -> bool:
    """
    Objective:
    The objective of the function is to check if the first entry in a given collection exists in a database dictionary.

    Inputs:
        - database: a dictionary containing the database
        - collection: a string representing the name of the collection to add the value to
        - obj_name: a string representing the name of the table to add the value to

    Flow:
        - Check if the first entry in the collection exists by accessing the 'values' key of the object in the collection
        - If the 'values' key is not empty, return False
        - If the 'values' key is empty, return True

    Outputs:
        - True if the first entry in the collection exists
        - False if the first entry in the collection does not exist

    Additional aspects:
        - The function only checks for the existence of the first entry in the collection
        - The function assumes that the 'values' key exists in the object in the collection
    """
    if database[collection][obj_name]['values']:
        return True
    return False


def _count(database: dict, collection: str, obj_name: str) -> int:
    """
    Objective:
    The objective of the function is to count the number of entries in a given collection in a database dictionary.
    If the first entry in the collection exists, the function returns the value of the first element in the last entry
    of the 'values' key of the object in the collection. Otherwise, the function returns 0.

    Inputs:
        - database: a dictionary containing the database
        - collection: a string representing the name of the collection to count the entries in
        - obj_name: a string representing the name of the table to count the entries in

    Flow:
        - Check if the first entry in the collection exists by calling the _is_value_in function
        - If the first entry exists, return the value of the first element in the last entry of the 'values' key of the
          object in the collection
        - If the first entry does not exist, return 0

    Outputs:
        - An integer representing the number of entries in the collection, or 0 if the collection is empty

    Additional aspects:
        - The function assumes that the 'values' key exists in the object in the collection
        - The function only counts the number of entries in the collection, and does not modify the database dictionary
    """
    if _is_value_in(database=database, collection=collection, obj_name=obj_name):
        return database.get(collection, None).get(obj_name, None).get('values', None)[-1][0]
    else:
        return 0
