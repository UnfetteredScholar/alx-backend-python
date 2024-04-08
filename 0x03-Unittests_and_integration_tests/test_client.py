#!/usr/bin/env python3
"""
Defines the TestGithubOrgClient class
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, patch, PropertyMock

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the GithubOrgClient.org method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self):
        """Tests the GithubOrgClient._public_repos_url property"""

        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/amazon/repos",
            }
            self.assertEqual(
                GithubOrgClient("amazon")._public_repos_url,
                "https://api.github.com/users/amazon/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock: MagicMock):
        """Tests the GithubOrgClient.public_repos property"""
        get_json_mock.return_value = [
            {"name": "Amazon"},
            {"name": "Amazon Dev"},
        ]
        client_obj = GithubOrgClient(
            "https://api.github.com/users/amazon/repos"
        )
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_pr_url:
            mock_pr_url.return_value = (
                "https://api.github.com/users/amazon/repos"
            )
            self.assertEqual(
                client_obj.public_repos(), ["Amazon", "Amazon Dev"]
            )
