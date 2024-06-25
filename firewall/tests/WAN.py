from tests import *

hosts_addresses['proxyserver.acme-28.test'] = ('100.100.6.3', '2001:470:b5b8:1c06:74da:b5ff:fed2:952a')

print('[+] Starting the tests:')


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
