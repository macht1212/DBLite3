import itertools

from NoSQLite3._funcs import _open_db


def select_all_values_with_index(db_name: str, collection: str, object: str) -> list:
    """
    The function returns a list of all object values with their indices
    :param db_name: the name of the database to retrieve the data from
    :param collection: the name of the collection to retrieve the data from
    :param object: the name of the object to retrieve the data from
    :return: list of values
    """
    DATABASE = _open_db(db_name=db_name)
    return [f'Index: {value[0]}, value: {value[1]}' for value in DATABASE[collection][object]['values']]


def select_all_values_without_index(db_name: str, collection: str, object: str) -> list:
    """
    The function returns a list of all object values without their indices
    :param db_name: the name of the database to retrieve the data from
    :param collection: the name of the collection to retrieve the data from
    :param object: the name of the object to retrieve the data from
    :return: list of values
    """
    DATABASE = _open_db(db_name=db_name)
    return [f'Value: {value[1]}' for value in DATABASE[collection][object]['values']]


def size(db_name: str, collection: str, object: str) -> int:
    """
    The function returns the number of elements in the object
    :param db_name: the name of the database to count the data from
    :param collection: the name of the collection to count the data from
    :param object: the name of the object to count the data from
    :return: int, number of incoming elements
    """
    DATABASE = _open_db(db_name=db_name)
    return len(DATABASE[collection][object]['values'])


def select_all_values_in_collection(db_name: str, collection: str) -> dict:
    """
    The function returns a list of all collection values
    :param db_name: the name of the database to retrieve the data from
    :param collection: the name of the collection to retrieve the data from
    :return: dictionary with objects and their values
    """
    DATABASE = _open_db(db_name=db_name)
    return DATABASE[collection]


# TODO
def gt(db_name: str, collection: str, object: str) -> list:
    pass


# TODO
def lt(db_name: str, collection: str, object: str) -> list:
    pass
