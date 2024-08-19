# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_secret_approvals_get200_response_approvals_inner_environment import ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment

class ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner(BaseModel):
    """
    ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner
    """
    id: StrictStr = Field(...)
    ldap_config_id: StrictStr = Field(default=..., alias="ldapConfigId")
    ldap_group_cn: StrictStr = Field(default=..., alias="ldapGroupCN")
    group: ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment = Field(...)
    __properties = ["id", "ldapConfigId", "ldapGroupCN", "group"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner:
        """Create an instance of ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner:
        """Create an instance of ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner.parse_obj(obj)

        _obj = ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner.parse_obj({
            "id": obj.get("id"),
            "ldap_config_id": obj.get("ldapConfigId"),
            "ldap_group_cn": obj.get("ldapGroupCN"),
            "group": ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment.from_dict(obj.get("group")) if obj.get("group") is not None else None
        })
        return _obj

