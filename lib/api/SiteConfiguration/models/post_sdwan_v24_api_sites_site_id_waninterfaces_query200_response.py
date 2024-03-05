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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lib.api.SiteConfiguration.models.wan_interface_query import WANInterfaceQuery
from typing import Optional, Set
from typing_extensions import Self

class PostSdwanV24ApiSitesSiteIdWaninterfacesQuery200Response(BaseModel):
    """
    PostSdwanV24ApiSitesSiteIdWaninterfacesQuery200Response
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="The actual count. ")
    deleted_count: Optional[StrictInt] = Field(default=None, description="The deleted number. ")
    deleted_ids: Optional[List[StrictStr]] = Field(default=None, description="The deleted IDs. ")
    description: Optional[Dict[str, Any]] = Field(default=None, description="Description of the query. Max size = 256. ")
    id: Optional[StrictStr] = Field(default=None, description="The ID. ")
    next_query: Optional[Dict[str, Any]] = Field(default=None, description="Details of the next query. ")
    total_count: Optional[StrictInt] = Field(default=None, description="Total number. ")
    items: Optional[List[WANInterfaceQuery]] = None
    __properties: ClassVar[List[str]] = ["count", "deleted_count", "deleted_ids", "description", "id", "next_query", "total_count", "items"]

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
        """Create an instance of PostSdwanV24ApiSitesSiteIdWaninterfacesQuery200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostSdwanV24ApiSitesSiteIdWaninterfacesQuery200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "deleted_count": obj.get("deleted_count"),
            "deleted_ids": obj.get("deleted_ids"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "next_query": obj.get("next_query"),
            "total_count": obj.get("total_count"),
            "items": [WANInterfaceQuery.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj


