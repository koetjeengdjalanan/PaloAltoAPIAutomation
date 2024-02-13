import http.client


class Update:
    """
    Update Site Configuration V4.9
    Source: https://pan.dev/sdwan/api/put-sdwan-v-4-9-api-sites-site-id/
    """

    def __init__(self, siteid: str, body: dict[str, any] = None) -> None:
        self.siteid = siteid
        self.body = body or {
            "address": {
                "city": "",
                "country": "",
                "post_code": "",
                "state": "",
                "street": "",
                "street2": "",
            },
            "admin_state": "",
            "element_cluster_role": "",
            "extended_tags": [{"key": "", "value": "", "value_type": ""}],
            "id": "",
            "location": {"latitude": 0, "longitude": 0},
            "multicast_peer_group_id": "",
            "name": "",
            "nat_policysetstack_id": "",
            "network_policysetstack_id": "",
            "perfmgmt_policysetstack_id": "",
            "policy_set_id": "",
            "priority_policysetstack_id": "",
            "security_policyset_id": "",
            "security_policysetstack_id": "",
            "service_binding": "",
            "tags": [""],
            "vrf_context_profile_id": "",
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
            url="/sdwan/v4.9/api/sites/" + self.siteid,
            body=payload,
            headers=headers,
        )
        res = conn.getresponse()
        data = res.read()
        return data.decode(encoding="utf-8")

    pass
