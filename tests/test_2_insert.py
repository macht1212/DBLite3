from LiteDB import insert_one, insert_many

db_name = 'qw'
collection = 'col'
object = '1'
value = 'value'
values = ['v1', 'v2']


def test_insert_one():
    insert_one(db_name=db_name, collection=collection, object=object, value=value)
    with open(f'{db_name}.json', 'r') as file:
        db = file.read()
    assert db == '{"col": {"1": {"values": [[1, "value"]]}, "12": {"values": null}}}'


def test_insert_many():
    insert_many(db_name=db_name, collection=collection, object=object, values=values)
    with open(f'{db_name}.json', 'r') as file:
        db = file.read()
    assert db == '{"col": {"1": {"values": [[1, "value"], [2, "v1"], [3, "v2"]]}, "12": {"values": null}}}'
