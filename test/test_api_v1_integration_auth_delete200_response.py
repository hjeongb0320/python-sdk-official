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

from infisicalapi_client.models.api_v1_integration_auth_delete200_response import ApiV1IntegrationAuthDelete200Response  # noqa: E501

class TestApiV1IntegrationAuthDelete200Response(unittest.TestCase):
    """ApiV1IntegrationAuthDelete200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1IntegrationAuthDelete200Response:
        """Test ApiV1IntegrationAuthDelete200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1IntegrationAuthDelete200Response`
        """
        model = ApiV1IntegrationAuthDelete200Response()  # noqa: E501
        if include_optional:
            return ApiV1IntegrationAuthDelete200Response(
                integration_auth = [
                    infisicalapi_client.models._api_v1_workspace__workspace_id__authorizations_get_200_response_authorizations_inner._api_v1_workspace__workspaceId__authorizations_get_200_response_authorizations_inner(
                        id = '', 
                        project_id = '', 
                        integration = '', 
                        team_id = '', 
                        url = '', 
                        namespace = '', 
                        account_id = '', 
                        metadata = null, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return ApiV1IntegrationAuthDelete200Response(
                integration_auth = [
                    infisicalapi_client.models._api_v1_workspace__workspace_id__authorizations_get_200_response_authorizations_inner._api_v1_workspace__workspaceId__authorizations_get_200_response_authorizations_inner(
                        id = '', 
                        project_id = '', 
                        integration = '', 
                        team_id = '', 
                        url = '', 
                        namespace = '', 
                        account_id = '', 
                        metadata = null, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testApiV1IntegrationAuthDelete200Response(self):
        """Test ApiV1IntegrationAuthDelete200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()