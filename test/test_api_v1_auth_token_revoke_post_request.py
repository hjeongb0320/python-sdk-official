# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from infisicalapi_client.models.api_v1_auth_token_revoke_post_request import ApiV1AuthTokenRevokePostRequest  # noqa: E501

class TestApiV1AuthTokenRevokePostRequest(unittest.TestCase):
    """ApiV1AuthTokenRevokePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuthTokenRevokePostRequest:
        """Test ApiV1AuthTokenRevokePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuthTokenRevokePostRequest`
        """
        model = ApiV1AuthTokenRevokePostRequest()  # noqa: E501
        if include_optional:
            return ApiV1AuthTokenRevokePostRequest(
                access_token = ''
            )
        else:
            return ApiV1AuthTokenRevokePostRequest(
                access_token = '',
        )
        """

    def testApiV1AuthTokenRevokePostRequest(self):
        """Test ApiV1AuthTokenRevokePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()