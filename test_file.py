import unittest
from copy import deepcopy
import file2
from unittest.mock import patch

class TestOfVkinder(unittest.TestCase):

    def setUp(self):
        str1 = "I'm a test string!"

    def test_of_delete_marks(self):
        str1 = "I'm a test string!"
        begin_len = len(str1)
        str2 = file2.delete_marks(str1)
        end_len = len(str2)
        self.assertNotEqual(str1, str2)
        self.assertGreater(begin_len, end_len)

    def test_of_make_string_from_dict(self):
        my_dict = {
            1: 'z',
            2: '&',
            'id': 'should be missed',
            'not_id': '00'
        }
        lst = file2.make_list_from_dict(my_dict)
        lst_len = len(lst)
        self.assertIsNotNone(lst)
        self.assertGreater(lst_len, 0)
        self.assertEqual(lst_len, 3)
        self.assertNotIn('should be missed', lst)

    def test_of_sort_data_dict(self):
        my_dict = {
            4: 13,
            5: 12,
            3: 14,
            1: 15,
            6: 11
        }
        res_list = file2.sort_data_dict(my_dict)
        print(res_list)
        self.assertIsNotNone(res_list)
        self.assertLess(res_list[1], res_list[2])
        self.assertIsNone(res_list[3])