
# ![Icon](img/account_tree_FILL0_wght400_GRAD0_opsz48.svg) LiteDB
![Static Badge](https://img.shields.io/badge/LiteDB-v0.1.0-blue)


LiteDB is NoSQL database.
LiteDB could be used as simple DB for simple projects.
This DB creates file with file extension **.json** (JavaScript Object Notification).

## Documentation

All information is stored in collections which contain objects.

### CREATE
To create new DataBase you need call *.create_db* method from **create** module

```python
from LiteDB.create import create_db
```
and pass to method db name. If database with this name has already existed, the Error will raise to console but
program will continue working.

Example (DB does not exist)::

    >>> from LiteDB.create import create_db
    >>> create_db(db_name='new')
    'DataBase db_name was created.'

Example (DB exists)::

    >>> from LiteDB.create import create_db
    >>> create_db(db_name='new')
    'DATABASE with name new has already existed'

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

To create collection you need call *.create_collection* method from **create** module

```python
from LiteDB.create import create_collection
```
and pass to method db name, table name and list of collections. If table with this name has already existed,
the Error will raise to console but program will continue working.

Example (Table does not exist)::  

    >>> from LiteDB.create import create_collection
    >>> create_collection(db_name='new', collection='col', objects=['o1', 'o2'])
    'Collection col with objects: o1, o2 was created.'

Example (Table exists)::

    >>> from LiteDB.create import create_collection
    >>> create_collection(db_name='new', collection='col', objects=['o1', 'o2'])
    'Collection with this name has already existed'

#### ADDITION INFO
```python
def create_table(db_name: str, collection: str, objects: list) -> None:
    """
    The function creates a table with collections
    :param  db_name: the selected database to create the table. Data is passed to the function as a string
    :param  collection: collection name. IMPORTANT! The table name must be unique. Data is passed to the function as a string
    :param  objects: objects names. A collection is similar to a column in a classic relational database, but at
            the same time it does not require a clear fixation of data relative to other such collections. Data is
            passed to the function as a list
    :return: None
    """
    pass
```

### INSERT

To insert one new value to DataBase you need call *.insert_one* method from **insert** module

```python
from LiteDB.insert import insert_one
```
and pass to method db name, collection name, object and value.

Example::

    >>> from LiteDB.insert import insert_one
    >>> insert_one(db_name='new_db', collection='coll', object='o1', value='some value')

#### ADDITION INFO
```python
def insert_one(db_name: str, collection: str, object: str, value) -> None:
    """
    The function adds one value to the collection, the value is entered into a separate list, which has its own serial
    number, calculated relative to the last serial number of the value.
    :param object: The name of the object to add the value to
    :param collection: The name of the collection to add the value to
    :param db_name: The name of the database to add the value to
    :param value: The value to be entered into the database
    :return: None
    """
    pass
```


To insert many new values to DataBase you need call *.insert_many* method from **insert** module

```python
from LiteDB.insert import insert_many
```
and pass to method db name, collection name, object and values.

Example::

    >>> from LiteDB.insert import insert_many
    >>> insert_one(db_name='new_db', collection='table', object='coll', values=['some value'])

#### ADDITION INFO
```python
def insert_many(db_name: str, collection: str, object: str, values: list) -> None:
    """
    The function adds many values to the collection, the value is entered into a separate list, which has its own serial
    number, calculated relative to the last serial number of the value.
    :param db_name: The name of the database to add values to
    :param collection: The name of the collection to add values to
    :param object: The name of the object to add values to
    :param values: The values to be entered into the database
    :return: None
    """
    pass
```


### UPDATE

To update values in the database, use the **update** module, which implements four methods to update data by their ID.

To update a single value by its ID, you need to import the *.update_value_by_id* method from the **update** module.

```python
from LiteDB.update import update_value_by_id
```

In this method, you must pass the name of the database, the name of the collection, the name of the object and the 
identifier of the value to be replaced, as well as the new value.

Example::
    
    >>> from LiteDB.UPDATE import update_value_by_id
    >>> update_value_by_id(db_name='new', collection='table', object='coll', id=1, value='some new value')

#### ADDITION INFO
```python
def update_value_by_id(db_name: str, collection: str, object: str, id: int, value) -> None:
    """
    The function updates the single value by the given identifier
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be modified
    :param object: the name of the object to be modified
    :param id: identifier of the value to be modified
    :param value: new value
    :return: None
    """
    pass
```    
To update a few values by their ID, you need to import the *.update_values_by_id* method from the **update** module.

```python
from LiteDB.update import update_values_by_id
```

In this method, you must pass the name of the database, the name of the 
table, the name of the collection and the identifiers of the values (list) to be replaced, as well as the new 
values (list).

Example::
    
    >>> from LiteDB.UPDATE import update_values_by_id
    >>> update_values_by_id(db_name='new', collection='table', object='coll', id=[1, 2], 
                            value=['some new value', 'second new value'])
      
#### ADDITION INFO
```python
def update_values_by_id(db_name: str, collection: str, object: str, id: list, values: list) -> None:
    """
    The function updates the many values by the given identifiers
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be modified
    :param object: the name of the object to be modified
    :param id: list of identifiers of the values to be modified
    :param values: list of the new values
    :return: None
    """
    pass
```

### ALTER

To change an object in the database, you need to call the *.alter_object* method from the **alter** module 
```python
from LiteDB.alter import alter_object
```
and pass the method name of db, collection name and old and new object name. 

Example::

    >>> from LiteDB.alter import alter_object
    >>> alter_object(db_name='new_db', collection='table', object_old='coll1', object_new='col2')

#### ADDITION INFO
```python
def alter_object(db_name: str, collection: str, object_old: str, object_new: str) -> None:
    """
    The function makes changes to the name of the object
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be modified
    :param object_old: the old name of the object to be modified
    :param object_new: the new name of the object to be modified
    :return: None
    """
    pass
```

To change a collection in the database, you need to call the *.alter_collection* method from the **alter** module (from 
alter import alter_collection) and pass the method name of db and old and new collection name. 

Example::

    >>> from LiteDB.alter import alter_collection
    >>> alter_collection(db_name='new_db', collection_new='table2', collection_old='table1')

#### ADDITION INFO
```python
def alter_collection(db_name: str, collection_new: str, collection_old: str) -> None:
    """
    The function makes changes to the name of the collection
    :param db_name: the name of the database to be modified
    :param collection_new: the new name of the collection to be modified
    :param collection_old: the old name of the collection to be modified
    :return: None
    """
    pass
```

To change a name of the database, you need to call the *.alter_db* method from the **alter** module (from alter 
import alter_db) and pass the method name of db.  

Example::

    >>> from LiteDB.alter import alter_db
    >>> alter_db(db_name='new_db')

#### ADDITION INFO
```python
def alter_db(db_name: str) -> None:
    """
    The function makes changes to the name of the database
    :param db_name: the name of the database to be modified
    :return: None
    """
    pass
```

### DROP/DELETE

To drop database, you need to import the *.drop_db method* from the **drop** module.

```python
from LiteDB.drop import drop_db
```

In this method, you must pass the name of the database.

Example::

    >>> from LiteDB.DROP import drop_db
    >>> drop_db(db_name='new')


#### ADDITION INFO
```python
def drop_db(db_name: str) -> None:
    """
    The function deletes the database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be dropped
    :return: None
    """
    pass
```


To drop collection from database, you need to import the *.drop_db* method from the **drop** module.

```python
from LiteDB.drop import drop_collection
```

In this method, you must pass the name of the database and the name of the
table.

Example::

    >>> from LiteDB.DROP import drop_tcollection
    >>> drop_db(db_name='new', collection='col')

#### ADDITION INFO
```python
def drop_table(db_name: str, collection: str) -> None:
    """
    The function deletes the table from database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be dropped
    :return: None
    """
    pass
```


To drop object from database, you need to import the *.drop_collection* method from the **drop** module.

```python
from LiteDB.drop import drop_object
```

In this method, you must pass the name of the database, the name of the collection and the name of the object.

Example::

    >>> from LiteDB.DROP import drop_collection
    >>> drop_db(db_name='new', collection='table', object='coll')

#### ADDITION INFO
```python
def drop_collection(db_name: str, collection: str, object: str) -> None:
    """
    The function deletes the collection from database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be modified
    :param object: the name of the object to be dropped
    :return: None
    """
    pass
```


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



