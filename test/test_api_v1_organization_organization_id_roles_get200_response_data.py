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

from infisicalapi_client.models.api_v1_organization_organization_id_roles_get200_response_data import ApiV1OrganizationOrganizationIdRolesGet200ResponseData  # noqa: E501

class TestApiV1OrganizationOrganizationIdRolesGet200ResponseData(unittest.TestCase):
    """ApiV1OrganizationOrganizationIdRolesGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1OrganizationOrganizationIdRolesGet200ResponseData:
        """Test ApiV1OrganizationOrganizationIdRolesGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1OrganizationOrganizationIdRolesGet200ResponseData`
        """
        model = ApiV1OrganizationOrganizationIdRolesGet200ResponseData()  # noqa: E501
        if include_optional:
            return ApiV1OrganizationOrganizationIdRolesGet200ResponseData(
                roles = [
                    infisicalapi_client.models._api_v1_organization__organization_id__roles_get_200_response_data_roles_inner._api_v1_organization__organizationId__roles_get_200_response_data_roles_inner(
                        id = '', 
                        name = '', 
                        description = '', 
                        slug = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = '', 
                        permissions = null, )
                    ]
            )
        else:
            return ApiV1OrganizationOrganizationIdRolesGet200ResponseData(
                roles = [
                    infisicalapi_client.models._api_v1_organization__organization_id__roles_get_200_response_data_roles_inner._api_v1_organization__organizationId__roles_get_200_response_data_roles_inner(
                        id = '', 
                        name = '', 
                        description = '', 
                        slug = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = '', 
                        permissions = null, )
                    ],
        )
        """

    def testApiV1OrganizationOrganizationIdRolesGet200ResponseData(self):
        """Test ApiV1OrganizationOrganizationIdRolesGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()