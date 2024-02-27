import http.client
from icecream import ic


class Update:
    """
    Update Site Configuration V4.9
    Source: https://pan.dev/sdwan/api/put-sdwan-v-4-9-api-sites-site-id/
    """

    def __init__(self, siteId: str = None, body: dict[str, any] = None) -> None:
        self.siteId = siteId
        self.body = body or {
            "address": {
                "city": {"req": False, "type": str, "value": None},
                "country": {"req": False, "type": str, "value": None},
                "post_code": {"req": False, "type": str, "value": None},
                "state": {"req": False, "type": str, "value": None},
                "street": {"req": False, "type": str, "value": None},
                "street2": {"req": False, "type": str, "value": None},
            },
            "admin_state": {"req": True, "type": str, "value": None},
            "element_cluster_role": {"req": True, "type": str, "value": None},
            "extended_tags": {
                "req": False,
                "type": list,
                "value": {
                    "type": dict[str, str],
                    "value": {
                        "key": {"type": str, "value": None},
                        "value": {"type": str, "value": None},
                        "value_type": {"type": str, "value": None},
                    },
                },
            },
            "id": {"req": True, "type": str, "value": None},
            "location": {
                "req": False,
                "type": dict[str, float],
                "value": {
                    "latitude": {"req": False, "type": float, "value": None},
                    "longitude": {"req": False, "type": float, "value": None},
                },
            },
            "multicast_peer_group_id": {"req": False, "type": str, "value": None},
            "name": {"req": True, "type": str, "value": None},
            "nat_policysetstack_id": {"req": False, "type": str, "value": None},
            "network_policysetstack_id": {"req": False, "type": str, "value": None},
            "perfmgmt_policysetstack_id": {"req": False, "type": str, "value": None},
            "policy_set_id": {"req": False, "type": str, "value": None},
            "priority_policysetstack_id": {"req": False, "type": str, "value": None},
            "security_policyset_id": {"req": False, "type": str, "value": None},
            "security_policysetstack_id": {"req": False, "type": str, "value": None},
            "service_binding": {"req": False, "type": str, "value": None},
            "tags": {
                "req": False,
                "type": list[str],
                "value": [{"type": str, "value": None}],
            },
            "vrf_context_profile_id": {"req": False, "type": str, "value": None},
        }

    def handle(self):
        """
        Handle the call of method
        """
        conn = http.client.HTTPConnection("api.sase.paloaltonetworks.com")
        payload = self.body
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        conn.request(
            method="PUT",
            url="/sdwan/v4.9/api/sites/" + self.siteId,
            body=payload,
            headers=headers,
        )
        res = conn.getresponse()
        data = res.read()
        return data.decode(encoding="utf-8")


up = Update(siteId="localhost")
# ic(up.body)
