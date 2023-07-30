import os

import pytest

from DBLite3 import create_db, create_collection, create_object
from DBLite3 import CreationError
from DBLite3._funcs import _open_db


class TestCreateDB:
    @pytest.mark.parametrize('db_name',
                             ('first',
                              'second',
                              'third'))
    def test_create_db_is_ex_false_no_ex(self, db_name):
        create_db(db_name)
        assert os.path.isfile(f'{db_name}.json')
        os.remove(f'{db_name}.json')

    @pytest.mark.parametrize('db_name',
                             ('first',
                              'second',
                              'third'))
    def test_create_db_is_ex_false_is_ex(self, db_name):
        create_db(db_name)
        with pytest.raises(CreationError):
            create_db(db_name)
        os.remove(f'{db_name}.json')

    @pytest.mark.parametrize('db_name',
                             ('first',
                              'second',
                              'third'))
    def test_create_db_is_ex_true_is_ex(self, db_name):
        create_db(db_name)
        create_db(db_name, if_exists=True)
        assert os.path.isfile(f'{db_name}.json')
        os.remove(f'{db_name}.json')

    def test_create_db_empty_name(self):
        db_name = ''
        with pytest.raises(ValueError):
            create_db(db_name)

    def test_create_db_non_str_name(self):
        db_name = 123
        with pytest.raises(ValueError):
            create_db(db_name)


class TestCreateCollection:

    def test_create_collection_positive_case(self):
        db_name, collection, objects = 'test', 'collection', ['o1', 'o2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        DB = _open_db(db_name)
        assert collection in DB.keys()

        for object in objects:
            assert object in DB[collection].keys()

        os.remove(f'{db_name}.json')

    @pytest.mark.parametrize('collection',
                             (123, 1234, True, list(), dict(), set()))
    def test_create_collection_col_name_non_str(self, collection):
        db_name, objects = 'test', ['o1', 'o2']
        with pytest.raises(ValueError):
            create_db(db_name)
            create_collection(db_name, collection, objects)
        os.remove(f'{db_name}.json')

    @pytest.mark.parametrize('objects',
                             (123, 1234, True, set(), dict(), 'sas'))
    def test_create_collection_object_non_list(self, objects):
        db_name, collection = 'test', '123'
        with pytest.raises(ValueError):
            create_db(db_name)
            create_collection(db_name, collection, objects)
        os.remove(f'{db_name}.json')

    def test_create_collection_non_unique_object_name(self):
        db_name, collection, objects = 'test', 'collection', ['o1', 'o1']
        create_db(db_name)
        with pytest.raises(ValueError):
            create_collection(db_name, collection, objects)
        os.remove(f'{db_name}.json')

    def test_create_collection_non_unique_collection_name(self):
        db_name, collection, objects = 'test', 'collection', ['o1', 'o2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(CreationError):
            create_collection(db_name, collection, objects)
        os.remove(f'{db_name}.json')


class TestCreateObject:

    @pytest.mark.parametrize('object', ('123', '23', 'True', 'list()', 'set()', 'dict()'))
    def test_create_object_positive_case(self, object):
        db_name, collection, objects = 'test', 'collection', ['o1', 'o2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        create_object(db_name, collection, object)
        DB = _open_db(db_name)
        assert object in DB[collection].keys()
        os.remove(f'{db_name}.json')

    @pytest.mark.parametrize('object', (123, 23, True, list(), set(), dict()))
    def test_create_object_non_str_obj_name(self, object):
        db_name, collection, objects = 'test', 'collection', ['o1', 'o2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(ValueError):
            create_object(db_name, collection, object)
        os.remove(f'{db_name}.json')

    def test_create_object_non_unique_object_name(self):
        db_name, collection, objects = 'test', 'collection', ['o1', 'o2']
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(CreationError):
            create_object(db_name, collection, 'o1')
        os.remove(f'{db_name}.json')

    @pytest.mark.parametrize('collection_', (123, 23, True, list(), set(), dict()))
    def test_create_object_non_str_col_name(self, collection_):
        db_name, collection, objects, object = 'test', 'collection', ['o1', 'o2'], '1'
        create_db(db_name)
        create_collection(db_name, collection, objects)
        with pytest.raises(ValueError):
            create_object(db_name, collection_, object)
        os.remove(f'{db_name}.json')

