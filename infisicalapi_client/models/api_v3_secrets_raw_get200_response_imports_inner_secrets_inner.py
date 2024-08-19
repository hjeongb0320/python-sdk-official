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


from typing import Any, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner(BaseModel):
    """
    ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner
    """
    id: StrictStr = Field(...)
    id: StrictStr = Field(default=..., alias="_id")
    workspace: StrictStr = Field(...)
    environment: StrictStr = Field(...)
    version: Union[StrictFloat, StrictInt] = Field(...)
    type: StrictStr = Field(...)
    secret_key: StrictStr = Field(default=..., alias="secretKey")
    secret_value: StrictStr = Field(default=..., alias="secretValue")
    secret_comment: StrictStr = Field(default=..., alias="secretComment")
    secret_reminder_note: Optional[StrictStr] = Field(default=None, alias="secretReminderNote")
    secret_reminder_repeat_days: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="secretReminderRepeatDays")
    skip_multiline_encoding: Optional[StrictBool] = Field(default=False, alias="skipMultilineEncoding")
    metadata: Optional[Any] = None
    __properties = ["id", "_id", "workspace", "environment", "version", "type", "secretKey", "secretValue", "secretComment", "secretReminderNote", "secretReminderRepeatDays", "skipMultilineEncoding", "metadata"]

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
    def from_json(cls, json_str: str) -> ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner:
        """Create an instance of ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if secret_reminder_note (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_reminder_note is None and "secret_reminder_note" in self.__fields_set__:
            _dict['secretReminderNote'] = None

        # set to None if secret_reminder_repeat_days (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_reminder_repeat_days is None and "secret_reminder_repeat_days" in self.__fields_set__:
            _dict['secretReminderRepeatDays'] = None

        # set to None if skip_multiline_encoding (nullable) is None
        # and __fields_set__ contains the field
        if self.skip_multiline_encoding is None and "skip_multiline_encoding" in self.__fields_set__:
            _dict['skipMultilineEncoding'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner:
        """Create an instance of ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner.parse_obj(obj)

        _obj = ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner.parse_obj({
            "id": obj.get("id"),
            "id": obj.get("_id"),
            "workspace": obj.get("workspace"),
            "environment": obj.get("environment"),
            "version": obj.get("version"),
            "type": obj.get("type"),
            "secret_key": obj.get("secretKey"),
            "secret_value": obj.get("secretValue"),
            "secret_comment": obj.get("secretComment"),
            "secret_reminder_note": obj.get("secretReminderNote"),
            "secret_reminder_repeat_days": obj.get("secretReminderRepeatDays"),
            "skip_multiline_encoding": obj.get("skipMultilineEncoding") if obj.get("skipMultilineEncoding") is not None else False,
            "metadata": obj.get("metadata")
        })
        return _obj

