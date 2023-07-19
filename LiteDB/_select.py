import itertools

from LiteDB._funcs import _open_db


def select_all_values_with_index(db_name: str, collection: str, object: str) -> list:
    """

    :param db_name:
    :param collection:
    :param object:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    return [f'Index: {value[0]}, value: {value[1]}' for value in DATABASE[collection][object]['values']]


def select_all_values_without_index(db_name: str, collection: str, object: str) -> list:
    """

    :param db_name:
    :param collection:
    :param object:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    return [f'Value: {value[1]}' for value in DATABASE[collection][object]['values']]


# TODO
def select_first_five_elements(db_name: str, collection: str, object: str) -> None:
    """

    :param db_name:
    :param collection:
    :param object:
    :return:
    """
    pass


# TODO
def size(db_name: str, collection: str, object: str) -> int:
    """

    :param db_name:
    :param collection:
    :param object:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    return len(DATABASE[collection][object]['values'])


# TODO
def gt(db_name: str, collection: str, object: str, ) -> list:
    pass


# TODO
def lt(db_name: str, collection: str, object: str, ) -> list:
    pass


def select_all_values_in_collection(db_name: str, collection: str) -> dict:
    """

    :param db_name:
    :param collection:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    return DATABASE[collection]
