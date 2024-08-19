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
from pydantic import BaseModel, Field, StrictStr

class ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner(BaseModel):
    """
    ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    slug: StrictStr = Field(...)
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    org_id: StrictStr = Field(default=..., alias="orgId")
    permissions: Optional[Any] = None
    __properties = ["id", "name", "description", "slug", "createdAt", "updatedAt", "orgId", "permissions"]

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
    def from_json(cls, json_str: str) -> ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner:
        """Create an instance of ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if permissions (nullable) is None
        # and __fields_set__ contains the field
        if self.permissions is None and "permissions" in self.__fields_set__:
            _dict['permissions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner:
        """Create an instance of ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner.parse_obj(obj)

        _obj = ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "slug": obj.get("slug"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "org_id": obj.get("orgId"),
            "permissions": obj.get("permissions")
        })
        return _obj

