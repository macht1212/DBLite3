from DBLite3._exceptions import SelectError
from DBLite3._funcs import _open_db


def select_all_values_with_index(db_name: str, collection: str, object: str) -> list:
    """
    Objective:
    The objective of the function is to retrieve all values of a specific object in a collection from a given database and return them as a list with their corresponding indices.

    Inputs:
        - db_name: a string representing the name of the database to retrieve the data from.
        - collection: a string representing the name of the collection to retrieve the data from.
        - object: a string representing the name of the object to retrieve the data from.

    Flow:
        - Call the _open_db function to retrieve the database dictionary object.
        - Check if the collection and object exist in the database.
        - Return a list of all values of the object with their corresponding indices.

    Outputs:
        - A list of strings representing the values of the object with their corresponding indices.

    Additional aspects:
        - The function raises a ValueError if the database file does not exist.
        - The function raises a KeyError if the collection or object do not exist in the database.
        - The function uses the _open_db function from the same module to retrieve the database dictionary object.
    """
    try:
        DATABASE = _open_db(db_name=db_name)
    except FileNotFoundError:
        raise ValueError(f'{db_name}.json does not exist')

    if collection not in DATABASE:
        raise KeyError(f'Collection {collection} does not exist in the database')
    if object not in DATABASE[collection]:
        raise KeyError(f'Object {object} does not exist in collection {collection}')

    return [f'Index: {value[0]}, value: {value[1]}' for value in DATABASE[collection][object]['values']]


def select_all_values_without_index(db_name: str, collection: str, object: str) -> list:
    """
    Objective:
    The objective of the function is to retrieve all values of a given object in a collection from a specified database and return them as a list without their indices.

    Inputs:
        - db_name: a string representing the name of the database to retrieve the data from.
        - collection: a string representing the name of the collection to retrieve the data from.
        - object: a string representing the name of the object to retrieve the data from.

    Flow:
        - Call the _open_db function to retrieve the database.
        - Check if the specified collection and object exist in the database.
        - Retrieve all values of the specified object from the collection.
        - Return a list of values without their indices.

    Outputs:
        - A list of values without their indices.

    Additional aspects:
        - The function raises a ValueError if the specified database does not exist.
        - The function raises a KeyError if the specified collection or object does not exist in the database.
    """
    try:
        DATABASE = _open_db(db_name=db_name)
    except FileNotFoundError:
        raise ValueError(f'{db_name}.json does not exist')

    if collection not in DATABASE:
        raise KeyError(f'Collection {collection} does not exist in the database')
    if object not in DATABASE[collection]:
        raise KeyError(f'Object {object} does not exist in collection {collection}')

    return [f'Value: {value[1]}' for value in DATABASE[collection][object]['values']]


def size(db_name: str, collection: str, object: str) -> int:
    """
    Objective:
    The objective of the "size" function is to return the number of elements in a specified object of a specified collection in a specified database.
    
    Inputs:
        - db_name: a string representing the name of the database to count the data from.
        - collection: a string representing the name of the collection to count the data from.
        - object: a string representing the name of the object to count the data from.
    
    Flow:
        - Call the "_open_db" function to open the specified database.
        - Check if the specified collection and object exist in the database.
        - Return the number of elements in the specified object.
    
    Outputs:
        - An integer representing the number of elements in the specified object.
    
    Additional aspects:
        - The function raises a ValueError if the specified collection or object does not exist in the database.
        - The function uses the "_open_db" function to open the database and returns the number of elements in the specified object.
    """
    with _open_db(db_name=db_name) as DATABASE:
        if collection not in DATABASE or object not in DATABASE[collection]:
            raise ValueError('Invalid collection or object name')
        return len(DATABASE[collection][object]['values'])


def select_all_values_in_collection(db_name: str, collection: str) -> dict:
    """
    Objective:
    The objective of the function is to retrieve all values from a specified collection in a given database and return them as a dictionary with object IDs as keys and object values as values.

    Inputs:
        - db_name: a string representing the name of the database to retrieve data from.
        - collection: a string representing the name of the collection to retrieve data from.

    Flow:
        - Check if the input parameters are valid strings.
        - Call the _open_db function to retrieve the database object.
        - Iterate over the objects in the specified collection and create a dictionary with object IDs as keys and object values as values.
        - Return the dictionary.

    Outputs:
        - A dictionary with object IDs as keys and object values as values.

    Additional aspects:
        - The function raises a ValueError if the input parameters are not valid strings.
        - The function raises a ValueError if there is an error retrieving data from the specified collection in the given database.
    """
    try:
        if not isinstance(db_name, str) or not db_name:
            raise ValueError('db_name must be a non-empty string')
        if not isinstance(collection, str) or not collection:
            raise ValueError('collection must be a non-empty string')
        DATABASE = _open_db(db_name=db_name)
        return {obj['id']: obj for obj in DATABASE[collection]}
    except (FileNotFoundError, KeyError) as e:
        raise ValueError(f'Error retrieving data from {collection} in {db_name}: {e}')


# TODO
def gt(db_name: str, collection: str, object: str) -> list:
    pass


# TODO
def lt(db_name: str, collection: str, object: str) -> list:
    pass
