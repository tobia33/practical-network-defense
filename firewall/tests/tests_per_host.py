from tests_wrapper import *

webserver = [
    [
        wrap_test_dns,
        wrap_test_internal_servers_network,
        wrap_test_ping_everything,
        # wrap_test_syslog_logserver,
        # wrap_test_log_collector_graylog
    ],
    [
        wrap_test_http_s_WAN,
        wrap_test_ssh_everyone_in_acme,
    ]
]

proxy = [
    [
        wrap_test_dns,
        wrap_test_http_s_WAN,
        wrap_test_internal_servers_network,
        wrap_test_ping_everything,
        # wrap_test_syslog_logserver,
        # wrap_test_log_collector_graylog
    ],
    [
        wrap_test_ssh_everyone_in_acme,
    ]
]

dns_logserver_graylog = [
    [
        wrap_test_dns,
        wrap_test_ping_everything,
        wrap_test_proxy_server
    ],
    [
        wrap_test_ssh_everyone_in_acme,
        wrap_test_http_s_webserver
    ]
]

client_ext_1 = [
    [
        wrap_test_dns,
        wrap_test_ping_everything,
        wrap_test_proxy_server,
        # wrap_test_syslog_logserver,
        # wrap_test_log_collector_graylog
    ],
    [
        wrap_test_ssh_everyone_in_acme,
        wrap_test_internal_servers_network,
        wrap_test_http_s_WAN,
        wrap_test_http_s_webserver

    ]
]

kali = [
    [
        wrap_test_dns,
        wrap_test_ssh_everyone_in_acme,
        wrap_test_internal_servers_network,
        wrap_test_ping_everything,
        wrap_test_proxy_server,
        wrap_test_http_s_WAN,
        wrap_test_http_s_webserver,
    ],
    [
    ]
]

wan = [
    [
        wrap_test_http_s_webserver,
        wrap_test_proxy_server,
        wrap_test_ping_DMZ,
        wrap_test_traceroute_DMZ
    ],
    [
        wrap_test_dns,
        wrap_test_internal_servers_network,
        wrap_test_ping_everything,
        wrap_test_ssh_everyone_in_acme,
        # wrap_test_syslog_logserver,
        # wrap_test_log_collector_graylog
    ]
]

alice = [
    [
        wrap_test_ssh_everyone_in_acme
    ],
    [
    ]
]

bob_charles = [
    [
        wrap_test_ssh_everyone_in_acme_but_internal,
    ],
    [
        wrap_test_internal_servers_network,
        wrap_test_ssh_everyone_in_acme,
    ]
]
