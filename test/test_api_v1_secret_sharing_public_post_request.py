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

from infisicalapi_client.models.api_v1_secret_sharing_public_post_request import ApiV1SecretSharingPublicPostRequest  # noqa: E501

class TestApiV1SecretSharingPublicPostRequest(unittest.TestCase):
    """ApiV1SecretSharingPublicPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretSharingPublicPostRequest:
        """Test ApiV1SecretSharingPublicPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretSharingPublicPostRequest`
        """
        model = ApiV1SecretSharingPublicPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1SecretSharingPublicPostRequest(
                encrypted_value = '',
                hashed_hex = '',
                iv = '',
                tag = '',
                expires_at = '',
                expires_after_views = 1
            )
        else:
            return ApiV1SecretSharingPublicPostRequest(
                encrypted_value = '',
                hashed_hex = '',
                iv = '',
                tag = '',
                expires_at = '',
        )
        """

    def testApiV1SecretSharingPublicPostRequest(self):
        """Test ApiV1SecretSharingPublicPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()