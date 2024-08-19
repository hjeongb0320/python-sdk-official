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

from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class ApiV1OrganizationGet200ResponseOrganizationsInner(BaseModel):
    """
    ApiV1OrganizationGet200ResponseOrganizationsInner
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    customer_id: Optional[StrictStr] = Field(default=None, alias="customerId")
    slug: StrictStr = Field(...)
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    auth_enforced: Optional[StrictBool] = Field(default=False, alias="authEnforced")
    scim_enabled: Optional[StrictBool] = Field(default=False, alias="scimEnabled")
    kms_default_key_id: Optional[StrictStr] = Field(default=None, alias="kmsDefaultKeyId")
    kms_encrypted_data_key: Optional[Any] = Field(default=None, alias="kmsEncryptedDataKey")
    __properties = ["id", "name", "customerId", "slug", "createdAt", "updatedAt", "authEnforced", "scimEnabled", "kmsDefaultKeyId", "kmsEncryptedDataKey"]

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
    def from_json(cls, json_str: str) -> ApiV1OrganizationGet200ResponseOrganizationsInner:
        """Create an instance of ApiV1OrganizationGet200ResponseOrganizationsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if customer_id (nullable) is None
        # and __fields_set__ contains the field
        if self.customer_id is None and "customer_id" in self.__fields_set__:
            _dict['customerId'] = None

        # set to None if auth_enforced (nullable) is None
        # and __fields_set__ contains the field
        if self.auth_enforced is None and "auth_enforced" in self.__fields_set__:
            _dict['authEnforced'] = None

        # set to None if scim_enabled (nullable) is None
        # and __fields_set__ contains the field
        if self.scim_enabled is None and "scim_enabled" in self.__fields_set__:
            _dict['scimEnabled'] = None

        # set to None if kms_default_key_id (nullable) is None
        # and __fields_set__ contains the field
        if self.kms_default_key_id is None and "kms_default_key_id" in self.__fields_set__:
            _dict['kmsDefaultKeyId'] = None

        # set to None if kms_encrypted_data_key (nullable) is None
        # and __fields_set__ contains the field
        if self.kms_encrypted_data_key is None and "kms_encrypted_data_key" in self.__fields_set__:
            _dict['kmsEncryptedDataKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1OrganizationGet200ResponseOrganizationsInner:
        """Create an instance of ApiV1OrganizationGet200ResponseOrganizationsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1OrganizationGet200ResponseOrganizationsInner.parse_obj(obj)

        _obj = ApiV1OrganizationGet200ResponseOrganizationsInner.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "customer_id": obj.get("customerId"),
            "slug": obj.get("slug"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "auth_enforced": obj.get("authEnforced") if obj.get("authEnforced") is not None else False,
            "scim_enabled": obj.get("scimEnabled") if obj.get("scimEnabled") is not None else False,
            "kms_default_key_id": obj.get("kmsDefaultKeyId"),
            "kms_encrypted_data_key": obj.get("kmsEncryptedDataKey")
        })
        return _obj

