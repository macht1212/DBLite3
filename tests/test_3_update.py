import os

import pytest

from DBLite3 import update_values_by_id, update_value_by_id
from DBLite3 import create_db, create_collection
from DBLite3 import insert_one_in_one_collection
from DBLite3._funcs import _open_db
from tests._test import word_generator


class TestUpdateValueById:

    @pytest.mark.parametrize('db_name', (word_generator(5) for _ in range(50)))
    def test_positive_case_value(self, db_name):
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2]
        create_db(db_name)
        create_collection(db_name, collection, obj_name)
        for value in values:
            insert_one_in_one_collection(db_name, collection, obj_name[0], value)

        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, '1'], [2, 2]]

        update_value_by_id(db_name, collection, obj_name[0], 1, '2')
        DB_u1 = _open_db(db_name)
        assert DB_u1[collection][obj_name[0]]['values'] == [[1, '2'], [2, 2]]

        update_value_by_id(db_name, collection, obj_name[0], 2, '21')
        DB_u2 = _open_db(db_name)
        assert DB_u2[collection][obj_name[0]]['values'] == [[1, '2'], [2, '21']]

        os.remove(os.path.join(db_name + '.json'))

    def test_non_existing_id(self):
        db_name = 'test'
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2]
        create_db(db_name)
        create_collection(db_name, collection, obj_name)
        for value in values:
            insert_one_in_one_collection(db_name, collection, obj_name[0], value)

        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, '1'], [2, 2]]

        with pytest.raises(ValueError):
            update_value_by_id(db_name, collection, obj_name[0], id=3, value='no')
        os.remove(os.path.join(db_name + '.json'))

    def test_change_value_type(self):
        db_name = 'test'
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2]
        create_db(db_name)
        create_collection(db_name, collection, obj_name)
        insert_one_in_one_collection(db_name, collection, obj_name[0], values[0])

        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, '1']]

        update_value_by_id(db_name, collection, obj_name[0], 1, values[1])
        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, 2]]
        os.remove(os.path.join(db_name + '.json'))

    def test_double_update(self):
        db_name = 'test'
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        create_db(db_name)
        create_collection(db_name, collection, obj_name)
        insert_one_in_one_collection(db_name, collection, obj_name[0], values[0])

        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, '1']]

        update_value_by_id(db_name, collection, obj_name[0], 1, values[1])
        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, 2]]

        update_value_by_id(db_name, collection, obj_name[0], 1, values[2])
        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, 'str']]
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db_name', (word_generator(5) for _ in range(50)))
    def test_non_existing_db(self, db_name):
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        with pytest.raises(FileNotFoundError):
            update_value_by_id(db_name, collection, obj_name[0], id=1, value=values[1])

    @pytest.mark.parametrize('collections', (word_generator(5) for _ in range(50)))
    def test_non_existing_collection(self, collections):
        db_name = 'test'
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        create_db(db_name)
        create_collection(db_name, collection, obj_name)

        with pytest.raises(ValueError):
            update_value_by_id(db_name, collections, obj_name[0], id=1, value=values[1])
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('obj_name_', (word_generator(5) for _ in range(50)))
    def test_non_existing_collection(self, obj_name_):
        db_name = 'test'
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        create_db(db_name)
        create_collection(db_name, collection, obj_name)

        with pytest.raises(ValueError):
            update_value_by_id(db_name, collection, obj_name_, id=1, value=values[1])
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db_name', (123, True, list, set, dict))
    def test_db_name_non_str(self, db_name):
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        with pytest.raises(FileNotFoundError):
            update_value_by_id(db_name, collection, obj_name[0], id=1, value=values[1])

    @pytest.mark.parametrize('collection', (123, True, str, set, dict))
    def test_collection_non_list(self, collection):
        db_name, collections, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collections:
            create_collection(db_name, col, objects)
        with pytest.raises(TypeError):
            update_value_by_id(db_name, collection, objects[0], id=1, value=values[1])
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('object_', (123, True, list, set, dict))
    def test_object_non_str(self, object_):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(TypeError):
            update_value_by_id(db_name, collection[0], object_, id=1, value=values[1])
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('id', (123, True, list, set, dict))
    def test_id_non_int(self, id):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(TypeError):
            update_value_by_id(db_name, collection[0], objects[0], id, value=values[1])
        os.remove(os.path.join(db_name + '.json'))


