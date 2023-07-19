from LiteDB import select_all_values_with_index, select_all_values_without_index, \
    size, select_all_values_in_collection

db_name_new = 'changed'
collection_new = 'colcol'
object_new = '11'


def test_select_all_values_with_index():
    result = select_all_values_with_index(db_name=db_name_new, collection=collection_new, object=object_new)
    assert result == ['Index: 1, value: value1', 'Index: 2, value: v11', 'Index: 3, value: v21']


def test_select_all_values_without_index():
    result = select_all_values_without_index(db_name=db_name_new, collection=collection_new, object=object_new)
    assert result == ['Value: value1', 'Value: v11', 'Value: v21']


def test_size():
    result = size(db_name=db_name_new, collection=collection_new, object=object_new)
    assert result == 3


def test_select_all_values_in_collection():
    result = select_all_values_in_collection(db_name=db_name_new, collection=collection_new)
    assert result == {'11': {'values': [[1, 'value1'], [2, 'v11'], [3, 'v21']]}, "12": {"values": None}}
