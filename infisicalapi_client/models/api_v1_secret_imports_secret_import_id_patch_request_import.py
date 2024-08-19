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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ApiV1SecretImportsSecretImportIdPatchRequestImport(BaseModel):
    """
    ApiV1SecretImportsSecretImportIdPatchRequestImport
    """
    environment: Optional[StrictStr] = Field(default=None, description="The new environment slug to import from.")
    path: Optional[StrictStr] = Field(default=None, description="The new path to import from.")
    position: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The new position of the secret import. The lowest number will be displayed as the first import.")
    __properties = ["environment", "path", "position"]

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
    def from_json(cls, json_str: str) -> ApiV1SecretImportsSecretImportIdPatchRequestImport:
        """Create an instance of ApiV1SecretImportsSecretImportIdPatchRequestImport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretImportsSecretImportIdPatchRequestImport:
        """Create an instance of ApiV1SecretImportsSecretImportIdPatchRequestImport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretImportsSecretImportIdPatchRequestImport.parse_obj(obj)

        _obj = ApiV1SecretImportsSecretImportIdPatchRequestImport.parse_obj({
            "environment": obj.get("environment"),
            "path": obj.get("path"),
            "position": obj.get("position")
        })
        return _obj

