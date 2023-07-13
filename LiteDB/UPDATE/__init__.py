from LiteDB._funcs import _open_db, _save_db


# To update values in the database, use the update module, which implements four methods to update data by their ID or
# by their old value.
#
# To update a single value by its ID, you need to import the .update_value_by_id method from the UPDATE module.
# (from LiteDB.UPDATE import update_value_by_id) In this method, you must pass the name of the database, the name of the
# table, the name of the collection and the identifier of the value to be replaced, as well as the new value.
#
# Example::
#
#     >>> from LiteDB.UPDATE import update_value_by_id
#     >>> update_value_by_id(db_name='new', table_name='table', collection='coll', id=1, value='some new value')
#
# To update a few values by their ID, you need to import the .update_values_by_id method from the UPDATE module. (
# from LiteDB.UPDATE import update_values_by_id) In this method, you must pass the name of the database, the name of
# the table, the name of the collection and the identifiers of the values (list) to be replaced, as well as the new
# values (list).
#
# Example::
#
#     >>> from LiteDB.UPDATE import update_values_by_id
#     >>> update_values_by_id(db_name='new', table_name='table', collection='coll', id=[1, 2],
#                             value=['some new value', 'second new value'])
#
# To update a single value by its old name, you need to import the .update_new_value_by_old_value method from the UPDATE
# module. (from LiteDB.UPDATE import update_new_value_by_old_value) In this method, you must pass the name of the
# database, the name of the table, the name of the collection and the old name of the value to be replaced, as well as
# the new value.
#
# Example::
#
#     >>> from LiteDB.UPDATE import update_new_value_by_old_value
#     >>> update_value_by_id(db_name='new', table_name='table', collection='coll',
#                             old_value='old', new_value='some new value')
#
# To update a few values by their old names, you need to import the .update_new_values_by_old_values method from the
# UPDATE module. (from LiteDB.UPDATE import update_new_values_by_old_values) In this method, you must pass the name of
# the database, the name of the table, the name of the collection and the old names of the values (list) to be replaced,
# as well as the new values (list).
#
# Example::
#
#     >>> from LiteDB.UPDATE import update_new_values_by_old_values
#     >>> update_new_values_by_old_values(db_name='new', table_name='table', collection='coll',
#                             old_value=['old1', 'old2'], new_value=['some new value', 'second new value'])


def update_value_by_id(db_name: str, table_name: str, collection: str, id: int, value) -> None:
    """
    The function updates the single value by the given identifier
    :param db_name: the name of the database to be modified
    :param table_name: the name of the table to be modified
    :param collection: the name of the collection to be modified
    :param id: identifier of the value to be modified
    :param value: new value
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    DATABASE[table_name][collection]['values'][id - 1][1] = value
    _save_db(db_name=db_name, DB=DATABASE)


def update_values_by_id(db_name: str, table_name: str, collection: str, id: list, values: list) -> None:
    """
    The function updates the many values by the given identifiers
    :param db_name: the name of the database to be modified
    :param table_name: the name of the table to be modified
    :param collection: the name of the collection to be modified
    :param id:
    :param values:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    for i, id in enumerate(id):
        DATABASE[table_name][collection]['values'][id - 1][1] = values[i]
    _save_db(db_name=db_name, DB=DATABASE)


def update_new_value_by_old_value(db_name: str, table_name: str, collection: str, old_value, new_value) -> None:
    """

    :param db_name:
    :param table_name:
    :param collection:
    :param old_value:
    :param new_value:
    :return:
    """
    pass


def update_new_values_by_old_values(db_name: str, table_name: str, collection: str, values: list) -> None:
    """

    :param db_name:
    :param table_name:
    :param collection:
    :param values:
    :return:
    """
    pass
