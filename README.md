
# ![Icon](img/icon.svg) DBLite3

![Static Badge](https://img.shields.io/badge/LiteDB-v0.2.0-blue)


DBLite3 is NoSQL self.
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
and pass to method db name. If self with this name has already existed, the Error will raise to console.

```python
def create_db(db_name: str, if_exists: bool = False) -> None:
    """
    Objective: 
    The objective of the create_db function is to create a new self in the base directory of the 
    project. The function takes in the name of the self as a string and an optional boolean parameter if_exists, 
    which is responsible for skipping an exception when creating a self with an already existing name. 
    
    Inputs:
        - db_name (str): the name of the self to be created. The name of the self must be unique in the project, otherwise the file will be overwritten.
        - if_exists (bool): an optional parameter responsible for skipping an exception when creating a self with an already existing name.
    
    Flow:
        - The function first checks if the self already exists using the _db_exists function.
        - If the self exists and if_exists is True, the function does nothing and returns None.
        - If the self exists and if_exists is False, the function raises a CreationError with a message indicating that the self already exists.
        - If the self does not exist, the function creates a new JSON file with the name of the self and writes an empty dictionary to it.
    
    Outputs:
        - None: the function does not return anything.
    
    Additional aspects:
        - The function uses the _db_exists function to check if the self already exists.
        - The function raises a CreationError if the self already exists and if_exists is False.
        - The function writes an empty dictionary to the new JSON file to initialize it.
        - The function assumes that the self is stored in a JSON file with the same name as the self name.
    """
    pass
```

To create collection you need call *.create_collection* method:

```python
from DBLite3 import create_collection
```
and pass to method db name, collection name and list of collections. If collection with this name has already existed,
the Error will raise to console but program will continue working.

```python
def create_collection(db_name: str, collection: str, objects: list) -> None:
    """
    Objective:
    The objective of the function is to create a new collection in a given self with a unique name and a list of objects. The function checks if the collection already exists and raises an error if it does. Otherwise, it creates a new collection with the given objects and saves it to the self.
    
    Inputs:
        - db_name: a string representing the name of the self where the collection will be created.
        - collection: a string representing the name of the new collection to be created.
        - objects: a list of strings representing the names of the objects to be added to the new collection.
    
    Flow:
        - The function opens the self with the given name using the _open_db function.
        - The function checks if the collection already exists in the self using the _does_collection_exists function. If it does, the function raises a CreationError.
        - If the collection does not exist, the function creates a new collection in the self with the given name and objects.
        - The function saves the updated self using the _save_db function.
    
    Outputs:
        - None: the function does not return anything.
    
    Additional aspects:
        - The function assumes that the self already exists and has been parsed into a dictionary.
        - The function only creates a new collection and does not perform any other operations on it.
        - The function overwrites the existing self file with the updated version.
    """
    pass
```


To create object you need call *.create_collection* method:

```python
from DBLite3 import create_object
```
and pass to method db name, collection name, collection name and object name. If collection with this name has already existed,
the Error will raise to console but program will continue working.

```python
def create_object(db_name: str, collection: str, object: str) -> None:
    """
    Objective:
    The objective of the function is to create a new object in a specified collection of a given self. The function checks if the object already exists in the collection and raises an error if it does. Otherwise, it adds the object to the collection with an empty 'values' field and saves the updated self.

    Inputs:
        - db_name: a string representing the name of the self to which the object is to be added.
        - collection: a string representing the name of the collection in which the object is to be added.
        - object: a string representing the name of the object to be added.

    Flow:
        - The function first opens the self using the _open_db function.
        - It then checks if the object already exists in the specified collection using the _object_exists function. If it does, the function raises a CreationError with an appropriate message.
        - If the object does not exist, the function adds the object to the collection with an empty 'values' field.
        - Finally, the updated self is saved using the _save_db function.

    Outputs:
        - None: the function does not return anything.

    Additional aspects:
        - The function assumes that the self already exists and has been parsed into a dictionary format.
        - The function only adds the object to a single collection and does not check for the existence of the collection itself.
        - The function does not handle any errors that may occur during the file operations.
    """
    pass
```

### INSERT

To insert one new value to one collection you need call *.insert_one_in_one_collection* method:

```python
from DBLite3 import insert_one_in_one_collection
```
and pass to method db name, collection name, object and value.


```python
def insert_one_in_one_collection(db_name: str, collection: str, object: str, value) -> None:
    """
    Objective:
    The objective of the 'insert_one_in_one_collection' function is to add a single value to a collection in a self. The function creates a new list for the value, with a serial number calculated relative to the last serial number of the value.
    
    Inputs:
        - db_name: a string representing the name of the self to add the value to
        - collection: a string representing the name of the collection to add the value to
        - object: a string representing the name of the object to add the value to
        - value: any type of value to be added to the self
    
    Flow:
        - Open the self using the '_open_db' function
        - Check if the first entry in the collection exists using the '_is_value_in' function
        - If the first entry does not exist, create a new list for the value with a serial number of 1
        - If the first entry exists, calculate the serial number of the new value relative to the last serial number of the value and add it to the list
        - Save the updated self using the '_save_db' function
    
    Outputs:
        - None
    
    Additional aspects:
        - The function assumes that the self, collection, and object already exist
        - The function does not handle any errors that may occur during the self operations
    """
    pass
```


To insert many new values to one collection you need call *.insert_many_in_one_collection* method:

```python
from DBLite3 import insert_many_in_one_collection
```
and pass to method db name, collection name, object and values.


```python
def insert_many_in_one_collection(db_name: str, collection: str, object: str, values: list) -> None:
    """
    Objective:
    The objective of the function is to add multiple values to a collection in a given self. The values are added to a separate list within the collection, with each value having its own serial number relative to the last serial number of the value.

    Inputs:
        - db_name: a string representing the name of the self to add values to
        - collection: a string representing the name of the collection to add values to
        - object: a string representing the name of the object to add values to
        - values: a list of values to be added to the self

    Flow:
        - Open the self using the _open_db function
        - Check if the collection already has values by accessing the 'values' key of the object in the collection
        - If the collection has values, set the count variable to the last serial number of the value
        - If the collection does not have values, set the count variable to 0
        - Check if the first entry in the collection exists using the _is_value_in function
        - If the first entry does not exist, append each value to the 'values' list with a serial number calculated relative to the last serial number of the value
        - If the first entry exists, append each value to the 'values' list with a serial number calculated relative to the last serial number of the value + 1
        - Save the updated self using the _save_db function

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the 'values' key exists in the object in the collection
        - The function overwrites the existing file with the same name if it already exists
        - The function does not handle any errors that may occur during the file operations
    """
    pass
```

To insert one value to many collections you need to use the *.insert_one_in_many_collections* method:
```python
from DBLite3 import insert_one_in_many_collections
```
and pass the method self name, list of collections, object name and values.


```python
def insert_one_in_many_collections(db_name: str, collections: list, object: str, value: Any) -> None:
    """
    Objective:
    The objective of the 'insert_one_in_many_collections' function is to insert a single value into multiple collections and objects in a self. The function takes in the name of the self, a list of collection names, an object name, and a value to be inserted.

    Inputs:
        - db_name: a string representing the name of the self to insert the value into
        - collections: a list of strings representing the names of the collections to insert the value into
        - object: a string representing the name of the object to insert the value into
        - value: any type of value to be inserted into the collections and object

    Flow:
        - Open the self using the '_open_db' function
        - For each collection in the list of collections:
            - Check if the collection and object exist in the self
            - Get the count of entries in the collection using the '_count' function
            - If the first entry in the collection exists, append the value to the 'values' key of the object in the collection with a new count value
        - Save the updated self using the '_save_db' function

    Outputs:
        - None

    Additional aspects:
        - The function raises a 'KeyError' if the collection or object does not exist in the self
        - The function uses the '_is_value_in' function to check if the first entry in the collection exists
        - The function uses the 'enumerate' function to get the index of each collection in the list of collections
        - The function raises a 'SaveError' if there is an error while saving the updated self
    """
    pass
```


### UPDATE
To update a single value by its ID, you need to import the *.update_value_by_id* method:

```python
from DBLite3 import update_value_by_id
```

In this method, you must pass the name of the self, the name of the collection, the name of the object and the 
identifier of the value to be replaced, as well as the new value.


```python
def update_value_by_id(db_name: str, collection: str, object: str, id: int, value) -> None:
    """
    Objective:
    The objective of the function is to update a single value in a specific object of a collection in a given self, based on the provided id.
    
    Inputs:
        - db_name: a string representing the name of the self to be modified.
        - collection: a string representing the name of the collection to be modified.
        - object: a string representing the name of the object to be modified.
        - id: an integer representing the id of the value to be modified.
        - value: any type representing the new value to be assigned to the specified id.
    
    Flow:
        - The function calls the _open_db() function to open the self and retrieve its content.
        - The function calls the _get_value_index() function to retrieve the index of the value to be modified.
        - The function updates the value at the retrieved index with the provided new value.
        - The function calls the _save_db() function to save the modified self.
    
    Outputs:
        - None
    
    Additional aspects:
        - The function assumes that the self, collection, object, and value with the provided names and id exist.
        - The function does not handle any errors that may occur during the file operations or the search for the value index.
    """
    pass
```    
To update a few values by their ID, you need to import the *.update_values_by_id* method:

```python
from DBLite3 import update_values_by_id
```

In this method, you must pass the name of the self, the name of the collection, the name of the collection and the identifiers of the values (list) to be replaced, as well as the new 
values (list).


```python
def update_values_by_id(db_name: str, collection: str, object: str, id: list, values: list) -> None:
    """
    Objective:
    The objective of the function is to update multiple values in a specific object of a collection in a given self, based on the provided identifiers.

    Inputs:
    - db_name: a string representing the name of the self to be modified.
    - collection: a string representing the name of the collection to be modified.
    - object: a string representing the name of the object to be modified.
    - id: a list of integers representing the identifiers of the values to be modified.
    - values: a list of the new values to replace the old ones.

    Flow:
    - The function calls the _open_db() function to open the self and retrieve its content.
    - The function iterates over the provided list of identifiers.
    - For each identifier, the function calls the _get_value_index() function to retrieve the index of the value in the specified object of the specified collection in the specified self, based on the provided identifier.
    - The function updates the value at the retrieved index with the corresponding value from the provided list of new values.
    - The function calls the _save_db() function to save the modified self.

    Outputs:
    - None

    Additional aspects:
    - The function assumes that the self, collection, object, and values with the provided names and identifiers exist.
    - The function does not handle any errors that may occur during the file operations or the update of the values.
    """
    pass
```

### ALTER

To change an object in the self, you need to call the *.alter_object* method:

```python
from DBLite3 import alter_object
```
and pass the method name of db, collection name and old and new object name. 


```python
def alter_object(db_name: str, collection: str, object_old: str, object_new: str) -> None:
    """
    Objective:
    The objective of the function is to modify the name of an object in a collection of a given self.

    Inputs:
        - db_name: a string representing the name of the self to be modified.
        - collection: a string representing the name of the collection to be modified.
        - object_old: a string representing the old name of the object to be modified.
        - object_new: a string representing the new name of the object to be modified.
    
    Flow:
        - Open the self using the _open_db function.
        - Modify the name of the object in the collection by creating a new key-value pair with the new name and the value of the old name, and then deleting the old key-value pair.
        - Save the modified self using the _save_db function.

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the object to be modified exists in the collection.
        - The function does not handle any errors that may occur during the self operations.
    """
    pass
```

To change a collection in the self, you need to call the *.alter_collection* method:

```python
from DBLite3 import alter_collection
```
and pass the method name of db and old and new collection name. 


```python
def alter_collection(db_name: str, collection_new: str, collection_old: str) -> None:
    """
    Objective:
    The objective of the function is to modify the name of a collection in a given self by changing the key of the collection in the dictionary object representing the self and saving the modified self back to the file.
    
    Inputs:
        - db_name: a string representing the name of the self to be modified.
        - collection_new: a string representing the new name of the collection to be modified.
        - collection_old: a string representing the old name of the collection to be modified.
    
    Flow:
        - Open the self file with the given name using the _open_db function.
        - Modify the key of the collection in the dictionary object representing the self by adding a new key with the new name and deleting the old key.
        - Save the modified self back to the file using the _save_db function.
    
    Outputs:
        - None
    
    Additional aspects:
        - The function uses the _open_db and _save_db functions from the same module to open and save the self file.
        - The function modifies the dictionary object representing the self in memory and saves it back to the file.
        - The function does not handle any errors that may occur during the file operations.
    """
    pass
```

To change a name of the self, you need to call the *.alter_db* method:

```python
from DBLite3 import alter_db
```
and pass the method old and new names of db.  


```python
def alter_db(db_name_old: str, db_name_new: str) -> None:
    """
    Objective:
    The objective of the 'alter_db' function is to modify the name of a self by renaming the file that contains the data of the self.

    Inputs:
        - db_name_old: a string representing the old name of the self to be modified.
        - db_name_new: a string representing the new name of the self to be modified.

    Flow:
        - The function uses the 'os.rename' method to rename the file that contains the data of the self.
        - The 'src' parameter of the 'os.rename' method is set to the old name of the self with the '.json' extension.
        - The 'dst' parameter of the 'os.rename' method is set to the new name of the self with the '.json' extension.

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the self is stored in a file with the '.json' extension.
        - The function does not check if the old self name exists before renaming it to the new name.
    """
    pass
```

### SELECT

To select all values with indexes from Database use *.select_all_values_with_index* method:
```python
from DBLite3 import select_all_values_with_index
```
and pass the method Database name, collection name and object name.

```python
def select_all_values_with_index(db_name: str, collection: str, object: str) -> list:
    """
    Objective:
    The objective of the function is to retrieve all values of a specific object in a collection from a given self and return them as a list with their corresponding indices.

    Inputs:
        - db_name: a string representing the name of the self to retrieve the data from.
        - collection: a string representing the name of the collection to retrieve the data from.
        - object: a string representing the name of the object to retrieve the data from.

    Flow:
        - Call the _open_db function to retrieve the self dictionary object.
        - Check if the collection and object exist in the self.
        - Return a list of all values of the object with their corresponding indices.

    Outputs:
        - A list of strings representing the values of the object with their corresponding indices.

    Additional aspects:
        - The function raises a ValueError if the self file does not exist.
        - The function raises a KeyError if the collection or object do not exist in the self.
        - The function uses the _open_db function from the same module to retrieve the self dictionary object.
    """
    pass
```

To select all values without indexes from Database use *.select_all_values_without_index* method:
```python
from DBLite3 import select_all_values_without_index
```
and pass the method Database name, collection name and object name.

```python
def select_all_values_without_index(db_name: str, collection: str, object: str) -> list:
    """
    Objective:
    The objective of the function is to retrieve all values of a given object in a collection from a specified self and return them as a list without their indices.

    Inputs:
        - db_name: a string representing the name of the self to retrieve the data from.
        - collection: a string representing the name of the collection to retrieve the data from.
        - object: a string representing the name of the object to retrieve the data from.

    Flow:
        - Call the _open_db function to retrieve the self.
        - Check if the specified collection and object exist in the self.
        - Retrieve all values of the specified object from the collection.
        - Return a list of values without their indices.

    Outputs:
        - A list of values without their indices.

    Additional aspects:
        - The function raises a ValueError if the specified self does not exist.
        - The function raises a KeyError if the specified collection or object does not exist in the self.    """
    pass
```

To get values size from object you need to use *.size* method:
```python
from DBLite3 import size
```
and pass the method Database name, collection name and object name.

```python
def size(db_name: str, collection: str, object: str) -> int:
    """
    Objective:
    The objective of the "size" function is to return the number of elements in a specified object of a specified collection in a specified self.
    
    Inputs:
        - db_name: a string representing the name of the self to count the data from.
        - collection: a string representing the name of the collection to count the data from.
        - object: a string representing the name of the object to count the data from.
    
    Flow:
        - Call the "_open_db" function to open the specified self.
        - Check if the specified collection and object exist in the self.
        - Return the number of elements in the specified object.
    
    Outputs:
        - An integer representing the number of elements in the specified object.
    
    Additional aspects:
        - The function raises a ValueError if the specified collection or object does not exist in the self.
        - The function uses the "_open_db" function to open the self and returns the number of elements in the specified object.
    """
    pass
```

To select all values from collection you need to use *.select_all_values_in_collection* method:

```python
from DBLite3 import select_all_values_in_collection
```
and pass the method self name and collection name.

```python
def select_all_values_in_collection(db_name: str, collection: str) -> dict:
    """
    Objective:
    The objective of the function is to retrieve all values from a specified collection in a given self and return them as a dictionary with object IDs as keys and object values as values.

    Inputs:
        - db_name: a string representing the name of the self to retrieve data from.
        - collection: a string representing the name of the collection to retrieve data from.

    Flow:
        - Check if the input parameters are valid strings.
        - Call the _open_db function to retrieve the self object.
        - Iterate over the objects in the specified collection and create a dictionary with object IDs as keys and object values as values.
        - Return the dictionary.

    Outputs:
        - A dictionary with object IDs as keys and object values as values.

    Additional aspects:
        - The function raises a ValueError if the input parameters are not valid strings.
        - The function raises a ValueError if there is an error retrieving data from the specified collection in the given self.
    """
    pass
```
            

### DROP/DELETE

To drop self, you need to import the *.drop_db* method:

```python
from DBLite3 import drop_db
```

In this method, you must pass the name of the self.


```python
def drop_db(db_name: str) -> None:
    """
    Objective:
    The objective of the drop_db function is to delete a self with a given name. It raises a DropError exception if the self does not exist and deletes the self file if it exists.
    
    Inputs:
        - db_name (str): the name of the self to be dropped.
    
    Flow:
        - The function first checks if the self exists using the _db_exists function.
        - If the self exists, the function deletes the self file using the os.remove method.
        - If the self does not exist, the function raises a DropError exception with a custom error message.
    
    Outputs:
        - None: The function does not return any value.
    
    Additional aspects:
        - The function assumes that the self is stored in a JSON file with the same name as the self name.
        - The function uses os.path.join to construct the file path instead of string concatenation to ensure compatibility across different operating systems.
        - The function raises a ValueError if db_name is not a non-empty string.
    """
    pass
```


To drop collection from self, you need to import the *.drop_db* method:

```python
from DBLite3 import drop_collection
```

In this method, you must pass the name of the self and the name of the collection.

```python
def drop_collection(db_name: str, collection: str) -> None:
    """
    Objective:
    The objective of the 'drop_collection' function is to delete a collection from a self. This function takes in the name of the self and the collection to be deleted as input parameters. If the collection exists in the self, it is deleted and the updated self is saved. If the collection does not exist, a custom 'DropError' exception is raised.
    
    Inputs:
        - db_name: a string representing the name of the self to be modified
        - collection: a string representing the name of the collection to be dropped
    
    Flow:
        - The function first checks if the input parameters 'db_name' and 'collection' are non-empty strings. If either of them is empty, a 'ValueError' exception is raised.
        - The function then opens the self using the '_open_db' function and stores it in the 'DATABASE' variable.
        - The function checks if the collection exists in the self using the '_does_collection_exists' function. If the collection exists, it is deleted from the self using the 'del' keyword.
        - The updated self is then saved using the '_save_db' function.
        - If the collection does not exist in the self, a 'DropError' exception is raised.
    
    Outputs:
        - None
    
    Additional aspects:
        - The function uses the '_open_db', '_does_collection_exists', and '_save_db' functions to open, check, and save the self, respectively.
        - The function raises custom exceptions 'ValueError' and 'DropError' if the input parameters are invalid or the collection does not exist in the self, respectively
    """
    pass
```


To drop object from self, you need to import the *.drop_collection* method from the **drop** module.

```python
from DBLite3 import drop_object
```

In this method, you must pass the name of the self, the name of the collection and the name of the object.


```python
def drop_collection(db_name: str, collection: str, object: str) -> None:
    """
    Objective:
    The objective of the 'drop_object' function is to delete a specified object from a specified collection in a given self. The function checks if the object exists in the collection and raises an error if it does not. If the object exists, it is deleted from the collection, and the modified self is saved.
    
    Inputs:
        - db_name: a string representing the name of the self to be modified
        - collection: a string representing the name of the collection to be modified
        - object: a string representing the name of the object to be dropped
    
    Flow:
        - The function takes in the inputs db_name, collection, and object
        - It checks if the inputs are valid strings and raises a ValueError if any of them are empty or not strings
        - It opens the self using the '_open_db' function and checks if the object exists in the specified collection using the '_object_exists' function
        - If the object exists, it is deleted from the collection using the 'del' keyword
        - The modified self is saved using the '_save_db' function
        - If the object does not exist, a 'DropError' is raised with a custom error message
    
    Outputs:
        - None
    
    Additional aspects:
        - The function raises a 'DropError' if any errors occur during the execution of the function
        - The function modifies the self and saves the modified version, which can result in data loss if used incorrectly
        - The function only deletes objects from a single collection and does not work across multiple collections in the self.
    """
    pass
```

To delete value from object you need to use *.delete_value* method:
```python
from DBLite3 import delete_value
```
and pass the method self name, collection name, object name and value id.

```python
def delete_value(db_name: str, collection: str, object: str, id: int) -> None:
    """
    Objective:
    The objective of the 'delete_value' function is to delete a value from a specific object in a collection of a given self, based on the provided id.
    
    Inputs:
        - db_name: a string representing the name of the self to delete the value from.
        - collection: a string representing the name of the collection to delete the value from.
        - object: a string representing the name of the object to delete the value from.
        - id: an integer representing the id of the value to delete.
        
    Flow:
        - The function calls the '_get_value_index' function to retrieve the index of the value to delete.
        - The function calls the '_open_db' function to open the self and retrieve its content.
        - The function checks if the collection, object, and values exist in the self. If any of them do not exist, it raises a ValueError.
        - The function checks if the index of the value to delete is not None.
        - If the index is not None, the function deletes the value from the list of values in the specified object of the specified collection in the specified self.
        - If the list of values becomes empty, the function sets it to None.
        - The function calls the '_save_db' function to save the updated self.
        
    Outputs:
        - None
    
    Additional aspects:
        - The function raises a DeleteError if any error occurs during the deletion process.
        - The function assumes that the self, collection, object, and value with the provided names and id exist.
        - The function does not handle any errors that may occur during the file operations or the search for the value index.
    """
    pass
```

To delete all values from collection you need to use *.delete_all_values* method:

```python
from DBLite3 import delete_all_values
```
and pass the method self name, collection name and object name.

```python
def delete_all_values(db_name: str, collection: str, object: str) -> None:
    """
    Objective:
    The objective of the 'delete_all_values' function is to delete all values from a specific object in a specific collection of a given self. The function uses the '_open_db' and '_save_db' functions from the same module to open and save the modified self. The function now handles any errors that may occur during the file operations.

    Inputs:
        - db_name: a string representing the name of the self to delete values from.
        - collection: a string representing the name of the collection to delete values from.
        - object: a string representing the name of the object to delete values from.

    Flow:
        - Open the self with the given name using the '_open_db' function.
        - Check if the given collection and object exist in the self.
        - If they exist, set the 'values' key of the object to None.
        - Save the modified self using the '_save_db' function.

    Outputs:
        - None

    Additional aspects:
        - The function raises a 'DeleteError' exception if an error occurs during the deletion operation.
        - The function handles errors that may occur during the file operations.
        - The function modifies the self in place and does not return a new self object.
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
* Using any data encryption library, implement a secure way to work with the self
* Add the ability to select values from all collections and objects together and compare



## Authors

- [@macht1212](https://www.github.com/macht1212) Alexander Nazimov


## License

[MIT](https://github.com/macht1212/LiteDB/blob/0711686a88e82182ed37199da73cea1b7595a75d/LICENSE.txt)


[//]: # (## Lessons Learned)



