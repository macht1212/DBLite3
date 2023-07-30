from DBLite3 import DeleteError
from DBLite3._funcs import _open_db, _save_db, _get_value_index


def delete_value(db_name: str, collection: str, obj_name: str, id: int) -> None:
    """
    Objective:
    The objective of the 'delete_value' function is to delete a value from a specific object in a collection of a given database, based on the provided id.
    
    Inputs:
        - db_name: a string representing the name of the database to delete the value from.
        - collection: a string representing the name of the collection to delete the value from.
        - obj_name: a string representing the name of the object to delete the value from.
        - id: an integer representing the id of the value to delete.
        
    Flow:
        - The function calls the '_get_value_index' function to retrieve the index of the value to delete.
        - The function calls the '_open_db' function to open the database and retrieve its content.
        - The function checks if the collection, object, and values exist in the database. If any of them do not exist, it raises a ValueError.
        - The function checks if the index of the value to delete is not None.
        - If the index is not None, the function deletes the value from the list of values in the specified object of the specified collection in the specified database.
        - If the list of values becomes empty, the function sets it to None.
        - The function calls the '_save_db' function to save the updated database.
        
    Outputs:
        - None
    
    Additional aspects:
        - The function raises a DeleteError if any error occurs during the deletion process.
        - The function assumes that the database, collection, object, and value with the provided names and id exist.
        - The function does not handle any errors that may occur during the file operations or the search for the value index.
    """
    try:
        index = _get_value_index(db_name=db_name, collection=collection, obj_name=obj_name, id=id)
        DATABASE = _open_db(db_name=db_name)
        
        if collection not in DATABASE or obj_name not in DATABASE[collection]:
            raise ValueError('Invalid collection or object')
        
        if 'values' not in DATABASE[collection][obj_name]:
            raise ValueError('No values found in object')
        
        if index is not None:
            if len(DATABASE[collection][obj_name]['values']) == 1:
                DATABASE[collection][obj_name]['values'] = None
            else:
                del DATABASE[collection][obj_name]['values'][index]
        
        _save_db(db_name=db_name, DB=DATABASE)
    
    except Exception as e:
        raise DeleteError(f'Error deleting value: {e}')


def delete_all_values(db_name: str, collection: str, obj_name: str) -> None:
    """
    Objective:
    The objective of the 'delete_all_values' function is to delete all values from a specific object in a specific collection of a given database. The function uses the '_open_db' and '_save_db' functions from the same module to open and save the modified database. The function now handles any errors that may occur during the file operations.

    Inputs:
        - db_name: a string representing the name of the database to delete values from.
        - collection: a string representing the name of the collection to delete values from.
        - obj_name: a string representing the name of the object to delete values from.

    Flow:
        - Open the database with the given name using the '_open_db' function.
        - Check if the given collection and object exist in the database.
        - If they exist, set the 'values' key of the object to None.
        - Save the modified database using the '_save_db' function.

    Outputs:
        - None

    Additional aspects:
        - The function raises a 'DeleteError' exception if an error occurs during the deletion operation.
        - The function handles errors that may occur during the file operations.
        - The function modifies the database in place and does not return a new database object.
    """
    DATABASE = _open_db(db_name=db_name)
    
    if collection in DATABASE and obj_name in DATABASE[collection]:
        try:
            DATABASE[collection][obj_name]['values'] = None
            _save_db(db_name=db_name, DB=DATABASE)
        except Exception as e:
            raise DeleteError(f'Error deleting values: {e}')
