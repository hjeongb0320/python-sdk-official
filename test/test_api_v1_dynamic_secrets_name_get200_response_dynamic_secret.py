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

from infisicalapi_client.models.api_v1_dynamic_secrets_name_get200_response_dynamic_secret import ApiV1DynamicSecretsNameGet200ResponseDynamicSecret  # noqa: E501

class TestApiV1DynamicSecretsNameGet200ResponseDynamicSecret(unittest.TestCase):
    """ApiV1DynamicSecretsNameGet200ResponseDynamicSecret unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1DynamicSecretsNameGet200ResponseDynamicSecret:
        """Test ApiV1DynamicSecretsNameGet200ResponseDynamicSecret
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1DynamicSecretsNameGet200ResponseDynamicSecret`
        """
        model = ApiV1DynamicSecretsNameGet200ResponseDynamicSecret()  # noqa: E501
        if include_optional:
            return ApiV1DynamicSecretsNameGet200ResponseDynamicSecret(
                id = '',
                name = '',
                version = 1.337,
                type = '',
                default_ttl = '',
                max_ttl = '',
                folder_id = '',
                status = '',
                status_details = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                inputs = None
            )
        else:
            return ApiV1DynamicSecretsNameGet200ResponseDynamicSecret(
                id = '',
                name = '',
                version = 1.337,
                type = '',
                default_ttl = '',
                folder_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1DynamicSecretsNameGet200ResponseDynamicSecret(self):
        """Test ApiV1DynamicSecretsNameGet200ResponseDynamicSecret"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()