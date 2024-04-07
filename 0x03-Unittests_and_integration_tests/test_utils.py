#!/usr/bin/env python3
"""
Defines the TestAccessNestedMap class
"""
import unittest
from typing import Dict, Sequence, Union
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """Test case for get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Dict[str, bool]):
        """Tests the get_json function"""
        attrs = {"json.return_value": test_payload}
        with patch(
            "utils.requests.get", return_value=Mock(**attrs)
        ) as request_get:
            self.assertEqual(get_json(test_url), test_payload)
            request_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test case for memoize"""

    def test_memoize(self):
        "Tests the memoize wrapper"

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass, "a_method", return_value=lambda: 42
        ) as a_method_patch:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property(), 42)
            self.assertEqual(test_obj.a_property(), 42)
            a_method_patch.assert_called_once()
