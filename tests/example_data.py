FW_FACTS = {
    "vendor": "Fortinet",
    "model": "Fortigate Model TBD",
    "uptime": None,
    "hostname": None,
    "fqdn": None,
    "os_version": "v6.0.6 build 272",
    "serial_number": "FWF60D4615007492",
    "interface_list": [
        "any",
        "dmz",
        "wan1",
        "wan2",
        "modem",
        "ssl.root",
        "lan",
        "internal1",
        "internal2",
        "internal3",
        "internal4",
        "internal5",
        "internal6",
        "internal7",
        "internal",
        "VMLAB-UPLINK",
        "AWS-test",
        "virtual-wan-link",
    ],
}
FW_POLICY_RESULT = [
    {
        "q_origin_key": 3,
        "policyid": 3,
        "name": "FW_POLICY01",
        "uuid": "a46cee10-e90c-51e9-a768-a9958694e060",
        "srcintf": [{"q_origin_key": "LAN", "name": "LAN"}],
        "dstintf": [{"q_origin_key": "VPN_ZONE", "name": "VPN_ZONE"}],
        "srcaddr": [
            {"q_origin_key": "GROUP_OBJECT_NETWORKS", "name": "GROUP_OBJECT_NETWORKS"}
        ],
        "dstaddr": [
            {"q_origin_key": "NET_OBJ_192.0.2.0_24", "name": "NET_OBJ_192.0.2.0_24"}
        ],
        "internet-service": "disable",
        "internet-service-id": [],
        "internet-service-custom": [],
        "internet-service-src": "disable",
        "internet-service-src-id": [],
        "internet-service-src-custom": [],
        "rtp-nat": "disable",
        "rtp-addr": [],
        "learning-mode": "disable",
        "action": "accept",
        "send-deny-packet": "disable",
        "firewall-session-dirty": "check-all",
        "status": "enable",
        "schedule": "always",
        "schedule-timeout": "disable",
        "service": [{"q_origin_key": "ALL", "name": "ALL"}],
        "dscp-match": "disable",
        "dscp-negate": "disable",
        "dscp-value": "000000",
        "tcp-session-without-syn": "disable",
        "utm-status": "disable",
        "profile-type": "single",
        "profile-group": "",
        "av-profile": "",
        "webfilter-profile": "",
        "dnsfilter-profile": "",
        "spamfilter-profile": "",
        "dlp-sensor": "",
        "ips-sensor": "",
        "application-list": "",
        "voip-profile": "",
        "icap-profile": "",
        "waf-profile": "",
        "ssh-filter-profile": "",
        "profile-protocol-options": "default",
        "ssl-ssh-profile": "",
        "logtraffic": "all",
        "logtraffic-start": "disable",
        "auto-asic-offload": "enable",
        "np-acceleration": "enable",
        "traffic-shaper": "",
        "traffic-shaper-reverse": "",
        "per-ip-shaper": "",
        "application": [],
        "app-category": [],
        "url-category": [],
        "app-group": [],
        "nat": "disable",
        "permit-any-host": "disable",
        "permit-stun-host": "disable",
        "fixedport": "disable",
        "ippool": "disable",
        "poolname": [],
        "session-ttl": 0,
        "vlan-cos-fwd": 255,
        "vlan-cos-rev": 255,
        "inbound": "disable",
        "outbound": "enable",
        "natinbound": "disable",
        "natoutbound": "disable",
        "wccp": "disable",
        "ntlm": "disable",
        "ntlm-guest": "disable",
        "ntlm-enabled-browsers": [],
        "fsso": "enable",
        "wsso": "enable",
        "rsso": "disable",
        "fsso-agent-for-ntlm": "",
        "groups": [],
        "users": [],
        "devices": [],
        "auth-path": "disable",
        "disclaimer": "disable",
        "vpntunnel": "",
        "natip": "0.0.0.0 0.0.0.0",
        "match-vip": "disable",
        "diffserv-forward": "disable",
        "diffserv-reverse": "disable",
        "diffservcode-forward": "000000",
        "diffservcode-rev": "000000",
        "tcp-mss-sender": 0,
        "tcp-mss-receiver": 0,
        "comments": "Rule Comment 01",
        "label": "",
        "global-label": "",
        "auth-cert": "",
        "auth-redirect-addr": "",
        "redirect-url": "",
        "identity-based-route": "",
        "block-notification": "disable",
        "custom-log-fields": [],
        "replacemsg-override-group": "",
        "srcaddr-negate": "disable",
        "dstaddr-negate": "disable",
        "service-negate": "disable",
        "internet-service-negate": "disable",
        "internet-service-src-negate": "disable",
        "timeout-send-rst": "disable",
        "captive-portal-exempt": "disable",
        "ssl-mirror": "disable",
        "ssl-mirror-intf": [],
        "scan-botnet-connections": "disable",
        "dsri": "disable",
        "radius-mac-auth-bypass": "disable",
        "delay-tcp-npu-session": "disable",
        "vlan-filter": "",
    },
    {
        "q_origin_key": 4,
        "policyid": 4,
        "name": "FW_POLICY02",
        "uuid": "a46eb0ba-e90c-51e9-c57a-0f0d7c3c0b64",
        "srcintf": [{"q_origin_key": "LAN", "name": "LAN"}],
        "dstintf": [{"q_origin_key": "VPN_ZONE", "name": "VPN_ZONE"}],
        "srcaddr": [
            {"q_origin_key": "GROUP_OBJECT_NETWORKS", "name": "GROUP_OBJECT_NETWORKS"}
        ],
        "dstaddr": [
            {"q_origin_key": "NET_OBJ_192.0.2.0_25", "name": "NET_OBJ_192.0.2.0_25"}
        ],
        "internet-service": "disable",
        "internet-service-id": [],
        "internet-service-custom": [],
        "internet-service-src": "disable",
        "internet-service-src-id": [],
        "internet-service-src-custom": [],
        "rtp-nat": "disable",
        "rtp-addr": [],
        "learning-mode": "disable",
        "action": "accept",
        "send-deny-packet": "disable",
        "firewall-session-dirty": "check-all",
        "status": "enable",
        "schedule": "always",
        "schedule-timeout": "disable",
        "service": [{"q_origin_key": "ALL", "name": "ALL"}],
        "dscp-match": "disable",
        "dscp-negate": "disable",
        "dscp-value": "000000",
        "tcp-session-without-syn": "disable",
        "utm-status": "disable",
        "profile-type": "single",
        "profile-group": "",
        "av-profile": "",
        "webfilter-profile": "",
        "dnsfilter-profile": "",
        "spamfilter-profile": "",
        "dlp-sensor": "",
        "ips-sensor": "",
        "application-list": "",
        "voip-profile": "",
        "icap-profile": "",
        "waf-profile": "",
        "ssh-filter-profile": "",
        "profile-protocol-options": "default",
        "ssl-ssh-profile": "",
        "logtraffic": "all",
        "logtraffic-start": "disable",
        "auto-asic-offload": "enable",
        "np-acceleration": "enable",
        "traffic-shaper": "",
        "traffic-shaper-reverse": "",
        "per-ip-shaper": "",
        "application": [],
        "app-category": [],
        "url-category": [],
        "app-group": [],
        "nat": "disable",
        "permit-any-host": "disable",
        "permit-stun-host": "disable",
        "fixedport": "disable",
        "ippool": "disable",
        "poolname": [],
        "session-ttl": 0,
        "vlan-cos-fwd": 255,
        "vlan-cos-rev": 255,
        "inbound": "disable",
        "outbound": "enable",
        "natinbound": "disable",
        "natoutbound": "disable",
        "wccp": "disable",
        "ntlm": "disable",
        "ntlm-guest": "disable",
        "ntlm-enabled-browsers": [],
        "fsso": "enable",
        "wsso": "enable",
        "rsso": "disable",
        "fsso-agent-for-ntlm": "",
        "groups": [],
        "users": [],
        "devices": [],
        "auth-path": "disable",
        "disclaimer": "disable",
        "vpntunnel": "",
        "natip": "0.0.0.0 0.0.0.0",
        "match-vip": "disable",
        "diffserv-forward": "disable",
        "diffserv-reverse": "disable",
        "diffservcode-forward": "000000",
        "diffservcode-rev": "000000",
        "tcp-mss-sender": 0,
        "tcp-mss-receiver": 0,
        "comments": "Rule Comment 02",
        "label": "",
        "global-label": "",
        "auth-cert": "",
        "auth-redirect-addr": "",
        "redirect-url": "",
        "identity-based-route": "",
        "block-notification": "disable",
        "custom-log-fields": [],
        "replacemsg-override-group": "",
        "srcaddr-negate": "disable",
        "dstaddr-negate": "disable",
        "service-negate": "disable",
        "internet-service-negate": "disable",
        "internet-service-src-negate": "disable",
        "timeout-send-rst": "disable",
        "captive-portal-exempt": "disable",
        "ssl-mirror": "disable",
        "ssl-mirror-intf": [],
        "scan-botnet-connections": "disable",
        "dsri": "disable",
        "radius-mac-auth-bypass": "disable",
        "delay-tcp-npu-session": "disable",
        "vlan-filter": "",
    },
]

