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

from infisicalapi_client.models.api_v2_service_token_get200_response import ApiV2ServiceTokenGet200Response  # noqa: E501

class TestApiV2ServiceTokenGet200Response(unittest.TestCase):
    """ApiV2ServiceTokenGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2ServiceTokenGet200Response:
        """Test ApiV2ServiceTokenGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2ServiceTokenGet200Response`
        """
        model = ApiV2ServiceTokenGet200Response()  # noqa: E501
        if include_optional:
            return ApiV2ServiceTokenGet200Response(
                id = '',
                name = '',
                scopes = None,
                permissions = [
                    ''
                    ],
                last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                secret_hash = '',
                encrypted_key = '',
                iv = '',
                tag = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                project_id = '',
                workspace = '',
                user = infisicalapi_client.models._api_v2_service_token_get_200_response_user._api_v2_service_token_get_200_response_user(
                    auth_methods = [
                        ''
                        ], 
                    id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    devices = null, 
                    email = '', 
                    first_name = '', 
                    last_name = '', 
                    mfa_methods = [
                        ''
                        ], 
                    __v = 1.337, 
                    _id = '', ),
                id = '',
                v = 1.337
            )
        else:
            return ApiV2ServiceTokenGet200Response(
                id = '',
                name = '',
                permissions = [
                    ''
                    ],
                secret_hash = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                project_id = '',
                workspace = '',
                user = infisicalapi_client.models._api_v2_service_token_get_200_response_user._api_v2_service_token_get_200_response_user(
                    auth_methods = [
                        ''
                        ], 
                    id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    devices = null, 
                    email = '', 
                    first_name = '', 
                    last_name = '', 
                    mfa_methods = [
                        ''
                        ], 
                    __v = 1.337, 
                    _id = '', ),
                id = '',
        )
        """

    def testApiV2ServiceTokenGet200Response(self):
        """Test ApiV2ServiceTokenGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()