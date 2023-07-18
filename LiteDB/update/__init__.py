from LiteDB._funcs import _open_db, _save_db, _get_value_id


# To update values in the database, use the update module, which implements four methods to update data by their ID or
# by their old value.
#
# To update a single value by its ID, you need to import the .update_value_by_id method from the update module.
# (from LiteDB.update import update_value_by_id) In this method, you must pass the name of the database, the name of the
# collection, the name of the object and the identifier of the value to be replaced, as well as the new value.
#
# Example::
#
#     >>> from LiteDB.update import update_value_by_id
#     >>> update_value_by_id(db_name='new', collection='table', object='coll', id=1, value='some new value')
#
# To update a few values by their ID, you need to import the .update_values_by_id method from the update module. (
# from LiteDB.update import update_values_by_id) In this method, you must pass the name of the database, the name of
# the collection, the name of the object and the identifiers of the values (list) to be replaced, as well as the new
# values (list).
#
# Example::
#
#     >>> from LiteDB.update import update_values_by_id
#     >>> update_values_by_id(db_name='new', collection='table', object='coll': str, id=[1, 2],
#                             value=['some new value', 'second new value'])


def update_value_by_id(db_name: str, collection: str, object: str, id: int, value) -> None:
    """
    The function updates the single value by the given identifier
    :param db_name: the name of the database to be modified
    :param collection: the name of the table to be modified
    :param object: the name of the collection to be modified
    :param id: identifier of the value to be modified
    :param value: new value
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    DATABASE[collection][object]['values'][id - 1][1] = value
    _save_db(db_name=db_name, DB=DATABASE)


def update_values_by_id(db_name: str, collection: str, object: str, id: list, values: list) -> None:
    """
    The function updates the many values by the given identifiers
    :param db_name: the name of the database to be modified
    :param collection: the name of the table to be modified
    :param object: the name of the collection to be modified
    :param id: list of identifiers of the values to be modified
    :param values: list of the new values
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    for i, id in enumerate(id):
        DATABASE[collection][object]['values'][id - 1][1] = values[i]
    _save_db(db_name=db_name, DB=DATABASE)