ACTIVE_VPN_RESULT = [
    {
        "proxyid": [
            {
                "proxy_src": [
                    {
                        "subnet": "0.0.0.0/0.0.0.0",
                        "port": 0,
                        "protocol": 0,
                        "protocol_name": "",
                    }
                ],
                "proxy_dst": [
                    {
                        "subnet": "0.0.0.0/0.0.0.0",
                        "port": 0,
                        "protocol": 0,
                        "protocol_name": "",
                    }
                ],
                "status": "up",
                "p2name": "dc2_hub",
                "p2serial": 1,
                "expire": 326,
                "incoming_bytes": 16260,
                "outgoing_bytes": 62612,
            }
        ],
        "name": "dc2_hub",
        "comments": "",
        "wizard-type": "custom",
        "creation_time": 643816,
        "type": "automatic",
        "incoming_bytes": 3175344,
        "outgoing_bytes": 8175083,
        "rgwy": "192.0.2.202",
    },
    {
        "proxyid": [
            {
                "proxy_src": [
                    {
                        "subnet": "0.0.0.0/0.0.0.0",
                        "port": 0,
                        "protocol": 0,
                        "protocol_name": "",
                    }
                ],
                "proxy_dst": [
                    {
                        "subnet": "0.0.0.0/0.0.0.0",
                        "port": 0,
                        "protocol": 0,
                        "protocol_name": "",
                    }
                ],
                "status": "up",
                "p2name": "dc1_hub",
                "p2serial": 1,
                "expire": 46,
                "incoming_bytes": 16324,
                "outgoing_bytes": 66158,
            }
        ],
        "name": "dc1_hub",
        "comments": "",
        "wizard-type": "custom",
        "creation_time": 643815,
        "type": "automatic",
        "incoming_bytes": 3175178,
        "outgoing_bytes": 8174342,
        "rgwy": "192.0.2.198",
    },
]

