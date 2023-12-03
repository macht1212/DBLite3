import numbers
from typing import Any

from DBLite3._exceptions import SelectError, OpenError
from DBLite3._funcs import _open_db, _is_value_in, _object_exists, _collection_exists


def select_all_values_with_index(db_name: str, collection: str, obj_name: str) -> dict:
    """
    Objective:
    The objective of the function is to retrieve all values of a specific object in a collection from a given self and return them as a list with their corresponding indices.

    Inputs:
        - db_name: a string representing the name of the self to retrieve the data from.
        - collection: a string representing the name of the collection to retrieve the data from.
        - obj_name: a string representing the name of the object to retrieve the data from.

    Flow:
        - Call the _open_db function to retrieve the self dictionary object.
        - Check if the collection and object exist in the self.
        - Return a list of all values of the object with their corresponding indices.

    Outputs:
        - A list of strings representing the values of the object with their corresponding indices.

    Additional aspects:
        - The function raises a ValueError if the self file does not exist.
        - The function raises a KeyError if the collection or object do not exist in the self.
        - The function uses the _open_db function from the same module to retrieve the self dictionary object.
    """
    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError:
        raise OpenError(f'{db_name}.json does not exist')

    if collection not in DATABASE:
        raise KeyError(f'Collection {collection} does not exist in the self')
    if obj_name not in DATABASE[collection]:
        raise KeyError(f'Object {obj_name} does not exist in collection {collection}')

    if not _collection_exists(collection=collection, DB=DATABASE):
        raise SelectError(f'Collection {collection} does not exist in Database.')
    if not _object_exists(collection=collection, obj_name=obj_name, DB=DATABASE):
        raise SelectError(f'Object {obj_name} does not exist in Database.')

    return {{value[0]}: value[1] for value in DATABASE[collection][obj_name]['values']}


def select_all_values_without_index(db_name: str, collection: str, obj_name: str) -> list:
    """
    Objective:
    The objective of the function is to retrieve all values of a given object in a collection from a specified self and return them as a list without their indices.

    Inputs:
        - db_name: a string representing the name of the self to retrieve the data from.
        - collection: a string representing the name of the collection to retrieve the data from.
        - obj_name: a string representing the name of the object to retrieve the data from.

    Flow:
        - Call the _open_db function to retrieve the self.
        - Check if the specified collection and object exist in the self.
        - Retrieve all values of the specified object from the collection.
        - Return a list of values without their indices.

    Outputs:
        - A list of values without their indices.

    Additional aspects:
        - The function raises a ValueError if the specified self does not exist.
        - The function raises a KeyError if the specified collection or object does not exist in the self.
    """
    try:
        DATABASE = _open_db(db_name=db_name)
    except FileNotFoundError:
        raise ValueError(f'{db_name}.json does not exist')

    if collection not in DATABASE:
        raise KeyError(f'Collection {collection} does not exist in the self')
    if obj_name not in DATABASE[collection]:
        raise KeyError(f'Object {obj_name} does not exist in collection {collection}')

    return [value[1] for value in DATABASE[collection][obj_name]['values']]


def size(db_name: str, collection: str, obj_name: str) -> int:
    """
    Objective:
    The objective of the "size" function is to return the number of elements in a specified object of a specified collection in a specified self.
    
    Inputs:
        - db_name: a string representing the name of the self to count the data from.
        - collection: a string representing the name of the collection to count the data from.
        - obj_name: a string representing the name of the object to count the data from.
    
    Flow:
        - Call the "_open_db" function to open the specified self.
        - Check if the specified collection and object exist in the self.
        - Return the number of elements in the specified object.
    
    Outputs:
        - An integer representing the number of elements in the specified object.
    
    Additional aspects:
        - The function raises a ValueError if the specified collection or object does not exist in the self.
        - The function uses the "_open_db" function to open the self and returns the number of elements in the specified object.
    """
    with _open_db(db_name=db_name) as DATABASE:
        if collection not in DATABASE or obj_name not in DATABASE[collection]:
            raise ValueError('Invalid collection or object name')
        return len(DATABASE[collection][obj_name]['values'])


