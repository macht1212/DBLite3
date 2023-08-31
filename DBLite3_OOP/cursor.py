from DBLite3_OOP._exceptions import CreationError
from DBLite3_OOP._funcs import _object_exists, _collection_exists


class Cursor:

    def __str__(self):
        return 'Cursor'

    @staticmethod
    def __info__():
        return "The cursor is a data change control object within a connector."

    class Creator:

        def __init__(self, database: dict) -> None:
            self.database = database

        def __str__(self):
            return 'Creator'

        @staticmethod
        def __info__():
            return 'The creator is an object for creating collections and objects in the database.'

        def createCollection(self, collection_: str) -> None:
            """
            Objective:
            The method creates an empty new collection.

            Inputs:
                - collection_: The string data type represents the name of the collection.

            Flow:
                - The method checks whether the received variable matches its data type. If the data type is incorrect,
                  a ValueError will be raised to the user.
                - The method checks for the existence of a collection with the same name in the database. In the event
                  of a collision, returns an error explaining the need to use unique collection names.
                - The method creates an empty collection.
            Outputs:
                None

            Additional aspects:
                - The method uses the function _collection_exists of checking for a collision in the database.
            """

            if not isinstance(collection_, str):
                raise ValueError('Collection must be a string!')

            if _collection_exists(collection_, self.database):
                raise CreationError('Collection must be unique!')

            try:
                self.database[collection_] = {}
            except CreationError as e:
                raise CreationError(f'Error: {e}')

            return

        def createCollections(self, collections_: list) -> None:
            """
            Objective:
            The method creates a few empty new collections.

            Inputs:
                - collections_: The list data type represents the names of the collections.

            Flow:
                - The method checks whether the received variable matches its data type. If the data type is incorrect,
                  a ValueError will be raised to the user.
                - The method checks for the existence of a collection with the same name in the database. In the event
                  of a collision, returns an error explaining the need to use unique collection names.
                - The method creates a few empty new collections in loop.
            Outputs:
                None

            Additional aspects:
                - The method uses the function _collection_exists of checking for a collision in the database.
            """

            if not isinstance(collections_, list):
                raise ValueError('Collections_ must be a list!')

            if len(collections_) != len(set(collections_)):
                raise CreationError('Collection must be unique!')

            for collection in collections_:
                if _collection_exists(collection, self.database):
                    raise CreationError('Collection must be unique!')
                try:
                    self.database[collection] = {}
                except CreationError as e:
                    raise CreationError(f'Error: {e}')

            return

        def createObject(self, collection_: str, object_name: str) -> None:
            """
            Objective:
            The method creates a new empty object inside the collection.

            Inputs:
                - collection_: the string data type represents the name of the collection.
                - object_name: the string data type represents the name of the object.

            Flow:
            - The method checks whether the data type of the passed parameters matches the given ones. Returns a
              ValueError if it doesn't match.
            - The method checks if the required collection exists in the database. Returns a ValueError if not present.
            - The method checks if the required object exists in the database. Returns a ValueError if present.
            - The method creates a new empty object in the required collection.

            Outputs:
                - None

            Additional aspects:
                - The method uses the function _collection_exists of checking for a collision in the database.
                - The method uses the function _object_exists of checking for an object in the database.
            """

            if not isinstance(collection_, str):
                raise ValueError('Collections_ must be a string!')
            if not isinstance(object_name, str):
                raise ValueError('Object must be a string!')

            if _object_exists(collection_, object_name, self.database):
                raise CreationError('Object must be unique!')

            try:
                self.database[collection_][object_name] = None
            except CreationError as e:
                raise CreationError(f'Error: {e}')

            return

        def createObjects(self, collection_: str, object_names: list) -> None:
            """
            Objective:
            The method creates several required objects within the given collection.

            Inputs:
                - collection_: the string data type represents the name of the collection.
                - object_name: the list data type represents the names of the objects.

            Flow:
                - The method checks the correspondence between the data types of the passed parameters and the given
                  ones. Returns an error if it doesn't match.
                - The method checks the existence of an object with the given name in the collection and returns an
                  error if it exists.
                - The method creates a new empty objects in the required collection.

            Outputs:
                - None

            Additional aspects:
                - The method uses the function _object_exists of checking for an object in the database.

            """

            if not isinstance(collection_, str):
                raise ValueError('Collections_ must be a string!')
            if not isinstance(object_names, list):
                raise ValueError('Object must be a list!')

            for object_name in object_names:
                if _object_exists(collection_, object_name, self.database):
                    raise CreationError('Object must be unique!')
                try:
                    self.database[collection_][object_name] = None
                except CreationError as e:
                    raise CreationError(f'Error: {e}')

            return

        def returnDatabase(self):
            """
            """
            return self.database
