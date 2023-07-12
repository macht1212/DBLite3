def _value_in(DATABASE: dict, table_name: str, collection: str) -> bool:
    """
    The function checks if the first entry in the collection exists
    :param DATABASE: dictionary containing the database
    :param table_name: The name of the table to add the value to
    :param collection: The name of the collection to add the value to
    :return: True if the first entry in the collection exists
    """
    if DATABASE[table_name][collection]['values']:
        return True
    return False
