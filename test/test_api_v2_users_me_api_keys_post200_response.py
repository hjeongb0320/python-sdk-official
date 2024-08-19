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

from infisicalapi_client.models.api_v2_users_me_api_keys_post200_response import ApiV2UsersMeApiKeysPost200Response  # noqa: E501

class TestApiV2UsersMeApiKeysPost200Response(unittest.TestCase):
    """ApiV2UsersMeApiKeysPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2UsersMeApiKeysPost200Response:
        """Test ApiV2UsersMeApiKeysPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2UsersMeApiKeysPost200Response`
        """
        model = ApiV2UsersMeApiKeysPost200Response()  # noqa: E501
        if include_optional:
            return ApiV2UsersMeApiKeysPost200Response(
                api_key = '',
                api_key_data = infisicalapi_client.models._api_v2_users_me_api_keys_get_200_response_inner._api_v2_users_me_api_keys_get_200_response_inner(
                    id = '', 
                    name = '', 
                    last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_id = '', )
            )
        else:
            return ApiV2UsersMeApiKeysPost200Response(
                api_key = '',
                api_key_data = infisicalapi_client.models._api_v2_users_me_api_keys_get_200_response_inner._api_v2_users_me_api_keys_get_200_response_inner(
                    id = '', 
                    name = '', 
                    last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_id = '', ),
        )
        """

    def testApiV2UsersMeApiKeysPost200Response(self):
        """Test ApiV2UsersMeApiKeysPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()