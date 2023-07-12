import os


def _db_exists(db_name: str) -> bool:
    """
    The function checks if the database exists in the base directory, returns False if it doesn't exist
    :param: db_name: db's name
    :return: bool (True if DB exists)
    """
    if os.path.exists(f'{db_name}.json'):
        return True
    return False


def _table_exists(table_name: str, DB: dict) -> bool:
    """
    The function checks if the table exists in the database, returns False if it doesn't exist
    :param table_name:
    :param DB:
    :return:
    """
    if table_name in DB.keys():
        return True
    return False
