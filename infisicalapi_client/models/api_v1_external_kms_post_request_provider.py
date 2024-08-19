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



from pydantic import BaseModel, Field, StrictStr, validator
from infisicalapi_client.models.api_v1_external_kms_post_request_provider_inputs import ApiV1ExternalKmsPostRequestProviderInputs

class ApiV1ExternalKmsPostRequestProvider(BaseModel):
    """
    ApiV1ExternalKmsPostRequestProvider
    """
    type: StrictStr = Field(...)
    inputs: ApiV1ExternalKmsPostRequestProviderInputs = Field(...)
    __properties = ["type", "inputs"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('aws'):
            raise ValueError("must be one of enum values ('aws')")
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
    def from_json(cls, json_str: str) -> ApiV1ExternalKmsPostRequestProvider:
        """Create an instance of ApiV1ExternalKmsPostRequestProvider from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of inputs
        if self.inputs:
            _dict['inputs'] = self.inputs.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1ExternalKmsPostRequestProvider:
        """Create an instance of ApiV1ExternalKmsPostRequestProvider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1ExternalKmsPostRequestProvider.parse_obj(obj)

        _obj = ApiV1ExternalKmsPostRequestProvider.parse_obj({
            "type": obj.get("type"),
            "inputs": ApiV1ExternalKmsPostRequestProviderInputs.from_dict(obj.get("inputs")) if obj.get("inputs") is not None else None
        })
        return _obj

