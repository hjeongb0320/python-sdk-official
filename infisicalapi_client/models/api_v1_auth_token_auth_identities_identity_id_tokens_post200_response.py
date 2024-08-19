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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response(BaseModel):
    """
    ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response
    """
    access_token: StrictStr = Field(default=..., alias="accessToken")
    expires_in: Union[StrictFloat, StrictInt] = Field(default=..., alias="expiresIn")
    access_token_max_ttl: Union[StrictFloat, StrictInt] = Field(default=..., alias="accessTokenMaxTTL")
    token_type: StrictStr = Field(default=..., alias="tokenType")
    __properties = ["accessToken", "expiresIn", "accessTokenMaxTTL", "tokenType"]

    @validator('token_type')
    def token_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Bearer'):
            raise ValueError("must be one of enum values ('Bearer')")
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
    def from_json(cls, json_str: str) -> ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response:
        """Create an instance of ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response:
        """Create an instance of ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response.parse_obj(obj)

        _obj = ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response.parse_obj({
            "access_token": obj.get("accessToken"),
            "expires_in": obj.get("expiresIn"),
            "access_token_max_ttl": obj.get("accessTokenMaxTTL"),
            "token_type": obj.get("tokenType")
        })
        return _obj

