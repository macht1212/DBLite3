from typing import Any

from DBLite3 import SaveError, OpenError
from DBLite3._funcs import _open_db, _save_db, _get_value_index


def update_value_by_id(db_name: str, collection: str, obj_name: str, id: int, value: Any) -> None:
    """
    Objective:
    The objective of the function is to update a single value in a specific object of a collection in a given database,
    based on the provided id.
    
    Inputs:
        - db_name: a string representing the name of the database to be modified.
        - collection: a string representing the name of the collection to be modified.
        - obj_name: a string representing the name of the object to be modified.
        - id: an integer representing the id of the value to be modified.
        - value: any type representing the new value to be assigned to the specified id.
    
    Flow:
        - The function calls the _open_db() function to open the database and retrieve its content.
        - The function calls the _get_value_index() function to retrieve the index of the value to be modified.
        - The function updates the value at the retrieved index with the provided new value.
        - The function calls the _save_db() function to save the modified database.
    
    Outputs:
        - None
    
    Additional aspects:
        - The function assumes that the database, collection, object, and value with the provided names and id exist.
        - The function does not handle any errors that may occur during the file operations or the search for the value
          index.
    """
    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')
    
    if not isinstance(collection, str) or not isinstance(obj_name, str) or not isinstance(id, int):
        raise TypeError('collection, object, and id must be str and int, respectively')
    if collection not in DATABASE or obj_name not in DATABASE[collection]:
        raise ValueError('Invalid collection or object')
    
    index = _get_value_index(db_name=db_name, collection=collection, obj_name=obj_name, id=id)
    
    if index is None:
        raise ValueError('Value with provided id does not exist')
    try:
        DATABASE[collection][obj_name]['values'][index][1] = value
    except Exception as e:
        raise Exception(f'Error {e}')
    
    try:
        _save_db(db_name=db_name, DB=DATABASE)
    except SaveError as e:
        raise SaveError(f'Error saving database: {e}')


def update_values_by_id(db_name: str, collection: str, obj_name: str, id: list, values: list) -> None:
    """
    Objective:
    The objective of the function is to update multiple values in a specific object of a collection in a given database,
    based on the provided identifiers.

    Inputs:
        - db_name: a string representing the name of the database to be modified.
        - collection: a string representing the name of the collection to be modified.
        - obj_name: a string representing the name of the object to be modified.
        - id: a list of integers representing the identifiers of the values to be modified.
        - values: a list of the new values to replace the old ones.

    Flow:
        - The function calls the _open_db() function to open the database and retrieve its content.
        - The function iterates over the provided list of identifiers.
        - For each identifier, the function calls the _get_value_index() function to retrieve the index of the value in
          the specified object of the specified collection in the specified database, based on the provided identifier.
        - The function updates the value at the retrieved index with the corresponding value from the provided list of
          new values.
        - The function calls the _save_db() function to save the modified database.

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the database, collection, object, and values with the provided names and identifiers
          exist.
        - The function does not handle any errors that may occur during the file operations or the update of the values.
    """
    if (not isinstance(collection, str) or not isinstance(obj_name, str) or not isinstance(id, list)
            or not isinstance(values, list)):
        raise ValueError('collection, object, and id must be str and int, respectively')
    if len(id) != len(values):
        raise ValueError('id and values lists must have the same length')

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    if collection not in DATABASE or obj_name not in DATABASE[collection]:
        raise ValueError('Invalid collection or object')
    
    for i, id in enumerate(id):
        index = _get_value_index(db_name=db_name, collection=collection, obj_name=obj_name, id=id)
        
        if index is None:
            raise ValueError(f'Value with id {id} not found in database')
        
        DATABASE[collection][obj_name]['values'][index][1] = values[i]
    
    try:
        _save_db(db_name=db_name, DB=DATABASE)
    except (SaveError, OpenError) as e:
        print(f'Error updating values by id: {e}')
