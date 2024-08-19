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

from infisicalapi_client.models.api_v1_workspace_workspace_id_audit_logs_get200_response import ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response  # noqa: E501

class TestApiV1WorkspaceWorkspaceIdAuditLogsGet200Response(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response:
        """Test ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response`
        """
        model = ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response(
                audit_logs = [
                    infisicalapi_client.models._api_v1_workspace__workspace_id__audit_logs_get_200_response_audit_logs_inner._api_v1_workspace__workspaceId__audit_logs_get_200_response_auditLogs_inner(
                        id = '', 
                        ip_address = '', 
                        user_agent = '', 
                        user_agent_type = '', 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = '', 
                        project_id = '', 
                        event = infisicalapi_client.models._api_v1_workspace__workspace_id__audit_logs_get_200_response_audit_logs_inner_event._api_v1_workspace__workspaceId__audit_logs_get_200_response_auditLogs_inner_event(
                            type = '', 
                            metadata = null, ), 
                        actor = infisicalapi_client.models._api_v1_workspace__workspace_id__audit_logs_get_200_response_audit_logs_inner_event._api_v1_workspace__workspaceId__audit_logs_get_200_response_auditLogs_inner_event(
                            type = '', 
                            metadata = null, ), )
                    ]
            )
        else:
            return ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response(
                audit_logs = [
                    infisicalapi_client.models._api_v1_workspace__workspace_id__audit_logs_get_200_response_audit_logs_inner._api_v1_workspace__workspaceId__audit_logs_get_200_response_auditLogs_inner(
                        id = '', 
                        ip_address = '', 
                        user_agent = '', 
                        user_agent_type = '', 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = '', 
                        project_id = '', 
                        event = infisicalapi_client.models._api_v1_workspace__workspace_id__audit_logs_get_200_response_audit_logs_inner_event._api_v1_workspace__workspaceId__audit_logs_get_200_response_auditLogs_inner_event(
                            type = '', 
                            metadata = null, ), 
                        actor = infisicalapi_client.models._api_v1_workspace__workspace_id__audit_logs_get_200_response_audit_logs_inner_event._api_v1_workspace__workspaceId__audit_logs_get_200_response_auditLogs_inner_event(
                            type = '', 
                            metadata = null, ), )
                    ],
        )
        """

    def testApiV1WorkspaceWorkspaceIdAuditLogsGet200Response(self):
        """Test ApiV1WorkspaceWorkspaceIdAuditLogsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()