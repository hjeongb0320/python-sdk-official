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

from infisicalapi_client.models.api_v1_secret_approvals_post200_response import ApiV1SecretApprovalsPost200Response  # noqa: E501

class TestApiV1SecretApprovalsPost200Response(unittest.TestCase):
    """ApiV1SecretApprovalsPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretApprovalsPost200Response:
        """Test ApiV1SecretApprovalsPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretApprovalsPost200Response`
        """
        model = ApiV1SecretApprovalsPost200Response()  # noqa: E501
        if include_optional:
            return ApiV1SecretApprovalsPost200Response(
                approval = infisicalapi_client.models._api_v1_secret_approvals_post_200_response_approval._api_v1_secret_approvals_post_200_response_approval(
                    id = '', 
                    name = '', 
                    secret_path = '', 
                    approvals = 1.337, 
                    env_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    enforcement_level = 'hard', 
                    environment = infisicalapi_client.models._api_v1_secret_approvals_get_200_response_approvals_inner_environment._api_v1_secret_approvals_get_200_response_approvals_inner_environment(
                        id = '', 
                        name = '', 
                        slug = '', ), 
                    project_id = '', )
            )
        else:
            return ApiV1SecretApprovalsPost200Response(
                approval = infisicalapi_client.models._api_v1_secret_approvals_post_200_response_approval._api_v1_secret_approvals_post_200_response_approval(
                    id = '', 
                    name = '', 
                    secret_path = '', 
                    approvals = 1.337, 
                    env_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    enforcement_level = 'hard', 
                    environment = infisicalapi_client.models._api_v1_secret_approvals_get_200_response_approvals_inner_environment._api_v1_secret_approvals_get_200_response_approvals_inner_environment(
                        id = '', 
                        name = '', 
                        slug = '', ), 
                    project_id = '', ),
        )
        """

    def testApiV1SecretApprovalsPost200Response(self):
        """Test ApiV1SecretApprovalsPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()