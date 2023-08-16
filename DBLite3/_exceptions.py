class CreationError(Exception):
    """
    Main functionalities:
    The CreationError class is an exception class that is raised when an error occurs during object creation.
    It provides a way to handle errors that occur during the creation of objects in a program.

    Methods:
        - __init__(self, message): Initializes the CreationError object with a message describing the error that
          occurred during object creation.
        - __str__(self): Returns the message attribute of the CreationError object as a string.

    Fields:
        - message (str): A description of the error that occurred during object creation.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InsertError(Exception):
    """
    Main functionalities:
    The InsertError class is a custom exception class that can be raised when an error occurs during insertion of data.
    It allows for the creation of custom error messages to be displayed when the exception is raised.

    Methods:
        - __init__(self, message): Initializes the InsertError object with a custom error message.
        - __str__(self): Returns the custom error message as a string.

    Fields:
        - message: A string that holds the custom error message.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class UpdateError(Exception):
    """
    Main functionalities:
    The UpdateError class is a custom exception class that can be used to raise exceptions when an update operation
    fails. It allows for the creation of custom error messages to provide more information about the error that occurred.

    Methods:
        - __init__(self, message): Initializes the UpdateError object with a custom error message.
        - __str__(self): Returns the custom error message as a string.

    Fields:
        - message: A string that contains the custom error message.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class AlterError(Exception):
    """
    Main functionalities:
    The AlterError class is a custom exception class that can be used to raise exceptions with a custom error message.
    It inherits from the built-in Exception class and allows for the creation of more specific error messages.

        Methods:
        - __init__(self, message): Constructor method that takes in a message parameter and assigns it to the message
          field.
        - __str__(self): Method that returns the message field as a string when the exception is raised.

    Fields:
        - message: A string field that holds the custom error message passed to the constructor.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DeleteError(Exception):
    """
    Main functionalities:
    The DeleteError class is designed to handle errors that occur during deletion operations. It allows for custom error
    messages to be passed in and displayed when an error occurs.

    Methods:
        - __init__(self, message): Constructor method that initializes the DeleteError object with a custom error message.
        - __str__(self): Method that returns the custom error message as a string.

    Fields:
        - message: A string that holds the custom error message passed in during object initialization.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DropError(Exception):
    """
    Main functionalities:
    The DropError class is an exception class that can be raised when an error occurs during a drop operation. It allows
    for custom error messages to be passed as arguments and provides a string representation of the error message.

    Methods:
        - __init__(self, message): Initializes the DropError object with a custom error message.
        - __str__(self): Returns the error message as a string.

    Fields:
        - message: A string that holds the custom error message passed as an argument during initialization.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class SelectError(Exception):
    """
    Main functionalities:
    The SelectError class is an exception class that is used to handle errors that occur during the selection process.
    It allows for the creation of custom error messages that can be raised when a specific error occurs.

    Methods:
        - __init__(self, message): Initializes the SelectError object with a custom error message.
        - __str__(self): Returns the error message as a string.

    Fields:
        - message: A string that contains the custom error message.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class SaveError(Exception):
    """
    Main functionalities:
    The SaveError class is an exception class that can be raised when there is an error while saving data. It allows for
    custom error messages to be passed as arguments and provides a string representation of the error message.

    Methods:
        - __init__(self, message): Constructor method that initializes the SaveError object with a custom error message.
        - __str__(self): Method that returns the string representation of the error message.

    Fields:
        - message: A string field that holds the custom error message passed as an argument to the constructor method.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class OpenError(Exception):
    """
    Main functionalities:
    The OpenError class is used to create custom exceptions for handling errors related to opening files or resources.
    It allows for the creation of specific error messages to be raised when an issue occurs during the opening process.

    Methods:
        - __init__(self, message): Initializes the OpenError object with a custom error message.
        - __str__(self): Returns the error message as a string when the exception is raised.

    Fields:
        - message: A string that holds the custom error message passed to the OpenError object during initialization.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
