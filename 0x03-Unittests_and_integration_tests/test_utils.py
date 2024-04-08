#!/usr/bin/env python3
"""
Unit Testing
"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        Test access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """
        Test access_nested_map function for raising KeyError.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json function.
        """
        mock_res = Mock()
        mock_res.json.return_value = test_payload
        with patch('utils.requests.get', return_value=mock_res) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test memoize decorator.
        """
        class TestClass:
            """
            Test class for memoization.
            """
            def a_method(self):
                """
                A method to be memoized.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property that calls a_method.
                """
                return self.a_method()

        mock_test_instance = TestClass()

        with patch.object(mock_test_instance, 'a_method') as mocker:
            test1 = mock_test_instance.a_property
            test2 = mock_test_instance.a_property

            mocker.assert_called_once()


if __name__ == "__main__":
    unittest.main()
