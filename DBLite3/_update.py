from typing import Any

from DBLite3._funcs import _open_db, _save_db, _get_value_index


def update_value_by_id(db_name: str, collection: str, object: str, id: int, value: Any) -> None:
    """
    The function updates the single value by the given identifier
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be modified
    :param object: the name of the object to be modified
    :param id: identifier of the value to be modified
    :param value: new value
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    index = _get_value_index(db_name=db_name, collection=collection, object=object, id=id)
    DATABASE[collection][object]['values'][index][1] = value
    _save_db(db_name=db_name, DB=DATABASE)


def update_values_by_id(db_name: str, collection: str, object: str, id: list, values: list) -> None:
    """
    The function updates the many values by the given identifiers
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be modified
    :param object: the name of the object to be modified
    :param id: list of identifiers of the values to be modified
    :param values: list of the new values
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    for i, id in enumerate(id):
        index = _get_value_index(db_name=db_name, collection=collection, object=object, id=id)
        DATABASE[collection][object]['values'][index][1] = values[i]
    _save_db(db_name=db_name, DB=DATABASE)
