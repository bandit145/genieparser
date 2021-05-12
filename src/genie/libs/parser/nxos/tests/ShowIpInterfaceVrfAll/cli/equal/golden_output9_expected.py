expected_output = {
    "Vlan300": {
        "interface_status": "protocol-up/link-up/admin-up",
        "iod": 7,
        "vrf": "",
        "ipv4": {
            "10.115.65.2/24": {
                "ip": "10.115.65.2",
                "ip_subnet": "10.115.65.0",
                "prefix_length": "24",
                "route_tag": "0",
                "route_preference": "0",
            },
            "10.115.69.2/24": {
                "ip": "10.115.69.2",
                "ip_subnet": "10.115.69.0",
                "prefix_length": "24",
                "route_tag": "0",
                "route_preference": "0",
                "secondary": True,
            },
            "10.115.72.2/24": {
                "ip": "10.115.72.2",
                "ip_subnet": "10.115.72.0",
                "prefix_length": "24",
                "route_tag": "0",
                "route_preference": "0",
                "secondary": True,
            },
            "10.115.77.2/24": {
                "ip": "10.115.77.2",
                "ip_subnet": "10.115.77.0",
                "prefix_length": "24",
                "route_tag": "0",
                "route_preference": "0",
                "secondary": True,
                "broadcast_address": "255.255.255.255",
            },
            "counters": {
                "unicast_packets_sent": 9853,
                "unicast_packets_received": 3233248,
                "unicast_packets_forwarded": 9422,
                "unicast_packets_originated": 441,
                "unicast_packets_consumed": 9385858,
                "unicast_bytes_sent": 1313118,
                "unicast_bytes_received": 192909900,
                "unicast_bytes_forwarded": 1272720,
                "unicast_bytes_originated": 41238,
                "unicast_bytes_consumed": 498894997,
                "multicast_packets_sent": 0,
                "multicast_packets_received": 10735961,
                "multicast_packets_forwarded": 0,
                "multicast_packets_originated": 0,
                "multicast_packets_consumed": 21471922,
                "multicast_bytes_sent": 0,
                "multicast_bytes_received": 858876880,
                "multicast_bytes_forwarded": 0,
                "multicast_bytes_originated": 0,
                "multicast_bytes_consumed": 858876880,
                "broadcast_packets_sent": 0,
                "broadcast_packets_received": 0,
                "broadcast_packets_forwarded": 0,
                "broadcast_packets_originated": 0,
                "broadcast_packets_consumed": 0,
                "broadcast_bytes_sent": 0,
                "broadcast_bytes_received": 0,
                "broadcast_bytes_forwarded": 0,
                "broadcast_bytes_originated": 0,
                "broadcast_bytes_consumed": 0,
                "labeled_packets_sent": 0,
                "labeled_packets_received": 0,
                "labeled_packets_forwarded": 0,
                "labeled_packets_originated": 0,
                "labeled_packets_consumed": 0,
                "labeled_bytes_sent": 0,
                "labeled_bytes_received": 0,
                "labeled_bytes_forwarded": 0,
                "labeled_bytes_originated": 0,
                "labeled_bytes_consumed": 0,
            },
        },
        "multicast_groups": ["224.0.0.102"],
        "ip_mtu": 1500,
        "proxy_arp": "disabled",
        "local_proxy_arp": "disabled",
        "multicast_routing": "disabled",
        "icmp_redirects": "disabled",
        "directed_broadcast": "disabled",
        "ip_forwarding": "disabled",
        "icmp_unreachable": "disabled",
        "icmp_port_unreachable": "enabled",
        "unicast_reverse_path": "none",
        "load_sharing": "none",
        "int_stat_last_reset": "never",
        "wccp_redirect_outbound": "disabled",
        "wccp_redirect_inbound": "disabled",
        "wccp_redirect_exclude": "disabled",
    }
}