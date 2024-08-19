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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator

class ApiV1AdminConfigPatchRequest(BaseModel):
    """
    ApiV1AdminConfigPatchRequest
    """
    allow_sign_up: Optional[StrictBool] = Field(default=None, alias="allowSignUp")
    allowed_sign_up_domain: Optional[StrictStr] = Field(default=None, alias="allowedSignUpDomain")
    trust_saml_emails: Optional[StrictBool] = Field(default=None, alias="trustSamlEmails")
    trust_ldap_emails: Optional[StrictBool] = Field(default=None, alias="trustLdapEmails")
    trust_oidc_emails: Optional[StrictBool] = Field(default=None, alias="trustOidcEmails")
    default_auth_org_id: Optional[StrictStr] = Field(default=None, alias="defaultAuthOrgId")
    enabled_login_methods: Optional[conlist(StrictStr)] = Field(default=None, alias="enabledLoginMethods")
    __properties = ["allowSignUp", "allowedSignUpDomain", "trustSamlEmails", "trustLdapEmails", "trustOidcEmails", "defaultAuthOrgId", "enabledLoginMethods"]

    @validator('enabled_login_methods')
    def enabled_login_methods_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('email', 'google', 'github', 'gitlab', 'saml', 'ldap', 'oidc'):
                raise ValueError("each list item must be one of ('email', 'google', 'github', 'gitlab', 'saml', 'ldap', 'oidc')")
        return value

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
    def from_json(cls, json_str: str) -> ApiV1AdminConfigPatchRequest:
        """Create an instance of ApiV1AdminConfigPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if allowed_sign_up_domain (nullable) is None
        # and __fields_set__ contains the field
        if self.allowed_sign_up_domain is None and "allowed_sign_up_domain" in self.__fields_set__:
            _dict['allowedSignUpDomain'] = None

        # set to None if default_auth_org_id (nullable) is None
        # and __fields_set__ contains the field
        if self.default_auth_org_id is None and "default_auth_org_id" in self.__fields_set__:
            _dict['defaultAuthOrgId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AdminConfigPatchRequest:
        """Create an instance of ApiV1AdminConfigPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AdminConfigPatchRequest.parse_obj(obj)

        _obj = ApiV1AdminConfigPatchRequest.parse_obj({
            "allow_sign_up": obj.get("allowSignUp"),
            "allowed_sign_up_domain": obj.get("allowedSignUpDomain"),
            "trust_saml_emails": obj.get("trustSamlEmails"),
            "trust_ldap_emails": obj.get("trustLdapEmails"),
            "trust_oidc_emails": obj.get("trustOidcEmails"),
            "default_auth_org_id": obj.get("defaultAuthOrgId"),
            "enabled_login_methods": obj.get("enabledLoginMethods")
        })
        return _obj

