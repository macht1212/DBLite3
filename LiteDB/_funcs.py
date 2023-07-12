import json


def _open_db(db_name: str) -> dict:
    """
    The function parses the json file and returns a dictionary
    :param db_name: the name of the database that is planned to be opened
    :return: dict
    """
    with open(f'{db_name}.json', 'r') as db:
        info = db.read()
        return json.loads(info)


def _save_db(db_name: str, DB: dict) -> None:
    """
    The function translates the dictionary into a json file
    :param db_name: the name of the database that is planned to be saved
    :param DB: dict of the database that is planned to be saved
    :return: None
    """
    with open(f'{db_name}.json', 'w') as db:
        db.write(str(json.dumps(DB)))
