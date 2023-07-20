from DBLite3._funcs import _open_db, _save_db, _is_value_in


def insert_one(db_name: str, collection: str, object: str, value) -> None:
    """
    The function adds one value to the collection, the value is entered into a separate list, which has its own serial
    number, calculated relative to the last serial number of the value
    :param object: The name of the object to add the value to
    :param collection: The name of the collection to add the value to
    :param db_name: The name of the database to add the value to
    :param value: The value to be entered into the database
    :return: None
    """

    DATABASE = _open_db(db_name=db_name)
    if _is_value_in(DATABASE=DATABASE, collection=collection, object=object):
        DATABASE[collection][object]['values'] = [(1, value)]
    else:
        count = DATABASE[collection][object]['values'][-1][0]
        DATABASE[collection][object]['values'].append((count + 1, value))

    _save_db(db_name=db_name, DB=DATABASE)


def insert_many(db_name: str, collection: str, object: str, values: list) -> None:
    """
    The function adds many values to the collection, the value is entered into a separate list, which has its own serial
    number, calculated relative to the last serial number of the value.
    :param db_name: The name of the database to add values to
    :param collection: The name of the collection to add values to
    :param object: The name of the object to add values to
    :param values: The values to be entered into the database
    :return: None
    """
    DATABASE = _open_db(db_name=db_name)
    if _is_value_in(DATABASE=DATABASE, collection=collection, object=object):
        for i, e in enumerate(values):
            DATABASE[collection][object]['values'] = [(1 + i, values[i])] # проблема тут: сохраняется последнее значение
    else:
        count = DATABASE[collection][object]['values'][-1][0]
        for i, e in enumerate(values):
            DATABASE[collection][object]['values'].append([count + i + 1, values[i]])
    _save_db(db_name=db_name, DB=DATABASE)
