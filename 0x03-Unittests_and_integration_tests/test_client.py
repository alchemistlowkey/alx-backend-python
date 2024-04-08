#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """
        Test org method of GithubOrgClient.
        """
        github_client = GithubOrgClient(org_name)

        result = github_client.org()

        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_json.assert_called_once_with(expected_url)


if __name__ == '__main__':
    unittest.main()