def select_all_values_in_collection(db_name: str, collection: str) -> dict:
    """
    Objective:
    The objective of the function is to retrieve all values from a specified collection in a given self and return them as a dictionary with object IDs as keys and object values as values.

    Inputs:
        - db_name: a string representing the name of the self to retrieve data from.
        - collection: a string representing the name of the collection to retrieve data from.

    Flow:
        - Check if the input parameters are valid strings.
        - Call the _open_db function to retrieve the self object.
        - Iterate over the objects in the specified collection and create a dictionary with object IDs as keys and object values as values.
        - Return the dictionary.

    Outputs:
        - A dictionary with object IDs as keys and object values as values.

    Additional aspects:
        - The function raises a ValueError if the input parameters are not valid strings.
        - The function raises a ValueError if there is an error retrieving data from the specified collection in the given self.
    """
    if not isinstance(db_name, str) or not db_name:
        raise ValueError('db_name must be a non-empty string')
    if not isinstance(collection, str) or not collection:
        raise ValueError('collection must be a non-empty string')

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    return {obj: obj['values'] for obj in DATABASE[collection]}


def select_value_by_id_with_index(db_name: str, collection: str, obj_name: str, id: int) -> dict:
    """
    Objective:
    The objective of the function is to select a value from a specific collection and object in a self dictionary based on the given ID. The function returns the value and its index in the form of a string.

    Inputs:
        - db_name: a string representing the name of the self to be searched
        - collection: a string representing the name of the collection to be searched
        - obj_name: a string representing the name of the object to be searched
        - id: an integer representing the ID of the value to be selected

    Flow:
        - Check if the input parameters are of the correct type
        - Open the self using the _open_db function
        - Check if the object is empty or if the ID is greater than the length of the values list
        - If the object is not empty and the ID is valid, select the value and its index from the values list
        - Return the value and its index in the form of a string

    Outputs:
        - A string containing the selected value and its index

    Additional aspects:
        - The function raises custom exceptions if there are errors during the selection process
        - The function assumes that the values list exists in the object in the collection
        - The function assumes that the ID is a valid index in the values list
    """
    if not isinstance(db_name, str):
        raise KeyError('DB name must be a string.')
    if not isinstance(collection, str):
        raise KeyError('Collection name must be a string.')
    if not isinstance(obj_name, str):
        raise KeyError('Object name must be a string.')
    if not isinstance(id, int):
        raise KeyError('Target must be numeric.')

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    if not _is_value_in(DB=DATABASE, collection=collection, obj_name=obj_name):
        raise SelectError("Object is empty.")
    elif id > len(DATABASE[collection][obj_name]['values']) + 1:
        raise SelectError("Length of values less then id number.")
    else:
        return {obj_name:
            {
                'index': DATABASE[collection][obj_name]['values'][id - 1][0],
                'value': DATABASE[collection][obj_name]['values'][id - 1][1]
            }
        }


def select_value_by_id_without_index(db_name: str, collection: str, obj_name: str, id: int) -> dict:
    """
    Objective:
    The objective of the select_value_by_id_without_index function is to select a value from a specific collection and object in a self dictionary based on the given ID. The function returns the value and its index in the form of a string. The function raises custom exceptions if there are errors during the selection process.

    Inputs:
        - db_name: a string representing the name of the self to be searched
        - collection: a string representing the name of the collection to be searched
        - obj_name: a string representing the name of the object to be searched
        - id: an integer representing the ID of the value to be selected

    Flow:
        - The function checks if the input parameters are of the correct type.
        - The function opens the self using the _open_db function.
        - The function checks if the object is empty or if the ID is greater than the length of the values list.
        - If the object is not empty and the ID is valid, the function selects the value and its index from the values list.
        - The function returns the value and its index in the form of a string.

    Outputs:
        - A string containing the selected value and its index.

    Additional aspects:
        - The function assumes that the values list exists in the object in the collection.
        - The function assumes that the ID is a valid index in the values list.
    """
    if not isinstance(db_name, str):
        raise KeyError('DB name must be a string.')
    if not isinstance(collection, str):
        raise KeyError('Collection name must be a string.')
    if not isinstance(obj_name, str):
        raise KeyError('Object name must be a string.')
    if not isinstance(id, int):
        raise KeyError('Target must be numeric.')

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    if not _is_value_in(DB=DATABASE, collection=collection, obj_name=obj_name):
        raise SelectError("Object is empty.")
    elif id > len(DATABASE[collection][obj_name]['values']) + 1:
        raise SelectError("Length of values less then id number.")
    else:
        return {obj_name:
            {
                'value': DATABASE[collection][obj_name]['values'][id - 1][1]
            }
        }


