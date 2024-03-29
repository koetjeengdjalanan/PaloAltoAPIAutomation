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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lib.api.SiteConfiguration.models.aggregate import Aggregate
from typing import Optional, Set
from typing_extensions import Self

class SpokeClusterQuery(BaseModel):
    """
    SpokeClusterQuery
    """ # noqa: E501
    aggregate: Optional[Aggregate] = None
    dest_page: Optional[StrictInt] = Field(default=None, description="The destination page. ")
    get_deleted: Optional[StrictBool] = Field(default=None, description="The number clusters deleted for a time frame. ", alias="getDeleted")
    group_by: Optional[List[StrictStr]] = Field(default=None, description="Group By")
    id: Optional[StrictStr] = Field(default=None, description="List the clusters by ID.     ")
    last_query_ts: Optional[StrictInt] = Field(default=None, description="Return the ID of a specified query in the current session. ")
    limit: Optional[StrictInt] = Field(default=None, description="The query limit. ")
    next_query: Optional[Dict[str, Any]] = Field(default=None, description="The  limit. ")
    var_query_params: Optional[Dict[str, Any]] = Field(default=None, alias="query_params")
    retrieved_fields: Optional[List[StrictStr]] = Field(default=None, description="Retrieve information from a field. ")
    retrieved_fields_mask: Optional[StrictBool] = Field(default=None, description="List the fields to query. ")
    sort_params: Optional[Dict[str, Any]] = None
    total_count: Optional[StrictInt] = Field(default=None, description="The total number of query parameters. ")
    __properties: ClassVar[List[str]] = ["aggregate", "dest_page", "getDeleted", "group_by", "id", "last_query_ts", "limit", "next_query", "query_params", "retrieved_fields", "retrieved_fields_mask", "sort_params", "total_count"]

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
        """Create an instance of SpokeClusterQuery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aggregate
        if self.aggregate:
            _dict['aggregate'] = self.aggregate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpokeClusterQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregate": Aggregate.from_dict(obj["aggregate"]) if obj.get("aggregate") is not None else None,
            "dest_page": obj.get("dest_page"),
            "getDeleted": obj.get("getDeleted"),
            "group_by": obj.get("group_by"),
            "id": obj.get("id"),
            "last_query_ts": obj.get("last_query_ts"),
            "limit": obj.get("limit"),
            "next_query": obj.get("next_query"),
            "query_params": obj.get("query_params"),
            "retrieved_fields": obj.get("retrieved_fields"),
            "retrieved_fields_mask": obj.get("retrieved_fields_mask"),
            "sort_params": obj.get("sort_params"),
            "total_count": obj.get("total_count")
        })
        return _obj


