#!/usr/bin/env python3
"""
Defines the TestAccessNestedMap class
"""
import unittest
from typing import Dict, Sequence, Union

from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Sequence, expected: Union[Dict, int]
    ) -> None:
        """Tests the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [({}, ("a",), KeyError), ({"a": 1}, ("a", "b"), KeyError)]
    )
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Sequence, error: KeyError
    ) -> None:
        """Tests the access_nested_map function for KeyError cases"""
        with self.assertRaises(error):
            access_nested_map(nested_map, path)
