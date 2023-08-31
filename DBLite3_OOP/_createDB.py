import os

from DBLite3_OOP._exceptions import CreationError
from DBLite3_OOP._funcs import _db_exists


def create_db(db_name: str, if_exists: bool = False) -> None:
    """
    Objective:


    Inputs:
        - db_name (str): the name of the database to be created. The name of the database must be unique in the project,
          otherwise the file will be overwritten.
        - if_exists (bool): an optional parameter responsible for skipping an exception when creating a database with an
          already existing name.

    Flow:


    Outputs:


    Additional aspects:

    """
    try:
        if not isinstance(db_name, str) or not db_name:
            raise ValueError('Database name must be a non-empty string')

        file_path = os.path.join(db_name + '.json')

        if _db_exists(db_name=db_name) and if_exists:
            print(f'DATABASE with name: {db_name} has already existed')
            return
        elif _db_exists(db_name=db_name):
            raise CreationError(f'DATABASE with name: {db_name} has already existed')
        else:
            try:
                with open(file_path, 'w') as f:
                    f.write('{}')
            except IOError as e:
                raise CreationError(f'Error: {e}')
        return
    except CreationError as e:
        raise CreationError(f'Error: {e}')
