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
from lib.api.SiteConfiguration.models.hub_service_endpoint import HubServiceEndpoint
from typing import Optional, Set
from typing_extensions import Self

class HubServiceEndpointConfig(BaseModel):
    """
    HubServiceEndpointConfig
    """ # noqa: E501
    active_service_endpoints: Optional[List[HubServiceEndpoint]] = Field(default=None, description="The active service endpoints of the site or tenant.           ")
    backup_service_endpoints: Optional[List[HubServiceEndpoint]] = Field(default=None, description="The backup service endpoints of the site or tenant. ")
    id: Optional[StrictStr] = Field(default=None, description="The ID of the Hub. ")
    site_id: StrictStr = Field(description="The ID of the site. ")
    __properties: ClassVar[List[str]] = ["active_service_endpoints", "backup_service_endpoints", "id", "site_id"]

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
        """Create an instance of HubServiceEndpointConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in active_service_endpoints (list)
        _items = []
        if self.active_service_endpoints:
            for _item in self.active_service_endpoints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['active_service_endpoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in backup_service_endpoints (list)
        _items = []
        if self.backup_service_endpoints:
            for _item in self.backup_service_endpoints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['backup_service_endpoints'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HubServiceEndpointConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active_service_endpoints": [HubServiceEndpoint.from_dict(_item) for _item in obj["active_service_endpoints"]] if obj.get("active_service_endpoints") is not None else None,
            "backup_service_endpoints": [HubServiceEndpoint.from_dict(_item) for _item in obj["backup_service_endpoints"]] if obj.get("backup_service_endpoints") is not None else None,
            "id": obj.get("id"),
            "site_id": obj.get("site_id")
        })
        return _obj

