from LiteDB.create import create_db, create_collection
from LiteDB.insert import insert_one, insert_many
from LiteDB.update import update_value_by_id, update_values_by_id
from LiteDB.drop import drop_db, drop_collection, drop_object
from LiteDB.alter import alter_object, alter_collection
from LiteDB.delete import delete_value, delete_all_values
from LiteDB.select import size, select_first_five_elements, select_all_values_without_index, \
    select_all_values_with_index, select_all_values_in_collection, gt, lt


# LiteDB is NoSQL database.
# LiteDB could be used as simple DB for simple projects.
# This DB creates file with file extension .json (JavaScript Object Notification).
#
# All information is stored in tables which contain collections.


__version__ = '0.1.0'
__author__ = "Alexander Nazimov (GitHub @macht1212)"
