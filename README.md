
# LiteDB

A simple NoSQL database for simple Projects.  



## Documentation

LiteDB is NoSQL database.
LiteDB could be used as simple DB for simple projects.
This DB creates file with file extension .json (JavaScript Object Notification).

All information is stored in tables which contain collections.

### CREATE
To create new DataBase you need call .create_db method from CREATE module 
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

To create table  you need call .create_table method from CREATE module 

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

### UPDATE

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

What did you learn while building this project? What challenges did you face and how did you overcome them?

