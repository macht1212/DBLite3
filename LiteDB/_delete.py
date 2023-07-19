from LiteDB._funcs import _open_db, _save_db, _get_value_index


def delete_value(db_name: str, collection: str, object: str, id: int) -> None:
    """
    The function deletes a value by its index
    :param db_name: The name of the database to delete values to
    :param collection: The name of the collection to delete values to
    :param object: The name of the object to delete values to
    :param id: ID of the value to delete
    :return: None
    """
    index = _get_value_index(db_name=db_name, collection=collection, object=object, id=id)
    DATABASE = _open_db(db_name=db_name)
    if len(DATABASE[collection][object]['values']) == 1:
        DATABASE[collection][object]['values'] = None
    else:
        del (DATABASE[collection][object]['values'][index])
    _save_db(db_name=db_name, DB=DATABASE)


def delete_all_values(db_name: str, collection: str, object: str) -> None:
    """
    The function deletes all values from database
    :param db_name: The name of the database to delete values to
    :param collection: The name of the collection to delete values to
    :param object: The name of the object to delete values to
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    DATABASE[collection][object]['values'] = None
    _save_db(db_name=db_name, DB=DATABASE)
