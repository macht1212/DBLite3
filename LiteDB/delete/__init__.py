from LiteDB._funcs import _open_db, _save_db


def delete_value(db_name: str, collection: str, object: str, id: int) -> None:
    """

    :param db_name:
    :param collection:
    :param object:
    :param id:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    if len(DATABASE[collection][object]) == 1:
        DATABASE[collection][object] = None
    else:
        del (DATABASE[collection][object]['value'][id - 1])
    _save_db(db_name=db_name, DB=DATABASE)


def delete_all_values(db_name: str, collection: str, object: str) -> None:
    """

    :param db_name:
    :param collection:
    :param object:
    :return:
    """
    DATABASE = _open_db(db_name=db_name)
    DATABASE[collection][object] = None
    _save_db(db_name=db_name, DB=DATABASE)