# response from API is 'true' and 'false' with no quotes or anything.
# Pandas seems to handle this fine, but for testing, setting true = True and false = False
true = True
false = False
INTERFACE_DETAILS_RESULT = [
    {"name": "any", "valid_in_policy": true, "icon": "fa-square-o"},
    {
        "name": "wan1",
        "real_interface_name": "wan1",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "dynamic_addressing": true,
        "dhcp4_client_count": 0,
        "dhcp6_client_count": 0,
        "role": "wan",
        "estimated_upstream_bandwidth": 0,
        "estimated_downstream_bandwidth": 0,
        "ipv4_addresses": [
            {"ip": "10.110.1.128", "netmask": "255.255.252.0", "cidr_netmask": 22}
        ],
        "mac_address": "e8:1c:ba:4f:d7:4e",
        "link": "up",
        "duplex": "full",
        "speed": 1000,
        "supports_device_id": true,
        "valid_in_policy": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_used": false,
        "is_physical": true,
        "media": "rj45",
        "managed_devices": [],
        "is_ipsecable": true,
        "is_routable": true,
        "tagging": [],
        "type": "physical",
        "icon": "ftnt-interface-rj45-up",
    },
    {
        "name": "wan2",
        "real_interface_name": "wan2",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "dynamic_addressing": true,
        "dhcp4_client_count": 0,
        "dhcp6_client_count": 0,
        "role": "wan",
        "estimated_upstream_bandwidth": 0,
        "estimated_downstream_bandwidth": 0,
        "mac_address": "e8:1c:ba:4f:d7:4f",
        "link": "down",
        "duplex": "half",
        "supports_device_id": true,
        "valid_in_policy": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_used": false,
        "is_physical": true,
        "media": "rj45",
        "managed_devices": [],
        "is_ipsecable": true,
        "is_routable": true,
        "tagging": [],
        "type": "physical",
        "icon": "ftnt-interface-rj45-down",
    },
    {
        "name": "modem",
        "vdom": "root",
        "is_system_interface": true,
        "status": "down",
        "dynamic_addressing": true,
        "role": "undefined",
        "mac_address": "00:00:00:00:00:00",
        "link": "down",
        "duplex": "half",
        "supports_device_id": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_used": false,
        "is_physical": true,
        "media": "rj45",
        "managed_devices": [],
        "is_modem": true,
        "is_modem_hidden": true,
        "tagging": [],
        "type": "physical",
        "icon": "ftnt-interface-rj45-down-disabled",
    },
    {
        "name": "ssl.root",
        "real_interface_name": "ssl.root",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "alias": "SSL VPN interface",
        "dynamic_addressing": false,
        "role": "undefined",
        "mac_address": "00:00:00:00:00:00",
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_used": false,
        "is_sslvpn": true,
        "managed_devices": [],
        "tagging": [],
        "type": "tunnel",
        "icon": "ftnt-vpn-tunnel-up",
    },
    {
        "link": "down",
        "duplex": "half",
        "name": "internal1",
        "type": "physical",
        "is_physical": true,
        "used_by_composite": true,
        "is_hardware_switch_member": true,
        "hardware_switch": "internal",
        "media": "rj45",
        "icon": "ftnt-interface-rj45-down",
    },
    {
        "link": "down",
        "duplex": "half",
        "name": "internal2",
        "type": "physical",
        "is_physical": true,
        "used_by_composite": true,
        "is_hardware_switch_member": true,
        "hardware_switch": "internal",
        "media": "rj45",
        "icon": "ftnt-interface-rj45-down",
    },
    {
        "link": "down",
        "duplex": "half",
        "name": "internal3",
        "type": "physical",
        "is_physical": true,
        "used_by_composite": true,
        "is_hardware_switch_member": true,
        "hardware_switch": "internal",
        "media": "rj45",
        "icon": "ftnt-interface-rj45-down",
    },
    {
        "link": "up",
        "duplex": "full",
        "speed": 1000,
        "name": "internal4",
        "type": "physical",
        "is_physical": true,
        "used_by_composite": true,
        "is_hardware_switch_member": true,
        "hardware_switch": "internal",
        "media": "rj45",
        "icon": "ftnt-interface-rj45-up",
    },
    {
        "link": "up",
        "duplex": "full",
        "speed": 1000,
        "name": "internal5",
        "type": "physical",
        "is_physical": true,
        "used_by_composite": true,
        "is_hardware_switch_member": true,
        "hardware_switch": "internal",
        "media": "rj45",
        "icon": "ftnt-interface-rj45-up",
    },
    {
        "link": "down",
        "duplex": "half",
        "name": "internal6",
        "type": "physical",
        "is_physical": true,
        "used_by_composite": true,
        "is_hardware_switch_member": true,
        "hardware_switch": "internal",
        "media": "rj45",
        "icon": "ftnt-interface-rj45-down",
    },
    {
        "link": "up",
        "duplex": "full",
        "speed": 1000,
        "name": "internal7",
        "type": "physical",
        "is_physical": true,
        "used_by_composite": true,
        "is_hardware_switch_member": true,
        "hardware_switch": "internal",
        "media": "rj45",
        "icon": "ftnt-interface-rj45-up",
    },
    {
        "link": "down",
        "duplex": "half",
        "name": "internal8",
        "type": "physical",
        "is_physical": true,
        "used_by_composite": true,
        "is_hardware_switch_member": true,
        "hardware_switch": "internal",
        "media": "rj45",
        "icon": "ftnt-interface-rj45-down",
    },
    {
        "name": "internal",
        "real_interface_name": "internal",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "dynamic_addressing": false,
        "dhcp4_client_count": 3,
        "dhcp6_client_count": 0,
        "role": "lan",
        "ipv4_addresses": [
            {"ip": "192.168.0.1", "netmask": "255.255.255.0", "cidr_netmask": 24}
        ],
        "mac_address": "e8:1c:ba:4f:d7:57",
        "supports_device_id": true,
        "device_id_enabled": true,
        "valid_in_policy": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_used": false,
        "is_hardware_switch": true,
        "members": [
            "internal1",
            "internal2",
            "internal3",
            "internal4",
            "internal5",
            "internal6",
            "internal7",
            "internal8",
        ],
        "managed_devices": [],
        "is_zone_member": true,
        "zone": "LAN",
        "is_ipsecable": true,
        "is_routable": true,
        "tagging": [],
        "type": "hard-switch",
        "link": "up",
        "icon": "ftnt-switch-up",
    },
    {
        "name": "dc1_hub",
        "real_interface_name": "dc1_hub",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "dynamic_addressing": false,
        "dhcp4_client_count": 0,
        "dhcp6_client_count": 0,
        "role": "undefined",
        "ipv4_addresses": [
            {"ip": "192.0.2.100", "netmask": "255.255.255.255", "cidr_netmask": 32}
        ],
        "mac_address": "00:00:00:00:00:00",
        "valid_in_policy": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_tunnel": true,
        "is_ipsec_static": true,
        "link": "up",
        "is_used": false,
        "managed_devices": [],
        "is_zone_member": true,
        "zone": "vpn",
        "is_routable": true,
        "tagging": [],
        "type": "tunnel",
        "icon": "ftnt-vpn-tunnel-up",
    },
    {
        "name": "dc2_hub",
        "real_interface_name": "dc2_hub",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "dynamic_addressing": false,
        "dhcp4_client_count": 0,
        "dhcp6_client_count": 0,
        "role": "undefined",
        "ipv4_addresses": [
            {"ip": "192.0.2.200", "netmask": "255.255.255.255", "cidr_netmask": 32}
        ],
        "mac_address": "00:00:00:00:00:00",
        "valid_in_policy": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_tunnel": true,
        "is_ipsec_static": true,
        "link": "up",
        "is_used": false,
        "managed_devices": [],
        "is_zone_member": true,
        "zone": "vpn",
        "is_routable": true,
        "tagging": [],
        "type": "tunnel",
        "icon": "ftnt-vpn-tunnel-up",
    },
    {
        "name": "WLAN-TEST-SSID",
        "real_interface_name": "WLAN-TEST-SSID",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "dynamic_addressing": false,
        "description": "test ssid",
        "dhcp4_client_count": 0,
        "dhcp6_client_count": 0,
        "role": "lan",
        "mac_address": "00:ff:0f:ce:8c:26",
        "link": "up",
        "supports_device_id": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_used": false,
        "is_wifi": true,
        "ssid": "WLAN-TEST-SSID",
        "is_local_bridge": true,
        "managed_devices": [],
        "is_ipsecable": true,
        "tagging": [],
        "type": "vap-switch",
        "icon": "fa-wifi-up",
    },
    {
        "name": "LAN",
        "is_zone": true,
        "valid_in_policy": true,
        "supports_device_id": true,
        "members": ["internal"],
        "device_id_enabled": true,
        "tagging": [],
        "type": "zone",
        "link": "up",
        "icon": "fa-zone-up",
    },
    {
        "name": "vpn",
        "is_zone": true,
        "valid_in_policy": true,
        "supports_device_id": true,
        "members": ["dc1_hub", "dc2_hub"],
        "tagging": [],
        "type": "zone",
        "link": "up",
        "icon": "fa-zone-up",
    },
    {
        "name": "virtual-wan-link",
        "is_virtual_wan_link": true,
        "status": "down",
        "role": "wan",
        "type": "virtual-wan",
        "load_balance_mode": "source-ip-based",
        "members": [],
        "sd_wan_settings": [],
        "icon": "ftnt-virtual-wan-link-down-disabled",
        "link": "down",
    },
    {
        "name": "lan",
        "real_interface_name": "lan",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "dynamic_addressing": false,
        "dhcp4_client_count": 14,
        "dhcp6_client_count": 0,
        "role": "lan",
        "ipv4_addresses": [
            {"ip": "192.168.1.1", "netmask": "255.255.255.0", "cidr_netmask": 24}
        ],
        "ipv6_addresses": [{"ip": "2001:db8:A000:82::", "cidr_netmask": 64}],
        "mac_address": "00:00:00:00:00:00",
        "supports_device_id": true,
        "device_id_enabled": true,
        "valid_in_policy": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": true,
        "compliance_enforced": false,
        "is_used": false,
        "is_software_switch": true,
        "members": ["internal"],
        "managed_devices": [],
        "is_ipsecable": true,
        "is_routable": true,
        "tagging": [],
        "type": "switch",
        "link": "up",
        "icon": "ftnt-switch-up",
    },
    {
        "name": "VMLAB-UPLINK",
        "real_interface_name": "VMLAB-UPLINK",
        "vdom": "root",
        "is_system_interface": true,
        "status": "up",
        "dynamic_addressing": false,
        "dhcp4_client_count": 0,
        "dhcp6_client_count": 0,
        "role": "lan",
        "ipv4_addresses": [
            {"ip": "10.200.255.0", "netmask": "255.255.255.254", "cidr_netmask": 31}
        ],
        "mac_address": "00:00:00:00:00:00",
        "supports_device_id": true,
        "valid_in_policy": true,
        "supports_fortitelemetry": true,
        "fortitelemetry": false,
        "compliance_enforced": false,
        "is_vlan": true,
        "vlan_interface": "internal",
        "vlan_id": 2000,
        "is_used": false,
        "managed_devices": [],
        "is_ipsecable": true,
        "is_routable": true,
        "tagging": [],
        "type": "vlan",
        "icon": "ftnt-vlan-up",
    },
]

