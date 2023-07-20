class CreationError(Exception):

    def __init__(self, text):
        self.text = text


class InsertError(Exception):

    def __init__(self, text):
        self.text = text


class UpdateError(Exception):

    def __init__(self, text):
        self.text = text


class AlterError(Exception):

    def __init__(self, text):
        self.text = text


class DeleteError(Exception):

    def __init__(self, text):
        self.text = text


class DropError(Exception):

    def __init__(self, text):
        self.text = text


class SelectError(Exception):

    def __init__(self, text):
        self.text = text
