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

class SpokeClusterQueryFilterResponse(BaseModel):
    """
    SpokeClusterQueryFilterResponse
    """ # noqa: E501
    advertisement_interval: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="List the intervals in which the active device advertises its status to the backup.  ")
    description: Optional[Any] = Field(default=None, description="The cluster description. ")
    id: Optional[StrictStr] = Field(default=None, description="The ID of the site. ")
    name: Optional[StrictStr] = Field(default=None, description="Name of the cluster. ")
    preempt: Optional[StrictBool] = Field(default=None, description="Indicates if preemption is required or not. ")
    site_id: Optional[StrictStr] = Field(default=None, description="Site Id")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Displays the details about the tags or labels applied to the clusters. ")
    __properties: ClassVar[List[str]] = ["advertisement_interval", "description", "id", "name", "preempt", "site_id", "tags"]

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
        """Create an instance of SpokeClusterQueryFilterResponse from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpokeClusterQueryFilterResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "advertisement_interval": obj.get("advertisement_interval"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "preempt": obj.get("preempt"),
            "site_id": obj.get("site_id"),
            "tags": obj.get("tags")
        })
        return _obj


