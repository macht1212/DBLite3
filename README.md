
# LiteDB

LiteDB is NoSQL database.
LiteDB could be used as simple DB for simple projects.
This DB creates file with file extension .json (JavaScript Object Notification).

## Documentation

All information is stored in tables which contain collections.

### CREATE
To create new DataBase you need call *.create_db* method from CREATE module 
```python
from LiteDB.CREATE import create_db
```
and pass to method db name. If database with this name has already existed, the Error will raise to console but
program will continue working.

Example (DB does not exist)::

    >>> from CREATE import create_db
    >>> create_db(db_name)
    'DataBase db_name was created.'

Example (DB exists)::

    >>> from CREATE import create_db
    >>> create_db(db_name)
    'DATABASE with this name has already existed'

To create table  you need call *.create_table* method from CREATE module 

```python
from LiteDB.CREATE import create_table
```
and pass to method db name, table name and list of collections. If table with this name has already existed,
the Error will raise to console but program will continue working.

Example (Table does not exist)::  

    >>> from CREATE import create_table
    >>> create_table(db_name, table_name, collections)
    'Table table_name with collections: col, col was created.'

Example (Table exists)::

    >>> from CREATE import create_table
    >>> create_table(db_name, table_name, collections)
    'Table with this name has already existed'

### INSERT

To insert one new value to DataBase you need call *.insert_one* method from INSERT module 
```python
from LiteDB.INSERT import insert_one
```
and pass to method db name, table name, collection and value.

Example::

    >>> from LiteDB.INSERT import insert_one
    >>> insert_one(db_name='new_db', table_name='table', collection='coll', value='some value')

To insert many new values to DataBase you need call *.insert_many* method from INSERT module 
```python
from LiteDB.INSERT import insert_many
```
and pass to method db name, table name, collection and values.

Example::

    >>> from LiteDB.INSERT import insert_many
    >>> insert_one(db_name='new_db', table_name='table', collection='coll', values=['some value'])

### UPDATE

To update values in the database, use the UPDATE module, which implements four methods to update data by their ID or 
by their old name.

To update a single value by its ID, you need to import the *.update_value_by_id* method from the UPDATE module.
```python
from LiteDB.UPDATE import update_value_by_id
```

In this method, you must pass the name of the database, the name of the table, the name of the collection and the identifier of the value to be replaced, as well as the new value.

Example::
    
    >>> from LiteDB.UPDATE import update_value_by_id
    >>> update_value_by_id(db_name='new', table_name='table', collection='coll', id=1, value='some new value')
    
To update a few values by their ID, you need to import the *.update_values_by_id* method from the UPDATE module.
```python
from LiteDB.UPDATE import update_values_by_id
```

In this method, you must pass the name of the database, the name of the 
table, the name of the collection and the identifiers of the values (list) to be replaced, as well as the new 
values (list).

Example::
    
    >>> from LiteDB.UPDATE import update_values_by_id
    >>> update_values_by_id(db_name='new', table_name='table', collection='coll', id=[1, 2], 
                            value=['some new value', 'second new value'])
                
To update a single value by its old name, you need to import the *.update_new_value_by_old_value* method from the UPDATE 
module. 
```python
from LiteDB.UPDATE import update_new_value_by_old_value
```

In this method, you must pass the name of the 
database, the name of the table, the name of the collection and the old name of the value to be replaced, as well as 
the new value.

Example::
    
    >>> from LiteDB.UPDATE import update_new_value_by_old_value
    >>> update_value_by_id(db_name='new', table_name='table', collection='coll',
                            old_value='old', new_value='some new value')
    
To update a few values by their old names, you need to import the *.update_new_values_by_old_values* method from the 
UPDATE module. 
```python
from LiteDB.UPDATE import update_new_values_by_old_values
```
In this method, you must pass the name of 
the database, the name of the table, the name of the collection and the old names of the values (list) to be replaced,
as well as the new values (list).

Example::
    
    >>> from LiteDB.UPDATE import update_new_values_by_old_values
    >>> update_new_values_by_old_values(db_name='new', table_name='table', collection='coll', 
                            old_value=['old1', 'old2'], new_value=['some new value', 'second new value'])

### ALTER

### DROP/DELETE

## Installation

Install my-project with pip

```bash
  pip install litedb
```
    
## Authors

- [@macht1212](https://www.github.com/macht1212) Alexander Nazimov


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Lessons Learned



