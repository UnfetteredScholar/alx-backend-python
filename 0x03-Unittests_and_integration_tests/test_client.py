#!/usr/bin/env python3
"""
Defines the TestGithubOrgClient class
"""
import unittest
from typing import Dict, Sequence, Union
from unittest.mock import MagicMock, patch

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([("google"), ("abc")])
    def test_org(self, org: str):
        """Test the TestGithubOrgClient.org method"""

        with patch(
            "client.get_json", return_value=lambda: {"org": org}
        ) as json_patch:
            client_obj = GithubOrgClient(org)

            self.assertEqual(client_obj.org(), {"org": org})
            json_patch.assert_called_once_with(
                client_obj.ORG_URL.format(org=org)
            )

    # @parameterized.expand(
    #     [
    #         ("google", {"login": "google"}),
    #         ("abc", {"login": "abc"}),
    #     ]
    # )
    # @patch(
    #     "client.get_json",
    # )
    # def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
    #     """Tests the `org` method."""
    #     mocked_fxn.return_value = MagicMock(return_value=resp)
    #     gh_org_client = GithubOrgClient(org)
    #     self.assertEqual(gh_org_client.org(), resp)
    #     mocked_fxn.assert_called_once_with(
    #         "https://api.github.com/orgs/{}".format(org)
    #     )
