import os
import json
from DBLite3._funcs import _open_db, _save_db, _db_exists, _does_collection_exists, _object_exists
from DBLite3._exceptions import CreationError, SaveError, OpenError


def create_db(db_name: str, if_exists: bool = False) -> None:
    """
    Objective:
    The objective of the create_db function is to create a new database in the base directory of the project. The function takes in the name of the database as a string and an optional boolean parameter if_exists, which is responsible for skipping an exception when creating a database with an already existing name.

    Inputs:
        - db_name (str): the name of the database to be created. The name of the database must be unique in the project, otherwise the file will be overwritten.
        - if_exists (bool): an optional parameter responsible for skipping an exception when creating a database with an already existing name.

    Flow:
        - The function first checks if the database already exists using the _db_exists function.
        - If the database exists and if_exists is True, the function does nothing and returns None.
        - If the database exists and if_exists is False, the function raises a CreationError with a message indicating that the database already exists.
        - If the database does not exist, the function creates a new JSON file with the name of the database and writes an empty dictionary to it.

    Outputs:
        - None: the function does not return anything.

    Additional aspects:
        - The function uses the _db_exists function to check if the database already exists.
        - The function raises a CreationError if the database already exists and if_exists is False.
        - The function writes an empty dictionary to the new JSON file to initialize it.
        - The function assumes that the database is stored in a JSON file with the same name as the database name.
    """
    try:
        if not isinstance(db_name, str) or not db_name:
            raise ValueError('db_name must be a non-empty string')

        file_path = os.path.join(db_name + '.json')

        if _db_exists(db_name=db_name) and if_exists:
            pass
        elif _db_exists(db_name=db_name):
            raise CreationError(f'DATABASE with name: {db_name} has already existed')
        else:
            try:
                with open(file_path, 'w') as f:
                    json.dump({}, f)
            except IOError as e:
                raise CreationError(f'Error creating database: {e}')
        return
    except CreationError as e:
        raise CreationError(f'Error: {e}')


def create_collection(db_name: str, collection: str, obj_name: list) -> None:
    """
    Objective:
    The objective of the create_collection function is to create a new collection in a given database with a unique name and a list of objects. The function checks if the collection already exists and raises an error if it does. Otherwise, it creates a new collection with the given objects and saves it to the database.

    Inputs:
        - db_name: a string representing the name of the database where the collection will be created.
        - collection: a string representing the name of the new collection to be created.
        - obj_name: a list of strings representing the names of the objects to be added to the new collection.

    Flow:
        - The function opens the database with the given name using the _open_db function.
        - The function checks if the collection already exists in the database using the _does_collection_exists function. If it does, the function raises a CreationError.
        - If the collection does not exist, the function creates a new collection in the database with the given name and objects.
        - The function saves the updated database using the _save_db function.

    Outputs:
        - None: the function does not return anything.

    Additional aspects:
        - The function assumes that the database already exists and has been parsed into a dictionary.
        - The function only creates a new collection and does not perform any other operations on it.
        - The function overwrites the existing database file with the updated version.
        - The function raises ValueErrors if the inputs are not of the expected type or format.
    """
    try:
        if not isinstance(collection, str) or not collection:
            raise ValueError('collection must be a non-empty string')
        if not isinstance(obj_name, list) or not obj_name:
            raise ValueError('objects must be a non-empty list')

        try:
            DATABASE = _open_db(db_name=db_name)
        except OpenError as e:
            raise OpenError(f'Error: {e}')

        if len(set(obj_name)) != len(obj_name):
            raise ValueError('objects parameter must contain only unique values')

        if _does_collection_exists(collection=collection, DB=DATABASE):
            raise CreationError(f'Collection with name: {collection} has already existed.')
        else:
            DATABASE[collection] = {}
            for o in obj_name:
                DATABASE[collection][o] = {'values': None}
        try:
            _save_db(db_name=db_name, DB=DATABASE)
        except SaveError as e:
            raise SaveError(f'Error {e}')

    except CreationError as e:
        raise CreationError(f'Error: {e}')


