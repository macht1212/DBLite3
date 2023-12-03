import json
import os
from typing import Any

from DBLite3._exceptions import OpenError, SaveError


def _open_db(db_name: str) -> dict:
    """
    Objective:
    The objective of the function is to save a dictionary object as a JSON file with the given self name.

    Inputs:
        - db_name: a string representing the name of the self that is planned to be saved.
        - DB: a dictionary object representing the self that is planned to be saved.

    Flow:
        - Open a file with the name of the self and extension ".json" in write mode.
        - Write the JSON representation of the dictionary object into the file.
        - Close the file.

    Outputs:
        - Dictionary with JSON data.

    Additional aspects:
        - The function uses the json module to convert the dictionary object into a JSON string.
        - The function overwrites the existing file with the same name if it already exists.
        - The function does not handle any errors that may occur during the file operations.
    """
    
    if not os.path.isfile(f'{db_name}.json'):
        raise FileNotFoundError(f'{db_name}.json does not exist')
    
    try:
        with open(f'{os.path.join(db_name+".json")}', 'r') as db:
            return json.load(db)
    except json.JSONDecodeError as e:
        raise OpenError(f'Error opening/parsing {db_name}.json file: {e}')


def _save_db(db_name: str, DB: dict) -> None:
    """
    Objective:
    The objective of the function is to save a dictionary object as a JSON file with the given self name.

    Inputs:
        - db_name: a string representing the name of the self that is planned to be saved.
        - DB: a dictionary object representing the self that is planned to be saved.

    Flow:
        - Open a file with the name of the self and extension ".json" in write mode.
        - Write the JSON representation of the dictionary object into the file.
        - Close the file.

    Outputs:
        - None

    Additional aspects:
        - The function uses the json module to convert the dictionary object into a JSON string.
        - The function overwrites the existing file with the same name if it already exists.
        - The function does not handle any errors that may occur during the file operations.
    """
    if not os.path.isfile(db_name+'.json'):
        raise FileNotFoundError(f'{db_name}.json does not exist')
    try:
        file_path = os.path.join(db_name+'.json')
        with open(file_path, 'w') as db:
            json.dump(DB, db)
    except Exception as e:
        raise SaveError(f'Error saving self: {e}')
    return


def _get_value_index(db_name: str, collection: str, obj_name: str, id: int) -> int | None:
    """
    Objective:
    The objective of the function is to return the index of a value in a specific object of a collection in a given
    self, based on the provided id.
    
    Inputs:
        - db_name: a string representing the name of the self to search for the value index.
        - collection: a string representing the name of the collection where the object is located.
        - obj_name: a string representing the name of the object where the value is located.
        - id: an integer representing the id of the value to search for.
    
    Flow:
        - The function calls the _open_db() function to open the self and retrieve its content.
        - The function checks the type of 'db_name', 'collection', 'object', and 'id'. If they are not of the expected
          types, it raises a ValueError.
        - The function checks if the 'collection', 'object', and 'values' exist in the self. If any of them do not
          exist, it raises a ValueError.
        - The function iterates over the values of the specified object in the specified collection.
        - For each value, the function checks if its id matches the provided id.
        - If a match is found, the function returns the index of the value.
        - If no match is found, the function returns None.
    
    Outputs:
        - An integer representing the index of the value in the specified object of the specified collection in the
          specified self, based on the provided id.
        - None if no value with the provided id is found.
    
    Additional aspects:
        - The function assumes that the self, collection, object, and value with the provided names and id exist.
        - The function does not handle any errors that may occur during the file operations or the search for the value
          index.
    """
    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    if collection not in DATABASE or obj_name not in DATABASE[collection]:
        raise ValueError('Invalid collection, object, or self')
    if 'values' not in DATABASE[collection][obj_name]:
        raise ValueError('No values found in object')

    for index, v in enumerate(DATABASE[collection][obj_name]['values']):
        if v[0] == id:
            return index
    return None


