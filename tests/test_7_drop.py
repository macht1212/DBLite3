import os
import pytest

from DBLite3._funcs import _open_db
from DBLite3 import drop_db, drop_object, drop_collection, DropError
from DBLite3 import create_db, create_collection
from tests._test import word_generator


class TestDropDB:

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, db):
        path = os.path.join(db+'.json')
        with open(path, 'w') as f:
            f.write('{}')

        assert os.path.isfile(path)

        drop_db(db)

        assert not os.path.isfile(path)

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_db_does_not_exist(self, db):
        with pytest.raises(DropError):
            drop_db(db)

    @pytest.mark.parametrize('db', (int, True, list, set, tuple))
    def test_db_name_is_non_str(self, db):
        with pytest.raises(ValueError):
            drop_db(db)


class TestDropCollection:

    @pytest.mark.parametrize('col', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, col):
        db = 'test'
        path = os.path.join(db + '.json')
        create_db(db)
        create_collection(db, col, ['o'])

        DB = _open_db(db)
        assert col in DB.keys()

        drop_collection(db, col)
        DB = _open_db(db)
        assert col not in DB.keys()
        os.remove(path)

    @pytest.mark.parametrize('col', (word_generator(5) for _ in range(50)))
    def test_collection_does_not_exist(self, col):
        db = 'test'
        path = os.path.join(db + '.json')
        create_db(db)

        with pytest.raises(DropError):
            drop_collection(db, col)

        os.remove(path)

    @pytest.mark.parametrize('db', (int, True, list, set, tuple))
    def test_db_name_is_non_str(self, db):
        with pytest.raises(ValueError):
            drop_collection(db, 'col')

    @pytest.mark.parametrize('col', (int, True, list, set, tuple))
    def test_collection_is_non_str(self, col):
        with pytest.raises(ValueError):
            drop_collection('db', col)


class TestDropObject:

    @pytest.mark.parametrize('obj', ([word_generator(5)] for _ in range(50)))
    def test_positive_case(self, obj):
        db = 'test'
        col = 'col'
        create_db(db)
        create_collection(db, col, obj)
        path = os.path.join(db+'.json')

        DB = _open_db(db)
        assert obj[0] in DB[col].keys()

        drop_object(db, col, obj[0])
        DB = _open_db(db)
        assert obj[0] not in DB[col].keys()

        os.remove(path)

    @pytest.mark.parametrize('obj', ([word_generator(5)] for _ in range(50)))
    def test_object_does_not_exist(self, obj):
        db = 'test'
        col = 'col'
        create_db(db)
        create_collection(db, col, ['o'])
        path = os.path.join(db + '.json')

        with pytest.raises(DropError):
            drop_object(db, col, obj[0])
        os.remove(path)

    @pytest.mark.parametrize('col', (word_generator(5) for _ in range(50)))
    def test_collection_does_not_exist(self, col):
        db = 'test'
        create_db(db)
        create_collection(db, 'col', ['o'])
        path = os.path.join(db + '.json')

        with pytest.raises(DropError):
            drop_object(db, col, 'o')
        os.remove(path)

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_db_does_not_exist(self, db):
        col = 'test'
        create_db(db)
        create_collection(db, 'col', ['o'])
        path = os.path.join(db + '.json')

        with pytest.raises(DropError):
            drop_object(db, col, 'o')
        os.remove(path)

    @pytest.mark.parametrize('obj', (int, True, list, set, tuple))
    def test_object_is_non_str(self, obj):
        db = 'test'
        create_db(db)
        create_collection(db, 'col', ['o'])
        path = os.path.join(db + '.json')

        with pytest.raises(ValueError):
            drop_object(db, 'col', obj)
        os.remove(path)

    @pytest.mark.parametrize('col', (int, True, list, set, tuple))
    def test_collection_is_non_str(self, col):
        db = 'test'
        create_db(db)
        create_collection(db, 'col', ['o'])
        path = os.path.join(db + '.json')

        with pytest.raises(ValueError):
            drop_object(db, col, 'obj')
        os.remove(path)

    @pytest.mark.parametrize('name', (int, True, list, set, tuple))
    def test_db_is_non_str(self, name):
        db = 'test'
        create_db(db)
        create_collection(db, 'col', ['o'])
        path = os.path.join(db + '.json')

        with pytest.raises(ValueError):
            drop_object(name, 'col', 'obj')
        os.remove(path)
