import os

from LiteDB import alter_object, alter_collection, alter_db
from LiteDB._funcs import _db_exists

db_name = 'qw'
db_name_new = 'changed'
collection = 'col'
collection_new = 'colcol'
object = '1'
object_new = '11'
value = 'value1'
values = ['v11', 'v21']
id = 1
ids = [2, 3]


def test_alter_object():
    alter_object(db_name=db_name, collection=collection, object_old=object, object_new=object_new)
    with open(f'{db_name}.json', 'r') as file:
        db = file.read()
    assert db == '{"col": {"12": {"values": null}, "11": {"values": [[1, "value1"], [2, "v11"], [3, "v21"]]}}}'


def test_alter_collection():
    alter_collection(db_name=db_name, collection_old=collection, collection_new=collection_new)
    with open(f'{db_name}.json', 'r') as file:
        db = file.read()
    assert db == '{"colcol": {"12": {"values": null}, "11": {"values": [[1, "value1"], [2, "v11"], [3, "v21"]]}}}'


def test_alter_db():
    alter_db(db_name_old=db_name, db_name_new=db_name_new)
    check = _db_exists(db_name=db_name_new)
    assert check == True
