import json
import os

from DBLite3_OOP._funcs import _open_db, _save_db
from DBLite3_OOP._exceptions import OpenError, SaveError


class Connector:

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def __str__(self) -> str:
        return 'Connector'

    @staticmethod
    def __info__() -> str:
        return ("Connector is a database connection object that connects to a database and transforms a JSON file "
                "into a Python dictionary format. At the end of work with the database, the connector closes the "
                "connection, saving all changes.")

    def open(self) -> dict:
        """
        Objective:
        The method creates a database object in the form of a dictionary.

        Inputs:
            - None

        Flow:
            - The method checks for the existence of a database file at the specified path. Returns a FileNotFoundError
              if not exist.
            - The method using the context manager opens the database file, parses them and returns them as a dictionary.

        Outputs:
            - Database in the form of a dictionary.

        Additional aspects:
            - The method uses the os module to work with the path and presence of the file.
            - The method uses the json module to parse information from the database.
        """
        if not os.path.isfile(f'{self.db_name}.json'):
            raise FileNotFoundError(f'{self.db_name}.json does not exist')

        try:
            with open(f'{os.path.join(self.db_name + ".json")}', 'r') as db:
                return json.load(db)
        except json.JSONDecodeError as e:
            raise OpenError(f'Error opening/parsing {self.db_name}.json file: {e}')

    def close(self, database: dict) -> None:
        """
        Objective:
        The method closes the connection to the database while saving all previously made changes.
        ATTENTION! Without closing the connection, the data entered into the database will not be saved and will be
        irretrievably lost.

        Inputs:
            - database: the generated database with all the changes made in the form of a dictionary.
            - self.db_name: an object of database name.

        Flow:
            - The method checks whether the data type of the passed parameter matches.
            - The method checks for the existence of a database file at the specified path. Returns a FileNotFoundError
              if not exist.
            - The method writes the updated data to the database file.

        Outputs:
            - None

        Additional aspects:
            - The method uses the os module to work with the path and presence of the file.
            - The method uses the json module to put information to the database.
        """
        if not isinstance(database, dict):
            raise ValueError('Database must be a dict!')

        if not os.path.isfile(self.db_name + '.json'):
            raise FileNotFoundError(f'{self.db_name}.json does not exist')

        try:
            file_path = os.path.join(self.db_name + '.json')
            with open(file_path, 'w') as db:
                json.dump(database, db)
        except Exception as e:
            raise SaveError(f'Error saving database: {e}')

        return


