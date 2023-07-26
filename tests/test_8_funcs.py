import os
import json
from DBLite3._funcs import _open_db, _save_db
from DBLite3._exceptions import SaveError

import pytest


class Test_SaveDb:
    #  Tests that a valid database can be saved
    def test_save_valid_db(self):
        db_name = 'test_db'
        DB = {'key': 'value'}
        _save_db(db_name, DB)
        with open(f'{db_name}.json', 'r') as db:
            assert json.load(db) == DB

    #  Tests that an empty database can be saved
    def test_save_empty_db(self):
        db_name = 'test_db'
        DB = {}
        _save_db(db_name, DB)
        with open(f'{db_name}.json', 'r') as db:
            assert json.load(db) == DB

    #  Tests that an error is raised when saving a database with an invalid name
    def test_save_db_invalid_name(self):
        db_name = 123
        DB = {'key': 'value'}
        with pytest.raises(TypeError):
            _save_db(db_name, DB)

    #  Tests that an error is raised when saving a database with non-serializable objects
    def test_save_db_non_serializable_objects(self):
        db_name = 'test_db'
        DB = {'key': set()}
        with pytest.raises(TypeError):
            _save_db(db_name, DB)

    #  Tests that an error is raised when saving a database with circular references
    def test_save_db_circular_references(self):
        db_name = 'test_db'
        DB = {'key': None}
        DB['key'] = DB
        with pytest.raises(TypeError):
            _save_db(db_name, DB)

    #  Tests that an existing database with the same name is overwritten
    def test_save_db_overwrite_existing(self):
        db_name = 'test_db'
        DB = {'key': 'value'}
        _save_db(db_name, DB)
        DB2 = {'key2': 'value2'}
        _save_db(db_name, DB2)
        with open(f'{db_name}.json', 'r') as db:
            assert json.load(db) == DB2

    #  Tests that a new file is created when saving a database with a new name
    def test_save_db_create_new(self):
        db_name = 'test_db'
        DB = {'key': 'value'}
        _save_db(db_name, DB)
        db_name2 = 'test_db2'
        DB2 = {'key2': 'value2'}
        _save_db(db_name2, DB2)
        with open(f'{db_name}.json', 'r') as db:
            assert json.load(db) == DB
        with open(f'{db_name2}.json', 'r') as db:
            assert json.load(db) == DB2

    #  Tests that a TypeError is raised when db_name is not a string
    def test_save_db_type_error_db_name(self):
        db_name = 123
        DB = {'key': 'value'}
        with pytest.raises(TypeError):
            _save_db(db_name, DB)

    #  Tests that a TypeError is raised when DB is not a dictionary
    def test_save_db_type_error_DB(self):
        db_name = 'test_db'
        DB = 'not a dictionary'
        with pytest.raises(TypeError):
            _save_db(db_name, DB)

    #  Tests that a SaveError is raised when a file operation error occurs
    def test_save_db_file_error(self):
        db_name = 'test_db'
        DB = {'key': 'value'}
        with pytest.raises(SaveError):
            _save_db(db_name, DB)

    #  Tests that the saved file has the correct name and extension
    def test_save_db_file_name(self):
        db_name = 'test_db'
        DB = {'key': 'value'}
        _save_db(db_name, DB)
        assert os.path.isfile(f'{db_name}.json')

    #  Tests that the saved file contains the correct JSON representation of the dictionary
    def test_save_db_file_content(self):
        db_name = 'test_db'
        DB = {'key': 'value'}
        _save_db(db_name, DB)
        with open(f'{db_name}.json', 'r') as db:
            assert json.load(db) == DB
