import os


def _db_exists(db_name: str) -> bool:
    """
    The function checks if the database exists in the base directory, returns False if it doesn't exist.
    :param: db_name: db's name
    :return: bool (True if DB exists)
    """
    if os.path.exists(f'{db_name}.json'):
        return True
    return False
