
# ![Icon](img/icon.svg) DBLite3

![Static Badge](https://img.shields.io/badge/LiteDB-v0.1.4-blue)


DBLite3 is NoSQL database.
DBLite3 could be used as simple DB for simple projects.
This DB creates file with file extension **.json** (JavaScript Object Notification).

## Documentation

All information is stored in collections which contain objects.  
All methods are allowed with common import:

```python
import DBLite3
```
but you can only import the required methods individually.  


### CREATE
To create new DataBase you need call *.create_db* method:

```python
from DBLite3 import create_db
```
and pass to method db name. If database with this name has already existed, the Error will raise to console.

Example (DB does not exist)::

    >>> from DBLite3 import create_db
    >>> create_db(db_name='name')

Example (DB exists)::

    >>> from DBLite3 import create_db
    >>> create_db(db_name='name')
    raise CreationError(f'DATABASE with name: {db_name} has already existed')
    NoSQLite3._exceptions.CreationError: DATABASE with name: name has already existed

You can also use optional parameter "if_exists" to bypass the display of the exception, but a new database with an 
already existing name will not be created.

#### ADDITION INFO
```python
def create_db(db_name: str, if_exists: bool = False) -> None:
    """
    The function creates a database in the base directory of the project
    :param  if_exists: an optional parameter responsible for skipping an exception when creating a database with an
            already existing name
    :param  db_name: the name of the database to be created. The name of the database must be unique in the project,
            otherwise the file will be overwritten. Data is passed to the function as a string
    :return: None
    """
    pass
```

To create collection you need call *.create_collection* method:

```python
from DBLite3 import create_collection
```
and pass to method db name, collection name and list of collections. If collection with this name has already existed,
the Error will raise to console but program will continue working.

Example (Collection does not exist)::  

    >>> from DBLite3 import create_collection
    >>> create_collection(db_name='name', collection='col', objects=['o1', 'o2'])

Example (Collection exists)::

    >>> from DBLite3 import create_collection
    >>> create_collection(db_name='name', collection='col', objects=['o1', 'o2'])
    raise CreationError(f'Collection with name: {collection} has already existed')
    NoSQLite3._exceptions.CreationError: Collection with name: col has already existed

#### ADDITION INFO
```python
def create_collection(db_name: str, collection: str, objects: list) -> None:
    """
    The function creates a collection with collections
    :param  db_name: the selected database to create the collection. Data is passed to the function as a string
    :param  collection: collection name. IMPORTANT! The collection name must be unique. Data is passed to the function as a string
    :param  objects: objects names. A collection is similar to a column in a classic relational database, but at
            the same time it does not require a clear fixation of data relative to other such collections. Data is
            passed to the function as a list
    :return: None
    """
    pass
```

### INSERT

To insert one new value to DataBase you need call *.insert_one* method:

```python
from DBLite3 import insert_one
```
and pass to method db name, collection name, object and value.

Example::

    >>> from DBLite3 import insert_one
    >>> insert_one(db_name='name', collection='col', object='o1', value='val')

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


To insert many new values to DataBase you need call *.insert_many* method:

```python
from DBLite3 import insert_many
```
and pass to method db name, collection name, object and values.

Example::

    >>> from DBLite3 import insert_many
    >>> insert_many(db_name='name', collection='col', object='o1', values=['val1', 'val2'])


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
To update a single value by its ID, you need to import the *.update_value_by_id* method:

```python
from DBLite3 import update_value_by_id
```

In this method, you must pass the name of the database, the name of the collection, the name of the object and the 
identifier of the value to be replaced, as well as the new value.

Example::

    >>> from DBLite3 import update_value_by_id
    >>> update_value_by_id(db_name='name', collection='col', object='o1', id=1, value='val2')


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
To update a few values by their ID, you need to import the *.update_values_by_id* method:

```python
from DBLite3 import update_values_by_id
```

In this method, you must pass the name of the database, the name of the collection, the name of the collection and the identifiers of the values (list) to be replaced, as well as the new 
values (list).

Example::
    
    >>> from DBLite3 import update_values_by_id
    >>> update_values_by_id(db_name='name', collection='col', object='o1', id=[1, 2], values=['val1', 'val2'])

      
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

To change an object in the database, you need to call the *.alter_object* method:

```python
from DBLite3 import alter_object
```
and pass the method name of db, collection name and old and new object name. 

Example::

    >>> from DBLite3 import alter_object
    >>> alter_object(db_name='name', collection='col', object_old='o1', object_new='o3')


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

To change a collection in the database, you need to call the *.alter_collection* method:

```python
from DBLite3 import alter_collection
```
and pass the method name of db and old and new collection name. 

Example::

    >>> from DBLite3 import alter_collection
    >>> alter_object(db_name='name', collection_old='col1', collection_new='col3')


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

To change a name of the database, you need to call the *.alter_db* method:

```python
from DBLite3 import alter_db
```
and pass the method old and new names of db.  

Example::
    
    >>> from DBLite3 import alter_db
    >>> alter_object(db_name_old='name1', db_name_new='name2')


#### ADDITION INFO
```python
def alter_db(db_name_old: str, db_name_new: str) -> None:
    """
    The function makes changes to the name of the database
    :param db_name_old: the old name of the database to be modified
    :param db_name_new: the new name of the database to be modified
    :return: None
    """
    pass
```

### SELECT

To select all values with indexes from Database use *.select_all_values_with_index* method

### DROP/DELETE

To drop database, you need to import the *.drop_db* method:

```python
from DBLite3 import drop_db
```

In this method, you must pass the name of the database.

Example::

    >>> from DBLite3 import drop_db
    >>> drop_db(db_name='name')


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


To drop collection from database, you need to import the *.drop_db* method:

```python
from DBLite3 import drop_collection
```

In this method, you must pass the name of the database and the name of the collection.

Example::
    
    >>> from DBLite3 import drop_collection
    >>> drop_collection(db_name='name', collection='col')


#### ADDITION INFO
```python
def drop_collection(db_name: str, collection: str) -> None:
    """
    The function deletes the collection from database. IMPORTANT! Using this feature will result in data loss
    :param db_name: the name of the database to be modified
    :param collection: the name of the collection to be dropped
    :return: None
    """
    pass
```


To drop object from database, you need to import the *.drop_collection* method from the **drop** module.

```python
from DBLite3 import drop_object
```

In this method, you must pass the name of the database, the name of the collection and the name of the object.

Example::

    >>> from DBLite3 import drop_object
    >>> drop_object(db_name='name', collection='col', object='o1')


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
  pip install DBLite3
```


## RoadMap
* Add a few variants of inserts (one-in-one, one-in-many, many-to-one, many-to-many)
* Add description field to *.create_db* method (optional)
* Add restrictions to values (uniqueness, insertion restriction, data type restriction)
* Using any data encryption library, implement a secure way to work with the database
* Add the ability to select values from all collections and objects together and compare



## Authors

- [@macht1212](https://www.github.com/macht1212) Alexander Nazimov


## License

[MIT](https://github.com/macht1212/LiteDB/blob/0711686a88e82182ed37199da73cea1b7595a75d/LICENSE.txt)


[//]: # (## Lessons Learned)



