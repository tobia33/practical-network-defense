from tests import *


print('[+] Starting the tests:')


print('\n[+] testing if dns is reachable')
dns_passed = test_dns()
if dns_passed:
    print('[+] dns is reachable')
else:
    print('[-] dns is not reachable')


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


print('\n[+] testing if everithing can be pinged')
ping_passed, ipv4_not_working, ipv6_not_working = test_ping_everything()
if ping_passed[0]:
    print('[+] all the hosts can be pinged through ipv4')
else:
    print('[-] the following hosts can\'t be pinged through ipv4', ipv4_not_working)
if ping_passed[1]:
    print('[+] all the hosts can be pinged through ipv6')
else:
    print('[-] the following hosts can\'t be pinged through ipv6', ipv6_not_working)
