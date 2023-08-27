import os

import pytest

from DBLite3 import create_db, create_collection
from DBLite3._funcs import _open_db
from DBLite3 import alter_db, alter_collection, alter_object
from tests._test import word_generator


class TestAlterDB:

    @pytest.mark.parametrize('new', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, new):
        db_name = 'test'
        create_db(db_name)
        assert os.path.exists(os.path.join(db_name + '.json'))

        alter_db(db_name, new)
        assert os.path.exists(os.path.join(new + '.json'))
        os.remove(os.path.join(new + '.json'))

    @pytest.mark.parametrize('db_name', (word_generator(5) for _ in range(50)))
    def test_file_not_found(self, db_name):
        new = 'test_new'
        with pytest.raises(FileNotFoundError):
            alter_db(db_name, new)

    @pytest.mark.parametrize('db_name', (123, True, list, set, dict))
    def test_old_name_is_non_str(self, db_name):
        new = 'test'
        with pytest.raises(ValueError):
            alter_db(db_name, new)

    @pytest.mark.parametrize('new', (123, True, list, set, dict))
    def test_new_name_is_non_str(self, new):
        db_name = 'test'
        with pytest.raises(ValueError):
            alter_db(db_name, new)


class TestAlterCollection:

    @pytest.mark.parametrize('collection_new', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, collection_new):
        db_name = 'test'
        collections = ['col']
        collection_old = 'col'
        obj_name = ['o']

        create_db(db_name)
        create_collection(db_name, collections[0], obj_name)

        DB = _open_db(db_name)
        assert collection_old in DB.keys()

        alter_collection(db_name, collection_new, collection_old)
        DB = _open_db(db_name)
        assert collection_new in DB.keys()
        assert collection_old not in DB.keys()

        os.remove(os.path.join(db_name+'.json'))

    @pytest.mark.parametrize('db_name', (word_generator(5) for _ in range(50)))
    def test_db_does_not_exist(self, db_name):
        old = 'd'
        new = 'n'
        with pytest.raises(FileNotFoundError):
            alter_collection(db_name, new, old)

    @pytest.mark.parametrize('old', (word_generator(5) for _ in range(50)))
    def test_old_collection_does_not_exist(self, old):
        db = 'test'
        new = 'n'
        create_db(db)
        create_collection(db, 'qw', ['o'])
        with pytest.raises(KeyError):
            alter_collection(db, new, old)
        os.remove(os.path.join(db+'.json'))

    @pytest.mark.parametrize('old', (word_generator(5) for _ in range(50)))
    def test_new_collection_has_already_existed(self, old):
        db = 'test'
        create_db(db)
        create_collection(db, old, ['o'])
        with pytest.raises(KeyError):
            alter_collection(db, old, old)
        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('old', (123, True, list, set, dict))
    def test_old_collection_non_str(self, old):
        db = 'test'
        new = 'n'
        create_db(db)
        with pytest.raises(ValueError):
            alter_collection(db, new, old)
        os.remove(os.path.join(db+'.json'))

    @pytest.mark.parametrize('new', (123, True, list, set, dict))
    def test_new_collection_non_str(self, new):
        db = 'test'
        old = 'n'
        create_db(db)
        with pytest.raises(ValueError):
            alter_collection(db, new, old)
        os.remove(os.path.join(db + '.json'))


class TestAlterObject:

    @pytest.mark.parametrize('new', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, new):
        db = 'test'
        collection = ['col']
        obj_name = ['q']
        create_db(db)
        create_collection(db, collection[0], obj_name)

        DB = _open_db(db)
        assert obj_name[0] in DB[collection[0]].keys()

        alter_object(db, collection[0], obj_name[0], new)
        DB = _open_db(db)
        assert new in DB[collection[0]].keys()
        assert obj_name[0] not in DB[collection[0]].keys()

        os.remove(os.path.join(db+'.json'))



