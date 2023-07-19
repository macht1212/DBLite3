from LiteDB import drop_db, drop_collection, drop_object
from LiteDB._funcs import _db_exists


db_name_new = 'changed'
collection_new = 'colcol'
object_new = '11'


def test_drop_object():
    drop_object(db_name=db_name_new, collection=collection_new, object=object_new)
    with open(f'{db_name_new}.json', 'r') as file:
        db = file.read()
    assert db == '{"colcol": {"12": {"values": null}}}'


def test_drop_collection():
    drop_collection(db_name=db_name_new, collection=collection_new)
    with open(f'{db_name_new}.json', 'r') as file:
        db = file.read()
    assert db == '{}'


def test_drop_db():
    drop_db(db_name=db_name_new)
    result = _db_exists(db_name=db_name_new)
    assert result == False
