### webserver tests
the webserver has to reach:
    - dns
    - internal server network
    - ping everything 
    - send syslog to logserver
    - send log collector to graylog

### proxy tests
the proxy has to reach:
    - dns
    - http/s wan
    - internal server network
    - ping everything 
    - send syslog to logserver
    - send log collector to graylog

### dns tests
the dns has to reach:
    - ping everything
    - proxy server

### log server
the log server has to reach:
    - ping everything
    - proxy server

### graylog
the graylog has to reach:
    - ping everything
    - proxy server

### greenbone
the greenbone server has to reach:
    - everyone in acme

### client ext 1
the client ext 1 has to reach:
    - dns
    - ping everything
    - proxy server
    - send syslog to logserver
    - send log collector to graylog

### kali
the kali host has to reach:
    - dns
    - ssh everyone in acme
    - internal server network
    - ping everything
    - proxy server
    - send syslog to logserver
    - send log collector to graylog

### WAN hosts
the hosts in WAN have to reach:
    - http/s in webserver
    - proxy server
    - ping DMZ
    - traceroute DMZ
