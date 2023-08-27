import os
import pytest

from DBLite3._funcs import _open_db, _save_db, _get_value_index, _count, _db_exists, _collection_exists, \
    _object_exists, _is_value_in

from _test import word_generator


class TestOpenDB:

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, db):
        with open(os.path.join(db + '.json'), 'w') as f:
            f.write('{}')

        assert os.path.isfile(os.path.join('./' + db + '.json'))
        dict_ = _open_db(db)
        assert dict_ == {}
        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_db_does_not_exist(self, db):
        with pytest.raises(FileNotFoundError):
            _open_db(db)


class TestSaveDB:

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, db):
        with open(os.path.join(db + '.json'), 'w') as f:
            f.write('{}')

        data = {
            "test": "result"
        }

        _save_db(db, data)

        DB = _open_db(db)
        assert DB == {"test": "result"}
        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_db_does_not_exist(self, db):
        with pytest.raises(FileNotFoundError):
            _save_db(db, {'1': '2'})


class TestGetValueIndex:

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, db):
        with open(os.path.join(db + '.json'), 'w') as f:
            f.write('{"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}')

        for i in range(1, 4):
            index = _get_value_index(db, 'coll', 'o', i)
            assert index == i - 1

        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('col', (word_generator(5) for _ in range(50)))
    def test_collection_does_not_exist(self, col):
        db = 'test'
        with open(os.path.join(db + '.json'), 'w') as f:
            f.write('{"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}')

        with pytest.raises(ValueError):
            _get_value_index(db, col, 'o', id=1)
        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('obj', (word_generator(5) for _ in range(50)))
    def test_object_does_not_exist(self, obj):
        db = 'test'
        with open(os.path.join(db + '.json'), 'w') as f:
            f.write('{"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}')

        with pytest.raises(ValueError):
            _get_value_index(db, 'coll', obj, id=1)
        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('id_', (word_generator(5) for _ in range(50)))
    def test_invalid_id(self, id_):
        db = 'test'
        with open(os.path.join(db + '.json'), 'w') as f:
            f.write('{"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}')

        assert not _get_value_index(db, 'coll', 'o', id_)

        os.remove(os.path.join(db + '.json'))


class TestCount:

    def test_value_in(self):
        data = {"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, 3]]}}}

        assert _count(data, 'coll', 'o') == 3

    def test_value_not_in(self):
        data = {"coll": {"o": {"values": []}}}

        assert _count(data, 'coll', 'o') == 0


class TestDBExists:

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_positive_case(self, db):
        with open(os.path.join(db + '.json'), 'w') as f:
            f.write('{}')

        assert _db_exists(db)
        os.remove(os.path.join(db + '.json'))

    @pytest.mark.parametrize('db', (word_generator(5) for _ in range(50)))
    def test_negative_case(self, db):
        assert not _db_exists(db)


class TestCollectionExists:

    def test_positive_case(self):
        data = {"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}

        assert _collection_exists('coll', data)

    def test_negative_case(self):
        data = {"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}

        assert not _collection_exists('col', data)


class TestObjectExists:

    def test_positive_case(self):
        data = {"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}

        assert _object_exists('coll', 'o', data)

    def test_negative_case(self):
        data = {"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}

        assert not _object_exists('coll', 'oo', data)


class TestIsValueIn:

    def test_positive_case(self):
        data = {"coll": {"o": {"values": [[1, "1"], [2, "2"], [3, "3"]]}}}

        assert _is_value_in(data, 'coll', 'o')

    def test_negative_case(self):
        data = {"coll": {"o": {"values": []}}}

        assert not _is_value_in(data, 'coll', 'o')