ROUTE_TABLE_RESULT = [
    {
        "ip_version": 4,
        "type": "static",
        "ip_mask": "0.0.0.0/0",
        "distance": 5,
        "metric": 0,
        "gateway": "10.110.0.1",
        "interface": "wan1",
    },
    {
        "ip_version": 4,
        "type": "bgp",
        "ip_mask": "10.0.0.0/8",
        "distance": 200,
        "metric": 0,
        "gateway": "192.0.2.100",
        "interface": "dc1_hub",
        "is_tunnel_route": true,
        "tunnel_parent": "dc1_hub",
        "install_date": 1570621707,
        "uptime": "8 09:52:00",
    },
]

DETECTED_DEVICES = [
    {
        "mac": "b0:a8:6e:01:61:81",
        "master_mac": "b0:a8:6e:01:61:81",
        "device_type": "Unknown",
        "type": "unknown",
        "device_type_source": "none",
        "device_category": "None",
        "category": "none",
        "ipv4_address": "192.168.1.4",
        "addresses": [
            {"address": "192.168.1.4", "type": "ipv4", "detected_interface": "lan"}
        ],
        "manufacturer": "Juniper Networks",
        "detected_interface": "lan",
        "last_seen": 494,
        "is_online": false,
        "online_status": "offline",
        "is_master_device": true,
        "other_macs": [],
        "other_devices": [],
        "online_interfaces": [],
        "last_seen_interface": "lan",
        "last_seen_mac": "b0:a8:6e:01:61:81",
        "interfaces": [
            {
                "master_detected": true,
                "detected_interface": "lan",
                "mac": "b0:a8:6e:01:61:81",
            }
        ],
    },
    {
        "mac": "78:7b:8a:4e:00:ab",
        "master_mac": "78:7b:8a:4e:00:ab",
        "device_type": "Router/NAT Device",
        "type": "router-nat-device",
        "device_type_source": "ac",
        "device_category": "None",
        "category": "none",
        "addresses": [],
        "manufacturer": "Apple, Inc.",
        "detected_interface": "lan",
        "last_seen": 0,
        "is_online": true,
        "online_status": "online",
        "is_master_device": true,
        "other_macs": [],
        "other_devices": [],
        "online_interfaces": ["lan"],
        "last_seen_interface": "lan",
        "last_seen_mac": "78:7b:8a:4e:00:ab",
        "interfaces": [
            {
                "master_detected": true,
                "detected_interface": "lan",
                "mac": "78:7b:8a:4e:00:ab",
            }
        ],
    },
    {
        "mac": "b0:a8:6e:01:61:83",
        "master_mac": "b0:a8:6e:01:61:83",
        "device_type": "Router/NAT Device",
        "type": "router-nat-device",
        "device_type_source": "lldp",
        "device_category": "None",
        "category": "none",
        "hostname": "WM-OFFICE-EX2200",
        "hostname_source": "lldp",
        "os_name": "Juniper ex2200-c-12",
        "os_version": "v12.3R12.4 build 2016-01-20",
        "os_source": "lldp",
        "addresses": [],
        "manufacturer": "Juniper Networks",
        "detected_interface": "lan",
        "last_seen": 0,
        "is_online": true,
        "online_status": "online",
        "is_master_device": true,
        "other_macs": [],
        "other_devices": [],
        "online_interfaces": ["lan"],
        "last_seen_interface": "lan",
        "last_seen_mac": "b0:a8:6e:01:61:83",
        "interfaces": [
            {
                "master_detected": true,
                "detected_interface": "lan",
                "mac": "b0:a8:6e:01:61:83",
            }
        ],
    },
    {
        "mac": "40:cb:c0:ce:81:83",
        "master_mac": "40:cb:c0:ce:81:83",
        "device_type": "Media Streaming",
        "type": "media-streaming",
        "device_type_source": "http",
        "device_category": "None",
        "category": "none",
        "hostname": "Apple-TV",
        "hostname_source": "dhcp",
        "os_name": "Apple TV",
        "os_version": "iOS modified (Model 12.1)",
        "os_source": "http",
        "ipv4_address": "192.168.1.118",
        "ipv6_address": "2001:db8:0:82:1ce1:e2b1:2b2a:5f65",
        "addresses": [
            {"address": "192.168.1.118", "type": "ipv4", "detected_interface": "lan"},
            {
                "address": "2001:db8:0:82:1ce1:e2b1:2b2a:5f65",
                "type": "ipv6",
                "detected_interface": "lan",
            },
        ],
        "manufacturer": "Apple, Inc.",
        "detected_interface": "lan",
        "last_seen": 104039,
        "is_online": false,
        "online_status": "offline",
        "is_master_device": true,
        "other_macs": [],
        "other_devices": [],
        "online_interfaces": [],
        "last_seen_interface": "lan",
        "last_seen_mac": "40:cb:c0:ce:81:83",
        "interfaces": [
            {
                "master_detected": true,
                "detected_interface": "lan",
                "mac": "40:cb:c0:ce:81:83",
            }
        ],
    },
]

