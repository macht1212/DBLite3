import os
import pytest

from DBLite3._funcs import _open_db
from DBLite3 import create_db, create_collection
from DBLite3 import insert_many_in_one_collection
from DBLite3 import delete_value, delete_all_values
from tests._test import word_generator


class TestDeleteValueById:

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, db):
        collection = 'col'
        obj = ['o']
        values = [1, 2, 3, 4, 5, 6, 7, 8]

        create_db(db)
        create_collection(db, collection, obj)
        insert_many_in_one_collection(db, collection, obj[0], values)

        DB = _open_db(db)
        assert [[i + 1, values[i]] for i in range(len(values))] == DB[collection][obj[0]]['values']

        delete_value(db, collection, obj[0], 1)
        DB = _open_db(db)
        assert [[i, values[i - 1]] for i in range(2, len(values) + 1)] == DB[collection][obj[0]]['values']

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_db_does_not_exist(self, db):
        with pytest.raises(FileNotFoundError):
            delete_value(db, 'collection', 'obj[0]', 1)

    @pytest.mark.parametrize('col', (word_generator(5) for _ in range(50)))
    def test_collection_does_not_exist(self, col):
        db = 'test'
        collection = 'col'
        obj = ['o']
        values = [1, 2, 3, 4, 5, 6, 7, 8]

        create_db(db)
        create_collection(db, collection, obj)
        insert_many_in_one_collection(db, collection, obj[0], values)

        DB = _open_db(db)
        assert [[i + 1, values[i]] for i in range(len(values))] == DB[collection][obj[0]]['values']

        with pytest.raises(ValueError):
            delete_value(db, col, obj[0], 1)

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('obj', (word_generator(5) for _ in range(50)))
    def test_object_does_not_exist(self, obj):
        db = 'test'
        collection = 'col'
        obj_ = ['o']
        values = [1, 2, 3, 4, 5, 6, 7, 8]

        create_db(db)
        create_collection(db, collection, obj_)
        insert_many_in_one_collection(db, collection, obj_[0], values)

        DB = _open_db(db)
        assert [[i + 1, values[i]] for i in range(len(values))] == DB[collection][obj_[0]]['values']

        with pytest.raises(ValueError):
            delete_value(db, collection, obj, 1)

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('name', (123, True, list, set, dict))
    def test_db_name_is_non_str(self, name):
        db = 'test'
        collection = 'col'
        obj = ['o']

        create_db(db)
        create_collection(db, collection, obj)
        with pytest.raises(ValueError):
            delete_value(name, collection, obj[0], 1)

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('col', (123, True, list, set, dict))
    def test_collection_is_not_str(self, col):
        db = 'test'
        collection = 'col'
        obj_ = ['o']
        values = [1]

        create_db(db)
        create_collection(db, collection, obj_)
        insert_many_in_one_collection(db, collection, obj_[0], values)

        DB = _open_db(db)
        assert [[i + 1, values[i]] for i in range(len(values))] == DB[collection][obj_[0]]['values']

        with pytest.raises(ValueError):
            delete_value(db, col, obj_[0], 1)

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('obj', (123, True, str, set, dict))
    def test_object_is_not_str(self, obj):
        db = 'test'
        collection = 'col'
        obj_ = ['o']
        values = [1]

        create_db(db)
        create_collection(db, collection, obj_)
        insert_many_in_one_collection(db, collection, obj_[0], values)

        DB = _open_db(db)
        assert [[i + 1, values[i]] for i in range(len(values))] == DB[collection][obj_[0]]['values']

        with pytest.raises(ValueError):
            delete_value(db, collection, obj, 1)

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('id_', (list, str, set, dict))
    def test_id_is_not_int(self, id_):
        db = 'test'
        collection = 'col'
        obj_ = ['o']
        values = [1]

        create_db(db)
        create_collection(db, collection, obj_)
        insert_many_in_one_collection(db, collection, obj_[0], values)

        DB = _open_db(db)
        assert [[i + 1, values[i]] for i in range(len(values))] == DB[collection][obj_[0]]['values']

        with pytest.raises(ValueError):
            delete_value(db, collection, obj_[0], id_)

        os.remove(os.path.join(db + '.json'))


class TestDeleteAllValues:

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, db):
        collection = 'col'
        obj = ['o']
        values = [1, 2, 3, 4, 5, 6, 7, 8]

        create_db(db)
        create_collection(db, collection, obj)
        insert_many_in_one_collection(db, collection, obj[0], values)

        DB = _open_db(db)
        assert [[i + 1, values[i]] for i in range(len(values))] == DB[collection][obj[0]]['values']

        delete_all_values(db, collection, obj[0])
        DB = _open_db(db)
        assert not DB[collection][obj[0]]['values']

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_db_does_not_exist(self, db):
        with pytest.raises(FileNotFoundError):
            delete_all_values(db, 'collection', 'obj[0]')

    @pytest.mark.parametrize('col', (word_generator(5) for _ in range(50)))
    def test_collection_does_not_exist(self, col):
        db = 'test'
        collection = 'col'
        obj = ['o']

        create_db(db)
        create_collection(db, collection, obj)
        with pytest.raises(KeyError):
            delete_all_values(db, col, obj[0])

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('obj_', (word_generator(5) for _ in range(50)))
    def test_object_does_not_exist(self, obj_):
        db = 'test'
        collection = 'col'
        obj = ['o']

        create_db(db)
        create_collection(db, collection, obj)
        with pytest.raises(KeyError):
            delete_all_values(db, collection, obj_)

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('col', (123, True, list, set, dict))
    def test_collection_is_non_str(self, col):
        db = 'test'
        collection = 'col'
        obj = ['o']

        create_db(db)
        create_collection(db, collection, obj)
        with pytest.raises(ValueError):
            delete_all_values(db, col, obj[0])

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('name', (123, True, list, set, dict))
    def test_db_name_is_non_str(self, name):
        db = 'test'
        collection = 'col'
        obj = ['o']

        create_db(db)
        create_collection(db, collection, obj)
        with pytest.raises(ValueError):
            delete_all_values(name, collection, obj[0])

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('obj_', (123, True, list, set, dict))
    def test_object_is_non_str(self, obj_):
        db = 'test'
        collection = 'col'
        obj = ['o']

        create_db(db)
        create_collection(db, collection, obj)
        with pytest.raises(ValueError):
            delete_all_values(db, collection, obj_)

        os.remove(os.path.join(db + '.json'))
