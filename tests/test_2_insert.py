import os

import pytest

from DBLite3 import (insert_one_in_many_collections,
                     insert_many_in_one_collection,
                     insert_one_in_one_collection,
                     create_db, create_collection)
from DBLite3._funcs import _open_db
from tests._test import word_generator


class TestInsertOneInOneCollection:

    @pytest.mark.parametrize('value', (word_generator(5) for _ in range(50)))
    def test_insert_value_to_empty_object(self, value):
        db_name = 'test'
        collection = 'col'
        objects = ['obj']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        insert_one_in_one_collection(db_name, collection, objects[0], value)
        DB = _open_db(db_name)
        assert DB[collection][objects[0]]['values'] == [[1, value]]
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('value2', (word_generator(5) for _ in range(50)))
    def test_insert_value_to_non_empty_object(self, value2):
        db_name, collection, objects = 'test', 'col', ['obj']
        value1 = 'value'
        create_db(db_name)
        create_collection(db_name, collection, objects)
        insert_one_in_one_collection(db_name, collection, objects[0], value1)
        insert_one_in_one_collection(db_name, collection, objects[0], value2)
        DB = _open_db(db_name)
        assert DB[collection][objects[0]]['values'] == [[1, value1], [2, value2]]
        os.remove(os.path.join(db_name + '.json'))

    def test_database_does_not_exist(self):
        db_name = 'non_existent_db'
        collection = 'test_collection'
        object = 'test_object'
        value = 'test_value'
        with pytest.raises(FileNotFoundError):
            insert_one_in_one_collection(db_name=db_name, collection=collection, obj_name=object, value=value)

    @pytest.mark.parametrize('collection1', (word_generator(5) for _ in range(50)))
    def test_collection_does_not_exist(self, collection1):
        db_name = 'test_db'
        collection = 'coll'
        object = ['test_object']
        value = 'test_value'
        create_db(db_name)
        create_collection(db_name, collection, object)
        with pytest.raises(KeyError):
            insert_one_in_one_collection(db_name=db_name, collection=collection1, obj_name=object[0], value=value)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('object', (word_generator(5) for _ in range(50)))
    def test_object_does_not_exist(self, object):
        db_name = 'test_db'
        collection = 'test_collection'
        obj = ['o']
        value = 'test_value'
        create_db(db_name)
        create_collection(db_name, collection, obj)
        with pytest.raises(KeyError):
            insert_one_in_one_collection(db_name=db_name, collection=collection, obj_name=object, value=value)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db_name', (123, True, list))
    def test_invalid_db_name(self, db_name):
        collection, object, value = 'col', 'o', 'value'
        with pytest.raises(KeyError):
            insert_one_in_one_collection(db_name, collection, object, value)

    @pytest.mark.parametrize('collection', (123, True, list))
    def test_invalid_collection_name(self, collection):
        db_name, col, object, value = 'test', 'col', ['o'], 'value'
        create_db(db_name)
        create_collection(db_name, col, object)
        with pytest.raises(KeyError):
            insert_one_in_one_collection(db_name, collection, object[0], value)
        os.remove(os.path.join(db_name + '.json'))


