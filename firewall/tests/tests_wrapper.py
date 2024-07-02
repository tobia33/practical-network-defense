from tests import *


def wrap_test_dns():
    print('\n[+] testing if dns is reachable')
    dns_passed = test_dns()
    if dns_passed:
        print('[+] dns is reachable')
    else:
        print('[-] dns is not reachable')

def wrap_test_internal_servers_network():
    print('\n[+] testing if internal servers network is reachable')
    isn_passed = test_internal_servers_network()
    if isn_passed[0]:
        print('[+] internal servers network is reachable through ipv4')
    else:
        print('[-] internal servers network is not reachable through ipv4')
    if isn_passed[1]:
        print('[+] internal servers network is reachable through ipv6')
    else:
        print('[-] internal servers network is not reachable through ipv6')

def wrap_test_ping_everything():
    print('\n[+] testing if everything can be pinged')
    ping_passed, ipv4_not_working, ipv6_not_working = test_ping_everything()
    if ping_passed[0]:
        print('[+] all the hosts can be pinged through ipv4')
    else:
        print('[-] the following hosts can\'t be pinged through ipv4', ipv4_not_working)
    if ping_passed[1]:
        print('[+] all the hosts can be pinged through ipv6')
    else:
        print('[-] the following hosts can\'t be pinged through ipv6', ipv6_not_working)

def wrap_test_http_s_WAN():
    print('\n[+] testing if web services on WAN are reachable')
    httpv4_passed, httpv6_passed = test_http_s_WAN()
    if httpv4_passed[0]:
        print('[+] http services on WAN are reachable through ipv4')
    else:
        print('[-] http services on WAN are not reachable through ipv4')
    if httpv4_passed[1]:
        print('[+] https services on WAN are reachable through ipv4')
    else:
        print('[-] https services on WAN are not reachable through ipv4')
    if httpv6_passed[0]:
        print('[+] http services on WAN are reachable through ipv6')
    else:
        print('[-] http services on WAN are not reachable through ipv6')
    if httpv6_passed[1]:
        print('[+] https services on WAN are reachable through ipv6')
    else:
        print('[-] https services on WAN are not reachable through ipv6')

def wrap_test_proxy_server():
    print('\n[+] testing if proxy is reachable')
    proxy_passed = test_proxy_server()
    if proxy_passed[0]:
        print('[+] proxy is reachable through ipv4')
    else:
        print('[-] proxy is not reachable through ipv4')
    if proxy_passed[1]:
        print('[+] proxy is reachable through ipv6')
    else:
        print('[-] proxy is not reachable through ipv6')

def wrap_test_ssh_everyone_in_acme():
    print('\n[+] testing if everyone in acme is reachable through ssh')
    ssh_passed, ipv4_not_working, ipv6_not_working = test_ssh_everyone_in_acme()
    if ssh_passed[0]:
        print('[+] all the hosts can be accessed through ssh with ipv4')
    else:
        print('[-] the following hosts can\'t be accessed through ssh with ipv4', ipv4_not_working)
    if ssh_passed[1]:
        print('[+] all the hosts can be accessed through ssh with ipv6')
    else:
        print('[-] the following hosts can\'t be accessed through ssh with ipv6', ipv6_not_working)

def wrap_test_http_s_webserver():
    print('\n[+] testing if webserver can be reached through http/s')
    httpv4_passed, httpv6_passed = test_http_s_webserver()
    if httpv4_passed[0]:
        print('[+] webserver is reachable with http and ipv4')
    else:
        print('[-] webserver is not reachable with http and ipv4')
    if httpv4_passed[1]:
        print('[+] webserver is reachable with https and ipv4')
    else:
        print('[-] webserver is not reachable with https and ipv4')
    if httpv6_passed[0]:
        print('[+] webserver is reachable with http and ipv6')
    else:
        print('[-] webserver is not reachable with http and ipv6')
    if httpv6_passed[1]:
        print('[+] webserver is reachable with https and ipv6')
    else:
        print('[-] webserver is not reachable with https and ipv6')

def wrap_test_ping_DMZ():
    print('\n[+] testing if dmz can be pinged')
    ping_passed = test_ping_DMZ()
    if ping_passed[0]:
        print('[+] dmz can be pinged with ipv4')
    else:
        print('[-] dmz can\'t be pinged with ipv4')
    if ping_passed[1]:
        print('[+] dmz can be pinged with ipv6')
    else:
        print('[-] dmz can\'t be pinged with ipv6')

def wrap_test_traceroute_DMZ():
    print('\n[+] testing if dmz can be reached with traceroute\n')
    trace_passed = test_traceroute_DMZ()
    if trace_passed[0]:
        print('[+] dmz can be reached with traceroute using ipv4')
    else:
        print('[-] dmz can\'t be reached with traceroute using ipv4')
    if trace_passed[1]:
        print('[+] dmz can be reached with traceroute using ipv6')
    else:
        print('[-] dmz can\'t be reached with traceroute using ipv6')

def wrap_test_syslog_logserver():
    print('\n[+] testing if log server can receive logs with syslog')
    syslog_passed = test_syslog_logserver()
    if syslog_passed[0]:
        print('[+] log server can receive logs with syslog through ipv4')
    else:
        print('[-] log server can\'t receive logs with syslog through ipv4')
    if syslog_passed[1]:
        print('[+] log server can receive logs with syslog through ipv6')
    else:
        print('[-] log server can\'t receive logs with syslog through ipv6')


def wrap_test_log_collector_graylog():
    print('\n[+] testing if graylog can collect logs')
    logcoll_passed = test_log_collector_graylog()
    if logcoll_passed[0]:
        print('[+] graylog can collect logs through ipv4')
    else:
        print('[-] graylog can\'t collect logs through ipv4')
    if logcoll_passed[1]:
        print('[+] graylog can collect logs through ipv6')
    else:
        print('[-] graylog can\'t collect logs through ipv6')
