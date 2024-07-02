import sys
from tests_per_host import *
from execute_tests import execute_tests

if __name__=='__main__':

    if (len(sys.argv) < 2):
        print('[-] Usage main.py [webserver|proxy|...]')
    
    host = sys.argv[1]
    
    
    if host == 'webserver':
        execute_tests(host, webserver)
    elif host == 'proxy':
        execute_tests(host, proxy)
    elif host == 'dns':
        execute_tests(host, dns_logserver_graylog)
    elif host == 'logserver':
        execute_tests(host, dns_logserver_graylog)
    elif host == 'graylog':
        execute_tests(host, dns_logserver_graylog)
    elif host == 'client_ext_1':
        execute_tests(host, client_ext_1)
    elif host == 'kali':
        execute_tests(host, kali)
    elif host == 'wan':
        hosts_addresses['proxyserver.acme-28.test'] = ('100.100.6.3', '2001:470:b5b8:1c06:74da:b5ff:fed2:952a')
        execute_tests(host, wan)