class TestUpdateValuesById:

    @pytest.mark.parametrize('db_name', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, db_name):
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2]
        create_db(db_name)
        create_collection(db_name, collection, obj_name)
        for value in values:
            insert_one_in_one_collection(db_name, collection, obj_name[0], value)

        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, '1'], [2, 2]]

        update_values_by_id(db_name, collection, obj_name[0], [1, 2], ['2', 3])
        DB = _open_db(db_name)
        assert DB[collection][obj_name[0]]['values'] == [[1, '2'], [2, 3]]
        os.remove(os.path.join(db_name + '.json'))

    def test_negative_case_non_ex_id(self):
        db_name = 'test'
        collections = ['col1', 'col2']
        obj_name = ['o']
        values = ['1', 2]
        create_db(db_name)
        for collection in collections:
            create_collection(db_name, collection, obj_name)
            for value in values:
                insert_one_in_one_collection(db_name, collection, obj_name[0], value)

        DB = _open_db(db_name)
        for collection in collections:
            assert DB[collection][obj_name[0]]['values'] == [[1, '1'], [2, 2]]

        with pytest.raises(ValueError):
            update_values_by_id(db_name=db_name,
                                collection=collections[0],
                                obj_name=obj_name[0],
                                id=[4, 5],
                                values=['1', '1'])

        os.remove(os.path.join(db_name + '.json'))

    def test_change_type_of_value(self):
        db_name = 'test'
        collections = ['col1', 'col2']
        obj_name = ['o']
        values = ['1', 2]
        create_db(db_name)
        for collection in collections:
            create_collection(db_name, collection, obj_name)
            for value in values:
                insert_one_in_one_collection(db_name, collection, obj_name[0], value)

        DB = _open_db(db_name)
        for collection in collections:
            assert DB[collection][obj_name[0]]['values'] == [[1, '1'], [2, 2]]

        update_values_by_id(db_name=db_name,
                            collection=collections[0],
                            obj_name=obj_name[0],
                            id=[1, 2],
                            values=['q', 'w'])

        DB = _open_db(db_name)
        assert DB[collections[0]][obj_name[0]]['values'] == [[1, 'q'], [2, 'w']]
        assert DB[collections[1]][obj_name[0]]['values'] == [[1, '1'], [2, 2]]
        os.remove(os.path.join(db_name + '.json'))

    def test_double_update(self):
        db_name = 'test'
        collections = ['col1', 'col2']
        obj_name = ['o']
        values = ['1', 2]
        create_db(db_name)
        for collection in collections:
            create_collection(db_name, collection, obj_name)
            for value in values:
                insert_one_in_one_collection(db_name, collection, obj_name[0], value)

        DB = _open_db(db_name)
        for collection in collections:
            assert DB[collection][obj_name[0]]['values'] == [[1, '1'], [2, 2]]

            update_values_by_id(db_name=db_name,
                                collection=collection,
                                obj_name=obj_name[0],
                                id=[1, 2],
                                values=['q', 'w'])

        DB = _open_db(db_name)
        for collection in collections:
            assert DB[collection][obj_name[0]]['values'] == [[1, 'q'], [2, 'w']]
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db_name', (word_generator(5) for _ in range(50)))
    def test_non_existing_db(self, db_name):
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        with pytest.raises(FileNotFoundError):
            update_values_by_id(db_name, collection, obj_name[0], id=[1, 2, 3], values=values)

    @pytest.mark.parametrize('collections', (word_generator(5) for _ in range(50)))
    def test_non_existing_collection(self, collections):
        db_name = 'test'
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        create_db(db_name)
        create_collection(db_name, collection, obj_name)

        with pytest.raises(ValueError):
            update_values_by_id(db_name, collection, obj_name[0], id=[1, 2, 3], values=values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('obj_name_', (word_generator(5) for _ in range(50)))
    def test_non_existing_collection(self, obj_name_):
        db_name = 'test'
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        create_db(db_name)
        create_collection(db_name, collection, obj_name)

        with pytest.raises(ValueError):
            update_values_by_id(db_name, collection, obj_name_, id=[1, 2, 3], values=values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('db_name', (123, True, list, set, dict))
    def test_db_name_non_str(self, db_name):
        collection = 'col'
        obj_name = ['o']
        values = ['1', 2, 'str']
        with pytest.raises(FileNotFoundError):
            update_values_by_id(db_name, collection, obj_name[0], id=[1, 2, 3], values=values)

    @pytest.mark.parametrize('collection', (123, True, list, set, dict))
    def test_collection_non_str(self, collection):
        db_name, collections, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collections:
            create_collection(db_name, col, objects)
        with pytest.raises(ValueError):
            update_values_by_id(db_name, collection, objects[0], id=[1, 2, 3], values=values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('object_', (123, True, list, set, dict))
    def test_object_non_str(self, object_):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(ValueError):
            update_values_by_id(db_name, collection[0], object_, id=[1, 2], values=values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('ids', (str, set, dict))
    def test_id_non_int(self, ids):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(TypeError):
            update_values_by_id(db_name, collection[0], objects[0], id=[ids, 2], values=values)
        os.remove(os.path.join(db_name + '.json'))

    @pytest.mark.parametrize('ids', (123, True, str, set, dict))
    def test_id_non_list(self, ids):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(ValueError):
            update_values_by_id(db_name, collection[0], objects[0], id=ids, values=values)
        os.remove(os.path.join(db_name + '.json'))

    def test_len_id_values(self):
        db_name, collection, objects = 'test', ['col', 'ss'], ['obj']
        values = ['value', 'value2']
        create_db(db_name)
        for col in collection:
            create_collection(db_name, col, objects)

        with pytest.raises(ValueError):
            update_values_by_id(db_name, collection[0], objects[0], id=[1, 2, 3], values=values)
        os.remove(os.path.join(db_name + '.json'))
