import pytest

from LiteDB import create_db, create_collection, create_object

db_name = 'qw'
collection = 'col'
objects = ['1']


def test_create_db():
    create_db(db_name='qw')
    with open('qw.json', 'r') as file:
        db = file.read()
    assert db == '{}'


def test_create_table():
    create_collection(db_name=db_name, collection=collection, objects=objects)
    with open(f'{db_name}.json', 'r') as file:
        db = file.read()
    assert db == '{"col": {"1": {"values": null}}}'


def test_create_object():
    create_object(db_name=db_name, collection=collection, object='12')
    with open(f'{db_name}.json', 'r') as file:
        db = file.read()
    assert db == '{"col": {"1": {"values": null}, "12": {"values": null}}}'

