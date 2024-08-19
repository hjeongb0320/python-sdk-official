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

from infisicalapi_client.models.api_v1_admin_config_get200_response import ApiV1AdminConfigGet200Response  # noqa: E501

class TestApiV1AdminConfigGet200Response(unittest.TestCase):
    """ApiV1AdminConfigGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AdminConfigGet200Response:
        """Test ApiV1AdminConfigGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AdminConfigGet200Response`
        """
        model = ApiV1AdminConfigGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1AdminConfigGet200Response(
                config = infisicalapi_client.models._api_v1_admin_config_get_200_response_config._api_v1_admin_config_get_200_response_config(
                    id = '', 
                    initialized = True, 
                    allow_sign_up = True, 
                    allowed_sign_up_domain = '', 
                    instance_id = '00000000-0000-0000-0000-000000000000', 
                    trust_saml_emails = True, 
                    trust_ldap_emails = True, 
                    trust_oidc_emails = True, 
                    default_auth_org_id = '', 
                    enabled_login_methods = [
                        ''
                        ], 
                    is_migration_mode_on = True, 
                    default_auth_org_slug = '', 
                    is_secret_scanning_disabled = True, )
            )
        else:
            return ApiV1AdminConfigGet200Response(
                config = infisicalapi_client.models._api_v1_admin_config_get_200_response_config._api_v1_admin_config_get_200_response_config(
                    id = '', 
                    initialized = True, 
                    allow_sign_up = True, 
                    allowed_sign_up_domain = '', 
                    instance_id = '00000000-0000-0000-0000-000000000000', 
                    trust_saml_emails = True, 
                    trust_ldap_emails = True, 
                    trust_oidc_emails = True, 
                    default_auth_org_id = '', 
                    enabled_login_methods = [
                        ''
                        ], 
                    is_migration_mode_on = True, 
                    default_auth_org_slug = '', 
                    is_secret_scanning_disabled = True, ),
        )
        """

    def testApiV1AdminConfigGet200Response(self):
        """Test ApiV1AdminConfigGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()