from LiteDB import delete_value, delete_all_values


db_name_new = 'changed'
collection_new = 'colcol'
object_new = '11'
id = 1


def test_delete_value():
    delete_value(db_name=db_name_new, collection=collection_new, object=object_new, id=id)
    with open(f'{db_name_new}.json', 'r') as file:
        db = file.read()
    assert db == '{"colcol": {"12": {"values": null}, "11": {"values": [[2, "v11"], [3, "v21"]]}}}'


def test_delete_all_values():
    delete_all_values(db_name=db_name_new, collection=collection_new, object=object_new)
    with open(f'{db_name_new}.json', 'r') as file:
        db = file.read()
    assert db == '{"colcol": {"12": {"values": null}, "11": {"values": null}}}'