def gt(db_name: str, collection: str, obj_name: str, target: numbers.Number) -> list:
    """
    Objective:
    The 'gt' function aims to retrieve a list of values and their indices from a specific collection and object in a self dictionary, where the value is greater than a given target value. The function also checks if the retrieved values are numeric and raises a custom SelectError if they are not.

    Inputs:
        - db_name: a string representing the name of the self to retrieve the values from.
        - collection: a string representing the name of the collection to retrieve the values from.
        - obj_name: a string representing the name of the object to retrieve the values from.
        - target: an integer or float representing the target value to compare the retrieved values to.

    Flow:
        - The function first checks if the input parameters are valid.
        - The function then tries to open the self using the '_open_db' function and checks if the first value in the collection is numeric using the '_is_value_in' function.
        - If the first value is not numeric, the function raises a SelectError.
        - The function then retrieves a list of values and their indices from the specified collection and object in the self dictionary where the value is greater than the target value.
        - The retrieved values and indices are returned as a list of lists.

    Outputs:
        - A list of lists containing the retrieved values and their indices where the value is greater than the target value.

    Additional aspects:
        - The function raises an OpenError if there is an issue opening the self.
        - The function raises a SelectError if the retrieved values are not numeric.
        - The function assumes that the specified collection and object exist in the self dictionary.
    """

    if not isinstance(db_name, str):
        raise KeyError('DB name must be a string.')
    if not isinstance(collection, str):
        raise KeyError('Collection name must be a string.')
    if not isinstance(obj_name, str):
        raise KeyError('Object name must be a string.')
    if not isinstance(target, numbers.Number):
        raise KeyError('Target must be numeric.')

    try:
        DATABASE = _open_db(db_name=db_name)

        if _is_value_in(DB=DATABASE, collection=collection, obj_name=obj_name):
            for value in DATABASE[collection][obj_name]['values']:
                if not isinstance(value[1], numbers.Number):
                    raise SelectError('This method is allowed only for numeric values.')
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    return [[f'Value: {v[1]}, index: {v[0]}'] for v in DATABASE[collection][obj_name]['values'] if v[1] > target]


def lt(db_name: str, collection: str, obj_name: str, target: numbers.Number) -> list:
    """
    Objective:
    The objective of the 'lt' function is to return a list of values and their indices from a specific collection and object in a self that are less than a given target value. The function also performs input validation and checks if the values in the collection are numeric.

    Inputs:
        - db_name: a string representing the name of the self to be queried.
        - collection: a string representing the name of the collection to be queried.
        - obj_name: a string representing the name of the object to be queried.
        - target: a numeric value representing the target value to compare the values in the collection against.

    Flow:
        - The function performs input validation to ensure that the inputs are of the correct type.
        - The function opens the self using the '_open_db' function and checks if the first value in the collection is numeric using the '_is_value_in' function.
        - The function returns a list of values and their indices from the collection and object that are less than the target value.

    Outputs:
        - A list of values and their indices from the collection and object that are less than the target value.

    Additional aspects:
        - The function raises a 'KeyError' if any of the inputs are of the incorrect type.
        - The function raises a 'SelectError' if the values in the collection are not numeric.
        - The function uses the '_open_db' and '_is_value_in' functions to access the self and check the values in the collection.
        - The function assumes that the 'values' key exists in the object in the collection.
    """
    if not isinstance(db_name, str):
        raise KeyError('DB name must be a string.')
    if not isinstance(collection, str):
        raise KeyError('Collection name must be a string.')
    if not isinstance(obj_name, str):
        raise KeyError('Object name must be a string.')
    if not isinstance(target, numbers.Number):
        raise KeyError('Target must be numeric.')

    try:
        DATABASE = _open_db(db_name=db_name)

        if _is_value_in(DB=DATABASE, collection=collection, obj_name=obj_name):
            for value in DATABASE[collection][obj_name]['values']:
                if not isinstance(value[1], numbers.Number):
                    raise SelectError('This method is allowed only for numeric values.')
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    return [[f'Value: {v[1]}, index: {v[0]}'] for v in DATABASE[collection][obj_name]['values'] if v[1] < target]


def select_values_from_similar_objects_in_collections(db_name: str, obj_name: str) -> Any:
    if not isinstance(db_name, str):
        raise KeyError('DB name must be a string.')
    if not isinstance(obj_name, str):
        raise KeyError('Object name must be a string.')

    try:
        DATABASE = _open_db(db_name=db_name)
    except OpenError as e:
        raise OpenError(f'Error: {e}')

    collections = DATABASE.keys()

    answer = []

    for collection in collections:
        if obj_name in DATABASE[collection].keys():
            answer.append({obj_name: DATABASE[collection][obj_name]['values']})
        else:
            answer.append({obj_name: 'None'})

    return answer

# def select
