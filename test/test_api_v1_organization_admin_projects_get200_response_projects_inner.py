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

from infisicalapi_client.models.api_v1_organization_admin_projects_get200_response_projects_inner import ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner  # noqa: E501

class TestApiV1OrganizationAdminProjectsGet200ResponseProjectsInner(unittest.TestCase):
    """ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner:
        """Test ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner`
        """
        model = ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner()  # noqa: E501
        if include_optional:
            return ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner(
                id = '',
                name = '',
                slug = '',
                auto_capitalization = True,
                org_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                version = 1.337,
                upgrade_status = '',
                pit_version_limit = 1.337,
                kms_certificate_key_id = '',
                audit_logs_retention_days = 1.337
            )
        else:
            return ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner(
                id = '',
                name = '',
                slug = '',
                org_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1OrganizationAdminProjectsGet200ResponseProjectsInner(self):
        """Test ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()