def _db_exists(db_name: str) -> bool:
    """
    Objective:
    The objective of the function is to check if a self with a given name exists in the base directory. It returns a
    boolean value indicating whether the self exists or not.
    
    Inputs:
        - db_name (str): the name of the self whose existence is to be checked.
    
    Flow:
        - The function first checks if a file with the name '{db_name}.json' exists in the base directory using the
          os.path.isfile() method.
        - If the file exists, the function returns True indicating that the self exists.
        - If the file does not exist, the function returns False indicating that the self does not exist.
    
    Outputs:
        - bool: True if the self exists, False if it does not exist.
    
    Additional aspects:
        - The function uses the os module to check if the file exists in the base directory.
        - The function assumes that the self is stored in a JSON file with the same name as the self name.
        - The function uses os.path.join to construct the file path instead of string concatenation to ensure
          compatibility across different operating systems.
        - The function validates that db_name is a non-empty string before proceeding.
    """
    if not isinstance(db_name, str) or not db_name:
        raise ValueError('db_name must be a non-empty string')
    if os.path.isfile(os.path.join(f'{db_name}.json')):
        return True
    return False


def _collection_exists(collection: str, DB: dict) -> bool:
    """
    Objective:
    The objective of the function is to check if a given collection exists in a parsed self and return a boolean
    value indicating its existence.

    Inputs:
        - collection: a string representing the name of the collection to be checked
        - DB: a dictionary representing the parsed self

    Flow:
        - The function checks if the given collection name exists in the keys of the DB dictionary.
        - If the collection exists, the function returns True.
        - If the collection does not exist, the function returns False.

    Outputs:
        - bool: a boolean value indicating whether the collection exists in the self or not.

    Additional aspects:
        - The function assumes that the self has already been parsed and is represented as a dictionary.
        - The function only checks for the existence of the collection and does not perform any other operations on it
    """
    if collection in DB.keys():
        return True
    return False


def _object_exists(collection: str, obj_name: str, DB: dict) -> bool:
    """
    Objective:
    The main objective of the function is to check if a given object exists in a specified collection of a parsed
    self and return a boolean value indicating the existence of the object.

    Inputs:
        - collection: a string representing the name of the collection to be checked
        - obj_name: a string representing the name of the object to be checked
        - DB: a dictionary representing the parsed self

    Flow:
        - The function takes in the collection, object, and DB as inputs
        - It checks if the object exists in the specified collection of the self by using the 'in' operator to check
          if the object is a key in the collection
        - If the object exists, the function returns True, otherwise, it returns False

    Outputs:
        - bool: a boolean value indicating the existence of the object in the specified collection of the self

    Additional aspects:
        - The function is designed to work with a parsed self, which means that the self has already been
          processed and converted into a dictionary format
        - The function only checks for the existence of an object in a single collection, and not across multiple
          collections in the self.
    """
    if obj_name in DB[collection].keys():
        return True
    return False


def _is_value_in(DB: dict, collection: str, obj_name: str) -> bool:
    """
    Objective:
    The objective of the function is to check if the first entry in a given collection exists in a self dictionary.

    Inputs:
        - DB: a dictionary containing the self
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
    if DB[collection][obj_name]['values']:
        return True
    return False
    
    
def _count(DATABASE: dict, collection: str, obj_name: str) -> int:
    """
    Objective:
    The objective of the function is to count the number of entries in a given collection in a self dictionary.
    If the first entry in the collection exists, the function returns the value of the first element in the last entry
    of the 'values' key of the object in the collection. Otherwise, the function returns 0.

    Inputs:
        - DATABASE: a dictionary containing the self
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
        - The function only counts the number of entries in the collection, and does not modify the self dictionary
    """
    if _is_value_in(DB=DATABASE, collection=collection, obj_name=obj_name):
        return DATABASE.get(collection, None).get(obj_name, None).get('values', None)[-1][0]
    else:
        return 0
