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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lib.api.SiteConfiguration.models.cluster_member import ClusterMember
from lib.api.SiteConfiguration.models.switch_over_event import SwitchOverEvent
from typing import Optional, Set
from typing_extensions import Self

class SpokeClusterStatus(BaseModel):
    """
    SpokeClusterStatus
    """ # noqa: E501
    cluster_members: Optional[List[ClusterMember]] = Field(default=None, description="Lists the members of the spoke cluster.  ")
    id: Optional[StrictStr] = Field(default=None, description="The ID of the spoke cluster. ")
    switch_over_events: Optional[List[SwitchOverEvent]] = Field(default=None, description="List the spoke cluster switch over event history. ")
    __properties: ClassVar[List[str]] = ["cluster_members", "id", "switch_over_events"]

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
        """Create an instance of SpokeClusterStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cluster_members (list)
        _items = []
        if self.cluster_members:
            for _item in self.cluster_members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cluster_members'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in switch_over_events (list)
        _items = []
        if self.switch_over_events:
            for _item in self.switch_over_events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['switch_over_events'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpokeClusterStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cluster_members": [ClusterMember.from_dict(_item) for _item in obj["cluster_members"]] if obj.get("cluster_members") is not None else None,
            "id": obj.get("id"),
            "switch_over_events": [SwitchOverEvent.from_dict(_item) for _item in obj["switch_over_events"]] if obj.get("switch_over_events") is not None else None
        })
        return _obj