def create_collections(db_name: str, collections: list, obj_name: list) -> None:
    """
    Objective:
    The objective of the function is to create collections in a parsed database. The function takes in the name of the database, a list of collection names, and a list of object names. The function creates a new collection for each name in the collection list and adds objects to each collection.
    
    Inputs:
        - db_name: a string representing the name of the database to create the collection in.
        - collections: a list of strings representing the names of the collections to be created.
        - obj_name: a list of strings representing the names of the objects to be added to each collection.
    
    Flow:
        - The function opens the parsed database using the _open_db function.
        - For each collection name in the collections list, the function checks if the collection already exists in the database using the _does_collection_exists function.
        - If the collection does not exist, the function creates a new collection with the given name in the database and adds objects to it.
        - The function saves the updated database using the _save_db function.
    
    Outputs:
        - None: the function does not return anything.
    
    Additional aspects:
        - The function raises a CreationError if a collection with the same name already exists in the database.
        - The function assumes that the database has already been parsed and is represented as a dictionary.
        - The function only creates collections and does not perform any other operations on them.
    """
    try:
        if not isinstance(collections, list):
            raise TypeError('collections parameter must be a list')
        if not isinstance(obj_name, list):
            raise TypeError('objects parameter must be a list')

        try:
            DATABASE = _open_db(db_name=db_name)
        except OpenError as e:
            raise OpenError(f'Error: {e}')

        if not collections or not obj_name:
            raise ValueError('collections and objects must not be empty')

        for collection in collections:
            if not isinstance(collection, str):
                raise TypeError('Collection name must be a string')
            if _does_collection_exists(collection=collection, DB=DATABASE):
                raise CreationError(f'Collection with name: {collection} has already existed.')
            else:
                DATABASE[collection] = {}
                for o in obj_name:
                    if not isinstance(o, str):
                        raise TypeError('Object name must be a string')
                    DATABASE[collection][o] = {'values': None}

        try:
            _save_db(db_name=db_name, DB=DATABASE)
        except SaveError as e:
            raise SaveError(f'Error creating collection: {e}')
        return

    except CreationError as e:
        raise CreationError(f'Error: {e}')


def create_object(db_name: str, collection: str, obj_name: str) -> None:
    """
    Objective:
    The objective of the function is to create a new object in a specified collection of a given database. The function checks if the object already exists in the collection and raises an error if it does. Otherwise, it adds the object to the collection with an empty 'values' field and saves the updated database.

    Inputs:
        - db_name: a string representing the name of the database to which the object is to be added.
        - collection: a string representing the name of the collection in which the object is to be added.
        - obj_name: a string representing the name of the object to be added.

    Flow:
        - The function first opens the database using the _open_db function.
        - It then checks if the object already exists in the specified collection using the _object_exists function. If it does, the function raises a CreationError with an appropriate message.
        - If the object does not exist, the function adds the object to the collection with an empty 'values' field.
        - Finally, the updated database is saved using the _save_db function.

    Outputs:
        - None: the function does not return anything.

    Additional aspects:
        - The function assumes that the database already exists and has been parsed into a dictionary format.
        - The function only adds the object to a single collection and does not check for the existence of the collection itself.
        - The function does not handle any errors that may occur during the file operations.
    """
    try:
        if not isinstance(db_name, str) or not db_name:
            raise ValueError('db_name must be a non-empty string')
        if not isinstance(collection, str) or not collection:
            raise ValueError('collection must be a non-empty string')
        if not isinstance(obj_name, str) or not obj_name:
            raise ValueError('object must be a non-empty string')

        try:
            DATABASE = _open_db(db_name=db_name)
        except OpenError as e:
            raise OpenError(f'Error: {e}')

        if collection not in DATABASE:
            raise ValueError(f'Collection {collection} does not exist in the database.')

        if _object_exists(collection=collection, obj_name=obj_name, DB=DATABASE):
            raise CreationError(f'Object with name: {obj_name} has already existed.')
        else:
            DATABASE[collection][obj_name] = {'values': None}

        try:
            _save_db(db_name=db_name, DB=DATABASE)
        except SaveError as e:
            raise SaveError(f'Error creating collection: {e}')

    except CreationError as e:
        raise CreationError(f'Error creating object: {e}')
