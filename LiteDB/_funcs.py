import json


def _open_db(db_name: str) -> dict:
    """

    :param db_name:
    :return:
    """
    with open(f'{db_name}.json', 'r') as db:
        info = db.read()
        return json.loads(info)


def _save_db(db_name: str, DB: dict) -> None:
    """

    :param db_name:
    :param DB:
    :return:
    """
    with open(f'{db_name}.json', 'w') as db:
        db.write(str(json.dumps(DB)))
