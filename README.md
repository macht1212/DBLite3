
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

#### ADDITION INFO
```python
def create_db(db_name: str) -> None:
    """
    The function creates a database in the base directory of the project
    :param  db_name: the name of the database to be created. The name of the database must be unique in the project,
            otherwise the file will be overwritten. Data is passed to the function as a string
    :return: None
    """
    pass
```

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

#### ADDITION INFO
```python
def create_table(db_name: str, table_name: str, collections: list) -> None:
    """
    The function creates a table with collections
    :param  db_name: the selected database to create the table. Data is passed to the function as a string
    :param  table_name: table name. IMPORTANT! The table name must be unique. Data is passed to the function as a string
    :param  collections: collection name. A collection is similar to a column in a classic relational database, but at
            the same time it does not require a clear fixation of data relative to other such collections. Data is
            passed to the function as a list
    :return: None
    """
    pass
```

### INSERT

To insert one new value to DataBase you need call *.insert_one* method from INSERT module 
```python
from LiteDB.INSERT import insert_one
```
and pass to method db name, table name, collection and value.

Example::

    >>> from LiteDB.INSERT import insert_one
    >>> insert_one(db_name='new_db', table_name='table', collection='coll', value='some value')

#### ADDITION INFO
```python
def insert_one(db_name: str, table_name: str, collection: str, value) -> None:
    """
    The function adds one value to the collection, the value is entered into a separate list, which has its own serial
    number, calculated relative to the last serial number of the value.
    :param collection: The name of the collection to add the value to
    :param table_name: The name of the table to add the value to
    :param db_name: The name of the database to add the value to
    :param value: The value to be entered into the database
    :return: None
    """
    pass
```


To insert many new values to DataBase you need call *.insert_many* method from INSERT module 
```python
from LiteDB.INSERT import insert_many
```
and pass to method db name, table name, collection and values.

Example::

    >>> from LiteDB.INSERT import insert_many
    >>> insert_one(db_name='new_db', table_name='table', collection='coll', values=['some value'])

#### ADDITION INFO
```python
def insert_many(db_name: str, table_name: str, collection: str, values: list) -> None:
    """
    The function adds many values to the collection, the value is entered into a separate list, which has its own serial
    number, calculated relative to the last serial number of the value.
    :param db_name: The name of the database to add values to
    :param table_name: The name of the table to add values to
    :param collection: The name of the collection to add values to
    :param values: The values to be entered into the database
    :return: None
    """
    pass
```


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

#### ADDITION INFO
```python
def update_value_by_id(db_name: str, table_name: str, collection: str, id: int, value) -> None:
    """
    The function updates the single value by the given identifier
    :param db_name: the name of the database to be modified
    :param table_name: the name of the table to be modified
    :param collection: the name of the collection to be modified
    :param id: identifier of the value to be modified
    :param value: new value
    :return: None
    """
    pass
```    
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
      
#### ADDITION INFO
```python
def update_values_by_id(db_name: str, table_name: str, collection: str, id: list, values: list) -> None:
    """
    The function updates the many values by the given identifiers
    :param db_name: the name of the database to be modified
    :param table_name: the name of the table to be modified
    :param collection: the name of the collection to be modified
    :param id: list of identifiers of the values to be modified
    :param values: list of the new values
    :return: None
    """
    pass
```          
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

To drop the database, table or collection, use the DROP module.

To drop database, you need to import the *.drop_db method* from the DROP module. 
```python
from LiteDB.DROP import drop_db
```

In this method, you must pass the name of the database.

Example::

    >>> from LiteDB.DROP import drop_db
    >>> drop_db(db_name='new')


To drop table from database, you need to import the *.drop_db* method from the DROP module.
```python
from LiteDB.DROP import drop_table
```

In this method, you must pass the name of the database and the name of the
table.

Example::

    >>> from LiteDB.DROP import drop_table
    >>> drop_db(db_name='new', table_name='table')

To drop collection from database, you need to import the *.drop_collection* method from the DROP module.
```python
from LiteDB.DROP import drop_collection
```

In this method, you must pass the name of the database, the name of the
table and the name of the collection.

Example::

    >>> from LiteDB.DROP import drop_collection
    >>> drop_db(db_name='new', table_name='table', collection='coll')

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



