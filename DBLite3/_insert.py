from typing import Any

from DBLite3._funcs import _open_db, _save_db, _is_value_in, _count
from DBLite3._exceptions import InsertError, OpenError, SaveError


def insert_one_in_one_collection(db_name: str, collection: str, obj_name: str, value: Any) -> None:
    """
    Objective:
    The objective of the 'insert_one_in_one' function is to add a single value to a collection in a self. The
    function creates a new list for the value, with a serial number calculated relative to the last serial number of the
    value. The function assumes that the self, collection, and object already exist and does not handle any errors
    that may occur during the self operations.

    Inputs:
        - db_name: a string representing the name of the self to add the value to
        - collection: a string representing the name of the collection to add the value to
        - obj_name: a string representing the name of the object to add the value to
        - value: any type of value to be added to the self

    Flow:
        - Open the self using the '_open_db' function
        - Check if the first entry in the collection exists using the '_is_value_in' function
        - If the first entry does not exist, create a new list for the value with a serial number of 1
        - If the first entry exists, calculate the serial number of the new value relative to the last serial number of
          the value and add it to the list
        - Save the updated self using the '_save_db' function

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the self, collection, and object already exist
        - The function does not handle any errors that may occur during the self operations
    """

    if not isinstance(db_name, str):
        raise KeyError('DB name must be a string')
    if not isinstance(collection, str):
        raise KeyError('Collection name must be a string')
    if not isinstance(obj_name, str):
        raise KeyError('Object name must be a string')

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    if collection not in DATABASE.keys():
        raise KeyError(f'Collection {collection} not found in self')
    if obj_name not in DATABASE[collection].keys():
        raise KeyError(f'Object {obj_name} not found in self')

    count = _count(DATABASE=DATABASE, collection=collection, obj_name=obj_name)

    try:
        if DATABASE[collection][obj_name]['values'] is None:
            DATABASE[collection][obj_name]['values'] = []
            DATABASE[collection][obj_name]['values'].append([count + 1, value])
        else:
            DATABASE[collection][obj_name]['values'].append([(count + 1), value])
    except InsertError as e:
        raise InsertError(f'Error: {e}')

    try:
        _save_db(db_name=db_name, DB=DATABASE)
    except SaveError as e:
        raise SaveError(f'Error: {e}')


def insert_many_in_one_collection(db_name: str, collection: str, obj_name: str, values: list) -> None:
    """
    Objective:
    The objective of the function is to add multiple values to a collection in a given self. The values are added to
     a separate list within the collection, with each value having its own serial number relative to the last serial
     number of the value.

    Inputs:
        - db_name: a string representing the name of the self to add values to
        - collection: a string representing the name of the collection to add values to
        - obj_name: a string representing the name of the object to add values to
        - values: a list of values to be added to the self

    Flow:
        - Open the self using the _open_db function
        - Check if the collection already has values by accessing the 'values' key of the object in the collection
        - If the collection has values, set the count variable to the last serial number of the value
        - If the collection does not have values, set the count variable to 0
        - Check if the first entry in the collection exists using the _is_value_in function
        - If the first entry does not exist, append each value to the 'values' list with a serial number calculated
          relative to the last serial number of the value
        - If the first entry exists, append each value to the 'values' list with a serial number calculated relative to
          the last serial number of the value + 1
        - Save the updated self using the _save_db function

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the 'values' key exists in the object in the collection
        - The function overwrites the existing file with the same name if it already exists
        - The function does not handle any errors that may occur during the file operations
    """
    if not isinstance(db_name, str):
        raise KeyError('DB name must be a string')
    if not isinstance(collection, str):
        raise KeyError('Collection name must be a string')
    if not isinstance(obj_name, str):
        raise KeyError('Object name must be a string')
    if not isinstance(values, list):
        raise KeyError('Values must be a list')

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        print(f'Error: {e}')
        return

    if collection not in DATABASE or obj_name not in DATABASE[collection]:
        raise KeyError(f'Collection {collection} or object {obj_name} not found in self')

    count = _count(DATABASE=DATABASE, collection=collection, obj_name=obj_name)

    try:
        if _is_value_in(DB=DATABASE, collection=collection, obj_name=obj_name):
            for value in list([count + i + 1, values[i]] for i, e in enumerate(values)):
                DATABASE[collection][obj_name]['values'].append(value)
        else:
            DATABASE[collection][obj_name]['values'] = [[1 + i, values[i]] if i == 0 else [count + i + 1, values[i]] for
                                                      i, e in enumerate(values)]
    except InsertError as e:
        raise InsertError(f'Error: {e}')

    try:
        _save_db(db_name=db_name, DB=DATABASE)
    except SaveError as e:
        raise SaveError(f'Error: {e}')

    return


def insert_one_in_many_collections(db_name: str, collections: list, obj_name: str, value: Any) -> None:
    """
    Objective:
    The objective of the 'insert_one_in_many_collections' function is to insert a single value into multiple collections
     and objects in a self. The function takes in the name of the self, a list of collection names, an object
     name, and a value to be inserted.

    Inputs:
        - db_name: a string representing the name of the self to insert the value into
        - collections: a list of strings representing the names of the collections to insert the value into
        - obj_name: a string representing the name of the object to insert the value into
        - value: any type of value to be inserted into the collections and object

    Flow:
        - Open the self using the '_open_db' function
        - For each collection in the list of collections:
            - Check if the collection and object exist in the self
            - Get the count of entries in the collection using the '_count' function
            - If the first entry in the collection exists, append the value to the 'values' key of the object in the
              collection with a new count value
        - Save the updated self using the '_save_db' function

    Outputs:
        - None

    Additional aspects:
        - The function raises a 'KeyError' if the collection or object does not exist in the self
        - The function uses the '_is_value_in' function to check if the first entry in the collection exists
        - The function uses the 'enumerate' function to get the index of each collection in the list of collections
        - The function raises a 'SaveError' if there is an error while saving the updated self
    """
    if not isinstance(db_name, str):
        raise KeyError('DB name must be a string')
    if not isinstance(collections, list):
        raise KeyError('Collection must be a list')
    if not isinstance(obj_name, str):
        raise KeyError('Object must be a string')

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    for collection in collections:

        if collection not in DATABASE or obj_name not in DATABASE[collection]:
            raise KeyError(f'Collection {collection} or object {obj_name} not found in self')

        count = _count(DATABASE=DATABASE, collection=collection, obj_name=obj_name)

        if _is_value_in(DB=DATABASE, collection=collection, obj_name=obj_name):
            DATABASE[collection][obj_name]['values'].append([count + 1, value])
        else:
            DATABASE[collection][obj_name]['values'] = [(1, value)]

    try:
        _save_db(db_name=db_name, DB=DATABASE)
    except SaveError as e:
        raise SaveError(f'Error: {e}')

    return
