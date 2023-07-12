
from LiteDB._funcs import _open_db, _save_db


def insert_one(db_name: str, table_name: str, collection: str, value) -> None:
    """

    :param collection:
    :param table_name:
    :param db_name:
    :param value:
    :return:
    """

    DATABASE = _open_db(db_name=db_name)
    if not DATABASE[table_name][collection]['values']:
        DATABASE[table_name][collection]['values'] = [(1, value)]
    else:
        count = DATABASE[table_name][collection]['values'][-1][0]
        DATABASE[table_name][collection]['values'].append((count+1, value))

    _save_db(db_name=db_name, DB=DATABASE)


def insert_many(db_name: str, table_name: str, collection: str, values: list) -> None:
    DATABASE = _open_db(db_name=db_name)
    pass
