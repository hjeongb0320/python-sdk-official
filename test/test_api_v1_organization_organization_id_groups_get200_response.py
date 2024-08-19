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

from infisicalapi_client.models.api_v1_organization_organization_id_groups_get200_response import ApiV1OrganizationOrganizationIdGroupsGet200Response  # noqa: E501

class TestApiV1OrganizationOrganizationIdGroupsGet200Response(unittest.TestCase):
    """ApiV1OrganizationOrganizationIdGroupsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1OrganizationOrganizationIdGroupsGet200Response:
        """Test ApiV1OrganizationOrganizationIdGroupsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1OrganizationOrganizationIdGroupsGet200Response`
        """
        model = ApiV1OrganizationOrganizationIdGroupsGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1OrganizationOrganizationIdGroupsGet200Response(
                groups = [
                    infisicalapi_client.models._api_v1_organization__organization_id__groups_get_200_response_groups_inner._api_v1_organization__organizationId__groups_get_200_response_groups_inner(
                        id = '', 
                        org_id = '', 
                        name = '', 
                        slug = '', 
                        role = '', 
                        role_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        custom_role = infisicalapi_client.models._api_v1_organization__organization_id__groups_get_200_response_groups_inner_custom_role._api_v1_organization__organizationId__groups_get_200_response_groups_inner_customRole(
                            id = '', 
                            name = '', 
                            slug = '', 
                            permissions = null, 
                            description = '', ), )
                    ]
            )
        else:
            return ApiV1OrganizationOrganizationIdGroupsGet200Response(
                groups = [
                    infisicalapi_client.models._api_v1_organization__organization_id__groups_get_200_response_groups_inner._api_v1_organization__organizationId__groups_get_200_response_groups_inner(
                        id = '', 
                        org_id = '', 
                        name = '', 
                        slug = '', 
                        role = '', 
                        role_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        custom_role = infisicalapi_client.models._api_v1_organization__organization_id__groups_get_200_response_groups_inner_custom_role._api_v1_organization__organizationId__groups_get_200_response_groups_inner_customRole(
                            id = '', 
                            name = '', 
                            slug = '', 
                            permissions = null, 
                            description = '', ), )
                    ],
        )
        """

    def testApiV1OrganizationOrganizationIdGroupsGet200Response(self):
        """Test ApiV1OrganizationOrganizationIdGroupsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()