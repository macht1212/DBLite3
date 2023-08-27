import os
import pytest

from DBLite3._funcs import _open_db
from DBLite3 import create_db, create_collection
from DBLite3 import insert_one_in_one_collection
from DBLite3 import (select_values_from_similar_objects_in_collections, select_all_values_in_collection,
                     select_all_values_with_index, select_value_by_id_with_index, select_value_by_id_without_index,
                     size, select_all_values_without_index, gt, lt)


class TestSelectAllValuesWithIndex:
    pass


class TestSelectAllValuesWithoutIndex:
    pass


class TestSize:
    pass


class TestSelectAllValuesInCollectionByIdWithIndex:
    pass


class TestSelectAllValuesInCollectionByIdWithoutIndex:
    pass


class TestGT:
    pass


class TestLT:
    pass


class TestSelectValuesFromSimilarObjectsInCollection:
    pass

