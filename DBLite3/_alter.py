import os

from DBLite3._funcs import _open_db, _save_db
from DBLite3._exceptions import DeleteError, SaveError, AlterError


def alter_object(db_name: str, collection: str, obj_name_old: str, object_name_new: str) -> None:
    """
    Objective:
    The objective of the function is to modify the name of an object in a collection of a given self.

    Inputs:
        - db_name: a string representing the name of the self to be modified.
        - collection: a string representing the name of the collection to be modified.
        - obj_name_old: a string representing the old name of the object to be modified.
        - object_name_new: a string representing the new name of the object to be modified.
    
    Flow:
        - Open the self using the _open_db function.
        - Modify the name of the object in the collection by creating a new key-value pair with the new name and the
          value of the old name, and then deleting the old key-value pair.
        - Save the modified self using the _save_db function.

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the object to be modified exists in the collection.
        - The function does not handle any errors that may occur during the self operations.
    """
    if not isinstance(db_name, str):
        raise ValueError('DB name must be a string!')
    if not isinstance(collection, str):
        raise ValueError('Collection name must be a string!')
    if not isinstance(obj_name_old, str):
        raise ValueError('Object name must be a string!')
    if not isinstance(obj_name_old, str):
        raise ValueError('Object name must be a string!')

    try:
        DATABASE = _open_db(db_name=db_name)
    except FileNotFoundError as f:
        raise FileNotFoundError('Database does not exist!')
    
    if collection not in DATABASE:
        raise KeyError(f'{collection} does not exist in {db_name}')
    
    if obj_name_old not in DATABASE[collection]:
        raise KeyError(f'{obj_name_old} does not exist in {collection}')
    if object_name_new in DATABASE[collection]:
        raise KeyError(f'{object_name_new} hsa already existed in {collection}')
    
    try:
        DATABASE[collection][object_name_new] = DATABASE[collection][obj_name_old]
        del DATABASE[collection][obj_name_old]
        _save_db(db_name=db_name, DB=DATABASE)
    except (DeleteError, SaveError) as e:
        print(f'Error deleting/saving object: {e}')


def alter_collection(db_name: str, collection_new: str, collection_old: str) -> None:
    """
    Objective:
    The objective of the function is to modify the name of a collection in a given self by changing the key of the
    collection in the dictionary object representing the self and saving the modified self back to the file.
    
    Inputs:
        - db_name: a string representing the name of the self to be modified.
        - collection_new: a string representing the new name of the collection to be modified.
        - collection_old: a string representing the old name of the collection to be modified.
    
    Flow:
        - Open the self file with the given name using the _open_db function.
        - Modify the key of the collection in the dictionary object representing the self by adding a new key with
          the new name and deleting the old key.
        - Save the modified self back to the file using the _save_db function.
    
    Outputs:
        - None
    
    Additional aspects:
        - The function uses the _open_db and _save_db functions from the same module to open and save the self file.
        - The function modifies the dictionary object representing the self in memory and saves it back to the file.
        - The function does not handle any errors that may occur during the file operations.
    """
    if not isinstance(db_name, str):
        raise ValueError('DB name must be a string!')
    if not isinstance(collection_old, str):
        raise ValueError('Collection name must be a string!')
    if not isinstance(collection_new, str):
        raise ValueError('Collection name must be a string!')

    try:
        DATABASE = _open_db(db_name=db_name)
    except FileNotFoundError as f:
        raise FileNotFoundError('Database does not exist!')
    
    if collection_old not in DATABASE:
        raise KeyError(f'{collection_old} does not exist in the self')
    
    if collection_new in DATABASE:
        raise KeyError('Collection already exists in the self')
    
    try:
        DATABASE[collection_new] = DATABASE.pop(collection_old)
        _save_db(db_name=db_name, DB=DATABASE)
    except AlterError as e:
        raise AlterError(f'Error altering collection: {e}')


def alter_db(db_name_old: str, db_name_new: str) -> None:
    """
    Objective:
    The objective of the 'alter_db' function is to modify the name of a self by renaming the file that contains the
    data of the self.

    Inputs:
        - db_name_old: a string representing the old name of the self to be modified.
        - db_name_new: a string representing the new name of the self to be modified.

    Flow:
        - The function uses the 'os.rename' method to rename the file that contains the data of the self.
        - The 'src' parameter of the 'os.rename' method is set to the old name of the self with the '.json'
          extension.
        - The 'dst' parameter of the 'os.rename' method is set to the new name of the self with the '.json'
          extension.

    Outputs:
        - None

    Additional aspects:
        - The function assumes that the self is stored in a file with the '.json' extension.
        - The function does not check if the old self name exists before renaming it to the new name.
    """
    if not isinstance(db_name_old, str):
        raise ValueError('DB name must be a string!')
    if not isinstance(db_name_new, str):
        raise ValueError('DB name must be a string!')

    if os.path.exists(os.path.join(db_name_old + '.json')):
        os.rename(src=os.path.join(db_name_old + '.json'), dst=os.path.join(db_name_new + '.json'))
    else:
        raise FileNotFoundError(f'{db_name_old}.json does not exist')
