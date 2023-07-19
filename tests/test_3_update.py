from LiteDB import update_value_by_id, update_values_by_id

db_name = 'qw'
collection = 'col'
object = '1'
value = 'value1'
values = ['v11', 'v21']
id = 1
ids = [2, 3]


def test_update_value_by_id():
    update_value_by_id(db_name=db_name, collection=collection, object=object, id=id, value=value)
    with open(f'{db_name}.json', 'r') as file:
        db = file.read()
    assert db == '{"col": {"1": {"values": [[1, "value1"], [2, "v1"], [3, "v2"]]}, "12": {"values": null}}}'


def test_update_values_by_id():
    update_values_by_id(db_name=db_name, collection=collection, object=object, id=ids, values=values)
    with open(f'{db_name}.json', 'r') as file:
        db = file.read()
    assert db == '{"col": {"1": {"values": [[1, "value1"], [2, "v11"], [3, "v21"]]}, "12": {"values": null}}}'
