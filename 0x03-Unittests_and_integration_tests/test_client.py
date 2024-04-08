#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock):
        """
        Test _public_repos_url method of GithubOrgClient.
        """
        known_p = {"repos_url": "https://api.github.com/orgs/example/repos"}

        mock.return_value = known_p

        github_client = GithubOrgClient("testing")

        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock
                          ) as mock_public_url_repo:
            mock_public_url_repo.return_value = known_p["repos_url"]
            result = github_client._public_repos_url
            self.assertEqual(result, known_p["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock):
        """
        Method to unit-test GithubOrgClient.public_repos.
        """
        # Define known payload
        known_payload = [{"name": "repo1"}, {"name": "repo2"}]
        # Mock to return known payload
        mock.return_value = known_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked:
            mocked.return_value = "school"
            # Create instance
            githuh_client = GithubOrgClient("test")
            # Call the method
            result = githuh_client.public_repos()

            expected = ["repo1", "repo2"]
            self.assertEqual(result, expected)

            mock.assert_called_once()
            mocked.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test has_license method of GithubOrgClient.
        """
        github_client = GithubOrgClient("test")

        result = github_client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)


@parameterized_class([
    "org_payload", "repos_payload", "expected_repos", "apache2_repos"],
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test class for GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup class method
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            cls.org_payload,
            cls.repos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method of GithubOrgClient.
        """

    def test_public_repos_with_license(self):
        """
        Test public_repos method of GithubOrgClient with license filter.
        """


if __name__ == '__main__':
    unittest.main()
