import socket
import os

hosts = [
    'webserver.acme-28.test',
    'proxyserver.acme-28.test',

    'dnsserver.acme-28.test',
    'logserver.acme-28.test',
    'greenbone.acme-28.test',
    'graylog.acme-28.test',

    'client-ext-1.acme-28.test',

    'kali.acme-28.test',
]

hosts_addresses = {}

"""
    All tests functions return a boolean or a list [bool, bool],
    The boolean is True if the test is passed
"""

'''
    test if dns is reachable 
    and populates dictionary with hostname and addresses
    returns True if the test is passed
'''
def test_dns():
    for host in hosts:
        try:
            info4  = socket.getaddrinfo(host, 0, family=socket.AF_INET)
            info6  = socket.getaddrinfo(host, 0, family=socket.AF_INET6)
        except:
            return False
        ipv4 = info4[0][4][0]
        ipv6 = info6[0][4][0]
        hosts_addresses[host] = (ipv4, ipv6)
    # print(hosts_addresses, '\n')
    return True

'''
    tests if internal servers network is reachable
'''
def test_internal_servers_network():
    result = [False, False]
    # ipv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex((hosts_addresses['graylog.acme-28.test'][0], 80))
    if res == 0:
        result[0] = True
    # ipv6
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex((hosts_addresses['graylog.acme-28.test'][1], 80))
    if res == 0:
        result[1] = True
    return result

'''
    tests if internal servers network is reachable
'''
def test_ping_everything():
    result = [True, True]
    ipv4_not_working = []
    ipv6_not_working = []
    # test hosts in acme
    for host, addresses in hosts_addresses.items():
        # ipv4
        response = os.system(f"ping {addresses[0]} -c 3 2>&1 >/dev/null")
        if response != 0:
            ipv4_not_working.append(host)
            result[0] = False
        # ipv6
        response = os.system(f"ping -6 {addresses[1]} -c 3 2>&1 >/dev/null")
        if response != 0:
            ipv6_not_working.append(host)
            result[1] = False
    # test host in wan
    # ipv4
    response = os.system(f"ping 8.8.8.8 -c 3 2>&1 >/dev/null")
    if response != 0:
        ipv4_not_working.append('8.8.8.8')
        result[0] = False
    # ipv6
    response = os.system(f"ping -6 2a00:1450:4007:80c::2004 -c 3 2>&1 >/dev/null")
    if response != 0:
        ipv6_not_working.append('2a00:1450:4007:80c::2004')
        result[1] = False
    return result, ipv4_not_working, ipv6_not_working


'''
    tests if http/s services in WAN are reachable
'''
def test_http_s_WAN():
    resultv4 = [False, False]
    resultv6 = [False, False]
    # ipv4 http
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex(('100.101.0.5', 80))
    if res == 0:
        resultv4[0] = True
    # ipv4 https
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex(('100.101.0.5', 443))
    if res == 0:
        resultv4[1] = True
    # ipv6 http
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex(('2a00:1450:4007:80c::2004', 80))
    if res == 0:
        resultv6[0] = True
    # ipv6 http
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex(('2a00:1450:4007:80c::2004', 443))
    if res == 0:
        resultv6[1] = True
    return resultv4, resultv6

'''
    tests if proxy server is reachable
'''
def test_proxy_server():
    result = [False, False]
    # ipv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex((hosts_addresses['proxyserver.acme-28.test'][0], 80))
    if res == 0:
        result[0] = True
    # ipv6
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex((hosts_addresses['proxyserver.acme-28.test'][1], 80))
    if res == 0:
        result[1] = True
    return result

# def test_everyone_in_acme    # GREENBONE TEST, NOT CLEAR

def test_ssh_everyone_in_acme():
    result = [True, True]
    # test hosts in acme
    ipv4_not_working = []
    ipv6_not_working = []

    for host, addresses in hosts_addresses.items():
        # ipv4
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        res = sock.connect_ex((addresses[0], 22))
        if res != 0:
            ipv4_not_working.append(host)
            result[0] = False
        # ipv6
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sock.settimeout(10)
        res = sock.connect_ex((addresses[1], 22))
        if res != 0:
            ipv6_not_working.append(host)
            result[1] = False
    return result, ipv4_not_working, ipv6_not_working

def test_http_s_webserver():
    resultv4 = [False, False]
    resultv6 = [False, False]
    # ipv4 http
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex(('100.100.6.2', 80))
    if res == 0:
        resultv4[0] = True
    # ipv4 https
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex(('100.100.6.2', 443))
    if res == 0:
        resultv4[1] = True

    # ipv6 http
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex(('2001:470:b5b8:1c06:40fa:57ff:fe4a:2073', 80))
    if res == 0:
        resultv6[0] = True
    # ipv6 https
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.settimeout(10)
    res = sock.connect_ex(('2001:470:b5b8:1c06:40fa:57ff:fe4a:2073', 443))
    if res == 0:
        resultv6[1] = True
    return resultv4, resultv6

def test_ping_DMZ():
    result = [False, False]
    # ipv4
    response = os.system(f"ping 100.100.6.2 -c 3 2>&1 >/dev/null")
    if response == 0:
        result[0] = True
    # ipv6
    response = os.system(f"ping -6 2001:470:b5b8:1c06:40fa:57ff:fe4a:2073 -c 3 2>&1 >/dev/null")
    if response == 0:
        result[1] = True
    return result

def test_traceroute_DMZ():
    result = [False, False]
    # ipv4
    response = os.popen(f"traceroute -I 100.100.6.2 | wc -l")
    response = response.buffer.read().strip()
    if response < b'5':
        result[0] = True
    # ipv6
    response = os.popen(f"traceroute -I -6 2001:470:b5b8:1c06:40fa:57ff:fe4a:2073 | wc -l")
    
    response = response.buffer.read().strip()
    if response < b'25':
        result[1] = True
    return result

def test_syslog_logserver():
    result = [False, False]
    # ipv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    res = sock.connect_ex((hosts_addresses['logserver.acme-28.test'][0], 514))
    if res == 0:
        result[0] = True
    # ipv6
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.settimeout(10)
    res = sock.connect_ex((hosts_addresses['logserver.acme-28.test'][1], 514))
    if res == 0:
        result[1] = True
    return result

def test_log_collector_graylog():
    result = [False, False]
    # ipv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    res = sock.connect_ex((hosts_addresses['graylog.acme-28.test'][0], 514))
    if res == 0:
        result[0] = True
    # ipv6
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.settimeout(10)
    res = sock.connect_ex((hosts_addresses['graylog.acme-28.test'][1], 514))
    if res == 0:
        result[1] = True
    return result