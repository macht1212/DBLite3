from LiteDB.INSERT.INSERT import _value_in
from LiteDB._funcs import _open_db, _save_db


def insert_one(db_name: str, table_name: str, collection: str, value) -> None:
    """
    The function adds one value to the collection, the value is entered into a separate list, which has its own serial
    number, calculated relative to the last serial number of the value.
    :param collection: The name of the collection to add the value to
    :param table_name: The name of the table to add the value to
    :param db_name: The name of the database to add the value to
    :param value: The value to be entered into the database
    :return: None
    """

    DATABASE = _open_db(db_name=db_name)
    if _value_in(DATABASE=DATABASE, table_name=table_name, collection=collection):
        DATABASE[table_name][collection]['values'] = [(1, value)]
    else:
        count = DATABASE[table_name][collection]['values'][-1][0]
        DATABASE[table_name][collection]['values'].append((count + 1, value))

    _save_db(db_name=db_name, DB=DATABASE)


def insert_many(db_name: str, table_name: str, collection: str, values: list) -> None:
    DATABASE = _open_db(db_name=db_name)
    if _value_in(DATABASE=DATABASE, table_name=table_name, collection=collection):
        for i, e in enumerate(values):
            DATABASE[table_name][collection]['values'] = [(1 + i, values[i])]
    else:
        count = DATABASE[table_name][collection]['values'][-1][0]
