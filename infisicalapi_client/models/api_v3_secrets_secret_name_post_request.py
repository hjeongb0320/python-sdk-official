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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class ApiV3SecretsSecretNamePostRequest(BaseModel):
    """
    ApiV3SecretsSecretNamePostRequest
    """
    workspace_id: StrictStr = Field(default=..., alias="workspaceId")
    environment: StrictStr = Field(...)
    type: Optional[StrictStr] = 'shared'
    secret_path: Optional[StrictStr] = Field(default='/', alias="secretPath")
    secret_key_ciphertext: StrictStr = Field(default=..., alias="secretKeyCiphertext")
    secret_key_iv: StrictStr = Field(default=..., alias="secretKeyIV")
    secret_key_tag: StrictStr = Field(default=..., alias="secretKeyTag")
    secret_value_ciphertext: StrictStr = Field(default=..., alias="secretValueCiphertext")
    secret_value_iv: StrictStr = Field(default=..., alias="secretValueIV")
    secret_value_tag: StrictStr = Field(default=..., alias="secretValueTag")
    secret_comment_ciphertext: Optional[StrictStr] = Field(default=None, alias="secretCommentCiphertext")
    secret_comment_iv: Optional[StrictStr] = Field(default=None, alias="secretCommentIV")
    secret_comment_tag: Optional[StrictStr] = Field(default=None, alias="secretCommentTag")
    metadata: Optional[Dict[str, StrictStr]] = None
    skip_multiline_encoding: Optional[StrictBool] = Field(default=None, alias="skipMultilineEncoding")
    __properties = ["workspaceId", "environment", "type", "secretPath", "secretKeyCiphertext", "secretKeyIV", "secretKeyTag", "secretValueCiphertext", "secretValueIV", "secretValueTag", "secretCommentCiphertext", "secretCommentIV", "secretCommentTag", "metadata", "skipMultilineEncoding"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('shared', 'personal'):
            raise ValueError("must be one of enum values ('shared', 'personal')")
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
    def from_json(cls, json_str: str) -> ApiV3SecretsSecretNamePostRequest:
        """Create an instance of ApiV3SecretsSecretNamePostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV3SecretsSecretNamePostRequest:
        """Create an instance of ApiV3SecretsSecretNamePostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV3SecretsSecretNamePostRequest.parse_obj(obj)

        _obj = ApiV3SecretsSecretNamePostRequest.parse_obj({
            "workspace_id": obj.get("workspaceId"),
            "environment": obj.get("environment"),
            "type": obj.get("type") if obj.get("type") is not None else 'shared',
            "secret_path": obj.get("secretPath") if obj.get("secretPath") is not None else '/',
            "secret_key_ciphertext": obj.get("secretKeyCiphertext"),
            "secret_key_iv": obj.get("secretKeyIV"),
            "secret_key_tag": obj.get("secretKeyTag"),
            "secret_value_ciphertext": obj.get("secretValueCiphertext"),
            "secret_value_iv": obj.get("secretValueIV"),
            "secret_value_tag": obj.get("secretValueTag"),
            "secret_comment_ciphertext": obj.get("secretCommentCiphertext"),
            "secret_comment_iv": obj.get("secretCommentIV"),
            "secret_comment_tag": obj.get("secretCommentTag"),
            "metadata": obj.get("metadata"),
            "skip_multiline_encoding": obj.get("skipMultilineEncoding")
        })
        return _obj