DHCP_LEASES = [
    {
        "ip": "192.168.1.110",
        "mac": "18:b4:30:01:ab:bb",
        "hostname": "02AA01AC081300TM",
        "expire_time": 1573850710,
        "status": "leased",
        "interface": "lan",
        "type": "ipv4",
        "reserved": false,
        "server_mkey": 1,
    },
    {
        "ip": "192.168.1.115",
        "mac": "40:98:ad:d5:7a:5e",
        "hostname": "UserpleWatch",
        "expire_time": 1573848785,
        "status": "leased",
        "interface": "lan",
        "type": "ipv4",
        "reserved": false,
        "server_mkey": 1,
    },
    {
        "ip": "192.168.1.119",
        "mac": "cc:95:d7:51:5c:c6",
        "vci": "Linux 3.4.39.13 armv7l",
        "expire_time": 1573841990,
        "status": "leased",
        "interface": "lan",
        "type": "ipv4",
        "reserved": false,
        "server_mkey": 1,
    },
    {
        "ip": "192.168.1.121",
        "mac": "e4:b2:fb:24:2d:54",
        "hostname": "User-iPhone",
        "expire_time": 1573841663,
        "status": "leased",
        "interface": "lan",
        "type": "ipv4",
        "reserved": false,
        "server_mkey": 1,
    },
]
