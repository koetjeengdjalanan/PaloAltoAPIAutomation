# coding: utf-8

"""
    Site Configuration

    List of APIs used to manage your site specific configuration attributes, and HA configuration for both branch and data center sites.

    The version of the OpenAPI document: Latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class HubCluster(BaseModel):
    """
    HubCluster
    """ # noqa: E501
    admin_up: Optional[StrictBool] = Field(default=None, description="The hub cluster admin state. ")
    id: Optional[StrictStr] = Field(default=None, description="The ID. ")
    load_alarm_threshold: Optional[StrictInt] = Field(default=None, description="The load alarm threshold. ")
    name: Optional[StrictStr] = Field(default=None, description="The resource name (Max size = 128). ")
    subscription_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The subscription factor. ")
    __properties: ClassVar[List[str]] = ["admin_up", "id", "load_alarm_threshold", "name", "subscription_factor"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of HubCluster from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HubCluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "admin_up": obj.get("admin_up"),
            "id": obj.get("id"),
            "load_alarm_threshold": obj.get("load_alarm_threshold"),
            "name": obj.get("name"),
            "subscription_factor": obj.get("subscription_factor")
        })
        return _obj

