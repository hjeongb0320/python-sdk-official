# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, conlist, constr, validator
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

APIV1WORKSPACEPROJECTSLUGROLESPOST200RESPONSEROLEPERMISSIONSINNERSUBJECT_ANY_OF_SCHEMAS = ["List[str]", "str"]

class ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInnerSubject(BaseModel):
    """
    ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInnerSubject
    """

    # data type: str
    anyof_schema_1_validator: Optional[constr(strict=True, min_length=1)] = None
    # data type: List[str]
    anyof_schema_2_validator: Optional[conlist(StrictStr)] = None
    if TYPE_CHECKING:
        actual_instance: Union[List[str], str]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(APIV1WORKSPACEPROJECTSLUGROLESPOST200RESPONSEROLEPERMISSIONSINNERSUBJECT_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInnerSubject.construct()
        error_messages = []
        # validate data type: str
        try:
            instance.anyof_schema_1_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[str]
        try:
            instance.anyof_schema_2_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInnerSubject with anyOf schemas: List[str], str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInnerSubject:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInnerSubject:
        """Returns the object represented by the json string"""
        instance = ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInnerSubject.construct()
        error_messages = []
        # deserialize data into str
        try:
            # validation
            instance.anyof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_1_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[str]
        try:
            # validation
            instance.anyof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_2_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInnerSubject with anyOf schemas: List[str], str. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

