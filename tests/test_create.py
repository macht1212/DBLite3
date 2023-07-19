from LiteDB import create_db, create_collection


def test_create_db():
    create_db(db_name='qw')
    with open('qw.json', 'r') as file:
        db = file.read()
    assert db == '{}'


def test_create_table():
    create_collection(db_name='new', collection='table', objects=['col'])
    with open('new.json', 'r') as file:
        db = file.read()
    assert db == '{"table": {"col": {"values": []}}}'
