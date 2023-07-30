import os

from DBLite3._exceptions import DropError
from DBLite3._funcs import _open_db, _save_db, _db_exists, _does_collection_exists, _object_exists


def drop_db(db_name: str) -> None:
    """
    Objective:
    The objective of the drop_db function is to delete a database with a given name. It raises a DropError exception if the database does not exist and deletes the database file if it exists.
    
    Inputs:
        - db_name (str): the name of the database to be dropped.
    
    Flow:
        - The function first checks if the database exists using the _db_exists function.
        - If the database exists, the function deletes the database file using the os.remove method.
        - If the database does not exist, the function raises a DropError exception with a custom error message.
    
    Outputs:
        - None: The function does not return any value.
    
    Additional aspects:
        - The function assumes that the database is stored in a JSON file with the same name as the database name.
        - The function uses os.path.join to construct the file path instead of string concatenation to ensure compatibility across different operating systems.
        - The function raises a ValueError if db_name is not a non-empty string.
    """
    if _db_exists(db_name=db_name):
        os.remove(f'{db_name}.json')
        return
    else:
        raise DropError(f'Database {db_name} does not exist.')


def drop_collection(db_name: str, collection: str) -> None:
    """
    Objective:
    The objective of the 'drop_collection' function is to delete a collection from a database. This function takes in the name of the database and the collection to be deleted as input parameters. If the collection exists in the database, it is deleted and the updated database is saved. If the collection does not exist, a custom 'DropError' exception is raised.
    
    Inputs:
        - db_name: a string representing the name of the database to be modified
        - collection: a string representing the name of the collection to be dropped
    
    Flow:
        - The function first checks if the input parameters 'db_name' and 'collection' are non-empty strings. If either of them is empty, a 'ValueError' exception is raised.
        - The function then opens the database using the '_open_db' function and stores it in the 'DATABASE' variable.
        - The function checks if the collection exists in the database using the '_does_collection_exists' function. If the collection exists, it is deleted from the database using the 'del' keyword.
        - The updated database is then saved using the '_save_db' function.
        - If the collection does not exist in the database, a 'DropError' exception is raised.
    
    Outputs:
        - None
    
    Additional aspects:
        - The function uses the '_open_db', '_does_collection_exists', and '_save_db' functions to open, check, and save the database, respectively.
        - The function raises custom exceptions 'ValueError' and 'DropError' if the input parameters are invalid or the collection does not exist in the database, respectively
    """
    if not db_name or not collection:
        raise ValueError('db_name and collection must be non-empty strings')
    
    DATABASE = _open_db(db_name=db_name)
    if _does_collection_exists(collection=collection, DB=DATABASE):
        del (DATABASE[collection])
        _save_db(db_name=db_name, DB=DATABASE)
        return
    else:
        raise DropError(f'Collection {collection} does not exist.')


def drop_object(db_name: str, collection: str, obj_name: str) -> None:
    """
    Objective:
    The objective of the 'drop_object' function is to delete a specified object from a specified collection in a given database. The function checks if the object exists in the collection and raises an error if it does not. If the object exists, it is deleted from the collection, and the modified database is saved.

    Inputs:
        - db_name: a string representing the name of the database to be modified
        - collection: a string representing the name of the collection to be modified
        - obj_name: a string representing the name of the object to be dropped

    Flow:
        - The function takes in the inputs db_name, collection, and object
        - It checks if the inputs are valid strings and raises a ValueError if any of them are empty or not strings
        - It opens the database using the '_open_db' function and checks if the object exists in the specified collection using the '_object_exists' function
        - If the object exists, it is deleted from the collection using the 'del' keyword
        - The modified database is saved using the '_save_db' function
        - If the object does not exist, a 'DropError' is raised with a custom error message

    Outputs:
        - None

    Additional aspects:
        - The function raises a 'DropError' if any errors occur during the execution of the function
        - The function modifies the database and saves the modified version, which can result in data loss if used incorrectly
        - The function only deletes objects from a single collection and does not work across multiple collections in the database.
    """
    try:
        if not isinstance(db_name, str) or not db_name:
            raise ValueError('db_name must be a non-empty string')
        if not isinstance(collection, str) or not collection:
            raise ValueError('collection must be a non-empty string')
        if not isinstance(obj_name, str) or not obj_name:
            raise ValueError('object must be a non-empty string')

        DATABASE = _open_db(db_name=db_name)
        if _object_exists(collection=collection, obj_name=obj_name, DB=DATABASE):
            del (DATABASE[collection][obj_name])
            _save_db(db_name=db_name, DB=DATABASE)
            return
        else:
            raise DropError(f'Object {obj_name} does not exist.')
    except Exception as e:
        raise DropError(f'Error dropping object: {e}')