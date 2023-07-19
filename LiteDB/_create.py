from LiteDB._funcs import _open_db, _save_db, _db_exists, _collection_exists, _object_exists
from LiteDB._exceptions import CreationError


def create_db(db_name: str, if_exists: bool = False) -> None:
    """
    The function creates a database in the base directory of the project
    :param  if_exists: an optional parameter responsible for skipping an exception when creating a database with an
            already existing name
    :param  db_name: the name of the database to be created. The name of the database must be unique in the project,
            otherwise the file will be overwritten. Data is passed to the function as a string
    :return: None
    """
    if _db_exists(db_name=db_name) and if_exists:
        pass
    elif _db_exists(db_name=db_name):
        raise CreationError(f'DATABASE with name: {db_name} has already existed')
    else:
        with open(f'./{db_name}.json', 'w') as f:
            f.write('{}')


def create_collection(db_name: str, collection: str, objects: list) -> None:
    """
    The function creates a collection with collections
    :param  db_name: the selected database to create the collection. Data is passed to the function as a string
    :param  collection: collection name. IMPORTANT! The collection name must be unique. Data is passed to the function as a string
    :param  objects: objects names. A collection is similar to a column in a classic relational database, but at
            the same time it does not require a clear fixation of data relative to other such collections. Data is
            passed to the function as a list
    :return: None
    """

    DATABASE = _open_db(db_name=db_name)
    if _collection_exists(collection=collection, DB=DATABASE):
        raise CreationError(f'Collection with name: {collection} has already existed.')
    else:
        DATABASE[collection] = {}
        for o in objects:
            DATABASE[collection][o] = {'values': None}
    _save_db(db_name=db_name, DB=DATABASE)


def create_object(db_name: str, collection: str, object: str) -> None:
    """

    :param db_name:
    :param collection:
    :param object:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    if _object_exists(collection=collection, object=object, DB=DATABASE):
        raise CreationError(f'Object with name: {object} has already existed.')
    else:
        DATABASE[collection][object] = {'values': None}
    _save_db(db_name=db_name, DB=DATABASE)