class TestInsertManyInOneCollection:

    @pytest.mark.parametrize('values', ([word_generator(5), word_generator(4)] for _ in range(50)))
    def test_insert_positive_case_to_empty_obj(self, values):
        db_name, collection, objects = 'test', 'col', ['obj']
        values = ['value1', 'value2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        insert_many_in_one_collection(db_name, collection, objects[0], values)
        DB = _open_db(db_name)
        assert DB[collection][objects[0]]['values'] == [[1, values[0]], [2, values[1]]]
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('values', ([word_generator(5), word_generator(6)] for _ in range(50)))
    def test_insert_positive_case_to_non_empty_obj(self, values):
        db_name, collection, objects = 'test', 'col', ['obj']
        value = 'value0'
        create_db(db_name)
        create_collection(db_name, collection, objects)
        insert_one_in_one_collection(db_name, collection, objects[0], value)
        insert_many_in_one_collection(db_name, collection, objects[0], values)
        DB = _open_db(db_name)
        assert DB[collection][objects[0]]['values'] == [[1, value], [2, values[0]], [3, values[1]]]
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db_name_non_ex', (word_generator(5) for _ in range(50)))
    def test_insert_non_exist_db(self, db_name_non_ex):
        db_name, collection, objects = 'test', 'col', ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(FileNotFoundError):
            insert_many_in_one_collection(db_name_non_ex, collection, objects[0], values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('col', (word_generator(5) for _ in range(50)))
    def test_insert_non_exist_collection(self, col):
        db_name, collection, objects = 'test', 'col', ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(KeyError):
            insert_many_in_one_collection(db_name, col, objects[0], values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('obj', (word_generator(5) for _ in range(50)))
    def test_insert_non_exist_object(self, obj):
        db_name, collection, objects = 'test', 'col', ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(KeyError):
            insert_many_in_one_collection(db_name, collection, obj, values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db_name', (123, True, list, set, dict))
    def test_db_name_non_str(self, db_name):
        name, collection, objects = 'test', 'col', ['obj']
        values = ['value', 'value2']
        create_db(name)
        create_collection(name, collection, objects)
        with pytest.raises(KeyError):
            insert_many_in_one_collection(db_name, collection, 'objects[0]', values)
        os.remove(os.path.join(name + '.json'))

    @pytest.mark.parametrize('collection', (123, True, list, set, dict))
    def test_collection_non_str(self, collection):
        db_name, collection_, objects = 'test', 'col', ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        create_collection(db_name, collection_, objects)
        with pytest.raises(KeyError):
            insert_many_in_one_collection(db_name, collection, 'objects[0]', values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('object', (123, True, list, set, dict))
    def test_object_non_str(self, object):
        db_name, collection, objects = 'test', 'col', ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(KeyError):
            insert_many_in_one_collection(db_name, collection, object, values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('values', (123, True, set, dict, str))
    def test_values_non_list(self, values):
        db_name, collection, objects = 'test', 'col', ['obj']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(KeyError):
            insert_many_in_one_collection(db_name, collection, objects[0], values)
        os.remove(os.path.join(db_name + '.json'))


class TestInsertOneInManyCollections:

    @pytest.mark.parametrize('values', ([word_generator(5), word_generator(4)] for _ in range(50)))
    def test_insert_positive_case_to_empty_obj(self, values):
        db_name, collection, objects = 'test', ['col1', 'col2'], ['obj1', 'obj2']
        create_db(db_name)
        create_collection(db_name, collection[0], objects)
        create_collection(db_name, collection[1], objects)
        insert_one_in_many_collections(db_name, collection, objects[0], values[0])
        DB = _open_db(db_name)
        for col in collection:
            assert DB[col][objects[0]]['values'] == [[1, values[0]]]
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('values', ([word_generator(5), word_generator(7)] for _ in range(50)))
    def test_insert_positive_case_to_non_empty_obj(self, values):
        db_name, collection, objects = 'test', ['col1', 'col2'], ['obj1', 'obj2']
        create_db(db_name)
        create_collection(db_name, collection[0], objects)
        create_collection(db_name, collection[1], objects)

        for i in range(len(collection)):
            insert_one_in_one_collection(db_name, collection[i], objects[0], values[0])

        insert_one_in_many_collections(db_name, collection, objects[0], values[1])
        DB = _open_db(db_name)
        for col in collection:
            assert DB[col][objects[0]]['values'] == [[1, values[0]], [2, values[1]]]
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_insert_non_exist_db(self, db):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(FileNotFoundError):
            insert_one_in_many_collections(db, collection, objects[0], values[0])
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('col', (['col', word_generator(5)] for _ in range(50)))
    def test_insert_non_exist_collection(self, col):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(KeyError):
            insert_one_in_many_collections(db_name, col, objects[0], values[0])
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('obj', (word_generator(5) for _ in range(50)))
    def test_insert_non_exist_object(self, obj):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(KeyError):
            insert_one_in_many_collections(db_name, collection, obj, values[0])
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db_name', (123, True, list, set, dict))
    def test_db_name_non_str(self, db_name):
        name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(name)
        for col in collection:
            create_collection(name, col, objects)

        with pytest.raises(KeyError):
            insert_one_in_many_collections(db_name, collection, 'objects[0]', values[0])
        os.remove(os.path.join(name + '.json'))

    @pytest.mark.parametrize('collection', (123, True, str, set, dict))
    def test_collection_non_list(self, collection):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(KeyError):
            insert_one_in_many_collections(db_name, collection, 'objects[0]', values[0])
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('object', (123, True, list, set, dict))
    def test_object_non_str(self, object):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(KeyError):
            insert_one_in_many_collections(db_name, collection, object, values[0])
        os.remove(os.path.join(db_name + '.json'))


