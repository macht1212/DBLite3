from typing import Any

from DBLite3._funcs import _open_db, _save_db, _is_value_in, _count
from DBLite3._exceptions import InsertError, OpenError, SaveError


def insert_one_in_one_collection(db_name: str, collection: str, object: str, value: Any) -> None:
    """
    Objective:
    The objective of the 'insert_one_in_one' function is to add a single value to a collection in a database. The function creates a new list for the value, with a serial number calculated relative to the last serial number of the value. The function assumes that the database, collection, and object already exist and does not handle any errors that may occur during the database operations.

    Inputs:
        - db_name: a string representing the name of the database to add the value to
        - collection: a string representing the name of the collection to add the value to
        - object: a string representing the name of the object to add the value to
        - value: any type of value to be added to the database

    Flow:
        - Open the database using the '_open_db' function
        - Check if the first entry in the collection exists using the '_is_value_in' function
        - If the first entry does not exist, create a new list for the value with a serial number of 1
        - If the first entry exists, calculate the serial number of the new value relative to the last serial number of the value and add it to the list
        - Save the updated database using the '_save_db' function

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the database, collection, and object already exist
        - The function does not handle any errors that may occur during the database operations
    """

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    if collection not in DATABASE or object not in DATABASE[collection]:
        raise KeyError(f'Collection {collection} or object {object} not found in database')

    count = _count(DATABASE=DATABASE, collection=collection, object=object)

    try:
        if DATABASE[collection][object]['values'] is None:
            DATABASE[collection][object]['values'] = []
            DATABASE[collection][object]['values'].append((count + 1, value))
        else:
            DATABASE[collection][object]['values'].append((count + 1, value))
    except InsertError as e:
        raise InsertError(f'Error: {e}')

    try:
        _save_db(db_name=db_name, DB=DATABASE)
    except SaveError as e:
        raise SaveError(f'Error: {e}')


def insert_many_in_one_collection(db_name: str, collection: str, object: str, values: list) -> None:
    """
    Objective:
    The objective of the function is to add multiple values to a collection in a given database. The values are added to a separate list within the collection, with each value having its own serial number relative to the last serial number of the value.

    Inputs:
        - db_name: a string representing the name of the database to add values to
        - collection: a string representing the name of the collection to add values to
        - object: a string representing the name of the object to add values to
        - values: a list of values to be added to the database

    Flow:
        - Open the database using the _open_db function
        - Check if the collection already has values by accessing the 'values' key of the object in the collection
        - If the collection has values, set the count variable to the last serial number of the value
        - If the collection does not have values, set the count variable to 0
        - Check if the first entry in the collection exists using the _is_value_in function
        - If the first entry does not exist, append each value to the 'values' list with a serial number calculated relative to the last serial number of the value
        - If the first entry exists, append each value to the 'values' list with a serial number calculated relative to the last serial number of the value + 1
        - Save the updated database using the _save_db function

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the 'values' key exists in the object in the collection
        - The function overwrites the existing file with the same name if it already exists
        - The function does not handle any errors that may occur during the file operations
    """
    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        print(f'Error: {e}')
        return

    if collection not in DATABASE or object not in DATABASE[collection]:
        raise KeyError(f'Collection {collection} or object {object} not found in database')

    count = _count(DATABASE=DATABASE, collection=collection, object=object)

    try:
        if _is_value_in(DB=DATABASE, collection=collection, object=object):
            DATABASE[collection][object]['values'].append([[count + i + 1, values[i]] for i, e in enumerate(values)])
        else:
            DATABASE[collection][object]['values'] = [(1 + i, values[i]) if i == 0 else [count + i + 1, values[i]] for
                                                      i, e in enumerate(values)]
    except InsertError as e:
        raise InsertError(f'Error: {e}')

    try:
        _save_db(db_name=db_name, DB=DATABASE)
    except SaveError as e:
        raise SaveError(f'Error: {e}')

    return


def insert_one_in_many_collections(db_name: str, collections: list, object: str, value: Any) -> None:
    """
    Objective:
    The objective of the 'insert_one_in_many_collections' function is to insert a single value into multiple collections and objects in a database. The function takes in the name of the database, a list of collection names, an object name, and a value to be inserted.

    Inputs:
        - db_name: a string representing the name of the database to insert the value into
        - collections: a list of strings representing the names of the collections to insert the value into
        - object: a string representing the name of the object to insert the value into
        - value: any type of value to be inserted into the collections and object

    Flow:
        - Open the database using the '_open_db' function
        - For each collection in the list of collections:
            - Check if the collection and object exist in the database
            - Get the count of entries in the collection using the '_count' function
            - If the first entry in the collection exists, append the value to the 'values' key of the object in the collection with a new count value
        - Save the updated database using the '_save_db' function

    Outputs:
        - None

    Additional aspects:
        - The function raises a 'KeyError' if the collection or object does not exist in the database
        - The function uses the '_is_value_in' function to check if the first entry in the collection exists
        - The function uses the 'enumerate' function to get the index of each collection in the list of collections
        - The function raises a 'SaveError' if there is an error while saving the updated database
    """
    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        print(f'Error: {e}')
        return

    for i, collection in enumerate(collections):

        if collection not in DATABASE or object not in DATABASE[collection]:
            raise KeyError(f'Collection {collection} or object {object} not found in database')

        count = _count(DATABASE=DATABASE, collection=collection, object=object)

        if _is_value_in(DB=DATABASE, collection=collection, object=object):
            DATABASE[collection][object]['values'].append((count + 1 + i, value))
        else:
            DATABASE[collection][object]['values'] = [(1, value)]

    try:
        _save_db(db_name=db_name, DB=DATABASE)
    except SaveError as e:
        raise SaveError(f'Error: {e}')

    return

