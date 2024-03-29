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

from pydantic import BaseModel, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from lib.api.SiteConfiguration.models.adjustment import Adjustment
from typing import Optional, Set
from typing_extensions import Self

class ClusterEvent(BaseModel):
    """
    ClusterEvent
    """ # noqa: E501
    adjustments: Optional[List[Adjustment]] = Field(default=None, description="Adjustments")
    effective_priority: Optional[StrictInt] = Field(default=None, description="Effective Priority")
    peer_connected: Optional[StrictBool] = Field(default=None, description="Peer Connected")
    time: Optional[StrictInt] = Field(default=None, description="Time")
    __properties: ClassVar[List[str]] = ["adjustments", "effective_priority", "peer_connected", "time"]

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
        """Create an instance of ClusterEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in adjustments (list)
        _items = []
        if self.adjustments:
            for _item in self.adjustments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['adjustments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adjustments": [Adjustment.from_dict(_item) for _item in obj["adjustments"]] if obj.get("adjustments") is not None else None,
            "effective_priority": obj.get("effective_priority"),
            "peer_connected": obj.get("peer_connected"),
            "time": obj.get("time")
        })
        return _obj


