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
from lib.api.SiteConfiguration.models.address import Address
from lib.api.SiteConfiguration.models.extended_tag import ExtendedTag
from lib.api.SiteConfiguration.models.location import Location
from typing import Optional, Set
from typing_extensions import Self

class SiteQueryFilterV4N8(BaseModel):
    """
    SiteQueryFilterV4N8
    """ # noqa: E501
    address: Optional[Address] = None
    admin_state: StrictStr = Field(description="The site mode of operation, can be in one of three states: Active - the site is in Control mode and network policy is applied. Monitor - the site is in Analytics mode, no network policy is applied. Disabled: the site is disabled. ")
    description: Optional[Any] = Field(default=None, description="Description for the site (Max size = 1024). ")
    element_cluster_role: StrictStr = Field(description="This attribute describes the type i.e. SPOKE or HUB. ")
    extended_tags: Optional[List[ExtendedTag]] = Field(default=None, description="Extended tags allow operators to add more information into the site object. Current extended tags allow for additional configuration related to Prisma Access and ZScaler to be added.               ")
    id: Optional[StrictStr] = Field(default=None, description="The ID. ")
    location: Optional[Location] = None
    multicast_peer_group_id: Optional[StrictStr] = Field(default=None, description="The multicast peer group ID. ")
    name: StrictStr = Field(description="The site name (Max size = 128). ")
    nat_policysetstack_id: Optional[StrictStr] = Field(default=None, description="ID for the NAT Policyset Stack. Can be retrieved using natpolicysetstack API. ")
    network_policysetstack_id: Optional[StrictStr] = Field(default=None, description="ID for the Path Policyset Stack. Can be retrieved using networkpolicysetstack API. ")
    policy_set_id: Optional[StrictStr] = Field(default=None, description="The ID for the Original Network Policy Set. Can be retrieved using policysets API. ")
    priority_policysetstack_id: Optional[StrictStr] = Field(default=None, description="ID for the QoS Policyset Stack. Can be retrieved using prioritypolicysetstack API. ")
    security_policyset_id: Optional[StrictStr] = Field(default=None, description="Security Policyset Id")
    security_policysetstack_id: Optional[StrictStr] = Field(default=None, description="ID for the Security Policyset Stack. Can be retrieved using ngfwpolicysetstack API. ")
    service_binding: Optional[StrictStr] = Field(default=None, description="Bind a site to a set of domains. Can be retrieved using sericebindingmaps API. ")
    tags: Optional[List[StrictStr]] = Field(default=None, description="A information field that can be added to identify the site. ")
    vrf_context_profile_id: Optional[StrictStr] = Field(default=None, description="The VRF (Virtual Routing and Forwarding) profile ID. ")
    __properties: ClassVar[List[str]] = ["address", "admin_state", "description", "element_cluster_role", "extended_tags", "id", "location", "multicast_peer_group_id", "name", "nat_policysetstack_id", "network_policysetstack_id", "policy_set_id", "priority_policysetstack_id", "security_policyset_id", "security_policysetstack_id", "service_binding", "tags", "vrf_context_profile_id"]

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
        """Create an instance of SiteQueryFilterV4N8 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in extended_tags (list)
        _items = []
        if self.extended_tags:
            for _item in self.extended_tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['extended_tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SiteQueryFilterV4N8 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": Address.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "admin_state": obj.get("admin_state"),
            "description": obj.get("description"),
            "element_cluster_role": obj.get("element_cluster_role"),
            "extended_tags": [ExtendedTag.from_dict(_item) for _item in obj["extended_tags"]] if obj.get("extended_tags") is not None else None,
            "id": obj.get("id"),
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "multicast_peer_group_id": obj.get("multicast_peer_group_id"),
            "name": obj.get("name"),
            "nat_policysetstack_id": obj.get("nat_policysetstack_id"),
            "network_policysetstack_id": obj.get("network_policysetstack_id"),
            "policy_set_id": obj.get("policy_set_id"),
            "priority_policysetstack_id": obj.get("priority_policysetstack_id"),
            "security_policyset_id": obj.get("security_policyset_id"),
            "security_policysetstack_id": obj.get("security_policysetstack_id"),
            "service_binding": obj.get("service_binding"),
            "tags": obj.get("tags"),
            "vrf_context_profile_id": obj.get("vrf_context_profile_id")
        })
        return _obj


