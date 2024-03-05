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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from lib.api.SiteConfiguration.models.lqm_config import LQMConfig
from lib.api.SiteConfiguration.models.vpn_link_configuration import VPNLinkConfiguration
from typing import Optional, Set
from typing_extensions import Self

class WANInterfaceV2N6(BaseModel):
    """
    WANInterfaceV2N6
    """ # noqa: E501
    bfd_mode: StrictStr = Field(description="Allowed values: aggressive - For fast failure detection of links. This mode is the default mode and is recommended by Prisma SD-WAN. non_aggressive - when you want to reduce the amount of probe traffic, or for links that are subjected to high loss or poor quality. ")
    bw_config_mode: StrictStr = Field(description="The bandwidth config mode. ")
    bwc_enabled: Optional[StrictBool] = Field(default=None, description="Bwc Enabled")
    cost: Optional[StrictInt] = Field(default=None, description="Cost value for the site WAN interface should be within range 0-1024. ")
    description: Optional[Any] = Field(default=None, description="The description of the WAN interface config (size max = 256). ")
    id: Optional[StrictStr] = Field(default=None, description="The ID. ")
    label_id: StrictStr = Field(description="The WAN interface label or Circuit label ID. This can be retrieved using the waninterfacelabels API. ")
    link_bw_down: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The circuit downstream capacity in MB. ")
    link_bw_up: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The circuit upstream capacity in MB. ")
    lqm_config: Optional[LQMConfig] = None
    lqm_enabled: Optional[StrictBool] = Field(default=None, description="The link quality monitoring parameters. ")
    name: Optional[StrictStr] = Field(default=None, description="The name of the WAN interface config (size max = 128). ")
    network_id: StrictStr = Field(description="The network ID. ")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An information field that can be added to identify the application. Maximum 10 Unique tags of length 1024 each are allowed. ")
    type: Optional[StrictStr] = Field(default=None, description="Type of WAN. ")
    use_for_application_reachability_probes: Optional[StrictBool] = Field(default=None, description="Indicates if the use for application reachability probe is selected. ")
    use_for_controller_connections: Optional[StrictBool] = Field(default=None, description="Indicates if the use for controller connections is selected.             ")
    vpnlink_configuration: Optional[VPNLinkConfiguration] = None
    __properties: ClassVar[List[str]] = ["bfd_mode", "bw_config_mode", "bwc_enabled", "cost", "description", "id", "label_id", "link_bw_down", "link_bw_up", "lqm_config", "lqm_enabled", "name", "network_id", "tags", "type", "use_for_application_reachability_probes", "use_for_controller_connections", "vpnlink_configuration"]

    @field_validator('bfd_mode')
    def bfd_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['aggressive', 'non_aggressive']):
            raise ValueError("must be one of enum values ('aggressive', 'non_aggressive')")
        return value

    @field_validator('bw_config_mode')
    def bw_config_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['auto', 'manual', 'manual_bwm_disabled']):
            raise ValueError("must be one of enum values ('auto', 'manual', 'manual_bwm_disabled')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PUBLIC_WAN', 'PRIVATE_WAN']):
            raise ValueError("must be one of enum values ('PUBLIC_WAN', 'PRIVATE_WAN')")
        return value

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
        """Create an instance of WANInterfaceV2N6 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of lqm_config
        if self.lqm_config:
            _dict['lqm_config'] = self.lqm_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vpnlink_configuration
        if self.vpnlink_configuration:
            _dict['vpnlink_configuration'] = self.vpnlink_configuration.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WANInterfaceV2N6 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bfd_mode": obj.get("bfd_mode"),
            "bw_config_mode": obj.get("bw_config_mode"),
            "bwc_enabled": obj.get("bwc_enabled"),
            "cost": obj.get("cost"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "label_id": obj.get("label_id"),
            "link_bw_down": obj.get("link_bw_down"),
            "link_bw_up": obj.get("link_bw_up"),
            "lqm_config": LQMConfig.from_dict(obj["lqm_config"]) if obj.get("lqm_config") is not None else None,
            "lqm_enabled": obj.get("lqm_enabled"),
            "name": obj.get("name"),
            "network_id": obj.get("network_id"),
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "use_for_application_reachability_probes": obj.get("use_for_application_reachability_probes"),
            "use_for_controller_connections": obj.get("use_for_controller_connections"),
            "vpnlink_configuration": VPNLinkConfiguration.from_dict(obj["vpnlink_configuration"]) if obj.get("vpnlink_configuration") is not None else None
        })
        return _obj


